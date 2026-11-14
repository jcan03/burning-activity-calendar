# Round 3 cross-check

This file compares the twelve analysis files (a01–a12) and three source and data files (w01–w03) from round 3 with each other and with `docs/harmonization-evidence.md`. It reconciles numbers that differ, sets conclusions that conflict against each other, answers the open questions, and says what the tests show about each piece of the provisional pipeline. It does not choose a method.

**Basis.** Every file reports reproducing the SPEC check numbers. The cross-check reproduced them too: MODIS 48,233, Suomi NPP 198,916, ratio 0.2425 (0.343 by day, 0.177 at night), 116 stable months, `use == True`, standard rows, local-date months. Three quantities were recomputed in `scripts/crosscheck_r3.py`, which runs in about one second. Its output is `out/crosscheck_r3.csv`. Intervals there come from 1,000 resamples of whole years.

## Reconciled numbers

| Quantity | Values in the files | Why they differ | Value to use |
|---|---|---|---|
| **Beta-binomial overdispersion ρ of MODIS given Suomi NPP, box** | a01: 0.060 (range 0.028–0.090 across splits, maximum likelihood on the 5 VIIRS-era years of each split). a03: 0.062 (0.039–0.083), maximum likelihood, 115 months. a02: median **0.0018**, "fitted on the box". | **An estimator artefact in a02.** a02 (`a02_run.py`, lines 107–110) uses a moment estimator weighted by (N−1)². Recomputed on the 116 stable months, 98.4% of that weight falls on the 5 largest months. The recomputed values are: maximum likelihood **0.061 (0.036–0.085)**; a02's weighted moment estimator **0.0017 (0.0010–0.011)**; an unweighted median of the moment estimates over months with N ≥ 10, **0.020 (0.014–0.035)**. Fire-season values are the same to within 0.002. One constant ρ does not fit: relative scatter is smaller in big months than a constant ρ implies, so each estimator answers a different question. | **About 0.06 for the box** (maximum likelihood), which means the kept share varies by about ±43% (SD) from month to month, as a03 states. At ρ = 0.0018 it would vary by about ±7.5%. For circles, a03 measured 0.07–0.13. a02's beta-binomial DR results use the 0.0018 value and should not be read as a test of overdispersion. |
| **Suomi NPP / NOAA-20, fire season 2024** | a04: 0.88 (9 months), the low point of its yearly series. a10: NOAA-20 / Suomi NPP 1.14 in 2024. | **Gaps missing from the outage list.** w03 found no Suomi NPP granules on 30 May – 3 June, 10–15 July and 24–28 July 2024. Recomputed (fire season, listed outage months dropped): 0.881 with every day kept, **0.985** after dropping the 10 UTC days with no granule for either satellite. No other year 2018–2025 moves by more than 0.001. | **About 0.99 in 2024.** The yearly Suomi NPP / NOAA-20 series is then 0.93–1.08 over 2018–2025, without 2024 as an outlier. a04's trend (−0.7% a year) and its March 2023 step test included the 2024 dip, so the true stability is, if anything, better than a04 states. |
| **Terra daytime level in the drift years, 2022 to 2026** | Evidence (m04): 0.95, 0.81, 0.77, 0.70, 0.46. a09: 0.91, 0.87, 0.81, 0.71, **0.50 (0.41–0.61)**. a09 against NOAA-20: 2026 0.49 (0.44–0.51). a06: 2026 0.50 (0.35–0.55) of the 2018–2021 ratio against NOAA-20. a10: 0.07 against 0.140. w03: Terra's daytime hotspots per hectare burned in 2026 are 0.41–0.45 of their 2021 and 2023 values; NOAA-20's are 0.74–0.93. | **Reference and size model.** m04 and a09 divide by an expected count from a size model fitted on 2012–2021, with different VIIRS references (a09 uses Suomi NPP, and NOAA-20 × k where Suomi NPP is masked). a06 and a10 use the raw ratio to NOAA-20. Recomputed raw fire-season Terra-day / NOAA-20-day ratios (including the near-real-time rows of 2026), relative to the pooled 2018–2021 value of 0.138: **1.07, 1.05, 0.95, 0.98 and 0.51**. The years 2018–2021 alone span 0.92–1.53 on this scale. | **2026: about 0.5 of normal** (0.41–0.61 across five methods, all independent of one another except in the reference years). **2022–2025: no decline in the raw ratio.** The gradual decline exists only after the size adjustment, which a09 says fits small years poorly (stable small years 0.6–1.6). |
| **Published daily-curve correction, over-correction of Terra by day in 2025–2026** | Methods document: 21–25%. a09: 26% and 37% (measured ÷ predicted 1.26 and 1.37, prediction intervals 0.59–2.45 and 0.92–1.97). | Different size model and VIIRS reference. | a09's values are the newer computation. Either way the published curve over-corrects, and the size of the over-correction is uncertain within roughly a factor of 2. |
| **Single-month error of one factor, fire season, whole box** | a01: 0.33 (0.26–0.38), MODIS converted to VIIRS, 67 months. a07: 0.31, VIIRS converted to MODIS, 67 months. a08: 0.30 (0.22–0.46), Aqua only, 68 months. a10: 32%. Evidence: about 30%. | The direction of conversion changes a percentage error, as do the sensor set and the treatment of zero months. | **About 30–33% median absolute error.** No conflict. |
| **How far one factor runs high in quiet or typical months** | a04: converted calendar-month medians 1.23 times actual (0.98–1.59). a10: geometric-mean ratio 1.15 (1.03–1.28) over 68 months. a05: +27% for the six smaller seasons of 2012–2021 (yearly totals). a03: fire-season ratio of sums 0.38 for the quietest third of months against 0.24 for the busiest. a08 (Aqua): median signed error +8% in months under 200 Suomi NPP hotspots. | Different statistics: a median of medians, a geometric mean of month pairs, yearly totals and ratios of sums by size class. | **They agree in direction: converted quiet months and quiet years run about 15–27% high.** The intervals overlap. Use 15% for a typical month, 23% for a calendar-month median and 27% for a small season, each with its source stated. |
| **Day and night split against one factor, single-month error, fire season** | a01 (U2): 0.28 against 0.33. a08 (Aqua): 0.26 against 0.30. a10: 27% against 32%. | Same pattern in three independent computations. | **About 4–5 points lower with the split. Every interval overlaps**, so it is not established. Over all months the split is worse for classes (a01: −6.9 points, −10.1 to −3.8). |
| **2 km cell-day ratio, MODIS to Suomi NPP** | Evidence: 0.65 (0.68 by day). a01: 0.668 (daytime). a07: 0.654 (union definition, 68 fire-season months), 0.69 (each sensor and pass separately, 116 months), 0.74 (same, fire season). | Definitions: the union of Terra and Aqua versus each sensor and pass counted separately. a07 reconciles them. | Quote the definition with the number. |
| **Same five-class label from each sensor's own history** | Evidence: 71%. a11: 68% (59–76), 68 months; 75% (67–83) with baseline median ≥ 10. a01 Protocol A: 69% (61–77). | a11: the earlier 71% included the month's own year in its baseline and used UTC months. | **About 68–69%** on the round-3 definitions. |
| **Range of the fire-season ratio across years** | Evidence: 0.19–0.40. a05: 0.23–0.41. a07: 0.199–0.408. a10: 0.20–0.41. | a05 drops 2020, the Aqua outage year. | 0.20–0.41 with 2020 kept. |
| **Months where MODIS is zero although Suomi NPP saw fire** | Evidence (median over circles): 36%, 33%, 16% and 6% at 25, 50, 100 and 150 km. a02 (pooled over circles): 40.5%, 31.7%, 14.9% and 4.2%. a03 conditions the other way: among months with MODIS zero, 40% (50 km) and 70% (100 km) had Suomi NPP hotspots. | Median over circles against pooled months; different conditioning in a03. | No conflict. |
| **Scale factor from NOAA-20 to Suomi NPP** | Evidence 1.011; a04 1.013; a05 0.995 (used to fill the 2022 gap); a09 1.034 by day and 1.001 at night. | Different windows and day/night splits. | All lie within ±3%. a09 notes that a few percent shifts every 2026 level by the same amount. |
| **Terra-day / NOAA-20 baseline 2018–2021** | a06: 0.138 (fire season). a10: 0.140 (all months). | Months included. | Recomputed: 0.138 (fire season). |
| **Night ratio in quiet months** | a12: about 0.08 (0.059–0.093), whichever way months are selected. a01: 0.03–0.12 in March–May and September–December, against 0.18–0.19 in July–August. | Consistent. | The night factor is seasonal; the pooled 0.177 applies only to summer. |
| **Rule behind the near-real-time day and night label** | SPEC and evidence: by orbit direction. a06: every near-real-time label equals the 85° sun-angle rule. | No near-real-time row lies between 83.6° and 96.5°, where the rules would disagree. | **Unresolved by this file.** The data are consistent with either statement. |
| **Decade trend in the factor, 2012–2016 against 2017–2021** | a04: all hours −2.9% a year (p 0.07); day −3.2% (p 0.05); day with size control −5.1% (−8.9 to −0.2). At a fixed day/night mix, 0.243 against 0.240. a10: weighting months equally, −0.10 in logs (p 0.26); with size control −0.15 (p 0.16). | a04's all-hours fall is a change in the day/night mix. a10 tests all hours with months weighted equally; a04's significant result is for daytime only. | The all-hours factor shows no trend at a fixed mix. A daytime decline is borderline. Neither file establishes a trend. |

