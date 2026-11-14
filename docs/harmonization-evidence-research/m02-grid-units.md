# Does counting active grid cells instead of pixels bring the sensors together?

## Answer

It closes most of the gap in level, but it reduces the year-to-year scatter only when day and night are counted separately. Over the fire seasons (April to October) of the stable-orbit period, 2012–2021, MODIS (Terra plus Aqua) records 0.24 hotspots for every Suomi NPP hotspot (yearly range 0.20–0.40). Counted as 2 km active cell-days, the ratio rises to 0.65 (yearly range 0.35–0.70), but the spread between years is about the same (coefficient of variation 0.21 for cell-days against 0.22 for pixels). The scatter comes from night passes. With daytime passes only, the 2 km cell-day ratio is 0.68, it ranges from 0.62 to 0.85 between years (coefficient of variation 0.10), and it does not depend on how active the year was. At night MODIS cell-days range from 0.08 to 0.61 of Suomi NPP's and track activity closely. Counting cells has costs: it squeezes big months (Suomi NPP's largest month falls from 62,646 pixels to 8,053 cell-days), and a union of two VIIRS satellites no longer adds up simply.

## Evidence

Terms used here:
- An **active cell-day** is a distinct pair of (grid cell, local date) with at least one hotspot. Cells come from a sinusoidal equal-area projection centred on the box (50.75°N, 120.25°W).
- A **fire day** is a local date with at least one hotspot.
- **Ratio** means the ratio of sums: the MODIS total divided by the Suomi NPP total over the months used.
- **CV** is the standard deviation of the 10 yearly ratios divided by their mean.
- **Slope** is the ordinary least-squares slope of log10(MODIS) on log10(SNPP) over months in which both are non-zero.

Months are keyed by local date. The 70 April–October months of February 2012 to December 2021 are used, less Aug and Sep 2020 (Aqua gap), which leaves 68 months for MODIS/SNPP. The intervals in brackets come from a bootstrap over the 10 years, resampling whole years so that months sharing a fire stay together. Rows of type 1–3 (volcano, static source, offshore) are excluded.

**Table 1. MODIS (Terra+Aqua) / Suomi NPP, April–October 2012–2021 (68 months; 1 month with a zero is dropped from slope and r)**

| Unit | Ratio [95% CI] | Yearly min–max | CV | Slope [95% CI] | r (logs) | Median monthly ratio |
|---|---|---|---|---|---|---|
| Pixels | 0.243 [0.238, 0.284] | 0.20–0.40 | 0.22 | 0.96 [0.91, 1.03] | 0.976 | 0.28 |
| 1 km cell-days | 0.616 [0.542, 0.632] | 0.34–0.64 | 0.21 | 1.06 [0.99, 1.14] | 0.967 | 0.50 |
| 2 km cell-days | 0.651 [0.555, 0.679] | 0.35–0.70 | 0.21 | 1.07 [0.99, 1.16] | 0.961 | 0.49 |
| 5 km cell-days | 0.645 [0.533, 0.689] | 0.35–0.72 | 0.23 | 1.06 [0.97, 1.17] | 0.954 | 0.48 |
| 10 km cell-days | 0.631 [0.518, 0.685] | 0.34–0.73 | 0.23 | 1.07 [0.96, 1.19] | 0.951 | 0.47 |
| 2 km cell-days, key includes day/night | 0.604 [0.540, 0.623] | 0.34–0.63 | 0.19 | 1.06 [0.98, 1.15] | 0.966 | 0.46 |
| Fire days, whole box | 0.668 [0.593, 0.729] | 0.45–0.79 | 0.17 | 1.17 [0.99, 1.54] | 0.809 | 0.64 |
| Fire days, 50 km around Kamloops (33 zero months dropped) | 0.45 [0.26, 0.66] | 0.12–0.86 | 0.61 | 0.71 [0.37, 0.97] | 0.669 | 0.50 |

Aqua alone against Suomi NPP: pixels 0.112 (yearly 0.11–0.21, CV 0.23); 2 km cell-days 0.407 (0.22–0.44, CV 0.25); 5 km 0.447 (CV 0.29). Aqua is further from VIIRS than Terra plus Aqua, and gridding does not tighten it either. With day and night counted together, the median monthly 2 km ratio (0.49) is well below the ratio of sums (0.65). The single factor is set by the big months and overstates a typical month by about a third.

**Table 2. Day and night separately, MODIS / Suomi NPP, April–October 2012–2021 (68 months; zero months dropped from the slope: 4 by day, 16 at night)**

| Unit | Ratio [95% CI] | Yearly min–max | CV | Slope [95% CI] | Median monthly ratio |
|---|---|---|---|---|---|
| Pixels, day | 0.339 [0.322, 0.430] | 0.31–0.59 | 0.20 | 0.89 [0.83, 0.93] | 0.42 |
| 2 km cell-days, day | 0.682 [0.665, 0.741] | 0.62–0.85 | 0.10 | 0.93 [0.85, 0.98] | 0.68 |
| 5 km cell-days, day | 0.722 [0.698, 0.738] | 0.56–0.83 | 0.10 | 0.92 [0.84, 0.98] | 0.72 |
| Fire days, day | 0.832 [0.785, 0.869] | 0.72–0.90 | 0.08 | 0.83 [0.68, 0.98] | 0.86 |
| Pixels, night | 0.184 [0.156, 0.191] | 0.04–0.19 | 0.31 | 1.08 [1.00, 1.14] | 0.13 |
| 2 km cell-days, night | 0.539 [0.333, 0.588] | 0.08–0.61 | 0.51 | 1.19 [1.05, 1.29] | 0.27 |

