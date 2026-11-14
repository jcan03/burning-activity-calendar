# Do MODIS and VIIRS rank months the same way against their own history?

## Answer

Mostly yes for the order of months, but only partly for the class label. Over the stable-orbit period (February 2012 to December 2021), the ratio of a month's hotspot count to its own sensor's same-month median agrees closely between MODIS (Terra plus Aqua) and Suomi NPP: Spearman 0.97 (95% interval 0.94 to 0.99) for 48 fire-season months, and 0.92 to 0.95 for all months. On the five-class scheme, the two sensors give the same class in 71% of those 48 months (Cohen's kappa 0.63, interval 0.49 to 0.77) and are never more than one class apart. That agreement comes almost entirely from extreme months: when either sensor puts a month between 0.5 and 2 times the median, they agree on only 11 of 25 months (44%). For 2022 to 2025, during the MODIS orbit drift, the two sensors gave the same class in 13 of 16 comparable fire-season months, which is no worse than in the stable period. Switching the MODIS baseline from 2012–2021 to 2001–2021 changes the class of 8% of fire-season months (4 of 48). Switching it to 2003–2021 changes 21% (10 of 48). The choice of baseline years therefore matters about as much as the choice of sensor.

## Evidence

Terms used here. The **ratio** is a month's count divided by the median count for the same calendar month over the baseline years (2012–2021 unless stated). The **five classes** split that ratio at 0.5, 0.8, 1.25 and 2. The **percentile** is the share of baseline years with a lower count, with ties counted as half. **Thirds** splits the percentile at 1/3 and 2/3. **Kappa** is agreement corrected for chance (1 means perfect agreement, 0 means chance level). The **median floor** drops a calendar month when either sensor's median is below the floor. The intervals come from a bootstrap that resamples whole years, 2000 times. Counts are all type-0 (vegetation fire) hotspots per UTC month, with day and night combined unless stated. No calendar-month median is zero. The smallest MODIS medians are 6 (June), 7 (January and February), 8 (May) and 12.5 (April).

**Table 1. MODIS against Suomi NPP, stable period. 3 MODIS outage months removed (2016-02, 2020-08, 2020-09); no Suomi NPP outages.**

| Set | Months | Dropped by floor | Spearman [95%] | Same class | Within one class | Kappa [95%] | Same third (kappa) |
|---|---|---|---|---|---|---|---|
| All months, no floor | 116 | 0 | 0.92 [0.88–0.95] | 66% | 94% | 0.57 [0.45–0.67] | 72% (0.57) |
| Apr–Oct, no floor | 68 | 0 | 0.94 [0.88–0.97] | 68% | 93% | 0.59 [0.47–0.72] | 75% (0.62) |
| All months, floor 10 | 78 | 38 | 0.95 [0.91–0.97] | 68% | 97% | 0.60 [0.48–0.71] | 71% (0.56) |
| **Apr–Oct, floor 10** | **48** | 20 (all May and June) | **0.97 [0.94–0.99]** | **71%** | **98%** | **0.63 [0.49–0.77]** | **77% (0.66)** |
| Apr–Oct, floor 50 | 29 | 39 | 0.98 [0.92–1.00] | 83% | 100% | 0.77 [0.61–0.91] | 86% (0.79) |
| Apr–Oct, floor 10, day only | 48 | 20 | 0.96 [0.90–0.99] | 77% | 100% | 0.71 [0.58–0.83] | 75% (0.63) |
| Apr–Oct, floor 10, night only | 29 | 39 | 0.98 [0.88–0.99] | 79% | 100% | 0.72 [0.56–0.86] | 79% (0.69) |

**Table 2. Confusion matrix for the 48 Apr–Oct months with floor 10. Rows are the MODIS class; columns are the Suomi NPP class.**

| MODIS \ Suomi NPP | <0.5 | 0.5–0.8 | 0.8–1.25 | 1.25–2 | >2 |
|---|---|---|---|---|---|
| <0.5 | 12 | 1 | 0 | 0 | 0 |
| 0.5–0.8 | 2 | 4 | 3 | 0 | 0 |
| 0.8–1.25 | 0 | 0 | 3 | 2 | 0 |
| 1.25–2 | 0 | 1 | 2 | 4 | 2 |
| >2 | 0 | 0 | 0 | 1 | 11 |

- In 23 of the 48 months, both sensors put the month below 0.5 or above 2, and they agree on all 23. In the other 25 months, they agree on 11 (44%). Six of the 14 disagreements are Aprils, where MODIS counts are 7 to 23.
- Within a single calendar month, the sensors rank the 9 or 10 years almost identically from July to October (Spearman 0.94 to 0.99), less well in May and June (0.83), and worst in April (0.65).
- Grouping months by local solar date instead of the UTC month changes nothing material (Spearman 0.969 against 0.971).

**Table 3. Practical question 1: the MODIS class under a 2001–2021 or 2003–2021 baseline instead of 2012–2021. No month moved by more than one class.**

| Months tested | Alternative baseline | Apr–Oct, floor 10 | All months, no floor |
|---|---|---|---|
| 2012–2021 | 2001–2021 | 4 of 48 (8%, 2–17%) | 24 of 116 (21%, 13–28%) |
| 2012–2021 | 2003–2021 | 10 of 48 (21%, 10–33%) | 35 of 116 (30%, 22–38%) |
| 2022–2025 | 2001–2021 | 1 of 18 (6%, 0–17%) | 5 of 45 (11%, 2–20%) |
| 2022–2025 | 2003–2021 | 3 of 18 (17%, 0–33%) | 12 of 45 (27%, 13–40%) |

The 2001–2021 baseline is Terra-only until July 2002, which lowers the early-year counts. Dropping those years (the 2003–2021 baseline) raises the August and September medians by 28% and 44% compared with 2012–2021. The interval on each share comes from resampling months.

**Table 4. Practical question 2: 2022–2025, with each sensor's month compared against its own 2012–2021 history.**

| Set | Months compared | Outage months removed | Removed by floor | Same class | Within one class | Kappa | Same third |
|---|---|---|---|---|---|---|---|
| Apr–Oct, floor 10 | 16 | 4 | 8 (May and June) | 13 (81%) | 100% | 0.74 | 94% |
| Apr–Oct, no floor | 24 | 4 | 0 | 17 (71%) | 96% | 0.61 | 92% |
| All months, floor 10 | 26 | 6 | 16 | 18 (69%) | 96% | 0.61 | 88% |

The three disagreements with floor 10 are 2024-04 (MODIS 13 hotspots), 2025-04 (MODIS 9 hotspots) and 2025-07. July 2025 overlaps a Suomi NPP partial-loss period (3 to 8 July) that the outage rule does not mask. Without it, 13 of 15 months agree. With no floor, the extra disagreements are May and June months with MODIS counts of 1 to 11.

**Table 5. Level check: Suomi NPP count divided by MODIS count, Apr–Oct months with at least 20 hotspots from each sensor.**

| Hotspots | Stable 2012–2021: median (IQR), months; range of yearly pooled ratios | Drift 2022–2025: median (IQR), months; range of yearly pooled ratios |
|---|---|---|
| Day and night | 3.7 (2.9–4.3), 38 months; 2.4–5.7 | 3.9 (3.4–4.5), 16 months; 3.8–4.4 |
| Day | 2.7 (2.2–3.2), 31 months; 1.7–3.2 | 2.6 (2.2–3.3), 16 months; 2.4–3.1 |
| Night | 6.7 (5.3–8.1), 23 months; 5.2–7.8 | 5.7 (5.3–7.9), 11 months; 4.8–5.6 |

NOAA-20 divided by Suomi NPP, over 35 Apr–Oct months from 2019 to 2025: median 0.98 (IQR 0.94–1.11).

## What this implies for the approach

- **Unit.** Anomalies against each sensor's own history remove the need for a cross-sensor factor only when the current month and its baseline come from the same sensor over the same years. The scale factor cancels, and the order of months is preserved (Spearman about 0.95). The exact label is not preserved in the middle classes. Under this scheme, a user would see a different label for about a third of months depending on the sensor, and for more than half of months that are near normal.
- **Target record.** Suomi NPP has 2.4 to 9 times as many hotspots per month (comparing calendar-month medians), so its spring and winter labels are less noisy than MODIS labels, which rest on medians of 6 to 12 hotspots. Most MODIS disagreements are low-count Aprils, Mays and Junes. Whichever record is chosen, those months need either a count floor or coarser classes.
- **Scaling.** Scaling is still needed wherever the baseline reaches back before 2012 and the current month comes from VIIRS. The day and night factors differ by more than two to one (2.7 against 6.7), so a single factor for day and night together would be distorted by changes in the day/night mix.
- **Combining VIIRS satellites.** NOAA-20 tracks Suomi NPP at about 1.0. The two can be averaged, or one can stand in for the other, but they must not be summed against a Suomi NPP baseline. This matters now that Suomi NPP has ended (2 November 2026).
- **MODIS since 2022.** These data show no detectable drift effect on either labels or levels from 2022 to 2025. With only 16 comparable months and 4 drift years, that is weak evidence.
- **Baseline years** change labels about as often as changing the sensor does. The baseline period should be fixed, stated, and kept to years with the same sensor mix.

## Limits

The comparisons are in-sample: the month being tested is inside its own baseline. The stable period has only 10 years, so each median rests on 9 or 10 values. The drift test has 16 fire-season months. The only VIIRS satellite tested against MODIS is Suomi NPP. Counts are raw: they are not corrected for MODIS duplicate detections, cloud cover or confidence. Partial-loss periods are not masked. This analysis cannot show whether a calendar built from NOAA-20 or from several satellites would match a Suomi NPP baseline, or how MODIS labels behave after 2025.

## How it was computed

The analyst's script `scripts/m05_anomaly.py` was re-run, and its log matched. The review script `scripts/m05-anomaly-agreement_review.py` was written independently. It counts type-0 hotspots per month for each sensor group, masks months that overlap an outage gap, builds medians and percentiles for each calendar month (leaving out January 2012), and computes the agreement statistics with a year-block bootstrap. It also covers day only, night only and local-date months, the alternative baselines, 2022–2025, and the level ratios. Outputs are the CSV files in `out/` whose names start with `m05-anomaly-agreement_review_`, plus the run log.
