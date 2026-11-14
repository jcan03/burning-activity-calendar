# An empirical detection curve for MODIS, and counts above a common threshold

## Answer

Where Suomi NPP saw fire, the chance that Aqua also saw it rises slowly with fire power. However, the power at which Aqua detects half the time is not a fixed property of the sensor. Using the power in a single 1 km cell, it is about 12 MW by day and at night. Using the power Aqua's larger pixel can actually see (the surrounding 3 km × 3 km), or using only isolated fires, it is about 55 to 70 MW. It also varies from 8 to 47 MW by day between years, depending on how clustered the fires were. The detection curve used as a converter is no better than separate day and night factors in large months. Over all 117 months it is worse than one factor (median error 0.37 against 0.30; paired difference +0.07, interval +0.01 to +0.19), because it over-predicts quiet months by about 40%. The published detection-limit formula does no better. A common power threshold does not bring the ratio to 1. By day, for 1 km cells, the ratio rises from 0.43 to 0.69 at 20 MW and becomes steadier across years (coefficient of variation 0.13 to 0.09), but half of Suomi NPP's cells are discarded and single-month prediction error does not improve. At night a threshold helps in large months but leaves too few records in most others.

## Evidence

**Data.** The analysis uses rows with `use == True`, standard (SP) rows only and local-date months. It covers February 2012 to December 2021 with August and September 2020 removed (Aqua gap), which leaves 117 months: 22,458 Aqua and 198,989 Suomi NPP hotspots. The SPEC check numbers were reproduced exactly (48,233; 198,916; 0.2425; 0.343 by day; 0.177 at night). The Aqua/Suomi NPP ratio is 0.113 (0.202 by day, 0.055 at night). A **cell-half-day** is a 1 km grid cell on one local date, by day or by night. Aqua **detected** a Suomi NPP cell if it has a hotspot in that cell or in one of its 8 neighbours in the same half-day. That gives 77,758 Suomi NPP cell-half-days (34,794 by day, 42,964 at night); the 10 cells with zero summed power are left out of the fits. Intervals are 95% intervals from resampling whole years (200 resamples for the fits, 1,000 for the scores).

**Table 1. Power (MW of summed Suomi NPP power) at which Aqua detection reaches 50% and 90%. Complementary log-log fit, 10 stable years.**

