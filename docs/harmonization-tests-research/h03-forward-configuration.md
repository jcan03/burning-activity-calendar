# h03: The configuration after Suomi NPP (NOAA-20 and NOAA-21 against a mixed baseline)

> Working file from the fourth follow-up (14 November 2026). The series, class schemes (`R5`, `P5`) and designs (`U1`, `SV`) are defined in [h00-definitions.md](h00-definitions.md), which is what "the spec" means below. The scripts and tables named here are kept outside version control with the cached data.

## 1. Summary

- The checks in the spec reproduced (116 stable months: M 48,233, S 198,916, ratio 0.2425; six C values within 0.1%; protocol B whole box 84.4% / 79.7% for U1 and 66.1% / 64.5% for SV).
- **Real configuration (C2 = NOAA-20 + NOAA-21, classed against U1, the converted-MODIS plus Suomi baseline), whole box, March 2023 to October 2026.** Exact agreement with the label the full record gives (C against ten years of Suomi NPP): R5 86.5% in Apr-Oct (28 months) and 78.1% over all 44 months; P5 82.2% and 72.0%. Within one class: 99.5% (R5) and 99.8% (P5) in Apr-Oct.
- **Benchmark SV (five VIIRS years only):** R5 66.3% (Apr-Oct) and 62.3% (all); P5 60.0% and 58.8%. The **gain of U1 over SV** in Apr-Oct is +20.2 points (R5, year-block 95% interval +14.7 to +26.0) and +22.2 points (P5, +17.5 to +28.8). Over all months it is +15.8 (R5) and +13.2 (P5). The gain, averaged over the 202 splits, is positive in every box and circle cell, every season and all four schemes. It is not positive in every single split: for C2 in the box, 0 to 7% of splits have a negative gain and the 5th percentile of the per-split gain is between -5 and +7 points. The interval rests on only four or five year blocks, covers test-year sampling only (not which years are pretend-MODIS), and is 4 to 30 points wide in the box and 4 to 10 in circles.
- **Source effect is small next to baseline effect.** C2 against the full baseline agrees with the truth in 97.7% (R5, all months) and 95.5% (P5). C2 / C summed over March 2023 to October 2026 is 1.001, and 0.998 to 1.004 by year (confirms f03). Single months can differ a lot when counts are tiny or a satellite is out (0.74 to 1.12 over all 44 months). NOAA-20 alone and NOAA-21 alone agree less (R5 89% and 93%).
- **Circles (100 km, 31 circles pooled)** show the same direction with smaller R5 gains: C2/U1 82.3% against SV 73.7% in Apr-Oct R5 (+8.6, interval +6.1 to +11.8); P5 +17.4 (+13.5 to +21.9). Circle source effect is larger (C2 against full 91% R5).
- **How hard the test is:** in the box 43% of Apr-Oct months (60% May-Sep, 70% Jun-Sep) fall in the top R5 class, because of 2023 and 2026. Rank classes spread more evenly (31% top class in Apr-Oct). The test is partly easy for the ratio scheme at the top and hard in the middle classes.

## 2. Method

Scripts are listed in section 6; all use the spec's data, filters and constants.

