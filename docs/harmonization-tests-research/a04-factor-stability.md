# Is the conversion factor stable, and does it survive the end of Suomi NPP?

## Answer

The MODIS (Terra plus Aqua) to VIIRS factor carries over to NOAA-20 without loss. Fitted directly on April 2018 to December 2021 it is 0.242 (95% interval 0.234–0.269, 43 months, 4 years), and chained through Suomi NPP it is 0.246. Suomi NPP and NOAA-20 show no step at March 2023 and no trend over 2019–2025. The all-hours factor is steady at a fixed day/night mix: 0.243 in 2012–2016 against 0.240 in 2017–2021. Its apparent fall from 0.281 to 0.237 between those halves comes from the night share of VIIRS hotspots rising from 48% to 62%. The separate day and night factors are not steady: the day factor fell 23% and the night factor rose 46%. Applied to the median month of a calendar month, the single factor runs high. In the overlap years, converted calendar-month medians came out about 23% above the actual Suomi NPP medians (year-block interval −2% to +59%). That bias, and the day/night mix of the pre-2012 years, matter more than the bootstrap interval of the factor (0.237–0.27), which changed none of the 31 test labels.

## Evidence

All counts use `use == True`, standard (SP) rows only, and months by local date. The data reproduce the check numbers exactly: 48,233 MODIS and 198,916 Suomi NPP hotspots, ratio 0.2425 (0.343 by day, 0.177 at night). "Ratio" means MODIS divided by VIIRS, as a ratio of sums. Intervals are 95% and come from resampling whole years. Standard-product VIIRS rows end in July 2026, so every VIIRS series stops there. Near-real-time rows were not mixed in.

**1. Direct factor against the chain through Suomi NPP.** The window is 2018-04 to 2021-12, without 2020-08 and 2020-09 (an Aqua gap), which leaves 43 months. No month had a zero count or a NOAA-20 outage.

| | All hours | Day | Night |
|---|---|---|---|
| MODIS / NOAA-20, direct | 0.242 (0.234–0.269) | 0.343 (0.32–0.42) | 0.184 (0.09–0.19) |
| MODIS / Suomi NPP, 116 stable months | 0.2425 (0.237–0.269) | 0.343 (0.32–0.41) | 0.177 (0.13–0.19) |
| Chain: 116-month factor × Suomi NPP/NOAA-20 in the window (1.013, 0.99–1.08) | 0.246 | 0.352 | 0.178 |

The chain and the direct fit are ratios of sums over the same months, so their agreement (chain/direct 1.02, 0.97–1.17) mostly restates one fact: the 2018–2021 MODIS/Suomi NPP ratio (0.239) matches the 10-year value. It is not independent confirmation. With only 4 years, there are just 35 distinct resamples. Suomi NPP/NOAA-20 by year was 1.08 (2018, 9 months), 1.04, 0.96, 0.99, 1.04, 1.06, 0.88 (2024, 9 months) and 1.01 (2025). The trend over 2019–2025 is −0.7% a year (−4.0 to +2.5).

**2. Split-half stability, MODIS / Suomi NPP, 116 stable months.**

| | 2012–16 | 2017–21 | Second ÷ first | Trend per year (10 annual ratios, t-interval) |
|---|---|---|---|---|
| All hours | 0.281 | 0.237 | 0.84 (0.75–0.92) | −2.9% (−6.0 to +0.3), p = 0.07 |
| Day | 0.424 | 0.328 | 0.77 (0.68–0.92) | −3.2% (−6.5 to +0.1), p = 0.05 |
| Night | 0.125 | 0.182 | 1.46 (1.14–1.90) | +1.6% (−9 to +13) |
| All hours at the 116-month day/night mix | 0.243 | 0.240 | 0.99 | — |
| Suomi NPP share at night | 48% | 62% | | |

The daytime decline appears in both Terra (0.187 to 0.133) and Aqua (0.238 to 0.196). It survives a month-level control for month size: −5.1% a year (−8.9 to −0.2) on 98 months with at least 10 Suomi NPP hotspots. Single years run from 0.196 (2020) to 0.331 (2016). MODIS put 33% of its hotspots at night in 2003–2011, against 21% in 2012–16 and 48% in 2017–21. If the 2003–2011 MODIS counts are converted with separate day and night factors, the implied all-hours factor for those years is 0.261, so the single factor would give them a total 7.7% higher.

**3. Fixed-date step tests.** The monthly tests are the analyst's. They regress the monthly log ratio on a step, use months where both counts are at least 10, and report Newey-West standard errors (6 lags) with an AR(1) check. The year-level tests are the reviewer's: a step in the annual fire-season log ratio, with years as the units. "Detectable" means the step size the test would find 80% of the time at the 5% level.

