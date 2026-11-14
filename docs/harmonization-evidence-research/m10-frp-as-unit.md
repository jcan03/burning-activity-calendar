# Is fire radiative power a better common unit than counts?

## Answer

No, not overall. Monthly summed fire radiative power (frp, the radiant heat output of the fire in a pixel, in megawatts) is not a more stable bridge between MODIS and Suomi NPP than hotspot counts. The data cover the stable-orbit period (February 2012 to December 2021) for the April to October fire season. With day and night pooled, a single factor fitted on the other years predicts MODIS (Terra plus Aqua) monthly values from Suomi NPP with a median error of 29% for counts and 38% for frp. The root-mean-square log error is 0.50 for counts and 0.66 for frp, from 67 months over 10 years. frp did worse in 99% of year-block bootstrap resamples. Almost all of the gap comes from night. For daytime alone, the two units cannot be told apart (RMSE log 0.63 for counts and 0.60 for frp; frp worse in only 36% of resamples). At night, frp is much worse (1.09 against 0.72). frp has one appealing property: daytime Aqua frp roughly equals daytime Suomi NPP frp (ratio 1.01, year range 0.62 to 1.17), while the count ratio is 0.20. That is a matter of scale, not of stability.

## Evidence

**Data used.** Standard-stream rows only (every stable-period row is standard). I removed 2,804 rows of type 1 to 3 (volcano, static source, offshore). Months were keyed by UTC `ym`. I masked months that overlap an outage `gap`: Terra 2016-02 and Aqua 2020-08 and 2020-09. Suomi NPP has no gap in this period, and no `partial` outage falls in it. A month was dropped when either side had zero hotspots, because a ratio cannot be formed. The same months were dropped for both units. The interval for each RMSE difference is a bootstrap over whole years (4,000 resamples).

**Table 1. MODIS against Suomi NPP, monthly sums, April to October 2012 to 2021**

| Target, period of day (months used of 68 to 70) | Unit | Ratio of sums | Year-to-year range | Year CV | SD of log monthly ratio | Leave-one-year-out RMSE log (median % error) | frp minus counts RMSE, 95% interval |
|---|---|---|---|---|---|---|---|
| Terra+Aqua, all (67) | counts | 0.242 | 0.19–0.40 | 0.23 | 0.50 | 0.50 (29%) | |
| | frp | 1.80 | 0.94–1.92 | 0.23 | 0.55 | 0.66 (38%) | +0.03 to +0.27 |
| Terra+Aqua, day (64) | counts | 0.339 | 0.31–0.59 | 0.20 | 0.56 | 0.63 (29%) | |
| | frp | 1.50 | 0.99–1.63 | 0.16 | 0.56 | 0.60 (33%) | −0.19 to +0.12 |
| Terra+Aqua, night (52) | counts | 0.184 | 0.03–0.19 | 0.32 | 0.61 | 0.72 (46%) | |
| | frp | 2.89 | 0.42–4.22 | 0.60 | 0.82 | 1.09 (147%) | +0.23 to +0.51 |
| Aqua, all (62) | counts | 0.112 | 0.11–0.21 | 0.23 | 0.58 | 0.61 (30%) | |
| | frp | 0.93 | 0.54–1.05 | 0.23 | 0.60 | 0.69 (43%) | −0.16 to +0.29 |
| Aqua, day (61) | counts | 0.201 | 0.19–0.32 | 0.16 | 0.65 | 0.69 (28%) | |
| | frp | 1.01 | 0.62–1.17 | 0.23 | 0.62 | 0.70 (46%) | −0.21 to +0.19 |
| Terra, day (63) | counts | 0.139 | 0.12–0.27 | 0.28 | 0.67 | 0.76 (34%) | |
| | frp | 0.49 | 0.27–0.74 | 0.29 | 0.80 | 0.81 (53%) | −0.10 to +0.21 |
| Terra, night (50) | counts | 0.126 | 0.07–0.14 | 0.18 | 0.52 | 0.55 (29%) | |
| | frp | 2.25 | 0.89–3.49 | 0.48 | 0.78 | 0.95 (99%) | +0.29 to +0.54 |

Here CV is the coefficient of variation of the yearly ratios (their standard deviation divided by their mean). The log-log slope of MODIS on Suomi NPP is between 0.89 and 1.11 in every row, with 0.96 for counts and 1.05 for frp in the Terra+Aqua all-hours row. So one multiplicative factor is an adequate form in both units. The table at all calendar months is in `out/m10-frp-as-unit_review_bridge.csv`. Using all months makes frp look worse still: 112 months, RMSE log 0.60 for counts against 0.83 for frp.

**Well-populated months.** This keeps only months where both sides had at least 30 hotspots (Terra+Aqua, 32 months). Counts still win (RMSE log 0.30 against 0.44; interval of the difference +0.02 to +0.25). For daytime alone at this threshold the gap is not resolved (Terra+Aqua 0.32 against 0.36, interval −0.11 to +0.16). For Aqua daytime counts are better (0.24 against 0.41, interval +0.05 to +0.29).

**Night is time-of-day sensitive in frp.** Terra's frp ratio to Suomi NPP is 0.49 by day and 2.25 by night, a factor of 4.6. Terra's count ratio is 0.14 by day and 0.13 by night. Terra's night pass, at about 22:30 local time, sees evening fires that are more intense than at Suomi NPP's 01:30 pass. Counts are almost insensitive to this, but frp is not.

