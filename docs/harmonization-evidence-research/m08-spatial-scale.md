# Does the relationship hold for the size of area a user would select?

## Answer

Only for large areas. Pooled over the April to October fire seasons of February 2012 to December 2021, the MODIS (Terra plus Aqua) to Suomi NPP count ratio is about 0.25 from 50 km radius upward. The year-to-year spread is still a factor of about 1.7 at 100 km radius (one circle-year in ten is below 0.22, one in ten above 0.38). At 25 km and below, 7 to 53% of circle-years have no Suomi NPP hotspot at all, so a ratio is not defined. A monthly count scaled by one factor matches the real MODIS count within a factor of 1.5 in about 70% of busy months at 100 km radius and 67% at 50 km. The five-class anomaly scheme agrees between sensors far better than chance wherever it can be computed, but at 50 km radius and below the calendar-month MODIS median is zero for most fire-season months, so the scheme is undefined there. The relationship also differs by a factor of about 1.8 between day and night passes. A user's circle of "tens of kilometres" falls below the size at which either approach holds.

## Evidence

Terms. A **circle-year** is one circle's April to October total in one year. **Busy month**: a fire-season month with at least 10 MODIS hotspots. **Shuffled baseline**: the agreement obtained when each VIIRS month is paired with the same calendar month of a different year (20 random year permutations). It shows what agreement would happen by chance.

Setup: 31 circles per radius (Kamloops plus 30 random centres, each circle fully inside the box), 119 UTC months, with February 2016 masked (Terra gap 18–24 Feb; the only outage in the period). That leaves 118 months, 70 of them in the fire season. All rows are standard (science-quality) data. 794 rows of type 1 to 3 were removed (static sources and offshore). Zero months are kept unless stated. Values are medians across the 31 circles, with the minimum and maximum in brackets.

| Radius (area) | Both sensors zero, fire season | VIIRS-only months (MODIS 0, SNPP >0) | P(MODIS 0 given SNPP >0) | MODIS-only months |
|---|---|---|---|---|
| 10 km (314 km²) | 0.91 | 0.04 [0–0.40] | 0.50 [0–1] | 0.00 [0–0.04] |
| 25 km (1,960 km²) | 0.69 | 0.10 [0.01–0.51] | 0.36 [0.06–0.72] | 0.03 [0–0.10] |
| 50 km (7,850 km²) | 0.27 | 0.23 [0.07–0.43] | 0.33 [0.17–0.49] | 0.06 [0–0.11] |
| 100 km (31,400 km²) | 0.03 | 0.16 [0.10–0.23] | 0.16 [0.10–0.24] | 0.01 [0–0.09] |
| 150 km (70,700 km²) | 0.00 | 0.06 [0.01–0.09] | 0.06 [0.01–0.09] | 0.00 |

| Radius | Fire-season ratio across circles | Circle-years p10 / p50 / p90 (undefined share) | Day ratio | Night ratio | Spearman, fire season | Busy months within ×1.5 (n per circle) |
|---|---|---|---|---|---|---|
| 10 km | 0.28 [0.00–1.00] | 0.00 / 0.12 / 0.58 (53%) | 0.40 | 0.17 | 0.70 [−0.02–1.00] | not testable (n = 1) |
| 25 km | 0.25 [0.15–0.37] | 0.00 / 0.27 / 0.62 (7%) | 0.37 | 0.18 | 0.77 [0.45–0.93] | 0.60 [0–1] (5) |
| 50 km | 0.25 [0.19–0.29] | 0.18 / 0.27 / 0.42 (0%) | 0.35 | 0.19 | 0.79 [0.69–0.85] | 0.67 [0.38–1] (15) |
| 100 km | 0.24 [0.23–0.26] | 0.22 / 0.27 / 0.38 (0%) | 0.32 | 0.19 | 0.89 [0.83–0.95] | 0.70 [0.56–0.80] (26) |
| 150 km | 0.25 [0.24–0.25] | 0.22 / 0.27 / 0.37 (0%) | 0.34 | 0.19 | 0.95 [0.94–0.97] | 0.78 [0.69–0.83] (38) |

For the Kamloops circle, a bootstrap over the 10 years (2,000 draws) gives a 95% interval for the pooled ratio of 0.23–0.31 at 100 km and 0.23–0.30 at 50 km. The "within ×1.5" column uses a single fire-season factor estimated with the test year left out.

