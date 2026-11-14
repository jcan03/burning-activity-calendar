"""Interim harmonization of MODIS and VIIRS hotspots for the burning calendar.

This is a stand-in so the app can be built. Replace it with the team's final
method by keeping the function names and the columns they return.

Method (see docs/harmonization-research.md):
- Filter rows, then count hotspots per day for each sensor family.
- Index = hotspots per satellite per 30 days, in VIIRS units. From 2012-02 it
  is the VIIRS rate. Before that it is the MODIS rate times one factor, k.
  Satellites are never added together.
- Each month is ranked against the same calendar month in other years.
- Days are Pacific days (UTC-7), not the UTC days in the FIRMS files.
"""
import sqlite3
from pathlib import Path

import numpy as np
import pandas as pd

DB = Path(__file__).parent / "data" / "kamloops.sqlite"
BOX = (49.0, -122.5, 52.5, -118.0)  # south, west, north, east of the cached data
MODIS, VIIRS = ["Terra", "Aqua"], ["N", "N20", "N21"]
STATIC_SITE = (50.68872, -120.40745)  # fixed night-time heat source west of Kamloops
UTC_OFFSET = -7  # hours. Hotspots are dated in Pacific time, as in Kamloops, not the UTC of the FIRMS files
LOCAL_DAY = f"date(acq_date || ' ' || substr(acq_time, 1, 2) || ':' || substr(acq_time, 3, 2), '{UTC_OFFSET} hours')"
# First and last day each satellite has data in FIRMS (None = still flying).
SERVICE = {"Terra": ("2000-11-01", None), "Aqua": ("2002-07-04", None), "N": ("2012-01-20", "2026-11-02"),
           "N20": ("2018-04-01", None), "N21": ("2023-03-01", None)}
# Whole days a satellite sent nothing: the gaps in docs/sensor-reference.md, trimmed to full days and
# checked against the data wherever the season was busy enough to show them. These are UTC days; a gap
# covers the same number of Pacific days, 7 hours earlier, which is near enough.
OUTAGES = {
    "Terra": [("2001-06-15", "2001-07-03"), ("2002-03-19", "2002-03-28"), ("2003-12-16", "2003-12-24"),
              ("2016-02-18", "2016-02-24"), ("2022-10-11", "2022-10-21")],
    "Aqua": [("2020-08-20", "2020-09-02"), ("2022-03-31", "2022-04-16")],
    "N": [("2022-07-27", "2022-08-10"), ("2024-11-03", "2024-11-05"), ("2026-03-10", "2026-03-12"),
          ("2026-04-29", "2026-04-30"), ("2026-07-11", "2026-07-16"), ("2026-08-03", "2026-08-03")],
    "N21": [("2026-11-05", "2026-11-06")],
}
SPLICE = pd.Period("2012-02")           # first month taken from VIIRS
OVERLAP = ("2012-02", "2025-12")        # months used to fit k and check the method
BASE_YEARS = (2001, 2025)               # complete years of standard data
MIN_SAT_DAYS, MIN_YEARS, TIE_SHARE, MIN_TYPICAL = 8, 8, 0.2, 3


def load_rows():
    """Filtered hotspots for the whole box: lat, lon, day (Pacific time), sat, nrt."""
    con = sqlite3.connect(f"file:{DB.as_posix()}?mode=ro", uri=True)
    df = pd.read_sql_query(
        "SELECT latitude lat, longitude lon, acq_date || acq_time utc, satellite sat, confidence conf, type FROM hotspots", con)
    con.close()
    day = (pd.to_datetime(df.utc, format="%Y-%m-%d%H%M") + pd.Timedelta(hours=UTC_OFFSET)).dt.normalize()
    conf = pd.to_numeric(df.conf, errors="coerce")
    km_north = (df.lat - STATIC_SITE[0]) * 111.2
    km_east = (df.lon - STATIC_SITE[1]) * 111.2 * np.cos(np.radians(STATIC_SITE[0]))
    keep = (
        ~df.type.isin([1, 2])                                             # volcano, static source
        & (np.hypot(km_north, km_east) > 0.4)                             # the static site, typed or not
        & np.where(df.sat.isin(MODIS), conf >= 30, df.conf != "l")        # low confidence
        & (day >= SERVICE["Terra"][0]) & (day < day.max())                # the first and last days are only part of a day
    )
    df = df[keep]
    return pd.DataFrame({"lat": df.lat, "lon": df.lon, "day": day[keep],
                         "sat": df.sat.astype("category"), "nrt": df.type.isna()})


def in_box(rows, bbox):
    south, west, north, east = bbox
    return rows[rows.lat.between(south, north) & rows.lon.between(west, east)]


def satellites_flying(end):
    """Number of satellites of each family in service on each day, outages removed."""
    days = pd.date_range("2000-11-01", end)
    flying = pd.DataFrame({s: (days >= a) & (days <= (b or end)) for s, (a, b) in SERVICE.items()}, index=days)
    for sat, gaps in OUTAGES.items():
        for a, b in gaps:
            flying.loc[a:b, sat] = False
    return pd.DataFrame({"sats_modis": flying[MODIS].sum(axis=1), "sats_viirs": flying[VIIRS].sum(axis=1)})


def daily(rows, bbox):
    """One row per day: hotspot counts and satellites flying for each family, plus an nrt flag."""
    flying = satellites_flying(rows.day.max())
    counts = in_box(rows, bbox).groupby(["day", "sat"], observed=True).size().unstack(fill_value=0)
    counts = counts.reindex(index=flying.index, columns=MODIS + VIIRS, fill_value=0)
    return pd.DataFrame({
        "count_modis": counts[MODIS].sum(axis=1), "count_viirs": counts[VIIRS].sum(axis=1),
        "sats_modis": flying.sats_modis, "sats_viirs": flying.sats_viirs,
        "nrt": flying.index >= rows.day[rows.nrt].min(),
    })


