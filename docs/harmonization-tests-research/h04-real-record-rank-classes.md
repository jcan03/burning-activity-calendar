# h04: The real record under rank classes

> Working file from the fourth follow-up (14 November 2026). The series, class schemes (`R5`, `P5`) and designs (`U1`, `SV`) are defined in [h00-definitions.md](h00-definitions.md), which is what "the spec" means below. The scripts and tables named here are kept outside version control with the cached data.

## 1. Summary

The real record has no known answer. This topic measures how much adding converted 2003–2011 MODIS years changes labels. It does not say which label is right. On the whole box, with the combined VIIRS series `C`, months of 2012–2025, a mixed 2003–2025 baseline gives a different five-class label from a VIIRS-only 2012–2025 baseline in **35 of 98 fire-season months under R5 (35.7%, 28–44)** and **29 of 98 under P5 (29.6%, 24–36)**. In both schemes the mixed baseline almost always gives the lower class (R5 31 lower and 4 higher; P5 24 lower and 5 higher). The 100 km circles give 37.0% (R5) and 34.2% (P5).

Changing the baseline length alone moves rank labels more than ratio labels: the permutation null is 24% for P5 and 21% for R5. The excess over that null is therefore smaller under P5. In the box it is +5 points (p = 0.19, not distinguishable from length alone), against +14 points under R5 (p = 0.024). In the circles it is +10 points under P5 (p = 0.025) and +16 under R5 (p = 0.001). The direction excess (mixed lower) remains under both schemes (p ≤ 0.07; the P5 box value is 0.065 to 0.074 depending on the permutation seed).

When the converted level is moved, P5 labels change slightly less than R5 labels in the fire season. Dividing by 1.6 changes 18 of 98 box labels under P5 and 23 under R5, and 14.0% against 16.1% of circle labels. The difference is within the bootstrap intervals in the box. Over all months the two schemes move by the same amount (41 against 40 of 167). The choice between `C` and f01's Suomi NPP stand-in changes about 5% of box labels and about 10% of circle labels on its own.

## 2. Method

- **Data.** `hotspots_v2.parquet`, `use == True`, all streams, months keyed by local date. The box is used, plus the 31 circles at 100 km and the 31 at 50 km, selected on planar `x_km`/`y_km` as in f01 and f03.
- **Checks reproduced** (`h04_checks.txt`, `h04_check3.csv`).
  - Check 1: 116 months, M = 48,233, S = 198,916, ratio 0.2425.
  - Check 2: `C` for the box is 629.5, 2,266.5, 4,751.1, 7,101.7, 690.0 and 29,589.9, all within 0.1%.
  - Check 3: Protocol B, 202 splits, R5. U1 agrees in 84.38% of fire-season months and 79.70% of all months. SV agrees in 66.1% and 64.5%.
  - f01 reproduction: with f01's stand-in series, box fire season 2012–2026, R5, the mixed and VIIRS-only labels differ in **41 of 105 months (38 lower, 3 higher)**, as in f01. On 2012–2025 the count is 38 of 98, and the permutation result is 38.8% against a null mean of 22.4% (95th percentile 33.7%, p = 0.012), as in the f01 review.
- **Series.**
  - Converted era: (Terra + Aqua) / f, with f = 0.24248 fitted on the 116 stable months. Each month is NaN if either satellite is masked (2003-12).
  - `C`: for each local day, the mean of the scaled counts of the VIIRS satellites flagged available (`avail_cat_plus_partial`, with NOAA-20 forced available from 2018-04-01 to 2018-06-04). Scale factors are 1, 1.0245 and 1.0503. A day with no satellite available counts 0. `C` runs from 2012-02 to 2026-10.
  - `V01`: f01's stand-in. It is Suomi NPP, with NOAA-20 × 1.011 used for Suomi NPP's masked months and for all of 2026.
