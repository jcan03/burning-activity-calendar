# Upstream fire product family, file formats and archives

Verified 2026-11-13. Every row was checked against the linked page on that date. Status tags: [confirmed] means the page supports the claim as written. [corrected] means the researcher's value was wrong or incomplete and the corrected value is given. [unverified] means the claim could not be confirmed on an opened page. Terms used below:
- "Collection" (C) / "Version" (V): NASA's reprocessing generation. MODIS fire products are Collection 6.1 (written "061" in file names). VIIRS fire products are Collection 2 / Version 002.
- "L2 swath": per-granule output in satellite (swath) geometry.
- "L3 tile": output gridded onto a sinusoidal tile grid (tiles named hXXvYY).
- "NRT": near-real-time FIRMS/LANCE data. "Standard": the science-quality reprocessed stream.
- Julian date "AYYYYDDD": acquisition year and day of year.

## Key facts

### MODIS Level 2 swath fire products (MOD14 Terra, MYD14 Aqua), Collection 6.1

| Item | MOD14 (Terra) V061 | MYD14 (Aqua) V061 | Source / status |
|---|---|---|---|
| Format | HDF4 | HDF4 | [LP DAAC MOD14](https://www.earthdata.nasa.gov/data/catalog/lpcloud-mod14-061), [LP DAAC MYD14](https://www.earthdata.nasa.gov/data/catalog/lpcloud-myd14-061) [confirmed] |
| Spatial resolution | 1 km (1000 m x 1000 m at nadir) | 1 km | same [confirmed] |
| Granule | 5-minute swath, about 2,030 km along track x 2,300 km across track (catalog) | same | same [confirmed] |
| Temporal coverage | 2000-02-24 to present | 2002-07-04 to present | same [confirmed] |
| DOI | 10.5067/MODIS/MOD14.061 | 10.5067/MODIS/MYD14.061 | same [confirmed] |
| File name | `MOD14.AYYYYDDD.HHMM.061.YYYYDDDHHMMSS.hdf` (example `MOD14.A2025224.1755.061.2025224212147.hdf`) | `MYD14.AYYYYDDD.HHMM.061.YYYYDDDHHMMSS.hdf` (example `MYD14.A2025224.0945.061.2025224201819.hdf`) | same [confirmed] |
| Data state on catalog page (2026-11-13) | ACTIVE; no Terra end-of-life notice on the page | ACTIVE; no Aqua end-of-life notice on the page | same [confirmed] |

- In the file name, HHMM is the acquisition start time of the 5-minute granule, and the trailing YYYYDDDHHMMSS is the production date and time. The catalog page describes HHMM as "acquisition time" and does not itself say "UTC". MODIS granule times are UTC, but that part is from memory. [LP DAAC MOD14](https://www.earthdata.nasa.gov/data/catalog/lpcloud-mod14-061) [confirmed; UTC unverified]
- The MOD14 V061 catalog variables table lists 30 variables per granule: Algorithm QA, CMG_night, Fire Mask, and 27 fire-pixel (FP_) variables: FP_AdjCloud, FP_AdjWater, FP_CMG_col, FP_CMG_row, FP_confidence, FP_land, FP_latitude, FP_line, FP_longitude, FP_MAD_DT, FP_MAD_R2, FP_MAD_T21, FP_MAD_T31, FP_MeanDT, FP_MeanR2, FP_MeanT21, FP_MeanT31, FP_NumValid, FP_power, FP_R2, FP_RelAzAng, FP_sample, FP_SolZenAng, FP_T21, FP_T31, FP_ViewZenAng, FP_WinSize. [LP DAAC MOD14](https://www.earthdata.nasa.gov/data/catalog/lpcloud-mod14-061) [confirmed; the full list was added]
- The Collection 6/6.1 User's Guide (Version 1.0, May 2021) describes each Level 2 granule as covering "approximately 2340 × 2030 km in the along-scan and along-track directions". It contains a fire mask, a pixel-level QA image with 19 bits of QA information per pixel, and a fire-pixel table. "Due to HDF file format and library limitations, the Fire Pixel Table is stored as 27 separate SDSs." The 27 FP_ SDSs plus Fire Mask, Algorithm QA and CMG_night give the catalog's 30 variables, so the guide and the catalog agree. [MODIS C6/C6.1 User's Guide](https://www.earthdata.nasa.gov/s3fs-public/2023-09/MODIS_C6_C6.1_Fire_User_Guide_1.0.pdf) [confirmed]
- The User's Guide copy hosted by LP DAAC (MOD14_User_Guide_V61.pdf) is the same document: same title, Version 1.0, May 2021. [LP DAAC copy](https://lpdaac.usgs.gov/documents/1005/MOD14_User_Guide_V61.pdf) [confirmed]

### MODIS Collection 6 vs 6.1

- No algorithm or product changes were made to the active fire products for Collection 6.1. The only differences come from updated calibration of MODIS bands 1 and 2 in the Level 1B input, which affects the internal cloud mask. The thermal bands were not affected, so FRP is unchanged. The guide says C6 and C6.1 "may be freely intermixed". [MODIS C6/C6.1 User's Guide §2.1](https://www.earthdata.nasa.gov/s3fs-public/2023-09/MODIS_C6_C6.1_Fire_User_Guide_1.0.pdf) [confirmed]
- Size of the C6 to C6.1 difference: in a one-day sample (8 July 2009), 18 of 17,610 C6 fire pixels (0.1 %) changed class. In a global one-month sample (January 2020, 17,825 granules), 99.64 % of granules had identical fire-pixel counts, the largest per-granule difference was 3 pixels, and the totals were 404,057 (C6) vs 404,052 (C6.1), a relative change of 0.001 %. [MODIS C6/C6.1 User's Guide §2.1](https://www.earthdata.nasa.gov/s3fs-public/2023-09/MODIS_C6_C6.1_Fire_User_Guide_1.0.pdf) [confirmed; added]
- MODIS Collection 6 land products were decommissioned in summer 2023, and C6.1 land reprocessing was completed for all products by August 2023 (MODIS Land news page, last updated 2025-11-13). [MODIS Land News](https://modis-land.gsfc.nasa.gov/news.html) [confirmed; added]
- FIRMS NRT MODIS (MCD14DL) moved from Collection 6 to 6.1 in April 2021. [MCD14DL product page](https://modaps.modaps.eosdis.nasa.gov/services/about/products/c61-nrt/MCD14DL-NRT.html), [FIRMS FAQ](https://www.earthdata.nasa.gov/data/tools/firms/faq) [confirmed]

### MODIS Level 3 tiled products (1 km sinusoidal grid)

| Item | MOD14A1 V061 | MYD14A1 V061 | MOD14A2 V061 | MYD14A2 V061 |
|---|---|---|---|---|
| Content | Daily fire composite; eight daily layers packaged per file | Same as MOD14A1, Aqua | 8-day summary (maximum Level 2 class per cell over 8 days) | Same as MOD14A2, Aqua |
| Format | HDF-EOS2 (.hdf) | HDF-EOS2 | HDF-EOS2 | HDF-EOS2 (from GEE and the guide; the LP DAAC page was not opened) |
| Catalog temporal resolution | 1 day | 1 day | 8 days | - |
| Coverage (LP DAAC) | 2000-02-18 to present | 2002-07-04 to present | 2000-02-18 to present | not opened |
| DOI | 10.5067/MODIS/MOD14A1.061 | 10.5067/MODIS/MYD14A1.061 | 10.5067/MODIS/MOD14A2.061 | not opened |
| Layers | FireMask (uint8, 1-9, fill 0), MaxFRP (uint32, MW, scale 0.1, 0-180000), QA (uint8 bit field, 0-6), sample (uint16, 0-1353) | same | FireMask, QA (no MaxFRP, no sample) | FireMask, QA |
| Example file | `MOD14A1.A2025209.h13v09.061.2025217235634.hdf` | `MYD14A1.A2025209.h18v08.061.2025217235501.hdf` | `MOD14A2.A2025209.h26v06.061.2025218000221.hdf` | - |
| Source / status | [LP DAAC MOD14A1](https://www.earthdata.nasa.gov/data/catalog/lpcloud-mod14a1-061) [confirmed] | [LP DAAC MYD14A1](https://www.earthdata.nasa.gov/data/catalog/lpcloud-myd14a1-061) [confirmed] | [LP DAAC MOD14A2](https://www.earthdata.nasa.gov/data/catalog/lpcloud-mod14a2-061) [confirmed] | [GEE MYD14A2](https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MYD14A2) [confirmed only as existing; DOI and LP DAAC page unverified] |

- The guide says the daily Level 3 product is tile based. Each file spans one of the 460 MODIS tiles, 326 of which contain land pixels, and is a 1 km gridded composite of fire pixels for each 24-hour period. "For convenience, eight days of data are packaged into a single file." Files with fewer than eight days occasionally occur when data are missing. The 8-day composite (MOD14A2/MYD14A2) "is the maximum value of the individual Level 2 pixel classes that fell into each 1-km grid cell over the entire 8-day compositing period". [MODIS C6/C6.1 User's Guide §3.4-3.5](https://www.earthdata.nasa.gov/s3fs-public/2023-09/MODIS_C6_C6.1_Fire_User_Guide_1.0.pdf) [confirmed]
- MOD14A1 start date is listed as 2000-02-18 on LP DAAC but 2000-02-24 on Earth Engine and on the L2 MOD14 page. See Conflicts. [confirmed as a conflict]

### MODIS Climate Modeling Grid (CMG) fire products

- These are 0.25° global grids (1440 x 720 per layer) produced monthly (MOD14CMQ Terra, MYD14CMQ Aqua) and for 8-day periods (MOD14C8Q, MYD14C8Q), in HDF4. The naming prefix encodes satellite (O = Terra, Y = Aqua, C = combined Terra/Aqua), period (M = monthly, 8 = 8-day) and grid (H = 0.5°, Q = 0.25°). [MODIS C6/C6.1 User's Guide §3.6, §5.4](https://www.earthdata.nasa.gov/s3fs-public/2023-09/MODIS_C6_C6.1_Fire_User_Guide_1.0.pdf) [confirmed]
- The eight layers are CorrFirePix (int16, corrected fire-pixel count), CloudCorrFirePix (int16, also corrected for cloud cover), MeanCloudFraction (int8), RawFirePix (int16, uncorrected count), CloudPix (int32), TotalPix (int32), MeanFRP (float32, MW) and NumPixFRP (int16). [User's Guide Table 9](https://www.earthdata.nasa.gov/s3fs-public/2023-09/MODIS_C6_C6.1_Fire_User_Guide_1.0.pdf) [confirmed]
- File names follow `M?D14CM?.YYYYMM.CCC.VV.hdf` (monthly) and `M?D14C8?.YYYYDDD.CCC.VV.hdf` (8-day). The guide's examples are `MYD14CMQ.200412.006.01.hdf` and `MYD14C8Q.2004361.006.01.hdf`. [User's Guide §5.4.1, §5.4.5](https://www.earthdata.nasa.gov/s3fs-public/2023-09/MODIS_C6_C6.1_Fire_User_Guide_1.0.pdf) [confirmed]
- The CMG and MCD14ML products are hosted on the University of Maryland SFTP server fuoco.geog.umd.edu (login "fire"), not on LP DAAC. The monthly CMG directory is MODIS/C6/Mx14CMQ. [User's Guide §4.3](https://www.earthdata.nasa.gov/s3fs-public/2023-09/MODIS_C6_C6.1_Fire_User_Guide_1.0.pdf) [confirmed]
- Unlike MCD14ML, the CMG product removes static, persistent and other non-vegetation-fire hot spots. [User's Guide FAQ 8.7.3](https://www.earthdata.nasa.gov/s3fs-public/2023-09/MODIS_C6_C6.1_Fire_User_Guide_1.0.pdf) [confirmed; added]

### MCD14ML: MODIS global monthly fire location product (standard)

- MCD14ML holds every Terra and Aqua fire pixel for one calendar month in one plain ASCII file. Fields are fixed-width and space-delimited, with a one-line header. It was introduced in Collection 5. [User's Guide §3.7, §5.5](https://www.earthdata.nasa.gov/s3fs-public/2023-09/MODIS_C6_C6.1_Fire_User_Guide_1.0.pdf) [confirmed]

| Col | Name | Units | Meaning |
|---|---|---|---|
| 1 | YYYYMMDD | - | UTC date |
| 2 | HHMM | - | UTC hour and minute |
| 3 | sat | - | T = Terra, A = Aqua |
| 4-5 | lat, lon | degrees | Fire pixel centre |
| 6 | T21 | K | Band 21 brightness temperature |
| 7 | T31 | K | Band 31 brightness temperature |
| 8 | sample | - | Sample number, 0-1353 (a proxy for scan angle) |
| 9 | FRP | MW | Fire radiative power |
| 10 | conf | % | Detection confidence, 0-100 |
| 11 | type | - | 0 presumed vegetation fire, 1 active volcano, 2 other static land source, 3 offshore |
| 12 | dn | - | Day/night algorithm flag, D or N (version 2 and later) |

Source for the table: [User's Guide Table 10](https://www.earthdata.nasa.gov/s3fs-public/2023-09/MODIS_C6_C6.1_Fire_User_Guide_1.0.pdf) [confirmed]

- Types 0-2 apply only to land pixels, and every hot spot over water gets type 3. Type 2 covers hot spots detected on 16 or more days in any calendar year, plus hot spots in any urban area (urban areas taken from the Collection 6 MCD12Q1 land cover). [User's Guide §5.5](https://www.earthdata.nasa.gov/s3fs-public/2023-09/MODIS_C6_C6.1_Fire_User_Guide_1.0.pdf) [confirmed]
- File name: `MCD14ML.YYYYMM.CCC.VV.txt`, where VV is the product version within a collection (currently "03"). The SFTP directory is MODIS/C6/MCD14ML, with example `MCD14ML.201701.006.03.txt.gz`. [User's Guide §4.3, §5.5.1](https://www.earthdata.nasa.gov/s3fs-public/2023-09/MODIS_C6_C6.1_Fire_User_Guide_1.0.pdf) [confirmed]
- Version history: version 2 added one more decimal of lat/lon precision and the dn column. Version 3 has the same format but "significantly improved typing of hot spots". Version 1 has 11 columns with 3-decimal lat/lon. [User's Guide §5.5.2](https://www.earthdata.nasa.gov/s3fs-public/2023-09/MODIS_C6_C6.1_Fire_User_Guide_1.0.pdf) [confirmed]
- A monthly file typically has 200,000 to 500,000 lines. [User's Guide FAQ 8.7.2](https://www.earthdata.nasa.gov/s3fs-public/2023-09/MODIS_C6_C6.1_Fire_User_Guide_1.0.pdf) [confirmed; added]
- MCD14ML does not filter out non-vegetation hot spots. Users have to apply the type field themselves. [User's Guide FAQ 8.7.3](https://www.earthdata.nasa.gov/s3fs-public/2023-09/MODIS_C6_C6.1_Fire_User_Guide_1.0.pdf) [confirmed; added]
- The guide advises against using NRT MODIS fire locations for time-series or long-term studies and recommends the standard MCD14ML for that use. FIRMS distributes MCD14ML-derived subsets through its Archive Download Tool. [User's Guide §4.5](https://www.earthdata.nasa.gov/s3fs-public/2023-09/MODIS_C6_C6.1_Fire_User_Guide_1.0.pdf) [confirmed]
- No Collection 6.1-specific MCD14ML directory, version string or DOI was found. The only published path is MODIS/C6/MCD14ML (guide dated May 2021), and no DOI exists for MCD14ML on any page opened. [unverified]

### FIRMS MODIS: NRT (MCD14DL) vs standard (MCD14ML)

- MCD14DL is the FIRMS NRT MODIS product. Its DOI is 10.5067/FIRMS/MODIS/MCD14DL.NRT.0061 and its formats are TXT, SHP, KML and WMS ("only the TXT and SHP files contain all the attributes"). [MCD14DL page](https://modaps.modaps.eosdis.nasa.gov/services/about/products/c61-nrt/MCD14DL-NRT.html) [confirmed]
- Version strings in the FIRMS "version" column: 6.1URT (ultra real-time), 6.1RT (real-time), 6.1NRT (near real-time), 6.1 (standard). [MCD14DL page](https://modaps.modaps.eosdis.nasa.gov/services/about/products/c61-nrt/MCD14DL-NRT.html), [FIRMS attributes](https://www.earthdata.nasa.gov/data/tools/firms/active-fire-data-attributes-modis-viirs) [confirmed]
- Standard (MCD14ML-derived) data replace NRT data in FIRMS when available. The lag is stated four ways: "usually after 2 months" (MCD14DL page, NRT vs standard section), "3-month lag" (same page, Known Issues), "2-3 month lag" (FIRMS FAQ) and "approximately a 5 month lag" (FIRMS Archive Download page). See Conflicts. [confirmed as stated]
- NRT uses predicted attitude and ephemeris, while standard uses definitive values. Standard also fills missing granules and removes maneuver-degraded data. The added NRT geolocation error is typically under 100 m but can reach several km after spacecraft maneuvers or severe space weather. The degraded period lasts under about 2 hours for Terra, NOAA-20 and NOAA-21, and up to 12 hours for Aqua. [FIRMS FAQ](https://www.earthdata.nasa.gov/data/tools/firms/faq) [confirmed; maneuver durations added]
- Day/night definition: in standard/ML data, solar zenith angle above 85° is night and below 85° is day. In NRT data, day/night is set by orbit direction (ascending = day, descending = night). The FAQ says NRT "is expected to change to match standard processing". [FIRMS FAQ](https://www.earthdata.nasa.gov/data/tools/firms/faq) [confirmed]
- The type attribute (0-3) exists only in standard MCD14ML-derived data, not in NRT. [FIRMS attributes](https://www.earthdata.nasa.gov/data/tools/firms/active-fire-data-attributes-modis-viirs), [MCD14DL page](https://modaps.modaps.eosdis.nasa.gov/services/about/products/c61-nrt/MCD14DL-NRT.html) [confirmed]
- FIRMS latency: NRT under 3 hours globally. RT (real-time) is given as within 30 minutes of overpass in one FAQ section and within one hour in another. URT (ultra real-time) is given as "within a minute" in one place and "within 5 minutes" in another. [FIRMS FAQ](https://www.earthdata.nasa.gov/data/tools/firms/faq) [confirmed; RT/URT added]

### FIRMS attribute sets (CSV/SHP)

| Attribute | MODIS | VIIRS 375 m |
|---|---|---|
| latitude, longitude | Centre of 1 km pixel (may hold more than one fire) | Centre of nominal 375 m pixel |
| brightness temperature | `brightness` = band 21/22 (K) | `bright_ti4` = I4 (K) ("Brightness" in web services) |
| second BT | `bright_t31` = band 31 (K) | `bright_ti5` = I5 (K) ("Brightness_2" in web services) |
| scan, track | Actual pixel size, grows toward scan edge | Actual pixel size, about 375 m at nadir |
| acq_date, acq_time | Date; overpass time UTC | same |
| satellite | A = Aqua, T = Terra | N = Suomi NPP, N20 = NOAA-20, N21 = NOAA-21 |
| confidence | 0-100 % | Categorical: low, nominal, high |
| version | 6.1URT / 6.1RT / 6.1NRT / 6.1 | Collection 1: 1.0NRT, 1.0. Collection 2: 2.0URT, 2.0RT (from the VJ114IMGTDL_NRT page) |
| frp | MW | MW |
| type | 0-3, standard only | Not listed on FIRMS attributes page (present in Vxx14IMGML files) |
| daynight | D / N | D / N |

Sources: [FIRMS attributes](https://www.earthdata.nasa.gov/data/tools/firms/active-fire-data-attributes-modis-viirs) [confirmed], [VJ114IMGTDL_NRT page](https://modaps.modaps.eosdis.nasa.gov/services/about/products/viirs-land-c2-nrt/vj114imgtdl_nrt.html) for the 2.0URT and 2.0RT strings [corrected: the researcher attributed these strings to the VIIRS User's Guide, which does not contain them]

- VIIRS confidence classes: low confidence by day is typically sun glint plus an I4 anomaly under 15 K. Nominal is free of potential sun glint, or an I4 anomaly over 15 K by day or night. High is a saturated pixel, by day or night. Low-confidence night pixels occur only over the South Atlantic Anomaly (11°E to 110°W, about 7°N to 55°S) and "have been removed from the NRT data distributed by FIRMS". [FIRMS attributes](https://www.earthdata.nasa.gov/data/tools/firms/active-fire-data-attributes-modis-viirs), [VJ114IMGTDL_NRT page](https://modaps.modaps.eosdis.nasa.gov/services/about/products/viirs-land-c2-nrt/vj114imgtdl_nrt.html) [confirmed]
- No FIRMS page opened defines the meaning of "2.0NRT" or "2.0" as a VIIRS version string. [unverified]

### VIIRS 375 m Level 2 swath products (Collection 2, V002)

| Item | VNP14IMG (Suomi NPP) | VJ114IMG (NOAA-20) | VJ214IMG (NOAA-21) |
|---|---|---|---|
| Format | netCDF-4 (.nc) | netCDF-4 | netCDF-4 |
| Resolution | 375 m (I-band) | 375 m | 375 m |
| Granule | 6-minute swath, about 3,060 km x 3,060 km | same | same |
| LP DAAC coverage | 2012-01-17 to "present", but delivery ceased 2026-11-02 (day 2026/306) | 2018-01-01 to present | 2023-02-10 to present |
| DOI | 10.5067/VIIRS/VNP14IMG.002 | 10.5067/VIIRS/VJ114IMG.002 | 10.5067/VIIRS/VJ214IMG.002 |
| Example name | `VNP14IMG.A2025224.1542.002.2025227210549.nc` | `VJ114IMG.A2025219.0542.002.2025219145527.nc` | `VJ214IMG.A2026009.1642.002.2026014154305.nc` |
| Source / status | [LP DAAC VNP14IMG](https://www.earthdata.nasa.gov/data/catalog/lpcloud-vnp14img-002) [confirmed] | [LP DAAC VJ114IMG](https://www.earthdata.nasa.gov/data/catalog/lpcloud-vj114img-002) [confirmed] | [LP DAAC VJ214IMG](https://www.earthdata.nasa.gov/data/catalog/lpcloud-vj214img-002) [confirmed] |

- File name pattern: `VNP14IMG.AYYYYDDD.HHMM.VVV.YYYYDDDHHMMSS.nc` (acquisition date, acquisition time, version 002, production timestamp). The VNP14IMG page recommends VJ214IMG as the primary replacement for Suomi NPP and VJ114IMG as the secondary one. Applying accurate geolocation to VNP14IMG variables requires the VNP03MODLL geolocation product. [LP DAAC VNP14IMG](https://www.earthdata.nasa.gov/data/catalog/lpcloud-vnp14img-002) [confirmed; VNP03MODLL note added]
- A Level 2 granule is a 6-minute orbit segment of about 202 scans. I-band channels have 32 detectors per scan and 6,400 samples per row, giving a ground swath about 3,060 km wide. [VIIRS C2 User's Guide v1.2 §3.1.1](https://www.earthdata.nasa.gov/s3fs-public/2025-06/VIIRS_C2_AF-375m_User_Guide_1.2.pdf) [confirmed]
- The first VIIRS active fires were detected on 19 January 2012. Data from that day were affected by cooling of the onboard calibration sources, so "users should adopt 20 January 2012 as the effective start date of the VIIRS active fire data record". [VIIRS C2 User's Guide v1.2](https://www.earthdata.nasa.gov/s3fs-public/2025-06/VIIRS_C2_AF-375m_User_Guide_1.2.pdf) [confirmed]
- Collection 2 changes from Collection 1: the product uses Collection 2 NASA Level 1B radiance and geolocation inputs instead of the SDR (Sensor Data Record) inputs used for C1. This removes spuriously calibrated "bad scans". New L1B quality flags "virtually eliminate" C1's spurious detections, and better NetCDF compression makes files smaller. [VIIRS C2 User's Guide v1.2 §2](https://www.earthdata.nasa.gov/s3fs-public/2025-06/VIIRS_C2_AF-375m_User_Guide_1.2.pdf) [confirmed]
- User's Guide history: v1.0 May 2024, v1.1 November 2024, and v1.2 June 2025 ("Updated for v3 VxxIMG14ML + new Known issues section"). NOAA-20 and NOAA-21 launched in 2017 and 2022. [VIIRS C2 User's Guide v1.2](https://www.earthdata.nasa.gov/s3fs-public/2025-06/VIIRS_C2_AF-375m_User_Guide_1.2.pdf) [confirmed; added]
- For latency-insensitive science, the guide recommends the non-NRT VNP14IMG/VNP14 stream from LP DAAC and LAADS over NRT, and warns of possible NRT coverage gaps. [VIIRS C2 User's Guide v1.2 §4.3](https://www.earthdata.nasa.gov/s3fs-public/2025-06/VIIRS_C2_AF-375m_User_Guide_1.2.pdf) [confirmed; added]

### VIIRS monthly fire location products (Vxx14IMGML)

- Monthly CSV files are produced per platform: VNP14IMGML (S-NPP), VJ114IMGML (NOAA-20) and VJ214IMGML (NOAA-21). The name pattern is `Vxx14IMGML.YYYYMM.CC.VV.csv` (the guide prints "YYYMM", a typo), with xx = NP, J1 or J2, collection CC = "02" and product version VV = "03". The example is `VNP14IMGML.201801.C2.03.csv.gz`, which writes the collection as "C2" rather than "02". [VIIRS C2 User's Guide v1.2 §3.2.1, §4.2.1](https://www.earthdata.nasa.gov/s3fs-public/2025-06/VIIRS_C2_AF-375m_User_Guide_1.2.pdf) [confirmed; the naming inconsistency was added]
- Columns after a one-line header: YYYYMMDD, HHMM (UTC), Line, Sample (0-6399), Lat, Lon, T4, T5, MeanT4, MeanT5, MeanDT, MADT4, MADT5, MADDT (K), FRP (MW), Rad13, Mean13 (M13 radiance, W m-2 sr-1 µm-1), AdjC (0-8), AdjW (0-8), WinS (10-35), Confidence (L/N/H), DNFlag (D/N), SZA, SAA, VZA, VAA, Glint (degrees), Type (0 vegetation fire, 1 volcano, 2 other static land, 3 offshore including all water detections), and PixArea (I-band pixel area, km²). [VIIRS C2 User's Guide v1.2 §3.2.2](https://www.earthdata.nasa.gov/s3fs-public/2025-06/VIIRS_C2_AF-375m_User_Guide_1.2.pdf) [confirmed]
- Hosting: SFTP server fuoco.geog.umd.edu, directory data/VIIRS/C2/VNP14IMGML. Files are posted 1-2 months after all Level 2 granules for a month have been generated. The guide warns that converting a monthly file to shapefile can exceed the 2 GB shapefile limit. [VIIRS C2 User's Guide v1.2 §4.2](https://www.earthdata.nasa.gov/s3fs-public/2025-06/VIIRS_C2_AF-375m_User_Guide_1.2.pdf) [confirmed]
- Known issue: a production bug set the Type field inconsistently in versions 1 and 2, so obvious type-2 static sources were often labelled type 0. It was "corrected in May 2025 and all VxxIMGML product files reprocessed to version 3". [VIIRS C2 User's Guide v1.2 §6.1](https://www.earthdata.nasa.gov/s3fs-public/2025-06/VIIRS_C2_AF-375m_User_Guide_1.2.pdf) [confirmed]
- No DOI or Earthdata catalog page was found for the Vxx14IMGML files. [unverified]

### FIRMS VIIRS 375 m: NRT and standard names, DOIs, coverage

| Item | Suomi NPP | NOAA-20 | NOAA-21 |
|---|---|---|---|
| NRT short name | VNP14IMGTDL_NRT | VJ114IMGTDL_NRT | VJ214IMGTDL_NRT |
| NRT DOI | 10.5067/FIRMS/VIIRS/VNP14IMGT_NRT.002 | 10.5067/FIRMS/VIIRS/VJ114IMGT_NRT.002 | 10.5067/FIRMS/VIIRS/VJ214IMGT_NRT.002 |
| NRT formats | TXT, SHP, KML, WMS | same | same |
| Standard name in FIRMS FAQ | VNP14IMGTML | "VJ114MGTML" (typo in FAQ) | VJ214IMGTML |
| FIRMS FAQ availability | 20 Jan 2012 to 2 Nov 2026 | 1 Apr 2018 to present | 17 Jan 2024 to present |
| FIRMS Archive Download coverage | 20 Jan 2012 to 2 Nov 2026 | 1 Apr 2018 to present | 1 Mar 2023 to present |
| NRT catalog temporal start | 2016-01-01 | (MODAPS page lists 20 Jan 2012 for related standard VJ114IMGT) | 2026-10-01 (catalog, as of 2026-11-13) |

Sources: [FIRMS FAQ](https://www.earthdata.nasa.gov/data/tools/firms/faq), [FIRMS Archive Download](https://firms.modaps.eosdis.nasa.gov/download/), [VNP14IMGTDL_NRT catalog](https://www.earthdata.nasa.gov/data/catalog/lancemodis-vnp14imgtdl-nrt-2), [VJ114IMGTDL_NRT page](https://modaps.modaps.eosdis.nasa.gov/services/about/products/viirs-land-c2-nrt/vj114imgtdl_nrt.html), [VJ214IMGTDL_NRT catalog](https://www.earthdata.nasa.gov/data/catalog/lancemodis-vj214imgtdl-nrt-2). [confirmed, with these corrections: the researcher said the VJ214IMGTDL_NRT catalog lists 2024-01-10 and describes itself as "VNP14IMG_NRT". On 2026-11-13 the catalog lists 2026-10-01 to present and names itself VJ214IMGTDL_NRT. NOAA-20 and NOAA-21 NRT DOIs added.]

- NRT latency is under 3 hours globally. The standard monthly files have a 2-3 month lag (FAQ). [FIRMS FAQ](https://www.earthdata.nasa.gov/data/tools/firms/faq) [confirmed]
- The VJ114IMGTDL_NRT page says standard VJ114IMGT data are "usually available after about 2 months" through the FIRMS download tool. [VJ114IMGTDL_NRT page](https://modaps.modaps.eosdis.nasa.gov/services/about/products/viirs-land-c2-nrt/vj114imgtdl_nrt.html) [confirmed; added]
- Suomi NPP: "Production and delivery of new FIRMS data from Suomi NPP ceased at 15:40 UTC on November 2, 2026". The LP DAAC Suomi NPP pages give "November 2, 2026 (2026/306)". [FIRMS FAQ](https://www.earthdata.nasa.gov/data/tools/firms/faq), [LP DAAC VNP14IMG](https://www.earthdata.nasa.gov/data/catalog/lpcloud-vnp14img-002) [confirmed]
- Orbit phasing, as worded in the FIRMS FAQ: "NOAA-21 is flying half an orbit, or 50 minutes, ahead of NOAA-20, with Suomi NPP between them". Elsewhere the same FAQ says "NOAA-20/21 passes over the equator about 50 minutes ahead of Suomi NPP at approximately 12:40 p.m. and 12:40 a.m." These two statements are not mutually consistent (see Conflicts). The VIIRS instrument on JPSS-2/NOAA-21 launched on 10 November 2022. [FIRMS FAQ](https://www.earthdata.nasa.gov/data/tools/firms/faq) [corrected: the researcher's claim that NOAA-21 is "about 50 minutes ahead of NOAA-20" omitted the conflicting second statement]
- FIRMS Archive Download formats are shapefile, CSV and JSON for hotspot data older than the last 7 days. It requires Earthdata Login or an emailed code. Burned-area products are delivered as HDF, GeoTIFF or shapefile from the UMD SFTP server. [FIRMS Archive Download](https://firms.modaps.eosdis.nasa.gov/download/) [confirmed]

### FIRMS MODIS coverage and known gaps

- Terra MODIS in FIRMS covers 1 November 2000 to present ("high-quality observations from November 2000"). Aqua covers July 2002 to present (high-quality from 4 July 2002). The FIRMS Archive Download lists MODIS C6.1 from 1 November 2000 to present. [FIRMS FAQ](https://www.earthdata.nasa.gov/data/tools/firms/faq), [FIRMS Archive Download](https://firms.modaps.eosdis.nasa.gov/download/) [confirmed]
- Known MODIS gaps listed in the FAQ: 15 April 2001, 15 June to 3 July 2001, and 19-28 March 2002. They are attributed to instrument outages or days with unusually low fire counts. [FIRMS FAQ](https://www.earthdata.nasa.gov/data/tools/firms/faq) [confirmed]
- The researcher's Terra 10:30 / Aqua 13:30 crossing times were not found in the parts of the FAQ that were read. The nominal design times appear in the Terra article (10:30 AM) and on MODIS Land News (Aqua 1:30 PM). Both have drifted (see the status section). [Terra: The End of An Era](https://science.nasa.gov/science-research/earth-science/terra-the-end-of-an-era/), [MODIS Land News](https://modis-land.gsfc.nasa.gov/news.html) [corrected source]

### VIIRS 750 m and gridded products

| Item | VNP14 V001 (S-NPP, 750 m) | VNP14 V002 (S-NPP, 750 m) | VNP14A1 V001 | VNP14A1 V002 | VJ114A1 V002 | VJ214A1 V002 |
|---|---|---|---|---|---|---|
| Type | L2 6-min swath, about 3,060 km | L2 6-min swath | Daily L3, 1 km | Daily L3, 1 km SIN tiles | Daily L3, 1 km | Daily L3, 1 km |
| Format | Listed HDF-EOS5, but example name ends .nc | netCDF-4 | HDF-EOS5 | HDF-EOS5 (.h5) | HDF-EOS5 (.h5) | HDF-EOS5 (.h5) |
| Coverage | 2012-01-19 to 2024-06-17 | 2012-01-17 to present; delivery ceased 2026-11-02 | 2012-01-19 to 2024-06-16 | 2012-01-17 to present; delivery ceased 2026-11-02 | 2018-01-01 to present | 2023-02-10 to present |
| DOI | 10.5067/VIIRS/VNP14.001 | 10.5067/VIIRS/VNP14.002 | 10.5067/VIIRS/VNP14A1.001 | 10.5067/VIIRS/VNP14A1.002 | 10.5067/VIIRS/VJ114A1.002 | 10.5067/VIIRS/VJ214A1.002 |
| Status | Deprecated; decommissioned 2025-04-08 | Active state, no new data | Deprecated; decommissioned 2025-04-08 | Active state, no new data | Active | Active |
| Example | `VNP14.A2024169.0530.001.2024169125255.nc` | `VNP14.A2025227.0548.002.2025227231352.nc` | - | `VNP14A1.A2025222.h24v07.002.2025224172143.h5` | `VJ114A1.A2025222.h12v08.002.2025223083701.h5` | `VJ214A1.A2026007.h28v13.002.2026015165059.h5` |
| Source | [VNP14 V001](https://www.earthdata.nasa.gov/data/catalog/lpcloud-vnp14-001) [confirmed] | [VNP14 V002](https://www.earthdata.nasa.gov/data/catalog/lpcloud-vnp14-002) [added] | [VNP14A1 V001](https://www.earthdata.nasa.gov/data/catalog/lpcloud-vnp14a1-001) [confirmed; dates are from the V001 page, not the V002 page the researcher cited] | [VNP14A1 V002](https://www.earthdata.nasa.gov/data/catalog/lpcloud-vnp14a1-002) [confirmed] | [VJ114A1](https://www.earthdata.nasa.gov/data/catalog/lpcloud-vj114a1-002) [added] | [VJ214A1](https://www.earthdata.nasa.gov/data/catalog/lpcloud-vj214a1-002) [added] |

- VNP14A1, VJ114A1 and VJ214A1 layers: FireMask (uint8, 0-9), MaxFRP (int32, MW, scale 0.1, fill 0), QA (uint8 bit field, 0-6) and sample (int16, 0-3199, fill -1). The sample range 0-3199 matches 3,200 M-band (750 m) samples per row, compared with 0-6399 for the 375 m I-band. This suggests the 1 km VIIRS daily grid is built from the 750 m VNP14 swath product rather than from VNP14IMG. That link is inferred, not stated on the page. [VNP14A1 V002](https://www.earthdata.nasa.gov/data/catalog/lpcloud-vnp14a1-002), [VJ114A1](https://www.earthdata.nasa.gov/data/catalog/lpcloud-vj114a1-002) [confirmed layers; inference unverified]
- The VNP14 V001 page says it is superseded by V002 for SNPP (VNP14, DOI 10.5067/VIIRS/VNP14.002) and NOAA-20 (VJ114, DOI 10.5067/VIIRS/VJ114.002). [VNP14 V001](https://www.earthdata.nasa.gov/data/catalog/lpcloud-vnp14-001) [added]
- VNP14A1 V002 recommends VJ214A1 as the primary Suomi NPP replacement and VJ114A1 as the secondary one. [VNP14A1 V002](https://www.earthdata.nasa.gov/data/catalog/lpcloud-vnp14a1-002) [confirmed]
- VNP14 (750 m) uses an adaptation of the C6 MODIS MOD14/MYD14 algorithm and performs comparably to Aqua MYD14 (1 km). VNP14IMG usually detects more fire pixels, especially at night. Global 2021 C2 statistics: by day, VNP14IMG had about 3 times as many fire pixels as VNP14, 53 % of VNP14IMG day pixels had no VNP14 match, and 11 % of VNP14 day pixels had no VNP14IMG match. By night, VNP14IMG had about 17 times as many, 85 % had no VNP14 match, and 0.8 % of VNP14 night pixels had no VNP14IMG match. [VIIRS C2 User's Guide v1.2 §1, §7](https://www.earthdata.nasa.gov/s3fs-public/2025-06/VIIRS_C2_AF-375m_User_Guide_1.2.pdf) [confirmed; statistics added]
- Sampling: the 3,060 km VIIRS swath gives about 15 % overlap between consecutive orbits at the equator and full global coverage every 12 h. Nominal S-NPP equator crossings are 1:30 pm and 1:30 am. Mid-latitudes get 3-4 looks per day. [VIIRS C2 User's Guide v1.2 §7](https://www.earthdata.nasa.gov/s3fs-public/2025-06/VIIRS_C2_AF-375m_User_Guide_1.2.pdf) [confirmed]

### Google Earth Engine dataset IDs

| GEE ID | Content | Dates shown on page (2026-11-13) | Bands | Status |
|---|---|---|---|---|
| `MODIS/061/MOD14A1` | Terra daily, 1 km | 2000-02-24 to 2026-11-08 | FireMask, MaxFRP (MW, scale 0.1), sample, QA | [GEE](https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MOD14A1) [confirmed] |
| `MODIS/061/MYD14A1` | Aqua daily, 1 km | 2002-07-04 to 2026-11-08 | same | [GEE](https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MYD14A1) [confirmed] |
| `MODIS/061/MOD14A2` | Terra 8-day, 1 km | 2000-02-18 to 2026-11-01 | FireMask, QA | [GEE](https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MOD14A2) [confirmed] |
| `MODIS/061/MYD14A2` | Aqua 8-day, 1 km | 2002-07-04 to 2026-11-01 | FireMask, QA | [GEE](https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MYD14A2) [added] |
| `NASA/VIIRS/002/VNP14A1` | S-NPP daily, 1 km | 2012-01-19 to 2026-11-02 | FireMask, MaxFRP, QA, sample | [GEE](https://developers.google.com/earth-engine/datasets/catalog/NASA_VIIRS_002_VNP14A1) [confirmed] |
| `NOAA/VIIRS/001/VNP14A1` | S-NPP daily V001, deprecated, superseded by NASA/VIIRS/002/VNP14A1 | 2012-01-19 to 2024-06-16 | - | [GEE](https://developers.google.com/earth-engine/datasets/catalog/NOAA_VIIRS_001_VNP14A1) [confirmed] |
| `FIRMS` | Daily 1 km raster of LANCE NRT MODIS (MOD14/MYD14) points | 2000-11-01 to 2026-11-11 | T21 (K), confidence (%), line_number | [GEE](https://developers.google.com/earth-engine/datasets/catalog/FIRMS) [confirmed] |
| `NASA/LANCE/SNPP_VIIRS/C2` | Daily 375 m raster of VNP14IMGTDL_NRT points | 2023-09-03 to 2026-11-02 | Bright_ti4, Bright_ti5, confidence (0-2), line_number, frp, acq_epoch, acq_time, DayNight | [GEE](https://developers.google.com/earth-engine/datasets/catalog/NASA_LANCE_SNPP_VIIRS_C2) [added] |
| `NASA/LANCE/NOAA20_VIIRS/C2` | Daily 375 m raster of VJ114IMGTDL_NRT points | 2023-10-08 to 2026-11-13 | same as above | [GEE](https://developers.google.com/earth-engine/datasets/catalog/NASA_LANCE_NOAA20_VIIRS_C2) [added] |
| `MODIS/061/MCD64A1` | Burned area, 500 m, monthly | 2000-11-01 to 2026-09-01 | BurnDate, Uncertainty, QA, FirstDay, LastDay | [GEE](https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MCD64A1) [confirmed] |

- In the GEE `FIRMS` collection, each point gets a 1 km bounding box rasterized onto the MODIS sinusoidal grid. Where boxes overlap, the higher-confidence detection is kept, and on a tie the brighter one. It is NRT, "not considered science quality", and carries no FRP, satellite or type band. [GEE FIRMS](https://developers.google.com/earth-engine/datasets/catalog/FIRMS) [confirmed]
- The GEE LANCE VIIRS C2 rasters are also NRT and "not considered to be of science quality". No GEE dataset for NOAA-21 (VJ214IMGTDL_NRT) or for VJ114A1/VJ214A1 was found. [GEE SNPP C2](https://developers.google.com/earth-engine/datasets/catalog/NASA_LANCE_SNPP_VIIRS_C2) [corrected: the researcher said no official GEE VIIRS 375 m fire dataset exists, but two LANCE NRT rasters exist]
- Community (unofficial) GEE assets: `projects/sat-io/open-datasets/MODIS_MCD14DL/MCD14DL_YYYY` (2000-2020) and `projects/sat-io/open-datasets/VIIRS/VNP14IMGTDL_NRT_YYYY` (2012-2021). These are yearly FIRMS shapefile exports ingested as vector FeatureCollections and curated outside NASA and Google. [GEE community catalog](https://gee-community-catalog.org/projects/firms_vector/) [confirmed; secondary source]

### Burned area vs active fire

- MCD64A1 V061 (MODIS Terra+Aqua burned area): HDF-EOS2, 500 m, monthly, 2000-11-01 to present, DOI 10.5067/MODIS/MCD64A1.061. It uses a burn-sensitive vegetation index from SWIR bands 5 and 7 plus a temporal texture measure, with dynamic thresholds, combined with 1 km MODIS active fire observations, to assign a burn date (day of year 1-366) to each 500 m cell. Layers: Burn Date, Burn Date Uncertainty, First Day, Last Day, QA. [LP DAAC MCD64A1](https://www.earthdata.nasa.gov/data/catalog/lpcloud-mcd64a1-061) [confirmed]
- VNP64A1 V002 (VIIRS S-NPP burned area): listed as HDF-EOS5 (the page also says .hdf), 500 m, monthly, 2012-03-01 to present, DOI 10.5067/VIIRS/VNP64A1.002. It uses 750 m VIIRS imagery (SWIR M8, M11) and 750 m VIIRS active fires, and is modelled on the MODIS combined product for continuity. S-NPP delivery ceased 2026-11-02. [LP DAAC VNP64A1](https://www.earthdata.nasa.gov/data/catalog/lpcloud-vnp64a1-002) [confirmed]
- Active-fire products record a thermal anomaly in a pixel at overpass time, as a point or pixel with FRP. Burned-area products record which 500 m cells burned in a month and on which day, from post-fire surface change. One is a count of detections and the other is an area, so they are not interchangeable. [LP DAAC MCD64A1](https://www.earthdata.nasa.gov/data/catalog/lpcloud-mcd64a1-061) [confirmed]

### Current mission status (2025-2026), added

- Earthdata alert of 2 May 2025 (page last updated 6 November 2026): Terra and Aqua "will begin shutting down operations" in "late 2026/early 2027", after which MODIS data will no longer be collected and a final MODIS reprocessing will take place. Both platforms are drifting out of their designed orbits. Users are told to explore similar VIIRS products. [Earthdata: Transition from MODIS to VIIRS](https://www.earthdata.nasa.gov/data/alerts-outages/transition-from-modis-viirs) [confirmed]
- NASA Science article (29 December 2025, updated 20 March 2026): end-of-science is projected for February 2027 for Terra and September 2027 for Aqua because of fuel and power limits. Terra's design crossing was 10:30 AM mean local time, and it was crossing at 10:15 AM by fall 2022. MODIS was still operating. [Terra: The End of An Era](https://science.nasa.gov/science-research/earth-science/terra-the-end-of-an-era/) [confirmed]
- MODIS Land News (last updated 2025-11-13) gives earlier end dates: December 2025 for Terra and August 2026 for Aqua. It says Aqua began drifting to a later crossing in July 2021, passed 1:45 PM in February 2023, and was projected to reach about 3:50 PM by August 2026. The last Terra maneuver is given as 27 February 2020 and Aqua's final maneuvers as 18 March 2021. [MODIS Land News](https://modis-land.gsfc.nasa.gov/news.html) [confirmed; conflicts with the later NASA article]
- LDOPE issue HC_MOD_26008 (opened 2026-01-08): orbit drift "has impacted MODIS data", affecting pixel size, spacing, scan gaps, bowtie overlap and diurnal-cycle sampling. Terra's final IAM and DMU were in 2022, Aqua's in 2021. [LDOPE issue 1254](https://landweb.modaps.eosdis.nasa.gov/displayissue?id=1254) [confirmed]
- LANCE User Working Group talk (May 2025, University of Maryland fire team): Terra's final IAM, DMU and a 6 km altitude decrease were in 2022, and Aqua's final IAM and DMU in 2021. The MODIS 1 km pixel had shrunk to about 970 m along-scan by spring 2025. Scan gaps at nadir were projected (Lin et al., 2023) to widen from about 1/2 to about 1¼ 250 m pixels by December 2026 for Terra and July 2026 for Aqua. The talk says the impact of drift on MODIS fire products "is under active investigation", and that spatial-sampling impacts "seem to have abruptly increased in magnitude in late 2024". [Giglio, LANCE UWG May 2025](https://landweb.modaps.eosdis.nasa.gov/data/filePost/LANCE_UWG_Orbit_Drift_Giglio_202505.pdf) [confirmed]
- MODIS Level 1 Version 7.0 (calibrated radiances MOD02/MYD02 at 250 m, 500 m and 1 km, plus MOD03/MYD03 geolocation) was released by LAADS (alert March 2026). Version 6.1 Level 1 is to be decommissioned on 30 September 2026. No statement about a Collection 7 MOD14/MYD14 or MCD14ML was found. [Earthdata: Version 7.0 MODIS L1](https://www.earthdata.nasa.gov/data/alerts-outages/version-7.0-modis-calibrated-radiances-geolocation-data-products-now-available) [confirmed]
- MODIS Land News (as of 2025-11-13) said Collection 7 land reprocessing was "planned to begin in summer of 2025". Whether a C7 fire product has been released was not found. [MODIS Land News](https://modis-land.gsfc.nasa.gov/news.html) [confirmed as plan; outcome unverified]
- On 2026-11-13 the MOD14/MYD14 V061 LP DAAC pages show ACTIVE with no end-of-mission notice, and the GEE MOD14A1/MYD14A1 collections run to 2026-11-08. MODIS fire data were therefore still being produced in early November 2026. [LP DAAC MOD14](https://www.earthdata.nasa.gov/data/catalog/lpcloud-mod14-061), [GEE MYD14A1](https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MYD14A1) [confirmed]

## Why these matter for combining the records

MODIS (1 km, MCD14ML) and VIIRS (375 m, Vxx14IMGML) standard records are distributed in different formats: fixed-width text vs CSV. They also use different column names and different confidence scales (0-100 % numeric for MODIS vs L/N/H categories for VIIRS), so fields must be mapped explicitly rather than by name. Both products carry a type field that separates vegetation fires from volcanoes, static industrial or urban sources and offshore detections. That field exists only in the standard products, not in FIRMS NRT. VIIRS type values before the May 2025 version-3 reprocessing were unreliable. Recent months in any FIRMS pull are NRT, which uses a different day/night rule (orbit direction vs solar zenith angle above 85°) and can carry geolocation errors after maneuvers. The NRT-to-standard replacement lag is quoted anywhere from 2 to 5 months. Record boundaries matter for any monthly series. The series is Terra-only from November 2000 to early July 2002, with known gaps in 2001 and March 2002. VIIRS starts 20 January 2012 (S-NPP), 2018 (NOAA-20) and 2023/2024 (NOAA-21). S-NPP ends at 15:40 UTC on 2 November 2026, and Terra and Aqua are expected to end between late 2026 and 2027. MODIS overpass times have drifted and its pixel geometry has changed since 2021-2022, which affects detection counts within the MODIS record itself. Gridded and Earth Engine products (MOD14A1, VNP14A1, the GEE FIRMS raster) collapse multiple detections into one cell value, so their counts are not the same as point counts. The 1 km VIIRS daily grid appears to come from the 750 m product, not the 375 m one.

## Conflicts and unverified items

1. **MOD14/MYD14 granule across-track size.** About 2,300 km per LP DAAC ([MOD14 catalog](https://www.earthdata.nasa.gov/data/catalog/lpcloud-mod14-061)). About 2,340 km per the User's Guide (May 2021, [guide](https://www.earthdata.nasa.gov/s3fs-public/2023-09/MODIS_C6_C6.1_Fire_User_Guide_1.0.pdf)). The guide is the more specific algorithm-team source, and the catalog value looks rounded.
2. **Fire-pixel table count (resolved).** The guide's 27 SDSs plus Fire Mask, Algorithm QA and CMG_night equal the catalog's 30 variables. There is no real conflict.
3. **MOD14A1 start date.** 2000-02-18 per LP DAAC ([MOD14A1](https://www.earthdata.nasa.gov/data/catalog/lpcloud-mod14a1-061)) vs 2000-02-24 per GEE ([GEE MOD14A1](https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MOD14A1)) and the MOD14 L2 page. The first L2 granule is 2000-02-24, so 2000-02-18 is most likely the start of the first 8-day file period (day 049). That explanation is inference.
4. **MOD14A1 temporal resolution.** LP DAAC lists "1 day" while each file packages eight daily layers. The guide confirms daily composites, eight per file. The two statements are consistent once read together.
5. **NRT-to-standard lag.** "Usually after 2 months" and "3-month lag" (both on the [MCD14DL page](https://modaps.modaps.eosdis.nasa.gov/services/about/products/c61-nrt/MCD14DL-NRT.html)). "2-3 month lag" ([FIRMS FAQ](https://www.earthdata.nasa.gov/data/tools/firms/faq)). "Approximately a 5 month lag" ([FIRMS Archive Download](https://firms.modaps.eosdis.nasa.gov/download/), current page). For VIIRS, 1-2 months after all granules exist ([VIIRS guide](https://www.earthdata.nasa.gov/s3fs-public/2025-06/VIIRS_C2_AF-375m_User_Guide_1.2.pdf)). The Archive Download page is the operational tool, so its 5-month figure probably best reflects current practice. This is not confirmed.
6. **NOAA-20 VIIRS start.** 2018-01-01 for VJ114IMG and VJ114A1 at LP DAAC vs 1 April 2018 in FIRMS (FAQ and Archive Download).
7. **NOAA-21 VIIRS start.** 2023-02-10 for VJ214IMG and VJ214A1 at LP DAAC, 1 March 2023 on FIRMS Archive Download, 17 January 2024 in the FIRMS FAQ, and 2026-10-01 in the VJ214IMGTDL_NRT catalog entry today (the researcher saw 2024-01-10 earlier). The catalog value appears to be a metadata reset, not a true start.
8. **S-NPP VIIRS start.** 2012-01-17 at LP DAAC (VNP14IMG, VNP14A1 V002, VNP14 V002), 2012-01-19 (VNP14 V001, VNP14A1 V001, GEE VNP14A1) and 20 January 2012 (User's Guide effective start, FIRMS). The User's Guide is authoritative for science use (20 January 2012). The VNP14IMGTDL_NRT catalog lists a 2016-01-01 start. The researcher's mention of a "V2 released April 2024 covering 2018 onward" announcement was not opened and is [unverified].
9. **VIIRS orbit phasing in the FIRMS FAQ.** "NOAA-21 is flying half an orbit, or 50 minutes, ahead of NOAA-20, with Suomi NPP between them" vs "NOAA-20/21 passes over the equator about 50 minutes ahead of Suomi NPP at approximately 12:40". Both quotes are from the same page ([FIRMS FAQ](https://www.earthdata.nasa.gov/data/tools/firms/faq)). They cannot both be exact. A NOAA/JPSS primary source should be used for phasing.
10. **FIRMS VIIRS standard product names.** VNP14IMGTML, "VJ114MGTML" and VJ214IMGTML (FIRMS FAQ) vs VNP14IMGML, VJ114IMGML and VJ214IMGML (VIIRS User's Guide). FIRMS's "T" names refer to its vector extracts of the ML files. "VJ114MGTML" is a typo.
11. **Vxx14IMGML collection field.** "CC = 02" in the naming rule vs "C2" in the example file names (same guide).
12. **VNP14 V001 format.** Listed as HDF-EOS5, but the example name ends in .nc ([VNP14 V001](https://www.earthdata.nasa.gov/data/catalog/lpcloud-vnp14-001)). V002 is netCDF-4.
13. **VNP64A1 format.** Listed HDF-EOS5 but described with .hdf files ([VNP64A1](https://www.earthdata.nasa.gov/data/catalog/lpcloud-vnp64a1-002)).
14. **Terra/Aqua end dates.** Terra: December 2025 ([MODIS Land News](https://modis-land.gsfc.nasa.gov/news.html), updated 2025-11-13) vs February 2027 ([NASA Science](https://science.nasa.gov/science-research/earth-science/terra-the-end-of-an-era/), updated 2026-03-20). Aqua: August 2026 vs September 2027. Earthdata says "late 2026/early 2027". The NASA Science article is the most recent.
15. **Terra final maneuver.** 27 February 2020 (MODIS Land News), "late 2020" (NASA Science), and 2022 for the final IAM+DMU (LDOPE and Giglio 2025). These may refer to different maneuver types.
16. **GEE VIIRS NRT end dates.** These differ between locale and cached versions of pages (search snippets showed 2025-10-16 and others). The English pages fetched today show 2026-11-02 (SNPP) and 2026-11-13 (NOAA-20).
17. **[unverified]** "2.0NRT" and "2.0" as FIRMS VIIRS version strings, and their meaning.
18. **[unverified]** UTC as the time base in the MOD14/VNP14IMG file-name HHMM. This is from memory: the catalog pages say only "acquisition time". MCD14ML and Vxx14IMGML columns are explicitly UTC.
19. **[unverified]** That VNP14A1 is gridded from the 750 m VNP14 rather than the 375 m VNP14IMG. This is inferred from the sample range 0-3199.

## Open questions

- Is there a Collection 6.1 (or Collection 7) MCD14ML path, version string or DOI? The only published path is MODIS/C6/MCD14ML, product version 03.
- Will MOD14/MYD14 be reprocessed to Collection 7 on the new Version 7.0 Level 1B? If so, will FIRMS and MCD14ML switch, and how large will the C6.1 to C7 difference be?
- What are the actual shutdown dates for Terra and Aqua MODIS science data (projected between late 2026 and September 2027), and when does FIRMS MODIS NRT stop?
- What has the UMD fire team concluded about the effect of orbit drift on MODIS fire counts? As of May 2025 it was "under active investigation".
- Have the FIRMS standard VIIRS extracts been regenerated from the May 2025 version-3 Vxx14IMGML files, and do FIRMS VIIRS downloads carry a type field?
- Exact orbit phasing of NOAA-20, NOAA-21 and S-NPP from a NOAA/JPSS primary source, since the FIRMS FAQ is internally inconsistent.
- Is there an Earthdata catalog page or DOI for MYD14A2 V061 and for the Vxx14IMGML files? Neither was opened or found.
- Earth Engine datasets for NOAA-21 VIIRS fire and for VJ114A1/VJ214A1 were not found.

## Sources

- MODIS/Terra Thermal Anomalies/Fire 5-Min L2 Swath 1km V061 (MOD14): https://www.earthdata.nasa.gov/data/catalog/lpcloud-mod14-061
- MODIS/Aqua Thermal Anomalies/Fire 5-Min L2 Swath 1km V061 (MYD14): https://www.earthdata.nasa.gov/data/catalog/lpcloud-myd14-061
- MOD14A1 V061: https://www.earthdata.nasa.gov/data/catalog/lpcloud-mod14a1-061
- MYD14A1 V061: https://www.earthdata.nasa.gov/data/catalog/lpcloud-myd14a1-061
- MOD14A2 V061: https://www.earthdata.nasa.gov/data/catalog/lpcloud-mod14a2-061
- MODIS Collection 6 and 6.1 Active Fire Product User's Guide v1.0 (May 2021): https://www.earthdata.nasa.gov/s3fs-public/2023-09/MODIS_C6_C6.1_Fire_User_Guide_1.0.pdf (identical copy: https://lpdaac.usgs.gov/documents/1005/MOD14_User_Guide_V61.pdf)
- VIIRS Collection 2 375 m Active Fire Product User's Guide v1.2 (June 2025): https://www.earthdata.nasa.gov/s3fs-public/2025-06/VIIRS_C2_AF-375m_User_Guide_1.2.pdf
- VNP14IMG V002: https://www.earthdata.nasa.gov/data/catalog/lpcloud-vnp14img-002
- VJ114IMG V002: https://www.earthdata.nasa.gov/data/catalog/lpcloud-vj114img-002
- VJ214IMG V002: https://www.earthdata.nasa.gov/data/catalog/lpcloud-vj214img-002
- VNP14 V001: https://www.earthdata.nasa.gov/data/catalog/lpcloud-vnp14-001
- VNP14 V002: https://www.earthdata.nasa.gov/data/catalog/lpcloud-vnp14-002
- VNP14A1 V001: https://www.earthdata.nasa.gov/data/catalog/lpcloud-vnp14a1-001
- VNP14A1 V002: https://www.earthdata.nasa.gov/data/catalog/lpcloud-vnp14a1-002
- VJ114A1 V002: https://www.earthdata.nasa.gov/data/catalog/lpcloud-vj114a1-002
- VJ214A1 V002: https://www.earthdata.nasa.gov/data/catalog/lpcloud-vj214a1-002
- MCD64A1 V061: https://www.earthdata.nasa.gov/data/catalog/lpcloud-mcd64a1-061
- VNP64A1 V002: https://www.earthdata.nasa.gov/data/catalog/lpcloud-vnp64a1-002
- FIRMS FAQ: https://www.earthdata.nasa.gov/data/tools/firms/faq
- FIRMS Active Fire Data Attributes: https://www.earthdata.nasa.gov/data/tools/firms/active-fire-data-attributes-modis-viirs
- FIRMS Archive Download: https://firms.modaps.eosdis.nasa.gov/download/
- MCD14DL NRT product page (LANCE/MODAPS): https://modaps.modaps.eosdis.nasa.gov/services/about/products/c61-nrt/MCD14DL-NRT.html
- VJ114IMGTDL_NRT product page (LANCE/MODAPS): https://modaps.modaps.eosdis.nasa.gov/services/about/products/viirs-land-c2-nrt/vj114imgtdl_nrt.html
- VNP14IMGTDL_NRT catalog: https://www.earthdata.nasa.gov/data/catalog/lancemodis-vnp14imgtdl-nrt-2
- VJ214IMGTDL_NRT catalog: https://www.earthdata.nasa.gov/data/catalog/lancemodis-vj214imgtdl-nrt-2
- Earth Engine MOD14A1: https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MOD14A1
- Earth Engine MYD14A1: https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MYD14A1
- Earth Engine MOD14A2: https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MOD14A2
- Earth Engine MYD14A2: https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MYD14A2
- Earth Engine VNP14A1 V002: https://developers.google.com/earth-engine/datasets/catalog/NASA_VIIRS_002_VNP14A1
- Earth Engine VNP14A1 V001 (deprecated): https://developers.google.com/earth-engine/datasets/catalog/NOAA_VIIRS_001_VNP14A1
- Earth Engine FIRMS: https://developers.google.com/earth-engine/datasets/catalog/FIRMS
- Earth Engine LANCE SNPP VIIRS C2: https://developers.google.com/earth-engine/datasets/catalog/NASA_LANCE_SNPP_VIIRS_C2
- Earth Engine LANCE NOAA-20 VIIRS C2: https://developers.google.com/earth-engine/datasets/catalog/NASA_LANCE_NOAA20_VIIRS_C2
- Earth Engine MCD64A1: https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MCD64A1
- GEE community catalog, archival FIRMS vectors (secondary): https://gee-community-catalog.org/projects/firms_vector/
- Earthdata alert, Transition from MODIS to VIIRS (2025-05-02): https://www.earthdata.nasa.gov/data/alerts-outages/transition-from-modis-viirs
- Earthdata alert, Version 7.0 MODIS L1 products (March 2026): https://www.earthdata.nasa.gov/data/alerts-outages/version-7.0-modis-calibrated-radiances-geolocation-data-products-now-available
- NASA Science, Terra: The End of An Era (2025-12-29): https://science.nasa.gov/science-research/earth-science/terra-the-end-of-an-era/
- MODIS Land Team News: https://modis-land.gsfc.nasa.gov/news.html
- LDOPE issue, MODIS Terra/Aqua Drift (2026-01-08): https://landweb.modaps.eosdis.nasa.gov/displayissue?id=1254
- Giglio, Terra/Aqua Orbit-Drift Update, LANCE UWG (May 2025): https://landweb.modaps.eosdis.nasa.gov/data/filePost/LANCE_UWG_Orbit_Drift_Giglio_202505.pdf
