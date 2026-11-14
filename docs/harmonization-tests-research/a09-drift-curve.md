# Using the orbit drift to trace the daily fire cycle

## Answer

Terra's daytime count fell steadily as its pass moved from 11:04 to 09:20. Allowing for the size of each fire year, it reached 0.91, 0.87, 0.81, 0.71 and 0.50 of its expected level in 2022–2026. Only 2026 is outside the year-to-year scatter of the stable years: its 95% prediction interval is 0.41–0.61.

A daily-cycle curve with the published width (2.81 h) but its peak left free fits Terra and Aqua daytime counts together with a peak at 13.4 h (95% interval 12.7–13.8). That is about 1.2 h earlier than the published 14.57 h. Fitted on 2012–2024 only, this curve predicts Terra daytime 2025 and 2026 to within 3–4% (measured ÷ predicted 1.03 and 0.97). Once single-year scatter is included, the 95% intervals are wide: 0.48–2.24 for 2025 and 0.69–1.72 for 2026. The published curve over-corrects Terra by 26% and 37% in 2025–2026, and it wrongly predicts a gain for Aqua.

Only the Terra daytime arc has a clear shape. Terra's evening arc is flat. The Aqua daytime and night arcs move only in 2026, by 0.90 and 0.70. The data support a correction for Terra daytime counts that carries a wide interval and rests on one decisive year (2026). For every other drift-period MODIS series they support flagging, not correcting.

## Evidence

**Definitions.**

- **Size-adjusted level**: a year's MODIS count divided by the count expected from the matching VIIRS count. The expectation comes from a Poisson fit of log(monthly MODIS) on log(monthly VIIRS) over the stable years 2012–2021, so the fit allows for the size of the fire year. A level of 1.0 means "as in 2012–2021".
- **VIIRS reference**: Suomi NPP through 2025, and NOAA-20 × k wherever Suomi NPP is masked. That covers 2022-07, 2022-08 and all of April–October 2026. The factor k is 1.034 by day and 1.001 at night, fitted on 2018–2025.
- **Pass time**: the median local solar hour of that pass's hotspots in each month.
- **Fit interval**: from refitting on resampled whole years.
- **Prediction interval**: also adds the scatter that a single year shows. That scatter is estimated from the stable years' year-level over-dispersion, which is 24 for Terra by day.

**Data.** All tables use fire-season months (April–October) of 2012–2026, local-date months, `use == True`, and the whole box. November 2026 is excluded. Standard rows are used, plus the near-real-time rows of September–October 2026: 94 Terra and 117 Aqua rows.

**Months handled.** Each arc has 105 candidate months.

- Outage months were removed: Terra 2022-10, and Aqua 2020-08, 2020-09 and 2022-04.
- Months with a zero VIIRS count were removed: 3 for Terra by day, 3 for Aqua by day, and 1 each at night.
- That leaves 101 valid months for Terra by day, 99 for Aqua by day, 103 for Terra at night and 101 for Aqua at night.
- Months with zero MODIS hotspots were kept, because the Poisson model handles them: 5 for Terra by day, 7 for Aqua by day, 25 for Terra at night and 41 for Aqua at night.
- No calendar classes are used, so no month is unclassifiable.

**Check.** The specification's check numbers were reproduced exactly: 116 months, MODIS 48,233, Suomi NPP 198,916, ratio 0.2425, day 0.343 and night 0.177.

**Table 1. Arcs by year.** Each cell gives the pass time, the size-adjusted level, and the 95% prediction interval. Stable-year levels are leave-one-year-out.

| Year | Terra day | Aqua day | Terra evening | Aqua night |
|---|---|---|---|---|
| 2012–21 range (all ten years) | 11:14; 0.62–1.61 | 12:57; 0.91–1.42 | 21:47; 0.55–1.05 | 02:12; 0–1.19 |
| 2012–21 range (2017, 2018, 2021 only) | 0.84–1.08 | 0.92–1.05 | 0.88–1.02 | 0.87–1.03 |
| 2022 | 11:04; 0.91 (0.56–1.46) | 13:06; 1.14 (0.91–1.43) | 21:35; 0.96 (0.75–1.23) | 02:19; 1.19 (0.79–1.81) |
| 2023 | 10:44; 0.87 (0.68–1.11) | 13:09; 0.95 (0.84–1.08) | 21:21; 0.95 (0.84–1.06) | 02:31; 1.05 (0.86–1.28) |
| 2024 | 10:32; 0.81 (0.53–1.25) | 13:31; 1.07 (0.86–1.35) | 21:09; 1.14 (0.92–1.42) | 02:57; 1.12 (0.75–1.68) |
| 2025 | 10:04; 0.71 (0.40–1.26) | 14:15; 1.07 (0.79–1.45) | 20:39; 1.07 (0.78–1.47) | 03:28; 0.97 (0.52–1.80) |
| 2026 | 09:20; **0.50 (0.41–0.61)** | 14:51; 0.90 (0.81–0.99) | 20:00; 1.09 (0.99–1.20) | 04:12; **0.70 (0.60–0.82)** |

