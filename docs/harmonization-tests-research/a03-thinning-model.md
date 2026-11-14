# Thinning as the conversion: how much scatter is irreducible, and what a zero means

## Answer

Treating MODIS as a random thinning of Suomi NPP hotspots (each kept with probability 0.343 by day and 0.177 at night) explains only a small part of the month-to-month scatter. Thinning hotspot by hotspot accounts for about 15% of the variance of the monthly log ratio in the box and 22–28% in 50 and 100 km circles. Thinning whole fire-days instead (all hotspots in one 2 km cell on one local date and pass kept or dropped together) accounts for about 40% in the box, 47–50% at 100 km and 67–70% at 50 km. The binomial model is rejected everywhere. A beta-binomial model with intra-class correlation ρ ≈ 0.06–0.09 fits much better, which means the kept share itself varies by about ±44% from month to month. The kept share also depends on the size of the month. At night it rises with size. In the fire season the daytime share falls with size, so quiet fire-season months run above busy ones overall. In circles, a month with no MODIS hotspot is consistent with up to about 6 Suomi NPP hotspots at 50 km and 17 at 100 km (90th percentile; 4 and 9 in the fire season). The inverse intervals from a beta-binomial model under-cover: nominal 90% intervals held the true count in 72–79% of held-out fire-season months.

## Evidence

All results use the Spec filter (`use == True`, standard rows only), local-date months and the 116 stable-orbit months (2012-02 to 2021-12, without 2016-02, 2020-08 and 2020-09). The check numbers reproduce exactly: MODIS 48,233, Suomi NPP 198,916, ratio 0.2425 (0.343 by day, 0.177 at night). No other outage falls in this period. The circles are the 31 Spec centres at each radius. They overlap, so pooled circle sample sizes overstate precision. All intervals are 95% intervals from resampling the 10 years. In the tables, **N** is the Suomi NPP count, **M** the MODIS (Terra plus Aqua) count, and **E** = 0.343·N(day) + 0.177·N(night) the expected thinned count.

**1. Share of observed scatter explained by thinning.** The share is the variance of ln(thinned/E) divided by the variance of ln(M/E), over the same unit-months, using 300 thinning draws. Unit-months with E = 0 are excluded (box 1, 50 km 1,127, 100 km 165). The log measure also drops months with M = 0 (box 4, 50 km 889, 100 km 639). The last column keeps those months and uses ln((x+0.5)/(E+0.5)) instead.

| Unit, months | Unit-months | SD observed | Random share | Clustered share | Clustered share, zeros kept |
|---|---|---|---|---|---|
| Box, all | 111 | 0.61 | 15% (10–25) | 40% (29–61) | 44% (35–59) |
| Box, fire season | 66 | 0.51 | 26% (19–45) | 64% (43–101) | 85% (57–128) |
| Box, E ≥ 10 | 88 | 0.48 | 10% (7–16) | 41% (29–66) | 42% (30–66) |
| 50 km, all | 1,580 | 0.68 | 28% (24–34) | 70% (60–85) | 86% (81–92) |
| 50 km, E ≥ 10 | 796 | 0.41 | 17% (14–22) | 108% (86–148) | 120% (94–162) |
| 100 km, all | 2,792 | 0.74 | 22% (18–29) | 47% (39–63) | 57% (47–73) |
| 100 km, E ≥ 10 | 1,448 | 0.40 | 14% (9–19) | 78% (49–107) | 86% (56–115) |

The median absolute percentage error (MAPE) of fire-season box months is 8% under random thinning and 16% under clustered thinning, against 31% observed. The 16% matches the ±15–20% that two identical VIIRS satellites differ by in one month (earlier evidence). In circles with E ≥ 10, clustered thinning matches or exceeds the observed scatter. That makes the 2 km fire-day grouping an over-correlated limit there, not a proof that all of the scatter is sampling.

**2. Beta-binomial fits of M given N, box.** These are in-sample maximum-likelihood fits. Months with N = 0 were dropped (1). Months with M > N were also dropped: none for all hours and 6 by day, all of them fire-season months. The slope is b in logit(p) = a + b·ln(N/100).

