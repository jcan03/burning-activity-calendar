# Round 5 cross-check (h01–h04)

> Working file from the fourth follow-up (14 November 2026). The series, class schemes (`R5`, `P5`) and designs (`U1`, `SV`) are defined in [h00-definitions.md](h00-definitions.md), which is what "the spec" means below. The scripts and tables named here are kept outside version control with the cached data.

Scope: the four reviewed reports were read in full; numbers reported by more than one topic were compared; headline numbers were recomputed with an own script (`scripts/x01_crosscheck.py`, log `out/x01_log.txt`, table `out/x01_results.csv`; about 11 s). This page reports what the tests show. It does not recommend a method.

Notation: U1 = converted MODIS plus VIIRS baseline; SV = short VIIRS-only benchmark (4 years in h01/h02, 5 in h03); gain = U1 minus SV in points of exact five-class agreement with the truth; FS = Apr–Oct. Intervals are 95% year-block bootstraps unless stated. R5 and P5 agreement rates are not comparable with each other (different base rates); gains within one scheme are.

## 1. Reconciled numbers to use

| # | Quantity | Box | 100 km circles | Source | Recomputed here |
|---|---|---|---|---|---|
| 1 | Protocol B, current S, 2012–21, FS, R5: U1 / SV / gain | 84.4 / 66.1 / +18.2 [13.8, 22.7] | 77.4 / 66.7 / +10.6 [8.3, 13.1] | h01 | yes, exact |
| 2 | same, P5 | 86.2 / 60.3 / +25.9 [18.8, 33.8] | 73.9 / 56.8 / +17.0 [13.1, 20.9] | h01 | yes, exact |
| 3 | same, all months, R5 / P5 gain | +15.2 / +18.9 | +8.4 / +13.0 | h01 | yes, exact |
| 4 | 100 km gain on rows all designs can classify, FS, R5 / P5 | – | +9.8 / +15.4 | h01 review | no |
| 5 | Gain by k (SV years 8,7,6,5,4), FS, R5 | 12.7, 9.0, 14.1, 13.6, 17.1 | 10.4, 5.5, 9.2, 6.8, 10.4 | h01 | no |
| 6 | same, P5 | 10.9, 15.8, 23.0, 28.7, 24.9 | 9.0, 11.2, 15.9, 22.7, 16.8 | h01 | no |
| 7 | Hindcast level error ×1.6, change in U1 FS, R5 / P5 | −13.2 [−18.0,−8.2] / −11.3 [−15.2,−5.9] | −8.2 / −8.3 | h01 | no |
| 8 | Calendar case (current Csn20=C, U1C vs SVC, Truth-C, 2018-04..2021), FS, R5 | 90.4 / 72.8 / +17.6 [7.7, 22.2] | 79.6 / 71.4 / +8.2 [5.3, 10.7] | h02 | yes, exact |
| 9 | same, P5 | 87.6 / 66.6 / +21.0 [15.6, 30.1] | 75.2 / 66.3 / +9.0 [2.9, 13.5] | h02 | yes, exact |
| 10 | S reference on the same 2018–21 months (S/U1/TS), FS, R5 / P5 gain | +15.2 / +22.6 | +8.6 / +12.6 | h02 | yes, exact |
| 11 | Loss when current = N20s instead of S (Truth-S), FS, R5 / P5 | +1.1 / −6.9 (both CIs include 0) | −11.7 [−16.4,−7.0] / −9.9 [−13.0,−4.9] | h02 | no |
| 12 | same against Truth-C, R5 | +3.0 | −0.7 [−5.7, 2.0] | h02 | no |
| 13 | Weakest gain: N20s/U1/Truth-S, FS, R5 / P5 | +15.4 / +16.3 | +2.7 [0.2, 4.7] / +6.5 [−0.0, 12.1] | h02 | no |
| 14 | After Suomi NPP: C2 vs U1, truth C vs full S, Mar 2023–Oct 2026, FS, R5: U1 / SV / gain | 86.5 / 66.3 / +20.2 [14.7, 26.0] (28 months) | 82.3 / 73.7 / +8.6 [6.1, 11.8] | h03 | yes, exact |
| 15 | same, P5 | 82.2 / 60.0 / +22.2 [17.5, 28.8] | 79.0 / 61.6 / +17.4 [13.5, 21.9] | h03 | yes, exact |
| 16 | same, all 44 months, R5 / P5 gain | +15.8 / +13.2 | +5.8 / +14.8 | h03 | yes, exact |
| 17 | C2 against full baseline (source effect only), all months, R5 / P5 | 97.7 / 95.5 | 91.1 / 91.9 | h03 | no |
| 18 | Real record, C 2012–25, FS labels differing mixed vs VIIRS-only, R5 | 35/98 = 35.7% (31 lower) | 37.0% (1,123–1,124 of 3,038) | h04 | yes |
| 19 | same, P5 | 29/98 = 29.6% (24 lower) | 34.2% (1,024 of 2,994) | h04 | yes, exact |
| 20 | Length-only permutation null, FS, R5 / P5 (p) | 21.4% (0.024–0.033) / 24.3% (0.18–0.19) | 21.1% (≤0.001) / 24.2% (0.025–0.027) | h04 | no |
| 21 | Real record level ÷1.6, labels changed, FS, R5 / P5 | 23 / 18 of 98 (diff +5.1, −4 to +13) | 16.1% / 14.0% (+2.1, −0.8 to +5.0) | h04 | no |
| 22 | Windows, labels differing, R5 / P5 | Apr–Oct 35/29 of 98; May–Sep 20/16 of 70; Jun–Sep 12/12 of 56 | 37.0/34.2%; 28.0/26.1%; 23.3/23.1% | h04 | yes |

