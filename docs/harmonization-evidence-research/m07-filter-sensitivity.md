# How sensitive are the results to confidence, type and static-source filters?

## Answer

None of the filters moves the stable-orbit MODIS-to-VIIRS ratio by more than its year-to-year spread. Over February 2012 to December 2021 (116 months), Terra plus Aqua divided by Suomi NPP is 0.242 (95% bootstrap interval 0.234–0.257). The ratio for single calendar years runs from 0.19 to 0.33. Dropping low-confidence rows moves the ratio the most (to 0.230). That −5% is a net figure: the daytime ratio rises by 4% and the night-time ratio falls by 11%, because VIIRS has no low-confidence rows at night. The one real static source in the box is a fixed, night-only heat source near 50.69°N, 120.41°W, about 6 km from Kamloops. It adds a steady 2.6 Suomi NPP hotspots a month (4.2 a month in the fire season), and MODIS has never detected it. In the quietest fire-season months that is 17% of the VIIRS count. Most of what the draft's "persistent-cell" mask removes elsewhere is real burning: cells that burned in more than one fire year, and November pile burning. Type filtering cannot be applied the same way through the whole record, because the Kamloops source is labelled type 0 before 2015. With near-real-time data, which has no type, a mask of that one site leaves about 0.3% of a VIIRS month uncorrected on average.

## Evidence

Sensors: MODIS means Terra and Aqua pooled. VIIRS means Suomi NPP (SNPP) unless named. Ratios are pooled sums (total MODIS divided by total SNPP), with 95% bootstrap intervals over months (2,000 resamples). The "year range" is the lowest and highest calendar-year ratio across the 10 years 2012 to 2021. Three outage months were dropped: February 2016 (Terra gap) and August and September 2020 (Aqua gap), which leaves 116 of 119 months. Four winter months have zero MODIS hotspots; they stay in the sums. No month has zero SNPP hotspots. November 2026 is left out everywhere.

**Confidence class and type (all rows to October 2026).** VIIRS has no low-confidence rows at night (0 of 410,754). By day, 10.2% of VIIRS rows are low confidence. For MODIS the low share is 7.3% by day and 10.6% at night. Among standard-quality rows, MODIS has 31 type-2 rows (other static land source) and VIIRS has 711 type-2 and 2,062 type-3 rows (offshore or water). There are no type-1 (volcano) rows. Of the 2,062 type-3 rows, 98.1% have a type-0 VIIRS hotspot within 2 km on the same local date. They are fire pixels on lakeshores during big fire years, not static sources.

**The one static source.** VIIRS hotspots within 1.5 km of 50.688°N, 120.408°W:

| Years | Type 0 | Type 2 | No type (near real time) |
|---|---|---|---|
| 2012–2014 | 72 | 0 | 0 |
| 2015–2021 | 33 | 345 | 0 |
| 2022–Oct 2026 | 47 | 366 | 58 |

All 921 of these rows are at night. By satellite they split into SNPP 469, NOAA-20 312 and NOAA-21 140. MODIS has no rows within 2 km of the site in 26 years. The source contributes 2.6 SNPP rows a month (stable window: 4.2 a month in the fire season, 0.2 in winter). From 2022 to October 2026 it contributes 2.7 to 3.2 rows a month for each VIIRS satellite. A three-satellite sum therefore carries about 9 a month from it.

**What the draft's mask removes.** The draft's "persistent-cell" rule flags a 0.01° cell if it has hotspots on at least 10 dates spread over at least 4 years, or on at least 5 out-of-season dates that make up at least half of its dates. This review rebuilt the rule on the same grid with November 2026 left out, which gives 87 VIIRS cells and 3,714 rows. Two of those cells are the Kamloops site, and they hold 895 of the rows. Only those two cells have 50 or more dates. In 57 of the 87 cells, at least half of the dates fall in a single year, which marks a fire event rather than a fixed source. SNPP rows the mask removes in the stable window:

| Month group (months) | SNPP rows | Removed at the site | Removed elsewhere |
|---|---|---|---|
| Busy fire season (51) | 179,714 | 238 | 915 |
| Quiet fire season (17) | 303 | 50 (16.5%) | 14 |
| Winter (48) | 19,757 | 10 (0.05%) | 338 (1.7%) |

"Quiet" means fire-season months with 36 or fewer SNPP hotspots, the bottom quarter of fire-season months. Of the 348 winter rows the mask removes, 284 are in November. They fall in cells active in 1 to 3 years, and 45% are daytime. That pattern fits slash-pile burning, which is real burning, not a static source.

**MODIS/SNPP ratio by filter (stable window).** "Type 0 only" keeps type-0 rows only. "Mask" removes the draft's persistent cells. "Site only" removes just the rows within 1.5 km of the Kamloops site. "All three" combines dropping low confidence, keeping type 0 only and removing the mask.

