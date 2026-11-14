"""Burning Activity Calendar: a Streamlit app over cached FIRMS hotspots.

Run:  streamlit run app.py
Needs data/kamloops.sqlite (python download_kamloops.py, then python build_db.py).
Runs offline: no FIRMS call, no MAP_KEY, no web map tiles.
"""
import numpy as np
import pandas as pd
import streamlit as st

import animations
import charts
import harmonize as h

st.set_page_config(page_title="Burning Activity Calendar", page_icon="🔥", layout="wide")

CUSTOM = "Custom box"
PRESETS = {  # south, west, north, east. The first is what the app opens on.
    "Kamloops area": (50.22, -121.04, 51.12, -119.62),   # 100 km square on the city; smaller is too noisy to rank
    "Okanagan Valley": (49.0, -119.9, 50.8, -118.5),
    "Shuswap": (50.4, -119.8, 51.5, -118.4),
    "Nicola Valley": (49.8, -121.3, 50.5, -120.0),
    "Fraser Canyon": (49.8, -122.2, 50.9, -121.0),
    "South Cariboo": (51.6, -122.5, 52.5, -120.5),
    "Southern Interior BC (all data)": h.BOX,
}
MONTH_NAMES = pd.date_range("2025-01-01", periods=12, freq="MS").strftime("%B").tolist()
FIRST = pd.Timestamp("2000-11-01")  # first day of the record


@st.cache_resource(show_spinner="Loading hotspots...")
def rows():
    return h.load_rows()


@st.cache_data(show_spinner=False)
def factor():
    return h.fit_k(h.monthly_rates(h.daily(rows(), h.BOX)))


@st.cache_data(show_spinner="Counting hotspots in this area...")
def tables(bbox):
    d = h.daily(rows(), bbox)
    return d, h.calendar_table(h.monthly_rates(d), factor()[0])


@st.cache_resource(show_spinner=False)
def weighted():
    """The hotspots with each one's share of the index, so 3D heights use the calendar's units."""
    return rows().assign(w=h.weights(rows(), factor()[0]))


@st.cache_data(max_entries=8, show_spinner="Building the timelapse...")
def timelapse_figure(bbox, start, stop):
    return animations.timelapse(rows(), bbox, start, stop)


@st.cache_data(max_entries=4, show_spinner="Building the 3D view...")
def columns_page(bbox, start, stop, cell_km, add_up, orbit):
    return animations.columns_3d(weighted(), bbox, start, stop, cell_km, add_up, orbit)


def ordinal(n):
    n = int(n)
    return f"{n}{'th' if 10 <= n % 100 <= 20 else {1: 'st', 2: 'nd', 3: 'rd'}.get(n % 10, 'th')}"


def sentence(t, r):
    """One plain sentence comparing a month with the same month in other years."""
    name, month = charts.month_name(t), t.strftime("%B")
    was = "so far is" if r.partial else "was"
    if np.isnan(r["index"]):
        return f"{name}: not enough satellite data to rank this month."
    if r.uncertain:
        return f"{name} cannot be ranked here: too many other years have the same value."
    if np.isnan(r.cls):
        return f"{name}: too few comparable years to rank this month."
    place = f"the busiest {month} on record" if r.record else f"the {ordinal(r['rank'])} busiest {month} of {r.n_years:.0f}"
    text = f"{name} {was} **{charts.CLASSES[int(r.cls)].lower()}**: {place} (compared with {r.since:.0f} to {h.BASE_YEARS[1]})."
    if not np.isnan(r.times_typical):
        x = r.times_typical
        amount = "more than 100" if x > 100 else f"about {x:.0f}" if x >= 10 else f"{x:.1f}"
        text += f" That is {amount} times a typical {month}."
    return text


def pick_month():
    """Calendar click: select that month."""
    points = st.session_state.calendar["selection"]["points"]
    if points:
        month = points[0]["customdata"]
        t = pd.Period(month[0] if isinstance(month, list) else month)
        st.session_state.year, st.session_state.month = t.year, t.month


def pick_area():
    """Box drawn on the map: use it as the area."""
    boxes = st.session_state.map["selection"]["box"]
    if boxes:
        west, east = sorted(boxes[0]["x"])
        south, north = sorted(boxes[0]["y"])
        st.session_state.area = CUSTOM
        st.session_state.south, st.session_state.north = round(max(south, h.BOX[0]), 2), round(min(north, h.BOX[2]), 2)
        st.session_state.west, st.session_state.east = round(max(west, h.BOX[1]), 2), round(min(east, h.BOX[3]), 2)