## 2. Numbers reported by more than one topic

| Quantity | Topics | Values | Verdict |
|---|---|---|---|
| Check 1 (M 48,233, S 198,916, 0.2425) | h01, h02, h03, h04, x01 | identical | agree |
| Check 2, C box (629.5, 2,266.5, 4,751.1, 7,101.7, 690.0, 29,589.9) | h01 rev, h02, h03, h04, x01 | identical | agree |
| Check 3 R5: U1 84.4/79.7, SV 66.1/64.5 | all four, x01 | identical (h04 84.38/79.70) | agree |
| Check 3 P5: U1 86.2/79.8, SV 60.3/60.9 | h01, h02, x01 | identical | agree |
| C for 2026 Apr–Oct (77, 17, 115, 18,365, 29,590, 243, 757) | h03 §3.7, h04 §3.4 | identical | agree |
| f01's 41 of 105 (V01, 2012–26, box FS R5), 38 of 98 on 2012–25 | h04, round 4 f01 | identical (f01: 41, 39.0%, 38 lower/3 higher) | agree |
| V01 R5 2012–25 = 38; C R5 = 35 | h04 §3.6 vs §3.1 | differ by the series (C vs V01 changes 4–5 box labels, §3.7) | consistent |
| S-current reference: h01 box FS R5 84.4/gain 18.2 vs h02 87.6/gain 15.2 (P5 25.9 vs 22.6; 100 km 10.6 vs 8.6, 17.0 vs 12.6) | h01, h02 | different test months (2012–21 vs 2018-04..2021) | consistent: x01 reproduces both with one code by changing only the test months |
| Gain at k = 5: 18.2 (R5) / 25.9 (P5) in item 1 vs 17.1 / 24.9 in the k table | h01 §3.1 vs §3.3 | 202 standard splits vs all 252 splits | consistent; use 18.2/25.9 (standard set) |
| C against U1, box FS R5 86.5 (h03 §3.5, 35 months) vs C2 against U1 86.5 (§3.2, 28 months) | h03 | coincidence of two different samples | both recomputed exactly |
| 100 km R5 real-record differ counts: 1,123 / 608 / 405 / 1,785 (FS/MJJAS/JJAS/all) | h04 analyst vs h04 review (rounded) and x01 | 1,124 / 609 / 406 / 1,786 when C is rounded to 6 decimals | one circle-month sits on a ratio edge in float arithmetic; ±0.1 point; no conclusion moves |
| h04 box R5 interval 28–44 vs 28–43 | h04 report vs review summary | bootstrap seed | trivial |
| h02 box gain range "+15 to +23" | h02 summary | the table's lowest box FS gain is +14.4 (S/U1C/TC, R5) | wording; true range +14.4 to +22.6 |
| 50 km "no class" share: h01 P5 truth 41% uncertain vs h04 29.8% P5 uncertain | h01, h04 | 9-year hindcast baseline vs 22-year real baseline; ties at zero are rarer with more years | not a conflict |
| SV P5 uncertain at 100 km: h01 10.8% (2012–21) vs h02 7.5–9.6% (2018–21) | h01, h02 | different test months | not a conflict |

No number differs between topics in a way that one of them gets wrong. All differences trace to test months, split sets, seeds, or one float tie.

## 3. Spot checks (own code, `x01_crosscheck.py`)

