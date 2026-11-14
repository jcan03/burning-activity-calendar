"""Behaviour tests for the calendar, the animations and the app.

Run:  python -m unittest -v
Needs data/kamloops.sqlite; the terrain tests also need the files from download_basemap.py.

Expected values are recomputed here from the cached data by a different route (plain SQL or
arithmetic), not stored, so the tests keep passing when the cache is refreshed.
"""
import json
import re
import sqlite3
import unittest

import numpy as np
import pandas as pd
from streamlit.testing.v1 import AppTest

import animations
import charts
import harmonize as h

APP = str(h.DB.parent.parent / "app.py")
KAMLOOPS = (50.22, -121.04, 51.12, -119.62)
OKANAGAN = (49.0, -119.9, 50.8, -118.5)      # does not contain the masked static site
EMPTY = (49.0, -118.2, 49.02, -118.19)
T = pd.Timestamp
FIRST, SUMMER_2021 = T("2000-11-01"), (T("2021-06-01"), T("2021-09-30"))


def page_data(html):
    """The data block that the 3D page's script plays from."""
    return json.loads(re.search(r"const D = (\{.*?\}), plot = document", html, re.S).group(1))


@unittest.skipUnless(h.DB.exists(), "needs data/kamloops.sqlite")
class WithData(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows = h.load_rows()
        cls.end = cls.rows.day.max()
        cls.daily = h.daily(cls.rows, h.BOX)
        cls.k, cls.k_by_year = h.fit_k(h.monthly_rates(cls.daily))
        cls.calendar = h.calendar_table(h.monthly_rates(cls.daily), cls.k)
        cls.points = cls.rows.assign(w=h.weights(cls.rows, cls.k))


class Harmonize(WithData):
    def test_filters_keep_the_documented_rows(self):
        con = sqlite3.connect(f"file:{h.DB.as_posix()}?mode=ro", uri=True)
        raw = pd.read_sql_query("SELECT latitude, longitude, instrument, confidence, type FROM hotspots", con)
        con.close()
        low = np.where(raw.instrument == "MODIS", pd.to_numeric(raw.confidence, errors="coerce") < 30, raw.confidence == "l")
        lat, lon, lat0, lon0 = (np.radians(v) for v in (raw.latitude, raw.longitude, *h.STATIC_SITE))
        km = 2 * 6371 * np.arcsin(np.sqrt(np.sin((lat - lat0) / 2) ** 2 + np.cos(lat0) * np.cos(lat) * np.sin((lon - lon0) / 2) ** 2))
        self.assertEqual(len(self.rows), int((~raw.type.isin([1, 2]) & ~low & (km > 0.4)).sum()))

    def test_monthly_counts_match_plain_sql(self):
        south, west, north, east = OKANAGAN
        con = sqlite3.connect(f"file:{h.DB.as_posix()}?mode=ro", uri=True)
        counted = dict(con.execute(
            "SELECT instrument, COUNT(*) FROM hotspots WHERE acq_date BETWEEN '2021-07-01' AND '2021-07-31' "
            "AND latitude BETWEEN ? AND ? AND longitude BETWEEN ? AND ? AND (type IS NULL OR type NOT IN (1, 2)) "
            "AND ((instrument = 'MODIS' AND CAST(confidence AS INTEGER) >= 30) OR (instrument = 'VIIRS' AND confidence <> 'l')) "
            "GROUP BY instrument", (south, north, west, east)).fetchall())
        con.close()
        july = h.daily(self.rows, OKANAGAN).loc["2021-07"]
        self.assertEqual((july.count_modis.sum(), july.count_viirs.sum()), (counted["MODIS"], counted["VIIRS"]))

    def test_index_is_hotspots_per_satellite_per_30_days(self):
        july = self.calendar.loc["2021-07"]             # Suomi NPP and NOAA-20 flew all 31 days
        self.assertAlmostEqual(july["index"], 30 * july.count_viirs / (2 * 31))
        early = self.calendar.loc["2005-08"]            # Terra and Aqua, scaled by k
        self.assertAlmostEqual(early["index"], self.k * 30 * early.count_modis / (2 * 31))

    def test_k_is_the_ratio_over_the_overlap(self):
        overlap = self.calendar.loc[h.OVERLAP[0]:h.OVERLAP[1]]
        self.assertAlmostEqual(self.k, overlap.rate_viirs.sum() / overlap.rate_modis.sum())
        self.assertTrue(5 < self.k < 12 and self.k_by_year.min() < self.k < self.k_by_year.max())

    def test_hotspot_weights_add_up_to_the_daily_index(self):
        for bbox in (h.BOX, KAMLOOPS):
            index = h.daily_index(h.daily(self.rows, bbox), self.k)
            inside = h.in_box(self.points, bbox)
            for month in ("2003-08", "2012-01", "2012-02", "2021-07", "2022-08"):   # both sides of the splice; an outage
                weights = inside.w[inside.day.dt.strftime("%Y-%m") == month].sum()
                self.assertAlmostEqual(weights, index.loc[month].sum(), places=6, msg=f"{month} {bbox}")

    def test_percentile_of_a_month_by_hand(self):
        row, index = self.calendar.loc["2021-07"], self.calendar["index"]
        others = index[(index.index.month == 7) & (index.index.year >= 2001) & (index.index.year <= 2025) & (index.index.year != 2021)]
        self.assertAlmostEqual(row.pct, ((others < row["index"]).sum() + 0.5 * (others == row["index"]).sum()) / len(others))
        self.assertEqual((row["rank"], row.n_years), (1 + (others > row["index"]).sum(), len(others) + 1))

    def test_ranks_and_classes_are_consistent(self):
        ranked = self.calendar[self.calendar.cls.notna()]
        self.assertTrue(ranked.pct.between(0, 1).all())
        self.assertTrue((ranked.cls == np.minimum((ranked.pct * 5).astype(int), 4)).all())
        self.assertTrue((ranked["rank"].between(1, ranked.n_years)).all())
        self.assertTrue((ranked[ranked.record]["rank"] == 1).all())
        self.assertFalse((ranked.uncertain).any())

    def test_flags_mark_the_right_months(self):
        c = self.calendar
        self.assertEqual(c.index[c.modis_scaled].max(), pd.Period("2012-01"))
        self.assertEqual(c.index[c.terra_only].max(), pd.Period("2002-06"))
        self.assertEqual(c.index[c.nrt].min(), self.rows.day[self.rows.nrt].min().to_period("M"))
        self.assertEqual(list(c.index[c.partial]), [self.end.to_period("M")] if self.end.day < self.end.days_in_month else [])

    def test_a_smaller_area_never_has_more_hotspots(self):
        small, whole = h.daily(self.rows, KAMLOOPS), self.daily
        self.assertTrue((small.count_viirs <= whole.count_viirs).all() and (small.count_modis <= whole.count_modis).all())
        self.assertEqual(h.daily(self.rows, EMPTY)[["count_modis", "count_viirs"]].to_numpy().sum(), 0)


class Animations(WithData):
    def test_steps_put_every_day_in_one_frame_in_order(self):
        for start, stop in [("2021-08-10", "2021-08-10"), ("2021-08-01", "2021-08-31"), ("2021-06-01", "2021-09-30"),
                            ("2020-01-01", "2020-12-31"), ("2021-03-15", "2023-11-20"), ("2000-11-01", str(self.end.date()))]:
            days = pd.Series(pd.date_range(start, stop))
            frame, labels = animations.steps(days, T(start), T(stop))
            self.assertEqual((frame.min(), frame.max(), frame.nunique()), (0, len(labels) - 1, len(labels)), msg=f"{start} to {stop}")
            self.assertTrue(frame.is_monotonic_increasing)

    def test_a_long_period_plays_month_by_month(self):
        days = pd.Series(pd.date_range(FIRST, self.end))
        frame, labels = animations.steps(days, FIRST, self.end)
        self.assertEqual(len(labels), len(pd.period_range(FIRST, self.end, freq="M")))
        self.assertEqual(labels[frame[days == T("2021-07-15")].iloc[0]], "July 2021")

    def test_timelapse_counts_every_hotspot(self):
        for bbox, (start, stop) in [(KAMLOOPS, SUMMER_2021), (h.BOX, (FIRST, self.end)), (EMPTY, SUMMER_2021)]:
            fig = animations.timelapse(self.rows, bbox, start, stop)
            inside = h.in_box(self.rows, bbox)
            total = int(inside.day.between(start, stop).sum())
            so_far = int(re.search(r"([\d,]+) so far", fig.frames[-1].layout.title.text).group(1).replace(",", ""))
            self.assertEqual(so_far, total)
            self.assertTrue(all(len(f.data[1].x) + len(f.data[2].x) <= 1000 for f in fig.frames))

    def test_3d_columns_hold_all_the_activity(self):
        start, stop = SUMMER_2021
        inside = h.in_box(self.points, KAMLOOPS)
        total = inside.w[inside.day.between(start, stop)].sum()
        for add_up in (False, True):
            html, top, cell_km, stretch = animations.columns_3d(self.points, KAMLOOPS, start, stop, 2, add_up)
            d = page_data(html)
            frames = [dict(zip(f[::2], f[1::2])) for f in d["heights"]]
            self.assertEqual(len(frames), len(d["dates"]))
            self.assertLessEqual(max(max(f.values(), default=0) for f in frames), d["top"] + 0.01)
            activity = [sum((height / d["top"]) ** 2 * top for height in f.values()) for f in frames]   # undo the square root
            self.assertAlmostEqual((activity[-1] if add_up else sum(activity)) / total, 1, delta=0.02)
            if add_up:
                self.assertTrue(all(later.get(square, 0) >= height - 0.01 for earlier, later in zip(frames, frames[1:])
                                    for square, height in earlier.items()))

    def test_3d_columns_stand_inside_the_area_on_the_ground(self):
        html, top, cell_km, stretch = animations.columns_3d(self.points, KAMLOOPS, FIRST, self.end, 2)
        d = {name: np.array(d) for name, d in page_data(html).items() if name in ("x0", "x1", "y0", "y1", "foot", "base")}
        self.assertTrue((d["x0"] >= 0).all() and (d["y0"] >= 0).all() and (d["x1"] > d["x0"]).all() and (d["y1"] > d["y0"]).all())
        self.assertTrue((d["foot"] <= d["base"] + 1e-9).all())

    def test_3d_squares_widen_when_there_are_too_many(self):
        html, top, cell_km, stretch = animations.columns_3d(self.points, h.BOX, FIRST, self.end, 2)
        self.assertGreater(cell_km, 2)
        self.assertLessEqual(len(page_data(html)["x0"]), 6000)

    def test_3d_with_no_hotspots_is_none(self):
        self.assertIsNone(animations.columns_3d(self.points, EMPTY, *SUMMER_2021, 2))


@unittest.skipUnless(charts.TERRAIN.exists() and charts.BASEMAP.exists(), "needs the files from download_basemap.py")
class Terrain(WithData):
    def at(self, grid, lat, lon, bbox):
        """The grid's value at places; the grid covers bbox with its south row first."""
        south, west, north, east = bbox
        row = np.round((np.asarray(lat) - south) / (north - south) * (grid.shape[0] - 1)).astype(int)
        col = np.round((np.asarray(lon) - west) / (east - west) * (grid.shape[1] - 1)).astype(int)
        return grid[row, col]

    def test_ground_is_the_right_way_up(self):
        elevation, water = charts.relief(KAMLOOPS, 180)
        self.assertTrue(300 < self.at(elevation, 50.6745, -120.3273, KAMLOOPS) < 450)      # Kamloops, in the valley
        self.assertTrue(self.at(elevation, 50.884, -119.886, KAMLOOPS) > 1000)             # Sun Peaks village
        self.assertTrue(self.at(water, 50.754, -120.70, KAMLOOPS))                          # the middle of Kamloops Lake
        self.assertFalse(self.at(water, 50.6745, -120.3273, KAMLOOPS))                      # the city is not

    def test_hotspots_fall_on_land(self):
        # If the ground were flipped or shifted, fires would land on lakes as often as anywhere else.
        elevation, water = charts.relief(h.BOX, 1800)
        on_water = self.at(water, self.rows.lat.to_numpy(), self.rows.lon.to_numpy(), h.BOX)
        self.assertLess(on_water.mean(), water.mean() / 3)

    def test_flat_map_picture_matches_the_area(self):
        picture = charts.terrain(KAMLOOPS, 1000)
        self.assertEqual(max(picture.size), 1000)
        south, west, north, east = KAMLOOPS
        self.assertAlmostEqual(picture.size[0] / picture.size[1], (east - west) / (north - south), delta=0.02)

    def test_3d_still_works_without_terrain(self):
        real = charts.TERRAIN
        charts.TERRAIN = real.with_name("missing.npz")
        charts._terrain.cache_clear()
        try:
            self.assertIsNone(charts.relief(KAMLOOPS, 180))
            self.assertIsNone(animations.columns_3d(self.points, KAMLOOPS, *SUMMER_2021, 2)[3])
        finally:
            charts.TERRAIN = real
            charts._terrain.cache_clear()


@unittest.skipUnless(h.DB.exists(), "needs data/kamloops.sqlite")
class App(unittest.TestCase):
    def run_app(self):
        at = AppTest.from_file(APP, default_timeout=180).run()
        self.assertFalse(at.exception, msg=[str(e.value) for e in at.exception])
        return at

    def choose(self, at, view=None, button=None, **selectboxes):
        for key, value in selectboxes.items():
            at.selectbox(key=key).set_value(value)
        if selectboxes:
            at.run()        # the buttons are named after the month in focus
        if button:
            [b for b in at.button if b.label.startswith(button)][0].click()
        if view:
            [r for r in at.radio if r.label == "View"][0].set_value(view)
        at.run()
        self.assertFalse(at.exception, msg=[str(e.value) for e in at.exception])
        return at

    def test_opens_on_the_kamloops_area_and_the_whole_record(self):
        at = self.run_app()
        self.assertEqual(at.subheader[0].value, "Kamloops area")
        self.assertEqual([t.label for t in at.tabs], ["Calendar", "Season and daily", "Map", "Method", "Download"])
        first, last = at.select_slider(key="months").value
        self.assertEqual((str(first), last), ("2000-11", h.load_rows().day.max().to_period("M")))

    def test_every_view_draws_for_every_kind_of_period(self):
        at = self.run_app()
        for button in ("Whole record", "All of", "June to September"):
            for view in ("Map", "Timelapse", "3D"):
                self.choose(at, view=view, button=button, year=2021, month=8)

    def test_every_area_draws(self):
        at = self.run_app()
        for area in ("Okanagan Valley", "Shuswap", "Nicola Valley", "Fraser Canyon", "South Cariboo", "Southern Interior BC (all data)"):
            self.choose(at, view="3D", area=area)

    def test_headline_agrees_with_the_calendar(self):
        at = self.choose(self.run_app(), year=2021, month=7, area="Southern Interior BC (all data)")
        rows = h.load_rows()
        k = h.fit_k(h.monthly_rates(h.daily(rows, h.BOX)))[0]
        july = h.calendar_table(h.monthly_rates(h.daily(rows, h.BOX)), k).loc["2021-07"]
        metrics = {m.label: m.value for m in at.metric}
        self.assertEqual(metrics["Index"], f"{july['index']:,.0f}")
        self.assertEqual(metrics["Rank among Julys"], f"{july['rank']:.0f} of {july.n_years:.0f}")
        self.assertIn("busiest July on record", at.markdown[0].value)

    def test_a_month_outside_the_record_says_so(self):
        at = self.choose(self.run_app(), year=2000, month=3)
        self.assertTrue(any("no data for March 2000" in i.value for i in at.info))

    def test_an_upside_down_box_is_refused(self):
        at = self.choose(self.run_app(), area="Custom box")
        at.number_input(key="south").set_value(51.0)
        at.number_input(key="north").set_value(50.0)
        at.run()
        self.assertTrue(any("South must be below north" in e.value for e in at.error))

    def test_an_empty_area_says_so(self):
        at = self.choose(self.run_app(), area="Custom box")
        for key, value in zip(("south", "west", "north", "east"), EMPTY):
            at.number_input(key=key).set_value(value)
        at.run()
        self.assertFalse(at.exception)
        self.assertTrue(any("No hotspots" in w.value for w in at.warning))

    def test_without_the_database_it_explains_how_to_build_it(self):
        real = h.DB
        h.DB = real.with_name("missing.sqlite")
        try:
            at = AppTest.from_file(APP, default_timeout=60).run()
        finally:
            h.DB = real
        self.assertTrue(any("download_kamloops.py" in e.value for e in at.error))


if __name__ == "__main__":
    unittest.main()
