# FIRMS hotspot file schema for MODIS and VIIRS

Verified 2026-11-13. "FIRMS" is NASA's Fire Information for Resource Management System. "NRT" means near-real-time processing through LANCE, which delivers data within about 3 hours. "RT" (real-time) and "URT" (ultra-real-time) are faster, temporary streams. "SP" or "standard" means science-quality processing, which uses definitive satellite position and attitude. "ML" refers to the monthly fire-location products: MCD14ML for MODIS and Vxx14IMGML for VIIRS.

Status tags: [confirmed] means the page linked at the end of the line was opened during verification and supports the fact. [corrected] means the researcher's value was wrong or incomplete and the line gives the verified value. [unverified] means the fact could not be confirmed on a page; each one says why.

One verification method needs explaining. To see the literal column headers and values, I opened four FIRMS yearly per-country CSV files of about 200 bytes each. I also tabulated the `version` and `satellite` columns in one small file (800 to 4,000 bytes) per year. These are files on FIRMS's own server, listed in its index `yearly_summary_files.txt`. No dataset was bulk-downloaded and no MAP_KEY was used. Values seen this way are labelled "observed in file".

## Key facts

### 1. Documented attribute tables (FIRMS NRT documentation)

The FIRMS documentation page lists these attributes. The column names in actual CSV files are lower-case (see section 2).