Across all ten stable years, the leave-one-year-out levels have a standard deviation of log of 0.28 for Terra by day. Across the three large fire years it is 0.13. Within the drift years, monthly pass time hardly varies inside a year (for Terra by day in 2026, 09:13–09:25). Binning by pass time therefore adds nothing beyond the yearly table.

**Table 2. Fitted peak of a Gaussian daily curve, width fixed at 2.81 h.** Fitted on all 15 years, with the size term fitted alongside.

| Fit | Peak (h) | 95%, drift and stable years resampled separately | 95%, all years resampled together* | Peak if fitted on 2012–2024 |
|---|---|---|---|---|
| Terra daytime alone | 13.2 | 12.3–14.6 | 12.2–14.3 | 13.1 |
| Aqua daytime alone | 13.5 | 12.2–14.0 | 12.9–14.0 | 13.0 |
| Terra and Aqua daytime together | 13.4 | 12.7–13.8 | 12.8–13.8 | 13.0 |
| Together, width also free | 13.4, width 2.9 h | 12.8–14.0; width 2.2–3.9 | | |

\*About 5% of the replicates had fewer than two distinct drift years and were dropped. Terra alone samples only the rising flank of the curve (09:20–11:15), so it cannot pin the peak and the width separately. Neither interval for the joint fit includes the published 14.57 h.

**Table 3. Terra daytime out of sample, measured ÷ predicted (1.0 is a perfect prediction).**

| Model | Trained on 2012–2024: 2025 | Trained on 2012–2024: 2026 | Leave one drift year out, root-mean-square log error over 2022–26 |
|---|---|---|---|
| No correction | 0.71 (0.39–1.28) | 0.50 (0.37–0.65) | 0.37 |
| Published curve (peak 14.57 h) | 1.26 (0.59–2.45) | 1.37 (0.92–1.97) | 0.18 |
| Gaussian, peak free, fitted jointly with Aqua | 1.03 (0.48–2.24) | 0.97 (0.69–1.72) | 0.04 |
| Log-linear in pass time | 0.99 (0.53–2.12) | 0.83 (0.62–1.43) | 0.10 |
| Linear trend in year, no pass time | 0.94 (0.49–1.92) | **0.70 (0.54–0.96)** | 0.19 |

The intervals are prediction intervals. With fit uncertainty alone, the joint Gaussian gives 0.91–1.46 for 2025 and 0.78–1.78 for 2026, as the analyst reported.

**Table 4. Terra daytime level after correction.** Each year's correction comes from the joint Gaussian fitted with that year left out.

| Year | Hotspots | Raw level | Corrected | 95% fit only | 95% prediction |
|---|---|---|---|---|---|
| 2022 | 360 | 0.91 | 0.98 | 0.89–1.05 | 0.59–1.74 |
| 2023 | 1,320 | 0.87 | 1.01 | 0.88–1.08 | 0.76–1.30 |
| 2024 | 393 | 0.81 | 1.03 | 0.94–1.11 | 0.64–1.67 |
| 2025 | 191 | 0.71 | 1.08 | 0.95–1.19 | 0.50–2.22 |
| 2026 | 1,120 | 0.50 | 1.02 | 0.85–1.21 | 0.74–1.44 |

All five corrected values lie inside the stable range (0.62–1.61 over all ten years, 0.84–1.08 over the large years).

**Table 5. Other arcs: slope per hour of later pass, log scale, all 15 years (95%).**

| Arc | Pass, stable → 2026 | Slope per hour | Shape |
|---|---|---|---|
| Terra day | 11:14 → 09:20 | +0.36 (0.19 to 0.48) | Clear |
| Aqua day | 12:57 → 14:51 | −0.06 (−0.18 to +0.05) | Weak; only 2026 is low |
| Terra evening | 21:47 → 20:00 | −0.05 (−0.16 to +0.14) | Flat |
| Aqua night | 02:12 → 04:12 | −0.17 (−0.25 to +0.20) | Too noisy; 2026 low at a pass near dawn |

