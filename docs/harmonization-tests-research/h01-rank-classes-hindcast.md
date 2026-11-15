# h01: Rank classes in the hindcast (current month = Suomi NPP, series S)

> Working file from the fourth follow-up (14 November 2026). The series, class schemes (`R5`, `P5`) and designs (`U1`, `SV`) are defined in [h00-definitions.md](h00-definitions.md), which is what "the spec" means below. The scripts and tables named here are kept outside version control with the cached data.

## 1. Summary

- Under rank classes the converted-MODIS baseline (U1) still beats the short VIIRS-only baseline (SV) in Protocol B (k = 5, 202 splits), and by more than under ratio classes. Whole box, fire season (Apr-Oct): P5 U1 86.2% against SV 60.3%, gain +25.9 points (95% year-block interval 18.8 to 33.8); R5 U1 84.4% against SV 66.1%, gain +18.2 (13.8 to 22.7). All months: P5 +18.9 (12.6 to 24.6), R5 +15.2 (10.5 to 19.6).
- Part of the larger P5 gain is probably structural, not a better method: with 4 VIIRS-only baseline years, SV ranks a month among 4 values (pct in steps of 0.25), so a one-place shift moves it a whole class. In the box no month is "uncertain" for any design, so ties play no part in the box numbers; in the circles they do (SV uncertain in 10.8% of 100 km fire-season rows), and on rows both designs can class the 100 km P5 gain is +15.4 rather than +17.0. The gain is not comparable across schemes (spec section 4); kappa gain is similar in direction (U1 0.83 vs SV 0.50 under P5; 0.79 vs 0.55 under R5).
- Gain by baseline length does not shrink cleanly. Box fire season, P5: +10.9 (k=1, 8 VIIRS-only years), +15.8, +23.0, +28.7, +24.9 (k=5, 4 years). R5: +12.7, +9.0, +14.1, +13.6, +17.1. Even with 8 VIIRS-only years the gain is positive, but at k = 1 U1 and SV differ by one year only, so this cannot be extrapolated to the real 14-year baseline.
- Level error in the converted years: at x1.6 U1 fire-season agreement falls 13.2 points under R5 and 11.3 under P5 (box); at x1.27, 5.2 vs 7.2; at x1.15, 1.4 vs 4.8. Circles at 100 km: the two schemes fall by about the same amount (-8.2 vs -8.3 at x1.6). Neither scheme is clearly less sensitive: the paired year-block interval of the difference (P5 change minus R5 change) includes zero at every multiplier, in the box and at 100 km. A x0.8 error costs almost nothing in the fire season (but about 5 to 6 points over all months in the box).
- Protocol A (single converted month, box fire season): converted and actual S get the same class in 69.1% (R5) and 76.5% (P5) of 68 months; median absolute percentage error 33%. Check 3 reproduced (U1 84.4% fire season, 79.7% all months under R5; SV 66.1%, 64.5%).

## 2. Method

Data: `hotspots_v2.parquet`, `use == True`, standard stream (SP), local months, stable period 2012-02 to 2021-12 without 2016-02, 2020-08, 2020-09 (116 months). `M` = Terra+Aqua, `S` = Suomi NPP. Units: whole box and the circles in `circles.csv` at 100, 50, 150 km (31 each; same projection as round 3 a02). Conversion factor f = ratio of sums M/S over the VIIRS-era years of each split, always fitted on the whole box, applied to circle M values. 2026-11 not used. The combined series C is not used (this topic keeps S as the current month).

Classes (spec section 4): R5 (ratio to baseline median; bands 0.5, 0.8, 1.25, 2; not classifiable when baseline median < 1), R3 (collapse of R5: <0.5, 0.5-2, >2). P5: pct = (below + 0.5 equal) / n over the baseline, class = min(floor(5 pct), 4), uncertain when >= 20% of baseline values equal v. P3: pct < 1/3, 1/3 to 2/3, > 2/3 (uncertain as P5). The month's own year is always left out; n counts valid years (outage months drop out).

Protocol B: split assigns k of the ten years to a pretend MODIS era. Truth = class of S in each VIIRS-era month against S from all other years (n = 9 values). U1 = baseline of converted MODIS-era values (M/f) plus S of other VIIRS-era years (n = 9). SV = S of the other VIIRS-era years only (n = 9 - k). Standard splits: two chronological plus 200 from `default_rng(1)`, drawn as in round 3 a01.

