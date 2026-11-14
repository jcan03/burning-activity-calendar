# Longer shots: an item-response model of the sensors, and hidden activity states

## Answer

Neither model is worth the team's time for the calendar. The Rasch model (an item-response model that gives each sensor-and-half-day "item" one difficulty) puts the four MODIS items 1.3 to 2.5 logits harder than Suomi NPP by day. However, it fits badly: an Andersen likelihood-ratio test gives 2,493 on 42 degrees of freedom. The gaps also double between weak and strong cell-days, and the items fall into a day group and a night group, not along one scale. Once its numbers are turned back into detection shares, it reproduces the simple cell-day ratios (Terra day 0.45, Aqua day 0.57 of Suomi NPP day) and adds nothing new. The hidden Markov model makes MODIS-only and Suomi NPP-only decoding agree in 90% of the 68 stable fire-season months (82–97%, held-out years), against 68% for the five-class scheme. That gain comes entirely from having fewer, coarser categories. Plain own-history ratio classes cut into the same number of groups, with the same shares, agree just as often: 91% for three groups and 85% for four, the same as the model.

## Evidence

### Part A: Rasch model of eight items

**Data.** The subjects are 12,781 active 5 km cell-days (one 5 km grid cell on one local date with at least one hotspot). They cover April–October 2018–2021, use `use == True` and standard rows, and come from Terra, Aqua, Suomi NPP and NOAA-20. All dates in the Aqua outage of 16 August – 2 September 2020 were dropped, removing 685 hotspots. Cell-days that no item detected are absent from the data by construction. The model was therefore estimated by **conditional maximum likelihood (CML)**. CML conditions on each cell-day's number of detecting items, so the fire's own strength drops out, and the selection "at least one detection" depends only on that number, which keeps the estimate valid. The 576 cell-days seen by all eight items carry no information under CML. The years are very unequal: 2018 has 3,487 cell-days, 2019 has 946, 2020 has 393 and 2021 has 7,955.

**Table A1. Difficulty relative to Suomi NPP day, in logits (higher means harder to trigger).** The intervals come from resampling whole years (4 years, 400 draws, so they are crude) and whole months (28 season-months). Ratios are against Suomi NPP day, over the same cell-days and hotspots.

| Item | Difficulty | Year interval | Month interval | Odds ratio exp(−b) | Cell-day ratio | Hotspot ratio |
|---|---|---|---|---|---|---|
| Terra day | 1.82 | 1.33–1.93 | 1.39–2.00 | 0.16 | 0.46 | 0.14 |
| Terra night | 1.48 | 1.32–2.54 | 1.33–2.07 | 0.23 | 0.54 | 0.23 |
| Aqua day | 1.32 | 0.97–1.40 | 1.09–1.51 | 0.27 | 0.58 | 0.20 |
| Aqua night | 2.50 | 2.38–4.10 | 2.26–3.53 | 0.08 | 0.32 | 0.11 |
| Suomi NPP night | −0.49 | −0.62–0.24 | −0.74–0.08 | 1.63 | 1.19 | 1.80 |
| NOAA-20 day | −0.04 | −0.07–0.04 | −0.09–0.04 | 1.04 | 1.01 | 0.98 |
| NOAA-20 night | −0.55 | −0.74–0.22 | −0.82–0.12 | 1.74 | 1.22 | 1.78 |

The standard errors that assume independent cell-days are about 0.03. They are far too narrow, because the resampling intervals are 5 to 30 times wider.

