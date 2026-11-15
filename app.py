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
TALL_3D = 440  # pixels: short enough that the period controls under the 3D view fit on a laptop screen with it


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


# No spinners on these two: a spinner would take the view's place and make the period controls under it jump.
@st.cache_data(max_entries=8, show_spinner=False)
def timelapse_figure(bbox, start, stop):
    return animations.timelapse(weighted(), bbox, start, stop, h.daily_index(tables(bbox)[0], factor()[0]))


@st.cache_data(max_entries=4, show_spinner=False)
def columns_page(bbox, start, stop, cell_km, add_up, orbit):
    return animations.columns_3d(weighted(), bbox, start, stop, cell_km, add_up, orbit, height=TALL_3D)


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
        amount = "more than 100 times" if x > 100 else f"about {x:.0f} times" if x >= 10 else f"{x:.1f} times"
        text += f" That is {'less than a tenth of' if x < 0.1 else amount} a typical {month}."
    return text


def pick_month():
    """Calendar click: select that month."""
    points = st.session_state.calendar["selection"]["points"]
    if points:
        month = points[0]["customdata"]
        t = pd.Period(month[0] if isinstance(month, list) else month)
        st.session_state.year, st.session_state.month = t.year, t.month


def pick_on_map():
    """Map selection: a circled region opens its own calendar; a box becomes the app's area."""
    selection = st.session_state.map["selection"]
    if selection["lasso"]:
        lon, lat = selection["lasso"][0]["x"], selection["lasso"][0]["y"]
        some = -(-len(lon) // 120)      # a line drawn by hand has far more corners than it needs
        st.session_state.region = tuple(zip(lon[::some], lat[::some]))
        st.session_state.open_region = len(st.session_state.region) > 2
    elif selection["box"]:
        west, east = sorted(selection["box"][0]["x"])
        south, north = sorted(selection["box"][0]["y"])
        st.session_state.area = CUSTOM
        st.session_state.south, st.session_state.north = round(max(south, h.BOX[0]), 2), round(min(north, h.BOX[2]), 2)
        st.session_state.west, st.session_state.east = round(max(west, h.BOX[1]), 2), round(min(east, h.BOX[3]), 2)


@st.cache_data(max_entries=8, show_spinner="Counting hotspots in the circled region...")
def region_table(shape):
    return h.calendar_table(h.monthly_rates(h.daily(rows(), h.BOX, shape)), factor()[0])


@st.dialog("Circled region", width="large")
def region_calendar(shape, t, colour, years):
    """The burning calendar of a region circled on the map."""
    c = region_table(shape)
    n = int(c.count_modis.sum() + c.count_viirs.sum())
    if n == 0:
        st.info("No hotspots in the circled region. Close this and circle a larger one.")
        return
    lon, lat = np.array(shape).T
    x, y = lon * 111.2 * np.cos(np.radians(lat.mean())), lat * 111.2
    km2 = abs(np.dot(x, np.roll(y, -1)) - np.dot(y, np.roll(x, -1))) / 2
    st.markdown(f"**{n:,} hotspot{'' if n == 1 else 's'}** since November 2000, in about {km2:,.0f} km².")
    if t in c.index:
        st.markdown(f"#### {sentence(t, c.loc[t])}")
    st.plotly_chart(charts.calendar(c, colour, t, years, top=max(c["index"].max(), 10)), config={"displayModeBar": False})
    st.caption("Index = hotspots per satellite per 30 days, in VIIRS units, for the circled region only. The "
               "darkest colour is this region's own busiest month, so its colours cannot be compared with the "
               "main calendar's. A small region has few hotspots, so many of its months cannot be ranked; the "
               "Summer column ranks June to September as a whole, which usually can be. Close this and circle "
               "again to look at another region.")


def pick_months(first, last):
    """Quick pick: move the period slider to these months, kept inside the record."""
    record = pd.period_range(FIRST, rows().day.max(), freq="M")
    st.session_state.months = (min(max(first, record[0]), record[-1]), max(min(last, record[-1]), record[0]))


def pick_period():
    """Timeline click: use the year or month that was clicked as the period."""
    points = st.session_state.timeline["selection"]["points"]
    if points and "customdata" in points[0]:
        months = points[0]["customdata"]
        pick_months(*(pd.Period(m, "M") for m in (months[0] if isinstance(months, list) else months).split()))


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
        bbox = (south, west, north, east)
    else:
        bbox = PRESETS[area]
    st.caption("Or use Box Select on the Map tab's 2D Summary.")

    st.header("Month in focus")
    left, right = st.columns(2)
    year = left.selectbox("Year", range(2000, latest.year + 1), key="year")
    month = right.selectbox("Month", range(1, 13), format_func=lambda m: MONTH_NAMES[m - 1], key="month")
    st.caption("Or click a month on the calendar.")

    st.header("Calendar")
    years = st.slider("Years shown", 2000, latest.year, (2000, latest.year))
    colour = st.radio("Colour by", ["index", "class"],
                      format_func={"index": "Hotspot activity", "class": "Compared with normal"}.get)
    st.caption(f"Data: NASA FIRMS, MODIS and VIIRS 375 m, to {end:%d %B %Y}.")

if bbox[0] >= bbox[2] or bbox[1] >= bbox[3]:
    st.stop()   # only now, so the rest of the sidebar is drawn and keeps its values

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
        two.metric(f"Rank for {t.strftime('%B')}", "-" if np.isnan(r["rank"]) else f"{r['rank']:.0f} of {r.n_years:.0f}")
        three.metric(f"Typical {t.strftime('%B')}", "-" if np.isnan(r.typical) else f"{r.typical:,.0f}",
                     help="Median of the same month in the other years.")
else:
    st.info(f"There is no data for {charts.month_name(t)}. The record runs from November 2000 to {end:%d %B %Y}.")

unranked = c.loc[str(h.BASE_YEARS[0]):str(h.BASE_YEARS[1])].uncertain.mean()
if unranked > 0.15:
    st.warning(f"In this area {unranked:.0%} of months cannot be ranked, because hotspots are too few. "
               "Small areas are noisy: a larger area gives a steadier calendar. The Summer column ranks June to "
               "September as a whole, which usually has enough hotspots.")

calendar_tab, season_tab, map_tab, method_tab, download_tab = st.tabs(
    ["Calendar", "Season and daily", "Map", "Method", "Download"], key="tabs")   # the key keeps the open tab open

with calendar_tab:
    st.plotly_chart(charts.calendar(c, colour, t, years), key="calendar", on_select=pick_month, selection_mode="points",
                    config={"displayModeBar": False})
    st.caption("Index = hotspots per satellite per 30 days, in VIIRS units. "
               "\"Compared with normal\" ranks each month against the same month in other years. "
               "The Summer column is June to September as a whole, ranked against the other summers.")
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
    # The view is on top and the period under it, so both are on screen while the period is changed.
    record = pd.period_range(FIRST, end, freq="M")
    bar = st.columns([3.2, 1.4, 2, 1.7], vertical_alignment="center")
    view = bar[0].radio("View", ["3D", "2D Timelapse", "2D Summary"], horizontal=True, label_visibility="collapsed")
    if view == "3D":
        wide = max(bbox[2] - bbox[0], bbox[3] - bbox[1]) > 1.5
        cell_km = bar[1].selectbox("Square size", [1, 2, 5, 10], index=2 if wide else 1, label_visibility="collapsed",
                                   format_func=lambda km: f"{km} km squares")
        add_up = bar[2].toggle("Add up through the period")
        orbit = bar[3].toggle("Rotate while it plays")
    # The 3D view keeps its height even with nothing to show, so the controls under it stay where they are.
    stage = st.container(height=TALL_3D + 16 if view == "3D" else "content", border=False)

    # The period: the whole record to start with. The timeline, the slider and the buttons all set it, month by month.
    timeline = st.container()   # drawn above the slider, but it needs the slider's months
    first, last = st.select_slider("Period", record, (record[0], record[-1]), key="months",
                                   format_func=lambda m: m.strftime("%b %Y"), label_visibility="collapsed")
    start, stop = max(first.start_time, FIRST), min(last.end_time.normalize(), end)
    if view != "2D Timelapse":  # the timelapse has the timeline in its own figure, so its playhead can move on it
        timeline.plotly_chart(animations.timeline(h.daily_index(d, k), start, stop), key="timeline", on_select=pick_period,
                              selection_mode="points", config={"displayModeBar": False})
    shown = start.year if start.year == stop.year else year     # the buttons follow the year the timeline is zoomed to
    picks = {"Whole record": (record[0], record[-1]), f"All of {shown}": (pd.Period(f"{shown}-01"), pd.Period(f"{shown}-12")),
             f"June to September {shown}": (pd.Period(f"{shown}-06"), pd.Period(f"{shown}-09")), charts.month_name(t): (t, t)}
    for column, (label, span) in zip(st.columns(len(picks)), picks.items()):
        column.button(label, on_click=pick_months, args=span, width="stretch",
                      disabled=span[1] < record[0] or span[0] > record[-1])
    n = h.in_box(rows(), bbox).day.between(start, stop).sum()
    st.caption(f"**{n:,} hotspot{'' if n == 1 else 's'}** in this area from {start:%d %b %Y} to {stop:%d %b %Y}. "
               "Click a year on the chart to zoom in to it, then click a month. For any other period, drag the "
               "ends of the slider or use a button.")

    if view == "2D Summary":
        points = h.in_box(rows(), bbox)
        points = points[points.day.between(start, stop)]
        sample = " (a sample of 20,000)" if len(points) > 20000 else ""
        title = f"Hotspots from {start:%d %b %Y} to {stop:%d %b %Y}{sample}"
        stage.caption("Scroll to zoom in. **Circle a region** with the mouse to open its burning calendar.")
        stage.plotly_chart(charts.hotspot_map(points, bbox, title), key="map", on_select=pick_on_map,
                           selection_mode=("lasso", "box"), config={"scrollZoom": True})
        if st.session_state.pop("open_region", False):
            region_calendar(st.session_state.region, t, colour, years)
        st.caption("The circled region's calendar counts every hotspot inside the line since 2000, whatever period "
                   "is shown. Double-click the map to zoom back out. To make a rectangle the app's area, pick Box "
                   "Select in the map's toolbar and drag. VIIRS has smaller pixels than MODIS, so it draws many "
                   "more dots for the same fire.")
    elif view == "2D Timelapse":
        stage.plotly_chart(timelapse_figure(bbox, start, stop), key="timeline", on_select=pick_period,
                           selection_mode="points", config={"displayModeBar": False, "scrollZoom": True})
        st.caption("Press Play. Scroll to zoom in, drag to move, and double-click to zoom back out. Coloured dots "
                   "are the hotspots of each step, and grey dots the three steps before. Busy steps show a sample "
                   "of the dots; the title counts every hotspot. VIIRS draws many more dots than MODIS for the "
                   "same fire. The upright line on the chart under the map shows where the timelapse has got to.")
        st.caption(f"Burn scars: a pale outline stays for 12 months around each big burnt patch, as in the 3D view. "
                   f"A patch is big when its squares, taken together, reach an activity of {animations.SCAR}. It "
                   "marks squares with hotspots, not a surveyed fire perimeter, and burning from before the period "
                   "shown leaves no outline.")
    else:
        page = columns_page(bbox, start, stop, cell_km, add_up, 50 if orbit else 0)
        if page is None:
            stage.info("No hotspots in this area and period.")
        else:
            html, top, cell_km, stretch = page
            stage.iframe(html, height=TALL_3D)
            what = ("Columns add up through the period, so they only rise" if add_up else
                    "Columns show the burning at each step, so they rise when a fire starts and drop when it is out")
            st.caption(f"Press Play. {what}. The upright line on the chart under the view shows where it has got to. "
                       f"Pause to rotate by dragging; scroll to zoom. Each column is a {cell_km} km square. "
                       f"Its height is the square root of its activity (hotspots per satellite, in VIIRS units); "
                       f"the tallest stands for {top:,.0f}. Heights are relative to the busiest square of this "
                       "period, so they cannot be compared between periods.")
            st.caption(f"Burn scars: a dark outline stays for 12 months around each big burnt patch, to show where a "
                       f"wildfire was after the columns drop. A patch is big when its squares, taken together, reach "
                       f"an activity of {animations.SCAR}; small and scattered burning gets no outline. It marks "
                       "squares with hotspots, not a surveyed fire perimeter, and burning from before the period "
                       "shown leaves no outline.")
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
   a factor measured on 2012 to 2021, when both flew and the MODIS orbits were still steady (it ranged from
   {k_by_year.min():.1f} to {k_by_year.max():.1f} by year).
3. **Rank, not count.** Each month is ranked against the same calendar month in other years, in five classes.
   Each summer (June to September) is ranked the same way against the other summers.
""")
    left, right = st.columns(2)
    left.plotly_chart(charts.adding_satellites(c), config={"displayModeBar": False})
    left.caption("Adding every hotspot together makes recent years look far busier, only because more satellites "
                 "are flying. The per-satellite index removes that.")
    o = c.loc[h.OVERLAP[0]:h.OVERLAP[1]].dropna(subset=["rate_modis", "rate_viirs"])
    within = (np.abs(np.log2((o.rate_viirs + 1) / (k * o.rate_modis + 1))) <= 1).mean()
    right.plotly_chart(charts.sensor_check(c, k), config={"displayModeBar": False})
    right.caption(f"Each dot is a month from 2012 to 2025, when both sensors flew. In this area {within:.0%} of months "
                  "agree within a factor of 2. The factor was measured on 2012 to 2021, so 2022 to 2025 test it on "
                  "years it was not fitted on.")
    st.markdown("""
**What to keep in mind**

- Hotspots are detections, not hectares burned. One large fire can give thousands of hotspots.
- Values before February 2012 are scaled from MODIS and are good to about a factor of 2.
- MODIS misses most small burns outside the fire season. From October to April, months since 2012 are ranked against
  2012 onward only, and earlier months against MODIS years only.
- Months since August 2026 use provisional near-real-time data and may change.
- Dates are in Pacific time (UTC-7), as in Kamloops, not the UTC dates in the FIRMS files.
- Small areas have few hotspots, so many months cannot be ranked. A whole summer usually can: in a test on
  areas about 100 km across, almost every summer could be ranked, against about 6 in 10 single summer months.
- Colours: brighter means more burning, on every chart and map. Blue marks below normal and amber above. The colours
  were chosen to stay distinct with colour-blind vision.
- Low-confidence detections and one fixed industrial heat source west of Kamloops are removed.
""")

with download_tab:
    dates = st.date_input("Date range", (start.date(), stop.date()), min_value=FIRST.date(), max_value=end.date())
    if len(dates) == 2:
        a, b = dates
        n = h.in_box(rows(), bbox).day.between(pd.Timestamp(a), pd.Timestamp(b)).sum()
        st.write(f"**{n:,} hotspot{'' if n == 1 else 's'}** in {area} from {a:%d %b %Y} to {b:%d %b %Y}, after quality filters.")
        st.download_button("Download hotspots (CSV)", lambda: h.raw_hotspots(bbox, a, b).to_csv(index=False),
                           file_name=f"hotspots_{a}_{b}.csv", mime="text/csv")
        st.caption("The file has every FIRMS column, unfiltered, so it can hold a few more rows than the count above. "
                   "Its acq_date and acq_time are UTC, as FIRMS gives them; local_date is the Pacific date (UTC-7) "
                   "used here. Long ranges over a large area take a few seconds. The dates start as the period "
                   "chosen on the Map tab.")
    st.download_button("Download the monthly index (CSV)", c.to_csv(index_label="month"),
                       file_name="monthly_index.csv", mime="text/csv")