## Conflicting conclusions

1. **Does overdispersion matter for random thinning?** a02 says the beta-binomial DR "behaves the same as the binomial one". a01 says it loses 9 points in the fire season (−11.4 to −6.0) and 12 over all months. **a01 is better supported.** a02's ρ is about 35 times too small (see the first row above). Both files agree that DR does not beat U1, and more overdispersion would only widen that gap.

2. **Should conversion be split by day and night?**
   - *For the split:* a07 finds that 68% (58–92%) of the day-night gap for MODIS, and 84% for Aqua, is detection rather than pixel geometry. a11 finds that day and night behave as separate dimensions. a08 and a10 find single-month errors 4–5 points lower in the fire season. a10 finds the split removes the typical-month bias (1.15 becomes 1.00). a04 finds that the 2003–2011 day/night mix would make a single factor give a 7.7% higher total than a split would.
   - *Against the split:* a01 finds it 6.9 points worse over all months, because a pooled night factor of 0.177 is wrong outside summer (0.03–0.12). a04 finds that the day factor fell 23% and the night factor rose 46% between the two halves of the decade. a10 finds the split puts the total 5% high. a07 finds that fitting day and night separately made every cell model worse.
   - **Better supported:** the mechanism is real, and the gain within the fire season is small and not significant. A split with one pooled night factor is measurably worse outside the fire season. No file tested a split with a seasonal night factor.