- **Baselines.** Mixed: the same calendar month in 2003–2025, excluding the month's own year (2003–2011 converted, 2012–2025 VIIRS). VIIRS-only: 2012–2025, excluding the own year. A year with no value is dropped from the baseline.
- **Schemes.** As defined in SPEC §4.
  - P5: `pct = (below + 0.5 × equal)/n`, class `min(floor(5·pct), 4)`. A month is uncertain when 20% or more of the baseline values equal `v`.
  - P3: the same tie rule, with cuts at 1/3 and 2/3.
  - R5 and R3: a month is classifiable only when the baseline median is at least 1.
  - Label differences are counted over months classifiable under both baselines.
- **Intervals.** Year-block bootstrap over the evaluated years, 2,000 draws.
- **Item 2 (permutation test).** This is f01's test. A permutation draws 9 of the pooled years as "early". Each remaining "late" year is classed against all pooled years except itself (long baseline) and against the other late years (short baseline). Both the value and the baseline come from the same mixed array. The observed case uses 2003–2011 as the early years. Two pools were used: 2003–2025 (late years 2012–2025, the real comparison) and 2003–2021 (late years 2012–2021, as in f01 Part 3b). There were 5,000 permutations (seed 2026), with box and circles in the same draws. The p-value is the share of permutations at or above the observed value.
- **Item 3 (level).** The converted 2003–2011 values were divided by 1, 1.15, 1.27 and 1.6, and multiplied by 1.25 (shown as divisor 0.8). A paired year-block bootstrap gives the R5 − P5 difference in the share of labels that changed (`h04_item3_contrast.csv`).

## 3. Results (series `C`, months of 2012–2025, unless stated)

### 3.1 Item 1: labels that differ between the mixed and VIIRS-only baselines

| Unit | Window | months | R5 differ (lower/higher) | R3 differ | P5 differ (lower/higher) | P3 differ |
|---|---|---|---|---|---|---|
| Box | Apr–Oct | 98 | 35, 35.7% (28–44) (31/4) | 18.4% (13–24) | 29, 29.6% (24–36) (24/5) | 15.3% (8–22) |
| Box | May–Sep | 70 | 20, 28.6% (17–40) (16/4) | 14.3% | 16, 22.9% (16–30) (11/5) | 11.4% |
| Box | Jun–Sep | 56 | 12, 21.4% (11–32) (8/4) | 7.1% | 12, 21.4% (13–32) (7/5) | 7.1% |
| Box | Nov–Mar | 69 | 26, 37.7% (28–49) (14/12) | 14.5% | 17, 24.6% (16–34) (13/4) | 10.1% |
| Box | all | 167 | 61, 36.5% (31–42) (45/16) | 16.8% | 46, 27.5% (22–34) (37/9) | 13.2% |
| 100 km | Apr–Oct | 3,038 / 2,994 | 37.0% (31–42) (33.8% / 3.2%) | 21.2% | 34.2% (30–38) (29.6% / 4.6%) | 19.5% |
| 100 km | May–Sep | 2,170 / 2,126 | 28.0% (22–34) | 18.8% | 26.1% (21–30) | 15.3% |
| 100 km | Jun–Sep | 1,736 / 1,692 | 23.3% (17–30) | 16.2% | 23.1% (18–28) | 14.0% |
| 100 km | Nov–Mar | 2,139 | 30.9% (26–36) | 12.7% | 33.6% (28–39) | 17.3% |
| 100 km | all | 5,177 / 5,133 | 34.5% (30–39) (28.5% / 6.0%) | 17.7% | 33.9% (30–37) (27.4% / 6.6%) | 18.6% |

The 50 km circles are in `h04_item1_differ.csv`. Under R5 only 1,787 of 3,038 fire-season circle-months are classifiable under both baselines, and 24.3% of those differ. Under P5 the figure is 2,112 months, of which 34.9% differ.

The direction intervals in the box (Apr–Oct) put the share where the mixed baseline is lower at 31.6% (26–38) under R5 and 24.5% (18–31) under P5. The share where it is higher is 4% to 5% in both.

**By calendar month, box** (differ out of 14 years; January out of 13; mixed lower in brackets):

| | J | F | M | A | M | J | J | A | S | O | N | D |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R5 | 1 (1) | 2 (0) | 5 (5) | 6 (6) | 8 (8) | 6 (6) | 4 (0) | 0 | 2 (2) | 9 (9) | 8 (8) | 10 (0) |
| P5 | 0 | 1 (0) | 5 (5) | 8 (8) | 4 (4) | 5 (5) | 3 (0) | 2 (0) | 2 (2) | 5 (5) | 8 (8) | 3 (0) |

