# Diagnostics borrowed from hydrology, quality control and clinical chemistry

## Answer

Double-mass curves (cumulative MODIS count plotted against cumulative VIIRS count) are straight through the stable-orbit years, with slope 0.242 (0.237–0.27) against Suomi NPP. The only clear later bend is Terra by day against NOAA-20: the slope falls from 0.140 to about 0.07 after October 2024, and most of that fall comes from 2026. Control charts built on fire-season monthly log ratios detect that loss only on the Terra-daytime series: a CUSUM chart first signals in 2025-09, and EWMA and single-month charts first signal in 2026-07. A Terra+Aqua daytime chart signals only in 2026-10. The all-hours Terra+Aqua chart never signals. When MODIS is converted to Suomi NPP units with one factor, 95% of fire-season months fall between 0.42 and 3.1 times the real Suomi NPP count. For NOAA-20 against Suomi NPP the range is 0.66–1.57. In both cases the spread of the log difference is about 2.3 times wider for converted MODIS, and that holds at every month size. Converted MODIS is therefore right on average and in rank order, but in a single month it is less than half as precise as a second VIIRS satellite.

## Evidence

Common basis for every number below: the standard filter (`use == True`), months keyed by local date (`ym_local`), and the box-wide factor. Every sensor-month listed in `masked_sensor_months.csv` is dropped from any pair that contains that sensor. Partial-outage months are kept: NOAA-20 in 2024-03 and 2025-07, Suomi NPP in 2025-07 and NOAA-21 in 2025-10. Intervals come from resampling whole years. Day and night are split by the delivered flag for standard rows. For near-real-time rows (August to October 2026) they are split by local solar hour, day being 06:00 to 18:00. That rule reproduces the delivered flag on all but 10 of 644,028 standard rows. The check numbers reproduce exactly: 116 months, 48,233 MODIS hotspots against 198,916 Suomi NPP, a ratio of 0.2425 (0.343 by day, 0.177 at night).

**1. Double-mass slopes.** The slope is the ratio of sums over the window. The stable windows are 2012-02 to 2021-12 against Suomi NPP and 2018-04 to 2021-12 against NOAA-20. The yearly columns are fire-season ratios.

| Pair | Stable slope (years) | Stable fire-season range | 2022 | 2023 | 2024 | 2025 | 2026 (Apr–Oct) |
|---|---|---|---|---|---|---|---|
| Terra+Aqua / Suomi NPP, all hours | 0.242 (0.237–0.27), 10 | 0.20–0.41 | 0.26 | 0.23 | 0.26 | 0.25 | — |
| Terra+Aqua / NOAA-20, all hours | 0.242 (0.234–0.27), 4 | 0.21–0.31 | 0.26 | 0.24 | 0.23 | 0.25 | **0.20** |
| Terra+Aqua / NOAA-20, day | 0.343 (0.32–0.43), 4 | 0.32–0.46 | 0.38 | 0.37 | 0.37 | 0.41 | **0.25** |
| Terra+Aqua / NOAA-20, night | 0.184 (0.09–0.19), 4 | 0.05–0.19 | **0.19** | 0.18 | 0.17 | 0.18 | 0.18 |
| Terra day / NOAA-20 | 0.140 (0.13–0.19), 4 | 0.13–0.21 | 0.15 | 0.15 | 0.13 | 0.14 | **0.07** |
| Aqua / NOAA-20, all hours | 0.111 (0.107–0.136), 4 | 0.11–0.15 | 0.12 | 0.11 | 0.10 | 0.12 | **0.09** |
| NOAA-20 / Suomi NPP | 0.988 (0.93–1.01), 4 | 0.93–1.08 | 0.98 | 0.94 | 1.14 | 1.01 | — |
| NOAA-21 / NOAA-20 | 0.996 (0.88–1.04), 2 | 0.87–1.04 | — | 1.04 | 0.87 | 0.88 | 0.96 |

The bend search extends the stable slope into the drift period and lets the slope change once. It places the bend for Terra by day in 2024-10, with a slope of 0.073 for the 24 months after it. For Terra+Aqua all hours the bend falls in 2024-07, with a slope of 0.203 for 27 months. For Terra+Aqua by day it falls in 2026-05. The fit is descriptive, not a significance test. Terra's daytime fire-season ratios in 2024 and 2025 (0.131 and 0.136) sit at the bottom of the four-year range rather than outside it. The bend at 2024-10 therefore mostly reflects 2026, which was a very large fire year. In 2026 the all-hours ratio fell less than the daytime ratio because the night ratio held at 0.18.

