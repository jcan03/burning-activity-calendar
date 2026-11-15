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


def pacific_day(acq_date, acq_time):
    """The Pacific day (UTC-7) of FIRMS dates and times: anything before 07:00 UTC belongs to the day before."""
    return pd.to_datetime(acq_date) - pd.to_timedelta((acq_time < "0700").astype(int), unit="D")


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
        raw = pd.read_sql_query("SELECT latitude, longitude, acq_date, acq_time, instrument, confidence, type FROM hotspots", con)
        con.close()
        low = np.where(raw.instrument == "MODIS", pd.to_numeric(raw.confidence, errors="coerce") < 30, raw.confidence == "l")
        lat, lon, lat0, lon0 = (np.radians(v) for v in (raw.latitude, raw.longitude, *h.STATIC_SITE))
        km = 2 * 6371 * np.arcsin(np.sqrt(np.sin((lat - lat0) / 2) ** 2 + np.cos(lat0) * np.cos(lat) * np.sin((lon - lon0) / 2) ** 2))
        day = pacific_day(raw.acq_date, raw.acq_time)
        kept = ~raw.type.isin([1, 2]) & ~low & (km > 0.4) & (day >= FIRST) & (day < day.max())
        self.assertEqual(len(self.rows), int(kept.sum()))

    def okanagan_sql(self, first, last):
        """MODIS and VIIRS hotspots kept in the Okanagan between two UTC times, each written as acq_date then acq_time."""
        south, west, north, east = OKANAGAN
        con = sqlite3.connect(f"file:{h.DB.as_posix()}?mode=ro", uri=True)
        counted = dict(con.execute(
            "SELECT instrument, COUNT(*) FROM hotspots WHERE acq_date || acq_time >= ? AND acq_date || acq_time < ? "
            "AND latitude BETWEEN ? AND ? AND longitude BETWEEN ? AND ? AND (type IS NULL OR type NOT IN (1, 2)) "
            "AND ((instrument = 'MODIS' AND CAST(confidence AS INTEGER) >= 30) OR (instrument = 'VIIRS' AND confidence <> 'l')) "
            "GROUP BY instrument", (first, last, south, north, west, east)).fetchall())
        con.close()
        return counted.get("MODIS", 0), counted.get("VIIRS", 0)

    def test_monthly_counts_match_plain_sql(self):
        july = h.daily(self.rows, OKANAGAN).loc["2021-07"]       # a Pacific month runs from 07:00 UTC on the 1st
        self.assertEqual((july.count_modis.sum(), july.count_viirs.sum()), self.okanagan_sql("2021-07-010700", "2021-08-010700"))

    def test_days_are_pacific_days(self):
        day = h.daily(self.rows, OKANAGAN).loc["2021-08-05"]
        self.assertEqual((day.count_modis, day.count_viirs), self.okanagan_sql("2021-08-050700", "2021-08-060700"))
        # Terra passes late in the evening, which is already 6 August in UTC. Those hotspots belong to 5 August.
        self.assertGreater(self.okanagan_sql("2021-08-060000", "2021-08-060700")[0], 100)

    def test_the_csv_download_is_cut_by_pacific_days(self):
        raw = h.raw_hotspots(OKANAGAN, "2021-08-05", "2021-08-06")
        self.assertEqual(sorted(raw.local_date.unique()), ["2021-08-05", "2021-08-06"])
        self.assertTrue((pacific_day(raw.acq_date, raw.acq_time).dt.strftime("%Y-%m-%d") == raw.local_date).all())
        con = sqlite3.connect(f"file:{h.DB.as_posix()}?mode=ro", uri=True)
        counted = con.execute(
            "SELECT COUNT(*) FROM hotspots WHERE acq_date || acq_time >= '2021-08-050700' AND acq_date || acq_time < '2021-08-070700' "
            "AND latitude BETWEEN ? AND ? AND longitude BETWEEN ? AND ?", (OKANAGAN[0], OKANAGAN[2], OKANAGAN[1], OKANAGAN[3])).fetchone()[0]
        con.close()
        self.assertEqual(len(raw), counted)

    def test_index_is_hotspots_per_satellite_per_30_days(self):
        july = self.calendar.loc["2021-07"]             # Suomi NPP and NOAA-20 flew all 31 days
        self.assertAlmostEqual(july["index"], 30 * july.count_viirs / (2 * 31))
        early = self.calendar.loc["2005-08"]            # Terra and Aqua, scaled by k
        self.assertAlmostEqual(early["index"], self.k * 30 * early.count_modis / (2 * 31))

    def test_k_is_the_ratio_over_the_stable_orbit_years(self):
        stable = self.calendar.loc["2012-02":"2021-12"]     # both sensors flying, before the MODIS orbits drifted
        self.assertAlmostEqual(self.k, stable.rate_viirs.sum() / stable.rate_modis.sum())
        self.assertTrue(5 < self.k < 12 and self.k_by_year.min() < self.k < self.k_by_year.max())
        self.assertEqual((self.k_by_year.index.min(), self.k_by_year.index.max()), (2012, 2021))

    def test_modis_after_its_orbits_drifted_does_not_move_k(self):
        drifted = h.monthly_rates(self.daily)
        drifted.loc["2022-01":, "rate_modis"] *= 0.5        # as if MODIS lost half its detections from 2022
        self.assertEqual(h.fit_k(drifted)[0], self.k)

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

    def test_a_circled_region_counts_only_what_is_inside(self):
        # A five-sided outline with its corners in anticlockwise order: a point is inside if it is left of every side.
        shape = [(-120.913, 50.3117), (-119.8731, 50.2771), (-119.7219, 50.9133), (-120.4127, 51.0619), (-121.0033, 50.7411)]
        left = np.ones(len(self.rows), bool)
        for (x0, y0), (x1, y1) in zip(shape, shape[1:] + shape[:1]):
            left &= ((x1 - x0) * (self.rows.lat - y0) - (y1 - y0) * (self.rows.lon - x0) > 0).to_numpy()
        inside = h.in_shape(self.rows, shape)
        self.assertEqual(len(inside), int(left.sum()))
        self.assertGreater(len(inside), 10000)
        self.assertEqual(len(h.in_shape(self.rows, shape[::-1])), len(inside))       # drawn the other way round
        counted = h.daily(self.rows, h.BOX, shape)
        self.assertEqual(counted.count_modis.sum() + counted.count_viirs.sum(), len(inside))
        self.assertEqual(len(counted), len(self.daily))                              # still the whole record

    def test_a_month_too_tied_to_place_gets_no_rank(self):
        c = h.calendar_table(h.monthly_rates(h.daily(self.rows, OKANAGAN)), self.k)
        self.assertTrue(c.uncertain.any())
        self.assertTrue(c[c.uncertain][["rank", "cls"]].isna().all().all())

    def test_off_season_months_are_ranked_against_viirs_months_only(self):
        january = self.calendar.loc["2020-01"]      # January 2012 still came from MODIS, so the baseline starts in 2013
        self.assertEqual((january.since, january.n_years), (2013, 13))
        november = self.calendar.loc["2020-11"]
        self.assertEqual((november.since, november.n_years), (2012, 14))
        self.assertEqual(self.calendar.loc["2020-07", "since"], 2001)

    def test_summer_index_is_the_mean_of_june_to_september(self):
        summers, months = h.summer_table(self.calendar), self.calendar["index"]
        for year in (2005, 2021):                           # scaled from MODIS; from VIIRS
            self.assertAlmostEqual(summers.loc[year, "index"], months.loc[f"{year}-06":f"{year}-09"].mean())
        self.assertEqual((bool(summers.loc[2011, "modis_scaled"]), bool(summers.loc[2012, "modis_scaled"])), (True, False))

    def test_rank_of_a_summer_by_hand(self):
        summers = h.summer_table(self.calendar)
        row, index = summers.loc[2017], summers["index"]
        others = index[(index.index >= 2001) & (index.index <= 2025) & (index.index != 2017)]
        self.assertAlmostEqual(row.pct, ((others < row["index"]).sum() + 0.5 * (others == row["index"]).sum()) / len(others))
        self.assertEqual((row["rank"], row.n_years, row.since), (1 + (others > row["index"]).sum(), len(others) + 1, 2001))
        self.assertEqual(row.cls, min(int(row.pct * 5), 4))

    def test_the_biggest_fire_season_is_the_record_summer(self):
        best = h.summer_table(self.calendar).loc[2021]      # 2021 burned more of this area than any other year on record
        self.assertEqual((best["rank"], best.cls, bool(best.record)), (1, 4, True))

    def test_a_small_area_can_rank_every_summer_but_not_every_month(self):
        c = h.calendar_table(h.monthly_rates(h.daily(self.rows, KAMLOOPS)), self.k)
        months = c[c.index.month.isin([6, 7, 8, 9])].loc["2001":"2025"]
        self.assertTrue(months.cls.isna().any())
        self.assertTrue(h.summer_table(c).loc[2001:2025].cls.notna().all())

    def test_summers_that_all_tie_are_not_ranked(self):
        c = h.calendar_table(h.monthly_rates(h.daily(self.rows, EMPTY)), self.k)
        summers = h.summer_table(c).loc[2001:2025]
        self.assertTrue(summers.uncertain.all() and summers.cls.isna().all())

    def test_an_unfinished_summer_is_not_rated(self):
        to_august = h.summer_table(self.calendar.loc[:"2025-08"])       # as if the record stopped at the end of August 2025
        self.assertTrue(np.isnan(to_august.loc[2025, "index"]) and np.isnan(to_august.loc[2025, "cls"]))
        under_way = self.calendar.copy()
        under_way.loc["2025-09", "partial"] = True                      # as if September 2025 were not over
        self.assertTrue(np.isnan(h.summer_table(under_way).loc[2025, "index"]))
        self.assertFalse(np.isnan(h.summer_table(self.calendar).loc[2025, "index"]))

    def test_outage_days_do_not_count_as_flying(self):
        self.assertEqual(self.daily.loc["2026-07-12", "sats_viirs"], 2)     # Suomi NPP out; NOAA-20 and NOAA-21 flying
        self.assertEqual(self.daily.loc["2001-06-20", "sats_modis"], 0)     # Terra, then the only satellite, was out
        self.assertEqual(self.daily.loc["2022-10-15", "sats_modis"], 1)

    def test_days_with_no_scene_do_not_count_as_flying(self):
        # NASA's scene catalogue has nothing from these satellites on these days, and neither has FIRMS.
        self.assertEqual(self.daily.loc["2024-07-12", "sats_viirs"], 2)     # Suomi NPP: 10-15 and 24-28 July 2024
        self.assertEqual(self.daily.loc["2023-07-20", "sats_viirs"], 2)     # NOAA-20: 19-22 July 2023
        self.assertEqual(self.daily.loc["2026-03-06", "sats_modis"], 1)     # Terra: 4-9 March 2026
        self.assertEqual(self.daily.loc["2002-08-03", "sats_modis"], 1)     # Aqua: 30 July to 7 August 2002

    def test_a_month_with_lost_days_is_divided_by_the_days_flown(self):
        july = self.calendar.loc["2024-07"]             # three satellites, less the 11 days Suomi NPP lost
        self.assertAlmostEqual(july["index"], 30 * july.count_viirs / (3 * 31 - 11))

    def test_no_viirs_satellite_counted_as_flying_is_silent_on_a_busy_day(self):
        counts = self.rows[self.rows.sat.isin(h.VIIRS)].groupby(["day", "sat"], observed=True).size().unstack(fill_value=0)
        counts = counts.reindex(index=self.daily.index, columns=h.VIIRS, fill_value=0)
        in_service = pd.DataFrame({s: (counts.index >= h.SERVICE[s][0]) & (counts.index <= (h.SERVICE[s][1] or self.end))
                                   for s in h.VIIRS}, index=counts.index)
        no_outage = self.daily.sats_viirs == in_service.sum(axis=1)
        busy = counts.sum(axis=1) >= 300
        silent = ((counts == 0) & in_service).any(axis=1)
        self.assertEqual(list(counts.index[no_outage & busy & silent].strftime("%Y-%m-%d")), [])

    def test_part_days_at_both_ends_are_left_out(self):
        con = sqlite3.connect(f"file:{h.DB.as_posix()}?mode=ro", uri=True)
        last = con.execute("SELECT MAX(acq_date || acq_time) FROM hotspots").fetchone()[0]
        con.close()
        downloaded = pd.to_datetime(last, format="%Y-%m-%d%H%M") - pd.Timedelta(hours=7)     # in Pacific time
        self.assertEqual(self.end, downloaded.normalize() - pd.Timedelta(days=1))
        self.assertGreaterEqual(self.rows.day.min(), FIRST)      # the evening of 31 October 2000 is not a whole day


