# How much do pixel size and scan position matter?

## Answer

Scan position (where in the swath a fire was seen) has a real but modest effect on a single day. Over a month it adds no usable information. On the 110 stable-orbit days when Aqua passed over the box once and both Aqua and Suomi NPP recorded at least 20 daytime hotspots, the Aqua/Suomi NPP ratio was about 20% lower on the most off-nadir third of days than on the near-nadir third (median 0.22 against 0.28). A scan filter that keeps only near-nadir pixels (MODIS scan at or below 1.5 km, VIIRS at or below 0.5 km) throws away 37% of Aqua and 27% of Suomi NPP fire-season hotspots. It does not reduce the month-to-month spread of the MODIS/VIIRS ratio: for Aqua/Suomi NPP the standard deviation of the log ratio goes from 0.35 to 0.43 over 35 months (change +0.08, 95% interval −0.02 to +0.17). Summed pixel area is a noisier unit than counts (standard deviation 0.47 against 0.35). For a monthly calendar, a scan-based filter or weighting is not worth its cost.

## Evidence

All figures use the shared table without November 2026 (735,689 rows). The **stable-orbit period** is February 2012 to December 2021, and the **fire season** is April to October. A **log ratio** is ln(MODIS/VIIRS), so a standard deviation of 0.35 means a typical month sits about 35% away from the central ratio. An **overpass** is all hotspots from one satellite with no gap longer than 10 minutes between them (20,016 overpasses).

**1. Where in the swath hotspots fall (all years).** The scan value is the pixel's size across the track.

| Sensor | Hotspots | Median scan (5th–95th percentile), km | Share in scan bins |
|---|---|---|---|
| Terra | 50,990 | 1.3 (1.0–3.7) | ≤1.2: 45%; 1.2–1.5: 18%; 1.5–2: 14%; 2–3: 13%; >3: 9% |
| Aqua | 44,596 | 1.3 (1.0–3.7) | 46 / 17 / 14 / 13 / 10% |
| Suomi NPP | 306,399 | 0.44 (0.35–0.63) | ≤0.4: 33%; 0.4–0.5: 41%; 0.5–0.6: 18%; >0.6: 8% |
| NOAA-20 | 238,735 | 0.44 (0.35–0.63) | 32 / 39 / 21 / 8% |
| NOAA-21 | 94,969 | 0.44 (0.35–0.63) | 32 / 41 / 20 / 7% |

For MODIS, scan rises steadily from nadir to swath edge and tracks the along-track size closely (correlation 0.98 for Aqua). **For VIIRS it does not** (correlation 0.55). VIIRS combines detector samples in three zones across the swath, so the across-track size jumps back down at each zone boundary. Track (the along-track size) is the reliable position marker. 37% of the Suomi NPP hotspots kept by "scan ≤ 0.5 km" lie outside the nadir zone (track above 0.45 km). The drift period does not change the MODIS mix. In fire season, 2022–2026, 27–42% of Aqua hotspots per year had scan above 1.5 km, against 18–49% per year in 2003–2021.

**2. Daily Aqua/Suomi NPP ratio against scan position (stable orbit, daytime, UTC date; local and UTC dates agree for every daytime row).** There were 164 days with at least 20 hotspots from each sensor. 119 of them fall in 2017, 2018 and 2021, across 28 months, and no day was lost to outages.

| Subset | Days | Slope of log ratio per km of Aqua mean scan | 95% interval (resampling months) |
|---|---|---|---|
| All days | 164 | −0.17 | −0.26 to −0.08 |
| All days, controlling for log Suomi NPP count | 164 | −0.09 | −0.18 to 0.00 |
| Days with one Aqua overpass | 110 | −0.57 | −0.95 to −0.20 |
| Same, controlling for log Suomi NPP count | 110 | −0.58 | −0.87 to −0.26 |
| Suomi NPP mean scan, all days | 164 | −0.34 | −1.16 to +0.44 |

Two things are mixed in the all-days slope. On the 54 days with two Aqua overpasses, Aqua saw the box from both swath edges (mean scan 2.5 km, against 1.2 km on one-pass days) and counted it twice. Off-nadir days were also busier fire days (median Suomi NPP count 249, against 138 on near-nadir days). On one-pass days, by thirds of Aqua mean scan:

| Third | Days | Aqua mean scan, km | Median ratio (interquartile range) | Pooled ratio (sum/sum) |
|---|---|---|---|---|
| Near nadir | 37 | 1.02 | 0.28 (0.20–0.36) | 0.23 |
| Middle | 36 | 1.15 | 0.25 (0.20–0.31) | 0.23 |
| Off nadir | 37 | 1.39 | 0.22 (0.17–0.26) | 0.19 |

Suomi NPP's daily mean scan hardly varies (standard deviation 0.05 km). One standard deviation of it moves the log ratio by −0.02 (interval −0.08 to +0.04), so a Suomi NPP effect cannot be detected here.

**3 and 4. Monthly ratio with scan filters and with pixel area.** These are stable-orbit fire-season months (70). Two months are dropped for the Aqua outage of 16 August to 2 September 2020. Months with fewer than 10 hotspots in any of the four series (MODIS and VIIRS, filtered and unfiltered) are also dropped, so filtered and unfiltered use the same months. The median ratio is a median of monthly ratios, and the pooled ratio is the sum of MODIS over the sum of VIIRS.