| Covariate, match rule | Cells (day / night) | Day P50 | Day P90 | Night P50 | Night P90 |
|---|---|---|---|---|---|
| Cell power, 3×3 match (analyst's main) | 34,784 / 42,964 | 11.7 (9.5–19.9) | 210 (181–262) | 12.2 (10.1–26.4) | 65 (61–86) |
| Cell power, same cell only | same | 261 (217–301) | 4,100 | 83 (73–102) | 390 |
| 3×3 power, 3×3 match | same | 55 (50–70) | 690 (580–780) | 66 (60–79) | 256 (223–263) |
| Isolated cells only (no other Suomi NPP cell within 2 km), 3×3 match | 3,692 / 3,885 | 54 (47–65) | 233 (189–293) | 70 (53–125) | 171 (129–287) |

The yearly P50 for the main definition ranges from 8.2 to 41.6 MW by day and from 9.1 to 123 MW at night. It is lowest in the two large years, 2017 and 2021, which supply 62% of daytime cells, and highest in quiet years such as 2012 and 2020 (`a08_rev_p50_by_year.csv`). That is why the intervals are lopsided. At 2–5 MW, Aqua "detects" 30% of all daytime cells but only 5% of isolated ones, so most low-power detections are neighbours of larger fires. Above 300 MW, Aqua missed 124 of 1,645 cells. In only 6 of those half-days did Aqua record nothing anywhere in the box, so the 0.92 daytime ceiling is not explained by Aqua failing to pass over.

The published limits are about 5 MW at 1 km² (the 50% point of Sofiev and Kouznetsov's logistic) and about 10–11 MW at Aqua's mean delivered pixel area of 2.3 km² by day and 2.1 km² at night. They match the cell-power P50 only by coincidence. Measured as neighbourhood or isolated-fire power, which is the more physical comparison, the 50% point is about 10 times the nominal limit. Suomi NPP fire power is shared among its 375 m pixels, and the two sensors pass minutes apart at different view angles, so these numbers are not MODIS-unit detection limits.

**Aqua hotspots with no Suomi NPP hotspot in the 3×3 neighbourhood in the same half-day:** 1,647 of 22,458 (7.3%), made up of 1,510 of 15,888 by day (9.5%) and 137 of 6,570 at night (2.1%). With a 5×5 neighbourhood the figure is 4.9%. Of the 1,647, 354 fall on half-days when Suomi NPP recorded no hotspot anywhere in the box (296 by day, 58 at night).

**Table 2. Predicting monthly Aqua counts from Suomi NPP, leave one year out.** The curve is refitted on 9 years each time, and a scale constant c is fitted on the same 9 years. MdAPE is the median absolute percentage error. The 9 months with zero Aqua hotspots are excluded from MdAPE but kept in the fits and totals. "Difference" is the paired year-resampled difference from one factor.

| Predictor | All 117 months | Difference from one factor | Fire season, 68 months | 17 months with ≥1,000 Suomi NPP hotspots | Fire-season total error per year, median (max) |
|---|---|---|---|---|---|
| One factor | 0.30 (0.24–0.38) | — | 0.30 (0.22–0.46) | 0.18 (0.17–0.27) | 0.09 (0.46) |
| Day and night factors | 0.33 (0.21–0.39) | +0.03 (−0.06 to +0.09) | 0.26 (0.15–0.40) | 0.13 (0.06–0.17) | 0.05 (0.31) |
| Fitted curve × c | 0.37 (0.29–0.51) | **+0.07 (+0.01 to +0.19)** | 0.27 (0.16–0.37) | 0.12 (0.10–0.18) | 0.07 (0.23) |
| Published limit as a step, 1 km² | 0.40 (0.28–0.49) | +0.10 (−0.01 to +0.18) | 0.26 (0.16–0.40) | 0.13 (0.10–0.20) | 0.08 (0.23) |
| Published 50% point, fitted slope, mean area | 0.38 (0.30–0.51) | +0.08 (+0.02 to +0.19) | 0.28 (0.16–0.38) | 0.12 (0.10–0.19) | 0.07 (0.24) |

In large months, the curve beats one factor (difference −0.06, interval −0.15 to −0.02) but not day and night factors (−0.01, interval −0.04 to +0.07). The median signed error of the curve is +40% in the 66 months with fewer than 200 Suomi NPP hotspots, +30% in the 18 months with 200–999 and +6% in the 24 months with 1,000 or more. For one factor the same figures are +8%, −4% and −1%. Night alone is not usable: 64 of 117 months have zero Aqua night hotspots, including 30 of the 68 fire-season months.

**Table 3. Common threshold T: count only records with power ≥ T for both sensors, 117 months.** The year-to-year coefficient of variation (CV) is computed over fire-season ratios. The leave-one-year-out MdAPE is computed on a fixed set of fire-season months chosen by raw Suomi NPP count of at least 100: 21 months by day and 23 at night for cells, 28 and 27 for hotspots. Results for all hours combined are in `a08_rev_threshold.csv`.

| Unit, time | T (MW) | Aqua kept | Suomi NPP kept | Ratio (interval) | CV | MdAPE |
|---|---|---|---|---|---|---|
| 1 km cell, day | 0 | 100% | 100% | 0.43 (0.41–0.44) | 0.13 | 0.10 |
| | 20 | 80% | 50% | 0.69 (0.66–0.69) | 0.09 | 0.09 |
| | 50 | 49% | 27% | 0.77 (0.72–0.80) | 0.14 | 0.10 |
| 1 km cell, night | 0 | 100% | 100% | 0.14 (0.05–0.17) | 0.72 | 0.75 |
| | 20 | 58% | 15% | 0.57 (0.44–0.58) | 0.45 | 0.15 |
| | 50 | 25% | 5% | 0.75 (0.68–0.79) | 0.64 | 0.22 (9 zero months) |
| Hotspot, day | 0 | 100% | 100% | 0.20 (0.19–0.23) | 0.17 | 0.15 |
| | 20 | 80% | 35% | 0.47 (0.44–0.53) | 0.16 | 0.16 |
| | 50 | 50% | 14% | 0.75 (0.69–1.05) | 0.45 | 0.42 |
| Hotspot, night | 0 | 100% | 100% | 0.055 (0.026–0.059) | 0.58 | 0.55 |
| | 20 | 59% | 3% | 0.93 (0.80–1.32) | 0.57* | 0.62 |

\*Three fire seasons had no Suomi NPP night hotspot at or above 20 MW and are left out of that CV.

## What this implies

- The team could say that Aqua misses most small fires that Suomi NPP sees and catches most large ones. That is the reason for the factor of about 5 by day and 18 at night. The team could not quote a single "MODIS detection limit" from these data: the 50% point moves between 12 and 70 MW with the definition and between about 8 and 47 MW across years.
- A detection-curve conversion does not beat day and night factors in any subset tested, and over all months it is measurably worse than one factor because it over-predicts quiet months. That is the opposite of the case where a curve was expected to help (small or quiet areas). The published limit formula does no better. This agrees with the earlier finding that a fitted curve is "not supported".
- A common threshold makes daytime cell ratios steadier across years. It does not make them equal to 1, and it does not cut single-month error in large months. At night it does cut error in large months (0.75 to 0.15 at 20 MW for cells), but it keeps 15% of Suomi NPP night cells, and many months then have no record at all. It is a usable unit only if the team accepts discarding most of the VIIRS record, and it still needs a factor.

## Limits

- Detection is measured only where Suomi NPP flagged fire, at slightly different times and view angles. Cloud, smoke and timing are folded into the curve, and the swath-edge effect cannot be tested because missed cells have no Aqua view angle.
- The power values are Suomi NPP shares of a 750 m pixel's power, summed. They are not MODIS power.
- Only Aqua is analysed. Terra, the drift period and areas smaller than the box are not tested, and no calendar classes were scored here.
- Ten years: the 90% points and every comparison between methods carry wide intervals.

## How it was computed

The analyst's scripts `a08_check.py`, `a08_build.py`, `a08_fit.py`, `a08_emul.py` and `a08_thresh.py` were re-run from a clean output folder and reproduced every number in the draft. The reviewer's script `scripts/a08-completeness_review.py` was written independently. It rebuilds the cells with its own neighbour lookup and fits the curves by its own maximum likelihood with year-weighted bootstraps. It adds three things: neighbourhood-power and isolated-cell fits with P50 by year; a check of whether each sensor recorded anything that half-day; and paired leave-one-year-out scores with a published-midpoint curve. Its outputs are `out/a08_rev_fits.csv`, `a08_rev_p50_by_year.csv`, `a08_rev_bins.csv`, `a08_rev_emulator.csv`, `a08_rev_threshold.csv` and `a08_rev_log.txt`. The analyst's original outputs are kept in `out/a08_analyst_orig/`.
