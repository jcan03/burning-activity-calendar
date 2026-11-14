# What extra data could be obtained, and how hard it would be

## Answer

Two extra sources can be used before tomorrow night, and both have already been downloaded without a login. The first is a **per-day availability flag for each satellite**, built from NASA's open granule catalogue (CMR). A granule is one 5-minute MODIS or 6-minute VIIRS scene. The catalogue lists 124,636 granules over the box for all five sensors, including passes that found no fire, and it took a few minutes to fetch. It found unlisted Suomi NPP gaps in peak fire season 2024 and showed that two dates in the team's outage list are wrong. The second is **British Columbia's open 2026 current-season fire layer**. It puts 2026 second of 27 years for area burned in the box (about 410,000 ha, behind 2021). Measured against that area, Terra's daytime yield is about 0.41–0.45 of its level in 2021 and 2023. NOAA-20's is 0.74–0.93 of its level in those years. GOES-West fire data, Sentinel-3 fire radiative power and the Landsat fire archive are all real and reachable, but each needs an account or days of processing, so they are "usable later". FIRMS acquisition times are whole minutes. The nearest registered industrial facility to the Kamloops static source is a pulp mill 0.4 km away. That is proximity, not identification.

## Evidence

### Verdicts

| Source | Access | Range | Box sample obtained? | Verdict |
|---|---|---|---|---|
| NASA CMR granule catalogue (standard MODIS and VIIRS fire products) | Open, no login | Terra Nov 2000, Aqua Jul 2002, Suomi NPP Jan 2012, NOAA-20 Jun 2018 (complete from then), NOAA-21 Feb 2023, all to the present | Yes, full history, 13 MB | **Usable before tomorrow night** |
| FIRMS swath outlines (June 2026) | Layer in the FIRMS map viewer only; no download is described | Not stated | No | Not usable as data. NASA says they are built from the same CMR bounding coordinates. |
| LAADS geoMeta files | Directory listing is open; the files redirect to a licence/login page | MODIS only, 2000 to 2026; no VIIRS | No (HTTP 303 to `/profiles/licenses/`) | Not needed; CMR gives the same content openly |
| BC Wildfire current-season fire points and perimeters | Open (OGL-BC), WFS, refreshed every 15 minutes | 2026 season; moved to the historical layer on 1 April 2027 | Yes, 645 points in box | **Usable before tomorrow night** (provisional) |
| GOES-West ABI fire product (FDC) on AWS | Open, no login | GOES-17: Aug 2018 to Jan 2023; GOES-18: 2022 to present | Yes, 3 files (2.0 MB) | Usable later: days of work to build a curve |
| Published diurnal cycles for boreal or montane conifer | Papers | — | — | No count-based curve for this region found |
| Sentinel-3 SLSTR fire radiative power (NTC) | Search open (STAC); download needs a free Copernicus Data Space account | 8 Aug 2020 to present | Catalogue only | Usable later |
| Landsat 8/9 active fire (FIRMS) | 7-day files open; archive needs Earthdata login or an emailed code; API needs a MAP_KEY | 20 June 2022 to present, US and southern Canada | Yes, 7-day file: 130 pixels in box | Usable later, and only as a spot check |
| VIIRS Nightfire | Data-use licence required since 10 Jan 2025 | Suomi NPP and NOAA-20 | No | Not usable before the deadline |
| NPRI facility registry (Canada) | Open CSV | 1993 to 2024 | Yes (13.7 MB) | Usable before tomorrow night, for labelling only |

### 1. Availability flag from the granule catalogue

Each sensor's catalogue entries for the box, compared day by day (UTC) with the team's FIRMS rows:

| Sensor | Granules | Median per day | Days with none | Of those, days with FIRMS hotspots |
|---|---|---|---|---|
| Terra | 38,761 | 4 | 86 | 1 (1 hotspot) |
| Aqua | 36,555 | 4 | 31 | 0 |
| Suomi NPP | 26,471 | 5 | 85 | 2 (2,937 near-real-time hotspots, 4–5 Aug 2026) |
| NOAA-20 | 15,270 | 4 | 96 | 39, all April–June 2018 (426 hotspots) |
| NOAA-21 | 7,579 | 5 | 48 | 1 (8 hotspots, 14 Jan 2026) |

- **Fire-free passes are listed.** Granules appear on days with no hotspots, for example every Terra day in March 2026.
- **Gaps missing from the team's outage list.**
  - Suomi NPP has no granules on 30 May – 3 June, 10–15 July and 24–28 July 2024. On 24–28 July, NOAA-20 recorded 559, 13, 143, 51 and 217 hotspots.
  - Terra has none on 5–10 March 2026 and 13–15 May 2025.
  - NOAA-21 has none on 10–14 January 2026.
- **Listed gaps the catalogue contradicts.**
  - Suomi NPP has 4–7 granules a day and 8–62 hotspots a day on 11–20 August 2022. The list says the gap ran until 20 August.
  - Terra has 4 granules on each of 26 and 27 March 2026, which the list marks as a gap.
