# How does a baseline of the real length behave?

## Answer

On the ten stable-orbit years (2012–2021), a converted MODIS era made mostly of small seasons still reproduces the all-Suomi-NPP class well. Exact five-class agreement in the fire season is 0.865 (95% interval 0.82–0.90), against 0.711 for a VIIRS-only baseline. The converted baseline median runs 11% high (1.09–1.14), and the share of months labelled above or below normal is off by 3 points or less. On the real data, a 2003–2025 baseline with converted MODIS before 2012 gives a different label from a VIIRS-only 2012–2025 baseline in 41 of 105 fire-season months in the box (39%, 33–45). In 38 of those 41 the mixed baseline gives the lower class. If the years were interchangeable, changing the baseline length alone would alter about 22% of labels (95th percentile 34%). The excess over that, and its one-sided direction, are systematic (permutation p = 0.014 for the share, 0.006 for the direction). Without any conversion (MODIS counts only), the box shows no excess over the length effect (26.5% against 25.6%), while 100 km circles show a partial one. None of the remedies tested raises agreement by more than the spread across splits.

## Evidence

**Terms.** *Mixed baseline*: the median for the same calendar month over 2003–2011 converted MODIS (Terra plus Aqua divided by 0.2425) and 2012–2025 VIIRS, leaving out the month's own year. *VIIRS-only baseline*: 2012–2025 without the own year. The VIIRS value is Suomi NPP, with NOAA-20 × 1.011 used for its masked months and for all of 2026. *Above normal*: ratio to the median of at least 1.25. *Below normal*: under 0.8. *Large seasons*: 2017, 2018 and 2021. Intervals resample whole years (2,000 draws).

**Part 1. Composition (Protocol B, all 582 choices of 5, 4 or 3 pretend MODIS-era years; box; fire season).** L is the number of large seasons in the pretend MODIS era. No truth or design baseline had a median under 1.

| Group | splits | U1 exact | SV exact | U1 bias above | U1 bias below | U1 median ÷ truth median |
|---|---|---|---|---|---|---|
| k = 5, L = 0 | 21 | 0.874 (0.80–0.93) | 0.607 | −0.025 (−0.06, 0.01) | 0.000 | 1.156 (1.12–1.19) |
| k = 5, L = 1 | 105 | 0.848 | 0.683 | −0.030 | +0.009 | 1.138 |
| k = 5, L = 2 | 105 | 0.836 | 0.689 | −0.029 | +0.017 | 1.109 |
| k = 5, L = 3 | 21 | 0.835 (0.78–0.90) | 0.600 | −0.016 | +0.001 | 1.043 (1.02–1.07) |
| Mostly small (L/k ≤ 0.25) | 301 | 0.865 (0.82–0.90) | 0.711 (0.63–0.77) | −0.026 (−0.06, 0.01) | +0.006 | 1.114 (1.09–1.14) |

- U1 agreement changes by about 1 point per large season, which is within the spread across splits (SD 0.05–0.06). The mean kappa for the mostly-small group is 0.81 for U1 against 0.61 for SV, so the gap is not caused by class counts.
- SV's bias changes with composition: its above-normal bias runs from −0.19 at L = 0 to +0.09 at L = 3. U1's stays within 3 points.
- The real 2003–2011 era has 2 large seasons out of 9 (2003, 2009), so it falls in the mostly-small group.

**Part 2. Remedies minus U1 (mostly-small group, fire season).**

| Remedy | change in exact agreement | SD across splits | change in above-normal bias |
|---|---|---|---|
| Geometric mean of yearly ratios | +0.008 (−0.003, 0.018) | 0.024 | +0.002 |
| Two-level, by season size | +0.002 (−0.017, 0.018) | 0.025 | +0.008 (0.003, 0.015) |
| Log-log, by season size | +0.006 (−0.019, 0.026) | 0.036 | +0.009 |
| Two-level, by monthly MODIS count | −0.025 (−0.043, −0.003) | 0.060 | −0.017 |
| One factor per calendar month (review addition) | −0.011 (−0.030, 0.009) | 0.063 | +0.003 |
| Fire-season and off-season factors (review addition) | 0.000 | 0.005 | 0.000 |

**Part 3. The real baseline, label comparison with the VIIRS-only baseline.** Every month was classifiable. 2012-01 has no VIIRS value.

| Set | months | labels differ | mixed lower / higher | coarse classes differ |
|---|---|---|---|---|
| Box, fire season | 105 | 41 (39.0%, 33–45) | 38 / 3 | 22% |
| Box, all months | 177 | 58 (32.8%, 29–37) | 47 / 11 | 16% |
| 100 km circles, fire season | 3,255 | 36.1% (31–41) | 33.2% / 2.9% | 21% |
| 100 km circles, all months | 5,487 | 34.6% (31–38) | 28.9% / 5.7% | 18% |
| Box, fire season, Terra-only 2001–02 added (vs mixed) | 105 | 8 (7.6%, 4–12) | 3 / 5 | 4% |
| 100 km, fire season, Terra-only added (vs mixed) | 3,255 | 10.6% (9–13) | 2.8% / 7.8% | 5% |