3. **Did Terra decline gradually in 2022–2025?** The evidence file rates this "moderate". a10's CUSUM chart signals in 2025-09, and all but two Terra-daytime z-scores in 2022–2025 are negative. Against that: a09's 2022–2025 Terra contrast (0.87) equals its own placebo (0.87); the recomputed raw ratios to NOAA-20 are 1.07, 1.05, 0.95 and 0.98 of the 2018–2021 level; and a06 places 2024 and 2025 inside the 2018–2025 range. **Better supported:** only 2026 is established. The gradual decline depends on the size model and on month-level weighting, so it is weak evidence.

4. **Correct the drift, or only flag it?** a09 says a Gaussian curve peaking at 13.4 h corrects Terra by day (2025: 1.03; 2026: 0.97, measured ÷ predicted) and beat a plain trend in year on the held-out 2026 (0.97 against 0.70). The methods document and the literature (Giglio and Roy 2024) favour flagging. a09 itself calls the validation thin: one decisive year, prediction interval 0.69–1.72 for 2026, and no support for any other pass. **Both stand, for different series.** A Terra-daytime correction can remove the 2026 bias in a point estimate, but it does not restore single-year precision (−30% to +70%). For the other three passes the data support flagging only.

5. **Where does the monthly scatter come from?** w01 says "most of the scatter therefore comes from sampling: overpass timing, cloud cover and clustered fires". That rests on binomial arithmetic only, not on a fitted model. a03 says "in the box, most of the disagreement is change in the true ratio". Its clustered thinning explains 40% (29–61) over all months but 64% (43–101) in fire-season months. **a03 is better supported for all months. For fire-season box months the split is undetermined**, since the interval reaches 100%. a10 gives an independent lower bound: two VIIRS satellites scatter with a log-difference SD of 0.22, against 0.52 for converted MODIS, so about 18% of the variance (20% in months of 1,000 or more hotspots) is the floor between two identical instruments.