| Series, step date | Monthly: step (95%); detectable | Year level: step (95%); detectable |
|---|---|---|
| MODIS/Suomi NPP, Apr 2018 (2012–21) | −5% (−20 to +12); ~27% (48 fire-season months) | −18% (−39 to +9); 49% (10 years) |
| Suomi NPP/NOAA-20, Mar 2023 (2018–25/26) | +0.3% (−7 to +8); ~12% (84 months) | −3% (−15 to +11); 20% (8 years) |
| MODIS/NOAA-20, Jan 2022 (2018–25/26) | −8% (−23 to +9); ~28% (63 months) | −4% (−21 to +18); 32% (8 years) |
| MODIS/Suomi NPP, Jan 2022 (2012–25/26) | −16% (−31 to +2); ~31% (110 months) | −10% (−29 to +15); 40% (14 years) |

No step is significant in either form. With whole years as the unit, only steps of about 20% between the VIIRS satellites, or 30–50% for MODIS series, would have been detected.

**4. Prediction intervals for one converted month (Protocol A, MODIS to VIIRS-equivalent, 116 months).** These are the analyst's nested leave-one-year-out CV+ intervals at 90% nominal coverage. CV+ is a jackknife+ variant with years as folds and residuals on the log(count + 1) scale. "Size-binned" means residuals are pooled only within bins of predicted count. Coverage was measured on held-out years.

| Predicted count | Months | Size-binned CV+ coverage | Median interval relative to the converted value | Negative binomial (one dispersion) coverage |
|---|---|---|---|---|
| 1000 or more | 25 | 0.92 (0.85–1.00) | 0.45× to 1.31× | 1.00, about 2× wider |
| 100–1000 | 29 | 0.90 (0.75–1.00) | 0.45× to 1.52× | 1.00 |
| 10–100 | 51 | 0.92 (0.82–1.00) | 0.39× to 4.9× | 0.94 |
| Under 10 | 11 | 0.55 (0.29–0.86) | none honest | 0.45 |

In the stable period, 4 months had MODIS = 0 with Suomi NPP above 0, and 1 month had the reverse. They were kept. A bin holds only about 20–26 residuals, so the finite-sample rule makes each 90% interval the full range of past residuals. Using plain 5th and 95th percentiles of the same residuals, the reviewer's coverage was 0.84, 0.72, 0.86 and 0.45.

**5. One factor applied to every MODIS-era year.** The baseline for a month is the median of 9 converted years (2003–2011 MODIS ÷ f, with 2003-12 dropped for a Terra gap) and 10 Suomi NPP years (2012–2021). It was applied to the 31 fire-season months from 2022-04 to 2026-07, using NOAA-20 × 1.011. All 31 months had a baseline median of at least 10, so none was unclassifiable. NOAA-20 2024-03 and 2025-07 were left out as outage months.

| f used | Five-class labels changed, of 31 |
|---|---|
| Bootstrap ends, 0.237 and 0.270 | 0 |
| 2017–21 half (0.237) / 2012–16 half (0.281) | 0 / 2 |
| f ± 20% | 2 / 2 |
| f − 30% | 7 |

The baseline median moves only in calendar months where the median is a converted value: May, June and July at most, by up to 10–13%. In the overlap, the leave-one-year-out conversion put calendar-month medians at a median 1.23 times the actual Suomi NPP medians (0.98–1.59). By calendar month the figure ranged from 0.92 (April) to 1.70 (June).

## What this implies

- The team can claim that the factor carries over to NOAA-20 within about 2%, and that NOAA-20 and Suomi NPP showed no measurable step or trend. It cannot claim the chain is independently confirmed, because the direct and chained figures share the same months.
- An all-hours factor is steadier than separate day and night factors in this record. Day/night factors are only as good as the day and night factors are stable, and here they moved in opposite directions by 20–45% between halves.
- The bootstrap interval of the factor (−2% to +11%) understates how wrong it could be for 2003–2011. That error does not average out across years. More realistic sizes are the 7.7% day/night-mix effect and the 23% median bias.
- A converted month can carry an empirical interval by size of month, about ×0.45 to ×1.3–1.5 for months of 100 or more hotspots, with a systematic factor range shown separately. Under about 10 predicted hotspots, no interval tested here was honest.
- None of the step tests can exclude steps of 20% or more.

## Limits

Only 10 stable years are available, three of them very large, and only 4 years for MODIS against NOAA-20. Year-level tests have 8–14 points. The analysis cannot say whether the opposite day/night movements are physical, an artefact of day/night labelling, or noise. It cannot check the factor before 2012. BC's burned-area totals (2,817 km² in 2003–2011 against 10,653 km² in 2012–2021) are too coarse to test it. The class-change results come from one set of 31 months and depend on where each month's median lies.

## How it was computed

The analyst's scripts `a04_common.py`, `a04_p12.py`, `a04_p2b.py`, `a04_p3.py`, `a04_p4.py` and `a04_p5.py` were re-run from a clean start and gave identical outputs. `a04-factor-stability_review.py` recomputes the check numbers, parts 1, 2, 4 and 5, the year-level step tests, the day/night composition, the median bias and the size-controlled trends, without the analyst's code. Its output is in `out/a04-factor-stability_review_*.csv` and `_log.txt`. All are kept with the cached data under `data/harmonization-analysis/round3/`, which is git-ignored.