Converted 2003–2011 median ÷ VIIRS 2012–2025 median, box: Mar 1.6, Apr 2.8, May 3.9, Jun 1.5, Jul 0.58, Aug 0.50, Sep 1.7, Oct 1.9, Nov 1.8. Each ratio's interval includes 1.

2026 fire season, box (classes 1–5; the value is NOAA-20 × 1.011, and the August–October counts come from near-real-time rows):

| | Apr | May | Jun | Jul | Aug | Sep | Oct |
|---|---|---|---|---|---|---|---|
| Mixed | 3 | 1 | 5 | 5 | 5 | 3 | 1 |
| VIIRS-only | 4 | 2 | 5 | 5 | 5 | 3 | 2 |
| Mixed + Terra-only | 3 | 1 | 5 | 5 | 5 | 3 | 1 |
| Mixed, calendar-month factor | 3 | 1 | 5 | 5 | 5 | 3 | 2 |

The remedies applied to the real box baseline left between 38 and 46 of the 105 fire-season labels different from VIIRS-only (analyst's table). A calendar-month factor gives 34.

**What the gap costs in level terms (box, fire season).**

| Pre-2012 converted values divided by | labels differ from VIIRS-only | labels changed vs plain mixed |
|---|---|---|
| 1 | 41 (39%) | – |
| 1.15 (typical-month bias) | 34 (32%) | 10, all upward |
| 1.27 (small-season bias) | 29 (28%) | 17, all upward |
| 1.6 (pre-2012 step from area burned) | 21 (20%) | 27, all upward |

**Part 4 and the length effect.** The months of 2012–2021 were classed against a long baseline (2003–2021) and a short one (2012–2021). The null was built from 1,000 random reassignments in the box and 300 in the circles. Each reassignment picks 9 of the pooled years as "early" at random, so the result shows what a length change alone does.

| Comparison, fire season | observed differ | null mean (95th pct) | p | observed long-lower | null mean | p |
|---|---|---|---|---|---|---|
| Box, MODIS counts only | 26.5% (19–33) | 25.6% (38%) | 0.46 | 22.1% | 12.0% | 0.12 |
| Box, converted + VIIRS, same years | 38.6% | 24.2% (39%) | 0.05 | 38.6% | 13.2% | 0.011 |
| Box, converted, 2012–2025 | 38.8% | 22.4% (34%) | 0.014 | 35.7% | 12.8% | 0.006 |
| 100 km, MODIS counts only | 33.0% | 24.3% (32%) | 0.023 | 29.1% | 13.5% | 0.020 |
| 100 km, converted, same years | 40.5% | 24.9% (33%) | 0.003 | 38.5% | 13.4% | 0.003 |

## What this implies

- The team could say that, on the stable years, a converted baseline of the real composition matches the VIIRS answer in about 87% of fire-season months, and that the small-season level bias moves class shares by 3 points or less there.
- The team could not say that a 24-year mixed baseline gives the same labels as VIIRS history. About 2 in 5 fire-season labels differ, and about 1 in 5 would be expected from the change of length alone. The excess consistently pushes current months lower, mostly in April, May, October and November.
- Two explanations fit the excess. One is real differences in burning before 2012 (more spring and autumn burning). The other is a pre-2012 conversion level that is too high. A level about 1.6 times too high would remove the excess. The data cannot separate the two. In the box, raw MODIS shows the shoulder-month pattern (April 2.7 times) but no excess label change beyond the length effect.
- No remedy tested is supported. Season-size factors cut the above-normal bias by about 1 point but do not change agreement. Factors keyed to the MODIS count make it worse.
- Suggested caveat for labels resting on pre-2012 years: they compare with history that includes converted 2003–2011 MODIS. Its spring and autumn medians are 1.6–3.9 times the VIIRS-era medians, and its level cannot be checked independently. Against VIIRS history alone, the label would differ in roughly two fire-season months in five, nearly always by one class higher.

## Limits

- Ten stable years, and the 582 splits reuse them. The SD across splits understates the uncertainty.
- Part 3 intervals resample only the evaluated years. The factor 0.2425 was fitted on 2012–2021, which includes evaluated years. Earlier work found that refitting changes labels by 0.3 points or less.
- The unlisted Suomi NPP gaps of May to July 2024 and the partial loss in July 2025 remain in the series. 2003-12 MODIS is masked. 2026 August–October values are near-real-time and untested against standard rows.
- The permutation null assumes years are interchangeable. Real fire regimes trend, so part of any "excess" may be genuine change.
- The circles are 100 km only and share years, so the effective sample is about 15 years.

## How it was computed

The analyst's `f01_build.py`, `f01_protocolB_composition.py`, `f01_B_summary.py` and `f01_real_baseline.py` were re-run from a clean start. Every output was byte-identical. `f01-real-length-baseline_review.py` recomputes the numbers independently: it reproduces the SPEC check (48,233, 198,916, 0.2425), builds local-date monthly counts with the standard filter, and selects circles by great-circle distance. It reruns Protocol B over all splits, Parts 3 and 4, the level sensitivity, two added remedies and the permutation null. Output is in `f01-real-length-baseline_review.csv` and `f01-real-length-baseline_review_log.txt`. `f01-real-length-baseline_review_streams.py` confirms that standard and near-real-time rows never share a date.