6. **How much does the small-season bias matter for labels?** a05 says the factor overstates small seasons by about 27% and that this "tilt[s] current quiet months toward below normal". a01 finds the U1 bias in labelled shares small (above −2.9 points, below +0.9) and finds that a factor 25% higher does not improve labels (−0.001, −0.040 to +0.035). a02 finds the below-normal share 2.0 points too high at 50 km and 3.1 at 100 km. **Both stand.** The bias is real in level but small in classes on the stable test years. Seven of the nine pre-2012 seasons are small, against six of ten in the test, so the stable-period hindcasts may understate the bias for the real pre-2012 baseline. That is untested.

7. **Can an enclosing region help small areas?** P5 and the methods catalogue (X2) propose regional context. a02's shrinkage (SH) lost at every radius, but a02 shows that its Protocol B cannot reward any move toward the box: the truth is defined on the very count being classed. In Protocol A it also lost (0.62 against 0.74 at 25 km). **Not settled.** The test cannot score regional context as a display aid.

8. **Is the outage list reliable enough to mask months?** a04, a09 and a10 mask months from `outages.csv`. w03 shows that list misses Suomi NPP gaps in May–July 2024, Terra gaps in March 2026 and May 2025, and NOAA-21 gaps in January 2026. It also lists a Suomi NPP gap through 20 August 2022 although data exist on 11–20 August. **w03 is better supported** (granule catalogue). The only result it was shown to move is the 2024 Suomi NPP / NOAA-20 ratio (row 2 above). The 2022 Suomi NPP masks in a09 and a10 discard some valid days but do not bias the ratios.

9. **Near-real-time day and night labels.** SPEC says near-real-time rows are labelled by orbit direction; a06 finds them identical to the sun-angle rule. Both are consistent with the data, because no near-real-time row falls in the zenith range where the rules disagree.

10. **Do the HMM states or coarse classes "agree better"?** a11 shows that the HMM's 90% agreement equals that of own-history classes cut into the same number and shares of groups (91%). The same mechanism applies to P4's coarse classes. a01's coarse agreement (92.5%) beats its exact agreement (84%) partly because there are fewer categories. **Agreement rates across schemes with different numbers of classes are not comparable.** Compare kappa, or schemes with the same number of classes.

## Answers to the open questions

**(a) Does a converted MODIS-era record give the right calendar class, and does it beat a short VIIRS-only baseline?**
At box scale, yes, on the ten stable years:
- U1 matches the all-Suomi NPP class in 84% of fire-season months (SD across splits 5 points, kappa 0.79). It matches in 80% of all months and is within one class in 98%.
- SV, the short VIIRS-only baseline, gets 66% and 65%.
- The gain is +18 points (14 to 23) in the fire season and +15 (10 to 20) over all months. U1 wins in 94–95% of 202 splits (a01).

In circles (a02), on months both designs can class, U1 beats SV by 12 points at 25 km, 11 at 50 km, 10 at 100 km and 20 at 150 km. Counting a refusal as a miss, SV leads by 3 points at 25 km (−0.035 to −0.024). U1 leads by 3 at 50 km on exact class, and on every measure from 100 km.