- **Monthly series** (`h03_build.py`): daily counts by local date and sensor from `hotspots_v2.parquet` (`use == True`), for the box and the 31 circles at 100 km, with the round 4 `daily_cube` loader. Availability: `avail_cat_plus_partial` (via f03_common `load_avail`, kind `n`, mode `cat_list_partial`), AND in service, with NOAA-20 forced available 2018-04-01 to 2018-06-04. Scale factors 1, 1.0245, 1.0503. `C` = daily mean of available VIIRS satellites (scaled), days with none count 0, summed by month. `C2` = same with NOAA-20 and NOAA-21 only (defined from 2023-03; NaN before). `N20s`, `N21s` = monthly hotspot sums times the scale factor, with no availability masking, as the spec defines them (so they fall under C when the satellite had flagged days). `N21s` NaN before 2023-03. `S` as a source = raw Suomi NPP, kept only for months in which all days were flagged available (37 of 58 months; the other 21 had at least one Suomi NPP day out).
- **Test months**: 2022-01 to 2026-10 (58 months; 44 from 2023-03). **Baseline years**: the ten stable years, valid cells only (stable months, without 2016-02, 2020-08, 2020-09; a year missing for a calendar month is dropped from that baseline, in every design). For every split, `f` = M/S ratio of sums on the box over the five VIIRS-era years of the split (valid cells). Circles use the box factor.
- **Splits**: the 202 standard splits (two chronological, 200 from `default_rng(1)`, same draw as a01). Pretend-MODIS years: baseline value = M / f. VIIRS-era years: S. `SV`: only the five VIIRS-era years. `full`: S, all ten years. The test month's year is never in the baseline.
- **Truth**: class of `C` against `full`. Second truth: class of S (months with all days available) against `full`. Designs = (source, baseline). "Source effect alone" = source against `full`. "Baseline effect alone" = C against U1 or SV. "Both" = C2 against U1 or SV.
- **Classes**: R5 and R3 (classifiable when baseline median is at least 1), P5 and P3 per the spec (pct with half-credit for ties; uncertain when 20% or more of baseline values equal v; P3 cuts at 1/3 and 2/3), computed in `h03_run.py:classify`. Truth months not classifiable are dropped from every denominator (none in the box; 0.6 to 1.8% of P5 circle months).
- **Scores**: exact agreement = (predicted class equals truth) over truth-classifiable months, where a design that cannot classify counts as a miss and is also reported as NC. Within one = absolute class difference at most 1. Kappa: Cohen's, pooled over months and splits, among pairs both classifiable. P schemes also: mean absolute pct difference and agreement on "highest on record" (v above every baseline value). Pooled over the 202 splits (months averaged over splits).
- **Intervals**: year-block bootstrap, 2,000 draws, resampling the test years present in the sample (five years for Jan 2022 samples; four, 2023 to 2026, for C2 and N21s samples). Circles: all 31 circles' rows are resampled together by year. Gain intervals use the same draws for U1 and SV. "SD splits" = standard deviation across the 202 splits of the gain in exact agreement (per-split gain computed over the sample's rows).
- Reported on whole box and the 31 circles at 100 km pooled. 50 km and 150 km were not run.

## 3. Results

Agreement in %, gain in percentage points, interval = year-block 95%. Full tables: `h03_scores.csv`, `h03_gains.csv`; compact text version `h03_report_tables.md` (every cell below is in it, plus R3/P3 and circle R3/P3).

### 3.1 True-class shares (truth = C against full), box, months from Jan 2022 (R5 classes 0 to 4: below 0.5 ... above 2)

| scheme | season | months | c0 | c1 | c2 | c3 | c4 |
|---|---|---|---|---|---|---|---|
| R5 | Apr-Oct | 35 | 14% | 20% | 11% | 11% | **43%** |
| R5 | May-Sep | 25 | 12% | 16% | 4% | 8% | **60%** |
| R5 | Jun-Sep | 20 | 5% | 10% | 5% | 10% | **70%** |
| R5 | all | 58 | 21% | 16% | 21% | 12% | 31% |
| P5 | Apr-Oct | 35 | 11% | 17% | 17% | 23% | 31% |
| P5 | May-Sep | 25 | 12% | 8% | 12% | 28% | 40% |
| P5 | Jun-Sep | 20 | 0% | 5% | 15% | 35% | 45% |
| P5 | all | 58 | 16% | 17% | 21% | 22% | 24% |

Circles (pooled, 31 x 35 = 1,085 Apr-Oct rows): R5 top class 42%, class 0 29%; P5 top class 29%. Circle P5 not classifiable (truth) 1.0% of Apr-Oct rows.

### 3.2 Real configuration, box (C2 from March 2023; "gain" is U1 minus SV)