In the 100 km circles (434 circle-months per calendar month), the most-changed months are April (R5 249, P5 241), October (266, 229), November (230, 239) and March (152, 192). The least-changed are August (60, 50) and July (70, 106).

The pattern is the same as f01's. The changes fall in spring and autumn and nearly always go downward. July, August and December change in the other direction (the mixed baseline is higher). Under P5 the mixed-baseline class shares are close to uniform (box fire season 27/18/21/15/18%). Under R5, 36% of mixed-baseline labels are in the lowest class, against 27% with the VIIRS-only baseline (`h04_class_shares.csv`).

The P5 percentiles move less than the class counts suggest. The mean absolute difference in `pct` between the two baselines is 0.068 in the box and 0.077 in the circles (fire season). The two baselines agree on whether a month is the highest on record in 96.9% of box fire-season months. The mixed baseline gives the highest on record in 4 months, the VIIRS-only baseline in 7.

### 3.2 Item 2: the length-only null (5,000 permutations)

| Pool (late years) | Unit, window | Scheme | observed differ | null mean (95th) | p | observed mixed lower | null mean (95th) | p |
|---|---|---|---|---|---|---|---|---|
| 2003–2025 (2012–25) | Box, Apr–Oct (98) | R5 | 35.7% | 21.4% (32.7%) | 0.024 | 31.6% | 12.3% (26.5%) | 0.015 |
| | | P5 | 29.6% | 24.3% (33.7%) | 0.19 | 24.5% | 11.7% (25.5%) | 0.065 |
| | Box, all (167) | R5 | 36.5% | 22.6% (32.1%) | 0.008 | 26.9% | 11.4% | 0.014 |
| | | P5 | 27.5% | 24.3% (31.7%) | 0.22 | 22.2% | 11.9% | 0.052 |
| | 100 km, Apr–Oct | R5 | 37.0% | 21.1% (28.3%) | 0.001 | 33.8% | 11.4% | 0.002 |
| | | P5 | 34.2% | 24.2% (32.2%) | 0.025 | 29.6% | 11.8% | 0.014 |
| 2003–2021 (2012–21) | Box, Apr–Oct (70) | R5 | 38.6% | 24.3% (37.1%) | 0.049 | 38.6% | 13.7% | 0.013 |
| | | P5 | 38.6% | 29.7% (42.9%) | 0.14 | 34.3% | 15.3% | 0.052 |
| | 100 km, Apr–Oct | R5 | 38.8% | 24.2% (31.8%) | 0.001 | 37.0% | 12.7% | 0.001 |
| | | P5 | 40.5% | 29.9% (40.4%) | 0.048 | 37.5% | 14.4% | 0.013 |

Under the coarse schemes, on the 2003–2025 pool, box Apr–Oct: R3 differs in 18.4% against a null of 12.5% (p = 0.15), and P3 in 15.3% against 12.2% (p = 0.22). In the circles: R3 21.2% against 12.8% (p = 0.009), and P3 19.5% against 12.6% (p = 0.021).

The excess over the null, in points (box Apr–Oct and circles Apr–Oct), is +14 and +16 for R5 and +5 and +10 for P5. Part of the gap between the schemes is the length effect itself. A rank with 22 baseline values against one with 13 moves the class more often than a median does, so the P5 null sits about 3 points higher. The `V01` series gives the same picture (`h04_perm.csv`).

### 3.3 Item 3: sensitivity to the level of the converted years

Each cell gives the labels changed against the plain mixed baseline (all of them upward when dividing and downward when multiplying), followed by the labels that differ from VIIRS-only.