- **Where the flag fails.**
  - It cannot see partial losses. Aqua's listed formatter failure (16 August – 2 September 2020) still shows 3–5 granules a day of normal size.
  - The catalogue of science-quality granules misses two days on which FIRMS has near-real-time rows (Suomi NPP, 4–5 August 2026).
  - NOAA-20 granules are listed only from June 2018, although FIRMS starts on 1 April 2018.
  - The near-real-time catalogue keeps about 7 days: NOAA-20 near-real-time granules exist only from 7 November 2026.

### 2. Daily fire cycle

| Source | Region and data | What it gives | Fit to Interior BC |
|---|---|---|---|
| Giglio 2007 (TRMM VIRS) | 15 tropical and subtropical regions | Peak burning 13:00–18:30 local time; earlier in forest | Tropics only |
| Giglio, Csiszar and Justice 2006 | Terra/Aqua, global | Boreal North America: midmorning and early-afternoon activity "about evenly matched"; the ratio "can potentially mute" the cycle at boreal latitudes | Qualitative |
| Gui et al. 2025 (GOES-16) | North America | Forest fires have a "bimodal diurnal cycle lasting 4–8 h" (abstract; the curve parameters are already in the team's methods file) | Fire radiative power, not counts; continental scale |
| NOAA RAVE ATBD v2.1 (2024) | GOES-16 2018–2020 and GOES-17 2020; 5 land covers × 11 ecoregions | Fire radiative power peaks "between 12 PM and 4 PM"; forest peaks latest in the "forested mountains" ecoregion | Values shown only in figures; no table |

No published count-based cycle for boreal or montane conifer forest in Canada was found. SEVIRI does not view North America.

**GOES-West over the box,** computed from the downloaded files:

| | GOES-18 (West, 137°W) | GOES-16 (East, 75°W) |
|---|---|---|
| View zenith angle at the box centre | 59–60° | 72.5° |
| Pixel at the box centre | about 2.3 × 4.1–4.3 km (9.4–9.8 km²) | about 4.2 × 6.5 km (27 km²) |
| Fire pixels in the box, 23 July 2024 at about 20:00 UTC | 14 (5-minute file) and 30 (10-minute full-disk file) | 19 |

NOAA-20 recorded 905 hotspots in the box that day.

Volume of the GOES-18 files: 288 files a day (70 MB) for the 5-minute regional product, or 144 files a day (165 MB) for the full disk. A whole April–October season of the 5-minute product is about 15 GB. Taking one file per hour cuts that to about 1.3 GB.

### 3. Third sensors

- **Sentinel-3 SLSTR.**
  - July 2026 had at least 200 granules over the box (the listing was truncated at 200), about 7 a day from Sentinel-3A and 3B.
  - Day passes fall at 17–19 UTC, about 09–11 local solar time. This is the only morning observer besides Terra.
  - Night passes fall at 04–06 UTC.
  - The fire file in each granule is about 0.9 MB; the full product is 77 MB.
  - Xu et al. 2021 found that fire radiative power from the S7 channel varies about tenfold across the scan; this was read from a search summary of the abstract only.
- **Landsat.** The open 7-day file had 11,783 pixels. 130 of them fell in the box, all from 12–14 November at about 18:45 UTC (daytime). Landsat records each 30 m fire pixel, a unit unlike the other sensors' hotspots. Some rows timed 02–06 UTC are labelled daytime, which is unexplained.

### 4. Precision of acquisition times

FIRMS defines `acq_time` only as "Time of acquisition/overpass of the satellite (in UTC)". The format is HHMM, so the precision is one minute.

In the team's rows, 18–24% of minute values are multiples of 5, close to the 20% expected by chance. If `acq_time` were the granule start time, every MODIS value would be a multiple of 5 and every VIIRS value a multiple of 6. So the field is a per-pixel or per-scan time rounded to the minute; this is an inference. The FIRMS FAQ gives Landsat times with seconds (HH:MM-SS), but the Landsat CSV carries HHMM.

### 5. BC 2026 fire records

The current-season points layer has 645 incidents in the box, all of type "Fire". 636 are out and 8 are under control. 642 have 2026 ignition dates, and their sizes sum to **409,666 ha**.

Ranked among 2000–2026, 2026 comes second: 2021 had 653,941 ha, 2026 409,666 ha, 2017 263,878 ha and 2023 217,297 ha. These sums use the r03 definition: the size of each incident whose point lies in the box.

Fire-season hotspots per 1,000 ha burned, with the static site removed:

| Year | Area (1,000 ha) | Terra day | Aqua day | NOAA-20 day | Terra day ÷ NOAA-20 day |
|---|---|---|---|---|---|
| 2021 | 654 | 6.70 | 10.02 | 52.6 | 0.127 |
| 2023 | 217 | 6.07 | 9.49 | 42.0 | 0.145 |
| 2026 | 410 | 2.74 | 7.19 | 39.1 | 0.070 |

Some data-quality problems are visible: ignition dates in 1429 and 2044, and one 2025 perimeter in the 2026 layer.

### 6. The fixed heat source

The nearest facility to 50.688°N, 120.408°W in Canada's National Pollutant Release Inventory is Kruger Inc.'s "Kamloops Mill (SFO)", a chemical pulp mill at 2005 Mission Flats Road. Its registry location is 50.6861°N, 120.4037°W, 0.37 km away. A Weyerhaeuser sawmill last reported in 2008 sits 0.76 km away. OpenStreetMap places the point at "Gate 2, Mission Flats". VIIRS Nightfire could characterise the source's temperature, but it needs a licence.

## What this implies

- The team could build the per-day availability flag that the daily-mean combination rule needs, from an open source, tonight. It could say that the flag records passes, not data quality. It could not claim that the flag detects partial losses, or that it covers the current month: near-real-time granules are kept for only about 7 days.
- The outage list understates Suomi NPP gaps during the 2024 fire season. Any month that used it as complete, such as July 2024, carries that error.
- An independent, provisional check of the 2026 Terra decline is available now, not only in April 2027. Measured against area burned, Terra's daytime yield fell much further than NOAA-20's. The 2026 figures are operational, not final.
- No published curve gives a local count-based daily fire cycle. Building one from GOES-West is feasible later, at a 60° view angle with pixels about 2.4 times nominal size.
- The Kamloops static source can be described as lying 0.4 km from a registered pulp mill. That is proximity, not identification.

## Limits

- Granule presence was checked against FIRMS rows only; how complete the granules were was not measured.
- The gap dates are UTC days.
- The catalogue was queried for science-quality collections only.
- The 2026 BC area is provisional and counts each whole fire whose point lies in the box, including any part outside it.
- One GOES timestamp per satellite was inspected.
- The diurnal search was limited to a few queries. The full text of Xu et al. 2021 and Giglio 2007 was not read; their citations were confirmed through Crossref, and Giglio's thesis summary (2006) was read in full.
- Sentinel-3 and Landsat archive contents for the box were not downloaded.

## Sources

- NASA FIRMS, "New FIRMS data product: satellite swath outlines", 25 June 2026. https://www.earthdata.nasa.gov/news/blog/new-firms-data-product-satellite-swath-outlines
- NASA FIRMS FAQ. https://www.earthdata.nasa.gov/data/tools/firms/faq ; attributes page: https://earthdata.nasa.gov/data/tools/firms/active-fire-data-attributes-modis-viirs ; archive download page: https://firms.modaps.eosdis.nasa.gov/download/ ; API: https://firms.modaps.eosdis.nasa.gov/api/area/
- NASA CMR search API (collections C2271754179, C2278858993, C2734202914, C2734197957, C2831626262 on LPCLOUD; LANCE near-real-time collections). https://cmr.earthdata.nasa.gov/search/
- LAADS geoMeta README. https://ladsweb.modaps.eosdis.nasa.gov/archive/geoMeta.json
- NOAA GOES on AWS: s3 buckets `noaa-goes16`, `noaa-goes17`, `noaa-goes18`, products ABI-L2-FDCC and FDCF.
- Kondragunta, Li, Zhang and Xu, 2024. RAVE Algorithm Theoretical Basis Document v2.1, NOAA/NESDIS/OSPO. https://www.ospo.noaa.gov/resources/documents/pdf/RAVE_ATBD.pdf
- Gui et al., 2025. Remote Sensing 18:52. https://doi.org/10.3390/rs18010052 (abstract)
- Giglio, 2007. Remote Sensing of Environment 108:407–421. https://doi.org/10.1016/j.rse.2006.11.018 (metadata only); Giglio, 2006, PhD thesis, University of Maryland. https://dataserver-coids.inpe.br/queimadas/queimadas/Publicacoes-Impacto/material3os/2006_Giglio_GlobalDetection_UMaryland_DE3os.pdf
- Giglio, Csiszar and Justice, 2006. Journal of Geophysical Research 111, G02016. https://doi.org/10.1029/2005JG000142
- Xu, Wooster, Polehampton, Yemelyanova and Zhang, 2021. Remote Sensing of Environment 261:112460. https://doi.org/10.1016/j.rse.2021.112460 (search summary of the abstract only)
- Copernicus Data Space STAC, collection `sentinel-3-sl-2-frp-ntc`. https://stac.dataspace.copernicus.eu/v1/collections/sentinel-3-sl-2-frp-ntc
- BC Data Catalogue: Fire Locations – Current; Fire Perimeters – Current; Fire Incident Locations – Historical (OGL-BC). https://catalogue.data.gov.bc.ca/dataset/bc-wildfire-fire-locations-current
- Environment and Climate Change Canada, NPRI geolocation bulk file, 1993 to present. https://open.canada.ca/data/dataset/40e01423-7728-429c-ac9d-2954385ccdfb
- Earth Observation Group, VIIRS Nightfire. https://eogdata.mines.edu/products/vnf/
- Scripts (in `round3/scripts/`): `w03_cmr.py` fetches the granules; `w03_compare.py` and `w03_flag.py` build and test the flag (output `round3/out/w03_daily_flag.csv`); `w03_goes.py` handles the GOES geometry; `w03_bc2026.py` handles the 2026 area and the yield per area (output `round3/out/w03_bc2026_density.csv`).