Strength: moderate. The evidence is ten years, dominated by 2017, 2018 and 2021, and the split SD understates uncertainty. The truth is a nine-year Suomi NPP median, not fire. Single-month conversion (Protocol A) is weaker: 69% (61–77) class agreement and 33% error in the fire season.

**(b) Does the direction of conversion matter, and does thinning fix the zero problem?**
- Converting VIIRS down by expectation (DE) and MODIS up (U1) give the same label in 11,705 of 11,706 cases (a01). Direction does not matter at box scale.
- Random thinning is no better: −2 points with a binomial draw (−4.6 to +0.2) and −9 to −12 points with a beta-binomial draw (a01).
- In circles, DR classes fewer months than U1 (13% against 17% at 25 km; 39% against 55% at 50 km), agrees less often, and leans further toward below normal (a02).
- **Thinning does not fix the zero problem.** It moves VIIRS onto MODIS's sparse scale, so the baseline medians that were zero stay zero.
- a03 quantifies what a MODIS-era zero means: up to 6 Suomi NPP hotspots at 50 km and 17 at 100 km (90th percentile over all months; 4 and 9 in the fire season), held out at 92% and 90% coverage.
- w01 adds that thinning is sound as an expected-value statement only, and that the downward direction is interpolation while the upward one extrapolates about 4.1-fold.

Strength: strong for "no difference by expectation", moderate for "random thinning is worse".

**(c) What is the smallest area at which converted history can be shown?**
On a02's scoring:
- 25 km: converted history loses to a VIIRS-only baseline when refusals count. Only 22% of fire-season circle-months have any defensible class.
- 50 km: grey zone. Exact class +3 points (1 to 4); coarse class +1 (−1 to +2), not significant.
- 100 km and above: converted history wins on every measure (+11 exact, +8 coarse).

So **about 100 km is where the tests support it without qualification, and 50 km is borderline.** This agrees with the evidence file ("marginal at 50 km, usable from about 100 km"). The bias toward above normal that MODIS zeros were expected to cause is small (+2.1 points at 25 km and +3.0 at 50 km in the affected months), and the rule "baseline median at least 1" is what keeps it small. Strength: moderate (31 overlapping circles, ten years).

**(d) How much of the monthly scatter is irreducible?**
Three estimates, from narrowest to widest:
1. Independent thinning of single hotspots: 15% of the variance in the box (10–25), 26% in the fire season.
2. The difference between two identical VIIRS satellites: about 18–20% (a10, recomputed from the SDs above).
3. Thinning whole 2 km fire-days: 40% in the box (29–61), 64% in the fire season (43–101), 47% at 100 km and 70% at 50 km (a03). a03 calls this grouping an over-correlated limit.

**About a fifth of the variance is irreducible by any factor, and up to half at circle scale.** The rest is month-to-month change in the true ratio, part of which depends on month size (a03 size slopes; a10). In plain terms: converted MODIS is within −40% to +70% of VIIRS in two months of three, against −20% to +25% for two VIIRS satellites (a10). Strength: moderate. The decomposition depends on the 2 km local-date grouping.

**(e) Is the factor stable in time, valid before 2012, and usable now that Suomi NPP has ended?**
- **Stable in time:** yes for the all-hours factor at a fixed day/night mix (0.243 against 0.240 in the two halves of the decade). No for the separate day and night factors (day −23%, night +46%) (a04). The double-mass curve is straight over 2012–2021 (a10).
- **Usable after Suomi NPP:** yes. The direct MODIS / NOAA-20 factor is 0.242 (0.234–0.269, 43 months), and NOAA-20 / Suomi NPP has no step or trend. The 2024 dip was outage days (row 2 above). The chain and the direct fit share their months, so they are not independent confirmation (a04).
- **Valid before 2012:**
  - Order is supported. Rank correlation with area burned is 0.88, and 84% of year pairs across the 2012 join are ordered correctly, against 89% within an era.
  - Level is not testable. BC's area-burned record can only detect a change of about twofold.
  - The factor overstates small seasons by about 27%, and 7 of the 9 pre-2012 seasons are small (a05).
  - Terra-only 2001–2002 fall at or below the 95% band of the 2003–2011 count-to-area line.