| Hours, months | Months used | p | Pearson dispersion | ρ (CI) | Size slope b (CI) |
|---|---|---|---|---|---|
| All, all months | 115 | 0.243 | 23 | 0.062 (0.039–0.083) | +0.04 (0.01–0.06) |
| All, fire season | 67 | 0.243 | 35 | 0.058 (0.032–0.077) | **−0.05 (−0.09 to −0.02)** |
| Day, all months | 106 | 0.343 | 17 | 0.080 (0.042–0.124) | 0.00 (−0.06 to 0.06) |
| Day, fire season | 59 | 0.339 | 24 | 0.093 (0.029–0.154) | **−0.09 (−0.17 to −0.01)** |
| Night, all months | 115 | 0.177 | 30 | 0.091 (0.047–0.131) | +0.22 (0.18–0.27) |
| Night, fire season | 67 | 0.184 | 40 | 0.089 (0.023–0.160) | +0.14 (0.07–0.19) |

A Pearson dispersion of 1 would mean binomial. The fire-season box ratio of sums by thirds of month size is 0.38 (0.28–0.48) for quiet months (N 0–39), 0.28 for middle months and 0.24 (0.24–0.30) for busy months (N ≥ 404). By day the same thirds give 0.87, 0.38 and 0.34. In circles, ρ is 0.07–0.13 by day and by night.

**3. Share of months with M = 0, by N, in circles.** The predictions use box parameters.

| Radius, N | Months (all / fire season) | Observed, all months (CI) | Observed, fire season (CI) | Binomial (fire season) | Beta-binomial (fire season) | Clustered (fire season) |
|---|---|---|---|---|---|---|
| 50 km, 3–4 | 320 / 176 | 0.66 (0.56–0.73) | 0.52 (0.40–0.64) | 0.38 | 0.41 | 0.50 |
| 50 km, 5–9 | 335 / 140 | 0.46 (0.40–0.54) | 0.36 (0.31–0.42) | 0.16 | 0.20 | 0.32 |
| 50 km, 10–19 | 260 / 124 | 0.25 (0.19–0.34) | 0.11 (0.06–0.20) | 0.03 | 0.07 | 0.20 |
| 50 km, 20–49 | 306 / 138 | 0.05 (0.02–0.09) | 0.01 (0.00–0.03) | 0.00 | 0.01 | 0.06 |
| 100 km, 5–9 | 368 / 252 | 0.35 (0.25–0.45) | 0.23 (0.14–0.35) | 0.18 | 0.23 | 0.30 |
| 100 km, 10–19 | 584 / 350 | 0.24 (0.17–0.35) | 0.11 (0.03–0.16) | 0.02 | 0.05 | 0.10 |

No month with N ≥ 50 had M = 0. Among months with N = 0, 13% (50 km) and 22% (100 km) still had M > 0.

**4. Suomi NPP count in months with M = 0.** These are all 31 circles over 116 months.

| Unit | M = 0 months | Share with N = 0 | Median N | 90th percentile | Maximum |
|---|---|---|---|---|---|
| 50 km, all / fire season | 1,866 / 1,061 | 52% / 60% | 0 / 0 | 6 / 4 | 36 / 27 |
| 100 km, all / fire season | 767 / 414 | 17% / 30% | 4 / 2 | 17 / 9 | 37 / 23 |
| Box | 4 (1 in fire season) | 0 | — | N = 1 to 17 | 17 |

The 90th percentile was also taken from nine years and checked on the tenth. It contained N in 92% of held-out M = 0 months at 50 km and 90% at 100 km.

**5. Inverse: coverage of the actual Suomi NPP count in held-out fire-season months.** In each fold, p and ρ are fitted on the box over the nine training years. The area prior is a negative binomial matched to the same unit's Suomi NPP counts for that calendar month in the training years. Coverage uses a randomised probability integral transform on an integer grid. A month with M > N counts as a miss; there were 1.5% of these in the box, 8.5% at 50 km and 5.6% at 100 km.