| Attribute (doc name) | MODIS (MCD14DL NRT) | VIIRS 375 m (Vxx14IMGTDL NRT) | Source |
|---|---|---|---|
| Latitude, Longitude | Centre of the 1 km fire pixel, "not necessarily the actual location of the fire" | Centre of the nominal 375 m fire pixel | [FIRMS attributes](https://www.earthdata.nasa.gov/data/tools/firms/active-fire-data-attributes-modis-viirs), [MCD14DL page](https://modaps.modaps.eosdis.nasa.gov/services/about/products/c61-nrt/MCD14DL-NRT.html) [confirmed] |
| Brightness / Bright_ti4 | `brightness`: channel 21/22 brightness temperature in K | `bright_ti4`: I-4 channel brightness temperature in K (called "Brightness" in web services) | [FIRMS attributes](https://www.earthdata.nasa.gov/data/tools/firms/active-fire-data-attributes-modis-viirs) [confirmed] |
| Scan, Track | Along-scan and along-track pixel size. "Scan and track reflect actual pixel size." The pixel is 1 km at nadir and grows toward the scan edge. | Along-scan and along-track pixel size, about 375 m at nadir | [MCD14DL page](https://modaps.modaps.eosdis.nasa.gov/services/about/products/c61-nrt/MCD14DL-NRT.html), [FIRMS attributes](https://www.earthdata.nasa.gov/data/tools/firms/active-fire-data-attributes-modis-viirs) [confirmed] |
| Acq_Date, Acq_Time | "Time of acquisition/overpass of the satellite (in UTC)" | Same wording | [MCD14DL page](https://modaps.modaps.eosdis.nasa.gov/services/about/products/c61-nrt/MCD14DL-NRT.html), [VNP14IMGTDL page](https://modaps.modaps.eosdis.nasa.gov/services/about/products/viirs-land-c2-nrt/vnp14imgtdl_nrt.html) [confirmed] |
| Satellite | "A = Aqua and T = Terra" (documented) | "N = Suomi NPP, N20 = NOAA-20 (formerly JPSS-1), N21 = NOAA-21" | [MCD14DL page](https://modaps.modaps.eosdis.nasa.gov/services/about/products/c61-nrt/MCD14DL-NRT.html), [VNP14IMGTDL page](https://modaps.modaps.eosdis.nasa.gov/services/about/products/viirs-land-c2-nrt/vnp14imgtdl_nrt.html) [confirmed]. **Actual MODIS CSVs say `Terra`/`Aqua` (section 2)** [corrected] |
| Confidence | 0–100 %, grouped into low, nominal and high classes | Classes low, nominal and high | [FIRMS attributes](https://www.earthdata.nasa.gov/data/tools/firms/active-fire-data-attributes-modis-viirs) [confirmed] |
| Version | "6.1URT", "6.1RT", "6.1NRT", "6.1" (standard) | Documented as "1.0NRT", "2.0URT", "2.0RT", "1.0" (standard). **Actual files say `2.0NRT` and `2` (section 2)** | [MCD14DL page](https://modaps.modaps.eosdis.nasa.gov/services/about/products/c61-nrt/MCD14DL-NRT.html), [VNP14IMGTDL page](https://modaps.modaps.eosdis.nasa.gov/services/about/products/viirs-land-c2-nrt/vnp14imgtdl_nrt.html) [corrected] |
| Bright_T31 / Bright_ti5 | `bright_t31`: channel 31 brightness temperature in K | `bright_ti5`: I-5 channel brightness temperature in K (called "Brightness_2" in web services) | [FIRMS attributes](https://www.earthdata.nasa.gov/data/tools/firms/active-fire-data-attributes-modis-viirs) [confirmed] |
| FRP | Pixel-integrated fire radiative power in MW | FRP in MW. The retrieval is a hybrid of 375 m and 750 m data and has used channel M13 since 2015. Sub-pixel FRP is reliable only for small or low-intensity fires. | [FIRMS attributes](https://www.earthdata.nasa.gov/data/tools/firms/active-fire-data-attributes-modis-viirs) [confirmed] |
| Type | 0 = presumed vegetation fire, 1 = active volcano, 2 = other static land source, 3 = offshore. "Only available for MCD14ML (standard quality) data." | Not listed in the NRT table | [FIRMS attributes](https://www.earthdata.nasa.gov/data/tools/firms/active-fire-data-attributes-modis-viirs) [confirmed] |
| DayNight | D = daytime fire, N = nighttime fire | D or N | [FIRMS attributes](https://www.earthdata.nasa.gov/data/tools/firms/active-fire-data-attributes-modis-viirs) [confirmed] |

- The VIIRS confidence classes are defined as follows. Low: daytime pixels, typically sun glint with an I-4 temperature anomaly under 15 K. Nominal: pixels free of sun-glint contamination with a strong anomaly above 15 K, day or night. High: saturated pixels, day or night. Low-confidence nighttime pixels occur only in a region of about 11° E to 110° W and 7° N to 55° S, linked to the South Atlantic Magnetic Anomaly, and "have been removed from the NRT data distributed by FIRMS." [VNP14IMGTDL page](https://modaps.modaps.eosdis.nasa.gov/services/about/products/viirs-land-c2-nrt/vnp14imgtdl_nrt.html), [FIRMS attributes](https://www.earthdata.nasa.gov/data/tools/firms/active-fire-data-attributes-modis-viirs) [confirmed]. The researcher attached the quote "less than 100 meters" to this fact. That quote supports the geolocation fact below, not the confidence definitions.
- Older documentation gave NOAA-20 the satellite code `1` ("1=NOAA-20 (designated JPSS-1 prior to launch)"). This text survives on a secondary mirror of old NASA wording. The archived 2020 NASA page itself returned no readable content. [GEE community catalog (secondary)](https://gee-community-catalog.org/projects/firms_vector/) [confirmed on a secondary source only]. Historical NOAA-20 NRT text files from third parties may therefore contain `1`.
- The NRT text products come as TXT, SHP, KML and WMS, and "only the TXT and SHP files contain all the attributes." [MCD14DL page](https://modaps.modaps.eosdis.nasa.gov/services/about/products/c61-nrt/MCD14DL-NRT.html), [VNP14IMGTDL page](https://modaps.modaps.eosdis.nasa.gov/services/about/products/viirs-land-c2-nrt/vnp14imgtdl_nrt.html) [confirmed]
- MODIS Collection 6.1 NRT data replaced Collection 6 in April 2021. NRT records are replaced with data derived from the standard MCD14ML product, "usually after about 2 months." [MCD14DL page](https://modaps.modaps.eosdis.nasa.gov/services/about/products/c61-nrt/MCD14DL-NRT.html) [confirmed]

### 2. Literal CSV columns and values as delivered

**Area API, NRT (MODIS_NRT and VIIRS_NOAA20_NRT).** These examples come from FIRMS Academy output dated June 2025. [FIRMS API tutorial](https://firms.modaps.eosdis.nasa.gov/content/academy/data_api/firms_api_use.html) [confirmed]
- VIIRS header: `latitude,longitude,bright_ti4,scan,track,acq_date,acq_time,satellite,instrument,confidence,version,bright_ti5,frp,daynight`. Example values: satellite `N20`, instrument `VIIRS`, confidence `l`/`n`/`h` (lower case), version `2.0NRT`.
- MODIS header from the country endpoint: `country_id,latitude,longitude,brightness,scan,track,acq_date,acq_time,satellite,instrument,confidence,version,bright_t31,frp,daynight`. Example values: country_id `PER`, satellite **`Terra` / `Aqua`** (words, not T/A), instrument `MODIS`, confidence integer, version `6.1NRT`.
- The NRT outputs have no `type` column. The header includes an `instrument` column, which the documentation tables do not list.

**VIIRS S-NPP NRT sample CSV.** Loaded with pandas, it has 14 columns: latitude, longitude, bright_ti4, scan, track (float64); acq_date (string, `2023-07-12`); acq_time (int64, "integer between 0..2359", for example `3`, `410`, `1950`); satellite `N`; instrument `VIIRS`; confidence `l`/`n`/`h`; version `2.0NRT` and `2.0URT` mixed in one file; bright_ti5, frp (float64); daynight `D`/`N`. [FIRMS data-ingest tutorial](https://firms.modaps.eosdis.nasa.gov/content/academy/data_ingest/firms_data_ingest.html) [confirmed]

**Yearly per-country CSVs (standard data, observed in file).** [Country file index](https://firms.modaps.eosdis.nasa.gov/data/country/yearly_summary_files.txt), [example MODIS file](https://firms.modaps.eosdis.nasa.gov/data/country/modis_2025_Kiribati.csv), [example S-NPP file](https://firms.modaps.eosdis.nasa.gov/data/country/viirs-snpp_2025_Palau.csv), [example NOAA-20 file](https://firms.modaps.eosdis.nasa.gov/data/country/viirs-jpss1_2025_Federated_States_of_Micronesia.csv) [confirmed, observed in file]

| Item | MODIS (`modis_YYYY_Country.csv`) | VIIRS S-NPP (`viirs-snpp_…`) and NOAA-20 (`viirs-jpss1_…`) |
|---|---|---|
| Header | `latitude,longitude,brightness,scan,track,acq_date,acq_time,satellite,instrument,confidence,version,bright_t31,frp,daynight,type` | `latitude,longitude,bright_ti4,scan,track,acq_date,acq_time,satellite,instrument,confidence,version,bright_ti5,frp,daynight,type` |
| satellite | `Terra`, `Aqua` | `N` (S-NPP), `N20` (NOAA-20) |
| instrument | `MODIS` | `VIIRS` |
| confidence | Integer 0–100 | `l`, `n`, `h` (lower case) |
| version | `6.2` for years 2000–2017, `6.03` for 2018–2022, `61.03` for 2023–2025 (one sampled file per year) | `2` (all years sampled: 2012, 2016, 2020, 2022, 2025) |
| acq_date | `YYYY-MM-DD` | `YYYY-MM-DD` |
| acq_time | Four-digit, zero-padded `HHMM` text, e.g. `0130` | Same, e.g. `0459` |
| scan / track | One decimal place, e.g. `1`, `1.1`, `3` / `1.7` | Two decimal places, e.g. `0.36` / `0.58`, `0.73` / `0.76` |
| type | Present, values 0–3 | Present, values 0–3 (type `2` seen in a NOAA-20 2019 file) |
| daynight | `D` / `N` | `D` / `N` |

- The yearly country files cover these years. MODIS: 2000–2025 (26 years). VIIRS S-NPP: 2012–2025. VIIRS NOAA-20 (`viirs-jpss1`): 2018–2025. There are **no NOAA-21 country files**. Each year also has an `…_all_countries.zip`. The 2025 files were last updated on 2026-10-10. [Country file index](https://firms.modaps.eosdis.nasa.gov/data/country/yearly_summary_files.txt) [corrected; the researcher's claim that country summaries ran "only through 2021" is out of date]
- The readme bundled with the country files says the data are in WGS84 geographic projection. It also says: "Use the Collection / Version field to distinguish between NRT and standard data." [AttributesReadme.txt](https://firms.modaps.eosdis.nasa.gov/data/country/AttributesReadme.txt) [confirmed]
- The country files use the same column names as the API, plus `type`. They have no `country_id` column; the API's country endpoint adds one. [FIRMS API tutorial](https://firms.modaps.eosdis.nasa.gov/content/academy/data_api/firms_api_use.html), [country file](https://firms.modaps.eosdis.nasa.gov/data/country/modis_2003_Malta.csv) [confirmed, observed in file]

**Third-party schema (apis.io).** It gives satellite examples "Terra, Aqua, Suomi-NPP, NOAA-20, NOAA-21" and versions such as "6.1SP". The primary files show `Terra`/`Aqua` for MODIS but `N`/`N20` for VIIRS, and no "SP" suffix was seen. [apis.io (secondary)](https://apis.io/schemas/nasa-firms/fire-detection/) [corrected]

### 3. acq_date and acq_time

- acq_date and acq_time are in UTC. The Area API notes that its dates are based on GMT. [MCD14DL page](https://modaps.modaps.eosdis.nasa.gov/services/about/products/c61-nrt/MCD14DL-NRT.html), [FIRMS API tutorial](https://firms.modaps.eosdis.nasa.gov/content/academy/data_api/firms_api_use.html) [confirmed]
- The format of acq_time differs between files:
  - In the country CSVs it is a four-digit zero-padded HHMM string (observed `0130`, `0459`).
  - The FIRMS tutorial reads it as an integer from 0 to 2359, e.g. `3` for 00:03. Leading zeros are lost on parsing and may also be absent in the raw API text; the raw API bytes were not inspected.
  - acq_date is `YYYY-MM-DD`.

  [FIRMS data-ingest tutorial](https://firms.modaps.eosdis.nasa.gov/content/academy/data_ingest/firms_data_ingest.html), [country file](https://firms.modaps.eosdis.nasa.gov/data/country/viirs-snpp_2025_Palau.csv) [confirmed]
- In the monthly products the time field is "UTC hour (HH) and minute (MM)" for MODIS and "UTC detection hour (HH) and minute (MM)" for VIIRS. Neither guide says whether the time is per pixel or per granule. [MODIS C6/6.1 User's Guide §5.5](https://earthdata.nasa.gov/s3fs-public/2023-09/MODIS_C6_C6.1_Fire_User_Guide_1.0.pdf), [VIIRS C2 User's Guide v1.2 §3.2.2](https://www.earthdata.nasa.gov/s3fs-public/2025-06/VIIRS_C2_AF-375m_User_Guide_1.2.pdf) [confirmed]
- A VIIRS Level-2 granule is a 6-minute orbit segment of about 202 scans. The HHMM in the granule file name is the "approximate beginning time". [VIIRS C2 User's Guide v1.2 §3.1.1, §4.1](https://www.earthdata.nasa.gov/s3fs-public/2025-06/VIIRS_C2_AF-375m_User_Guide_1.2.pdf) [confirmed]. A MODIS granule covers 5 minutes [unverified, from memory].
- **Inference from observed data (not stated by NASA):** MODIS acq_time values in country files include `1858`, `1837`, `1823` and `0051`. These are not multiples of 5 minutes, which is where MODIS 5-minute granule start times fall. So MODIS acq_time is probably the scan or pixel time to the minute rather than the granule start time. [country file](https://firms.modaps.eosdis.nasa.gov/data/country/modis_2025_Jordan.csv), [MODIS guide example rows §5.5](https://earthdata.nasa.gov/s3fs-public/2023-09/MODIS_C6_C6.1_Fire_User_Guide_1.0.pdf) [unverified; this is an inference]

### 4. Version strings and processing streams

| Stream | MODIS (documented) | MODIS (observed) | VIIRS (documented) | VIIRS (observed) |
|---|---|---|---|---|
| URT | `6.1URT` | — | `2.0URT` | `2.0URT` |
| RT | `6.1RT` | — | `2.0RT` | — |
| NRT | `6.1NRT` | `6.1NRT` (API, 2025) | `1.0NRT` | `2.0NRT` (API and sample, 2023–2025) |
| Standard | `6.1` | `6.2`, `6.03`, `61.03` in country files | `1.0` | `2` in country files |

Sources: [MCD14DL page](https://modaps.modaps.eosdis.nasa.gov/services/about/products/c61-nrt/MCD14DL-NRT.html), [VNP14IMGTDL page](https://modaps.modaps.eosdis.nasa.gov/services/about/products/viirs-land-c2-nrt/vnp14imgtdl_nrt.html), [FIRMS API tutorial](https://firms.modaps.eosdis.nasa.gov/content/academy/data_api/firms_api_use.html), [data-ingest tutorial](https://firms.modaps.eosdis.nasa.gov/content/academy/data_ingest/firms_data_ingest.html), [country files](https://firms.modaps.eosdis.nasa.gov/data/country/yearly_summary_files.txt) [corrected: VIIRS NRT is `2.0NRT`, not `1.0NRT`; the standard-processing strings in files differ from the documentation]

- RT and URT records carry a version followed by "RT" or "URT"; NRT records carry a version followed by "NRT". RT and URT data are removed once the matching NRT detections are processed, or when they are older than 6 hours. [FIRMS FAQ](https://www.earthdata.nasa.gov/data/tools/firms/faq), [Area API](https://firms.modaps.eosdis.nasa.gov/api/area/) [confirmed]

### 5. Day/night flag

- The `daynight` value is `D` or `N` everywhere. How it is assigned depends on the stream. Standard (ML) processing uses solar zenith angle, with values above 85° labelled night. NRT uses orbit direction: ascending is day, descending is night. The FAQ says the NRT rule is expected to change to match standard processing. [FIRMS FAQ](https://www.earthdata.nasa.gov/data/tools/firms/faq) [confirmed]

### 6. Geolocation accuracy

| Case | Value | Source |
|---|---|---|
| NRT, MODIS and VIIRS | Extra error from predicted rather than definitive attitude and ephemeris is "routinely less than 100 meters" | [MCD14DL page](https://modaps.modaps.eosdis.nasa.gov/services/about/products/c61-nrt/MCD14DL-NRT.html), [VNP14IMGTDL page](https://modaps.modaps.eosdis.nasa.gov/services/about/products/viirs-land-c2-nrt/vnp14imgtdl_nrt.html) [confirmed] |
| NRT after maneuvers or space weather | Up to several km. This lasts under about 2 h for Terra and NOAA-20/21, and up to 12 h for Aqua. | [FIRMS FAQ](https://www.earthdata.nasa.gov/data/tools/firms/faq) [confirmed] |
| MODIS standard (C6.1) | Nadir-equivalent RMSE: Terra 43 m track / 45 m scan; Aqua 46 m track / 53 m scan. Goal is about 20 % of a 250 m pixel, i.e. 50 m at nadir. (MCST presentation, 18 Nov 2019) | [MCST MODIS geolocation status](https://mcst.gsfc.nasa.gov/sites/default/files/meetings_files/06_MODIS_GEO_Lin.pdf) [confirmed; added] |
| VIIRS standard | Nadir-equivalent RMSE: S-NPP C1 59 m track / 52 m scan; NOAA-20 C1 58 / 55 m; NOAA-20 C2 55 / 49 m. All under 75 m, which is 20 % of the I-band pixel. (Lin et al., SPIE 2020) | [Lin et al. 2020, NTRS](https://ntrs.nasa.gov/api/citations/20210026335/downloads/1150112.pdf) [confirmed; added] |

These are sensor geolocation figures. The FIRMS point is the centre of a pixel that is 1 km (MODIS) or 375 m (VIIRS) at nadir and larger off nadir. So the position of the fire inside the pixel is uncertain on a much larger scale than these geolocation errors.

### 7. Monthly ML products (UMD SFTP), for comparison with FIRMS CSVs

- **MCD14ML (MODIS)** is a plain ASCII file with fixed-width, space-delimited fields and a one-line header: `YYYYMMDD HHMM sat lat lon T21 T31 sample FRP conf type dn`.
  - Units and values: `sat` is T or A; lat and lon are in degrees at the pixel centre; T21 and T31 are in K; `sample` ranges 0–1353; FRP is in MW; `conf` is a percentage from 0 to 100; `type` is 0–3; `dn` is D or N.
  - There are no scan or track columns.
  - Files are named `MCD14ML.YYYYMM.CCC.VV.txt`, with VV currently "03".
  - Version 2 and later add one decimal of lat/lon precision and the `dn` column. Version 3 keeps the version-2 format but types hot spots much better.

  [MODIS C6/6.1 User's Guide §5.5](https://earthdata.nasa.gov/s3fs-public/2023-09/MODIS_C6_C6.1_Fire_User_Guide_1.0.pdf) [confirmed]
- **MODIS type rules.** Types 0–2 apply only to land pixels; any detection over water is type 3. Type 2 covers hot spots detected on 16 or more days in a calendar year, plus detections in any urban area (from the C6 MCD12Q1 land cover). Some static sources remain unflagged even in version 3. [MODIS guide §5.5, §7.2.3](https://earthdata.nasa.gov/s3fs-public/2023-09/MODIS_C6_C6.1_Fire_User_Guide_1.0.pdf) [confirmed]
- **Vxx14IMGML (VIIRS)** is a comma-separated file with a one-line header.
  - Name pattern: `Vxx14IMGML.YYYYMM.CC.VV.csv`, where xx is NP (S-NPP), J1 (NOAA-20) or J2 (NOAA-21). CC is "currently 02" and VV is "currently 03". The guide's own listing shows `VNP14IMGML.201801.C2.03.csv.gz`, so the collection field is written `C2`.
  - Columns: YYYYMMDD, HHMM (UTC), Line, Sample (0–6399), Lat, Lon, T4, T5, MeanT4, MeanT5, MeanDT, MADT4, MADT5, MADDT (all in K), FRP (MW), Rad13, Mean13 (W m⁻² sr⁻¹ µm⁻¹), AdjC, AdjW (0–8), WinS (10–35), Confidence (`L`/`N`/`H`, upper case), DNFlag (D/N), SZA, SAA, VZA, VAA, Glint (degrees), Type (0–3), PixArea (km²).

  [VIIRS C2 User's Guide v1.2 §3.2](https://www.earthdata.nasa.gov/s3fs-public/2025-06/VIIRS_C2_AF-375m_User_Guide_1.2.pdf) [confirmed, with the CC detail corrected]
- **VIIRS ML type bug.** In product versions 1 and 2, the Type field was set inconsistently, and obvious type-2 sources were often labelled 0. The bug was fixed in May 2025 and all files were reprocessed to version 3. [VIIRS C2 guide §6.1](https://www.earthdata.nasa.gov/s3fs-public/2025-06/VIIRS_C2_AF-375m_User_Guide_1.2.pdf) [confirmed]

### 8. Record coverage, latency and access

| Item | Value | Source |
|---|---|---|
| Archive download coverage | MODIS C6.1: 1 Nov 2000 to present. VIIRS S-NPP: 20 Jan 2012 to 2 Nov 2026. NOAA-20: 1 Apr 2018 to present. NOAA-21: 1 Mar 2023 to present. | [Archive Download](https://firms.modaps.eosdis.nasa.gov/download/) [confirmed] |
| Archive formats | SHP, CSV, JSON, for data older than the last 7 days | [Archive Download](https://firms.modaps.eosdis.nasa.gov/download/) [confirmed] |
| NRT to standard lag | About 5 months (archive page); 2–3 months (FAQ); about 2 months (MCD14DL page) | see Conflicts [confirmed, sources disagree] |
| NOAA-21 NRT in FIRMS | 17 Jan 2024 to present (VJ214IMGTDL_NRT) | [FIRMS FAQ](https://www.earthdata.nasa.gov/data/tools/firms/faq) [confirmed] |
| S-NPP effective record start | 20 Jan 2012. First detections were on 19 Jan 2012, while on-board calibration sources were cooling. | [VIIRS C2 guide §1, §4](https://www.earthdata.nasa.gov/s3fs-public/2025-06/VIIRS_C2_AF-375m_User_Guide_1.2.pdf) [confirmed] |
| API data availability (June 2025 example) | MODIS_SP 2000-11-01 to 2025-01-31. VIIRS_SNPP_SP 2012-01-20 to 2025-02-28. VIIRS_NOAA20_SP 2018-04-01 to 2025-02-28. VIIRS_NOAA21_NRT from 2024-01-17. No VIIRS_NOAA21_SP row was listed then. | [FIRMS API tutorial](https://firms.modaps.eosdis.nasa.gov/content/academy/data_api/firms_api_use.html) [confirmed; added] |
| Area API | `/api/area/csv/[MAP_KEY]/[SOURCE]/[AREA]/[DAY_RANGE]/[DATE]`. Sources: LANDSAT_NRT, MODIS_NRT, MODIS_SP, VIIRS_NOAA20_NRT/SP, VIIRS_NOAA21_NRT/SP, VIIRS_SNPP_NRT/SP. DAY_RANGE is 1–5. DATE is YYYY-MM-DD. AREA is west,south,east,north or `world`. Limit is 5,000 transactions per 10 minutes. | [Area API](https://firms.modaps.eosdis.nasa.gov/api/area/) [confirmed] |
| NRT web files | SHP, KML and CSV for the last 24 h, 48 h and 7 days, updated every 60 min. TXT files for the last 2 months. | [FIRMS FAQ](https://www.earthdata.nasa.gov/data/tools/firms/faq) [confirmed] |
| Use of NRT for time series | The MODIS guide says NRT fire locations "should not be used for time series analyses or long-term studies". | [MODIS guide §4.4–4.5](https://earthdata.nasa.gov/s3fs-public/2023-09/MODIS_C6_C6.1_Fire_User_Guide_1.0.pdf) [confirmed] |
| VIIRS coverage | Swath of about 3060 km with about 15 % overlap between orbits at the equator, giving global coverage every 12 h. S-NPP equator crossings are at 13:30 and 01:30. Mid-latitudes get 3–4 looks per day. | [VIIRS C2 guide §7](https://www.earthdata.nasa.gov/s3fs-public/2025-06/VIIRS_C2_AF-375m_User_Guide_1.2.pdf) [confirmed] |

### 9. Status changes and outages affecting the schema or record

- **Suomi NPP end.** The FIRMS banner reads: "Suomi NPP is no longer delivering new data." A FIRMS blog post of 27 Oct 2026 says production and delivery cease "at 13:00 Universal Time (UTC) on November 2, 2026." The FIRMS FAQ gives 15:40 UTC on 2 Nov 2026 (see Conflicts). Historical S-NPP data remain available. API users are told to switch from VIIRS_SNPP_NRT/SP to VIIRS_NOAA20_NRT or VIIRS_NOAA21_NRT. [FIRMS blog](https://www.earthdata.nasa.gov/news/blog/transitioning-from-s-npp-viirs-omps-what-nasa-firms-users-need-know), [FIRMS attributes](https://www.earthdata.nasa.gov/data/tools/firms/active-fire-data-attributes-modis-viirs), [Earthdata alert](https://www.earthdata.nasa.gov/data/alerts-outages/content/data-alert-history/21880) [confirmed]
- **MODIS status.** The same blog says MODIS remains available but users should plan to transition. Terra is currently the only morning overpass. When Aqua ends, NOAA-20 and NOAA-21 will cover the afternoon orbit. [FIRMS blog](https://www.earthdata.nasa.gov/news/blog/transitioning-from-s-npp-viirs-omps-what-nasa-firms-users-need-know) [confirmed; added]
- **Aqua outage.** The Aqua formatter-multiplexer unit (FMU) failed on 16 Aug 2020, and regular science telemetry was lost for about two weeks (16 Aug – 2 Sep 2020). Products were generated from limited Direct Broadcast data during the gap. [MODIS guide §7.2.4](https://earthdata.nasa.gov/s3fs-public/2023-09/MODIS_C6_C6.1_Fire_User_Guide_1.0.pdf) [confirmed]

## Why these matter for combining the records

- The same physical attribute is stored under different column names for each sensor (`brightness`/`bright_t31` versus `bright_ti4`/`bright_ti5`). The brightness values come from different spectral bands.
- Confidence uses incompatible scales: an integer 0–100 for MODIS, and `l`/`n`/`h` letters for VIIRS. The letters are lower case in FIRMS CSVs and upper case `L`/`N`/`H` in the VIIRS monthly product.
- The satellite field mixes words (`Terra`, `Aqua`) with codes (`N`, `N20`, `N21`). Older third-party NOAA-20 files may carry `1`.
- The literal `version` strings in standard files (`6.2`, `6.03`, `61.03`, `2`) do not match the documentation (`6.1`, `1.0`). This matters because the version field is the documented way to tell NRT from standard records.
- The `type` column exists only in standard files. In NRT files it is absent, so static-source information is missing for the most recent months.
- The day/night flag is assigned by different rules in NRT and standard processing.
- acq_time is UTC and appears either as zero-padded text or as an integer, which changes how a value such as `0051` parses.
- Coverage starts and ends differ by satellite: S-NPP stops on 2 Nov 2026, NOAA-21 starts in 2023 or 2024 depending on the stream, and there are no NOAA-21 country files.

## Conflicts and unverified items

1. **MODIS satellite codes.** The documentation says `T`/`A` ([MCD14DL page](https://modaps.modaps.eosdis.nasa.gov/services/about/products/c61-nrt/MCD14DL-NRT.html); MCD14ML `sat` column, [MODIS guide](https://earthdata.nasa.gov/s3fs-public/2023-09/MODIS_C6_C6.1_Fire_User_Guide_1.0.pdf)). FIRMS API and country CSVs say `Terra`/`Aqua` ([API tutorial, 2025](https://firms.modaps.eosdis.nasa.gov/content/academy/data_api/firms_api_use.html); [country files, updated 2026-10-10](https://firms.modaps.eosdis.nasa.gov/data/country/modis_2025_Jordan.csv)). The files themselves are authoritative for what a parser will see. `T`/`A` applies to MCD14ML text files and possibly to legacy NRT TXT files.
2. **VIIRS version string.** The documentation lists `1.0NRT` and `1.0` ([FIRMS attributes](https://www.earthdata.nasa.gov/data/tools/firms/active-fire-data-attributes-modis-viirs), [VNP14IMGTDL page](https://modaps.modaps.eosdis.nasa.gov/services/about/products/viirs-land-c2-nrt/vnp14imgtdl_nrt.html)). The FIRMS Academy outputs (2023 and 2025) show `2.0NRT` and `2.0URT`, and the country files show `2`. The observed values are more authoritative for current data. The documentation tables appear stale since the move to VIIRS Collection 2.
3. **MODIS standard version string.** The documentation says `6.1`. Country files show `6.2` (2000–2017), `6.03` (2018–2022) and `61.03` (2023–2025), with one file sampled per year. These may encode collection plus MCD14ML file version (C6 v02, C6 v03, C6.1 v03). That reading is an inference and is not documented. If it is right, country files for 2000–2022 may be Collection 6 rather than 6.1. Unresolved.
4. **NRT-to-standard lag.** About 5 months ([Archive Download](https://firms.modaps.eosdis.nasa.gov/download/), current); 2–3 months ([FIRMS FAQ](https://www.earthdata.nasa.gov/data/tools/firms/faq)); about 2 months ([MCD14DL page](https://modaps.modaps.eosdis.nasa.gov/services/about/products/c61-nrt/MCD14DL-NRT.html)). The archive page is the operational statement for FIRMS. The API availability example from June 2025 showed SP data ending 4–5 months before the query date, which is consistent with about 5 months.
5. **S-NPP cutoff time.** 13:00 UTC on 2 Nov 2026 ([FIRMS blog, 27 Oct 2026](https://www.earthdata.nasa.gov/news/blog/transitioning-from-s-npp-viirs-omps-what-nasa-firms-users-need-know)) versus 15:40 UTC on 2 Nov 2026 ([FIRMS FAQ](https://www.earthdata.nasa.gov/data/tools/firms/faq), current). A search snippet also mentioned an Earthdata alert giving 1 Nov 2026; I did not confirm this on an opened page. The FAQ is newer and may give the actual time production stopped, while the blog gives the planned time. The archive coverage date of 2 Nov 2026 is consistent with both.
6. **NOAA-21 start date.** The archive page gives 1 Mar 2023 ([Archive Download](https://firms.modaps.eosdis.nasa.gov/download/)). The FAQ gives 17 Jan 2024 for NRT, which matches the API availability for VIIRS_NOAA21_NRT ([FAQ](https://www.earthdata.nasa.gov/data/tools/firms/faq), [API tutorial](https://firms.modaps.eosdis.nasa.gov/content/academy/data_api/firms_api_use.html)). The 2023 start presumably comes from standard reprocessing; this is not confirmed.
7. **Yearly country summaries "only through 2021".** This came from the researcher's search summary of a forum post. It is contradicted by the current file index, which has files through 2025 ([index](https://firms.modaps.eosdis.nasa.gov/data/country/yearly_summary_files.txt)). Corrected.
8. **Unverified:** that the MODIS granule length is 5 minutes (from memory); that acq_time is a pixel or scan time rather than a granule time (inference from minute values only); and the units of scan and track. NASA does not state the unit, but the values (MODIS about 1–4.8, VIIRS about 0.32–0.8) are consistent with km.
9. **Unverified:** the exact headers of Archive Download CSVs (`fire_archive_*.csv` / `fire_nrt_*.csv`). No NASA page lists them, and the downloads require a request. They are presumably the same as the country files (standard, with `type`) and the API NRT output (no `type`).

## Open questions

- Do Area API `*_SP` outputs include the `type` column, and do they use the same `version` strings as the country files (`61.03`, `2`)? No SP API example was found.
- Is the raw acq_time in Area API CSVs zero-padded (`0051`) or not (`51`)? Only pandas-parsed output was seen.
- What do the MODIS standard version strings `6.2`, `6.03` and `61.03` mean, and are the 2000–2022 country files Collection 6 or 6.1?
- Is there a NASA statement on whether acq_time is a pixel, scan or granule time?
- Has the NRT day/night rule been changed to the solar-zenith (85°) rule, and from what date?
- Will NOAA-21 yearly country files and a VIIRS_NOAA21_SP history back to March 2023 be published?
- What satellite code appears for NOAA-21 in standard files? It is expected to be `N21` per the documentation but was not observed.

## Sources

- Active Fire Data Attributes MODIS and VIIRS (Earthdata FIRMS): https://www.earthdata.nasa.gov/data/tools/firms/active-fire-data-attributes-modis-viirs
- FIRMS FAQ (Earthdata): https://www.earthdata.nasa.gov/data/tools/firms/faq
- MCD14DL NRT product page (LANCE MODAPS): https://modaps.modaps.eosdis.nasa.gov/services/about/products/c61-nrt/MCD14DL-NRT.html
- VNP14IMGTDL_NRT product page (LANCE MODAPS): https://modaps.modaps.eosdis.nasa.gov/services/about/products/viirs-land-c2-nrt/vnp14imgtdl_nrt.html
- FIRMS Archive Download: https://firms.modaps.eosdis.nasa.gov/download/
- FIRMS Area API: https://firms.modaps.eosdis.nasa.gov/api/area/
- FIRMS Academy, Data Ingest and Manipulation in Python: https://firms.modaps.eosdis.nasa.gov/content/academy/data_ingest/firms_data_ingest.html
- FIRMS Academy, API usage tutorial: https://firms.modaps.eosdis.nasa.gov/content/academy/data_api/firms_api_use.html
- FIRMS yearly country file index: https://firms.modaps.eosdis.nasa.gov/data/country/yearly_summary_files.txt
- FIRMS country files AttributesReadme.txt: https://firms.modaps.eosdis.nasa.gov/data/country/AttributesReadme.txt
- Example country files (headers inspected): https://firms.modaps.eosdis.nasa.gov/data/country/modis_2025_Kiribati.csv , https://firms.modaps.eosdis.nasa.gov/data/country/viirs-snpp_2025_Palau.csv , https://firms.modaps.eosdis.nasa.gov/data/country/viirs-jpss1_2025_Federated_States_of_Micronesia.csv , https://firms.modaps.eosdis.nasa.gov/data/country/modis_2003_Malta.csv , https://firms.modaps.eosdis.nasa.gov/data/country/modis_2025_Jordan.csv
- MODIS Collection 6 and 6.1 Active Fire Product User's Guide v1.0: https://earthdata.nasa.gov/s3fs-public/2023-09/MODIS_C6_C6.1_Fire_User_Guide_1.0.pdf
- VIIRS Collection 2 375 m Active Fire Product User's Guide v1.2 (June 2025): https://www.earthdata.nasa.gov/s3fs-public/2025-06/VIIRS_C2_AF-375m_User_Guide_1.2.pdf
- Lin, Wolfe, Dellomo, Tan, Zhang, "SNPP and NOAA-20 VIIRS on-orbit geolocation trending and improvements", Proc. SPIE 11501 (2020): https://ntrs.nasa.gov/api/citations/20210026335/downloads/1150112.pdf
- MCST, "(Terra, Aqua) MODIS Geolocation Status", Lin et al., 18 Nov 2019: https://mcst.gsfc.nasa.gov/sites/default/files/meetings_files/06_MODIS_GEO_Lin.pdf
- FIRMS blog, "Transitioning from S-NPP VIIRS & OMPS: What NASA FIRMS users need to know" (27 Oct 2026): https://www.earthdata.nasa.gov/news/blog/transitioning-from-s-npp-viirs-omps-what-nasa-firms-users-need-know
- Earthdata alert, Suomi NPP data announcement: https://www.earthdata.nasa.gov/data/alerts-outages/content/data-alert-history/21880
- GEE community catalog, Archival NRT FIRMS vector data (secondary): https://gee-community-catalog.org/projects/firms_vector/
- apis.io NASA FIRMS Fire Detection schema (secondary): https://apis.io/schemas/nasa-firms/fire-detection/
