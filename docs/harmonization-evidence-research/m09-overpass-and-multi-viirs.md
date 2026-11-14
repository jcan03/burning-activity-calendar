# How many looks per day does each sensor get here, and how should several VIIRS satellites be combined?

## Answer

On the busiest 5% of days, each VIIRS satellite has detections in about two passes over the whole box in daytime (around 12:40 local solar time) and two at night (around 02:10). Terra and Aqua each have about 1.3 in daytime and 0.8 to 1.3 at night. Two passes of the same satellite are one orbit apart, about 100 minutes. A single 10 km area gets fewer looks: about 1.4 per half-day from a VIIRS satellite and 1.1 from a MODIS sensor. Summed over the satellites flying, the box gets about 1.8 detecting passes per day with Terra only, 4.7 with Terra and Aqua, 8.1 with Suomi NPP added, 12.6 with NOAA-20 and 16.4 with NOAA-21. VIIRS hotspot counts add up with the number of satellites: two satellites give 1.99 times the Suomi NPP count and three give 2.95 times. Active 5 km cell-days grow only 1.24 and 1.37 times, because 64 to 69% of them are seen by more than one satellite. The most consistent combined series is a mean of the satellites that have data on each day, scaled to Suomi NPP and summed over the month. Its departure from its own complete-month value is under 1% in the median and at most 11% (90th percentile) in simulated outages.

## Evidence

**Detecting passes per high-activity day.** A high-activity day is a local date at or above the 95th percentile of total hotspots across all sensors in its era. That gives 32 to 178 days per era. Days on which a sensor detected nothing count as zero. A pass is a run of one sensor's detections with no gap over 30 minutes in time. Day and night were split by local solar hour (06 to 18); this matches the `daynight` label for more than 99.9% of rows. The intervals are bootstrap 95% intervals over days.

| Sensor (eras) | Day passes | Night passes | Day / night local solar hour | Per 10 km cell, day / night (E4–E5) |
|---|---|---|---|---|
| SNPP, NOAA-20, NOAA-21 (2012–2026) | 1.81–1.88 (CI about 1.7–1.94), median 2 | 1.82–1.91, median 2 | 12.6–12.75 / 2.2–2.3 | 1.39–1.42 / 1.43–1.47 |
| Terra, stable orbit (2002–2023) | 1.34–1.38 | 0.95–1.21 | 11.2–11.3 / 21.7–21.8 | 1.08–1.09 / 1.12–1.14 |
| Aqua, stable orbit (2002–2023) | 1.31–1.42 | 0.76–1.21 | 12.9 / 2.2 | 1.10–1.12 / 1.07–1.08 |
| Terra, drifted (Mar 2023–Oct 2026, 67 days) | 1.28 | 1.30 | 10.0 / 20.6 | — |
| Aqua, drifted (same days) | 1.31 | 1.30 | 14.0 / 3.5 | — |

- The median spacing between two passes of the same sensor in the same half-day is 98 to 100 minutes, which is one orbit.
- Aqua's night count rose from 0.76–0.81 before 2018 to 1.2–1.3 after. Aqua itself did not change: in fire-season nights with 10 or more Aqua hotspots, it had 1.3 to 1.4 passes in every period. The high-activity days after 2018 simply had bigger fires.
- Totals by era: 1.81, 4.65, 8.06, 12.63 and 16.39 passes per day. With Suomi NPP removed from the last era the total is about 12.7 (by subtraction).

**VIIRS counts against the number of satellites.** These are fire-season months (April to October) in which every satellite involved was complete, meaning no `gap` or `partial` overlap in the outage list. Nine 2018–2026 months were dropped as outages.

| Ratio (months) | Ratio of sums (bootstrap 95%) | Range across years | Median month (p10–p90) |
|---|---|---|---|
| (SNPP+N20)/SNPP, 2018-04..2026-10, both ≥100 (32) | 1.99 (1.94–2.02) | 1.93–2.13 | 1.97 (1.77–2.16) |
| (SNPP+N20+N21)/SNPP, 2023-04..2026-10, all ≥100 (14) | 2.95 (2.78–3.08) | 2.81–3.13 | 2.90 (2.69–3.12) |
| NOAA-21/SNPP, same (14) | 0.97 (0.90–1.00) | 0.83–0.99 | 0.91 (0.89–1.02) |

When small months are kept (all 54 non-zero months), the ratio of sums stays at 1.99, but the mean of the monthly ratios rises to 2.09. Low-count months make single-month ratios noisy.

**Combination rules at the boundaries.** The table gives monthly hotspot counts.

| Month | SNPP / N20 / N21 | Mean | Max | Reference (SNPP) |
|---|---|---|---|---|
| 2018-04 (NOAA-20 starts) | 77 / 110 / – | 93.5 (+21%) | 110 (+43%) | 77 |
| 2023-03 (NOAA-21 from day 2) | 94 / 103 / 111 | 102.7, or 98.5 without NOAA-21 | 111 | 94 |
| 2026-11 (SNPP ends 2 Nov; partial month, excluded) | 48 / 729 / 682 | 486 if SNPP is still averaged in | 729 | none |