class Calendar(WithData):
    def summer_squares(self, view, c=None):
        """The calendar figure and the value drawn in each year's summer square."""
        fig = charts.calendar(self.calendar if c is None else c, view, pd.Period("2021-07"), (2000, self.end.year))
        [squares] = [t for t in fig.data if t.type == "heatmap" and t.name == "Summer"]
        return fig, dict(zip(squares.y, np.asarray(squares.z, dtype=float)[:, 0]))

    def test_each_summer_has_a_square_in_the_colour_of_its_class(self):
        fig, squares = self.summer_squares("class")
        self.assertEqual(squares[2021], 4)                          # the record summer: much above normal
        self.assertEqual(squares[2017], h.summer_table(self.calendar).loc[2017, "cls"])
        self.assertTrue(np.isnan(squares[2000]))                    # the record starts in November 2000
        self.assertEqual(fig.layout.xaxis.ticktext[-1], "Summer")   # after December

    def test_summer_squares_use_the_months_colour_scale(self):
        _, squares = self.summer_squares("index")
        self.assertAlmostEqual(squares[2021], np.log10(self.calendar["index"].loc["2021-06":"2021-09"].mean() + 1))

    def test_a_summer_that_cannot_be_ranked_is_marked_so(self):
        c = h.calendar_table(h.monthly_rates(h.daily(self.rows, EMPTY)), self.k)
        self.assertEqual(self.summer_squares("class", c)[1][2010], 5)       # 5 is "Cannot be ranked", as for a month

    def test_pointing_at_a_summer_square_gives_its_rank(self):
        fig, _ = self.summer_squares("class")
        texts = [text for t in fig.data if t.hovertext is not None for text in t.hovertext if "Summer 2021" in text]
        self.assertEqual(len(texts), 1)
        self.assertIn("Much above normal (record): rank 1 of 25", texts[0])

    def test_clicking_a_summer_square_picks_its_busiest_month(self):
        fig, _ = self.summer_squares("class")
        picks = {y: m for t in fig.data if t.customdata is not None for x, y, m in zip(t.x, t.y, t.customdata) if x > 12.5}
        self.assertEqual(picks[2021], "2021-07")                    # July 2021 is the busiest month on record
        busiest_2003 = self.calendar["index"].loc["2003-06":"2003-09"].idxmax()
        self.assertEqual(picks[2003], str(busiest_2003))


