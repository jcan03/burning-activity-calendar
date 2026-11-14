# Box counting: separating the pixel-size effect from the sensitivity effect

## Answer

Counting occupied grid cells instead of hotspots explains the gap between the sensors, but it does not make the conversion more accurate. Over the 116 stable-orbit months, MODIS (Terra plus Aqua) records 0.24 hotspots per Suomi NPP hotspot. In occupied cells the ratio rises to 0.58 at 1 km and 0.69 at 2 km. The MODIS-to-Suomi NPP ratio splits exactly into two parts. The first is a geometric part: 2.56 Suomi NPP hotspots per occupied 1 km cell, 2.26 by day and 2.80 at night. The second is a remaining part: 0.62 MODIS hotspots per Suomi NPP 1 km cell. The remaining part carries about two thirds of the day-night difference for MODIS (68%, interval 58–92%) and about five sixths for Aqua (84%, interval 80–95%). It also carries all of the year-to-year variation at night. In the 10-year data, the two parts rise together in big fire years and largely cancel. For all hours together, the share of year-to-year variation carried by each part cannot be determined. In leave-one-year-out prediction of monthly MODIS counts, no cell-based link beat the plain ratio of hotspot counts. A link that allows saturation did not saturate: the fitted curves are convex, not concave.

## Evidence

Data and conventions throughout: `use == True` and standard rows only. Months are keyed by local date. The stable period has 116 months (2012-02 to 2021-12, without 2016-02, 2020-08 and 2020-09); Aqua-only results use 117 months, keeping 2016-02. The SPEC check numbers were reproduced exactly: MODIS 48,233, Suomi NPP 198,916, ratio 0.2425 (day 0.343, night 0.177). Terms used below:

- An **occupied cell** is a distinct combination of sensor, local date, day or night pass, and grid cell (from `x_km`, `y_km`). Counts are summed over months.
- **Intervals** are 95% year-block bootstrap intervals. The 10 calendar years are resampled whole, with 1,000–2,000 draws.

**Occupied cells, sums over 116 months**

| | Hotspots | 1 km | 2 km | 4 km | 8 km |
|---|---|---|---|---|---|
| Suomi NPP | 198,916 | 77,705 | 47,136 | 30,772 | 22,086 |
| MODIS | 48,233 | 45,167 | 32,408 | 22,688 | 16,820 |
| Ratio, MODIS to Suomi NPP | 0.24 | 0.58 | 0.69 | 0.74 | 0.76 |

Moving the grid origin by half a cell changes the 1 km and 2 km ratios by less than 0.002.

**How occupied cells fall with cell size.** The box-counting exponent D is defined by N(s) ∝ s^−D. Here N(s) is the number of occupied cells at cell size s. D was fitted by least squares on the log of counts summed over 116 months.

| Series | Pooled D (interval) | Median of 10 single-year fits (range) |
|---|---|---|
| Suomi NPP, 0.375–4 km | 0.71 (0.45–0.79) | 0.42 (0.34–0.83) |
| Suomi NPP, 1–8 km | 0.60 (0.34–0.70) | 0.31 (0.25–0.76) |
| MODIS, 1–8 km | 0.49 (0.29–0.54) | 0.29 (0.20–0.59) |
| Aqua, 1–8 km (117 months) | 0.47 (0.29–0.53) | 0.30 (0.22–0.59) |

D is not a property of the sensor. It follows fire activity: over 1–8 km, Suomi NPP D is 0.14, 0.29 and 0.66, and MODIS D is 0.17, 0.24 and 0.51, in months with 10–99 (53 months), 100–999 (34) and 1,000 or more (24) Suomi NPP hotspots. Part of this is mechanical. A month with only a few hotspots occupies one cell per hotspot at every size, so its D is near 0. The 5 months with fewer than 10 hotspots give exactly 0. The pooled values are set by 2017, 2018 and 2021.

**Decomposition.** The ratio splits exactly as M/S = (M/C1) ÷ (S/C1):

- M is MODIS hotspots and S is Suomi NPP hotspots.
- C1 is Suomi NPP occupied 1 km cells.
- G = S/C1 is the geometric part.
- Rm = M/C1 is the remaining part.

| 116 months | Ratio | G | Rm |
|---|---|---|---|
| All hours | 0.242 | 2.56 | 0.62 |
| Day | 0.343 | 2.26 | 0.78 |
| Night | 0.177 | 2.80 | 0.50 |
| Aqua, all hours (117 months) | 0.113 | 2.56 | 0.29 |

Across calendar years, G ranges from 1.68 (2020) to 2.79 (2021). It rises with activity.

**Day-night gap** (log of day ratio ÷ night ratio; intervals from 2,000 year resamples):

| | Gap | Geometric share | Remaining share |
|---|---|---|---|
| MODIS | 0.66 (0.56–1.13) | 0.32 (0.08–0.42) | 0.68 |
| Aqua | 1.31 (1.19–1.89) | 0.16 (0.05–0.20) | 0.84 |

**Year-to-year variation.** The share of the variance of log(ratio) across years carried by G is computed as cov(log ratio, −log G) ÷ var(log ratio). Rm carries the remainder. The table covers 10 years.