def weights(rows, k):
    """Each hotspot's share of the daily index, so maps of hotspots can use the same units.

    A VIIRS hotspot from the splice onward counts 1 / VIIRS satellites flying that day. A MODIS
    hotspot before it counts k / MODIS satellites flying. The family the index does not use counts 0.
    """
    flying = satellites_flying(rows.day.max())
    viirs = rows.sat.isin(VIIRS).to_numpy()
    sats = np.where(viirs, flying.sats_viirs.reindex(rows.day), flying.sats_modis.reindex(rows.day))
    used = (viirs == (rows.day >= SPLICE.start_time).to_numpy()) & (sats > 0)
    return np.where(used, np.where(viirs, 1.0, k) / np.maximum(sats, 1), 0.0)


def monthly_rates(d):
    """Monthly hotspots per satellite per 30 days for each family, with data-quality flags."""
    m = d.groupby(d.index.to_period("M")).sum()
    for fam in ("modis", "viirs"):
        enough = m[f"sats_{fam}"] >= MIN_SAT_DAYS
        m[f"rate_{fam}"] = (30 * m[f"count_{fam}"] / m[f"sats_{fam}"]).where(enough)
    end = d.index.max()
    m["modis_scaled"] = m.index < SPLICE
    m["terra_only"] = m.index < pd.Period("2002-07")
    m["nrt"] = m.nrt > 0
    m["outage"] = m.index.isin([pd.Period(a, "M") for gaps in OUTAGES.values() for a, b in gaps]
                               + [pd.Period(b, "M") for gaps in OUTAGES.values() for a, b in gaps])
    m["partial"] = (m.index == end.to_period("M")) & (end.day < end.days_in_month)
    return m


def fit_k(m):
    """MODIS-to-VIIRS factor from the overlap months, and the same factor fitted year by year."""
    o = m.loc[OVERLAP[0]:OVERLAP[1]].dropna(subset=["rate_modis", "rate_viirs"])
    by_year = o.groupby(o.index.year)[["rate_viirs", "rate_modis"]].sum()
    return o.rate_viirs.sum() / o.rate_modis.sum(), by_year.rate_viirs / by_year.rate_modis


def calendar_table(m, k):
    """Add the harmonized index and each month's rank against the same calendar month.

    Baseline: May-September months are ranked against every year from 2001. Other
    months are ranked against VIIRS months only (February 2012 onward), because MODIS
    misses the small burns that dominate the off-season. Off-season months before
    then are ranked against MODIS years only. A month too tied to place gets no rank.
    """
    m = m.copy()
    from_modis = k * m.rate_modis
    m["index"] = m.rate_viirs.where(m.index >= SPLICE, from_modis)
    out = {}
    for t in m.index:
        fire_season = 5 <= t.month <= 9
        modis_ranked = not fire_season and t < SPLICE
        series = from_modis if modis_ranked else m["index"]
        first = pd.Period(f"{BASE_YEARS[0]}-01") if fire_season or modis_ranked else SPLICE
        same = series[(series.index.month == t.month) & (series.index >= first)
                      & (series.index.year <= BASE_YEARS[1]) & (series.index.year != t.year)].dropna()
        v = m["index"][t]
        r = {"modis_ranked": modis_ranked, "n_years": len(same) + 1}
        if not np.isnan(v) and len(same) >= MIN_YEARS:
            r["pct"] = ((same < v).sum() + 0.5 * (same == v).sum()) / len(same)
            r["uncertain"] = (same == v).mean() >= TIE_SHARE
            r["since"] = same.index.year.min()
            r["typical"], r["low"], r["high"] = same.median(), same.quantile(0.1), same.quantile(0.9)
            r["times_typical"] = v / r["typical"] if r["typical"] >= MIN_TYPICAL else np.nan
            if not r["uncertain"]:
                r["cls"] = min(int(r["pct"] * 5), 4)
                r["record"] = v > same.max()
                r["rank"] = 1 + (same > v).sum()
        out[t] = r
    cols = ["pct", "cls", "uncertain", "record", "rank", "n_years", "since", "typical", "low", "high",
            "times_typical", "modis_ranked"]
    ranks = pd.DataFrame.from_dict(out, orient="index").reindex(columns=cols)
    ranks["uncertain"], ranks["record"] = ranks.uncertain.eq(True), ranks.record.eq(True)   # unset means no
    return m.join(ranks)


def daily_index(d, k):
    """Indicative daily index: hotspots per satellite per day, in VIIRS units."""
    viirs = d.count_viirs / d.sats_viirs.where(d.sats_viirs > 0)
    modis = k * d.count_modis / d.sats_modis.where(d.sats_modis > 0)
    return viirs.where(d.index >= SPLICE.start_time, modis)


def raw_hotspots(bbox, start, end):
    """Unfiltered FIRMS rows in the area and range of Pacific days, for the CSV download."""
    south, west, north, east = bbox
    con = sqlite3.connect(f"file:{DB.as_posix()}?mode=ro", uri=True)
    df = pd.read_sql_query(
        f"SELECT *, {LOCAL_DAY} local_date FROM hotspots WHERE local_date BETWEEN ? AND ? AND latitude BETWEEN ? AND ? "
        "AND longitude BETWEEN ? AND ? ORDER BY acq_date, acq_time",
        con, params=(str(start), str(end), south, north, west, east))
    con.close()
    return df