| Converted values | Box Apr–Oct R5 (n = 98) | Box Apr–Oct P5 (98) | Box all R5 (167) | Box all P5 (167) | 100 km Apr–Oct R5 (3,038) | 100 km Apr–Oct P5 (3,006) |
|---|---|---|---|---|---|---|
| ÷ 1 | 0, 35 | 0, 29 | 0, 61 | 0, 46 | 0, 37.0% | 0, 34.2% |
| ÷ 1.15 | 6, 32 | 5, 24 | 7, 59 | 12, 38 | 4.2%, 35.5% | 3.9%, 31.9% |
| ÷ 1.27 | 13, 26 | 8, 25 | 23, 50 | 22, 40 | 8.0%, 33.5% | 7.6%, 30.0% |
| ÷ 1.6 | 23, 18 | 18, 21 | 40, 39 | 41, 35 | 16.1%, 29.8% | 14.0%, 26.9% |
| × 1.25 | 10, 42 | 11, 35 | 23, 63 | 22, 59 | 4.9%, 38.1% | 5.4%, 36.8% |

**Which scheme moves less.** In the fire season, P5 labels move slightly less than R5 labels when the converted level moves downward. At ÷ 1.6 the difference is 5 of 98 box labels (23.5% against 18.4%; paired difference +5.1 points, 95% interval −4 to +14) and 2.1 points in the circles (16.1% against 14.0%, −0.8 to +5.0). Neither difference is outside its interval.

Across all months the schemes are equal in the box (÷ 1.6: 40 against 41). In the circles the gap is small but consistent: R5 changes 20.5% and P5 18.2% (+2.3 points, 0.6 to 4.0). For an upward move (× 1.25) P5 moves as much as R5 or slightly more. The coarse schemes do not differ (R3 against P3, within ±1 point in the circles).

So rank classes are not materially less sensitive to the converted level. Where there is a difference, it is about one label in five fewer at the largest shift. A ÷ 1.6 shift takes R5 to 18 of 98 box labels different from VIIRS-only. Under P5 the count stops at about 21 of 98, because the length-only floor is higher.

### 3.4 Item 4: January–October 2026 (box; value `C`; classes 1–5, or 1–3 for R3/P3)

| Month | C | R5 mixed / VIIRS-only | P5 mixed / VIIRS-only | P5 pct mixed / VIIRS-only | R3 | P3 |
|---|---|---|---|---|---|---|
| Jan | 163 | 5 / 5 | 5 / 5 | 0.86 / 0.92 | 3 / 3 | 3 / 3 |
| Feb | 50 | 3 / 3 | 3 / 3 | 0.48 / 0.43 | 2 / 2 | 2 / 2 |
| Mar | 31 | 1 / 1 | 1 / 1 | 0.00 / 0.00 | 1 / 1 | 1 / 1 |
| Apr | 77 | 3 / **4** | 3 / **4** | 0.52 / 0.64 | 2 / 2 | 2 / 2 |
| May | 17 | 1 / **3** | 2 / 2 | 0.26 / 0.36 | 1 / **2** | 1 / **2** |
| Jun | 115 | 5 / 5 | 5 / **4** | 0.83 / 0.79 | 3 / 3 | 3 / 3 |
| Jul | 18,365 | 5 / 5 | 5 / 5 | 0.96 / 0.93 | 3 / 3 | 3 / 3 |
| Aug | 29,590 | 5 / 5 | 5 / 5 | 0.96 / 0.93 | 3 / 3 | 3 / 3 |
| Sep | 243 | 3 / 3 | 3 / 3 | 0.52 / 0.57 | 2 / 2 | 2 / 2 |
| Oct | 757 | 1 / **2** | 2 / 2 | 0.26 / 0.29 | 1 / **2** | 1 / 1 |

In the box, 3 of 10 labels differ under R5, 2 of 10 under P5, 2 under R3 and 1 under P3. July and August 2026 sit at the top of every scheme but are not the highest on record (1 of 23 baseline values is above them under the mixed baseline). With `V01` as the value and the mixed baseline, the R5 labels are identical. P5 differs in 2 of 10 months: February is class 2 instead of 3, and June is class 4 instead of 5.

The 100 km circles (310 circle-months, Jan–Oct) differ under R5 in 86 (27.7%; 72 lower), under P5 in 84 (27.1%; 69 lower, 15 higher), under R3 in 42 and under P3 in 39. By month, R5 and P5 respectively: April 17/31 and 24/31, October 23/31 and 18/31, May 11 and 9, July 10 and 4, August 0 and 3. The 50 km circles differ in 37 of 191 R5-classifiable months and 65 of 236 P5-certain months, split about evenly in direction (`h04_item4_2026_circles.csv`).

