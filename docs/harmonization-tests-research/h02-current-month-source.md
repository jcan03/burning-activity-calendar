# h02: Current month from NOAA-20 or the combined series, inside the hindcast

> Working file from the fourth follow-up (14 November 2026). The series, class schemes (`R5`, `P5`) and designs (`U1`, `SV`) are defined in [h00-definitions.md](h00-definitions.md), which is what "the spec" means below. The scripts and tables named here are kept outside version control with the cached data.

## 1. Summary

The hindcast (Protocol B, 202 splits, k = 5) was re-scored on the 2018-04 to 2021-12 test months with the current month taken from Suomi NPP (S), NOAA-20 × 1.0245 (N20s) or the combined series (Csn20 = C). **On the whole box the source of the current month makes no clear difference.** The 5-class fire-season agreement of the mixed baseline is 87.6% with S, 88.7% with N20s and 89.8% with Csn20 (ratio classes R5, Truth-S). Under rank classes (P5) it is 88.8%, 81.9% and 87.6%. The NOAA-20 drop under P5 (−6.9 points, 95% year CI −19.6 to +5.7) comes almost entirely from 2018, and is −0.6 points without 2018. **On the 100 km circles the loss is real when the truth is Suomi NPP's own label** (an upper bound, because that truth shares S's current value; against Truth-C, which contains NOAA-20, the N20s loss is −0.7, −5.7 to +2.0): −11.7 points for N20s (−16.4 to −7.0) and −6.1 for Csn20 (−8.7 to −2.6) under R5, and −9.9 and −5.1 under P5. Against Truth-C the calendar case (Csn20 current, U1C baseline) scores 79.6% (R5) and 75.2% (P5) at 100 km, close to the old S/U1/Truth-S reference (80.7% and 75.6%). **The mixed baseline has a positive gain over the VIIRS-only benchmark in every box and 100 km fire-season case**, by +15 to +23 points on the box and +3 to +13 points at 100 km, and the interval excludes zero in all but one case (N20s, Truth-S, P5, 100 km: +6.5, −0.0 to +12.1). The gain for N20s against Truth-S at 100 km shrinks to +2.7 points (R5, +0.2 to +4.7), and to +1.7 (−1.3 to +3.5) without 2018. The combined series beats NOAA-20 alone by about 5 points at 100 km. Single satellites score the same against Truth-C (S 75.4% and N20s 74.6% under R5), and Csn20's loss against Truth-S is about half of N20s's loss. Both facts fit "C is better because half of it is the satellite the truth is built from". The loss is almost all month-to-month scatter between satellites, not scale: NOAA-20 with factor 1.0, 1.0245 or an oracle factor changes agreement by at most 1.6 points. Only 26 box fire-season months (19 without 2018) from 4 years (3 whole) carry these results. Box intervals are 6 to 15 points wide for exact agreement and up to 36 points wide for contrasts.

## 2. Method