| Filter | All, 116 months [interval] (year range) | Day | Night | Winter, 48 months [interval] |
|---|---|---|---|---|
| Raw | 0.242 [0.234, 0.257] (0.19–0.33) | 0.343 | 0.176 | 0.241 [0.214, 0.261] |
| Drop low confidence | 0.230 [0.222, 0.248] (0.18–0.33) | 0.357 | 0.157 | 0.227 [0.200, 0.250] |
| Type 0 only | 0.242 [0.235, 0.258] | 0.343 | 0.177 | 0.241 |
| Mask | 0.243 [0.236, 0.260] | 0.345 | 0.177 | 0.245 [0.219, 0.265] |
| Site only | 0.242 [0.235, 0.257] | 0.343 | 0.176 | 0.241 |
| All three | 0.233 [0.223, 0.251] | 0.359 | 0.159 | 0.231 [0.202, 0.254] |

The day and night ratios differ by a factor of 2, and in winter by a factor of 4 (winter night 0.084, winter day 0.367). That gap is far larger than the effect of any filter.

**Quiet months depend on how "quiet" is chosen.** Both definitions below pick 17 months, and 14 of them overlap.

| Quiet months picked by | Raw ratio [interval] | Mask | Site only | Drop low confidence |
|---|---|---|---|---|
| Low SNPP count (36 or fewer, as in the draft) | 0.271 [0.206, 0.340] | 0.343 | 0.324 | 0.191 |
| Low MODIS count (8 or fewer) | 0.182 [0.137, 0.250] | 0.217 | 0.211 | 0.136 |

Picking months by a low count on one sensor biases the ratio toward that sensor (a selection effect). So the level of the quiet-month ratio is not a robust number. What holds under both definitions is the direction of the static-source effect: removing the site raises the quiet-month ratio by 16 to 20%.

**Near-real-time months (no type).** Near-real-time VIIRS rows run from August to October 2026 (88,497 rows); MODIS has 208 such rows in September and October 2026. Applying the mask to them removes 0.10% in August, 2.1% in September and 0.14% in October 2026. To estimate what would be lost without the type column, take the 244 standard-quality VIIRS sensor-months since 2018 and count the type-not-0 rows that the mask does not catch. They average 0.30% of a month's count (median 0, 99th percentile 3.8%, maximum 5.1%, all in months with few rows). Almost all of them are type 3, which is real fire.

## What this implies for the approach

- **Target record and unit:** static-source and filter choices do not favour either target record. In quiet months the Kamloops source is an added constant, not a proportional bias, so a single scale factor cannot remove it. It has to be masked before any scaling, whatever the unit. In fire radiative power it is small, because its rows have low FRP.
- **Scaling:** day and night need separate treatment much more than any filter does (0.34 against 0.18). Dropping low confidence pushes the two in opposite directions, so a confidence rule chosen after a pooled scale factor has been fitted would leave that factor biased.
- **Combining VIIRS satellites:** summing the satellites adds the static offset once per satellite, about 9 a month with three. Mask the site separately for each satellite.
- **MODIS since 2022:** no filter here affects the MODIS drift question. MODIS has only 31 static rows in total and never sees the site.
- **Filters that matter:** masking the Kamloops site, matters only for areas that contain it. A confidence rule, applied the same way across the whole record, for day and night separately.
- **Filters that make no practical difference:** type 0 only (0.4% of SNPP rows, and it would remove real lakeshore fire). A broad persistent-cell mask: removes real burning, including November pile burns.

## Limits

- The site was identified by its position only; the facility was not identified. (The team later judged it likely to be the Kruger pulp mill at Mission Flats; see [harmonization-tests.md](../harmonization-tests.md#static-and-recurring-sources).) Other weak static sources may sit below the VIIRS detection limit.
- The quiet-month results rest on 17 months and 300 to 400 SNPP hotspots, and the level of the ratio depends on how the months are picked.
- "Real fire" for type 3 and the pile-burning reading rest on timing, location and nearby fire pixels, not on fire perimeters or burn permits.
- MODIS and VIIRS confidence classes are not on the same scale. MODIS counts were not corrected for duplicate pixels from overlapping scans.
- The month key is the UTC month while cell dates are local dates. This only matters for hotspots near midnight on the last day of a month.

## How it was computed

- The analyst's scripts `m07_a_shares.py`, `m07_c_mask.py`, `m07_c2_types.py`, `m07_d_ratio.py` and `m07_e_nrt_static.py` were re-run from a clean start, and every draft number was reproduced.
- `scripts/m07-filter-sensitivity_review.py` is a separate implementation written for this review. It rebuilds the mask, isolates the site within 1.5 km, computes ratios by day and night under each filter, tests two definitions of quiet months, checks type-3 neighbours and estimates the near-real-time leakage. Its output tables are the files `out/m07-filter-sensitivity_review_*.csv`.