Scoring. Scored set = months where the truth is classified (R: baseline median >= 1; P: not uncertain). If the design cannot classify such a month it counts as a miss for exact and within-one agreement and is left out of kappa. Both shares are reported: "scored n" is truth-classified over all rows; "unclass %" is the share of ALL rows where the design is unclassifiable. Within-one counts a design only when it is classified. Kappa is pooled over the scored, design-classified rows. MAD pct = mean |pct(design) - pct(truth)| over all rows; highest-on-record agreement = share of rows where design and truth agree on whether S exceeds every baseline value. These two use pct and highest, which do not depend on scheme, so they repeat across R and P lines.

Intervals: year-block bootstrap (2000 draws, 1000 for k and robustness tables) resampling the 10 evaluation years, with pooled agreement computed from per-year counts pooled over splits (and over circles). "sd splits" is the standard deviation, over splits, of the per-split gain (pooled over circles). For circles, rows pool 31 circles and many splits, so the effective sample is closer to 10 years than to the row count; use the intervals, not the denominators.

Item 2: all C(10,k) splits for k = 1..5 (10, 45, 120, 210, 252). Item 3: k = 5 standard splits with the converted values multiplied by 0.8, 1.15, 1.27, 1.6 (SV and truth are unaffected). Item 4: Protocol A leave-one-year-out, f from the other nine years; the converted value M/f and the actual S are both classed against S from the nine other years; scored set = truth-classified months; MdAPE over months with S > 0.

## 3. Results

Full tables (every subset, scheme and unit): `out/h01_tables.md` (generated by `h01_tables.py`). Below, the box in full for the four schemes and the key rows for circles.

### 3.1 Protocol B, whole box, k = 5, 202 splits (all rows scored: 0% unclassifiable for every design and scheme)

Exact agreement %, [95% year-block interval]. Gain = U1 minus SV in points. Rows per subset: fire season 6,862, May-Sep 4,842, Jun-Sep 3,832, Nov-Mar 4,844, all 11,706.

| subset | scheme | U1 exact | SV exact | U1 within1 | SV within1 | U1 kappa | SV kappa | gain [95%] | sd splits |
|---|---|---|---|---|---|---|---|---|---|
| Fire season | R5 | 84.4 [80.7,88.6] | 66.1 [59.1,73.0] | 98.1 | 90.4 | 0.79 | 0.55 | 18.2 [13.8,22.7] | 10.5 |
| Fire season | R3 | 92.5 [88.5,96.1] | 77.7 [72.2,82.7] | 100.0 | 96.6 | 0.89 | 0.66 | 14.8 [9.9,20.5] | 10.4 |
| Fire season | P5 | 86.2 [81.2,91.0] | 60.3 [54.5,66.8] | 99.8 | 96.6 | 0.83 | 0.50 | 25.9 [18.8,33.8] | 11.7 |
| Fire season | P3 | 87.8 [80.0,93.3] | 73.3 [66.4,81.5] | 100.0 | 100.0 | 0.82 | 0.60 | 14.5 [4.2,24.2] | 9.8 |
| May-Sep | R5 | 84.2 [79.3,89.5] | 69.3 [61.5,77.9] | 97.3 | 87.6 | 0.77 | 0.56 | 15.0 [9.8,19.9] | 13.7 |
| May-Sep | P5 | 89.6 [85.3,93.9] | 60.3 [53.2,68.4] | 100.0 | 95.9 | 0.87 | 0.50 | 29.3 [22.8,37.1] | 13.3 |
| May-Sep | R3 / P3 | 92.0 / 90.5 | 77.0 / 73.3 | 100 / 100 | 95.2 / 100 | 0.88 / 0.86 | 0.65 / 0.60 | 15.1 [9.0,21.2] / 17.2 [9.1,24.2] | 13.6 / 10.8 |
| Jun-Sep | R5 | 88.7 [83.4,94.4] | 72.3 [63.9,81.5] | 96.6 | 86.0 | 0.82 | 0.57 | 16.5 [10.6,23.1] | 14.7 |
| Jun-Sep | P5 | 90.7 [83.8,97.1] | 60.3 [51.8,69.6] | 100.0 | 95.5 | 0.88 | 0.50 | 30.3 [21.9,38.9] | 15.4 |
| Jun-Sep | R3 / P3 | 94.3 / 92.1 | 77.2 / 73.6 | 100 / 100 | 94.2 / 100 | 0.91 / 0.88 | 0.64 / 0.61 | 17.1 [10.5,24.6] / 18.5 [8.9,27.1] | 15.4 / 12.7 |
| Nov-Mar | R5 | 73.1 [62.0,84.0] | 62.2 [56.7,68.3] | 95.5 | 95.3 | 0.66 | 0.53 | 10.9 [2.1,19.7] | 14.0 |
| Nov-Mar | P5 | 70.6 [62.5,80.1] | 61.7 [53.9,71.9] | 97.5 | 96.9 | 0.63 | 0.52 | 9.0 [1.1,17.4] | 16.3 |
| Nov-Mar | R3 / P3 | 84.1 / 81.3 | 79.1 / 73.9 | 100 / 100 | 100 / 100 | 0.72 / 0.72 | 0.64 / 0.61 | 5.0 [-3.5,12.9] / 7.4 [-2.0,17.4] | 9.3 / 10.1 |
| All | R5 | 79.7 [74.8,84.2] | 64.5 [61.0,68.4] | 97.0 | 92.4 | 0.74 | 0.55 | 15.2 [10.5,19.6] | 7.7 |
| All | R3 | 89.0 [83.9,93.7] | 78.3 [74.6,81.7] | 100.0 | 98.0 | 0.83 | 0.66 | 10.7 [5.8,16.4] | 6.5 |
| All | P5 | 79.8 [75.8,85.0] | 60.9 [56.5,65.6] | 98.8 | 96.7 | 0.75 | 0.51 | 18.9 [12.6,24.6] | 9.4 |
| All | P3 | 85.1 [79.1,89.9] | 73.5 [67.2,80.0] | 100.0 | 100.0 | 0.77 | 0.61 | 11.6 [2.6,20.1] | 7.8 |