**Cross-sensor test.** The curve fitted on Terra alone (peak 13.2 h) predicts Aqua daytime 2026 at measured ÷ predicted 1.06 (0.71–1.32). The published curve gives 0.76 (0.64–0.85) and no curve gives 0.90 (0.75–1.00). The test rejects the published peak. It cannot separate a peak near 13 h from no curve at all for Aqua.

**Table 6. Contrast against NOAA-20: drift years against 2018–2021, size-adjusted.** Ratio of sums of observed over expected, years resampled within each block.

| Series | 2022–26 | 2022–25 | 2026 | Placebo 2020–21 against 2018–19 | Analyst's version (mean of yearly logs), 2022–26 |
|---|---|---|---|---|---|
| Terra day | 0.69 (0.51–0.92) | 0.87 (0.71–0.94) | 0.49 (0.44–0.51) | 0.87 | 0.74 |
| Aqua day | 0.98 (0.86–1.09) | 1.06 | 0.90 (0.82–0.92) | 0.89 | 1.00 |
| Terra evening | 1.01 (0.94–1.70) | 0.96 | 1.07 | 1.11 | 1.31 |
| Aqua night | 0.88 (0.71–1.13) | 1.05 | 0.69 (0.64–0.76) | 0.91 | 0.89 |
| MODIS, all four passes | 0.92 (0.85–1.10) | 0.98 | 0.85 (0.82–0.97) | 0.96 | 0.96 |

The 2018–2021 block has four years and the placebo blocks have two. Bootstrap intervals for blocks that small are unreliable, so the placebo values are shown as point estimates of the method's noise. The 2022–2025 Terra daytime contrast (0.87) equals its placebo (0.87). Only 2026 stands clearly apart.

## What this implies

- **What the team could claim.** Terra's daytime count fell to about half its expected level in 2026, and the earlier years' decline is consistent with the earlier pass. A daily curve peaking near 13.4 h, with the published width, removes that bias for Terra by day, and it passed a test on 2025–2026 that was held out of the fit.
- **What the team could not claim.**
  - A corrected single drift year is not accurate to better than about −30% to +70% (95%) in 2026, and it is worse in small years. The correction removes a bias. It does not restore precision.
  - The published curve is not usable as published. It over-corrects Terra by 26–37% and fails for Aqua.
  - Nothing in this analysis supports correcting Aqua by day, Aqua at night or Terra's evening pass. For those series, flagging 2026 or the whole drift period is what the data support.
- **The validation is thin.** The curve beat a plain trend in year on exactly one held-out year (2026: 0.97 against 0.70). That is evidence that pass time, rather than steady ageing, drives the decline. It does not exclude other changes that sped up in 2026.
- **The combined total is a cancellation.** The MODIS total across all four passes is close to normal through 2025 (0.98) and about 15% low in 2026. That holds only because the passes move in different directions, so it says little about any single pass.

## Limits

- The test rests on five drift years and one drift path for each sensor. Pass time and calendar year move together, so only the acceleration in 2026 separates them.
- The 2026 reference is NOAA-20 × k. An error of a few percent in k shifts every 2026 level by the same amount.
- The size model is a power law. It fits small fire years poorly: stable small years range from 0.6 to 1.6.
- The published curve describes fire radiative power over a continent, not hotspot counts. A count curve for Interior BC peaking earlier is plausible but has not been checked against an independent daily cycle, such as one from geostationary satellites.
- The results are box-wide only. Circles of 25–100 km will be far noisier.
- Night passes cannot be fitted with a daytime Gaussian.

## How it was computed

The analyst's scripts were re-run from a clean start and reproduce the draft. These include `scripts/a09_arcs.py`, `scripts/a09_fit.py`, `scripts/a09_joint.py` and `scripts/a09_contrast.py`.

The reviewer's independent script, `scripts/a09-drift-curve_review.py`, takes about one minute. It writes `out/a09-drift-curve_review_{arcs,peaks,slopes,oos,contrast}.csv` and a log. It:

1. builds the monthly table and the VIIRS reference;
2. fits the stable-year Poisson size model and computes leave-one-year-out levels;
3. estimates year-level over-dispersion for the prediction intervals;
4. fits the Gaussian curves (width fixed, and both free), the log-linear model, the year-trend model and the published curve;
5. runs the 2012–2024 test, the leave-one-drift-year-out test and the cross-sensor test, with 300 year-block replicates;
6. computes the NOAA-20 contrast as a ratio of sums.