**2. Control charts.** A control chart tracks a monthly statistic against limits set from a reference period and flags months that fall outside them. The monitored statistic here is z = (ln((y+0.5)/(x+0.5)) − mean) / SD, with the mean and SD taken from the stable window. Only fire-season months with at least 100 reference hotspots are charted. Months below the threshold or in an outage are skipped, not filled. Zero numerators were never reached. The CUSUM chart adds up deviations (k = 0.5, alarm at h = 4). The EWMA chart is an exponentially weighted average (λ = 0.2, exact 3-SD limits). The Shewhart chart flags any single month beyond 3 SD. The leave-one-year-out (LOYO) column sets limits from the other stable years and runs each held-out year from a fresh start.

| Pair | Months charted (stable) | Skipped: below 100 / outage | SD | First CUSUM / EWMA / single-month signal | Held-out years with any alarm (CUSUM/EWMA/single) |
|---|---|---|---|---|---|
| Terra+Aqua / Suomi NPP, all, to 2025-12 | 48 (32) | 44 / 6 | 0.31 | none / none / none | 0/0/0 of 10 |
| Terra+Aqua / NOAA-20, all, to 2026-10 | 35 (15) | 24 / 4 | 0.46 | none / none / none | 0/1/1 of 4 |
| Terra+Aqua / NOAA-20, day | 29 (12) | 30 / 4 | 0.23 | 2026-10 / 2026-10 / none | 0/1/1 of 4 |
| Terra+Aqua / NOAA-20, night | 31 (13) | 28 / 4 | 0.66 | none / none / none | 0/0/0 of 4 |
| **Terra day / NOAA-20** | 29 (12) | 33 / 1 | 0.26 | **2025-09 / 2026-07 / 2026-07** | 0/0/0 of 4 (12 months) |
| Aqua / NOAA-20, all | 36 (15) | 24 / 3 | 0.35 | none / none / none | 1/1/1 of 4 |
| NOAA-20 / Suomi NPP, run to 2025-12 | 32 (15) | 22 / 2 | 0.16 | none / none / none | 0/1/1 of 4 |
| NOAA-21 / NOAA-20 (limits 2023–24) | 17 (9) | 11 / 0 | 0.14 | none in 8 monitored | 0/0/0 of 2 |

All Terra-daytime z-scores from 2022 to 2025 but two are negative, which is the gradual decline the CUSUM accumulates. Simulated with independent normal values, the charts raise a false alarm on average every 165 months (CUSUM), 530 months (EWMA) and 370 months (single month). They catch a persistent 1-SD shift after about 8.5, 10 and 45 months.

**A monthly rule for NOAA-21 against NOAA-20.** The rule is illustrative.

1. In each month from April to October, skip the month if NOAA-20 has fewer than 100 hotspots or if either satellite has a listed outage.
2. Compute z = (ln((N21+0.5)/(N20+0.5)) + 0.003) / 0.14.
3. Raise an alarm if |z| > 3, which means a ratio outside 0.66–1.52. Also raise one if a CUSUM sum (S⁺ = max(0, S⁺ + z − 0.5), and its mirror) exceeds 4, or if the EWMA (E = 0.2z + 0.8E) exceeds 1.0 in size.
4. After an alarm, check the outage list, then reset S and E to zero.

Through 2026-10 the rule has not alarmed (z from −1.9 to +0.8). The SD of 0.14 rests on 9 months, and its 95% interval is 0.09–0.26. Only about 4 months a year reach the threshold. A persistent 14% shift would therefore take two to three fire seasons to detect.

**3. Method comparison.** The basis is the 68 fire-season months of the stable period. MODIS is converted with a factor fitted on the other nine years (leave one year out, whole box). The basis for NOAA-20 is 54 fire-season months from 2018-04 to 2025-12. All statistics are computed on ln(count+1). There was one zero month on each side, and dropping them changes little: the bias moves to 1.13 and the limits to 0.44–2.9. Bias is the geometric-mean ratio. The limits of agreement are the range expected to hold 95% of months. The proportional-bias test regresses the difference on the mean, with standard errors clustered by year. Passing-Bablok is a rank-based regression. Lin's concordance correlation coefficient (CCC) measures closeness to the 1:1 line.

