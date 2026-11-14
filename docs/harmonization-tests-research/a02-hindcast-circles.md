# Does a converted MODIS-era record give the right calendar class? User-sized areas

## Answer

On the fire-season months where a class can be computed by both, a baseline that mixes scaled-up MODIS years with Suomi NPP years (design U1) matches the true class more often than a short Suomi NPP-only baseline (SV) at every radius. The gain is about 12 points of exact agreement at 25 and 50 km, 10 at 100 km and 20 at 150 km. U1 refuses more months than SV below 100 km, so it also matters how refusals are counted. If a refusal counts as a miss, SV is ahead at 25 km by 3 points. U1 is ahead from 50 km on exact class (by 3 points) and from 100 km on coarse class. Random thinning (DR) does not remove any bias that U1 has: it agrees less often, classes fewer months, and leans further toward "below normal". Shrinking a circle toward the whole box (SH) lowers agreement at every radius. In this test it cannot do otherwise, for a reason explained below. At 25 km only 22% of fire-season circle-months have any definable class, and MODIS reads zero in 40% of the months in which Suomi NPP saw fire.

## Evidence

**Data used.** Standard rows with `use == True`, keyed by the local-date month. The period is the ten stable-orbit years 2012–2021, April–October only. The circles are the 31 per radius in `circles.csv`. Both factors are fitted on the whole box: the MODIS factor (Terra + Aqua divided by Suomi NPP, a ratio of sums) and the Suomi NPP reference. The check numbers reproduce: 48,233 MODIS and 198,916 Suomi NPP hotspots, ratio 0.2425 (0.343 by day, 0.177 at night), 116 months.

**How months were handled.** August and September 2020 (the Aqua outage) are removed for all sensors. That drops 62 of 2,170 circle-months per radius and leaves 2,108. February 2016 lies outside the fire season. Zero months are kept as valid counts, both in baselines and as months to classify. They are 67% of the evaluated circle-months at 25 km, 37% at 50 km, 8% at 100 km and 2% at 150 km. A month is **not classifiable** when its baseline median is below 1. Such months are reported, not dropped.

**Protocol B** is the mixed-era baseline test. Each split uses five years as a pretend MODIS era and five as a VIIRS era. The truth is the class of each VIIRS-era month against the Suomi NPP median of the other nine years. Results pool 200 random splits. Intervals are 95% year-block bootstraps over the ten evaluated years. Coverage-adjusted results count a design's refusal as a miss among months that have a truth.

| Radius | Months with a truth | U1 classes | SV classes | DR classes | U1 exact* | SV exact* | U1 − SV, same months | U1 − SV, coverage-adjusted exact | U1 − SV, coverage-adjusted coarse |
|---|---|---|---|---|---|---|---|---|---|
| 25 km | 22% | 17% | 29% | 13% | 0.85 | 0.75 | +0.12 (0.11 to 0.13) | −0.03 (−0.035 to −0.024) | −0.05 (−0.07 to −0.04) |
| 50 km | 67% | 55% | 66% | 39% | 0.82 | 0.71 | +0.11 (0.09 to 0.13) | +0.03 (0.01 to 0.04) | +0.01 (−0.01 to 0.02) |
| 100 km | 100% | 99.9% | 98% | 97% | 0.77 | 0.68 | +0.10 (0.07 to 0.12) | +0.11 (0.08 to 0.13) | +0.08 (0.06 to 0.11) |
| 150 km | 100% | 100% | 100% | 100% | 0.87 | 0.67 | +0.20 (0.15 to 0.25) | +0.20 (0.15 to 0.25) | +0.13 (0.08 to 0.16) |

\*Exact agreement among months where the truth and that design both give a class. "Same months" means months where the truth, U1 and SV all give a class: 31,900 pooled split-months at 25 km, 103,500 at 50 km, 207,000 at 100 km and 211,000 at 150 km. The paired differences resample years. Conditional agreement is higher at 25 km than at 100 km only because few, clear-cut months are classifiable at 25 km. Compare radii on the coverage-adjusted columns.

**Bias in labelled shares.** These are among months classed by both the truth and the design. Each entry is the design's share minus the truth's share, in percentage points.

| Radius | U1 above | U1 below | DR above | DR below | SV above | SV below | SH above | SH below |
|---|---|---|---|---|---|---|---|---|
| 25 km | −0.2 (−1.4, 1.1) | +0.1 (−1.7, 2.0) | −1.3 (−3.0, 0.8) | +1.3 (−1.4, 4.4) | −3.3 | +3.2 | −0.8 | −0.1 |
| 50 km | −1.7 (−3.4, −0.3) | +2.0 (1.2, 2.9) | −4.8 (−6.7, −2.8) | +3.9 (2.6, 5.4) | −3.6 | +5.3 | −3.6 | +2.4 |
| 100 km | −3.2 | +3.1 | −3.0 | +3.7 | −3.7 | +3.7 | −3.8 | +3.2 |

Overall, the feared direction does not appear. Zeros in the MODIS era were expected to make VIIRS months read above normal, but U1 reads slightly too few months as above normal. The bias does appear where it should, though at a small size. Take months whose truth median is 1 to 3 hotspots and whose baseline holds three or more zero MODIS-era years. There, U1 labels 2.1 points too many above normal at 25 km (−0.8 to 5.7, 17,900 split-months) and 3.0 at 50 km (1.1 to 5.1, 44,400). In those months the U1 median is below the truth median 76% and 69% of the time. Elsewhere it is masked, because scaling a single MODIS hotspot by about 4 raises other medians. The not-classifiable rule also hides it: U1 classes only 33% and 43% of these months.