class Animations(WithData):
    def test_steps_put_every_day_in_one_frame_in_order(self):
        for start, stop in [("2021-08-10", "2021-08-10"), ("2021-08-01", "2021-08-31"), ("2021-06-01", "2021-09-30"),
                            ("2020-01-01", "2020-12-31"), ("2021-03-15", "2023-11-20"), ("2000-11-01", str(self.end.date()))]:
            days = pd.Series(pd.date_range(start, stop))
            frame, labels = animations.steps(days, T(start), T(stop))
            self.assertEqual((frame.min(), frame.max(), frame.nunique()), (0, len(labels) - 1, len(labels)), msg=f"{start} to {stop}")
            self.assertTrue(frame.is_monotonic_increasing)
        days = pd.Series(pd.date_range("2023-01-01", "2023-09-06"))        # 2-day frames, with one day left over
        self.assertEqual(animations.steps(days, T("2023-01-01"), T("2023-09-06"))[1][-2:], ["04 Sep to 05 Sep 2023", "06 Sep 2023"])

    def test_a_long_period_plays_month_by_month(self):
        days = pd.Series(pd.date_range(FIRST, self.end))
        frame, labels = animations.steps(days, FIRST, self.end)
        self.assertEqual(len(labels), len(pd.period_range(FIRST, self.end, freq="M")))
        self.assertEqual(labels[frame[days == T("2021-07-15")].iloc[0]], "July 2021")

    def test_timeline_zooms_from_years_to_months(self):
        index = h.daily_index(self.daily, self.k)
        years = animations.timeline(index, FIRST, self.end).data[1]             # the layer that takes the click
        self.assertEqual((years.customdata[0], years.customdata[-1]), ("2000-01 2000-12", f"{self.end.year}-01 {self.end.year}-12"))
        for start, stop in [("2021-01-01", "2021-12-31"), ("2021-07-01", "2021-07-31")]:    # a month shown: the year stays up
            months = animations.timeline(index, T(start), T(stop)).data[1]
            self.assertEqual(list(months.customdata), [f"2021-{m:02d} 2021-{m:02d}" for m in range(1, 13)])

    def timelapse(self, bbox, start, stop, points=None):
        index = h.daily_index(h.daily(self.rows, bbox), self.k)
        return animations.timelapse(self.points if points is None else points, bbox, start, stop, index)

    def test_timelapse_counts_every_hotspot(self):
        for bbox, (start, stop) in [(KAMLOOPS, SUMMER_2021), (h.BOX, (FIRST, self.end)), (EMPTY, SUMMER_2021)]:
            fig = self.timelapse(bbox, start, stop)
            inside = h.in_box(self.rows, bbox)
            total = int(inside.day.between(start, stop).sum())
            so_far = int(re.search(r"([\d,]+) so far", fig.frames[-1].layout.title.text).group(1).replace(",", ""))
            self.assertEqual(so_far, total)
            self.assertTrue(all(len(f.data[1].x) + len(f.data[2].x) <= 1000 for f in fig.frames))

    def test_timelapse_playhead_marks_each_step_on_its_timeline(self):
        # Each frame's last trace is the playhead: an upright line on the timeline under the map.
        fig = self.timelapse(KAMLOOPS, *SUMMER_2021)                              # one frame a day
        clickable = [t for t in fig.data if t.customdata is not None][0]          # the timeline's layer that takes the click
        self.assertEqual(clickable.customdata[0], "2021-01 2021-01")              # zoomed to the year, as the period is in it
        self.assertEqual(fig.data[fig.frames[0].traces[-1]].xaxis, clickable.xaxis)
        self.assertNotEqual(clickable.xaxis, fig.data[1].xaxis)                   # not on the map
        heads = [f.data[-1].x for f in fig.frames]
        self.assertTrue(all(len(x) == 2 and x[0] == x[1] for x in heads))
        self.assertEqual([T(x[0]) for x in heads], list(pd.date_range(*SUMMER_2021)))
        self.assertEqual(T(fig.data[fig.frames[0].traces[-1]].x[0]), SUMMER_2021[0])   # before Play: at the first step
        whole = self.timelapse(KAMLOOPS, FIRST, self.end)                         # one frame a month
        self.assertEqual([T(f.data[-1].x[0]).strftime("%B %Y") for f in whole.frames], [f.name for f in whole.frames])

    def test_timelapse_outlines_big_burnt_patches_for_twelve_months(self):
        south, west, north, east = KAMLOOPS
        km_east = 111.2 * np.cos(np.radians((south + north) / 2))

        def fire(x, y, hotspots):
            """Hotspots of activity 1 each on 10 July 2021, at a place given in km from the area's south-west corner."""
            return pd.DataFrame({"lat": south + y / 111.2, "lon": west + x / km_east, "day": T("2021-07-10"),
                                 "sat": "N", "w": 1.0}, index=range(hotspots))

        # In this area's 2 km squares: one square that is big alone (150 is over SCAR), two touching squares that are
        # only big together (60 each), and a lone square that is too small (60).
        points = pd.concat([fire(21, 21, 150), fire(41, 21, 60), fire(43, 21, 60), fire(61, 61, 60)], ignore_index=True)
        fig = self.timelapse(KAMLOOPS, T("2019-01-01"), T("2023-12-31"), points)  # long enough to play month by month

        def outline_km(frame):
            lon, lat = (np.array(v, dtype=float) for v in (frame.data[3].x, frame.data[3].y))
            return np.nansum(np.hypot(np.diff(lon) * km_east, np.diff(lat) * 111.2))   # the gaps between lines are NaN

        length = {f.name: outline_km(f) for f in fig.frames}
        outlined = [name for name, km in length.items() if km > 0]
        self.assertEqual((outlined[0], outlined[-1], len(outlined)), ("July 2021", "June 2022", 12))
        # Once round the 2 km square (8 km) and once round the 2 km by 4 km pair (12 km), with no line between the pair.
        self.assertAlmostEqual(length["July 2021"], 20, delta=0.2)
        july = [f for f in fig.frames if f.name == "July 2021"][0]
        east_km = (np.array(july.data[3].x, dtype=float) - west) * km_east
        self.assertAlmostEqual(np.nanmin(east_km), 20, delta=0.1)
        self.assertAlmostEqual(np.nanmax(east_km), 44, delta=0.1)                 # nothing round the small square at 61 km

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
        south, west, north, east = KAMLOOPS
        wide, tall = (east - west) * 111.2 * np.cos(np.radians((south + north) / 2)), (north - south) * 111.2
        self.assertTrue((d["x0"] >= 0).all() and (d["y0"] >= 0).all() and (d["x1"] > d["x0"]).all() and (d["y1"] > d["y0"]).all())
        self.assertTrue((d["x1"] <= wide + 0.01).all() and (d["y1"] <= tall + 0.01).all())
        self.assertTrue((d["foot"] <= d["base"] + 1e-9).all())

    def test_3d_burn_scars_last_twelve_months(self):
        # The page's script outlines squares that burned in the last `keep` frames; it needs each square's grid place.
        whole = page_data(animations.columns_3d(self.points, KAMLOOPS, FIRST, self.end, 2)[0])
        self.assertEqual(whole["keep"], 12)                                   # monthly frames
        summer = page_data(animations.columns_3d(self.points, KAMLOOPS, *SUMMER_2021, 2)[0])
        self.assertEqual((len(summer["dates"]), summer["keep"]), (122, 365))   # daily frames: a scar outlasts the period
        left = np.array(summer["col"]) * summer["cell"]
        self.assertTrue((np.abs(left - np.array(summer["x0"])) < summer["cell"]).all())      # the scar's square is the column's
        self.assertEqual(len(summer["ground"]) % summer["across"], 0)
        # Only big patches are outlined: the script turns heights back into activity to add a patch up.
        html, top, cell_km, stretch = animations.columns_3d(self.points, KAMLOOPS, *SUMMER_2021, 2)
        self.assertEqual((summer["big"], summer["adds"]), (animations.SCAR, False))
        self.assertAlmostEqual(summer["most"], top)      # the activity that the tallest height stands for

    def test_3d_page_knows_the_time_of_each_step(self):
        # The page's script moves a playhead on the period timeline to each step's time, in plotly's milliseconds.
        summer = page_data(animations.columns_3d(self.points, KAMLOOPS, *SUMMER_2021, 2)[0])     # one frame a day
        self.assertEqual(list(pd.to_datetime(summer["at"], unit="ms")), list(pd.date_range(*SUMMER_2021)))
        whole = page_data(animations.columns_3d(self.points, KAMLOOPS, FIRST, self.end, 2)[0])   # one frame a month
        self.assertEqual([t.strftime("%B %Y") for t in pd.to_datetime(whole["at"], unit="ms")], whole["dates"])

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

    def test_map_tab_offers_3d_first_then_the_two_flat_views(self):
        view = [r for r in self.run_app().radio if r.label == "View"][0]
        self.assertEqual(list(view.options), ["3D", "2D Timelapse", "2D Summary"])
        self.assertEqual(view.value, "3D")          # what the Map tab opens on

    def test_every_view_draws_for_every_kind_of_period(self):
        at = self.run_app()
        for button in ("Whole record", "All of", "June to September"):
            for view in ("3D", "2D Timelapse", "2D Summary"):
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
        self.assertEqual(metrics["Rank for July"], f"{july['rank']:.0f} of {july.n_years:.0f}")
        self.assertIn("busiest July on record", at.markdown[0].value)

    def test_a_month_that_cannot_be_ranked_shows_no_rank(self):
        at = self.choose(self.run_app(), year=2012, month=1, area="Okanagan Valley")
        self.assertIn("cannot be ranked", at.markdown[0].value)
        self.assertEqual({m.label: m.value for m in at.metric}["Rank for January"], "-")

    def test_a_quick_pick_outside_the_record_is_switched_off(self):
        at = self.choose(self.run_app(), year=2000, month=3)
        disabled = {b.label: b.disabled for b in at.button}
        self.assertTrue(disabled["June to September 2000"] and disabled["March 2000"])
        self.assertFalse(disabled["All of 2000"] or disabled["Whole record"])

    def test_buttons_follow_the_year_the_timeline_is_zoomed_to(self):
        at = self.run_app()
        self.assertIn(f"All of {h.load_rows().day.max().year}", [b.label for b in at.button])   # the year in focus
        at.select_slider(key="months").set_range(pd.Period("2021-03"), pd.Period("2021-05"))
        at.run()
        self.assertFalse(at.exception, msg=[str(e.value) for e in at.exception])
        self.assertIn("All of 2021", [b.label for b in at.button])

    def test_a_circled_region_opens_its_calendar(self):
        at = self.choose(self.run_app(), view="2D Summary")      # the view whose map a region is circled on
        at.session_state["region"] = ((-120.9, 50.3), (-119.9, 50.3), (-119.8, 50.9), (-120.9, 50.9))
        at.session_state["open_region"] = True      # what circling a region on the map sets
        at.run()
        self.assertFalse(at.exception, msg=[str(e.value) for e in at.exception])
        self.assertTrue(any("km²" in m.value and "hotspots" in m.value for m in at.markdown))

    def test_a_month_outside_the_record_says_so(self):
        at = self.choose(self.run_app(), year=2000, month=3)
        self.assertTrue(any("no data for March 2000" in i.value for i in at.info))

    def test_an_upside_down_box_is_refused(self):
        at = self.choose(self.run_app(), area="Custom box")
        at.number_input(key="south").set_value(51.0)
        at.number_input(key="north").set_value(50.0)
        at.run()
        self.assertTrue(any("South must be below north" in e.value for e in at.error))

    def test_a_refused_box_does_not_reset_the_sidebar(self):
        at = self.choose(self.run_app(), year=2015, month=8, area="Custom box")
        at.number_input(key="south").set_value(51.5)        # above north: refused
        at.run()
        at.number_input(key="south").set_value(50.5)
        at.run()
        self.assertEqual((at.selectbox(key="year").value, at.selectbox(key="month").value), (2015, 8))
        self.assertIn("August 2015", at.markdown[0].value)

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
