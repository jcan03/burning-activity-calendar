# A per-day availability flag, and the VIIRS satellites combined with it

## Answer

NASA's open scene catalogue gives a usable per-day flag for whole-day and half-day losses. On the days it marks empty, FIRMS has almost no hotspots. There are two holes, where the catalogue is silent but data exist: Suomi NPP near-real-time data on 4–6 August 2026, and NOAA-20 before 5 June 2018. The flag cannot see losses inside a scene. A hotspot-count check finds such a loss only when three quarters or more of the hotspots are gone and the fire is large. That check found one new loss: NOAA-20 recorded no hotspots on 19–22 July 2023. With day-level masking, the stable-period MODIS to Suomi NPP ratio moves from 0.2425 to 0.238. The factors that bring NOAA-20 and NOAA-21 to the Suomi NPP level move from 1.011 to 1.025 and from 1.034 to 1.050. The daily-mean combined VIIRS series is not affected by any real outage month. Classed against a Suomi NPP baseline, NOAA-20 alone changes the five-class label of 13–16% of fire-season box months (interval roughly 3–29%) and about 23% of 100 km circle-months. Where the baseline median is at least 10 hotspots, the circle figure is about 14%. That is the label noise the change of satellite adds on its own.

## Evidence

**Basis.** Hotspots use `use == True` and local-date months. The SPEC check was reproduced: MODIS 48,233, Suomi NPP 198,916, ratio 0.2425 (0.343 by day, 0.177 at night), 116 months. A scene is placed on a local date by its time plus the box-centre offset of −8.02 h. VIIRS passes keep their UTC date. Terra night passes (03–06 UTC) move to the previous local date. A sensor-day is **available** when it has at least one day scene and one night scene, minus the days on the outage list and the count-check suspects. One exception: Suomi NPP 11–20 August 2022 is kept as available, because the catalogue shows scenes and the hotspot counts are normal. Outage days add zero to a month. No month is dropped. All intervals are 95% and come from resampling whole years.

**Part 1: catalogue gaps since 2012 that the outage list lacks** (no scenes; local dates). Earlier gaps are in `f03_review_zero_scene_runs.csv`.

| Sensor | Days with no scene |
|---|---|
| Suomi NPP | 25 Mar 2012; 26 Jul 2023; 30 May–3 Jun, 10–15 Jul, 24–28 Jul, 26 Sep 2024 |
| Terra | 12–15 May 2025; 4–9 Mar 2026 |
| NOAA-20 | 30 Sep 2023; 1 Apr–4 Jun 2018 (the catalogue is incomplete here, but FIRMS has 406 rows against Suomi NPP's 434, so treated as available) |
| NOAA-21 | 27–28 Feb 2024; 10–14 Jan 2026 |

The catalogue also shows half-day losses (only a day pass or only a night pass) that the list lacks. Examples: Suomi NPP on 3–4 August 2021 had 336 and 759 hotspots, against NOAA-20's 1,208 and 2,011. NOAA-21 on 20 July 2024 had 239 against about 850.

**Listed gaps the catalogue contradicts** (`f03_review_listed_vs_catalogue.csv`):
- **Suomi NPP 26 Jul–20 Aug 2022:** scenes exist on 11–20 August, with 408 hotspots.
- **Aqua 16 Aug–2 Sep 2020:** the scenes look normal, but there are only 25 hotspots. This is a real loss that the catalogue cannot see.
- **Terra 15 Apr 2001 and 26–27 Mar 2026:** scenes exist, with 0 hotspots.
- **Suomi NPP 2–6 Nov 2024:** scenes exist on 3 of the 5 days. The list is about 3 days too wide.
- **NOAA-20, NOAA-21 and the 2025 "partial" entries:** normal scenes, as expected for a partial loss.

**Partial-loss count check.** Each satellite's daily count is compared with what the other VIIRS satellites imply (see the analyst's simulation, re-run). A loss of 75% is found in 87–92% of the fire-season windows that can be tested, but only 18–55% of June–September windows have enough fire to test. A loss of 50% is found in 8–34%. On Terra the check gives false alarms in about 7% of healthy windows. The confirmed new loss is NOAA-20 on 19–22 July 2023: 0, 0, 0 and 0 hotspots against Suomi NPP's 34, 141, 360 and 597, with normal scenes.