Across the 10 years, the correlation between the yearly 2 km ratio and log10 of Suomi NPP's yearly cell-days is 0.85 for day and night combined, −0.08 for day only and 0.94 for night only. Years with little fire (2012, 2020) have low combined ratios (0.37, 0.35) because MODIS barely detects small fires at night: its night ratios were 0.17 and 0.08 in those years. For daytime 2 km cell-days, the median month (0.68) equals the ratio of sums (0.68), so one factor describes a typical month as well as a big one.

**Table 3. Combining VIIRS satellites, 2 km cell-days, April–October 2018–2021 (28 months)**

| Comparison | Pixels | 2 km cell-days | Fire days |
|---|---|---|---|
| NOAA-20 / Suomi NPP | 0.99 (yearly 0.93–1.08) | 1.02 (1.00–1.03) | 1.00 |
| Union of SNPP and NOAA-20 / SNPP | 1.99 (1.93–2.08) | 1.23 (1.21–1.42) | 1.13 |

Suomi NPP and NOAA-20 count alike in every unit. Their pixels add up, so the union is about twice Suomi NPP. Cell-days overlap, so the union adds only 21–42% to Suomi NPP's count. The gain is larger in quiet years: 1.42 in 2020 and 1.21 in 2021. Across the 20 months with at least 20 Suomi NPP cell-days, the union-to-SNPP ratio has a median of 1.34 (range 1.08–1.70) and correlates −0.72 with log activity.

**Drift period.** These are April–October yearly ratios for 2022–2025, with months that overlap a gap in MODIS or Suomi NPP masked (Apr, Jul, Aug and Oct 2022 are masked). Daytime 2 km cell-days give 0.76, 0.69, 0.87 and 0.76, against a stable-period range of 0.62–0.85. Daytime pixels give 0.42, 0.32, 0.37 and 0.38 (stable 0.31–0.59). Aqua daytime 2 km cell-days give 0.54–0.64 (stable 0.44–0.62). Daytime fire days reach 0.92–0.97 in 2022–2024, above the stable maximum of 0.90, which is close to the ceiling. Only 2024 lies outside the stable range in any cell-day unit, and only just.

**What is lost.** Suomi NPP's largest month in April–October is 62,646 pixels, 8,053 2 km cell-days, 3,553 5 km cell-days and 31 fire days. The median month is 88 pixels, 43 cell-days and 17 fire days. The rank correlation of MODIS against Suomi NPP months falls from 0.96 for pixels to 0.94 for 2 km and 0.93 for 5 km cell-days, and to 0.87 for fire days. In 8 of 70 months Suomi NPP had fire on 28 or more days, so whole-box fire days are near their ceiling.

## What this implies for the approach

- **Unit.** Cell-days by themselves do not make the history more trustworthy. Daytime cell-days do, halving the year-to-year spread of the factor (CV 0.20 to 0.10). Grid size from 1 to 5 km changes little. At 10 km the correlation is a little lower and the interval wider, with no gain.
- **Scaling.** One factor works for daytime cell-days: the slope is just below 1, the median month matches the sum, and nothing depends on activity. At night no single factor works, because the ratio moves eightfold with activity. If night passes are used at all, they need their own factor, a curve, or a lower weight.
- **Target record.** Daytime cell-days put MODIS at about 0.68 of Suomi NPP, roughly 1.5 times apart rather than about 3 times for daytime pixels. Either direction of conversion is more stable in this unit than in pixels.
- **Combining VIIRS satellites.** In cell-days, do not take the union of satellites. It inflates the count by 21–42%, and more in quiet years. Counting each satellite separately and averaging keeps a factor of about 1.0 between them.
- **MODIS since 2022.** At yearly level, daytime cell-day ratios for 2022–2025 stay within or just above the stable range. This does not show that drift is harmless, but it gives no evidence for a separate drift-period factor in this unit.
- **Area size.** A 50 km circle is too small for per-sensor fire days: in 33 of 68 fire-season months, MODIS or Suomi NPP recorded no fire day.

## Limits

These are 10 years in one box, so each yearly range rests on 10 values, and the drift check rests on 4 years with 2022 thin (3 months). The cell-day ratio depends on how many distinct fires burn and how large they are. A user's smaller area will have fewer cells and noisier ratios, and this analysis did not test area sizes between the circle and the box. Near-real-time rows carry no type flag, so the current month cannot be cleaned of static and offshore sources the way the history was. In the standard data such rows number about 85 a year for Suomi NPP (1,202 in 2012–2025) and about 135 a year for NOAA-20. Keeping them changes the 2 km ratio little (0.651 to 0.647) but raises the slope from 1.07 to 1.14, and the fire-day slope from 1.17 to 1.49. The causes of MODIS's night shortfall (detection threshold, pass times) were not separated.

## How it was computed

- `scripts/m02_grid_units.py` is the analyst's script. It was re-run from a clean start, and its numbers reproduced.
- `scripts/m02-grid-units_review.py` is an independent recomputation. It uses a local-date month key, a sinusoidal equal-area grid, a year-block bootstrap and day/night splits, adds the VIIRS-union and drift checks, and writes `out/m02r_*.csv`. Its printed output is in `out/m02r_run.txt`, and it runs in about 6 minutes.
- `scripts/m02-grid-units_review_extra.py` computes the correlations with activity, the yearly union ratios and the type 2/3 row counts (`out/m02r_extra_run.txt`).