- **Ordering.** Every interval places the VIIRS items below every MODIS item. NOAA-20 day equals Suomi NPP day (−0.04, interval −0.09 to 0.04). Within MODIS, Aqua night is clearly the hardest item. The order of Terra day, Terra night and Aqua day is not stable.
- **Stability between halves.** The halves are 2018–19 (4,433 cell-days) and 2020–21 (8,348). Their rank correlation of the eight difficulties is 0.88. Individual difficulties move by up to 0.44 logits: Terra night −0.44, NOAA-20 night −0.42, Terra day +0.35. Terra night goes from the second-hardest MODIS item to the easiest. In effect this compares 2018 with 2021. In 2020 on its own, Aqua night never detected an informative cell-day, so its difficulty is infinite.
- **Fit.** Splitting cell-days by the number of items that saw them, the Andersen likelihood-ratio test gives 2,493 on 42 degrees of freedom. Splitting at 1–2 against 3–7 items gives 1,052 on 7 degrees of freedom. Both p-values are effectively zero. The Rasch model assumes item gaps that do not depend on fire strength, and they do. Terra day sits 1.1 logits above Suomi NPP day among cell-days seen by one item and 2.9 logits above among those seen by seven. For Aqua day the gap grows from 0.7 to 2.4. In other words, the VIIRS detection curves are steeper.
- **Local dependence.** Items that pass at the same time detect the same cell-day together more often than the model predicts: Suomi NPP day with NOAA-20 day 1.30 times as often, the two VIIRS nights 1.29, Terra day with Aqua day 1.26. Day–night pairs do so less often: Terra night with Aqua night 0.63, Terra day with Terra night 0.76. Activity on a cell-day therefore has at least two dimensions, daytime and night-time burning. Among the 3,761 cell-days seen by one item only, 15% were seen only by Terra at night (about 21:30 local solar time), where the model expects 4%.
- **Completeness.** A Rasch odds ratio is not a detection ratio. Assuming a normal distribution of fire strength and fitting it to the truncated score distribution (which it fits poorly) gives the detection shares that follow from the model. Relative to Suomi NPP day these are Terra day 0.45, Terra night 0.53, Aqua day 0.57, Aqua night 0.31 and NOAA-20 day 1.01, essentially the observed cell-day ratios. The same fit implies that 47% of active cell-days were missed by all eight items (year interval 38–56%). That figure rests entirely on the assumed strength distribution and should not be used.

### Part B: hidden activity states

**Model.** The data are monthly counts for 10 streams (five sensors, each by day and by night), November 2000 to October 2026, from `use == True` standard and near-real-time rows. Of 3,120 stream-months, 1,810 were observed. The rest are missing: the sensor was not yet flying, had ended, or had a listed outage that month. The 272 observed zero months are kept as zeros. Counts follow a negative binomial distribution whose mean is a stream scale × a shared calendar-month profile × a state level. The states are ordered and follow a Markov chain. The model was fitted by EM with 12 random restarts. The likelihood has several local optima: in 20 restarts the best three-state optimum appeared 3 times.

**Fit.** With three states the levels are 0.15, 0.64 and 10.6 (relative to their geometric mean), and the chance of staying in a state from one month to the next is 0.45–0.64. The four-state model has a lower BIC (Bayesian information criterion): log-likelihood −7,539 against −7,622 for 14 more parameters. In both, the fitted calendar profile puts October and November above August. That profile describes a typical year and is not a per-month median.

**Table B1. MODIS-only against Suomi NPP-only decoding.** The months are the 68 stable-orbit April–October months (2012–2021, without 2020-08 and 2020-09). All of them are classifiable, with no month dropped for a zero baseline. The intervals come from resampling whole years (10 years, 1,000 draws). "Own-history" classes compare each sensor's count with its median for the same calendar month over the other nine years.

| Scheme | Categories | Same category | Kappa |
|---|---|---|---|
| Own-history, five classes | 5 | 68% (59–76) | 0.55 |
| Own-history, three coarse classes (0.5, 2) | 3 | 79% (68–90) | 0.69 |
| HMM, three states, held-out year | 3 | 90% (82–97) | 0.82 |
| Own-history, three classes cut at HMM shares | 3 | 91% (84–97) | 0.84 |
| HMM, four states, held-out year | 4 | 85% (79–92) | 0.79 |
| Own-history, four classes cut at HMM shares | 4 | 85% (81–90) | 0.79 |