| scheme | season | months | C2 vs full | C2 U1 | C2 SV | gain [95% CI] | SD splits | kappa U1 / SV | within-1 U1 / SV |
|---|---|---|---|---|---|---|---|---|---|
| R5 | Apr-Oct | 28 | 100.0 | 86.5 | 66.3 | +20.2 [+14.7, +26.0] | 8.3 | 0.81 / 0.54 | 99.5 / 93.7 |
| R5 | May-Sep | 20 | 100.0 | 89.8 | 72.6 | +17.2 [+8.0, +24.9] | 11.3 | 0.83 / 0.55 | 99.3 / 91.6 |
| R5 | Jun-Sep | 16 | 100.0 | 88.9 | 72.2 | +16.7 [+8.6, +23.9] | 12.9 | 0.78 / 0.46 | 99.1 / 89.5 |
| R5 | all | 44 | 97.7 | 78.1 | 62.3 | +15.8 [+12.4, +19.6] | 9.5 | 0.72 / 0.51 | 98.9 / 94.2 |
| P5 | Apr-Oct | 28 | 96.4 | 82.2 | 60.0 | +22.2 [+17.5, +28.8] | 11.9 | 0.76 / 0.47 | 99.8 / 97.4 |
| P5 | May-Sep | 20 | 95.0 | 82.6 | 60.7 | +21.9 [+11.8, +31.9] | 15.2 | 0.75 / 0.44 | 100 / 97.6 |
| P5 | Jun-Sep | 16 | 93.8 | 86.0 | 62.1 | +23.9 [+8.7, +39.0] | 15.4 | 0.77 / 0.38 | 100 / 97.7 |
| P5 | all | 44 | 95.5 | 72.0 | 58.8 | +13.2 [+11.4, +15.4] | 9.1 | 0.65 / 0.48 | 99.5 / 96.8 |
| R3 | Apr-Oct | 28 | 100.0 | 94.4 | 80.1 | +14.3 [+11.3, +16.9] | 7.8 | 0.91 / 0.68 | 100 / 98.8 |
| R3 | all | 44 | 97.7 | 91.8 | 79.4 | +12.4 [+9.0, +15.4] | 6.9 | 0.87 / 0.67 | 100 / 99.2 |
| P3 | Apr-Oct | 28 | 96.4 | 94.8 | 75.8 | +19.0 [+16.5, +22.6] | 8.9 | 0.92 / 0.63 | 100 / 100 |
| P3 | all | 44 | 97.7 | 93.4 | 76.7 | +16.8 [+13.1, +19.7] | 7.1 | 0.90 / 0.65 | 100 / 100 |

(R3 and P3 May-Sep and Jun-Sep gains are +13.7 to +20.4, all intervals above zero; see `h03_report_tables.md`.) "C2 vs full" is the source effect alone; the rest of the gap to 100% in "C2 U1" is the baseline.

### 3.3 Real configuration, 31 circles at 100 km pooled (C2 from March 2023)

| scheme | season | months/circle | C2 vs full | C2 U1 | C2 SV | gain [95% CI] | SD splits | kappa U1 / SV |
|---|---|---|---|---|---|---|---|---|
| R5 | Apr-Oct | 28 | 91.4 | 82.3 | 73.7 | +8.6 [+6.1, +11.8] | 3.9 | 0.74 / 0.63 |
| R5 | May-Sep | 20 | 92.9 | 83.8 | 74.6 | +9.1 [+6.4, +10.9] | 4.9 | 0.74 / 0.61 |
| R5 | Jun-Sep | 16 | 95.4 | 86.0 | 76.4 | +9.6 [+6.1, +11.9] | 5.6 | 0.75 / 0.60 |
| R5 | all | 44 | 91.1 | 73.7 | 67.9 | +5.8 [+3.6, +8.4] | 5.3 | 0.65 / 0.58 |
| P5 | Apr-Oct | 27.7 | 93.0 | 79.0 | 61.6 | +17.4 [+13.5, +21.9] | 6.8 | 0.73 / 0.51 |
| P5 | May-Sep | 19.7 | 92.5 | 77.8 | 58.2 | +19.6 [+15.4, +24.7] | 9.4 | 0.71 / 0.45 |
| P5 | Jun-Sep | 15.7 | 95.9 | 82.2 | 60.3 | +21.8 [+17.5, +27.1] | 10.8 | 0.76 / 0.45 |
| P5 | all | 43.7 | 91.9 | 73.4 | 58.6 | +14.8 [+12.5, +17.6] | 5.9 | 0.66 / 0.48 |
| R3 | Apr-Oct | 28 | 94.8 | 88.7 | 80.5 | +8.1 [+5.6, +10.3] | 3.6 | 0.83 / 0.71 |
| P3 | Apr-Oct | 27.7 | 95.7 | 86.9 | 77.4 | +9.6 [+6.7, +12.5] | 6.5 | 0.80 / 0.66 |

(P rows: fewer than 28 months per circle on average because truth months with an uncertain rank class are dropped.)

Circle intervals are narrower than the box's because 31 circles are pooled, but circles in the same year share fire years, so they are not 31 independent samples; the year-block bootstrap resamples whole years for all circles together and is the honest width. The circle SV baseline fails to classify 0.8 to 1.4% of R5 rows (median below 1) against about 0.1% for U1.