Own daily cube from the parquet (`use`, local dates; M and S from SP rows), own 100 km circle membership, own C and C2 from `avail_cat_plus_partial` with the NOAA-20 2018-04-01..06-04 exception (C rounded to 6 decimals), own R5/P5 classifiers, 202 standard splits, year-block bootstrap (2,000 draws, seed 5).
- Checks 1–2: exact (C values to 0.1).
- **Rank-class gain, current S, box FS: P5 86.2 / 60.3, +25.9 [18.7, 33.9]; R5 +18.2 [13.8, 22.6].** 100 km P5 +17.0, R5 +10.6. All months and the May–Sep/Jun–Sep rows also match h01 to 0.1.
- **Rank-class gain, current month = combined series (h02 calendar case), box FS: P5 87.6 / 66.6, +21.0 [15.8, 30.1]; R5 90.4 / 72.8, +17.6 [8.0, 22.2].** 100 km P5 +9.0, R5 +8.2. Match.
- h02 S reference on 2018–21 (+15.2 R5, +22.6 P5 box): match, which shows that the h01/h02 difference is the test months.
- h03 real configuration (C2): every box and 100 km cell in §3.2/3.3 matches, including all four seasons; h03 §3.5 (C, 58 months) matches.
- h04: box FS 35/98 (31 lower) R5 and 29/98 (24 lower) P5; all windows and 100 km shares match (R5 ±1 circle-month, above).

## 4. Answers

**Q1. Rank classes: does the converted baseline still beat the short VIIRS-only one?** Yes. Box, FS, 2012–21: P5 +25.9 points [18.8, 33.8] against R5 +18.2 [13.8, 22.7]; all months P5 +18.9, R5 +15.2. 100 km: P5 +17.0 [13.1, 20.9], R5 +10.6 [8.3, 13.1], positive in all 31 circles under both; on rows every design can classify, +15.4 and +9.8. The P5 gain is larger, but part of that is probably the 4-value SV rank grid (not tested). Strength: strong for the sign; moderate for the P5-versus-R5 size.

**Q2. Longer VIIRS-only baseline.** The gain does not shrink steadily from 4 to 8 VIIRS years. Box FS R5 17.1 → 12.7 and P5 24.9 → 10.9 from k = 5 to k = 1, with P5 peaking at k = 4 (28.7, likely a rank-grid effect); 100 km R5 5.5–10.4, P5 9.0–22.7. Every interval stays above zero, but at k = 1 U1 and SV differ by one year. The range tested stops at 8 years against a 9-year truth, so the gain over a real 14-year VIIRS-only baseline is unknown. It cannot be read off this trend. Strength: weak.

**Q3. Which scheme is less sensitive to a level error?** Hindcast: neither clearly. At ×1.6 the box FS drop is R5 −13.2 and P5 −11.3; 100 km −8.2 and −8.3. The paired P5-minus-R5 contrast includes zero at every multiplier in the box and at 100 km, and at ×1.15 P5 drops more in the box (−4.8 vs −1.4). Real record: at ÷1.6, P5 changes 18 of 98 box FS labels against 23 for R5 (+5.1, −4 to +13), and in the circles 14.0% against 16.1% (+2.1, −0.8 to +5.0). Over all months the box is equal (41 vs 40), and the order reverses for ×1.25. At most, rank classes are slightly less sensitive. Strength: weak.

**Q4. Current month from NOAA-20 or the combined series.** Box: no clear loss (R5 N20s −S +1.1, Csn20 −S +2.2; P5 −6.9 and −1.2, all CIs include 0; the P5 N20s loss is 2018 and is −0.6 without it). 100 km, against Suomi NPP's own label: N20s −11.7 (R5) and −9.9 (P5); combined −6.1 and −5.1. This is an upper bound, because against Truth-C the N20s loss is −0.7 (−5.7 to +2.0). The loss is satellite-to-satellite scatter, not scale (factor 1.0 / 1.0245 / oracle within 1.6 points). The converted baseline still beats its matching benchmark in every box and 100 km FS case. Calendar case: box +17.6 (R5) and +21.0 (P5); 100 km +8.2 and +9.0. The weakest case is N20s against Truth-S at 100 km, +2.7 R5 (+0.2 to +4.7) and +6.5 P5 (−0.0 to +12.1), and without 2018 its interval includes zero. Strength: moderate at 100 km, weak on the box (26 months, 4 test years).