Share of months in each true class (%, fire season / all):
R5 classes 0-4: 31/16/6/16/31 and 28/17/10/19/26. R3: 31/38/31 and 28/47/26. P5: 21/21/18/20/20 and 21/21/17/21/21 (near 20% each by construction). P3: 31/38/31 and 31/38/31. (Other subsets in `out/h01_tables.md`.)

Rank-only measures (box, U1 against SV): mean absolute pct difference from the truth 0.041 vs 0.116 (fire season), 0.057 vs 0.115 (all); Nov-Mar 0.080 vs 0.113. Agreement on "highest on record": U1 98.0% vs SV 89.4% (fire season), 96.8% vs 89.6% (all); Jun-Sep 100% vs 89.4%. The share of fire-season months that are truly highest on record is in `h01_B_summary.csv` (`truth_highest_share`).

### 3.2 Circles (31 per radius, rows pooled), fire season and all months, k = 5, 202 splits

Exact agreement %, gain in points [95% year-block interval]. "Unclass U1/SV" = share of all rows the design cannot classify (R5 baseline median < 1; P5 20% ties). "Scored" = truth-classified rows / all rows.

| radius | subset | scheme | scored | U1 | SV | gain [95%] | kappa U1 / SV | unclass U1 / SV % |
|---|---|---|---|---|---|---|---|---|
| 100 km | Fire season | R5 | 212,722/212,722 | 77.4 | 66.7 | 10.6 [8.3,13.1] | 0.70 / 0.57 | 0.1 / 1.7 |
| 100 km | Fire season | P5 | 201,513/212,722 | 73.9 | 56.8 | 17.0 [13.1,20.9] | 0.69 / 0.51 | 4.6 / 10.8 |
| 100 km | Jun-Sep | R5 | 118,792/118,792 | 82.0 | 70.8 | 11.2 [6.8,15.5] | 0.73 / 0.58 | 0.1 / 3.0 |
| 100 km | Jun-Sep | P5 | 110,944/118,792 | 77.5 | 56.5 | 20.9 [15.6,25.9] | 0.75 / 0.50 | 7.5 / 11.3 |
| 100 km | Nov-Mar | R5 | 150,164/150,164 | 68.6 | 63.4 | 5.2 [0.3,10.1] | 0.61 / 0.53 | 1.9 / 0.0 |
| 100 km | Nov-Mar | P5 | 149,570/150,164 | 66.4 | 58.9 | 7.6 [0.5,14.6] | 0.58 / 0.51 | 0.3 / 4.1 |
| 100 km | All | R5 | 362,886/362,886 | 73.7 | 65.4 | 8.4 [5.1,11.5] | 0.66 / 0.55 | 0.8 / 1.0 |
| 100 km | All | P5 | 351,083/362,886 | 70.7 | 57.7 | 13.0 [7.8,18.1] | 0.64 / 0.51 | 2.8 / 8.0 |
| 50 km | Fire season | R5 | 141,655/212,722 | 64.9 | 62.3 | 2.6 [0.6,4.3] | 0.75 / 0.59 | 44.7 / 34.1 |
| 50 km | Fire season | P5 | 125,749/212,722 | 73.7 | 58.2 | 15.5 [12.6,18.6] | 0.70 / 0.52 | 37.4 / 42.0 |
| 50 km | All | R5 | 269,027/362,886 | 60.1 | 62.8 | -2.7 [-3.7,-1.5] | 0.72 / 0.58 | 42.0 / 27.0 |
| 50 km | All | P5 | 241,099/362,886 | 69.5 | 57.4 | 12.2 [9.0,15.5] | 0.65 / 0.52 | 31.7 / 36.0 |
| 150 km | Fire season | R5 | 212,722/212,722 | 87.3 | 67.3 | 20.0 [14.9,24.5] | 0.83 / 0.57 | 0.0 / 0.0 |
| 150 km | Fire season | P5 | 210,604/212,722 | 80.2 | 59.0 | 21.2 [14.3,27.5] | 0.75 / 0.51 | 0.2 / 3.4 |
| 150 km | All | R5 | 362,886/362,886 | 78.6 | 65.2 | 13.4 [9.5,17.0] | 0.72 / 0.55 | 0.0 / 0.0 |
| 150 km | All | P5 | 360,768/362,886 | 76.3 | 59.4 | 16.9 [9.2,23.9] | 0.70 / 0.51 | 0.1 / 2.6 |