### 3.4 Source effect alone (source against the full baseline), months from March 2023

| unit | scheme | season | C2 | N20s | N21s |
|---|---|---|---|---|---|
| box | R5 | Apr-Oct (28) | 100.0 [100, 100] | 89.3 [78.6, 100] | 92.9 [85.7, 100] |
| box | R5 | all (44) | 97.7 [93.5, 100] | 88.6 [83.3, 95.2] | 93.2 [90.0, 97.8] |
| box | P5 | Apr-Oct (28) | 96.4 [89.3, 100] | 89.3 [78.6, 100] | 92.9 [85.7, 100] |
| box | P5 | all (44) | 95.5 [85.7, 100] | 88.6 [81.0, 95.5] | 90.9 [80.0, 100] |
| circles | R5 | Apr-Oct (28) | 91.4 [89.4, 93.3] | 84.3 [80.9, 87.8] | 86.2 [81.9, 90.7] |
| circles | R5 | all (44) | 91.1 [88.6, 93.0] | 82.9 [80.1, 86.0] | 84.6 [82.3, 87.0] |
| circles | P5 | Apr-Oct (28) | 93.0 [90.9, 95.6] | 83.4 [78.7, 87.9] | 86.8 [83.0, 90.3] |
| circles | P5 | all (44) | 91.9 [89.9, 94.5] | 82.1 [78.0, 85.7] | 84.5 [80.8, 88.5] |

Within one class is 100% in the box for every source and 95.6 to 100% in circles (lowest: circle NOAA-20 alone, P5, Apr-Oct 95.6%, with 2.6% not classifiable). Kappa 0.85 to 1.00 in the box. NOAA-20 alone from January 2022 (35 Apr-Oct months): box R5 91.4%, P5 91.4%, circles R5 83.3%. R3 and P3 source effects (box 93 to 100%, circles 88 to 96%) are in `h03_report_tables.md`.

### 3.5 Baseline effect alone (C, all VIIRS, 58 months from Jan 2022), box

| scheme | season | months | U1 [95% CI] | SV [95% CI] | gain [95% CI] | SD splits | kappa U1 / SV |
|---|---|---|---|---|---|---|---|
| R5 | Apr-Oct | 35 | 86.5 [81.0, 91.0] | 65.5 [59.1, 72.8] | +20.9 [+16.5, +25.3] | 10.8 | 0.82 / 0.53 |
| R5 | May-Sep | 25 | 88.0 [79.4, 96.5] | 71.7 [62.3, 84.4] | +16.3 [+9.7, +22.7] | 14.1 | 0.80 / 0.54 |
| R5 | Jun-Sep | 20 | 87.4 [76.1, 97.5] | 71.9 [59.6, 85.2] | +15.5 [+10.0, +20.5] | 13.8 | 0.75 / 0.46 |
| R5 | all | 58 | 78.9 [69.8, 85.8] | 62.9 [57.3, 67.2] | +16.0 [+12.7, +18.9] | 10.4 | 0.73 / 0.53 |
| P5 | Apr-Oct | 35 | 84.9 [81.0, 89.1] | 58.8 [51.8, 65.8] | +26.2 [+20.7, +32.2] | 13.5 | 0.81 / 0.47 |
| P5 | May-Sep | 25 | 85.9 [82.2, 89.3] | 60.7 [52.1, 69.5] | +25.3 [+18.9, +31.6] | 16.5 | 0.81 / 0.46 |
| P5 | Jun-Sep | 20 | 90.2 [87.0, 95.3] | 61.8 [52.9, 70.7] | +28.4 [+17.0, +39.3] | 16.4 | 0.85 / 0.42 |
| P5 | all | 58 | 75.8 [70.5, 81.1] | 58.9 [53.7, 65.1] | +16.9 [+12.9, +22.2] | 9.7 | 0.69 / 0.48 |

Circles, same table: R5 Apr-Oct 81.3 / 73.7, gain +7.6 [+6.1, +9.3]; P5 Apr-Oct 81.4 / 62.2, gain +19.2 [+15.3, +22.9]; all months R5 +5.3, P5 +15.9. R3 and P3 in the CSV (gains +4.2 to +14.8 in circles, +9.3 to +23.0 in the box).

