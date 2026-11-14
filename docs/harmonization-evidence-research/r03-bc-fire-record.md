# An independent British Columbia fire record to judge the join

## Answer

The BC Wildfire Service historical fire incident points (one point per incident, with discovery date and final size, Open Government Licence – British Columbia) give 30,028 dated incidents in the box for 2000–2025. Every sensor's fire-season hotspot count ranks years by area burned about equally well: Spearman rho 0.84 for Terra (2001–2025), 0.88 for Aqua (2003–2025) and 0.89 for Suomi NPP (2012–2025). Measured this way, the whole-season VIIRS-to-MODIS count ratio did not change after the MODIS orbits began drifting. With outage months removed from both sensors, Suomi NPP/Terra is 7.66 in 2012–2021 and 7.75 in 2022–2025. Allowing for year size, the estimated shift is −1% (95% interval −21% to +23%). Suomi NPP/Aqua is 8.93 and then 9.16, a +5% shift (−13% to +26%). In 2022–2025 hotspots per km² burned fell by about 10% for MODIS and VIIRS alike, so the independent record shows no loss that is specific to MODIS. The day and night split does seem to have moved, though no single shift is significant with only four drift years: Terra's daytime count fell relative to VIIRS (+12% in the SNPP/Terra day ratio), its night count rose (−16% in the night ratio), and Aqua's daytime count rose (−9% in the SNPP/Aqua day ratio).

## Evidence

**Source.** "BC Wildfire Fire Incident Locations – Historical", layer `WHSE_LAND_AND_NATURAL_RESOURCE.PROT_HISTORICAL_INCIDENTS_SP`. The catalogue record was opened. It gives the licence as OGL-BC, the purpose as "visual or analytical purposes", says the data are not for legal use, and says the layer is refreshed each 1 April with the previous season. It defines IGNITION_DATE as the discovery date, CURRENT_SIZE as the area inside the outer perimeter in hectares, and FIRE_YEAR as the fiscal year. The data were downloaded as CSV through the public WFS (web feature service). The server reports 40,592 features in the exact box, which matches the local copy row for row, so the download is complete. Points were clipped on the LATITUDE and LONGITUDE attributes, inclusive. Year means the calendar year of ignition. Area counts every dated row: Fire, Nuisance Fire, Duplicate and Agency Assist. No year from 2000 to 2025 has zero area. The smallest is 2011, with 533 ha.

**Annual area burned in the box (ha, dated incidents).** Full table: `out/r03-bc-fire-record_review_annual_area.csv`.

| Year | Area | Year | Area | Year | Area |
|---|---|---|---|---|---|
| 2003 | 122,382 | 2015 | 24,137 | 2022 | 45,814 |
| 2009 | 87,678 | 2017 | 263,878 | 2023 | 217,297 |
| 2010 | 28,169 | 2018 | 99,749 | 2024 | 62,212 |
| 2011 | 533 | 2021 | 653,941 | 2025 | 17,205 |

Undated rows are 10,005 in the box for 2000–2025. They are mostly Smoke Chase (5,956), Nuisance Fire, Unknown and field-activity rows with zero size. The only sizeable undated area is in 2024 and 2025: 2,440 ha of Prescribed Fire across both years, plus a 1,472 ha Duplicate row in 2025. These are not wildfire, so the 2025 wildfire total is not undercounted. At least 90% of each year's area comes from fires discovered in April to October.

**Rank correlation, fire-season hotspots against annual area.** "Fair" seasons leave out any season with a gap outage in April to October.

| Sensor, years | n | rho | 95% bootstrap | Fair seasons only |
|---|---|---|---|---|
| Terra 2001–2025 | 25 | 0.84 | 0.60–0.96 | 0.85 (n=23) |
| Aqua 2003–2025 | 23 | 0.88 | 0.68–0.97 | 0.90 (n=21) |
| Suomi NPP 2012–2025 | 14 | 0.89 | 0.52–1.00 | 0.87 (n=13) |
| NOAA-20 2018–2025 | 8 | 0.98 | 0.73–1.00 | same |
| Terra 2001–2021 | 21 | 0.75 | 0.36–0.93 | 0.78 (n=20) |

The four drift years, 2022–2025, fall in exactly the same order as area for Terra, Aqua and Suomi NPP. With n=4 that is weak evidence.

**VIIRS/MODIS count ratio, April–October.** A month is removed from both sensors when either one has a gap outage. Nine sensor-months were removed: Terra 2001-04, 06 and 07 and 2022-10; Aqua 2020-08 and 09 and 2022-04; Suomi NPP 2022-07 and 08. The table gives the pooled ratio, with a bootstrap over years in brackets, and the median of the yearly ratios. The size-controlled shift is the 2022–2025 coefficient from an ordinary least squares fit of ln(yearly ratio) = a + b·ln(area) + c·[year ≥ 2022] over 2012–2025, 14 years, with its 95% interval. `out/r03-bc-fire-record_review_ratios_masked.csv`, `…_ratio_shift_size_controlled.csv`

| Ratio | 2012–2021 pooled (10 y) | 2022–2025 pooled (4 y) | Yearly medians | Size-controlled shift |
|---|---|---|---|---|
| SNPP/Terra, all | 7.66 (6.54–7.86) | 7.75 (6.97–8.13) | 7.27 → 7.15 | −1% (−21 to +23) |
| SNPP/Terra, day | 7.21 | 7.62 | 5.90 → 7.71 | +12% (−13 to +43) |
| SNPP/Terra, night | 7.95 | 7.81 | 9.05 → 7.31 | −16% (−33 to +6) |
| SNPP/Aqua, all | 8.93 (7.33–9.18) | 9.16 (8.30–9.54) | 8.34 → 8.59 | +5% (−13 to +26) |
| SNPP/Aqua, day | 4.98 | 4.58 | 4.40 → 4.07 | −9% (−21 to +4) |
| Aqua/Terra, day | 1.45 (2003–2011: 1.31) | 1.65 | 1.40 → 1.71 | not fitted |