R3, P3, within-one, May-Sep, MAD pct and highest-on-record for every radius are in `out/h01_tables.md`. Per-circle gains, fire season (`h01_B_percircle_circ*.csv`): at 100 km the U1 minus SV gain is positive in all 31 circles under both schemes (R5 mean 10.6, range 5.1 to 18.2; P5 mean 17.0, range 10.3 to 24.7); at 150 km also all 31 (R5 20.0, P5 21.2); at 50 km P5 is positive in all 31 (mean 15.3, range 1.8 to 23.1) while R5 is positive in 18 of 31 (mean 1.9, range -10.9 to 20.8). At 50 km the R5 numbers are dominated by unclassifiable months (baseline median < 1 in 34% to 45% of rows); the 50 km "agreement" counts those as misses for the design and drops months the truth cannot class, so the R5 and P5 rows are on different months and the R5 gain of +2.6 is not a clean comparison. Restricted to rows where the truth, U1 and SV can all class the month (review check, `out/h01-review_extra.csv`), the 50 km gain is R5 +10.8 [8.9,12.9] and P5 +15.7 [13.0,18.9] in the fire season (49% and 53% of rows), and R5 +10.0, P5 +13.0 over all months; the negative all-months R5 gain above comes entirely from U1 being unclassifiable more often than SV (42.0% against 27.0% of rows: converted MODIS months are often 0 at 50 km, pulling the 9-value median below 1). At 100 km the same restriction gives R5 +9.8 [7.2,12.6] and P5 +15.4 [11.6,19.5] (fire season; 98% and 87% of rows).

### 3.3 Baseline length: all splits, k = 1..5 (box; gain in points [95% interval], exact %)

| k | splits | SV baseline years | R5 fire U1 / SV / gain | P5 fire U1 / SV / gain | R5 all U1 / SV / gain | P5 all U1 / SV / gain |
|---|---|---|---|---|---|---|
| 1 | 10 | 8 | 94.9 / 82.2 / 12.7 [8.1,18.4] | 96.6 / 85.6 / 10.9 [5.6,15.7] | 94.3 / 78.9 / 15.3 [12.8,17.9] | 95.3 / 85.4 / 9.9 [6.7,13.6] |
| 2 | 45 | 7 | 91.2 / 82.2 / 9.0 [6.2,12.2] | 93.5 / 77.7 / 15.8 [7.3,23.5] | 89.8 / 80.3 / 9.5 [7.2,11.4] | 90.9 / 77.6 / 13.4 [7.9,18.5] |
| 3 | 120 | 6 | 88.5 / 74.4 / 14.1 [10.3,18.6] | 90.8 / 67.8 / 23.0 [12.0,32.3] | 86.1 / 71.5 / 14.6 [11.9,17.3] | 86.9 / 67.7 / 19.2 [11.1,26.0] |
| 4 | 210 | 5 | 86.3 / 72.6 / 13.6 [10.1,17.2] | 88.3 / 59.6 / 28.7 [21.1,35.5] | 82.8 / 70.9 / 11.9 [8.4,15.1] | 83.1 / 59.7 / 23.4 [17.2,29.5] |
| 5 | 252 | 4 | 84.4 / 67.3 / 17.1 [13.3,21.4] | 86.0 / 61.1 / 24.9 [18.2,32.2] | 79.7 / 65.0 / 14.7 [10.0,18.9] | 79.6 / 61.1 / 18.5 [12.4,23.9] |