Strength: strong for continuity through NOAA-20; weak for the level before 2012.

**(f) Can the drift be corrected, or only flagged?**
- **Terra by day:** the data support a correction in 2026, with a fitted curve peaking at 13.4 h (12.7–13.8), not the published 14.57 h. But the 2026 prediction interval is 0.69–1.72, and the validation rests on one decisive year (a09).
- **Aqua by day, Aqua at night and Terra's evening pass:** flagging only. Aqua at night is 0.70 (0.60–0.82) in 2026 at a pass near dawn, which no daytime curve can model.
- **Detection:** only a Terra-daytime monitoring chart detected the loss (CUSUM 2025-09; EWMA and single-month 2026-07). An all-hours Terra+Aqua chart never signalled (a10).
- **Independent check:** w03's provisional BC 2026 burned area confirms the 2026 Terra-daytime loss (0.41–0.45 of 2021 and 2023 yields).

Strength: strong that 2026 Terra daytime is about half; weak that any correction is accurate for a single year.

**(g) What should the day and night rule be?**
- The 85° sun-angle rule reproduces every delivered label, standard and near-real-time, on all five sensors (737,244 rows). A pass-based rule (local solar hour 06:00–18:00) differs on 10 rows, all from one Terra pass on 24 July 2026 (a06).
- The choice changes no count in August–October 2026 and no July 2026 class.
- The rules will diverge in summer as the MODIS twilight passes approach 85°. Terra's evening pass and Aqua's dawn pass already have 39% of July 2026 rows under 90°. The sun-angle rule would then move parts of those passes into the day series; a pass rule keeps each pass whole.
- Neither rule makes MODIS's night series comparable to VIIRS's 02:10 pass.

Strength: strong for the current data; untested for 2027.

**(h) Which cross-field approaches earned a place, which did not, and why?**

| Approach | Verdict | Reason |
|---|---|---|
| Thinning as expectation (DE) | Earned, as an explanation | Identical to U1 by construction and in practice. It frames the MODIS-equivalent view and the "zero means up to N" table (a01, a03, w01). |
| Beta-binomial zero table and inverse | Partly earned | The zero table holds on held-out years (90–92%). Inverse intervals under-cover (72–79% for nominal 90%) (a03). |
| Random thinning (DR), binomial or beta-binomial | Not earned | Worse than U1, classes fewer months (a01, a02). |
| Control charts (CUSUM, EWMA) | Earned, as a monitor | The only method that flagged Terra's daytime loss early. One SD of 0.14 rests on 9 months, so a NOAA-21 monitor detects only large shifts (a10, w02). |
| Double-mass curve | Earned, as a picture | Straight in the stable years; the bend shows only for Terra by day. The USGS 5-year rule would ignore a one-year break (a10, w02). |
| Bland-Altman limits on logs | Earned, as a communication tool | It states plainly that converted MODIS is less than half as precise as a second VIIRS satellite. The limits should be stated with seasons as units: ±1.24 SD of uncertainty at n = 10 (w02). |
| Passing-Bablok, Lin's CCC | Not earned | The CCC is inflated by the range of counts, and Passing-Bablok is underpowered with about 10 seasons (a10, w02). |
| Conformal / CV+ intervals by size of month | Earned for months of about 10 or more predicted hotspots | Coverage 0.90–0.92 nominal, 0.72–0.86 with plain percentiles. Nothing honest below 10 (a04). Coverage varies with only 10 calibration seasons (w02). |
| Drift as a sampler of the daily cycle | Partly earned | Terra by day only. Its peak contradicts the published curve. The validation is thin (a09). |
| Box counting and the pixel/sensitivity decomposition | Earned as an explanation, not as a converter | It explains why the factor is about 4: about 2.6 pixels per cell × about 0.6. No cell-based link beat the plain ratio, and D is not a sensor property (a07). |
| Empirical detection curve; common FRP threshold | Not earned | The curve is worse than one factor over all months (+0.07, +0.01 to +0.19). A threshold steadies daytime cell ratios but discards half or more of VIIRS and does not cut single-month error (a08). |
| Rasch item-response model | Not earned | Rejected by fit (likelihood-ratio 2,493 on 42 df). It reproduces the cell-day ratios. Its useful by-product is evidence that day and night are separate dimensions (a11). |
| Hidden Markov states | Not earned | Its agreement equals that of coarse ratio classes with the same shares, and its states mean "ordinary, big, extreme", not relative to normal (a11). |
| Shrinkage toward the region (SH) | Untested in a fair form | Protocol B cannot reward it (a02). |
| Static-source screen | Earned, as a check | It confirms that Kamloops is the only persistent fixed source. Two weak sources stopped in 2016. Persistence masks would remove real burning (a12). |
| Granule-catalogue availability flag | Earned, as data | It found unlisted outages that bias a yearly ratio by 12% (w03; row 2 above). |