**Simulated outages, which have a known truth.** The test used 17 clean two-satellite months and 15 clean three-satellite months, all with Suomi NPP at 100 or more hotspots. In each month, L consecutive days of Suomi NPP were deleted, at every possible start day. Each rule's result was then compared with the same rule on the full month. The table gives the median absolute departure, with the 90th percentile in brackets, in percent, for the 2-satellite and 3-satellite configurations.

| Rule | 3-day gap | 8-day gap | 20-day gap |
|---|---|---|---|
| Naive mean (keeps the partial satellite) | 2.0 (12) / 1.2 (11) | 11 (32) / 5.1 (25) | 37 (48) / 26 (34) |
| Mean of satellites complete that month | 3.3 (17) / 2.5 (5.9) | same | same |
| Daily mean of satellites with data, scaled | **0.3 (1.7) / 0.2 (1.5)** | **0.7 (3.4) / 0.5 (2.4)** | **2.1 (11) / 1.6 (4.7)** |
| Max | 0.7 (7.8) / 0.3 (5.2) | 1.8 (13) / 1.7 (8.3) | 3.4 (17) / 1.9 (11) |
| Reference with monthly fallback | 6.0 (28) / 12 (24) | same | same |
| Reference with daily fallback | 0.6 (3.4) / 0.6 (4.9) | 1.4 (6.8) / 1.7 (12) | 4.2 (20) / 4.9 (21) |

With no gap, the mean is 3–5% from the complete Suomi NPP month in the median, and up to 10–12% at the 90th percentile. That is satellite-to-satellite noise. The max is 0% in the median but 6% (2 satellites) and 18% (3 satellites) at the 90th percentile, so its upward bias grows with each added satellite.

**Real Suomi NPP outage months.** The naive mean is 418 against NOAA-20's 603 in July 2022, and 1613 against 2199 in August 2022. That is roughly 30% too low. The daily scaled mean gives 630 and 2264. The listed outages overstate some gaps. Suomi NPP has 943 to 2366 hotspots per day on 4–6 August 2026, which are listed as gap days. In July 2026 the eight flagged days held only about 2% of the month's fire: Suomi NPP had 18,105 hotspots against NOAA-20's 17,815. A month-level rule nonetheless discards the whole Suomi NPP month.

**Same cell and date.** This uses 5 km cells and local dates, and drops days within one day of a listed outage.

| Configuration | Cell-days | Seen by 2 or more satellites (range across years) | All three | Union / SNPP cell-days |
|---|---|---|---|---|
| SNPP+N20, 2018-04..2023-03, 1132 days | 17,370 | 64% (37–71%) | – | 1.24 |
| All three, 2023-03..2026-10, 921 days | 11,257 | 69% (61–74%) | 49% | 1.37 |

## What this implies for the approach

- **Combining VIIRS satellites.** Combine per day, then sum to the month. Each day, average the satellites that have data, after scaling each to Suomi NPP: NOAA-20 ×1.011 and NOAA-21 ×1.034, from clean fire-season months. This avoids the naive mean's 30% collapse in outage months. It also avoids the max's bias, which grows with each satellite, and the reference rule's 6–12% error in fallback months. It needs a daily availability flag. The outage list alone is imperfect, so a check in the data (zero hotspots while the other satellites see fire) would help.
- **Unit.** Raw counts scale with the number of satellites, but cell-days do not. A union of cell-days across satellites steps up by 1.24 and then 1.37 times at the 2018 and 2023 boundaries, so any cell-based unit should be computed per satellite and then averaged.
- **Target record.** VIIRS gives about 3.7 detecting passes per satellite per day over the box, against about 2.6 for each MODIS sensor. At a single 10 km area, a VIIRS satellite gets about 1.4 per half-day and a MODIS sensor about 1.1. The two records sample fire at different hours: 12:40 and 02:10 for VIIRS, against 11:15/21:45 and 12:55/02:10 before the drift.
- **Scaling.** Factors between VIIRS satellites are within 3–4% of 1 on aggregate. Single months scatter by ±15–20%, so per-month factors would only fit noise.
- **MODIS since 2022.** Terra's passes moved to 10:00 and 20:40, and Aqua's to 14:00 and 03:30. The number of passes did not change. So drift alters when MODIS looks, not how often.

## Limits

- Pass counts include only passes that detected something. They are a lower bound on looks; cloud and smoke reduce them, and some passes over the box had no fire to see.
- The per-cell numbers count only cell-days with at least one detection.
- Only 14–17 clean months support each ratio, and a few large months dominate them.
- The simulation removes whole days, not single orbits.
- MODIS has an unlisted break between standard and near-real-time data (Terra 30 Aug–7 Sep 2026).

## How it was computed

The analyst's scripts were re-run and reproduced their logs exactly: `scripts/m09_q1q2_overpasses.py`, `m09_q3q4_monthly.py` and `m09_q5_cells.py`. The independent check is `scripts/m09-overpass-and-multi-viirs_review.py`. It does four things:

1. Clusters passes on a continuous time line for each sensor and counts them on high-activity days and per 10 km cell.
2. Computes ratios of monthly sums with a bootstrap over months (4000 resamples) and the range across years.
3. Runs the block-gap simulation and the real-outage comparison.
4. Measures overlap between satellites in 5 km cells.

Outputs are in `out/m09-overpass-and-multi-viirs_*.csv` and `_review_log.txt`.
