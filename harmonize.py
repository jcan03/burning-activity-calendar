"""Interim harmonization of MODIS and VIIRS hotspots for the burning calendar.

This is a stand-in so the app can be built. Replace it with the team's final
method by keeping the function names and the columns they return.

Method (see docs/harmonization-research.md):
- Filter rows, then count hotspots per day for each sensor family.
- Index = hotspots per satellite per 30 days, in VIIRS units. From 2012-02 it
  is the VIIRS rate. Before that it is the MODIS rate times one factor, k,
  fitted on 2012-02 to 2021-12. Satellites are never added together.
- Each month is ranked against the same calendar month in other years, and
  each summer (June to September) against the other summers.
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
# Whole days a satellite sent nothing. Two sources, each checked against the data: on every day listed
# the satellite has no hotspots.
# - The gaps in docs/sensor-reference.md, trimmed to full days. These are UTC days; a gap covers the same
#   number of Pacific days, 7 hours earlier, which is near enough.
# - Days with no scene from the satellite in NASA's granule catalogue, by local date, and NOAA-20's four
#   days of July 2023 with normal scenes but no hotspots (docs/harmonization-tests.md, "Availability flag").
OUTAGES = {
    "Terra": [("2001-06-15", "2001-07-03"), ("2002-03-19", "2002-03-28"), ("2002-04-14", "2002-04-14"),
              ("2003-02-10", "2003-02-11"), ("2003-10-02", "2003-10-04"), ("2003-10-06", "2003-10-07"),
              ("2003-10-09", "2003-10-09"), ("2003-10-11", "2003-10-13"), ("2003-12-16", "2003-12-24"),
              ("2004-02-18", "2004-02-18"), ("2006-06-20", "2006-06-20"), ("2006-08-22", "2006-08-22"),
              ("2008-12-20", "2008-12-22"), ("2016-02-18", "2016-02-26"), ("2022-10-10", "2022-10-22"),
              ("2025-05-12", "2025-05-15"), ("2026-03-04", "2026-03-09")],
    "Aqua": [("2002-07-30", "2002-08-07"), ("2002-09-13", "2002-09-13"), ("2002-11-15", "2002-11-15"),
             ("2003-03-14", "2003-03-14"), ("2003-05-12", "2003-05-12"), ("2020-08-20", "2020-09-02"),
             ("2022-03-31", "2022-04-16")],
    "N": [("2012-03-25", "2012-03-25"), ("2022-07-27", "2022-08-10"), ("2023-07-26", "2023-07-26"),
          ("2024-05-30", "2024-06-03"), ("2024-07-10", "2024-07-15"), ("2024-07-24", "2024-07-28"),
          ("2024-09-26", "2024-09-26"), ("2024-11-03", "2024-11-05"), ("2025-07-05", "2025-07-07"),
          ("2026-03-10", "2026-03-12"), ("2026-04-28", "2026-04-30"), ("2026-06-01", "2026-06-02"),
          ("2026-07-11", "2026-07-16"), ("2026-08-03", "2026-08-03")],
    "N20": [("2023-07-19", "2023-07-22"), ("2023-09-30", "2023-09-30"), ("2024-02-04", "2024-02-04")],
    "N21": [("2024-02-27", "2024-02-28"), ("2026-01-10", "2026-01-13"), ("2026-11-05", "2026-11-06")],
}
SPLICE = pd.Period("2012-02")           # first month taken from VIIRS
FIT = ("2012-02", "2021-12")            # months used to fit k: both sensors flying, before the MODIS orbits drifted
OVERLAP = ("2012-02", "2025-12")        # months used to check the method, so 2022 onward tests k on years it was not fitted on
BASE_YEARS = (2001, 2025)               # complete years of standard data
SUMMER = [6, 7, 8, 9]                   # months of the summer rating: where the two sensors see the same fires
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


def in_shape(rows, shape):
    """Rows inside a closed outline drawn on the map: a list of (lon, lat) corners."""
    lon, lat = np.array(shape).T
    rows = in_box(rows, (lat.min(), lon.min(), lat.max(), lon.max()))
    x, y, inside = rows.lon.to_numpy(), rows.lat.to_numpy(), np.zeros(len(rows), bool)
    for x0, y0, x1, y1 in zip(lon, lat, np.roll(lon, -1), np.roll(lat, -1)):
        if y0 != y1:    # a point is inside if a line going east from it crosses the outline an odd number of times
            inside ^= ((y0 > y) != (y1 > y)) & (x < x0 + (x1 - x0) * (y - y0) / (y1 - y0))
    return rows[inside]


def satellites_flying(end):
    """Number of satellites of each family in service on each day, outages removed."""
    days = pd.date_range("2000-11-01", end)
    flying = pd.DataFrame({s: (days >= a) & (days <= (b or end)) for s, (a, b) in SERVICE.items()}, index=days)
    for sat, gaps in OUTAGES.items():
        for a, b in gaps:
            flying.loc[a:b, sat] = False
    return pd.DataFrame({"sats_modis": flying[MODIS].sum(axis=1), "sats_viirs": flying[VIIRS].sum(axis=1)})


def daily(rows, bbox, shape=None):
    """One row per day: hotspot counts and satellites flying for each family, plus an nrt flag.

    Counts the hotspots in the box, or inside `shape` (see in_shape) when one is given.
    """
    flying = satellites_flying(rows.day.max())
    inside = in_box(rows, bbox) if shape is None else in_shape(rows, shape)
    counts = inside.groupby(["day", "sat"], observed=True).size().unstack(fill_value=0)
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
    """MODIS-to-VIIRS factor from the stable-orbit months, and the same factor fitted year by year."""
    o = m.loc[FIT[0]:FIT[1]].dropna(subset=["rate_modis", "rate_viirs"])
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
        out[t] = {"modis_ranked": modis_ranked, **rank_among(m["index"][t], same, same.index.year)}
    return m.join(rank_columns(out, ["modis_ranked"]))


def rank_among(v, same, years):
    """Where a value stands among the same period in other years. A value too tied to place gets no rank."""
    r = {"n_years": len(same) + 1}
    if not np.isnan(v) and len(same) >= MIN_YEARS:
        r["pct"] = ((same < v).sum() + 0.5 * (same == v).sum()) / len(same)
        r["uncertain"] = (same == v).mean() >= TIE_SHARE
        r["since"] = years.min()
        r["typical"], r["low"], r["high"] = same.median(), same.quantile(0.1), same.quantile(0.9)
        r["times_typical"] = v / r["typical"] if r["typical"] >= MIN_TYPICAL else np.nan
        if not r["uncertain"]:
            r["cls"] = min(int(r["pct"] * 5), 4)
            r["record"] = v > same.max()
            r["rank"] = 1 + (same > v).sum()
    return r


def rank_columns(out, extra=()):
    cols = ["pct", "cls", "uncertain", "record", "rank", "n_years", "since", "typical", "low", "high", "times_typical"]
    ranks = pd.DataFrame.from_dict(out, orient="index").reindex(columns=cols + list(extra))
    ranks["uncertain"], ranks["record"] = ranks.uncertain.eq(True), ranks.record.eq(True)   # unset means no
    return ranks


def summer_table(c):
    """One row per year: June to September as a whole, ranked against the other summers.

    A small area often has too few hotspots to rank a single month; four months together usually have
    enough. The value is the mean of the four monthly index values, so it is in the calendar's units.
    Summers are ranked by the months' rules, against every other year from 2001. A summer with a month
    missing or not finished gets no value.
    """
    months = c[c.index.month.isin(SUMMER)]
    by_year = months.groupby(months.index.year)
    whole = (by_year["index"].count() == len(SUMMER)) & ~by_year.partial.any()
    s = by_year[["nrt", "modis_scaled", "outage"]].any()
    s.insert(0, "index", by_year["index"].mean().where(whole))
    base = s["index"].loc[BASE_YEARS[0]:BASE_YEARS[1]].dropna()
    out = {year: rank_among(v, base.drop(year, errors="ignore"), base.index.drop(year, errors="ignore"))
           for year, v in s["index"].items()}
    return s.join(rank_columns(out))


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