Circles at 100 km (gain, fire season): R5 10.4, 5.5, 9.2, 6.8, 10.4 and P5 9.0, 11.2, 15.9, 22.7, 16.8 for k = 1..5 (full table in `out/h01_tables.md`; "sd splits" about 4 to 11 points for k > 1). Jun-Sep rows are in `h01_k_summary.csv`. Splits are not independent (the same ten years; k=1 has only 10 splits), so treat the k=1 and k=2 intervals as optimistic.

What this does and does not say. (a) The gain does not fall in a straight line as the VIIRS-only baseline gets longer. Under R5 it fluctuates (9 to 17 points, 5.5 to 10.4 at 100 km) with a slight upward drift towards k = 5; under P5 it is larger at k = 3-5 than at k = 1-2, and drops from k = 4 to k = 5. (b) The P5 pattern is mostly produced by the rank grid: a baseline of n values only gives pct in steps of 1/n, and the class boundaries at 0.2, 0.4... fall differently for n = 4, 5, 6, 7, 8 (for n = 5 the two top ranks share the top class), so SV agreement with the 9-value truth is not monotone in n (box fire season P5: 85.6, 77.7, 67.8, 59.6, 61.1). The k = 4 vs k = 5 reversal is most likely this rather than a real effect of length (not tested directly). (c) At k = 1 SV and truth share 8 of 9 baseline values and U1 differs from the truth only by one converted year; U1 is near perfect (95 to 97%) while SV is at 82 to 86%, so dropping a single year from a 9-year baseline changes the class of 13 to 18% of fire-season months. (d) The real VIIRS-only baseline is 14 years, which is outside the range tested (at most 8); the converted-MODIS gain at 14 VIIRS years cannot be read from this table, and a trend line through k = 1..5 would extrapolate noise. What can be said: over the range 4 to 8 years, with the other years supplied by MODIS conversion, the converted baseline reproduces the 9-year truth better than the VIIRS-only years, under both schemes, with 95% intervals above zero at every k. What cannot be said: that the advantage persists, or vanishes, at 14 years; and that these 10 test years (2012-2021, with the large 2017, 2018 seasons) represent the rest.

### 3.4 Wrong level in the converted era: U1 exact %, change in points against x1.0 (k = 5, 202 splits)

Box (change vs 1.0; SV does not use converted values: fire season R5 66.1, P5 60.3, all R5 64.5, P5 60.9):

| subset | scheme | x0.8 | x1.0 | x1.15 | x1.27 | x1.6 |
|---|---|---|---|---|---|---|
| Fire season | R5 | 84.2 (-0.1) | 84.4 | 83.0 (-1.4) | 79.2 (-5.2) | 71.1 (-13.2) |
| Fire season | P5 | 84.5 (-1.8) | 86.2 | 81.5 (-4.8) | 79.1 (-7.2) | 74.9 (-11.3) |
| Fire season | R3 | 93.1 (+0.6) | 92.5 | 90.8 (-1.7) | 88.9 (-3.6) | 84.2 (-8.3) |
| Fire season | P3 | 89.4 (+1.6) | 87.8 | 88.1 (+0.3) | 85.8 (-2.0) | 82.6 (-5.2) |
| Jun-Sep | R5 | 89.8 (+1.0) | 88.7 | 88.5 (-0.2) | 86.3 (-2.5) | 82.0 (-6.7) |
| Jun-Sep | P5 | 93.7 (+3.1) | 90.7 | 86.4 (-4.2) | 83.6 (-7.0) | 81.9 (-8.8) |
| All | R5 | 74.8 (-4.9) | 79.7 | 79.0 (-0.7) | 76.4 (-3.3) | 70.9 (-8.8) |
| All | P5 | 73.8 (-6.0) | 79.8 | 78.3 (-1.5) | 77.3 (-2.5) | 74.0 (-5.8) |