## What the tests say about each piece

**P1. VIIRS satellites combined as a daily mean of those with data, summed over the month.**
- *Supported:* round 2 (strong). w03 shows that the per-day flag the rule needs can be built from the open granule catalogue tonight. The recomputation shows why the flag matters: unlisted Suomi NPP gaps lowered its 2024 fire-season ratio to NOAA-20 from 0.985 to 0.881.
- *Undercut:* the catalogue cannot see partial losses (Aqua's 2020 failure looks normal). It keeps near-real-time granules for only about 7 days, so the current month may lack a flag.
- *Untested:* the rule at circle scale; its use as the "current month" in the a01/a02 hindcasts, which used Suomi NPP alone; the scale factors (1.011 for NOAA-20, 1.034 for NOAA-21) re-estimated with the flag applied.

**P2. One overlap factor split by day and night, fitted on the whole box over February 2012 to December 2021.**
- *Supported:*
  - Fitting on the whole box over the stable years: refitting without the classed year changes labels by ≤ 0.003 (a01, a02). Factor errors of ±20% change 0–5 points (a01) and 2 of 31 labels (a04).
  - The split has a mechanism (a07, a11) and slightly lower fire-season error (a01, a08, a10, not significant). It removes the typical-month bias (a10) and accounts for the 2003–2011 mix (a04, 7.7%).
- *Undercut:*
  - The pooled night factor of 0.177 is wrong outside summer (0.03–0.12), so U2 is 6.9 points worse than U1 over all months (a01).
  - The day and night factors moved −23% and +46% between halves of the decade (a04).
  - Any single factor runs 15–27% high in quiet months and small seasons (a03, a04, a05, a10).
- *Untested:* a split with a seasonal or fire-season-only night factor; a size-dependent factor scored in class terms.

**P3. MODIS only up to 2011, VIIRS alone from 2012, drift-period MODIS flagged, not corrected.**
- *Supported:*
  - VIIRS from 2012 avoids the drift entirely. The Terra-daytime loss in 2026 is about 0.5, confirmed by five methods and by BC area burned (a06, a09, a10, w03).
  - Flagging is what the data support for three of the four MODIS passes (a09).
  - Pre-2012 MODIS is internally stable: the Terra/Aqua trend is +0.2% a year (−0.4 to +1.0) (a05).
  - The rank order of converted pre-2012 years holds (a05).
- *Undercut:*
  - The level of pre-2012 history cannot be validated, and it is plausibly about 25% high for small seasons (a05).
  - Terra-only 2001–2002 sit low against area burned (a05).
  - a09 shows that Terra by day could be corrected, if the team wanted drift-period MODIS shown as data rather than flagged.
- *Untested:* how a baseline of about 24 years, including 2000–2011 converted years, performs as a whole. Every hindcast used 9–10 stable years.

**P4. Validation by holding out whole years; each converted month shown with an interval and coarse classes.**
- *Supported:*
  - Whole-year hold-outs are the right unit (w02; a10 limits). Random hold-outs understate error.
  - Size-binned CV+ intervals are honest for months of about 10 or more predicted hotspots (a04).
  - Coarse classes agree more often (a01: 92.5% against 84%).
- *Undercut:*
  - No interval tested is honest below about 10 predicted hotspots (a04).
  - Model-based beta-binomial intervals under-cover (a03).
  - With 10 calibration seasons, delivered coverage itself varies (SD about 0.11 at 80%; w02).
  - A single factor's error does not average across years, so a per-month interval omits a systematic component (a04, methods catalogue).
  - Coarse classes agree more partly just because there are fewer of them (a11).
- *Untested:* calibration of class probabilities; intervals at circle scale; intervals for the drift and Terra-only years.

**P5. Converted pre-2012 history only for areas of about 100 km radius or more; below that, VIIRS from 2012 with the enclosing region as context.**
- *Supported:* the 100 km cut is where converted history beats the VIIRS-only baseline on every measure (a02). At 25 km, VIIRS-only gets 3 points more right.
- *Undercut:*
  - At 50 km, converted history is already ahead on exact class (+3), so the cut is conservative rather than necessary.
  - About a third of SV's 25 km labels fall in months a full Suomi NPP record could not class (a02).
  - Near Kamloops, a VIIRS-only small-area record depends on removing the static site: 87% of quiet-summer counts within 25 km (a12).
- *Untested:* enclosing-region context as a display (a02's SH test could not reward it), and the other fallbacks (season instead of month, presence or absence).

**Alternative: comparisons with pre-2012 years made in MODIS-equivalent terms by thinning VIIRS counts.**
- *Supported:* by expectation it gives the same class as scaling up in all but 1 of 11,706 cases (a01). It is the interpolating direction (w01).
- *Undercut:*
  - Random thinning is worse (a01, a02).
  - It does not fix zeros, and it classes fewer small-area months (a02).
  - A thinned series cannot be presented as a simulation of MODIS, because random thinning reproduces only 15–26% of the box scatter (a03, w01).
- *Untested:* how users read MODIS-equivalent numbers. They differ from the counts the app shows for the current month by a factor of about 4.

## Still missing

1. **A hindcast with the real baseline length.** Every class test used 9–10 stable years. Nothing tested a baseline of about 24 years that includes converted 2003–2011, Terra-only 2000–2002 and drift-period years. The small-season bias (about +27%) may matter more there, because 7 of the 9 pre-2012 seasons are small.
2. **A day and night split with a seasonal night factor**, or a split applied only April–October. a01 identifies the cause of U2's loss; no file tested the fix.
3. **The current month from NOAA-20, or from the daily-mean rule (P1), in the hindcasts,** instead of Suomi NPP alone, and P1 at circle scale.
4. **Small-area displays scored fairly.** Regional context, a season instead of a month, and presence or absence need a test in which the truth is not defined on the classed count itself.
5. **Calibrated class probabilities**, and any honest interval for months under about 10 predicted hotspots.
6. **An independent daily fire cycle** (GOES-West, days of work per w03) to check a09's 13.4 h peak before any Terra correction is relied on.
7. **The granule-based availability flag applied throughout:** re-mask the outage months in a04, a09 and a10, and re-estimate the NOAA-20 and NOAA-21 scale factors. Partial losses and current-month near-real-time coverage stay unflagged.
8. **Final 2026 BC area burned**, to confirm w03's provisional Terra check (April 2027).
9. **How month size changes overdispersion and the factor**, modelled jointly rather than as one ρ and one f, and tested in class terms.
10. **NOAA-21 against MODIS directly.** There is still no stable-orbit overlap, only a chain through NOAA-20.
11. **Whether near-real-time and standard rows differ in anything other than the day and night label** for the current month: counts, `type`, and the static-site rows.
12. **Whether S137 and S133 should be removed** from 2012–2016 circles near them. The effect is small and local.