Kappa is agreement corrected for chance. The "held-out year" rows refit the model without that year (all streams of that year set missing) and then decode that year. In-sample decoding gives 87–93%, depending on the number of states and on whether neighbouring months are used. Treating MODIS from 2022 onward as missing changes agreement by under 2 points.

- **The 71% figure.** This analysis gets 68% on the 68 months. Applying the earlier floor (baseline median of at least 10, which leaves 48 months) gives 75% (67–83). The earlier 71% used a baseline that included the month's own year and UTC months. On the same 48 months the three-state HMM gets 90% and the matched three-class scheme 94%.
- **Interpretability.** In the three-state model, the low state holds 41 of the 68 months: median Suomi NPP ratio to normal 0.49, spanning all five classes (22, 10, 4, 4 and 1 months). The middle state has median ratio 2.4 (18 months). The top state has median ratio 76 (9 months: July–September 2017, May, August and September 2018, and June–August 2021). The states mean "ordinary, big, extreme", not "below, near, above normal". Of the 28 months that either sensor calls near normal (0.5–2), the three-state model puts 20 in its low state. It agrees on 86% of them by not separating them, where the five classes agree on 21%. The four-state model splits off a near-normal state (median ratio 1.2), but that state contains months from all five classes.
- **Stability when years are left out.** For three states, leaving out each stable year changes the state of a median of 1.6% (at most 4.9%) of the other fire-season months, and the top level ranges from 8.7 to 11.8. For four states the median is 3.3% (at most 13%). The four-state solution also depends on the optimum: the default start's optimum differs from the best in 32% of months.

## What this implies

- The team could say that a Rasch analysis confirms that MODIS items are much harder to trigger than VIIRS items and that NOAA-20 and Suomi NPP are equivalent. It could not use the Rasch difficulties as conversion factors. The model is rejected, the gaps depend on fire strength, and turned back into detection shares they equal the cell-day ratios already measured.
- The Rasch fit points to two things that matter for any method: day and night behave as separate dimensions, and VIIRS gains more than MODIS as fires strengthen. Both support keeping day and night apart rather than relying on one factor.
- The team could not claim that hidden states make MODIS and VIIRS agree better than ratio classes. The higher agreement equals what coarser ratio classes give at the same number of categories.
- Hidden states would label months "ordinary, big, extreme". That does not answer "how does this month compare with normal" for near-normal months.

## Limits

- Part A rests on four fire seasons, one of which supplies 62% of the cell-days. The year intervals use only four resampling units.
- The Rasch analysis cannot see cell-days that every sensor missed. Any completeness figure beyond detected cell-days rests on an assumption.
- A two-dimensional or two-parameter item-response model, which the misfit points to, was not fitted.
- The HMM uses one seasonal profile for all streams and has several local optima. Twelve restarts may not find the global one.
- Part B tests agreement between sensors, not correctness. No ground truth for monthly classes exists.
- Neither part used the circles. Below 100 km, counts are smaller and both models would do worse.

## How it was computed

The check numbers were reproduced (48,233; 198,916; ratio 0.2425; 0.343 by day, 0.177 at night) by `a11_check.py`. `a11_rasch.py` builds the 5 km cell-day by item table and fits Rasch CML with elementary symmetric functions and a sum-to-zero constraint. It also runs year and month bootstraps, fits each half, each year and each score group separately, runs the Andersen tests, computes pair co-detection and item fit, and fits the truncated normal model. `a11_hmm.py` defines and fits the negative-binomial HMM by EM. `a11_hmm_test.py` runs the decoding comparisons, the leave-one-year-out refits and the sensitivity checks. `a11_hmm_matched.py` builds the own-history class schemes matched to the HMM's shares. The scripts are in `round3/scripts/` and the tables, all beginning `a11_`, are in `round3/out/`.