100 km circles, fire season: R5 78.4 (+1.0), 77.4, 75.3 (-2.0), 73.6 (-3.7), 69.2 (-8.2); P5 75.0 (+1.1), 73.9, 72.0 (-1.9), 70.6 (-3.3), 65.6 (-8.3). Circles, all months: R5 -1.8, -0.7, -1.6, -4.5; P5 -1.3, -0.9, -1.8, -5.2 for x0.8, 1.15, 1.27, 1.6. Intervals for each cell are in `h01_robust_summary.csv`; at the box the 95% intervals of neighbouring multipliers overlap widely (e.g. R5 fire season x1.0 [81.0,88.6] against x1.27 [73.0,86.1]), because all multipliers use the same ten years and the changes are paired, so the point changes are better evidence than the overlap suggests. Paired year-block intervals of the change (review, `out/h01-review_robust.csv`), box fire season: R5 x0.8 -0.1 [-3.9,3.4], x1.15 -1.4 [-4.1,1.1], x1.27 -5.2 [-9.0,-1.1], x1.6 -13.2 [-18.0,-8.2]; P5 -1.8 [-6.2,2.2], -4.8 [-8.5,-0.9], -7.2 [-11.3,-2.3], -11.3 [-15.2,-5.9]. The paired scheme contrast, P5 change minus R5 change (`out/h01-review_extra.csv`), box fire season: -1.6 [-8.4,5.0], -3.3 [-7.4,1.1], -2.0 [-7.2,3.4], +2.0 [-3.9,8.2]; at 100 km every contrast is within ±1 point except Jun-Sep x1.6 (-2.6 [-5.9,0.3]). No interval excludes zero.

Under a too-high conversion U1 still beats SV at every level tested: at x1.6, box fire season R5 71.1 vs SV 66.1, P5 74.9 vs SV 60.3.

### 3.5 Protocol A: converted month against actual S (leave one year out)

Share of held-out months in which the converted value and the actual S get the same class [95% year-block interval]; scored = truth-classified months; MdAPE over months with S > 0 (n in brackets).

| unit | subset | scored | R5 same class | P5 same class | R3 | P3 | MdAPE |
|---|---|---|---|---|---|---|---|
| box | Fire season | 68 | 69.1 [61.4,77.4] | 76.5 [68.2,84.3] | 79.4 | 73.5 | 33% (67) |
| box | Jun-Sep | 38 | 81.6 [71.1,91.7] | 81.6 [69.4,92.1] | 84.2 | 78.9 | 31% (37) |
| box | All | 116 | 63.8 [58.1,69.6] | 69.0 [61.2,77.1] | 75.9 | 72.4 | 32% (115) |
| 100 km | Fire season | 2,108 (P5 1,998) | 62.8 [57.8,67.6] | 63.3 [55.7,71.1] | 72.4 | 72.6 | 52% (1,944) |
| 100 km | Jun-Sep | 1,178 (P5 1,101) | 75.8 [67.3,84.4] | 69.5 [57.9,80.6] | 79.7 | 76.6 | 69% (1,033) |
| 100 km | All | 3,596 (P5 3,480) | 61.3 [56.3,66.0] | 61.8 [55.6,68.2] | 70.4 | 71.1 | 48% (3,428) |
| 150 km | Fire season | 2,108 (P5 2,087) | 68.0 [61.7,74.8] | 69.9 [59.9,79.9] | 79.0 | 79.7 | 35% (2,077) |
| 50 km | Fire season | 1,404 (P5 1,248) | 63.0 [59.2,66.3] | 58.7 [51.9,65.0] | 68.9 | 66.0 | 92% (1,326) |

Rank-class agreement is higher than ratio-class agreement for the box (76.5 vs 69.1% in the fire season) but the intervals overlap; for circles it is about the same at 100 and 150 km (63.3 vs 62.8, 69.9 vs 68.0) and lower at 50 km (58.7 vs 63.0). The classes have different base rates, so these two columns are not a ranking of schemes. Within one class: R5 95.6%, P5 94.1% (box fire season); mean |pct difference| 0.089. The converted-value MdAPE is 33% in the box, higher in smaller circles, because small counts are noisy.

## 4. How strong

- Solid: the sign and rough size of the U1 gain in the box under every scheme in the fire season (intervals exclude 0 for every fire-season, May-Sep, Jun-Sep and all-months row); the check-3 reproduction; robustness to a x1.6 level error being worse than x1.15 or x0.8 under all four schemes.
- Moderate: the size of the P5 gain compared with the R5 gain. It is larger in the box, but SV under P5 is limited by having only 4 baseline values (a coarse rank grid and more tie-driven "uncertain" months, 10.8% of 100 km fire-season rows), so part of the P5 gain is a weak benchmark. Kappa gain: P5 +0.33 vs R5 +0.24 (box, fire season).
- Weak: the Nov-Mar results (box intervals reach near zero for R5 and P5; R3 and P3 intervals include zero), the k-dependence, the 50 km R5 comparison, and any statement about which scheme tolerates a level error better. The two schemes lose similar amounts (R5 -13.2, P5 -11.3 at x1.6 in the box; -8.2 vs -8.3 in circles); at x1.15 the box drop is larger for P5 (-4.8 vs -1.4) and at x0.8 P5 loses 1.8 where R5 loses 0.1, but the paired year-block interval of the scheme contrast includes zero at every multiplier (section 3.4).