Rank extras (P5, C2, from March 2023): mean absolute pct difference from truth, U1 / SV: box 0.034 / 0.113 (Apr-Oct), 0.048 / 0.107 (all); circles 0.048 / 0.105 and 0.062 / 0.108. Agreement on "highest on record", U1 / SV: box 98.5 / 83.4% (Apr-Oct), 99.0 / 88.4% (all); circles 98.7 / 88.1% and 98.4 / 90.0%.

### 3.6 Truth = Suomi NPP (37 months with all days available; 27 of them from March 2023)

Box, all months: C against full 94.6% (R5, P5; 86.0 to 100); C2 against full 88.9% (R5), 85.2% (P5), n = 27. Mixed baselines: C U1 77.0% / SV 60.1% (R5), 70.0% / 55.4% (P5); C2 U1 75.7% / SV 58.5% (R5), 65.2% / 55.0% (P5). With Suomi NPP as truth the gain is +17 (R5) and +15 (P5) for C, +17 and +10 for C2, intervals in `h03_scores.csv` (e.g. C2 R5 U1 75.7 [64.0, 90.5], SV 58.5 [46.0, 72.1]; they overlap, but the gain is computed on the same draws). Circles: C U1 66.7% / SV 64.0% (R5), 69.3% / 58.1% (P5). The gap between "C against full" and 100% (about 5 points box, 15 to 18 circles) is the disagreement between combined VIIRS and Suomi NPP alone in the same months, not a design effect. The 37 months exclude every month in which Suomi NPP lost a day, and that includes most of the largest fire months (2022-07, 2022-08, 2023-07, 2024-07, 2026-07, 2026-08), so this sample under-represents the top class.

S as the current-month source (truth C, the same 37 months; added by the reviewer from `h03_scores.csv` / `h03-review_scores.csv`): box R5 against full 94.6%, U1 76.2% [63.6, 86.2], SV 63.0%, gain +13.1 [+7.5, +20.7]; P5 full 94.6%, U1 71.9%, SV 54.3%, gain +17.5 [+10.9, +23.1]. Apr-Oct (20 months): R5 gain +24.4, P5 +24.5. Circles, all months: R5 gain +4.9 [+1.7, +8.0], P5 +15.3 [+12.3, +18.8].

### 3.7 Context

- **C2 / C** (box, summed, March 2023 to October 2026; `h03_ratio_C2_C_by_year.csv`): 2023 1.004 (10 months), 2024 1.002, 2025 0.998, 2026 0.999 (10 months); all 1.001 (C = 100,259, C2 = 100,367). Apr-Oct and Jun-Sep are the same (1.001). N20s / C = 0.992 and N21s / C = 0.990 overall, but by year 0.955 to 1.026 (N20s) and 0.915 to 1.017 (N21s). Confirms f03: at the level of sums the two-satellite series is close to the three-satellite one. Month by month it is not always: ratio 0.74 to 1.12; five months outside 0.90 to 1.10 (2024-05 0.74, 2024-06 1.11, 2025-05 1.12, 2026-03 0.885, 2026-06 0.884), all with C below about 120 hotspots. Among the 29 months with C of at least 100 the ratio is 0.88 to 1.05.
- **Monthly values, box, Apr-Oct months** (hotspots; satellite-days available out of the days in the month; no month had a day with no satellite):