Yearly SNPP/Terra ratios range from 5.0 to 9.1 in 2012–2021 and from 7.0 to 8.2 in 2022–2025. Pooled ratios are dominated by 2021 (6,539 km²), which is why the table also gives yearly medians and a size-controlled fit.

**Between VIIRS satellites, pooled, masked.** NOAA-20/SNPP is 0.99 (0.93–1.01) for 2018–2021 and 0.98 (0.94–1.11) for 2022–2025. NOAA-21/SNPP is 0.97 (0.89–0.99) for 2023–2025 (3 years); its daytime ratio alone is 0.92.

**Hotspots per km² burned, pooled.** Fair seasons only; 2022 is dropped for Terra, Aqua and Suomi NPP, and 2020 for Aqua.

| Sensor | 2003–2011 | 2012–2021 | 2023–2025 |
|---|---|---|---|
| Terra | 3.14 (2.42–7.14) | 2.20 (1.99–4.40) | 1.95 (1.81–3.41) |
| Aqua | 2.84 (2.15–6.71) | 1.89 (1.68–3.85) | 1.64 (1.54–2.89) |
| Suomi NPP | – | 16.86 (15.34–29.75) | 15.27 (14.21–24.85) |

Hotspot counts grow more slowly than area. A log-log fit over 2012–2021 gives slopes of 0.71 for Terra, 0.65 for Aqua and 0.75 for Suomi NPP. For 2023–2025, observed counts divided by the fit's prediction (geometric mean) are 0.79 for Terra, 0.68 for Aqua and 0.79 for Suomi NPP. All lie within about one residual standard deviation (0.58–0.74 in ln units).

## What this implies for the approach

- **Target record.** All sensors rank years against area equally well, so this check gives no reason to prefer a MODIS-equivalent or a VIIRS-equivalent target.
- **Unit.** Raw counts are not proportional to area: the slope is about 0.7, so small years get many hotspots per km². The VIIRS/MODIS ratio between sensors is much steadier than hotspots per km² burned. Bridging sensors through their own overlap is better supported than calibrating each one to burned area.
- **Scaling.** One whole-season factor (about 7.7 for SNPP/Terra, about 9 for SNPP/Aqua) held through 2022–2025. Even so, a single year's ratio scatters by about ±20%. The day and night ratios moved in opposite directions after 2022 and roughly cancel in the total. A factor computed only from 2012–2021 and applied by day and night separately would therefore carry the drift error. A combined day-plus-night factor would not.
- **Combining VIIRS satellites.** Suomi NPP, NOAA-20 and NOAA-21 count within about 3% of each other, with NOAA-21 by day 8% lower. Treating the satellites as near-equivalent, or averaging them, is supported at the season level.
- **MODIS since 2022.** There is no sign that MODIS stopped tracking burned area. The evidence points toward keeping drift-period MODIS only as Terra and Aqua summed over day and night, or toward checking the day and night channels against VIIRS. It does not support using Terra daytime counts alone.

## Limits

- Area is attributed to the discovery date. Large fires burn for weeks, so monthly comparisons are loose: monthly Spearman rho is 0.30–0.33 for 2001–2021, from the earlier script. Only annual comparisons are reliable.
- Fires are clipped by their start point, so area that burns across the box edge is misplaced in both directions. This was not quantified; doing so would need the perimeter layer and geospatial tools.
- Half of the "Fire" records are 0.01 ha or smaller, far below the detection limit of either sensor. One fire supplies 14–80% of a year's area. Industrial, agricultural and dated prescribed burns are not in this record, but they may produce hotspots. Prescribed fires appear here only for 2024–2025, and without dates.
- There are only four drift years, three of them fair for every sensor. Every post-2022 interval is wide and includes zero change.
- BC uses satellite hotspots operationally, so the two records may not be fully independent. This is unconfirmed.

## How it was computed

`scripts/r03-bc-fire-record_review.py` does the following. It reads `external/bcfire/inc_*.csv`, removes duplicate OBJECTIDs, clips to the box and sums CURRENT_SIZE by ignition year. It then counts FIRMS hotspots of type 0 for April–October by sensor, year and day/night, and masks gap-outage months in pairs. Finally it computes Spearman correlations, pooled and median ratios with a 4,000-sample bootstrap over years, the size-controlled OLS fit and the log-log fit. The researcher's `r03_bc_fire_record.py`, `r03_missing_check.py` and `r03_bigyears.py` were re-run and reproduce the draft's numbers.

## Sources

- Catalogue record, including licence and field definitions: https://catalogue.data.gov.bc.ca/api/3/action/package_show?id=bc-wildfire-fire-incident-locations-historical (human page: https://catalogue.data.gov.bc.ca/dataset/bc-wildfire-fire-incident-locations-historical)
- Open Government Licence – British Columbia 2.0: https://www2.gov.bc.ca/gov/content?id=A519A56BC2BF44E4A008B33FCF527F61
- WFS used for the download and for the feature count: https://openmaps.gov.bc.ca/geo/pub/WHSE_LAND_AND_NATURAL_RESOURCE.PROT_HISTORICAL_INCIDENTS_SP/ows