## 5. Limits and surprises

- Only ten years, so every interval is built on ten year-blocks; the 2017, 2018 and 2021 seasons dominate the extremes. Circle rows share those years; the circles are not independent of each other or of the box.
- The truth itself is a 9-year baseline, not a 14 or 26-year one; the question answered is how well a mixed baseline reproduces a 9-year baseline.
- A surprise: the P5 benchmark SV is worse at k = 4 (5 baseline years) than at k = 5 (4), and the gain peaks at k = 4. It is a property of the 1/n rank grid with the 0.2-wide classes, not of data quality. A rank scheme with a fixed class count compared across baselines of different n is not like-for-like.
- A surprise: the R5 gain at 50 km nearly vanishes (and reverses for all months) because the baseline median falls under 1 in about 40% of cells, more often for U1 than for SV; on rows where every design can class the month it is about +10 points (section 3.2). P5 does not stay classifiable in more cells: its truth is uncertain (ties) in 41% of 50 km fire-season rows against 33% unclassifiable under R5; P5 leaves U1 unclassifiable less often (37% vs 45%) but SV more often (42% vs 34%).
- Treatment of unclassifiable months (miss for the design, dropped for the truth) was my choice; the spec does not fix it. In the box nothing is unclassifiable so the headline is unaffected.
- The conversion factor in each split is fitted on the VIIRS-era years of that split (the round 3 rule); in a real calendar f would come from all stable years. This choice barely matters: with f from all ten years, or from the split's VIIRS-era years minus the month's own year, U1 agreement moves by at most 0.5 points (box and 100 km, fire season and all months, R5 and P5; `out/h01-review_extra.csv`).
- Circle 25 km was not run. The combined VIIRS series and the Suomi-NPP-free configuration are not part of this topic.

## 6. Files (all in the round's working folder; run each with `python -I`, `h01_build.py` first)

Scripts (`scripts/`):
- `h01_build.py`: builds the monthly M and S cube for box and circles from the parquet; prints check 1 (116 months, M 48,233, S 198,916, 0.2425).
- `h01_lib.py`: shared functions (classes R5, R3, P5, P3, split lists, Protocol B row generator, scoring, bootstrap). Not run alone.
- `h01_B.py`: item 1 (and check 3 printout); box and circles at 100, 50, 150 km, 202 splits.
- `h01_k.py`: item 2 (k = 1..5, all splits; box and 100 km).
- `h01_robust.py`: item 3 (multipliers 0.8, 1.15, 1.27, 1.6 and 1.0; box and 100 km).
- `h01_A.py`: item 4 (Protocol A; box, 100, 50, 150 km).
- `h01_tables.py`: prints the markdown tables from the summary csv files, writes `out/h01_tables.md` when redirected.

Tables (`out/`):
- `h01_cube.npz`: monthly cube (M, S).
- `h01_B_summary.csv`: item 1, every unit, subset, scheme, design (U1, SV) with gain and intervals. `h01_B_percircle_circ100.csv`, `_circ50.csv`, `_circ150.csv`: per-circle fire-season agreement and gain.
- `h01_k_summary.csv`: item 2. `h01_robust_summary.csv`: item 3. `h01_A_summary.csv`: item 4.
- `h01_tables.md`: the printed tables used above, including all subsets and the circle k and robustness tables.

## 7. Review

**Re-run.** All seven analyst scripts (`h01_build`, `h01_B`, `h01_k`, `h01_robust`, `h01_A`, `h01_tables`) were re-run in order (about 40 s in all). Every `h01_*` csv is identical to the original to the last digit and `h01_tables.md` is byte-identical. Check 1 prints 116 months, M 48,233, S 198,916, 0.2425. Every number in sections 1 to 3 that I traced back to a table matches it.