**Months the truth cannot judge.** At 25 km, 35% of SV's labels (21,600 split-months) and 7% of U1's (2,400) fall in months whose nine-year Suomi NPP median is below 1. At 50 km the figures are 12% (16,100) and 5% (5,900). Both designs call most of these months below normal (SV 77%, U1 74% at 25 km).

**MODIS zero when Suomi NPP saw fire.** This uses the ten stable years, April–October, and 31 circles per radius.

| Radius | Suomi NPP ≥ 1 | MODIS = 0 | Suomi NPP ≥ 10 | MODIS = 0 |
|---|---|---|---|---|
| 25 km | 699 months | 40.5% (34–49) | 303 | 4.3% (3.0–6.9) |
| 50 km | 1,326 | 31.7% (27–37) | 657 | 2.1% (0.8–4.0) |
| 100 km | 1,944 | 14.9% (10–19) | 1,270 | 3.1% (0.9–5.9) |
| 150 km | 2,077 | 4.2% (0.9–7.9) | 1,738 | 0.3% (0.0–1.1) |

**Protocol A** is the single-month conversion, leaving one year out. For U1, exact agreement among truth-classifiable months is 0.74 (0.71–0.78, 472 months) at 25 km and 0.63 (0.59–0.66, 1,404 months) at 50 km. The median absolute percentage error, for months with at least 10 Suomi NPP hotspots, is 0.37 (0.31–0.52, 303 months) at 25 km and 0.34 at 50 km. The draft reported 0.48 and 0.36. Its figures also required the baseline median to be at least 1.

**DR and SH details.** The beta-binomial version of DR behaves the same as the binomial one. The overdispersion fitted on the box is tiny (median ρ = 0.0018), and a box fit cannot represent clumping within a circle. SH's weight is w = v / (v + m / (n + 0.5)). It is fitted by regressing the squared log-anomaly difference between circle and box on 1 / (n + 0.5), with n the baseline median and the circle's Suomi NPP counts from other years. That gives v ≈ 2.6 at 25 km and 1.9 at 50 km. The noise term m hit its floor of 1 in most fits, so w ≈ 0.8. In Protocol B the month being classed is an actual Suomi NPP count, and the truth is defined on that same count. Any move toward the box therefore moves away from the truth, so this test cannot reward SH. In Protocol A, where the classed month carries conversion noise, SH also lost: 0.62 against 0.74 at 25 km. SH keeps U1's gate, so it adds no coverage.

## What this implies

- The team could claim the following. Wherever a converted MODIS-era baseline gives a class, it matches the long Suomi NPP record's class more often than a 2012-onward VIIRS-only baseline does, at every radius tested. Where both give a class, it is within one class about 96% of the time.
- The team could not claim that the converted baseline gives more correct labels for 25 km circles overall. Counting refusals, SV gets 3 points more right there. About a third of SV's 25 km labels, however, are for months that a full Suomi NPP record could not class at all.
- From 50 km, the converted baseline gives more correct exact labels even when refusals count as misses. From 100 km it does so on every measure.
- The feared above-normal bias is small. It is confined to quiet months with mostly-zero MODIS years. The not-classifiable rule (median at least 1) is what keeps it small, so a statement about bias holds only together with that rule.
- Neither thinning (DR) nor this form of shrinkage (SH) has evidence in its favour here.
- At 25 km, any design leaves most fire-season months (78% or more) without a defensible monthly class. How to present those months is a display choice that this test does not score.

## Limits

- The ten stable years stand in for 2000–2011. Terra-only years (2000–2002) and drift-period MODIS are not tested.
- Intervals rest on ten years and are dominated by 2017, 2018 and 2021.
- The two chronological splits have no interval. On them U1 still beats SV at every radius on shared months.
- The truth is itself a nine-year Suomi NPP median with its own sampling noise at small counts. It is not ground truth about fire.
- Only April–October months were evaluated.
- SH was tested in one form only. A design that shrinks the baseline median, or that relaxes the gate, is untested.
- The fallbacks for small areas (an enclosing region, a season instead of a month, presence or absence) were not scored.

## How it was computed

- The analyst's scripts were re-run from a clean start and their outputs were identical: `a02_cube.py` (counts), `a02_run.py` (both protocols), `a02_summ.py`, `a02_extra.py` and `a02_zero.py`.
- The reviewer's independent script is `scripts/a02-hindcast-circles_review.py`. It rebuilds the counts, draws its own 200 random splits with `default_rng(1)` and `choice`, and runs U1, SV, DR (100 draws), SH and Protocol A. It also adds the paired coverage-adjusted differences, the low-median zero-year bias, a factor fitted without the evaluated year, and an analysis of months the truth cannot class.
- Outputs are in `out/a02-hindcast-circles_review_*.csv` and `out/a02-hindcast-circles_review_B_records.parquet`.
- The reviewer's figures match the analyst's to within 0.01. Refitting the factor without the evaluated year changes U1 by less than 0.003.