def pick_months(first, last):
    """Quick pick: move the period slider to these months, kept inside the record."""
    record = pd.period_range(FIRST, rows().day.max(), freq="M")
    st.session_state.months = (min(max(first, record[0]), record[-1]), max(min(last, record[-1]), record[0]))


if not h.DB.exists():
    st.error("No cached data found. Run `python download_kamloops.py`, then `python build_db.py`.")
    st.stop()

end = rows().day.max()
latest = end.to_period("M")
k, k_by_year = factor()
st.session_state.setdefault("year", latest.year)
st.session_state.setdefault("month", latest.month)

with st.sidebar:
    st.header("Area")
    area = st.selectbox("Area", list(PRESETS) + [CUSTOM], key="area", label_visibility="collapsed")
    if area == CUSTOM:
        kam = PRESETS["Kamloops area"]
        left, right = st.columns(2)
        south = left.number_input("South", h.BOX[0], h.BOX[2], kam[0], 0.1, key="south")
        north = right.number_input("North", h.BOX[0], h.BOX[2], kam[2], 0.1, key="north")
        west = left.number_input("West", h.BOX[1], h.BOX[3], kam[1], 0.1, key="west")
        east = right.number_input("East", h.BOX[1], h.BOX[3], kam[3], 0.1, key="east")
        if south >= north or west >= east:
            st.error("South must be below north, and west must be left of east.")
            st.stop()
        bbox = (south, west, north, east)
    else:
        bbox = PRESETS[area]
    st.caption("Or drag a box on the Map tab.")

    st.header("Month in focus")
    left, right = st.columns(2)
    year = left.selectbox("Year", range(2000, latest.year + 1), key="year")
    month = right.selectbox("Month", range(1, 13), format_func=lambda m: MONTH_NAMES[m - 1], key="month")
    st.caption("Or click a month on the calendar.")

    st.header("Calendar")
    years = st.slider("Years shown", 2000, latest.year, (2000, latest.year))
    view = st.radio("Colour by", ["index", "class"],
                    format_func={"index": "Hotspot activity", "class": "Compared with normal"}.get)
    st.caption(f"Data: NASA FIRMS, MODIS and VIIRS 375 m, to {end:%d %B %Y}.")

d, c = tables(bbox)
t = pd.Period(year=year, month=month, freq="M")

st.title("Burning Activity Calendar")
st.caption("Kamloops and the Southern Interior of British Columbia. Satellite fire hotspots from MODIS and VIIRS, "
           "2000 to today, harmonized into one record.")

if c.count_modis.sum() + c.count_viirs.sum() == 0:
    st.warning("No hotspots were detected in this area. Choose a larger area.")
    st.stop()

st.subheader(area)
if t in c.index:
    r = c.loc[t]
    st.markdown(f"#### {sentence(t, r)}")
    notes = charts.flags(r)
    if notes:
        st.caption("Note: " + "; ".join(notes) + ".")
    if not np.isnan(r["index"]):
        one, two, three = st.columns(3)
        one.metric("Index", f"{r['index']:,.0f}", help="Hotspots per satellite per 30 days, in VIIRS units.")
        two.metric(f"Rank among {t.strftime('%B')}s", "-" if np.isnan(r["rank"]) else f"{r['rank']:.0f} of {r.n_years:.0f}")
        three.metric(f"Typical {t.strftime('%B')}", "-" if np.isnan(r.typical) else f"{r.typical:,.0f}",
                     help="Median of the same month in the other years.")
else:
    st.info(f"There is no data for {charts.month_name(t)}. The record runs from November 2000 to {end:%d %B %Y}.")

unranked = c.loc[str(h.BASE_YEARS[0]):str(h.BASE_YEARS[1])].uncertain.mean()
if unranked > 0.15:
    st.warning(f"In this area {unranked:.0%} of months cannot be ranked, because hotspots are too few. "
               "Small areas are noisy: a larger area gives a steadier calendar.")

calendar_tab, season_tab, map_tab, method_tab, download_tab = st.tabs(
    ["Calendar", "Season and daily", "Map", "Method", "Download"])