| Unit (months) | Flat prior, binomial (50/80/90%) | Flat prior, beta-binomial | Area prior, beta-binomial (90% CI) |
|---|---|---|---|
| Box (68) | 16 / 29 / 37 | 43 / 66 / 76 | 38 / 71 / 79 (74–85) |
| 50 km (2,108) | 25 / 53 / 64 | 29 / 60 / 72 | 40 / 66 / 76 (72–80) |
| 100 km (2,108) | 24 / 42 / 50 | 37 / 63 / 75 | 37 / 65 / 76 (71–80) |

With a flat prior, the beta-binomial posterior median overstates N by a factor of about 1.55 (median log bias +0.44 to +0.48, for months with N ≥ 10). The area prior removes this bias in circles (0.00 to +0.01) and leaves +0.13 in the box. The 90% intervals span a factor of about 4.5–5 between their upper and lower ends.

**Formulas, fitted on the whole box (116 months).**
- M | N ~ BetaBinomial(N, α, β), with α = p(1−ρ)/ρ and β = (1−p)(1−ρ)/ρ. Take p = 0.2425 and ρ = 0.062 (fold range 0.053–0.070), which gives α = 3.67 and β = 11.4. The mean is Np and the variance is Np(1−p)(1+(N−1)ρ).
- P(M = 0 | N) = Γ(N+β)Γ(α+β) / (Γ(N+α+β)Γ(β)).
- Night only: logit p = −2.233 + 0.223·ln(N/100) over all months.
- Inverse with a flat prior and binomial likelihood: N − M ~ NegBin(M+1, p). For M = 0 this gives a median of 2 and a 90th percentile of 8, which is too narrow in practice.

## What this implies

- The team can say that roughly half of a monthly MODIS-versus-VIIRS disagreement at 50–100 km is what sampling whole fire-days would produce. No conversion factor can remove that part. In the box, most of the disagreement is change in the true ratio from month to month.
- A binomial (independent-hotspot) uncertainty band cannot be claimed. It covers less than half the time at 100 km and in the box. Beta-binomial bands are closer but still run about 10–15 points short of nominal.
- A MODIS-era zero at 50 km cannot be read as "no fire". About 40% of fire-season zero months had Suomi NPP hotspots, typically up to 4 and up to 27 at the extreme. At 100 km about 70% did, typically up to 9.
- Fire-season zeros at given N are roughly what clustered thinning predicts, which is within the interval below N = 10 and somewhat too high above it. The large excess of zeros over every model comes from off-season months, so a zero table should be split by season.
- One constant kept share is biased by month size within the fire season, in opposite directions by day and by night.

## Limits

- The shares of variance explained are shares of the observed scatter around a constant factor. That scatter includes any real change in the true ratio, and the shares depend on the 2 km, local-date grouping.
- Circle results pool 31 overlapping circles and rest on only 10 independent years.
- Months with M > N cannot be produced by any thinning model. Dropping them from the fits biases the kept share down in small months.
- The beta-binomial and size-slope fits in Evidence 2 are in-sample. The area-prior settings (moment fit on nine values, k clipped to 0.2–50) were not tuned.
- This analysis says nothing about the drift period after 2021 or about NOAA-20 and NOAA-21.

## How it was computed

The analyst's scripts `a03_tables.py`, `a03_thinning.py`, `a03_fit.py`, `a03_zeros.py`, `a03_zeros_cluster.py` and `a03_inverse.py` were re-run from a clean start and reproduce their saved tables exactly. The reviewer's independent recomputation is in `a03-thinning-model_review.py`. It uses great-circle circle membership, its own thinning draws and beta-binomial fits, the fire-season size fits, the seasonal zero table and the held-out check on N given M = 0. The inverse step on an integer grid with randomised probability integral transform coverage is in `a03-thinning-model_review_griddiag.py`. The outputs are in `out/a03-thinning-model_review_*.csv`.