**Per-hotspot frp (stable period, MW, median / 99th percentile).** Terra day 41.8 / 1,092, night 30.8 / 1,097. Aqua day 49.7 / 1,718, night 24.6 / 564. Suomi NPP day 12.8 / 265, night 2.4 / 45. NOAA-20 (2018–2025) has a median of 4.2 and NOAA-21 (2023–2025) a median of 4.7, against 4.4 for Suomi NPP over all hours. A MODIS hotspot is a coarse pixel that holds several VIIRS-sized fire pixels, so per-hotspot values are not comparable. Only sums are.

**Scan dependence.** Spearman rank correlation of frp with scan width is 0.45 for Terra, 0.47 for Aqua and 0.14 for Suomi NPP. The median frp per hotspot goes from the narrowest-scan eighth of pixels to the widest-scan eighth as follows: Terra 20 to 93 MW, Aqua 22 to 116 MW, Suomi NPP 3.6 to 6.9 MW. Dividing MODIS frp by pixel area removes the trend (correlation −0.07 for Terra and −0.03 for Aqua). The per-hotspot rise is therefore pixel size, not a retrieval bias. What it means for summed frp over a fixed area was not tested.

**Zero and missing VIIRS frp.** No row is missing. Zero frp appears in 0.16% of Suomi NPP rows, 0.22% of NOAA-20 rows and 0.37% of NOAA-21 rows. Nearly all of these are daytime pixels at the 367 K saturation value. For Suomi NPP there were 0 zeros in 10,740 rows in 2012 to 2014 and 284 in 188,677 rows (0.15%) in 2015 to 2021. At the later rate, about 16 zeros would be expected in 2012 to 2014 (Poisson probability of none: 1e-7). So the zero behaviour did change, which is consistent with the 2015 M13 change. I tested whether the frp split itself differed by measuring the share of rows that carry exactly the same frp as another pixel in the same granule. That share is 51% in 2012 to 2014 and 76% in 2015 to 2021, but it is just as low in the later small-fire years (45 to 53% in 2016, 2019 and 2020). It follows fire size, so it gives no evidence that the split method changed. The zeros are too few to move monthly sums materially.

**Top 1% of hotspots.** This covers April to October months with at least 100 hotspots. The top 1% supply a median 11.7% of the monthly frp sum for Suomi NPP (33 months, 10th to 90th percentile 7.6–21.1%, maximum 28%) and 13.2% for Terra+Aqua (24 months, 6.7–22.0%, maximum 27%). Removing them changes the Terra+Aqua frp ratio from 1.803 to 1.800 and the SD of the log ratio from 0.354 to 0.340 (analyst's computation, reproduced). So extreme hotspots are not the main source of instability. In a month with fewer than 100 hotspots, the "top 1%" is a single hotspot.

## What this implies for the approach

- **Unit.** Counts are at least as good a bridge as frp in every combination tested, and clearly better whenever night is included. frp is defensible only as a daytime-only unit, and even there it gains no stability.
- **Scaling.** If frp is used, it needs separate day and night factors at a minimum. A single pooled frp factor mixes night ratios that vary 10-fold between years. A curve is not needed, because the slopes are near 1.
- **Target record.** frp's main attraction is that daytime Aqua and Suomi NPP are already on the same scale (ratio about 1.0). A VIIRS-equivalent target would then need little rescaling for Aqua daytime. That convenience does not reduce error.
- **Combining VIIRS satellites.** Per-hotspot frp distributions of NOAA-20 and NOAA-21 are close to those of Suomi NPP. This does not test a bridge. NOAA-21 has the highest zero-frp share (0.37%).
- **MODIS since 2022.** Terra's frp ratio changes 4.6-fold between its 22:30 night pass and Suomi NPP's 01:30 pass, while its count ratio barely changes. This suggests, without directly testing it, that the orbit drift will shift a frp bridge more than a count bridge.
- **Small user areas.** Both units degrade sharply in months with few hotspots. frp also degrades more there, because a few pixels carry most of the sum.

## Limits

The study area is one box, and the spread rests on 10 fire seasons dominated by 2017, 2018 and 2021, so the intervals are rough. MODIS overlap duplicates were kept. They inflate both units, so ratios include them. Months are keyed by UTC. 690 Terra night rows (2.7% of Terra rows and 2.1% of Terra frp) fall in a different local-solar month and were not moved. No drift-period bridge was fitted. NOAA-20 and NOAA-21 were not bridged to MODIS. The effect of the M13 change on frp magnitude cannot be separated from fire mix.

## How it was computed

`scripts/m10_main.py` is the analyst's script. I re-ran it, and it reproduced every number in the draft. `scripts/m10-frp-as-unit_review.py` is my independent recomputation. It builds monthly counts and frp sums per sensor (and per day or night) from rows of type 0 or empty, masks gap months and zero months, and computes the ratio of sums, the yearly ratios, the log-ratio SD, the slope and the leave-one-year-out error. It also bootstraps the frp-minus-counts error difference over years, and checks zero frp, the equal-split pattern, the UTC and local month slip, the top-1% share and scan dependence. Its output tables are in `out/m10-frp-as-unit_review_*.csv`.