| month | C | C2 | N20s | N21s | days S/N20/N21 | month | C | C2 | N20s | N21s | days S/N20/N21 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2022-04 | 53 | - | 57 | - | 30/30/- | 2024-08 | 2,454 | 2,425 | 2,490 | 2,360 | 31/31/31 |
| 2022-05 | 16 | - | 16 | - | 31/31/- | 2024-09 | 135 | 140 | 150 | 130 | 28/30/30 |
| 2022-06 | 5 | - | 6 | - | 29/30/- | 2024-10 | 271 | 257 | 233 | 280 | 31/31/31 |
| 2022-07 | 629 | - | 610 | - | 25/31/- | 2025-04 | 50 | 50 | 48 | 52 | 30/30/30 |
| 2022-08 | 2,266 | - | 2,247 | - | 21/31/- | 2025-05 | 9 | 10 | 10 | 11 | 31/31/31 |
| 2022-09 | 4,083 | - | 4,098 | - | 30/30/- | 2025-06 | 16 | 15 | 13 | 16 | 30/30/30 |
| 2022-10 | 1,675 | - | 1,670 | - | 31/31/- | 2025-07 | 665 | 694 | 673 | 701 | 25/25/31 |
| 2023-04 | 102 | 100 | 93 | 107 | 30/30/30 | 2025-08 | 199 | 203 | 227 | 179 | 31/31/31 |
| 2023-05 | 116 | 111 | 98 | 123 | 31/31/31 | 2025-09 | 2,663 | 2,622 | 2,710 | 2,353 | 30/30/29 |
| 2023-06 | 742 | 741 | 702 | 779 | 30/30/30 | 2025-10 | 691 | 697 | 731 | 663 | 31/31/30 |
| 2023-07 | 4,751 | 4,743 | 3,657 | 4,675 | 29/27/31 | 2026-04 | 77 | 75 | 74 | 76 | 27/30/30 |
| 2023-08 | 24,200 | 24,293 | 23,874 | 24,712 | 31/31/31 | 2026-05 | 17 | 19 | 16 | 21 | 30/31/31 |
| 2023-09 | 1,678 | 1,712 | 1,690 | 1,734 | 30/28/30 | 2026-06 | 115 | 102 | 92 | 111 | 28/30/30 |
| 2023-10 | 855 | 847 | 876 | 818 | 31/30/31 | 2026-07 | 18,365 | 18,276 | 18,216 | 18,336 | 23/31/31 |
| 2024-04 | 40 | 43 | 47 | 38 | 29/26/30 | 2026-08 | 29,590 | 29,679 | 30,056 | 29,302 | 27/31/31 |
| 2024-05 | 10 | 7 | 8 | 6 | 29/31/31 | 2026-09 | 243 | 232 | 216 | 248 | 30/30/30 |
| 2024-06 | 22 | 24 | 28 | 21 | 27/30/29 | 2026-10 | 757 | 756 | 802 | 709 | 31/31/31 |
| 2024-07 | 7,102 | 7,164 | 7,328 | 6,379 | 18/31/30 | | | | | | |

- All 58 months (with raw S, total satellite-days and C2/C): `h03_context_months_box.csv` has, for each of the 58 months, C, C2, N20s, N21s, raw S, satellite-days available (Suomi NPP, NOAA-20, NOAA-21, all, NOAA-20 plus NOAA-21), days with no satellite, and C2/C.
- 21 of 58 test months have at least one Suomi NPP day out (for example 2022-07: 25 of 31 days; 2022-08: 21 of 31). Raw Suomi NPP in those months is far below C (2022-08: 1,022 against 2,266).

## 4. How strong

- **Solid**: the direction. U1 beats SV for C2 in every cell (box and circles, four schemes, four seasons), and by 12 to 24 points in the box and 5 to 22 in circles. Reproduction of the earlier 84.4 / 66 result on a different set of months (C instead of S, 2022 to 2026 instead of the stable years) with C against U1 giving 86.5% (R5, Apr-Oct) supports it. The source effect (C2 against full) is much smaller than the baseline effect, and C2 against C is within 0.5% in sums.
- **Weak**: the size of the gain. Only four (C2) or five test years exist, and 2023 and 2026 supply most of the top-class months. Box intervals for the gain are 7 to 30 points wide; the Jun-Sep P5 interval is +8.7 to +39.0. The standard deviation across splits (7 to 17 points) is a further spread: the result depends on which five years are the pretend-MODIS years. The bootstrap with four or five blocks has little coverage guarantee (four blocks give only 35 distinct resamples), and the splits reuse the same ten years. The interval covers test-year sampling only; in several cells it is narrower than the spread across splits (box R5 Apr-Oct: interval half-width about 6 points, split SD 8.3). The deployed calendar has one fixed baseline, so the per-split spread is the more relevant one for "how big will the gain be": for C2 in the box the 5th to 95th percentile of per-split gains is +7 to +36 (R5 Apr-Oct), 0 to +39 (P5 Apr-Oct), 0 to +32 (R5 all) and 0 to +30 (P5 all); in 0 to 7% of splits U1 does worse than SV.
- **Comparing schemes**: base rates differ. For R5 about 43 to 70% of fire-season box months are in the top class, so SV and U1 both get many right by predicting a high month is high. P5 spreads classes evenly, and SV is lower (59 to 62%) than for R5 (62 to 73%). For C2 in the box the P5 gain is larger than the R5 gain in the three seasonal windows (+2.0 Apr-Oct, +4.7 May-Sep, +7.2 Jun-Sep) but smaller over all months (-2.6). Kappa shows the same order (U1 0.65 to 0.83, SV 0.38 to 0.55).
- P3 and R3 are easier (U1 91.8 to 98%); a coarse grouping hides single-class errors that R5 and P5 expose.