with calendar_tab:
    st.plotly_chart(charts.calendar(c, view, t, years), key="calendar", on_select=pick_month, selection_mode="points",
                    config={"displayModeBar": False})
    st.caption("Index = hotspots per satellite per 30 days, in VIIRS units. "
               "\"Compared with normal\" ranks each month against the same month in other years.")
    if t in c.index and not np.isnan(c.loc[t, "index"]):
        st.plotly_chart(charts.month_history(c, t), config={"displayModeBar": False})
    with st.expander("Show the calendar as a table"):
        shown = c[(c.index.year >= years[0]) & (c.index.year <= years[1])]
        table = pd.DataFrame({
            "Month": shown.index.strftime("%Y-%m"), "Index": shown["index"].round(1),
            "Compared with normal": [charts.CLASSES[int(x)] if not np.isnan(x) else "Not ranked" for x in shown.cls],
            "Rank": shown["rank"], "Of years": shown.n_years, "MODIS hotspots": shown.count_modis,
            "VIIRS hotspots": shown.count_viirs, "Notes": ["; ".join(charts.flags(row)) for _, row in shown.iterrows()],
        })
        st.dataframe(table, hide_index=True)

with season_tab:
    st.plotly_chart(charts.season(d, k, year), config={"displayModeBar": False})
    st.caption("A steep rise is a burst of burning. The grey band is where the middle 80% of other years sit.")
    if t in c.index:
        st.plotly_chart(charts.daily_bars(d, k, t), config={"displayModeBar": False})
        st.caption("Daily values are indicative only and are not ranked: on a single day the two sensors often "
                   "disagree, and a few days usually hold most of a month's hotspots.")

with map_tab:
    # The period: the whole record to start with. Quick picks and the slider both set it, month by month.
    record = pd.period_range(FIRST, end, freq="M")
    picks = {"Whole record": (record[0], record[-1]), f"All of {year}": (pd.Period(f"{year}-01"), pd.Period(f"{year}-12")),
             f"June to September {year}": (pd.Period(f"{year}-06"), pd.Period(f"{year}-09")), charts.month_name(t): (t, t)}
    for column, (label, span) in zip(st.columns(len(picks)), picks.items()):
        column.button(label, on_click=pick_months, args=span, width="stretch")
    timeline = st.container()   # drawn above the slider, but it needs the slider's months
    first, last = st.select_slider("Period", record, (record[0], record[-1]), key="months",
                                   format_func=lambda m: m.strftime("%b %Y"), label_visibility="collapsed")
    start, stop = max(first.start_time, FIRST), min(last.end_time.normalize(), end)
    timeline.plotly_chart(animations.timeline(h.daily_index(d, k), start, stop), config={"displayModeBar": False})
    n = h.in_box(rows(), bbox).day.between(start, stop).sum()
    st.caption(f"**{n:,} hotspots** in this area from {start:%d %b %Y} to {stop:%d %b %Y}. "
               "Drag the two ends of the slider, or use a button above, to choose the period.")

    view = st.radio("View", ["Map", "Timelapse", "3D"], horizontal=True, label_visibility="collapsed")
    if view == "Map":
        points = h.in_box(rows(), bbox)
        points = points[points.day.between(start, stop)]
        sample = " (a sample of 20,000)" if len(points) > 20000 else ""
        title = f"Hotspots from {start:%d %b %Y} to {stop:%d %b %Y}{sample}"
        st.plotly_chart(charts.hotspot_map(points, bbox, title), key="map", on_select=pick_area, selection_mode="box")
        st.caption("Drag a box on the map to zoom in to a smaller area. For a wider view, pick another area in the "
                   "sidebar. VIIRS has smaller pixels than MODIS, so it draws many more dots for the same fire.")
    elif view == "Timelapse":
        st.plotly_chart(timelapse_figure(bbox, start, stop), config={"displayModeBar": False})
        st.caption("Press Play. Coloured dots are the hotspots of each step, and grey dots the three steps before. "
                   "Busy steps show a sample of the dots; the title counts every hotspot. VIIRS draws many more "
                   "dots than MODIS for the same fire.")
    else:
        wide = max(bbox[2] - bbox[0], bbox[3] - bbox[1]) > 1.5
        left, middle, right = st.columns([1, 1.5, 2])
        cell_km = left.selectbox("Square size", [2, 5, 10], index=1 if wide else 0, format_func=lambda km: f"{km} km")
        add_up = middle.toggle("Add up through the period")
        orbit = right.toggle("Rotate while it plays")
        page = columns_page(bbox, start, stop, cell_km, add_up, 50 if orbit else 0)
        if page is None:
            st.info("No hotspots in this area and period.")
        else:
            html, top, cell_km, stretch = page
            st.iframe(html, height=640)
            what = ("Columns add up through the period, so they only rise" if add_up else
                    "Columns show the burning at each step, so they rise when a fire starts and drop when it is out")
            st.caption(f"Press Play. {what}. Pause to rotate by dragging; scroll to zoom. Each column is a {cell_km} km square. "
                       f"Its height is the square root of its activity (hotspots per satellite, in VIIRS units); "
                       f"the tallest stands for {top:,.0f}. Heights are relative to the busiest square of this "
                       "period, so they cannot be compared between periods.")
            if stretch:
                st.caption(f"The ground is real elevation, coloured from dry valley floors through forest to bare "
                           f"summits, with lakes and wide rivers in blue. It is drawn {stretch:.0f} times taller than "
                           "true so the mountains show.")
    if charts.BASEMAP.exists() or charts.TERRAIN.exists():
        st.caption("Terrain: NASA GIBS. Elevation and shaded relief from the ASTER Global Digital Elevation Model "
                   "(NASA/METI); water from the MODIS land and water mask.")