| Radius | Fire-season months where the anomaly class can be computed (of 70) | Exact class agreement | Shuffled baseline | Within one class | Shuffled baseline | Months/year with ≥10 MODIS: Apr–Oct, Nov–Mar |
|---|---|---|---|---|---|---|
| 10 km | 0 | not meaningful | – | – | – | 0.1, 0.0 |
| 25 km | 10 | 0.60 (n = 10) | 0.23 | 0.90 | 0.41 | 0.5, 0.3 |
| 50 km | 30 | 0.57 [0.33–0.83] | 0.24 | 0.80 | 0.41 | 1.5, 1.0 |
| 100 km | 70 | 0.59 [0.47–0.72] | 0.21 | 0.84 [0.76–0.91] | 0.43 | 2.6, 1.9 |
| 150 km | 70 | 0.73 [0.66–0.80] | 0.20 | 0.93 [0.90–0.94] | 0.45 | 3.8, 2.5 |

Further findings:
- **The ratio depends on the level of activity at large radii.** At 100 and 150 km, the ratio is 0.35–0.37 in a circle's quietest third of fire-season months and 0.24 in its busiest third. As a result, the mean of monthly ratios (0.32) exceeds the ratio of totals (0.24). At 50 km it is flat (0.22 to 0.25).
- **November is a busy burning month outside the defined fire season.** It has at least 10 MODIS hotspots in 9 of 10 years at 50 km and in 10 of 10 years at 100 km. Its ratio (0.25–0.26 median) matches the fire-season ratio.
- **One unflagged persistent source dominates the small Kamloops circle.** 93 of the 151 Suomi NPP hotspots within 10 km of Kamloops fall in one 0.01° cell (50.69°N, 120.41°W) across 31 months. No MODIS hotspots fall there, and the cell has no static-source type. Removing it raises the Kamloops 10 km ratio from 0.08 to 0.21 and cuts its VIIRS-only months from 40% to 6%.
- **Robustness checks.** Using local-date months instead of UTC months changes no ratio at the third decimal. Reusing one centre set (valid at 50 km) at 10 and 25 km changes shares by no more than 0.05 and leaves the conclusions unchanged.

## What this implies for the approach

- **Target record.** MODIS is silent in 16–50% of the months in which Suomi NPP saw fire, for circles of 10–100 km. A VIIRS-to-MODIS mapping therefore loses information at user scales. Mapping MODIS history up to VIIRS-equivalent cannot create the missing detections either. At small areas the target choice matters less than whether any harmonized history can be shown at all.
- **Unit.** Raw counts give a stable long-run factor only from about 50 km radius. Anomalies against each sensor's own history agree 2.5 to 3.5 times more often than chance, which supports anomalies as the unit. However, they need a non-zero calendar-month median, which holds for all fire-season months only from about 100 km radius.
- **Scaling.** If one factor is used, it should differ for day and night (about 0.34 and 0.19). A curve or a factor by activity level is supported at 100 km and above. A factor by season adds little, since November matches the summer ratio.
- **Smallest reliable areas, by this evidence.** Count scaling is reliable from about 100 km radius, which still leaves roughly 30% of busy months off by more than ×1.5. It is marginal at 50 km. The anomaly approach is defined for all fire-season months from about 100 km, and for July to September only at 50 km.
- **Below about 50 km.** The data support showing no MODIS-era class for a user's circle. Alternatives consistent with the data are the anomaly of an enclosing circle of about 100 km, a seasonal or annual period instead of a month, presence or absence only, or the Suomi NPP-era record (2012 onward) alone.
- **Persistent sources.** Small circles near towns need a persistent-source mask beyond the FIRMS `type` field.
- **Combining VIIRS satellites and MODIS since 2022.** This analysis does not address either. More VIIRS satellites would reduce VIIRS-only zeros, but not MODIS zeros.

## Limits

- Suomi NPP is the only VIIRS satellite here, and the period is the stable-orbit period only. Nothing here covers NOAA-20/21 or the drift period.
- The 100 and 150 km circles overlap heavily, because a 150 km circle fits only in a strip about 0.25° of longitude wide. The spread across circles at these sizes is not independent and is understated.
- Anomaly medians are in-sample from the same 10 years. At 25 and 50 km, agreement is computed only on the months that survive the zero-median exclusion.
- The busy-month test uses a threshold of 10 MODIS hotspots and has few months per circle below 100 km.
- Fire radiative power and active-cell units were not tested.
- The persistent Kamloops source was not identified, and other circles were not screened for such sources.

## How it was computed

The analyst's script, `scripts/m08_spatial_scale.py`, was re-run from a clean start and reproduced every number in its draft. An independent review script, `scripts/m08-spatial-scale_review.py`, rebuilds the circles with the same seed rule and counts monthly hotspots by great-circle distance. It then adds the following: the conditional silence share, day and night ratios, local-month and nested-centre checks, the shuffled-year anomaly baseline, the leave-one-year-out monthly scaling test, ratios by activity tercile, November, and the Kamloops persistent cell. Outputs are in `out/m08-spatial-scale_review_per_circle.csv`, `out/m08-spatial-scale_review_summary.csv` and `out/m08-spatial-scale_review_extra.csv`.