## 5. Limits and surprises

- **Test of the future configuration is imitated, not observed.** Baselines use only the ten stable years, imitated mixing with S, where the pretend-MODIS values are real MODIS counts of those years, not drifted ones. The real calendar adds MODIS years back to 2000 to 2011 and 2022 onward. U1's 10-value baseline has a different length from the real one. **The benchmark is short by construction:** SV has four or five years, while the truth and U1 have nine or ten and U1 shares five of its values exactly with the truth baseline. In November 2026 the real VIIRS-only alternative would have 14 Suomi NPP years (2012-2025), not five, so the size of the gain here measures U1 against a five-year baseline and should not be read as the gain over the VIIRS-only option the team actually has.
- **Mixed C2 sample.** C2 starts in March 2023, so the 2022 months and the 2023 January and February months are only available for C and N20s. Rows labelled "C" in 3.2 and 3.3 are restricted to the same 44 months as C2; 3.5 uses all 58.
- **Surprise: U1 sometimes beats the source-effect ceiling** (for example box P3 May-Sep C2 U1 97.0% against C2 vs full 95.0%). Both are against the same truth, and with 20 months and four years a one-month swing is 5 points; read these as ties.
- **Surprise: in the circles, C2 against the full baseline is only 91 to 92% (R5, P5) while C2 itself agrees with C within 0.5% in the box sums.** Small circle counts make single hotspots move months across class edges. Raw N20s and N21s cell counts are not masked for flagged days, so NOAA-21 and NOAA-20 alone are lower in months with outages (for example NOAA-20 in 2023-07: 27 of 31 days, 3,657 against C 4,751).
- Ties and uncertain classes: P5 on the box never leaves a month unclassified in the truth. In circles, 0.6 to 1.8% of P5 truth months are uncertain (20% or more of baseline values tie, typically zeros); those are dropped from every denominator, and a design that is uncertain where the truth is not counts as a miss.
- Kappa is pooled across splits and not given an interval for the source-only rows; its gain is bootstrapped in `h03_gains.csv` (columns `gain_kappa*`).
- 50 km and 150 km circles were not run. N21s covers only 44 months. Truth S has 37 months (27 from March 2023), so its intervals are wide.
- The scale factors (1.0245, 1.0503) were fitted on 2018 to 2026 data that include the test months, so the C and C2 series are not fitted out of sample; their effect on class agreement was not isolated.

## 6. Files

All in the round's working folder. Run in this order with `python -I`, each from a clean start; `h03_build.py` about 1 minute, `h03_run.py` about 20 seconds.

- `scripts/h03_build.py`: builds monthly M, S, C, C2, N20s, N21s for the box and 100 km circles; prints checks 1 and 2; writes the next three files.
- `out/h03_monthly.npz`: monthly arrays (units x months) and satellite-days.
- `out/h03_context_months_box.csv`: the 58 test months, box values and satellite-days.
- `out/h03_ratio_C2_C_by_year.csv`: C2 / C and N20s, N21s over C, by year and window.
- `scripts/h03_run.py`: check 3 and the full scoring (202 splits, bootstrap 2,000 draws); writes the next four tables.
- `out/h03_check3.csv`: protocol B reproduction (R5, whole box).
- `out/h03_scores.csv`: every design (group, scheme, truth, season, sample, source, baseline): agreement, within one, kappa, not classifiable, pct difference, highest on record, with intervals and split SD.
- `out/h03_gains.csv`: U1 minus SV for every source with intervals, split SD and the share of splits with positive gain.
- `out/h03_true_class_shares.csv`: true-class shares by group, scheme and season.
- `scripts/h03_tables.py`: formats the compact tables; writes `out/h03_report_tables.md`.
- `scripts/h03-review.py`, `scripts/h03-review2.py` (reviewer): independent rebuild and rescoring; tables `out/h03-review_*.csv` (scores, gains with per-split percentiles, class shares, context, C2/C by year, check 3, realconfig summary, and `h03-review_compare.csv`, the cell-by-cell comparison with `h03_scores.csv`).