### 3.5 Item 5: uncertain (P5) and not classifiable (R5), mixed baseline

| Unit | Window | months | P5 uncertain | R5 not classifiable |
|---|---|---|---|---|
| Box | every window | 167 (2012–25), 10 (2026) | 0 | 0 |
| 100 km | Apr–Oct | 3,038 | 32, 1.1% (0.3–1.9) | 0 |
| 100 km | Jun–Sep | 1,736 | 32, 1.8% (0.6–3.3) | 0 |
| 100 km | Nov–Mar | 2,139 | 0 | 0 |
| 50 km | Apr–Oct | 3,038 | 906, 29.8% (25–35) | 1,111, 36.6% (36–37) |
| 50 km | May–Sep | 2,170 | 828, 38.2% (32–45) | 1,019, 47.0% (46–48) |
| 50 km | Jun–Sep | 1,736 | 611, 35.2% (27–43) | 667, 38.4% (37–40) |
| 50 km | Nov–Mar | 2,139 | 345, 16.1% (13–19) | 502, 23.5% (22–24) |
| 50 km | all | 5,177 | 1,251, 24.2% (21–28) | 1,613, 31.2% (31–32) |

Every P5-uncertain month has a value of 0 tied with many zero years. With the VIIRS-only baseline the shares are slightly higher (100 km Apr–Oct: 41 uncertain, 1.3%). In 2026 the 50 km circles show 27% P5-uncertain and 34% R5-not-classifiable in Apr–Oct. The rank scheme leaves about a fifth fewer 50 km months without a class than the ratio scheme. In both schemes about a third of 50 km fire-season months get no class.

### 3.6 Item 6: candidate windows for using converted years (box, 2012–2025; labels in the window that differ from VIIRS-only)

| Window | months | R5 | R3 | P5 | P3 |
|---|---|---|---|---|---|
| Apr–Oct | 98 | 35 (31 lower) | 18 | 29 (24 lower) | 15 |
| May–Sep | 70 | 20 (16 lower) | 10 | 16 (11 lower) | 8 |
| Jun–Sep | 56 | 12 (8 lower) | 4 | 12 (7 lower) | 4 |

Months outside the window would keep their VIIRS-only label, so no other label changes. Narrowing the window from Apr–Oct to Jun–Sep removes April, May and October, which hold most of the downward changes. Under R5 the change count falls from 35 to 12, and under P5 from 29 to 12. In June–September the two schemes change the same number of box labels (12 of 56; 21%), and the 100 km circles show the same: 23.3% and 23.1%. With `V01` the counts are 38/21/12 (R5) and 27/14/11 (P5).

### 3.7 The VIIRS series on its own (`C` against `V01`, same baseline)

| | Box Apr–Oct (98) | Box all (167) | 100 km Apr–Oct (3,038) | Box 2026 Jan–Oct (10) |
|---|---|---|---|---|
| Mixed baseline, R5 | 5 (5.1%, 1–10) | 11 (6.6%) | 10.8% (7–15) | 0 |
| Mixed baseline, P5 | 5 (5.1%, 1–10) | 9 (5.4%) | 9.9% (7–13) | 2 |
| VIIRS-only baseline, R5 | 4 (4.1%, 0–9) | 16 (9.6%) | 14.3% (11–18) | 2 |
| VIIRS-only baseline, P5 | 5 (5.1%, 0–11) | 11 (6.6%) | 12.1% (9–15) | 1 |

The series choice is a smaller effect than the baseline choice (about 5% against 30–36% of box labels). It is not negligible in the circles, where it changes 10–14% of labels, split evenly in direction.

## 4. How strong