| Pair, time of day | Months | Unit, variant | Median (pooled) ratio | SD of log ratio | Log-log slope | Range of yearly ratios |
|---|---|---|---|---|---|---|
| Aqua/Suomi NPP, all | 35 | counts | 0.130 (0.111) | 0.35 | 0.93 | 0.11–0.21 |
| | | counts, filtered | 0.118 (0.096) | 0.43 | 0.90 | 0.08–0.20 |
| | | pixel area | 1.15 (1.11) | 0.47 | 0.96 | 0.66–1.93 |
| | | area, filtered | 0.76 (0.64) | 0.47 | 0.89 | 0.53–1.35 |
| Aqua/Suomi NPP, day | 31 | counts | 0.214 | 0.42 | 0.87 | 0.19–0.33 |
| | | counts, filtered | 0.188 | 0.53 | 0.86 | 0.15–0.31 |
| Terra+Aqua/Suomi NPP, all | 42 | counts | 0.279 | 0.33 | 0.94 | 0.18–0.41 |
| | | counts, filtered | 0.242 | 0.38 | 0.92 | 0.19–0.42 |
| Terra+Aqua/Suomi NPP, night | 26 | counts | 0.146 | 0.36 | 1.09 | 0.10–0.19 |
| | | counts, filtered | 0.148 | 0.29 | 1.04 | 0.12–0.19 |

- Changes in the SD of the log ratio under the filter (resampling months 2,000 times, 95% intervals): Aqua all +0.08 (−0.02 to +0.17), Aqua day +0.12 (−0.02 to +0.27), Aqua night −0.05 (−0.15 to +0.07), Terra+Aqua day +0.14 (+0.03 to +0.26), Terra+Aqua night −0.08 (−0.13 to −0.01). Only the night subsets ever improve.
- The added spread is not just from having fewer hotspots. After subtracting the counting (Poisson) part, the remaining SD still rises, from 0.31 to 0.38 for Aqua/Suomi NPP. The filter's cost also varies widely by month: across the 41 months with at least 10 Aqua hotspots, it discarded between 8% and 63% of them (5th–95th percentile).
- A filter that really selects the VIIRS nadir zone (track ≤ 0.45 km) discards 46% of Suomi NPP hotspots and still does not reduce the spread (Aqua all: 0.35 to 0.37, change interval −0.08 to +0.12).
- Keeping every month with at least 1 hotspot (59 Aqua months) gives the same picture: SD 0.46 unfiltered and 0.60 filtered.
- These SDs depend heavily on single months. Daytime September 2012 (Aqua 17 against Suomi NPP 13) alone moves the Aqua daytime SD between about 0.29 and 0.42.

**5. Same-overpass neighbours (all years).** This is the share of hotspots that have another hotspot from the same overpass within half a pixel width. Width is the larger of scan and track. A neighbour that close means the two footprints overlap by more than half, which is a proxy for duplicates. The share within one width also includes ordinary adjacent pixels.

| Bin | Terra | Aqua | | VIIRS bin (track) | Suomi NPP | NOAA-20 | NOAA-21 |
|---|---|---|---|---|---|---|---|
| scan ≤1.2 km | 2% | 2% | | ≤0.45 km (nadir zone) | 10% | 9% | 8% |
| 1.2–1.5 | 16% | 15% | | 0.45–0.65 | 32% | 33% | 30% |
| 1.5–2 | 31% | 32% | | 0.65–0.9 | 43% | 45% | 49% |
| 2–3 | 53% | 51% | | | | | |
| >3 | 81% | 78% | | | | | |
| All, ≤0.5 width (≤1 width) | 23% (68%) | 22% (66%) | | All | 22% (80%) | 22% (80%) | 20% (80%) |

## What this implies for the approach

- **Target record:** scan position does not favour either target. Both records carry overlap duplication of a similar overall size (about 21–23% of hotspots at half a pixel width), concentrated at the swath edges.
- **Unit:** do not use summed pixel area. It is noisier than counts and it gives the most weight to the duplicated edge-of-swath MODIS pixels. A unit that merges neighbouring detections, such as active grid cells per day, removes overlap duplicates without dropping data. The analyst's cluster test made the spread tighter (SD 0.30 against 0.37 over 40 months), which this review did not re-derive independently.
- **Scaling:** no scan filter or weighting. The single-day effect (about 20% across thirds) averages out within a month, and filtering adds spread. The log-log slope stays below 1 by day (0.87–0.94) and above 1 by night (1.04–1.09) with or without the filter. That supports separate day and night factors, or a curve, more than a single factor.
- **Combining VIIRS satellites:** all three VIIRS satellites have the same swath-position mix and the same neighbour rates, so swath geometry gives no reason to weight them differently.
- **MODIS since 2022:** the share of off-nadir MODIS hotspots in 2022–2026 stays within its earlier year-to-year range, so the drift brings no new scan-position correction.

## Limits

The daily analysis rests on 164 days, nearly three-quarters of them in three large fire years. It cannot separate swath position from fire size, smoke or the time between overpasses. Swath coverage of the box is not known, so a pass whose edge cut through the box could not be identified. The half-width neighbour share is a proxy for duplicates, and about 9% of VIIRS nadir-zone hotspots still have such a neighbour, which this analysis does not explain. All monthly statistics are for the whole box. A small user-selected area will have more low-count months, where counting noise dominates.

## How it was computed

- The analyst's script `scripts/m06_scan.py` was re-run from a clean start. Its output matched its saved log exactly.
- The independent check is `scripts/m06-scan-angle_review.py`, with its log in `out/m06-scan-angle_review_log.txt` and tables in `out/m06-scan-angle_review_*.csv`.
- It drops November 2026 and builds 10-minute overpasses.
- It counts daytime Aqua and Suomi NPP hotspots per day, fits a least-squares line to the log ratio and bootstraps it by day and by month.
- It totals months with outage masking and a minimum of 10 hotspots, and also a minimum of 1.
- It compares scan-filtered, track-filtered and pixel-area variants, with month-resampled intervals for the change in SD.
- It finds each hotspot's nearest same-overpass neighbour on a flat projection centred on that overpass.