## 7. Review

**Re-run.** `h03_build.py`, `h03_run.py` and `h03_tables.py` were re-run from the existing inputs. All eight output files (`h03_monthly.npz`, `h03_context_months_box.csv`, `h03_ratio_C2_C_by_year.csv`, `h03_check3.csv`, `h03_scores.csv`, `h03_gains.csv`, `h03_true_class_shares.csv`, `h03_report_tables.md`) came out byte-identical to the analyst's. Every number in sections 1 to 3 was checked against those tables.

**Independent recomputation** (`h03-review.py`, written without the analyst's code or `f03_common.py`): daily counts from `hotspots_v2.parquet` (`use == True`, keyed by `local_date`; 100 km circles from `circles.csv` with the parquet's own x/y projection), availability from `avail_cat_plus_partial` with the NOAA-20 2018-04-01 to 2018-06-04 exception, C and C2 as daily means of scaled available satellites, its own R5/R3/P5/P3 classifier, the 202 splits, its own year-block bootstrap (2,000 draws, different seed). Results:
- Spec checks: 116 months, M 48,233, S 198,916, 0.2425; C for the six f03 months identical to the analyst's (629.5, 2,266.5, 4,751.1, 7,101.7, 690.0, 29,589.9; all within 0.05% of f03); protocol B U1 84.4% / 79.7%, SV 66.1% / 64.5%.
- C2/C by year and window, the five outlying months and the 29 months with C of at least 100: identical.
- True-class shares (box and circles): identical.
- All 1,440 score rows (agreement, within one, kappa, not classifiable, pct difference, highest on record): largest difference 0.04 points in agreement and 0.0006 in kappa, only in a few circle cells where a value sits exactly on a class edge (floating-point tolerance). Gains and split SDs: within 0.04 points. Bootstrap interval ends differ by up to about 4 to 6 points in a few small-sample cells (S truth, different seed and Monte Carlo noise); headline intervals agree within 0.5 points.

**Specific checks, all passed:** the MODIS factor is fitted only on each split's VIIRS-era stable years, never on test months; no test month's year is in any baseline (baselines 2012-2021, tests 2022-2026); months keyed by local date; static-site and non-vegetation rows excluded through `use`; correct availability column and the NOAA-20 spring 2018 exception (not material for 2022 onward); truth and designs use the same masking (C and C2 from the same flag, the baseline S raw in every design); rank class and the 20% tie rule match the spec (independent implementation agrees); intervals resample whole years.

**Corrections made in this report (before → after):**
1. Section 4: "the P5 gain is larger by +2 to +6 points in the box" → larger by +2.0, +4.7 and +7.2 in Apr-Oct, May-Sep and Jun-Sep but smaller (-2.6) over all months.
2. Section 4: "SV is lower (59 to 63%) than for R5 (about 66 to 73%)" → 59 to 62% against 62 to 73%.
3. Section 1: "interval ... is wide (6 to 30 points across cells)" → 4 to 30 points wide in the box, 4 to 10 in circles.
4. Section 1: "The gain is positive in every ... cell" → qualified as the split-averaged gain; 0 to 7% of individual splits have a negative gain for C2 in the box, and the per-split 5th percentile is -5 to +7 points.
5. Section 3.3: P5 and P3 circle month counts 28/20/16/44 → 27.7/19.7/15.7/43.7 (uncertain truth months dropped).
6. Added: the per-split percentile spread and the point that the year-block interval does not include it (section 4); the short-benchmark caveat (SV has five years, the real VIIRS-only alternative in 2026 would have 14) (section 5); that the S-truth sample excludes most of the largest fire months (3.6); S as a current-month source, which the task listed but the report did not show (3.6); and the per-month context values for the 35 Apr-Oct months, which the task asked to be reported (3.7).

No headline number changed. The analyst's statement (in the returned summary) that the gain interval excludes zero in all but one of the 320 truth-C cells is confirmed with the reviewer's own draws: the exception is circles, R3, May-Sep, with S as the current-month source (gain +4.9, lower end -0.01).

**Could not confirm / not done:** 50 km and 150 km circles were not run by either. The effect of fitting the scale factors 1.0245 and 1.0503 on data that include the test months was not isolated. Whether a four-block bootstrap has anything like 95% coverage cannot be checked with these data; the intervals should be read as indicative.