| MODIS | Ratio range | Share carried by G (interval) | Correlation of G and Rm |
|---|---|---|---|
| All hours, calendar year | 0.20–0.33 | 0.35 (−0.33 to 3.2) | 0.73 |
| All hours, April–October | 0.20–0.41 | 0.24 (−0.25 to 1.14) | 0.56 |
| Day, calendar year | 0.31–0.49 | 0.64 (0.05–1.22) | 0.23 |
| Night, calendar year | 0.05–0.19 | −0.46 (−0.95 to −0.22) | 0.92 |
| Aqua day, calendar year | 0.19–0.28 | 0.78 (0.17–1.54) | 0.45 |
| Aqua night, calendar year | 0.006–0.062 | −0.27 (−0.45 to −0.15) | 0.92 |

A negative share means G moves against the ratio. At night, big years have more Suomi NPP pixels per cell, but MODIS night detections rise even faster.

**Leave-one-year-out prediction of monthly MODIS counts.** Each model was fitted on 9 years (all months) and tested on the 10th. Scores are for fire-season (April–October) months and are median absolute percentage errors (MdAPE). The difference from the plain ratio carries a year-bootstrap interval.

| Model, pooled day and night | 67 months, MODIS ≥ 1 | 46 months, Suomi NPP ≥ 40 | 68 months, log error* |
|---|---|---|---|
| Plain hotspot ratio | 0.31 | 0.28 | 0.30 |
| 1 km cell ratio | 0.36 (+0.05; −0.07 to +0.09) | 0.31 (+0.03; −0.10 to +0.10) | 0.32 (+0.02; −0.07 to +0.10) |
| 1 km power law | 0.37 (+0.06; 0.00 to +0.12) | 0.34 | 0.38 |
| 1 km saturating | 0.43 (+0.12; +0.01 to +0.16) | 0.41 | 0.46 |
| 2 km cell ratio | 0.56 (+0.25; +0.11 to +0.57) | 0.45 | 0.44 |
| 2 km power law | 0.39 | 0.36 | 0.41 |

\*The log error is the median of |log((predicted+1)/(actual+1))|. It keeps the one zero month, 2012-06.

The power-law exponent on cells is above 1 (1.12 at 1 km, 1.19 at 2 km). Two saturating forms were fitted: the analyst's exponential form and an independent Michaelis–Menten form, a·x/(1+x/K). Both pushed the saturation level K to its upper bound, which makes the fit effectively linear. Fitting day and night separately made every cell model worse. For Aqua alone (62 months with Aqua ≥ 1), the plain ratio scores 0.30, the 1 km cell ratio 0.37, the 1 km power law 0.34 and the saturating link 0.39. Sharing an overpass time with Suomi NPP does not change the ranking.

**Zero and excluded months.** The 3 outage months are excluded by the SPEC rule. Among the 116 months, MODIS is zero in 4 (one in the fire season, 2012-06), Suomi NPP in 1 (2020-06, when MODIS had 1), and Aqua in 9 of 117 (6 in the fire season). Log fits drop zero months in training. No calendar classes are used, so no month is unclassifiable.

**Against the earlier evidence.** The evidence file gives 0.65 for MODIS against Suomi NPP in 2 km cell-days. That analysis took the union of Terra and Aqua and merged day and night passes. With that definition this data gives 0.654 (68 fire-season months), which matches. With this task's definition (each sensor and pass counted separately) the same months give 0.74, and 0.69 over all 116 months. The 0.19–0.40 fire-season range is reproduced (0.199–0.408). The finding that a curve does not beat one factor agrees with the evidence file.

## What this implies

- The team can state why one MODIS hotspot corresponds to about four Suomi NPP hotspots. About 2.6 of the 375 m pixels fall in each occupied 1 km cell, more in big fires. On top of that, MODIS records only about 0.6 hotspots per such cell. The team can also show that the day-night difference comes mostly from the second part, not from pixel size. This gives a physical reason for separate day and night factors.
- The team cannot claim that a cell-based or multi-scale conversion is more stable or more accurate than one hotspot factor. Here it was not, in leave-one-year-out error for MODIS or for Aqua.
- The team cannot claim that a box-counting exponent is a fixed sensor property usable for scale transfer. It varies from 0 to about 0.8 with month size, and at the same scale range the two sensors' typical yearly values are nearly equal (0.31 and 0.29).
- A year's conversion error cannot be blamed on pixel geometry alone. At night it is detection, and over all hours the split is undetermined.

## Limits

The analysis covers 10 years in one box, and 2017, 2018 and 2021 dominate every pooled sum. The "remaining part" is not pure sensitivity. It also contains MODIS's own geometry: pixels that grow off nadir, the 1 km grid not matching the MODIS footprint, and Terra and Aqua counted as two looks. The scale fits span only about one decade, and the curves are not single power laws. The drift period (2022 onward), near-real-time rows and circles were not used, so nothing here shows how the parts behave in a small area or after 2021.

## How it was computed

- `scripts/a07_cells.py`, `a07_analysis.py`, `a07_extra.py` are the analyst's scripts. They were re-run from a clean start and their outputs are byte-identical.
- `scripts/a07-box-counting_review.py` is an independent recomputation of the cells (`np.unique` keys), the exponents, the decomposition with intervals, the leave-one-year-out comparison (with predictor-side month selection and a zero-tolerant log error) and the reconciliation with the 0.65 definition. It writes `out/a07rev_*.csv`, logs to `out/a07rev_run.txt`, and runs in about 20 seconds.