| Statistic | Converted MODIS, one factor | Converted MODIS, day/night factors | NOAA-20 vs Suomi NPP |
|---|---|---|---|
| Bias | 1.15 (1.03–1.28) | 1.00 (0.92–1.09) | 1.02 (0.97–1.07) |
| 95% limits of agreement | 0.42–3.15 | 0.38–2.67 | 0.66–1.57 |
| SD of log difference | 0.52 (0.42–0.61) | 0.50 | 0.22 (0.16–0.27) |
| Proportional bias, slope (p) | −0.013 (0.67) | 0.015 (0.59) | −0.023 (0.012) |
| Passing-Bablok slope | 0.99 (0.93–1.05) | 1.02 (0.97–1.07) | 0.98 (0.965–0.995) |
| Passing-Bablok intercept | 0.19 (−0.18 to 0.65) | −0.06 (−0.46 to 0.27) | 0.12 (0.01–0.26) |
| Lin's CCC | 0.974 (0.95–0.985) | 0.978 | 0.996 (0.993–0.998) |
| Median absolute error; within 25% | 32%; 29% | 27%; 38% | 10%; 70% |
| Ratio of sums (converted / Suomi NPP) | 0.99 | 1.05 | 0.99 |

Two features of the table need explaining. First, the single factor is right in total (ratio of sums 0.99) but 15% high in a typical month, because quiet months run higher than busy ones. Fitting the factor on fire-season months only gives the same 1.14. The day/night factors remove the typical-month bias but put the total 5% high. Second, the concordance correlation looks high for both pairs because counts span four orders of magnitude, so the limits of agreement discriminate better.

By size of month (geometric mean of the pair). The Poisson column is the spread that independent counting noise alone would produce.

| Size (hotspots) | Converted MODIS: months, bias, limits, SD (Poisson SD) | NOAA-20 vs Suomi NPP: months, bias, limits, SD (Poisson SD) |
|---|---|---|
| under 30 | 16, 1.18, 0.25–5.4, 0.78 (0.68) | 13, 1.08, 0.55–2.1, 0.35 (0.56) |
| 30–300 | 26, 1.17, 0.44–3.1, 0.50 (0.28) | 15, 1.06, 0.72–1.55, 0.19 (0.18) |
| 300–1,000 | 9, 1.07, 0.55–2.1, 0.34 (0.11) | 9, 1.03, 0.76–1.40, 0.16 (0.06) |
| 1,000 and over | 17, 1.12, 0.64–1.96, 0.29 (0.04) | 17, 0.94, 0.73–1.20, 0.13 (0.03) |

**4. The "stable decade" trend.** Against Suomi NPP the ratio of sums was 0.281 in 2012–16 and 0.237 in 2017–21. Suomi NPP counted 23,234 hotspots in the first half against 175,682 in the second, so a few large months set both values. Weighting fire-season months equally, with at least 100 reference hotspots, the difference shrinks to −0.10 in logs (p 0.26, 32 months, clustered by year). Adjusting for month size gives −0.15 (p 0.16). The trend is possible but not established.

## What this implies

- The team could claim that converted MODIS reproduces the level, rank order and month-to-month swing of VIIRS: Passing-Bablok slope near 1, no proportional bias, total within 1%. It could not claim that a single converted month is interchangeable with a VIIRS month. Even in months of 1,000 or more hotspots, 95% of months lie between 0.64 and 1.96 times the real count, against 0.73–1.20 for two VIIRS satellites.
- In plain terms for a judge, about two fire-season months in three fall inside the following bands (one SD of the log difference). Two VIIRS satellites fall within −20% to +25% of each other, and within −12% to +14% in the busiest months. Converted MODIS falls within −40% to +70% of VIIRS, and within −25% to +33% in the busiest months.
- Whether a single factor or day/night factors is "unbiased" depends on whether totals or typical months are scored. Both statements are true at once.
- A drift monitor on all-hours Terra+Aqua counts would not have detected the Terra daytime loss. Only a Terra-daytime chart did, and it first signalled in 2025-09.
- A NOAA-21 monitor at a threshold of 100 can detect only large or persistent changes, and only after several seasons.

## Limits

Every NOAA-20 pair rests on four stable years, and the NOAA-21 limits rest on two seasons. The false-alarm rates are therefore counts out of 2 to 4 held-out years, not rates. The charts assume independent, normal log ratios with no seasonal structure. The Poisson comparison assumes independent counts, which two VIIRS satellites watching the same fires are not; that is why their observed spread falls below Poisson in small months. Results apply to the whole box. Smaller areas will scatter more. The cause of the 2026 Terra fall, and of the possible 2012–21 trend, is not established.

## How it was computed

The analyst's scripts are `a10_prep.py`, `a10_doublemass.py`, `a10_doublemass_drift.py`, `a10_control.py`, `a10_control_sens.py` and `a10_method_comp.py`. They were re-run from a clean start and reproduced their outputs byte for byte. The reviewer's script, `a10-diagnostics_review.py`, recomputes every table independently from the parquet file and runs in about 10 seconds. Its outputs are `out/a10-diagnostics_review_*.csv`. Year-block bootstraps use 1,000 draws for the slopes, 500 for the method statistics and 300 for Passing-Bablok.