**Independent recomputation** (`scripts/h01-review.py`, own code from the specs; tables `out/h01-review_*.csv`). Own monthly cube from the parquet (`use`, SP stream, `ym_local`, same three dropped months for both M and S), own rank classes in integer arithmetic (`pct = (2·below + equal)/(2n)`, class `floor(5·num/2n)` capped at 4, uncertain when `5·equal ≥ n`), own R5 by `nanmedian`, own splits, kappa and year-block bootstrap (different seeds). Results:
- Check 1: 116 / 48,233 / 198,916 / 0.2425, exact. Check 2 (not run by the analyst; combined series C with `avail_cat_plus_partial` and the NOAA-20 2018-04-01 to 06-04 exception): all six f03 values within 0.1%. Check 3: U1 84.4% fire season, 79.7% all months; SV 66.1%, 64.5%.
- Item 1: every point estimate (exact, within-one, kappa, gain, sd across splits, unclassifiable shares, scored n) for the box and the 50, 100, 150 km circles, all five subsets and four schemes, matches the analyst to 0.1 point; per-circle gains match (100 km: R5 mean 10.6, 31/31 positive; P5 17.0, 31/31; 50 km R5 18/31). Bootstrap intervals agree within about 0.5 point (seed differences), e.g. box fire season P5 gain [18.9, 33.7] against [18.8, 33.8].
- Items 2, 3 and 4: every point estimate in sections 3.3, 3.4 and 3.5 reproduced exactly (k sweep, multipliers, Protocol A same-class shares, MdAPE 33%, n = 68).

**Things specifically checked and found in order:** f is fitted on the split's VIIRS-era years, never on the converted (MODIS-era) years; including the evaluated year in the fit is the round 3 protocol and changes U1 by at most 0.5 point (section 5). The month's own year is always out of every baseline. Months keyed by `ym_local`. `use` removes the static site and non-vegetation rows. The availability flag is not needed for series S, and no Suomi NPP sensor-month in 2012-2021 is in `masked_sensor_months.csv`; the dropped months are masked identically in M and S, so truth, U1 and SV see the same months. The P5/P3 classes and the 20% tie rule follow the spec (my integer version gives identical classes). Intervals resample whole evaluation years, not months.

**Corrections made (before -> after):**
1. Summary: "ties at small counts make [SV] 'uncertain' more often" stated as a cause of the larger box P5 gain -> in the box no month is uncertain for any design, so ties play no part there; they matter only in circles. Wording; conclusion unchanged.
2. Section 3.2, 50 km: the R5 gains (+2.6 fire season, -2.7 all months) were left as "not clean" -> added the like-for-like gain on rows all designs can class: R5 +10.8 [8.9,12.9], P5 +15.7 [13.0,18.9] (fire season); the negative all-months R5 gain is produced entirely by U1 being unclassifiable more often (42% vs 27% of rows). Also added the 100 km like-for-like gains (R5 +9.8, P5 +15.4 against +10.6, +17.0). Changes the reading of the 50 km result.
3. Section 5: "P5 stays classifiable in more cells" -> false for the truth (41% uncertain under P5 against 33% unclassifiable under R5) and for SV (42% vs 34%); true only for U1 (37% vs 45%).
4. Section 3.3 (c): "both designs are close to perfect" at k = 1 -> U1 is 95-97%, SV 82-86%. (b): the k = 4/5 reversal "is this" -> "most likely this (not tested directly)".
5. Section 3.4 and 4: "not bootstrapped as paired differences" / "within the splits' sd" -> added paired year-block intervals of each change and of the P5-minus-R5 contrast; no contrast interval excludes zero, which supports (and now evidences) "neither scheme is clearly less sensitive". Added that x0.8 costs 4.9 (R5) and 6.0 (P5) points over all months in the box, with intervals excluding zero.
6. Section 3.5: Protocol A rank agreement "the same or lower for circles" -> about the same at 100 and 150 km (P5 slightly higher), lower at 50 km.

**Not confirmed / open.** The claim that the larger P5 gain is partly "structural" (4-value rank grid) is a plausible reading, not something I tested. The year-block bootstrap resamples only evaluation years; the baseline years inside each split are not resampled, so all intervals are somewhat narrow. 25 km circles were not run (not required).

Review files: `scripts/h01-review.py` (checks 1-3, items 1-4; `out/h01-review_checks.csv`, `_B.csv`, `_B_percircle.csv`, `_k.csv`, `_robust.csv`, `_A.csv`, log `_log.txt`), `scripts/h01-review_extra.py` (like-for-like gains, factor variants, paired scheme contrast; `out/h01-review_extra.csv`). Analyst originals kept in `out/h01-review_orig/`.
