# Does a converted MODIS-era record give the right calendar class? Whole box

## Answer

Over the whole box, a mixed baseline in which five MODIS years are scaled up with one factor (design U1) gives the same five-class label as a full Suomi NPP baseline in 84% of fire-season months and 80% of all months. The standard deviation (SD) across the 202 test splits is 5 points. It is within one class in 97–98% of months. A short baseline from the VIIRS years alone (SV) gets 66% and 65%. U1 beats SV by 18 points in the fire season (95% year-bootstrap interval 14 to 23) and by 15 points over all months (10 to 20). U1 wins in 94–95% of splits. The direction of conversion does not matter at this scale: thinning VIIRS down by expectation (DE) gives the same label as U1 in 11,705 of 11,706 cases. Thinning at random (DR) is only about 2 points worse, not the 5 points the draft reported, because of a code bug corrected here. Neither a day/night split (U2) nor 2 km daytime cell-days (UC) beats U1 at box scale. U2 is level with U1 in the fire season and 7 points worse over all months. UC's apparent shortfall comes mostly from scoring cell-day labels against count-based truth. In its own units UC gains as much over a short baseline as U1 does.

## Evidence

**Terms.** *Exact*: the design's five-class label equals the truth's. *Within one*: no more than one class apart. *Coarse*: same of three classes (below 0.5, 0.5–2, above 2). *Kappa*: Cohen's kappa over the five classes. *Bias above* and *bias below*: the design's share of months labelled above 1.25 (or below 0.8) minus the truth's share. *Truth*: the class of a Suomi NPP month against the median of Suomi NPP counts for the same calendar month in the other nine stable years.

**Data.** The data are hotspots with `use == True` and standard (SP) rows only, keyed by local-date month. The test period is the 116 stable-orbit months from 2012-02 to 2021-12, without 2016-02, 2020-08 and 2020-09. MODIS means Terra plus Aqua. The check numbers reproduce exactly: MODIS 48,233, Suomi NPP 198,916, ratio 0.2425 (day 0.343, night 0.177). The 2 km daytime cell-day ratio is 0.668.

**Zero and unclassifiable months.** Every truth baseline median in the box is 13 or more (median 90), so no month is unclassifiable and the "baseline median at least 10" restriction removes nothing. Its results equal the "all months" results. No design baseline median fell below 1 in MODIS units, so zeros never break DE here. The three outage months are excluded for both sensors. Some individual months are zero: Suomi NPP in 1 month (2020-06), MODIS in 4, and MODIS at night in 31, mostly in winter. Months with a zero actual value are left out of percentage error only, so the error counts are 67 fire-season and 115 all months for U1 and U2, and 65 and 112 for UC. They are kept in all class scores. The truth is concentrated in the extremes: only 5.7% of fire-season rows in Protocol B are truly "normal" (0.8–1.25), and 31% fall in each outer class.

**Protocol B (mixed-era baseline).** 202 splits and 11,706 classed rows in all (6,862 in the fire season). The table shows the mean over splits, with the SD across splits in brackets.

| Design | Fire season: exact | Kappa | Within one | Coarse | Bias above / below | All months: exact | Kappa |
|---|---|---|---|---|---|---|---|
| U1 (= DE) | 0.844 (0.053) | 0.785 | 0.981 | 0.925 | −0.029 / +0.009 | 0.797 (0.054) | 0.736 |
| U2 | 0.830 (0.053) | 0.767 | 0.998 | 0.937 | −0.003 / −0.027 | 0.727 (0.050) | 0.645 |
| DR, binomial (corrected) | 0.823 (0.046) | 0.756 | 0.980 | 0.909 | −0.029 / −0.003 | 0.774 (0.052) | 0.706 |
| DR, beta-binomial | 0.734 (0.045) | 0.627 | 0.970 | 0.814 | −0.019 / −0.003 | 0.656 (0.054) | 0.546 |
| UC vs count truth | 0.759 (0.069) | 0.674 | 0.943 | 0.892 | −0.010 / −0.027 | 0.686 (0.053) | 0.591 |
| SV | 0.661 (0.093) | 0.551 | 0.904 | 0.776 | −0.058 / +0.002 | 0.645 (0.062) | 0.546 |
| UC vs cell-day truth | 0.873 (0.083) | 0.826 | 0.993 | 0.948 | +0.049 / +0.019 | 0.807 (0.056) | 0.750 |
| SV in cell-days vs cell-day truth | 0.693 (0.102) | 0.594 | 0.894 | 0.789 | −0.004 / +0.019 | 0.660 (0.077) | 0.564 |

For the random-thinning designs, the share of draws that gave the true class averages 0.79 (binomial) and 0.67 (beta-binomial) in the fire season. The beta-binomial overdispersion averaged 0.060 (range 0.028–0.090). In months whose truth baseline is at least 100 (3,325 fire-season rows), exact agreement is 0.952 for U1 and DR, 0.922 for U2, 0.918 for UC, 0.889 for beta-binomial DR and 0.702 for SV. This subset is selected on the truth baseline, which an app would not know.

**Paired differences in exact agreement.** The first two columns are pooled rows, with a 95% interval from 4,000 resamples of the ten classed years. "Split SD" is the SD of the paired difference across the 202 splits.

