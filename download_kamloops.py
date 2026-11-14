"""Download FIRMS hotspots for the Kamloops area into data/kamloops/.

Run once while online:  python download_kamloops.py
The app then reads the cached CSVs and needs no network or MAP_KEY.

Sources:
- Open yearly Canada CSVs (no key): MODIS 2000+, VIIRS S-NPP 2012+ and
  VIIRS NOAA-20 2018+, clipped to BBOX.
- FIRMS Area API (needs FIRMS_MAP_KEY in .env): every date after the last
  yearly file, plus all of NOAA-21, which has no yearly files. Standard (SP)
  data where it exists, near-real-time (NRT) after that.

Output: one CSV per source and year, with the FIRMS columns unchanged plus a
`source` column. acq_time is zero-padded text (HHMM, UTC). Re-running skips
files already downloaded, except API files for the current year, which are
fetched again because they are still filling in.
"""
import io
import os
import time
from datetime import date, timedelta
from pathlib import Path

import pandas as pd
import requests
from dotenv import load_dotenv

# Kamloops and the surrounding Thompson-Okanagan: west, south, east, north (degrees).
BBOX = (-122.5, 49.0, -118.0, 52.5)
OUT_DIR = Path(__file__).parent / "data" / "kamloops"
FIRMS = "https://firms.modaps.eosdis.nasa.gov"

# (yearly country file prefix, Area API source stem) for each sensor.
SENSORS = [
    ("modis", "MODIS"),
    ("viirs-snpp", "VIIRS_SNPP"),
    ("viirs-jpss1", "VIIRS_NOAA20"),
    (None, "VIIRS_NOAA21"),  # no yearly country files
]

# Read as text so "0130" and "6.03" keep their exact form.
TEXT_COLS = {"acq_time": str, "version": str}


def clip(df, source):
    west, south, east, north = BBOX
    df = df[df.longitude.between(west, east) & df.latitude.between(south, north)].copy()
    df["acq_time"] = df["acq_time"].str.zfill(4)
    df["source"] = source
    return df


def save(df, path):
    tmp = path.with_suffix(".part")
    df.to_csv(tmp, index=False)
    os.replace(tmp, path)
    print(f"  {path.name}: {len(df)} hotspots")


def country_files():
    """(prefix, year, size in bytes) for every yearly Canada file in the FIRMS index."""
    r = requests.get(f"{FIRMS}/data/country/yearly_summary_files.txt", timeout=60)
    r.raise_for_status()
    files = []
    for line in r.text.splitlines():
        name, size = line.split(",")[:2]
        if name.endswith("_Canada.csv"):
            prefix, year, _ = name.split("_")
            files.append((prefix, int(year), int(size)))
    return files


def download_country(prefix, year, size):
    path = OUT_DIR / f"country_{prefix}_{year}.csv"
    if path.exists():
        return
    print(f"{prefix} {year} Canada file ({size / 1e6:.0f} MB)")
    url = f"{FIRMS}/data/country/{prefix}/{year}/{prefix}_{year}_Canada.csv"
    with requests.get(url, stream=True, timeout=120) as r:
        r.raise_for_status()
        r.raw.decode_content = True
        chunks = pd.read_csv(r.raw, dtype=TEXT_COLS, chunksize=500_000)
        df = pd.concat(clip(c, f"country:{prefix}") for c in chunks)
    save(df, path)


def api_get(url, key):
    """GET a FIRMS API URL and return its text. Never prints the URL, which holds the key."""
    for _ in range(10):
        try:
            r = requests.get(url, timeout=120)
        except requests.RequestException as e:
            print(f"  network error ({type(e).__name__}), retrying in 30 s")
            time.sleep(30)
            continue
        text = r.text
        if "limit" in text[:200].lower():
            print("  FIRMS transaction limit reached, waiting 60 s")
            time.sleep(60)
        elif r.status_code >= 500:
            print(f"  FIRMS HTTP {r.status_code}, retrying in 30 s")
            time.sleep(30)
        elif r.status_code != 200 or text.startswith("Invalid"):
            raise RuntimeError(f"FIRMS HTTP {r.status_code}: {text[:200].replace(key, '<KEY>')}")
        else:
            return text
    raise RuntimeError("FIRMS request kept failing; try again later")


def availability(key):
    """{API source: (first date, last date)} from the FIRMS data availability API."""
    text = api_get(f"{FIRMS}/api/data_availability/csv/{key}/ALL", key)
    df = pd.read_csv(io.StringIO(text))
    return {row.data_id: (date.fromisoformat(row.min_date), date.fromisoformat(row.max_date))
            for row in df.itertuples()}


def fetch_range(key, source, start, end):
    """All Area API hotspots for one source from start to end, inclusive, 5 days per call."""
    area = ",".join(str(v) for v in BBOX)
    frames = []
    day = start
    while day <= end:
        days = min(5, (end - day).days + 1)
        text = api_get(f"{FIRMS}/api/area/csv/{key}/{source}/{area}/{days}/{day}", key)
        if text.strip():
            frames.append(pd.read_csv(io.StringIO(text), dtype=TEXT_COLS))
        day += timedelta(days=days)
    # Quiet 5-day windows return only a header; drop them unless every window was quiet.
    df = pd.concat([f for f in frames if len(f)] or frames)
    df = df[df.acq_date.between(str(start), str(end))]
    return clip(df, f"api:{source}")


def download_api(key, stem, after, avail):
    """Fetch every date after `after` for one sensor: SP first, then NRT. One file per year."""
    for kind in ("SP", "NRT"):
        source = f"{stem}_{kind}"
        if source not in avail:
            continue
        first, last = avail[source]
        first = max(first, after + timedelta(days=1))
        if kind == "NRT" and f"{stem}_SP" in avail:
            first = max(first, avail[f"{stem}_SP"][1] + timedelta(days=1))
        for year in range(first.year, last.year + 1):
            path = OUT_DIR / f"api_{source}_{year}.csv"
            if path.exists() and year < date.today().year:
                continue
            start, end = max(first, date(year, 1, 1)), min(last, date(year, 12, 31))
            if start > end:
                continue
            print(f"{source} {start} to {end} (Area API)")
            save(fetch_range(key, source, start, end), path)


def main():
    load_dotenv(Path(__file__).parent / ".env")
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    print(f"Area: west, south, east, north = {BBOX}")

    files = country_files()
    for prefix, stem in SENSORS:
        for p, year, size in sorted(files):
            if p == prefix:
                download_country(p, year, size)

    key = os.environ.get("FIRMS_MAP_KEY", "").strip()
    if not key:
        print("No FIRMS_MAP_KEY in .env: skipped recent dates and NOAA-21 (Area API).")
        return
    avail = availability(key)
    for prefix, stem in SENSORS:
        years = [y for p, y, _ in files if p == prefix]
        after = date(max(years), 12, 31) if years else date(1900, 1, 1)
        download_api(key, stem, after, avail)
    print(f"Done. Files are in {OUT_DIR}")


if __name__ == "__main__":
    main()