with method_tab:
    st.markdown(f"""
**How it works.** Satellites flag a hotspot when a patch of ground looks hot enough to be burning. Two sensor families
do this: MODIS (2 satellites, since 2000) and VIIRS (up to 3 satellites, since 2012). They cannot be added together,
because VIIRS sees about {k:.1f} times as many hotspots per satellite as MODIS, and the number of satellites has
changed five times.

1. **Count per satellite.** Each month's hotspots are divided by the number of satellite-days in service.
2. **One unit.** From February 2012 the index is the VIIRS rate. Before that it is the MODIS rate times {k:.1f},
   a factor measured on the 14 years when both flew (it ranged from {k_by_year.min():.1f} to {k_by_year.max():.1f} by year).
3. **Rank, not count.** Each month is ranked against the same calendar month in other years, in five classes.
""")
    left, right = st.columns(2)
    left.plotly_chart(charts.adding_satellites(c), config={"displayModeBar": False})
    left.caption("Adding every hotspot together makes recent years look far busier, only because more satellites "
                 "are flying. The per-satellite index removes that.")
    o = c.loc[h.OVERLAP[0]:h.OVERLAP[1]].dropna(subset=["rate_modis", "rate_viirs"])
    within = (np.abs(np.log2((o.rate_viirs + 1) / (k * o.rate_modis + 1))) <= 1).mean()
    right.plotly_chart(charts.sensor_check(c, k), config={"displayModeBar": False})
    right.caption(f"Each dot is a month from 2012 to 2025, when both sensors flew. In this area {within:.0%} of months "
                  "agree within a factor of 2.")
    st.markdown("""
**What to keep in mind**

- Hotspots are detections, not hectares burned. One large fire can give thousands of hotspots.
- Values before February 2012 are scaled from MODIS and are good to about a factor of 2.
- MODIS misses most small burns outside the fire season. From October to April, months since 2012 are ranked against
  2012 onward only, and earlier months against MODIS years only.
- Months since August 2026 use provisional near-real-time data and may change.
- Small areas have few hotspots, so many months cannot be ranked.
- Low-confidence detections and one fixed industrial heat source west of Kamloops are removed.
""")

with download_tab:
    dates = st.date_input("Date range", (start.date(), stop.date()), min_value=FIRST.date(), max_value=end.date())
    if len(dates) == 2:
        a, b = dates
        n = h.in_box(rows(), bbox).day.between(pd.Timestamp(a), pd.Timestamp(b)).sum()
        st.write(f"**{n:,} hotspots** in {area} from {a:%d %b %Y} to {b:%d %b %Y}, after quality filters.")
        st.download_button("Download hotspots (CSV)", lambda: h.raw_hotspots(bbox, a, b).to_csv(index=False),
                           file_name=f"hotspots_{a}_{b}.csv", mime="text/csv")
        st.caption("The file has every FIRMS column, unfiltered, so it can hold a few more rows than the count above. "
                   "Long ranges over a large area take a few seconds. The dates start as the period chosen on the Map tab.")
    st.download_button("Download the monthly index (CSV)", c.to_csv(index_label="month"),
                       file_name="monthly_index.csv", mime="text/csv")
