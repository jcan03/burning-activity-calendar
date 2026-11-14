# How stable is the VIIRS-to-MODIS count ratio?

## Answer

Over the stable-orbit period (February 2012 to December 2021, 116 usable months), MODIS (Terra plus Aqua) recorded 0.242 hotspots for every Suomi NPP VIIRS hotspot in the whole box. Put the other way, VIIRS recorded about 4.1 hotspots for every MODIS hotspot. The interval from resampling whole years is 0.237 to 0.268. The pooled ratio is stable because three big fire years (2017, 2018 and 2021) supply most of the hotspots, and each of them sits at 0.234 to 0.244. Single months and quiet years are not stable. Half of all months fall between 0.16 and 0.31. Fire-season ratios in the seven quieter years range from 0.19 to 0.40, about five times the scatter that random counting alone would produce. The day ratio (0.34) is about twice the night ratio (0.18). The log-log slope is close to 1, between 0.94 and 1.09 depending on which months are used, so there is no consistent sign that the ratio changes with activity. One factor predicts large fire-season months to within about 14% (median error); no tested scaling does reliably better once whole years are left out.

## Evidence

All counts below use standard-quality rows with `type` 0. Months are UTC months. Three months are dropped because they overlap an outage: February 2016 (Terra) and August and September 2020 (Aqua). That leaves 116 of 119 months. No kept month has zero VIIRS hotspots. Four winter months have zero MODIS hotspots; they stay in the ratios of sums and are left out of the log fits and the percentage-error scores. A ratio of sums is total MODIS divided by total VIIRS. The year-block interval is the 2.5th to 97.5th percentile over 4,000 resamples of whole years, because months within a year are not independent.

**Overall (116 months: 48,233 MODIS hotspots, 199,013 VIIRS hotspots)**

| Quantity | Value | Year-block interval |
|---|---|---|
| Ratio of sums, all months | 0.242 | 0.237–0.268 |
| Ratio of sums, fire season (68 months) | 0.242 | 0.238–0.286 |
| Ratio of sums, November to March (48 months) | 0.241 | 0.215–0.263 |
| Monthly ratios, all 116: median (25th–75th percentile; 5th–95th) | 0.231 (0.163–0.305; 0.033–0.486) | |
| Monthly ratios, 58 months with VIIRS ≥ 100: median (5th–95th) | 0.237 (0.147–0.356) | |
| Ratio of sums, day / night (FIRMS `daynight` flag) | 0.343 / 0.177 | 0.324–0.412 / 0.129–0.187 |

The ten largest months hold 82% of VIIRS hotspots and 80% of MODIS hotspots, so the pooled ratio reflects those months. The mean of the monthly ratios (0.246) is close to the ratio of sums only by coincidence; the two answer different questions.

**Fire season (April to October) by year**

| Year | MODIS | VIIRS | Ratio | Day ratio | Night ratio |
|---|---|---|---|---|---|
| 2012 | 195 | 769 | 0.254 | 0.41 | 0.12 |
| 2013 | 868 | 2,151 | 0.404 | 0.59 | 0.13 |
| 2014 | 467 | 1,740 | 0.268 | 0.40 | 0.15 |
| 2015 | 1,153 | 4,345 | 0.265 | 0.39 | 0.19 |
| 2016 | 782 | 2,189 | 0.357 | 0.50 | 0.12 |
| 2017 | 9,914 | 42,325 | 0.234 | 0.31 | 0.18 |
| 2018 | 6,089 | 24,991 | 0.244 | 0.38 | 0.17 |
| 2019 | 766 | 2,621 | 0.292 | 0.42 | 0.14 |
| 2020 (5 months) | 128 | 665 | 0.192 | 0.40 | 0.03 |
| 2021 | 23,108 | 97,477 | 0.237 | 0.32 | 0.19 |

Across these ten years the coefficient of variation (standard deviation divided by mean) is 0.23 for the combined ratio, 0.20 for the day ratio and 0.33 for the night ratio. Splitting by day and night therefore does not make the year-to-year ratio steadier. When each year's MODIS share is compared with the pooled share, the standardized departures have a standard deviation of 5.3; pure counting noise would give about 1. 2013 and 2016 lie 13 and 9 standard errors above the pooled share. Hotspots cluster in space and time, so part of this excess is expected, but the quiet-year scatter is too large to be counting noise alone.