- **Solid.** The reproductions hold: checks 1–3, f01's 41 of 105, and its permutation figures. The mixed baseline shifts box and circle labels downward in spring and autumn under both schemes (the share lower is well above the null, p ≤ 0.07 in every case and ≤ 0.015 for the circles). P5 and R5 change nearly the same number of labels in June–September. Small circles are often unclassifiable under either scheme.
- **Moderate.** Under P5 the box excess over the length-only null is not distinguishable from zero (p = 0.19), while under R5 it is (p = 0.024). The box has only 14 evaluated years, and the P5 null is wide (95th percentile 34%), so "not distinguishable" here is a weak negative. In the circles P5 still shows an excess (p = 0.025).
- **Weak.** P5 being less sensitive to the converted level is a 2–5 point difference with intervals that include zero in the box, and it reverses for upward shifts. Disagreement counts are not strictly comparable across schemes either, because P5 spreads months evenly across classes and R5 puts more of them in the end classes. A scheme with more populated boundaries has more chances to flip.

## 5. Limits and surprises

- There is no truth on the real record. A different label under the mixed baseline may reflect real pre-2012 burning (more spring and autumn fire) or a conversion level that is too high. Neither scheme separates the two.
- The intervals resample only evaluated years. The factor 0.2425 was fitted on years that are also evaluated. The circles share years, so the effective sample is about 14 years.
- The permutation null assumes interchangeable years. A trend in the fire regime would show up as "excess".
- `C` before April 2018 is Suomi NPP on flagged-available days. It differs from raw Suomi NPP only on flagged days. The August–October 2026 values are near-real-time rows.
- Ties and floating point. `C` is a sum of fractional daily means, so two months with the same hotspot pattern can differ in the last digit. One 2026 P5 label (Kamloops 100 km circle, May, VIIRS-only baseline) depended on this and is counted here as a tie with May 2025, as the rank rule says. Rounding the values to six decimals leaves every P5 count unchanged and moves R5 counts by at most one circle-month in 3,038.
- Permutation p-values carry Monte Carlo error: box Apr–Oct R5 is 0.024 (5,000 permutations) and 0.025 to 0.033 in the review reruns; P5 is 0.18 to 0.19.
- **Surprise 1.** Rank classes do not remove the length effect; they enlarge it. A mixed 23-year baseline and a 13-year baseline give different P5 labels in about 24% of months even when the years are interchangeable, against 21% under R5.
- **Surprise 2.** The 50 km circles have more unclassifiable months in May–September (47% under R5) than in April or October, because spring burning is widespread and summer fire is concentrated.

## 6. Files

Scripts are in `round5/scripts/`. Run them in this order with `python -I`; each needs only the outputs of `h04_build.py`.

- `h04_build.py`: builds the monthly counts per sensor and `C` for the box, the 100 km circles and the 50 km circles. Runs checks 1 and 2. Writes `out/h04_monthly.csv` and `out/h04_checks.txt`.
- `h04_common.py`: module (not run directly). Loader, masks, f, the `V01` stand-in, and the R5/R3/P5/P3 classifiers.
- `h04_check3.py`: check 3, Protocol B with U1 and SV under R5. Writes `out/h04_check3.csv`.
- `h04_real.py`: Items 1, 3, 4, 5 and 6, plus the series choice. Log in `out/h04_real_log.txt`.
- `h04_perm.py`: Item 2, the permutation null (default 5,000 permutations, about 2 minutes). Writes `out/h04_perm.csv`; log in `out/h04_perm_log.txt`.

Tables are in `round5/out/`.

- `h04_labels.csv.gz`: every label (series × unit × month × baseline/level × scheme), with pct and median.
- `h04_item1_differ.csv`: mixed against VIIRS-only, by series, unit, scheme, window and year set, with intervals and P5 pct/top-of-record statistics.
- `h04_item1_by_month.csv`: the same, by calendar month (box and 100 km).
- `h04_perm.csv`: the permutation null, observed against null.
- `h04_item3_level.csv`: level sensitivity. `h04_item3_contrast.csv`: paired R5 − P5 bootstrap.
- `h04_item4_2026_box.csv`, `h04_item4_2026_circles.csv`: 2026 labels.
- `h04_item5_uncertain.csv`: P5 uncertain and R5 not classifiable.
- `h04_item6_windows.csv`: candidate windows.
- `h04_series_choice.csv`: `C` against `V01`.
- `h04_class_shares.csv`: class base rates.
- `h04_check3.csv`, `h04_checks.txt`: checks.