**Q5. Configuration after Suomi NPP (C2 against the mixed baseline).** Box, Mar 2023–Oct 2026, the label agrees with the full-record label in 86.5% of 28 Apr–Oct months (R5) and 82.2% (P5). Over all 44 months it agrees in 78.1% and 72.0%, and within one class in 99.5% and 99.8% (FS). The 5-year SV benchmark gets 66.3% and 60.0% (FS), a gain of +20.2 [14.7, 26.0] (R5) and +22.2 [17.5, 28.8] (P5). The all-months gain is +15.8 and +13.2. At 100 km: 82.3% vs 73.7% (+8.6) and 79.0% vs 61.6% (+17.4). The source alone costs little: C2 against the full baseline is 97.7% / 95.5% (box, all months), and C2/C summed is 1.001. Per split, 0–7% of box splits have a negative gain, and the 5–95% range is +7 to +36 (R5 FS) and 0 to +39 (P5 FS). Strength: moderate for direction. The size is relative to a 5-year benchmark, not the real 14-year option.

**Q6. Real record, labels that differ between mixed and VIIRS-only baselines.** Box FS (C, 2012–25): R5 35 of 98 (35.7%; 31 lower), P5 29 of 98 (29.6%; 24 lower). 100 km: 37.0% and 34.2%. Excess over the length-only null: R5 +14 points in the box (p 0.024–0.033) and +16 at 100 km (p ≤ 0.001). P5 +5 in the box (p 0.18–0.19, not distinguishable from length alone) and +10 at 100 km (p 0.025–0.027). By calendar month, the changes are in spring and autumn and are nearly all downward. Box R5 (of 14 years): Oct 9, May 8, Nov 8, Apr 6, Jun 6, Mar 5, all lower; Dec 10 and Jul 4, all higher. Box P5: Apr 8, Nov 8, Mar 5, Jun 5, Oct 5, May 4, all lower; Jul 3, Aug 2, Dec 3, all higher. At 100 km the most-changed months are Apr, Oct, Nov and Mar. Jul, Aug and Dec change least or in the other direction. Strength: strong for the counts, moderate for the excess (it is real for R5 and for circles, and weak or absent for box P5), and its cause (real pre-2012 burning or a high conversion level) is unknown.

**Q7. Apr–Oct, May–Sep or Jun–Sep.** Real record, box labels that differ from VIIRS-only: R5 35/98 → 20/70 → 12/56; P5 29/98 → 16/70 → 12/56. At 100 km: R5 37.0 → 28.0 → 23.3%, P5 34.2 → 26.1 → 23.1%. In Jun–Sep the two schemes change the same number of labels. Hindcast (h01, box): the converted-baseline gain holds in every window. R5 +18.2 / +15.0 / +16.5 and P5 +25.9 / +29.3 / +30.3. Calendar case (h02, box): R5 +17.6 / +13.2 / +14.0 and P5 +21.0 / +25.5 / +27.9, on 26, 18 and 14 distinct months. C2 (h03, box): R5 +20.2 / +17.2 / +16.7 and P5 +22.2 / +21.9 / +23.9. So the narrower windows remove most of the real-record disagreement (April, May and October) without losing the hindcast gain. The narrow windows have few months, with box P5 Jun–Sep intervals as wide as +8.7 to +39.0. Jun–Sep is also the easy case for R5: 70% of 2022–26 box months are in the top class. Strength: moderate.

**Q8. Untested or too weak.** (a) The gain over a real 14-year VIIRS-only baseline: every benchmark has 4–8 years. (b) Whether a disagreement on the real record is a conversion error or real pre-2012 fire. (c) A truth independent of both Suomi NPP and NOAA-20 in 2018–21, so it is unknown whether C gives a *truer* label. (d) Year-block intervals rest on 10 years (h01), 4 years (h02, h03; only 35 distinct resamples) or 14 years (h04). They do not resample baseline years or include the split spread, so they are too narrow. (e) Scheme comparisons of level sensitivity: no contrast interval excludes zero. (f) The "structural" share of the larger P5 gain (the 4-value rank grid) has not been tested. (g) Results at 50 km: a third to two-fifths of months get no class under either scheme. h03 did not run 50 or 150 km, and 25 km was not run anywhere. (h) The N20/N21 scale factors were fitted on data that include the test months. (i) Box P5 real-record excess (p ≈ 0.19) is a weak negative with 14 years.

## 5. Files
- `scripts/x01_crosscheck.py`: own rebuild and recompute of items A (h01), B (h02 calendar case and S reference), C (h03 C2 and C), D (h04 label differences).
- `out/x01_results.csv`: every recomputed cell (agreement, gain, interval, n; label-difference counts).
- `out/x01_log.txt`: run log, including checks 1–2.