**Activity.** When the 68 fire-season months are split into thirds by VIIRS count, the ratio of sums falls as activity rises: 0.31 (0.24–0.39) in the low third (VIIRS 1–45), 0.28 (0.23–0.34) in the middle third (46–366) and 0.24 (0.23–0.26) in the high third (404–62,646). Across all 116 months the thirds look flat (0.24, 0.23, 0.24), but only because winter months, which have low ratios, fill the low third.

**Log-log slope** (ordinary least squares of log MODIS on log VIIRS; reverse means log VIIRS on log MODIS, inverted)

| Months | n | Slope | Year-block interval | Reverse slope |
|---|---|---|---|---|
| All, MODIS > 0 | 112 | 1.01 | 0.94–1.07 | 1.10 |
| Fire season, MODIS > 0 | 67 | 0.96 | 0.91–1.02 | 1.01 |
| Fire season, VIIRS ≥ 80 | 35 | 0.99 | 0.94–1.05 | 1.02 |
| All, VIIRS ≥ 100 | 58 | 1.09 | 1.03–1.19 | 1.14 |
| Fire season, Poisson likelihood (all 68 months) | 68 | 0.96 | 0.93–0.98 | |

**Leave-one-year-out prediction of monthly MODIS counts.** Each year is predicted from factors fitted on the other nine. The score is the median absolute percentage error (median APE). Intervals come from resampling years.

| Months scored | n | One factor | Day and night factors | Calendar-month factors | Power law |
|---|---|---|---|---|---|
| All, MODIS > 0 | 112 | 31 (27–39) | 35 (22–42) | 26 (18–32) | 30 (24–35) |
| Fire season, VIIRS ≥ 80 | 35 | 23 (16–31) | 18 (11–34) | 15 (10–29) | 23 (18–33) |
| Fire season, VIIRS ≥ 400 | 23 | 14 (7–29) | 11 (8–20) | 10 (4–16) | 20 (14–29) |

The paired difference from one factor (resampling years) excludes zero only once: calendar-month factors on all months, 5.6 points better (0.6 to 13.2). In fire-season months with VIIRS ≥ 80, the day-and-night gain is 4.9 points (−2.4 to 10.1) and the calendar-month gain is 7.6 points (−0.4 to 15.7); both intervals include no gain. The one-factor error for a whole fire-season total, rather than a single month, is about 10% (median over years).

## What this implies for the approach

- **Target record.** Either direction works for big fire seasons, because a ratio near 0.24 holds in 2017, 2018 and 2021. Converting VIIRS to MODIS-equivalent removes about three quarters of the hotspots, which makes quiet areas and quiet months even noisier.
- **Unit.** Raw counts carry a month-level error of about 15–30% after scaling, and much more in quiet months. This evidence does not test grid cells, fire radiative power or anomalies. However, the size of the quiet-month scatter argues for a unit or display that does not depend on a precise cross-sensor factor.
- **Scaling.** One factor (about 0.24, or 4.1 VIIRS per MODIS) is defensible for large fire-season months and seasonal totals. Day and night factors (0.34 and 0.18) differ clearly but did not measurably improve leave-one-year-out error. Calendar-month factors rest on 9–10 months each and move with single events: June is 0.30 by UTC month but 0.52 by local date, because one Terra evening pass on 30 June 2021 falls in July in UTC. A fitted power law adds nothing, because the slope is close to 1.
- **Combining VIIRS satellites.** Not tested here. Every factor above is for Suomi NPP alone.
- **MODIS since 2022.** The ratio depends on the day/night mix and on overpass times (Terra's night pass is at about 21:45 local, Aqua's and VIIRS's at about 02:00). The drift changes both, so these stable-period factors should not be applied to MODIS after 2021 without a separate check.

## Limits

- Whole box only; a user-selected area will have fewer hotspots and wider scatter.
- Ten years, with three years dominating; the high-activity estimates rest on a handful of months.
- The cause of the high ratios in quiet years (for example, burn type or fire size) is not tested.
- `type` 0 filtering cannot be applied to near-real-time rows, which have no `type`.
- UTC months split the evening Terra pass from the same local day; the overall ratio is unchanged (0.2424 either way), but 7 months change by more than 0.02.

## How it was computed

`scripts/m01-ratio-stability_review.py` builds monthly counts independently from the shared table (standard rows, `type` 0, Terra plus Aqua against Suomi NPP), drops months that overlap an outage, and prints every number above: ratios of sums with month and year-block bootstraps, calendar-month, day/night, activity and yearly ratios, log-log and Poisson slopes, leave-one-year-out scores with paired comparisons, and the local-date check. Tables are in `out/m01-ratio-stability_*.csv`. The analyst's `scripts/m01_ratio.py` was re-run and reproduces its own numbers.