**Part 2: ratios with day-level masking** (my recomputation; the analyst's values agree to 0.001).

| Quantity | No day mask | Day mask |
|---|---|---|
| MODIS / Suomi NPP, 116 stable months | 0.2425 (0.237–0.266) | **0.2381 (0.231–0.267)** |
| Same, all 119 months kept | 0.2425 | 0.2381 |
| NOAA-20 factor (Suomi NPP ÷ NOAA-20), Apr 2018–Oct 2026, 9 years | 1.001 (0.96–1.04) | **1.0245 (1.014–1.047)** |
| Same, standard rows only, to Jul 2026 | — | 1.0275 (1.015–1.053) |
| NOAA-21 factor (Suomi NPP ÷ NOAA-21), Mar 2023–Oct 2026, 4 years | 1.027 (1.016–1.054) | **1.0503 (1.030–1.083)** |

The earlier factors of 1.011 and 1.034 come from dropping whole months. The analyst reproduces them as 1.014 and 1.034.

| Year | Suomi NPP / NOAA-20, fire season, unmasked, then masked | NOAA-21 / NOAA-20, all months, unmasked, then masked |
|---|---|---|
| 2018 | 1.077 to 1.067 | |
| 2019 | 1.043 to 1.034 | |
| 2020 | 0.928 to 0.928 | |
| 2021 | 0.995 to 1.017 | |
| 2022 | 0.831 to 1.031 | |
| 2023 | 1.064 to **1.028** | 1.036 to 1.002 |
| 2024 | 0.881 to **0.994** | 0.880 to 0.929 |
| 2025 | 0.993 to 0.994 | 0.887 to 0.914 |
| 2026 (to Oct) | | 0.962 to 0.962 |

**Part 3: the combined series.** The rule: each day, take the mean of the available satellites, each scaled to Suomi NPP, then sum over the month. The table gives each alternative's difference from the combined series on the whole box (recomputed).

| Month | Combined | Suomi NPP alone | NOAA-20 alone | Plain monthly mean |
|---|---|---|---|---|
| 2022-07 | 629 | −64% | −3% | −34% |
| 2022-08 | 2,266 | −55% | −1% | −28% |
| 2023-07 (NOAA-20 loss) | 4,753 | −0.4% | **−23%** | −8% |
| 2024-07 | 7,102 | −18% | +3% | −8% |
| 2024-11 | 690 | −23% | −0.5% | −7% |
| 2026-08 | 29,590 | −4% | +2% | −1% |

At each change in the number of satellites, the combined series stays level with Suomi NPP alone. A plain sum of the satellites does not: it is 1.93 times Suomi NPP from April 2018 and 2.9 times from March 2023.

| Period | Combined ÷ Suomi NPP | Plain sum ÷ Suomi NPP |
|---|---|---|
| Apr–Oct 2018 | 0.980 | 1.93 |
| Mar–Oct 2023 | 1.008 | 2.9 |

The analyst also imposed 7-day Suomi NPP outages on months with no flagged day. The median error of the combined series was 0.9% on the box and 1.2% on 100 km circles. The plain mean's error was 7.1% and 6.8%. With 15-day outages the analyst's simulation gives 1.7% and 23%.

**Part 4: share of months whose five-class label differs from Suomi NPP's own label.** The candidate is NOAA-20 alone. The baseline is Suomi NPP's counts for 2012–2021, without the tested year. The test years are 2018–2021 and 2023–2025. Every box month and every 100 km circle-month is classifiable (baseline median at least 1).

| Scope | Months | Label changed | Two or more classes apart |
|---|---|---|---|
| Box, fire season, all months | 49 | 16% (4–29%) | 0% |
| Box, fire season, no flagged day for either satellite | 37 | **13.5% (3–23%)** | 0% |
| Box, fire season, baseline median ≥ 100 | 24 | 1 month (4%) | 0% |
| Box, all months | 84 | 25% (19–30%) | 2.4% |
| 100 km circles, fire season | 1,519 | 23% (18–28%) | 7.4% |
| 100 km circles, fire season, baseline median ≥ 10 | 939 | **14% (11–18%)** | 1.5% |

- **Combined series.** It changes 10% of fire-season box months and 16% at 100 km. In 2018–2021 half of that series is Suomi NPP itself, so these figures look better than they should. For NOAA-20 plus NOAA-21 alone (2023–2025), the figures are 2 of 21 box months (0–29%) and 21% at 100 km.
- **Factor fitted without the tested year.** Leave-one-year-out factors range from 1.018 to 1.037. They give the same box labels as before, and 23.1% against 23.0% at 100 km. The overlap between fitting and testing years does not matter here.

## What this implies

- The team could say that its VIIRS availability is checked day by day against NASA's catalogue. It could also say that the combined series is not biased by any listed or unlisted outage in 2018–2026. It could not say that the flag detects losses inside a scene, or that it is verified for the current month: the catalogue holds near-real-time scenes for only about a week, and it missed 4–6 August 2026.
- The Suomi NPP / NOAA-20 series is flat once masked: 0.93–1.07 by year, with no outlier year. The earlier 2023 and 2024 values were outage artefacts.
- NOAA-21 runs 5–9% lower relative to NOAA-20 in 2024–2025 than in 2023. Four years cannot separate drift from year-to-year variation.
- Even with a perfect conversion, a current month taken from NOAA-20 or NOAA-21 instead of Suomi NPP gets a different label in roughly one fire-season month in seven on the box, and one in seven to one in four on 100 km circles. The rate depends on how small the counts are. Almost all changes are by one class, and they fall in months that sit near a class boundary or have few hotspots. With these five classes, no conversion can be expected to agree with Suomi NPP's own labels in much more than about 85% of box months, or about 77–86% of 100 km circle-months.

## Limits

- **Count-check tuning and testing.** The count-check thresholds were chosen after looking at the data. Its detection rates come from imposed losses on healthy periods, not from real losses.
- **Intervals.** They rest on 7–10 years, and on 3–4 years for NOAA-21. Circle intervals are optimistic, because the circles overlap and share fires.
- **Near-real-time rows.** The August–October 2026 near-real-time months give Suomi NPP / NOAA-20 = 0.999, against 1.046 in January–July 2026. Dropping them moves the NOAA-20 factor by 0.3%. Whether near-real-time and standard counts differ was not resolved.
- **NOAA-20 before 5 June 2018.** These days are assumed available. In July 2018, Suomi NPP saw 1.38 times NOAA-20's hotspots, so early NOAA-20 months may be less reliable.
- **Terra masking.** Four Terra days masked by the count check are probably fire cycles, not losses. Releasing them leaves every ratio unchanged to four decimals.

## How it was computed

- **Analyst's pipeline.** The analyst's scripts `f03_flag.py` to `f03_part4b.py` were re-run from a clean start and reproduced the draft. The flag is `f03_availability_flag_localdate.csv`; its main tables are `f03_part2_*.csv`, `f03_part3_*.csv` and `f03_part4_summary.csv`.
- **Independent recomputation.** `f03-availability-flag_review.py` rebuilds the day flag directly from the catalogue CSVs. It then recomputes the gap lists, the ratios and factors, the outage-month comparison, and the label changes, including the no-flagged-day months, the leave-one-year-out factor and the count thresholds. Its outputs are `f03_review_headline.csv`, `f03_review_zero_scene_runs.csv`, `f03_review_listed_vs_catalogue.csv`, `f03_review_part3_box.csv`, `f03_review_part4_summary.csv`, `f03_review_part4_rows.csv` and `f03_review_log.txt`.