| Contrast | Fire season | All months | Split SD (fire season) | Larger than the spread? |
|---|---|---|---|---|
| U1 − SV | +0.182 (0.139 to 0.226) | +0.152 (0.103 to 0.196) | 0.105 | Yes. U1 wins in 94% of splits |
| DR − SV | +0.161 (0.123 to 0.196) | +0.129 (0.082 to 0.173) | 0.104 | Yes |
| U2 − SV | +0.169 (0.121 to 0.218) | +0.083 (0.023 to 0.145) | 0.096 | Yes |
| UC − SV (count truth) | +0.097 (0.003 to 0.179) | +0.041 (−0.042 to 0.115) | 0.118 | Borderline / no |
| UC − SV, both in cell-days | +0.180 (0.131 to 0.229) | +0.147 (0.081 to 0.211) | 0.114 | Yes |
| U2 − U1 | −0.013 (−0.048 to 0.021) | −0.069 (−0.101 to −0.038) | 0.045 | No / yes, worse |
| DR − U1 | −0.021 (−0.046 to 0.002) | −0.023 (−0.042 to −0.007) | 0.039 | No / just |
| Beta-binomial DR − DR | −0.089 (−0.114 to −0.060) | −0.118 (−0.147 to −0.091) | 0.057 | Yes, worse |
| UC − U1 (count truth) | −0.085 (−0.175 to −0.013) | −0.111 (−0.176 to −0.062) | 0.087 | Yes, but the units differ |
| U1 with f fitted without the classed year − U1 | +0.001 (−0.001 to 0.004) | 0.000 | 0.014 | No |
| U1 with f 20% too low − U1 | −0.045 (−0.084 to −0.007) | −0.029 | 0.063 | Small |
| U1 with f 25% too high − U1 | −0.001 (−0.040 to 0.035) | −0.049 | 0.055 | Small |

U1 misses mostly by one class. In the fire season, 681 rows are one class too low, 259 one class too high and 132 two classes too low. The two chronological splits give U1 0.939 against SV 0.667 when 2012–16 is the MODIS era, and 0.914 against 0.629 in the reverse split.

**Why U2 loses outside summer.** The night ratio of MODIS to Suomi NPP is 0.18–0.19 in July and August, but 0.03–0.12 in March–May and September–December. In those months it is 0.00–0.08 in individual years. A pooled night factor of 0.177 therefore converts quiet-month MODIS baselines too low. U2 then labels 5.6 points too many months above normal, and its exact agreement in March falls to 0.41 against U1's 0.76.

**Protocol A (single-month conversion).** 116 months, each held-out year fitted on the other nine. Intervals come from 2,000 resamples of years.

| Design | Fire season: median abs. % error | Fire season: class agreement | All months: error | All months: agreement |
|---|---|---|---|---|
| U1 (= DE) | 0.33 (0.26–0.38) | 0.69 (0.61–0.77) | 0.32 (0.27–0.36) | 0.64 (0.58–0.70) |
| U2 | 0.28 (0.23–0.40) | 0.66 (0.59–0.74) | 0.34 (0.30–0.40) | 0.55 (0.49–0.62) |
| UC (own units / count truth) | 0.29 (0.20–0.44) | 0.62 / 0.53 | 0.30 (0.25–0.44) | 0.59 / 0.50 |
| DR | — | 0.69 (0.61–0.77) | — | 0.65 (0.58–0.72) |

All the design differences in Protocol A lie inside the year-bootstrap intervals.

**Against the earlier evidence.** The results agree with it. Protocol A's 69% fire-season agreement matches the 71% same-label rate for each sensor against its own history. The 33% error matches "about 30% over all fire-season months". UC's lower error in large months (0.18 against 0.25 where the baseline is at least 100) matches "modest gain for a single month". "Splitting gave no measurable gain" holds for the fire season. The new finding is that U2 is worse over all months, for the reason given above. The 16% of fire-season labels that U1 gets wrong lies within the 8–21% that the evidence found changes when the baseline years change.

## What this implies

- At whole-box scale the team could claim that a baseline whose MODIS years are converted with one ratio-of-sums factor reproduces the all-VIIRS label in about 5 of 6 fire-season months and is within one class in about 49 of 50. It could also claim that this is clearly better, by 15–18 points, than a VIIRS-only baseline of the same span.
- The team could claim that converting up or down gives the same labels at this scale. Random thinning adds little error with a binomial draw and loses about 9–12 points with a beta-binomial draw.
- The team could not claim from this test that a day/night split or cell-days improve labels for the whole box. Over all months a pooled night factor makes labels worse.
- Labels are not sensitive to the exact factor: an error of 20–25% in f costs 0–5 points.
- None of this transfers to circles of 100 km radius or less, where zeros occur.

## Limits

- The test covers only ten stable-orbit years. The splits reuse them, so the split SD understates the uncertainty. The year bootstrap resamples only the classed years and holds the baseline years fixed.
- The "truth" is a nine-year Suomi NPP median. The real calendar uses about 24 years, including Terra-only years and drift-period MODIS, and neither of those was tested.
- The test does not cover areas smaller than the box, NRT rows, or NOAA-20 or NOAA-21 as the current sensor.
- The baseline-at-least-100 subset is selected on the truth baseline.

## How it was computed

- `scripts/a01_build.py`, `a01_hindcast.py` and `a01_analyse_B.py` (the analyst's scripts) were re-run from a clean start and reproduced the draft's tables byte for byte.
- `scripts/a01-hindcast-box_review.py` rebuilds the monthly counts and cell-days from the parquet independently and reruns Protocols A and B. It adds the corrected DR, UC and SV scored in cell-days, f fitted without the classed year, and f shifted by ±20–25%. The outputs are `out/a01-hindcast-box_review_*.csv` and `_log.txt`.
- `scripts/a01-hindcast-box_review_extra.py` checks the zero months, the truth class mix and the monthly day and night ratios.