- **Data** as in the round 5 spec. Hotspots `use == True`, keyed by `ym_local` / `local_date`. M and S use standard (SP) rows only, as in round 3 a01; in 2012–2021 all rows are SP. NOAA-20 is the raw monthly count (all streams). C and Csn20 are built daily from the f03 flag `avail_cat_plus_partial`, with NOAA-20 forced available on 2018-04-01..06-04. They are the mean over available VIIRS satellites of the scaled counts (S × 1, NOAA-20 × 1.0245, NOAA-21 × 1.0503), summed by month. C equals Csn20 exactly in 2018-04..2021-12 (max difference 0 over all units). `Cst` = C from April 2018 and S before. Units are the box and 31 circles at 50, 100 and 150 km (centres from `circles.csv`, same km projection as round 3 a02). The conversion factor is always fitted on the box.
- **Splits.** The 202 standard splits as in `a01_hindcast.py`: two chronological, then 200 from `default_rng(1)`. In each split, f = ΣM/ΣS over the split's VIIRS-era years (all valid months, box).
- **Scored rows.** For each split, each VIIRS-era year among 2018–2021, and each valid month from 2018-04 (2016-02, 2020-08 and 2020-09 excluded, as in the stable-period rules). Year sets are "2018-21" (2018 Apr–Dec plus 2019–21) and "2019-21".
- **Current-month sources.** S; N20s = NOAA-20 × 1.0245; N20x1 = NOAA-20 × 1.0. N20o = NOAA-20 × an *oracle* factor per unit (ΣS/ΣNOAA-20 over all scored months in that unit; box 1.013). N20oy = per-unit, per-year oracle (box 2018–2021: 1.084, 1.043, 1.019, 0.994). Csn20 = C.
- **Baselines** (calendar month, the other nine years of 2012–2021): U1 = M/f for MODIS-era years plus S for VIIRS-era years. U1C = M/f plus Cst. SV = S, other VIIRS-era years only. SVC = Cst, other VIIRS-era years only.
- **Truths.** Truth-S (TS) is the class of S against S of the nine other years. Truth-C (TC) is the class of Cst against Cst of the nine other years.
- **Classes.** R5, R3, P5 and P3 exactly as in the spec. P3 = min(floor(3·pct), 2). R5/R3 are not classifiable when the baseline median is below 1. P5/P3 are "uncertain" when ties make up 20% or more of the baseline (with SV's four-year baseline a single tie is enough).
- **Scores.** Rows where the truth is not classifiable are dropped (shares in tables). A design label that is not classifiable counts as a miss in *exact* and *within one*; its share is reported. Kappa uses rows where both are classifiable. Rates are pooled over all split rows.
- **Intervals.** Year-block bootstrap: 2,000 resamples of the 4 (or 3) test years, from per-year sums pooled over splits and circles (seed 11). The split SD is the SD across splits of per-split agreement (splits with at least one scored year).
- **Contrasts.** Gain = design minus matching benchmark (U1−SV, U1C−SVC), same source and truth. Source loss = source minus S (or minus Csn20), same baseline and truth. Both use the paired year bootstrap.

**Checks reproduced** (`h02_check.txt`, `h02_check3.csv`):
1. 116 stable months: M = 48,233, S = 198,916, ratio 0.2425. Exact.
2. C for the box: 2022-07 629.5, 2022-08 2,266.5, 2023-07 4,751.1, 2024-07 7,101.7, 2024-11 690.0, 2026-08 29,589.9. All within 0.1% of the f03 values.
3. Protocol B, box, all ten years as test years, mean over splits: U1 84.36% fire season and 79.71% all months. SV 66.13% and 64.50%. Matches the spec (84.4 / 79.7 / ~66 / ~65). Under P5 the same run gives U1 86.2% / 79.8% and SV 60.3% / 60.9%.

Before April 2018, C (S on its available days) differs from S in 3 of 74 box months (2012-03, 2012-11, 2017-09; −1% to −12%). As the task asks, `Cst` uses S itself there.

## 3. Results

### 3.1 Main table, fire season (April–October), test years 2018-04..2021-12

Exact % with 95% year-bootstrap CI. "Gain" is points over the matching VIIRS-only benchmark (SV for U1, SVC for U1C). Box: 2,550 rows over splits (26 distinct months). 100 km: 79,050 rows (806 distinct circle-months).

| Unit | Scheme | Current / baseline / truth | Exact % | Split SD | Within 1 | Kappa | Not classif. % | Benchmark % | Gain (95% CI) |
|---|---|---|---|---|---|---|---|---|---|
| box | R5 | S / U1 / TS (reference) | 87.6 (81.5–94.5) | 8.4 | 99.5 | 0.825 | 0.0 | 72.4 | +15.2 (+9.6 to +19.5) |
| box | R5 | N20s / U1 / TS | 88.7 (85.8–92.3) | 8.2 | 100 | 0.838 | 0.0 | 73.3 | +15.4 (+5.9 to +23.6) |
| box | R5 | Csn20 / U1 / TS | 89.8 (84.7–94.1) | 7.8 | 100 | 0.855 | 0.0 | 73.3 | +16.5 (+6.6 to +21.5) |
| box | R5 | S / U1C / TC | 86.3 (79.9–93.3) | 8.4 | 98.3 | 0.805 | 0.0 | 71.9 | +14.4 (+5.1 to +20.7) |
| box | R5 | N20s / U1C / TC | 89.3 (86.0–93.2) | 7.7 | 99.5 | 0.845 | 0.0 | 72.8 | +16.5 (+8.0 to +24.2) |
| box | R5 | **Csn20 / U1C / TC (calendar)** | 90.4 (85.2–94.1) | 9.2 | 99.0 | 0.862 | 0.0 | 72.8 | +17.6 (+7.7 to +22.2) |
| box | P5 | S / U1 / TS (reference) | 88.8 (81.3–94.4) | 9.1 | 100 | 0.858 | 0.0 | 66.2 | +22.6 (+15.6 to +28.8) |
| box | P5 | N20s / U1 / TS | 81.9 (72.9–88.1) | 8.4 | 100 | 0.771 | 0.0 | 65.6 | +16.3 (+4.2 to +31.9) |
| box | P5 | Csn20 / U1 / TS | 87.6 (83.0–94.2) | 8.6 | 100 | 0.843 | 0.0 | 66.6 | +21.0 (+15.6 to +30.1) |
| box | P5 | **Csn20 / U1C / TC (calendar)** | 87.6 (83.0–94.2) | 8.6 | 100 | 0.843 | 0.0 | 66.6 | +21.0 (+15.6 to +30.1) |
| c100 | R5 | S / U1 / TS (reference) | 80.7 (75.0–88.0) | 4.6 | 95.6 | 0.731 | 0.1 | 72.1 | +8.6 (+5.9 to +11.0) |
| c100 | R5 | N20s / U1 / TS | 69.0 (62.3–78.4) | 5.7 | 88.6 | 0.569 | 0.1 | 66.3 | +2.7 (+0.2 to +4.7) |
| c100 | R5 | Csn20 / U1 / TS | 74.5 (67.1–82.9) | 5.7 | 93.6 | 0.647 | 0.1 | 69.3 | +5.3 (+4.0 to +6.9) |
| c100 | R5 | S / U1C / TC | 75.4 (67.5–84.2) | 6.2 | 94.1 | 0.661 | 0.1 | 67.9 | +7.5 (+6.6 to +8.6) |
| c100 | R5 | N20s / U1C / TC | 74.6 (69.0–83.1) | 5.2 | 95.5 | 0.652 | 0.1 | 70.1 | +4.6 (+2.2 to +7.6) |
| c100 | R5 | **Csn20 / U1C / TC (calendar)** | 79.6 (73.9–86.0) | 4.2 | 96.0 | 0.720 | 0.1 | 71.4 | +8.2 (+5.3 to +10.7) |
| c100 | P5 | S / U1 / TS (reference) | 75.6 (63.8–86.7) | 9.3 | 96.4 | 0.713 | 2.2 | 63.0 | +12.6 (+6.3 to +18.0) |
| c100 | P5 | N20s / U1 / TS | 65.7 (52.0–81.8) | 10.5 | 87.6 | 0.612 | 5.3 | 59.2 | +6.5 (−0.0 to +12.1) |
| c100 | P5 | Csn20 / U1 / TS | 70.6 (58.1–84.5) | 9.8 | 94.4 | 0.648 | 2.2 | 62.3 | +8.2 (+2.7 to +13.0) |
| c100 | P5 | S / U1C / TC | 71.6 (61.3–83.7) | 8.0 | 94.7 | 0.663 | 2.4 | 59.3 | +12.3 (+8.6 to +14.6) |
| c100 | P5 | N20s / U1C / TC | 71.2 (58.5–82.1) | 8.8 | 93.0 | 0.685 | 5.2 | 63.2 | +8.0 (+1.1 to +13.8) |
| c100 | P5 | **Csn20 / U1C / TC (calendar)** | 75.2 (64.1–84.6) | 7.8 | 96.8 | 0.708 | 2.1 | 66.3 | +9.0 (+2.9 to +13.5) |

On the box, P5 Truth-S and Truth-C are identical in every scored month, and U1 and U1C give identical P5 labels. Those rows are therefore duplicates. Truth not classifiable: 0% in the box. At 100 km it is 0% under R5, 5.6% under P5 Truth-S and 2.4% under P5 Truth-C. P5 extras (mean |Δpct|, highest-on-record agreement): box reference 0.041 / 97.0%, box calendar 0.041 / 97.0%, 100 km reference 0.056 / 97.6%, 100 km calendar 0.055 / 98.1%. The other cases are in `h02_summary_tables.txt`.

**Without 2018** (2019-21, 1,885 box rows / 19 months; 58,435 circle rows / 589 circle-months), R5 / P5 exact %:

| Unit | S/U1/TS | N20s/U1/TS | Csn20/U1/TS | Csn20/U1C/TC | N20s/U1C/TC |
|---|---|---|---|---|---|
| box R5 | 88.5 | 90.0 | 88.0 | 88.8 (gain +16.2, +2.3 to +23.0) | 90.8 |
| box P5 | 87.2 | 86.5 | 88.8 | 88.8 (gain +22.4, +15.4 to +34.3) | 86.5 |
| c100 R5 | 81.3 | 70.8 | 76.3 | 81.0 (gain +7.0, +4.7 to +8.7) | 76.3 |
| c100 P5 | 74.3 | 65.7 | 70.3 | 73.6 (gain +6.6, −1.5 to +11.7) | 69.4 |

**Per test year** (fire season, box P5): S/U1/TS 93.4, 77.3, 89.0, 95.5 for 2018–2021. N20s/U1/TS 68.7, 87.3, 89.0, 83.8. The N20s box P5 loss sits in 2018 (−24.7 points) and 2021 (−11.7). 2019 goes the other way (+10.0). At 100 km R5, N20s is below S in every year (−15.2, −10.9, −17.9, −4.4).

### 3.2 (a) Points lost when the current month is not Suomi NPP (fire season; same baseline and truth)

| Unit | Years | Scheme | Truth / baseline | N20s − S | Csn20 − S | N20s − Csn20 |
|---|---|---|---|---|---|---|
| box | 2018-21 | R5 | TS / U1 | +1.1 (−3.9 to +6.7) | +2.2 (−3.1 to +6.8) | −1.1 (−7.3 to +4.7) |
| box | 2018-21 | P5 | TS / U1 | −6.9 (−19.6 to +5.7) | −1.2 (−6.8 to +3.4) | −5.7 (−13.5 to +3.1) |
| box | 2019-21 | P5 | TS / U1 | −0.6 (−11.7 to +10.0) | +1.6 (0.0 to +4.6) | −2.3 (−11.7 to +5.4) |
| box | 2018-21 | R5 | TC / U1C | +3.0 (−0.8 to +7.3) | +4.1 (−0.4 to +8.3) | −1.1 (−7.3 to +3.4) |
| c100 | 2018-21 | R5 | TS / U1 | −11.7 (−16.4 to −7.0) | −6.1 (−8.7 to −2.6) | −5.5 (−8.7 to −3.3) |
| c100 | 2018-21 | P5 | TS / U1 | −9.9 (−13.0 to −4.9) | −5.1 (−7.4 to −2.3) | −4.8 (−6.3 to −2.6) |
| c100 | 2019-21 | R5 | TS / U1 | −10.5 (−17.9 to −4.4) | −5.0 (−7.1 to −1.5) | −5.4 (−10.9 to −2.9) |
| c100 | 2019-21 | P5 | TS / U1 | −8.6 (−12.1 to −3.3) | −4.1 (−6.7 to −1.3) | −4.6 (−6.5 to −2.0) |
| c100 | 2018-21 | R5 | TC / U1C | −0.7 (−5.7 to +2.0) | +4.2 (+1.6 to +6.5) | −4.9 (−8.3 to −2.2) |
| c100 | 2018-21 | P5 | TC / U1C | −0.4 (−2.8 to +3.3) | +3.6 (+0.9 to +6.9) | −4.0 (−5.8 to −2.5) |
| c50 | 2018-21 | R5 / P5 | TS / U1 | −9.7 / −9.8 | −6.1 / −2.8 | −3.6 / −6.9 |
| c150 | 2018-21 | R5 / P5 | TS / U1 | −11.7 / −11.8 | −3.3 / −6.8 | −8.4 / −5.1 |

The VIIRS-only benchmark loses less from the same change: at 100 km R5/TS, SV drops by −5.7 for N20s against −11.7 for U1. A design that agrees more with the truth has more to lose.

### 3.3 (b) Mixed baseline against the VIIRS-only benchmark, other seasons and coarse classes (2018-21)

Exact % (gain in points, 95% CI). The full grid for 50/100/150 km and all four seasons is in `h02_summary_tables.txt`.

| Unit | Season | Scheme | S/U1/TS | N20s/U1/TS | Csn20/U1C/TC |
|---|---|---|---|---|---|
| box | JJAS | R5 / P5 | 91.7 (+12.2) / 91.0 (+26.0) | 91.9 (+12.0) / 90.1 (+26.8) | 94.2 (+14.0) / 92.9 (+27.9) |
| box | MJJAS | R5 / P5 | 89.0 (+9.9) / 91.3 (+24.1) | 91.8 (+13.0) / 90.5 (+24.7) | 91.8 (+13.2) / 92.7 (+25.5) |
| box | ALL | R5 / P5 | 79.5 (+12.8) / 80.3 (+16.0) | 76.6 (+12.9) / 77.2 (+15.2) | 84.3 (+14.7) / 82.4 (+19.1) |
| box | FS | R3 / P3 | 94.3 (+12.9) / 89.5 (+9.3) | 94.6 (+13.6) / 88.4 (+7.6) | 95.1 (+13.9) / 89.9 (+8.7) |
| c100 | JJAS | R5 / P5 | 83.6 (+7.0) / 78.1 (+14.5) | 79.2 (+5.5) / 69.8 (+10.0) | 83.2 (+8.1) / 77.8 (+12.6) |
| c100 | MJJAS | R5 / P5 | 82.3 (+6.5) / 75.7 (+12.6) | 72.8 (+3.0) / 65.5 (+7.4) | 80.8 (+7.3) / 75.0 (+9.3) |
| c100 | ALL | R5 / P5 | 76.9 (+6.1) / 68.9 (+8.2) | 66.1 (+1.5) / 59.1 (+2.8) | 75.1 (+5.5) / 68.6 (+5.2) |
| c100 | FS | R3 / P3 | 87.6 (+7.3) / 85.1 (+9.0) | 78.6 (+3.6) / 73.4 (+0.9) | 87.8 (+7.2) / 84.0 (+4.9) |
| c150 | FS | R5 / P5 | 90.1 (+16.4) / 86.3 (+18.3) | 78.4 (+8.7) / 74.5 (+12.4) | 90.3 (+16.4) / 86.3 (+18.3) |
| c50 | FS | R5 / P5 | 69.0 (+0.5) / 74.3 (+11.1) | 59.3 (−3.2) / 64.5 (+5.8) | 68.0 (+0.9) / 71.8 (+7.8) |

Share of splits in which the design beats its benchmark (fire season, 2018-21). Box: R5 74–81%, P5 77–93%. 100 km: 89–95% for S/U1 and the calendar case under R5, but 64% for N20s/U1/TS (R5), where it loses in 31% of splits. At 50 km under R5 the mixed baseline does not beat the benchmark even with S (+0.5, −2 to +4). Under P5 it does (+11.1).

### 3.4 (d) Scale against scatter (Truth-S, U1, fire season, 2018-21, exact %)

| Unit | Scheme | S | N20 × 1.0 | N20 × 1.0245 | N20 × oracle (unit) | N20 × oracle (unit-year) |
|---|---|---|---|---|---|---|
| box | R5 | 87.6 | 88.4 | 88.7 | 88.6 | 88.9 |
| box | P5 | 88.8 | 83.5 | 81.9 | 82.1 | 82.4 |
| c100 | R5 | 80.7 | 68.9 | 69.0 | 68.8 | 69.5 |
| c100 | P5 | 75.6 | 65.4 | 65.7 | 65.2 | 65.7 |
| c50 | R5 / P5 | 69.0 / 74.3 | 59.3 / 64.0 | 59.3 / 64.5 | 59.0 / 63.3 | 59.1 / 64.8 |
| c150 | R5 / P5 | 90.1 / 86.3 | 78.6 / 75.0 | 78.4 / 74.5 | 78.7 / 74.2 | 76.9 / 75.5 |

Any factor, including one fitted on the test months themselves and per year, gives the same agreement within 1.6 points. Under P5 the rank of a scaled value moves only when the factor crosses a baseline value, so the factor barely matters. Month-to-month scatter of N20s against S on the scored months (`h02_n20_scatter.csv`, months with S ≥ 10): SD of log(N20s/S) is 0.17 on the box, 0.27 at 100 km and 0.36 at 50 km. The median absolute difference is 8% on the box and 12.5% at 100 km, against 4% and 6% for C against S. On the box, the sum of N20s/S by year is 0.945, 0.982, 1.006 and 1.031 for 2018–2021. Over all scored months it is 1.013, so 1.0245 is about 1% high on these months. That 1% does not move the scores.

## 4. How strong

- **Solid, with a caveat on what it measures.** At 100 km and 50/150 km, a NOAA-20 current month loses about 10–12 points of agreement with Suomi NPP's own label, and the combined series loses about 5–6. S scores 'perfectly' on the current value by construction (same value as the truth), so this is the cost of differing from Suomi NPP, not of a worse baseline. Against Truth-C the N20s loss is −0.7 at 100 km. No truth here is independent of both satellites. The CIs exclude zero, the losses appear in every test year, and they are the same with and without 2018. The loss is scatter between satellites, not scale (3.4).
- **Solid.** Against its own truth (Csn20/U1C/TC) the calendar case at 100 km reaches 79.6% (R5) and 75.2% (P5), level with the old reference (80.7% and 75.6%). Its gain over SVC (+8.2 R5, +9.0 P5) is the same size as the reference gain (+8.6, +12.6 under P5).
- **Moderate.** The mixed baseline has a positive gain over the benchmark for every source on the box (+15 to +23) and at 100 km (+3 to +13) in the fire season; the interval touches or includes zero for N20s at 100 km under P5 and, without 2018, for N20s at 100 km under both schemes and for the calendar case at 100 km under P5 (−1.5 to +11.7). At 50 km under R5 the gain is about zero even for S. The weakest cases are N20s against Truth-S at 100 km: +2.7 R5 (+0.2 to +4.7), +6.5 P5 (−0.0 to +12.1), and +1.7 R5 without 2018 (−1.3 to +3.5).
- **Weak.** Everything on the box. There are 26 distinct fire-season months (19 without 2018) in 4 (3) years. The splits reuse them, so the 2,550 rows are not independent. Box exact-agreement CIs are 7 to 15 points wide, and the box N20s − S contrast under P5 runs from −19.6 to +5.7. The box shows no loss under R5 (+1.1, +2.2) and a loss under P5 driven by 2018. Neither is distinguishable from zero.
- **Interval caveat.** A bootstrap over 3–4 clusters understates the uncertainty. It can produce only a handful of distinct resamples, and the year-to-year spread is estimated from 3–4 values. The true intervals are wider than shown. Some 100 km intervals look very narrow (for example −2.3, −3.0 to −1.3) only because the 3 years happened to agree.

## 5. Limits and surprises

- **(c) Is the combined series better than NOAA-20 alone, and why?** Against Truth-S, Csn20 beats N20s by about 5 points at 100 km (5.5 R5, 4.8 P5). Csn20's loss relative to S (−6.1) is about half of N20s's (−11.7). That is what one would expect if C's departure from S is half of NOAA-20's departure, because C = (S + N20s)/2 on most days. Against Truth-C, which contains NOAA-20 for half and *is* Csn20 in the scored year, the two single satellites score the same at 100 km: S 75.4%, N20s 74.6% (R5); 71.6% and 71.2% (P5). Csn20 scores 79.6% / 75.2% there only because it is the truth's own value. So in this test the advantage of C over NOAA-20 alone is fully explained by C containing the satellite the truth is made from. These years hold no truth independent of both satellites, so the test cannot show whether averaging two satellites gives a *truer* label. It shows only that C is closer to either single-satellite truth than the other satellite is.
- **2018.** NOAA-20's 2018 months (catalogue silent before 5 June; S/N20s = 1/0.945 in 2018) cause the box P5 loss. Without 2018 the box loss is gone (−0.6 points). At 100 km, dropping 2018 changes the losses by 1–1.5 points.
- **Surprise.** On the box, NOAA-20 and C as the current month score slightly *better* than S itself under R5 (88.7 and 89.8 against 87.6). This is noise in 26 months: with S the misses come only from the baseline, and a different current value can land in the right class by chance.
- **Surprise.** On the box, Truth-S and Truth-C give the same P5 class in all 26 fire-season months and in 42 of 43 months overall. Under R5 they differ in 2 of 26 (8%). At 100 km the truths differ in 17–19% of circle-months under both schemes (`h02_truth_agree.csv`), so "which truth" matters at 100 km and not on the box.
- **Not-classifiable shares** at 100 km under P5 are higher for N20s (5.3%) than for S or C (2.2%). Those misses are counted against N20s. This comes from ties at zero: of the 806 scored fire-season circle-months, NOAA-20 has 120 with zero hotspots, S has 69 and C has 65. For SV/SVC under P5, one tie in four baseline years makes the label uncertain (7.5–9.6% not classifiable for SV with S at 100 km).
- **Partly done.** The task asked for the gain with its interval for every source × baseline combination. Every combination, including SV/SVC, N20x1 and the oracle factors, is in `h02_scores.csv` / `h02_contrasts.csv`. The tables here show a subset. The truth is Suomi NPP-based in 2012–2018-03 for both truths, as the task defines. The spec's C before April 2018 (S on available days) differs from S in 3 box months; the reviewer scored that variant and the calendar-case numbers did not change (see Review).

## 6. Files

Scripts (run in order with `python -I`, from any directory; each needs only the previous one's output):
- `round5/scripts/h02_build.py`: monthly M, S, NOAA-20, NOAA-21, C and Csn20 for the box and the 50/100/150 km circles. Runs checks 1 and 2. Under 1 s.
- `round5/scripts/h02_hindcast.py`: check 3, the 202-split hindcast for all sources × baselines × truths × schemes, bootstraps, contrasts, scatter and truth agreement. About 30 s.
- `round5/scripts/h02_summary.py`: report tables.

Tables (`round5/out/`):
- `h02_monthly.npz`, `h02_monthly_box.csv`: monthly series (all units / box only).
- `h02_check.txt`, `h02_check3.csv`, `h02_log.txt`: check output, check 3 table, oracle factors and scatter log.
- `h02_scores.csv`: one row per unit × season × year set × truth × scheme × source × baseline. Exact with CI, split SD, within one, kappa, not-classifiable shares, and for P5 mean |Δpct| and highest-on-record agreement.
- `h02_contrasts.csv`: gains over benchmark and source-vs-source differences, with year CI, split SD, share of splits better or worse, and per-year differences.
- `h02_peryear.csv`: exact agreement per test year (box and 100 km, R5 and P5).
- `h02_truth_shares.csv`: share of rows in each true class.
- `h02_truth_agree.csv`: Truth-S against Truth-C agreement on distinct months.
- `h02_n20_scatter.csv`: NOAA-20 and C against S, month-to-month scatter.
- `h02_summary_tables.txt`: all report tables, including the full season × scheme × radius grid.
- Review: `round5/scripts/h02-review.py`; `round5/out/h02-review_headline.csv`, `h02-review_log.txt`, `h02-review_rerun_*.log`, `h02-review_orig/` (copy of the analyst tables before the re-run).

## Review

**Re-run.** `h02_build.py`, `h02_hindcast.py` and `h02_summary.py` were re-run. `h02_scores.csv`, `h02_contrasts.csv`, `h02_peryear.csv`, `h02_truth_shares.csv`, `h02_n20_scatter.csv`, `h02_truth_agree.csv`, `h02_check3.csv` and `h02_summary_tables.txt` are byte-identical to the analyst's originals (kept in `out/h02-review_orig/`).

**Independent recompute** (`scripts/h02-review.py`, no analyst code; own daily cube from the parquet, own km projection, own availability handling with the NOAA-20 2018-04-01..06-04 exception, own rank and ratio classifiers, own bootstrap with a different seed, 2,000 draws). Box and 100 km, fire season, 202 splits:
- Check 1: M 48,233, S 198,916, ratio 0.24248. Check 3 (all ten years, box, mean over splits): U1 R5 84.36% FS / 79.71% ALL, SV 66.13% / 64.50%; P5 U1 86.23 / 79.75, SV 60.30 / 60.87. All equal to the report.
- Every exact-agreement figure in the main table (S, N20s, Csn20 × U1, U1C, SV, SVC × TS, TC, R5 and P5, box and c100) matches to the 0.1 point shown. Row counts match (2,550 box; 79,050 c100 R5; 74,634 / 77,185 c100 P5), as do 26 months and 806 circle-months.
- Gains, source losses and C-vs-N20s contrasts match to 0.1 point, and the interval ends to within 0.5 point (different bootstrap seed). Example: c100 R5 N20s − S −11.7 (−16.4 to −7.0) against mine −11.7 (−16.4 to −7.0). Box P5 N20s − S −6.9 (−19.6 to +5.7) against mine −6.9 (−19.6 to +5.7). The 2019-21 values also match (box P5 N20s − S −0.6 (−11.7 to +10.0); c100 R5 gain for N20s +1.7 (−1.3 to +3.5)).
- Per-year box P5 (S 93.4, 77.3, 89.0, 95.5; N20s 68.7, 87.3, 89.0, 83.8) and c100 R5 per-year N20s − S (−15.2, −10.9, −17.9, −4.4) match.
- (d): N20 × 1.0 / × 1.0245 / unit oracle: box R5 88.4 / 88.7 / 88.6, box P5 83.5 / 81.9 / 82.1, c100 R5 68.9 / 69.0 / 68.9, c100 P5 65.4 / 65.7 / 65.2. Box oracle factor 1.0132. SD of log(N20s/S) 0.170 (box), 0.271 (c100); median absolute difference 7.9% / 12.5% for N20s and 4.1% / 6.0% for C. All match.
- Zero-hotspot circle-months at 100 km (fire season, scored): N20s 120, S 69, C 65. Match.

**Checks for the listed pitfalls.** Months are keyed by local date. Only `use` rows are used. The own year is left out of every baseline and every truth. The availability column is `avail_cat_plus_partial`, with the NOAA-20 spring 2018 exception. M and S use standard rows, NOAA-20 all rows, which are the same in 2018-2021. Rank class: below-count plus half the ties, divided by n, `min(floor(5 pct), 4)`, uncertain when ties are 20% or more; no off-by-one. Intervals resample whole years. Benchmarks are matched (SV with S-built truths, SVC with C-built). The factor f is fitted on the box over the split's VIIRS-era years, which include the test year itself (the round 3 protocol). Refitting f without the test year changes no exact figure by more than 0.5 point (box R5 S/U1/TS 88.0, N20s 88.6, Csn20 89.8; c100 R5 80.7, 69.0, 74.5), so this does not matter here.

**Corrections made to the report** (no number changed; all numbers were right):
1. Summary and section 4 said the mixed baseline "beats the VIIRS-only benchmark in every box and 100 km fire-season case". Before: that wording. After: positive gain in every case, interval excludes zero in all but one fire-season case with 2018, and N20s at 100 km includes or touches zero under P5 and, without 2018, under both schemes (R5 −1.3 to +3.5, P5 −4.3 to +14.2); about zero at 50 km under R5 even for S. Wording only.
2. Summary said box intervals are "10 to 35 points wide"; section 4 said "7 to 15". Now: 6 to 15 for exact agreement and up to 36 for contrasts (2019-21 box P5 gain +20.6, +4.4 to +40.9).
3. The 100 km loss of −11.7 was described as "real" without saying it is measured against a truth that shares S's current value. Added that it is an upper bound: against Truth-C the N20s loss is −0.7 (−5.7 to +2.0), and neither truth is independent of both satellites. Changes how (a) should be read, not the number.
4. "Not done" said the spec's C-before-April-2018 variant was not scored. The reviewer scored it: box and 100 km exact agreement for Csn20/U1C/TC, SVC, N20s and S are identical to 4 decimals (box R5 90.35 / 72.78, c100 R5 79.56 / 71.38, c100 P5 75.23 / 66.26).

**Could not confirm.** The 50 km and 150 km figures, the J-A-S-O seasons beyond JJAS, R3/P3 and the split-share percentages (64%, 31%, 74-81%) were not recomputed. The interval caveat stands: bootstrap over 3 or 4 years is too narrow to be taken at face value, and the 100 km results come from 31 overlapping circles of one box and the same four years, so the effective sample is closer to the 26 box months than to 79,050 rows.