## 7. Review

**Re-run.** All four analyst scripts were re-run in order (`h04_build`, `h04_check3`, `h04_real`, `h04_perm`). Every table and log was byte-identical to the analyst's, except `h04_labels.csv.gz` (gzip header only; content not compared). The numbers in sections 1 to 3 were then checked against an independent rebuild.

**Independent recomputation** (`scripts/h04-review_build.py`, `h04-review_main.py`, `h04-review_check3.py`, `h04-review_perm.py`, `h04-review_perm12k.py`, `h04-review_extra.py`, `h04-review_diff2026.py`, `h04-review_rounded.py`; tables `out/h04-review_*.csv`). It starts from the parquet file and the availability flag and uses its own daily cube, `C`, masks, factor and classifiers. It did not use the analyst's code or `f03_common.py`.
- Checks 1 to 3 reproduce exactly: 116 months, 48,233 and 198,916, f = 0.24248; `C` for the box 629.5, 2,266.5, 4,751.1, 7,101.7, 690.0, 29,589.9; Protocol B R5 U1 84.38% and 79.70%, SV 66.13% and 64.49%.
- f01 reproduction, 41 of 105 (38 lower, 3 higher): exact. A check that circle membership uses the same planar rule as the data (`x_km` equals 111.195 km per degree times cos 50.75 degrees, to 0.0005 km) passed.
- Item 1 (all schemes, windows, box and 100 km and 50 km): all counts identical to the report, including by calendar month, the by-month direction split, class shares, mean absolute `pct` difference (0.068 and 0.077) and highest-on-record agreement (96.9%).
- Item 3 (all five levels, box and circles, two windows): identical counts and shares; paired bootstrap at ÷ 1.6 gives +5.1 points (−4.1 to +13.3) in the box and +2.1 (−0.8 to +5.0) in the circles, as reported.
- Item 4 box labels: identical for all schemes. Item 5: identical (906 and 1,111 at 50 km; 32 at 100 km; all uncertain months are zeros under the mixed baseline). Item 6 and the `C` against `V01` table: identical.
- Item 2, own permutation code (value and baseline both from the mixed array; 3,000 and 12,000 permutations, other seeds): box Apr–Oct R5 null 21.5–21.8% (95th 32.7–33.7%), p 0.025–0.033; P5 null 24.3–24.4%, p 0.18–0.19; circles R5 21.0–21.1%, p ≤ 0.001; P5 24.1%, p 0.027. All agree with the analyst within Monte Carlo error.

**Corrections.**

| Item | Before | After | Matters |
|---|---|---|---|
| 2026, 100 km circles, P5, Jan–Oct, labels differing | 83 (26.8%; 14 higher) | 84 (27.1%; 15 higher); one circle-month where a float rounding broke a tie with May 2025 | changes a number only |
| 100 km May 2026, P5 differing circles | 8 | 9 | changes a number only |
| Direction (mixed lower) significance in the box | p ≤ 0.065 | p ≤ 0.07 (box P5 0.065 to 0.074 across seeds) | wording only |
| Limits | no note on ties or Monte Carlo error | two bullets added | wording only |

No headline number or conclusion changed.

**Looked for and not found.** Conversion factor fitted on years it is tested on: the factor uses 2012–2021 VIIRS months and is applied to 2003–2011, so the converted years are not tested against it. It is fitted on years that are also evaluated as months of 2012–2021, which the report already states; the real record has no truth, so this affects only the level, which item 3 varies. Own year in its baseline: excluded everywhere. UTC keys: local dates used. Static source and non-vegetation rows: removed by `use`. Availability column and NOAA-20 spring 2018 exception: correct. Masked sensor-months: handled as NaN for both baselines, which share the same years. Rank off-by-one and ties: match SPEC (tie rule 20%, half weight). Intervals: whole-year resamples.

**Not confirmed.** The tie decision in the one 2026 circle-month above is a numerical judgement. Whether the excess over the length-only null reflects real pre-2012 burning or a high conversion level cannot be known on this record. The P5 box excess is not distinguishable from zero with 14 years.
