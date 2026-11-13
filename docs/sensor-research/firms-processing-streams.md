# FIRMS processing streams, latency, versions and archive coverage

Verified 2026-11-13. NASA FIRMS (Fire Information for Resource Management System) delivers active-fire "hotspot" records from MODIS (Terra, Aqua) and VIIRS (Suomi NPP, NOAA-20, NOAA-21). Terms used below:

- **NRT (near real-time):** data produced globally by NASA LANCE (Land, Atmosphere Near real-time Capability for EOS) from the full downlinked orbit data.
- **RT (real-time) and URT (ultra real-time):** data produced regionally from direct-broadcast ground stations. They are available only for the United States and Canada.
- **SP (standard processing):** science-quality data. In FIRMS these are the monthly fire-location ("ML") files produced by the University of Maryland (UMD) fire team.
- **Collection:** a full reprocessing of an instrument's archive. Within a collection there can be a product "version", such as MCD14ML version 03.

Status tags: [confirmed] means the page was opened and supports the fact. [corrected] means the researcher's value was changed. [unverified] means the fact could not be confirmed on a page.

## Key facts

### Latency tiers (NRT, RT, URT)

| Tier | Latency stated | Source | Status |
|---|---|---|---|
| NRT | "within 3 hours of a satellite observation (on a best-effort basis)" | [FIRMS FAQ](https://www.earthdata.nasa.gov/data/tools/firms/faq) | [confirmed] |
| NRT | "generally within 30 minutes to two hours after satellite observation" (LANCE product pages for MCD14DL, VNP14IMGTDL_NRT and VJ114IMGTDL_NRT) | [MCD14DL page](https://modaps.modaps.eosdis.nasa.gov/services/about/products/c61-nrt/MCD14DL-NRT.html), [VNP14IMGTDL_NRT](https://modaps.modaps.eosdis.nasa.gov/services/about/products/viirs-land-c2-nrt/vnp14imgtdl_nrt.html), [VJ114IMGTDL_NRT](https://modaps.modaps.eosdis.nasa.gov/services/about/products/viirs-land-c2-nrt/vj114imgtdl_nrt.html) | [confirmed] |
| NRT email alerts | "usually sent within 3 hours"; VIIRS alerts "within 4 hours" | [FIRMS FAQ](https://www.earthdata.nasa.gov/data/tools/firms/faq) | [confirmed] |
| RT | "within 30 minutes of overpass" (summary passage); "generally available in FIRMS 20-25 minutes after satellite observation" (Real-Time MODIS section); ground stations process Level 0 to Level 2 in "30-60 minutes"; EOSDIS definition of real-time is "within one hour of the satellite fly-over" | [FIRMS FAQ](https://www.earthdata.nasa.gov/data/tools/firms/faq) | [confirmed]. The FAQ is internally inconsistent; see Conflicts. |
| URT | "within 5 minutes" (summary passage); "within 1-2 minutes of satellite observation" (URT section); "within 1 minute" (ground-station passage); "within minutes" (update text) | [FIRMS FAQ](https://www.earthdata.nasa.gov/data/tools/firms/faq) | [confirmed]. The FAQ is internally inconsistent. |
| URT | "less than 60 seconds of satellite fly over for much of the US and Canada" | [FIRMS API area page](https://firms.modaps.eosdis.nasa.gov/api/area/) | [confirmed] |
| URT | About 25 s for MODIS and about 50 s for VIIRS from observation to detection, for CONUS. The article is dated 20 July 2022 (last updated 9 April 2025) and covers Terra, Aqua, S-NPP and NOAA-20. | [Earthdata article, FIRMS URT](https://www.earthdata.nasa.gov/learn/articles/firms-urt-data) | [confirmed] |

### Where RT and URT exist, and how they are replaced

- URT data come from four direct-readout ground stations: Mayaguez (Puerto Rico), Hampton (Virginia) and Madison (Wisconsin). They cover most of the conterminous United States plus southern Canada and northern Mexico. URT is not produced globally. [FIRMS FAQ](https://www.earthdata.nasa.gov/data/tools/firms/faq) [confirmed]
  - The 2022 article describes direct-broadcast antennas "throughout the continental United States, as well as Puerto Rico and Hawaii", feeding a central point at the University of Wisconsin–Madison. [Earthdata article](https://www.earthdata.nasa.gov/learn/articles/firms-urt-data) [confirmed]
- In the API, the sources MODIS_NRT, VIIRS_SNPP_NRT, VIIRS_NOAA20_NRT and VIIRS_NOAA21_NRT each mix NRT, RT and URT records. LANDSAT_NRT covers the US and Canada only. [FIRMS API area page](https://firms.modaps.eosdis.nasa.gov/api/area/) [confirmed]
- "RT and URT data are removed when corresponding NRT detections are processed or RT/URT is older than 6 hours." [FIRMS API area page](https://firms.modaps.eosdis.nasa.gov/api/area/) [confirmed]
- RT and URT records carry a Version value with the suffix "RT" or "URT"; the FAQ gives the example "2.0" followed by RT or URT. [FIRMS FAQ](https://www.earthdata.nasa.gov/data/tools/firms/faq) [confirmed]

### Version attribute strings

| Sensor | Version string | Meaning | Source | Status |
|---|---|---|---|---|
| MODIS | `6.1URT` | Collection 6.1 ultra real-time | [Attributes page](https://www.earthdata.nasa.gov/data/tools/firms/active-fire-data-attributes-modis-viirs) | [confirmed] |
| MODIS | `6.1RT` | Collection 6.1 real-time | same | [confirmed] |
| MODIS | `6.1NRT` | Collection 6.1 NRT (the page prints "Collection 61") | same | [confirmed] |
| MODIS | `6.1` | Collection 6.1 standard processing (no suffix) | same | [confirmed] |
| VIIRS | `1.0NRT`, `1.0` | Collection 1 NRT and standard. The page lists only these two and no Collection 2 strings. | same; also [VIIRS I-band page](https://earthdata.nasa.gov/data/instruments/viirs/viirs-i-band-375-m-active-fire-data) | [confirmed] (page content). The page appears out of date (see below). |
| VIIRS | `2.0` (+ RT/URT) | Collection 2. The FAQ gives "2.0" as its example Version value. The LANCE NRT pages say Version identifies "VIIRS Collection 1 or VIIRS Collection 2". | [FIRMS FAQ](https://www.earthdata.nasa.gov/data/tools/firms/faq), [VNP14IMGTDL_NRT](https://modaps.modaps.eosdis.nasa.gov/services/about/products/viirs-land-c2-nrt/vnp14imgtdl_nrt.html) | [confirmed] |

### Standard processing (SP): source products, naming and lag

- FIRMS standard data are the UMD monthly fire-location ASCII files: MCD14ML (MODIS Terra and Aqua combined), VNP14IMGML (S-NPP), VJ114IMGML (NOAA-20) and VJ214IMGML (NOAA-21). [FIRMS FAQ](https://www.earthdata.nasa.gov/data/tools/firms/faq) [confirmed]
- The FAQ's product list also spells the VIIRS standard products as "VNP14IMGTML", "VJ114MGTML" and "VJ214IMGTML". These are typos or inconsistencies. The user guide uses VNP14IMGML, VJ114IMGML and VJ214IMGML. [FIRMS FAQ](https://www.earthdata.nasa.gov/data/tools/firms/faq), [VIIRS C2 375 m User Guide v1.2](https://www.earthdata.nasa.gov/s3fs-public/2025-06/VIIRS_C2_AF-375m_User_Guide_1.2.pdf) [confirmed]
- MCD14ML files are "a subset of the standard quality Level 2G raster products available through Earthdata Search". [FIRMS FAQ](https://www.earthdata.nasa.gov/data/tools/firms/faq) [confirmed]
- MCD14ML file naming is `MCD14ML.YYYYMM.CCC.VV.txt`, where CCC is the collection and VV is the product version, "currently 03". The format is a fixed-width ASCII table. Version 2 added one more digit of latitude and longitude precision and a day/night (dn) column. Version 3 has the same format but "significantly improved typing of hot spots". Example file names in the guide: `MCD14ML.201701.006.03.txt.gz`. [MODIS C6/C6.1 Active Fire User's Guide v1.0 (May 2021)](https://www.earthdata.nasa.gov/s3fs-public/2023-09/MODIS_C6_C6.1_Fire_User_Guide_1.0.pdf) [confirmed]
- MCD14ML first appeared in Collection 5. [MODIS User's Guide](https://www.earthdata.nasa.gov/s3fs-public/2023-09/MODIS_C6_C6.1_Fire_User_Guide_1.0.pdf) [confirmed]
- VIIRS ML file naming is `Vxx14IMGML.YYYYMM.CC.VV.csv`, where xx is NP, J1 or J2, CC is the collection ("currently 02") and VV is the version ("currently 03"). The guide's own example file name is `VNP14IMGML.201801.C2.03.csv.gz`, so CC appears as "C2" in practice. Each file is comma-separated and includes a Type field (0 = vegetation fire, 1 = volcano, 2 = other static land source, 3 = offshore/water), a DNFlag field and the solar zenith angle (SZA). [VIIRS C2 User Guide v1.2](https://www.earthdata.nasa.gov/s3fs-public/2025-06/VIIRS_C2_AF-375m_User_Guide_1.2.pdf) [confirmed]
- **Known issue with VIIRS ML Type values:** a bug in the Collection 2 ML production software set the Type field inconsistently in product versions 1 and 2. Static type-2 hotspots were often labelled type 0. The bug was "corrected in May 2025 and all VxxIMGML product files reprocessed to version 3." [VIIRS C2 User Guide v1.2, sec. 6.1](https://www.earthdata.nasa.gov/s3fs-public/2025-06/VIIRS_C2_AF-375m_User_Guide_1.2.pdf) [confirmed; added by verifier]
- The upstream Level 2 swath products behind the ML files are listed below. [VIIRS C2 User Guide](https://www.earthdata.nasa.gov/s3fs-public/2025-06/VIIRS_C2_AF-375m_User_Guide_1.2.pdf), [MODIS User's Guide](https://www.earthdata.nasa.gov/s3fs-public/2023-09/MODIS_C6_C6.1_Fire_User_Guide_1.0.pdf) [confirmed]
  - MODIS: MOD14 (Terra) and MYD14 (Aqua).
  - VIIRS: VNP14IMG (S-NPP), VJ114IMG (NOAA-20) and VJ214IMG (NOAA-21), each generated independently for its sensor at NASA Land SIPS.

**Lag before standard data appear in FIRMS**

| Statement | Source | Status |
|---|---|---|
| ML files "available through FIRMS with a 2-3 month lag" | [FIRMS FAQ](https://www.earthdata.nasa.gov/data/tools/firms/faq) | [confirmed] |
| NRT is "replaced with standard science quality data as they become available (with approximately a 5 month lag)" | [FIRMS Archive Download](https://firms.modaps.eosdis.nasa.gov/download/) (same text on [firms2 mirror](https://firms2.modaps.eosdis.nasa.gov/download/)) | [confirmed] |
| Standard data "usually after 2 months" | [MCD14DL LANCE page](https://modaps.modaps.eosdis.nasa.gov/services/about/products/c61-nrt/MCD14DL-NRT.html), [VNP14IMGTDL_NRT](https://modaps.modaps.eosdis.nasa.gov/services/about/products/viirs-land-c2-nrt/vnp14imgtdl_nrt.html), [VJ114IMGTDL_NRT](https://modaps.modaps.eosdis.nasa.gov/services/about/products/viirs-land-c2-nrt/vj114imgtdl_nrt.html) | [confirmed] |

- The country-summary ZIP files on the FIRMS server were last modified on 10 October 2026 for the 2025 files (MODIS and NOAA-20). This was checked from HTTP headers on 2026-11-13. It is consistent with a refresh months after the year ends, but it does not by itself show when SP replaced NRT. [FIRMS country zips, e.g. modis_2025_all_countries.zip](https://firms.modaps.eosdis.nasa.gov/data/country/zips/modis_2025_all_countries.zip) [confirmed (header only); added by verifier]
- No published monthly release schedule for SP was found. [unverified]

### How NRT differs from SP

The FAQ states that the core Level 2 algorithms are identical in NRT and SP. It lists the following differences. [FIRMS FAQ](https://www.earthdata.nasa.gov/data/tools/firms/faq) [confirmed]

| Aspect | NRT | SP |
|---|---|---|
| Geolocation | Usually < 100 m error. After manoeuvres or severe space weather the error can be several km, typically for < 2 h for Terra MODIS and NOAA-20/21 VIIRS and up to 12 h for Aqua MODIS. | Uses the best available position data. Missing granules are ingested, and data degraded by manoeuvres are removed. |
| Hotspot "type" attribute | Not included | Included in ML files. VIIRS ML files also have Type (see the user guide). |
| Day/night flag | Set from orbit direction (ascending = day, descending = night) | Set from solar zenith angle; > 85° = night |

- The FIRMS attributes page says Type is available "only for MODIS MCD14ML". That is now incomplete, because the VIIRS C2 ML files carry Type. [Attributes page](https://www.earthdata.nasa.gov/data/tools/firms/active-fire-data-attributes-modis-viirs), [VIIRS C2 User Guide](https://www.earthdata.nasa.gov/s3fs-public/2025-06/VIIRS_C2_AF-375m_User_Guide_1.2.pdf) [corrected: the researcher said NRT lacks type and ML has it; the VIIRS ML also has it]
- The VIIRS guide says NRT data "are primarily meant for use in support of fire management applications requiring low-latency data access". It warns of "possible coverage gaps resulting from temporary interruptions in the NRT data processing chain" and says scientific studies "should favor the non-NRT VNP14IMG and VNP14 data stream". (The researcher attributed "primarily meant" to the FAQ; it is in the user guide, not the FAQ.) [VIIRS C2 User Guide sec. 4.3](https://www.earthdata.nasa.gov/s3fs-public/2025-06/VIIRS_C2_AF-375m_User_Guide_1.2.pdf) [corrected: source attribution]
- The FAQ notes that, for science, the Level 2G products retain pixel-level quality information and "account for overlapping satellite orbits to avoid double-counting fire detections". [FIRMS FAQ](https://www.earthdata.nasa.gov/data/tools/firms/faq) [confirmed]
- No source quantifies how much NRT and SP detection counts differ. [unverified]

### Collections served and collection history

**MODIS**

- FIRMS serves MODIS Collection 6.1. The FAQ says it "has been available since April 2021". The archive tool is labelled "MODIS Collection 6.1: 1 November 2000 - present". [FIRMS FAQ](https://www.earthdata.nasa.gov/data/tools/firms/faq), [Archive Download](https://firms.modaps.eosdis.nasa.gov/download/) [confirmed]
- "Collection 61 data replaced Collection 6 (DOI:10.5067/FIRMS/MODIS/MCD14DL.NRT.006) in April 2021." C6.1 had no fire-algorithm changes, only Level 1B calibration changes. [MCD14DL Earthdata page](https://www.earthdata.nasa.gov/learn/find-data/near-real-time/firms/mcd14dl), [MCD14DL LANCE page](https://modaps.modaps.eosdis.nasa.gov/services/about/products/c61-nrt/MCD14DL-NRT.html) [confirmed]
- The user guide quantifies C6 versus C6.1 [MODIS User's Guide sec. 2.1](https://www.earthdata.nasa.gov/s3fs-public/2023-09/MODIS_C6_C6.1_Fire_User_Guide_1.0.pdf) [confirmed; added by verifier]:
  - Only the calibration of bands 1 and 2 changed. The thermal bands and FRP are unchanged.
  - For January 2020, global fire pixels were 404,057 in C6 and 404,052 in C6.1, a difference of 0.001%. 99.64% of granules had no difference.
  - The guide says the two collections "may be freely intermixed".
- Collection history:

| Collection | FIRMS FAQ wording | MODIS User's Guide v1.0 wording | Status |
|---|---|---|---|
| 1 | First products after launch | Same | [confirmed] |
| 3 | First Terra reprocessing, June 2001; first Aqua version | Same | [confirmed] |
| 4 | Began December 2002 for Terra, "somewhat later" for Aqua | Began December 2002, terminated December 2006 | [confirmed] |
| 5 | Began "early 2007"; added FRP | Production "commenced in mid-2006"; MCD14ML new in C5 | [confirmed]; dates differ (see Conflicts) |
| 6 | "began in 2015" | Commenced February 2015, to continue through 31 December 2021 | [confirmed] |
| 6.1 | Available since April 2021 | Mini-reprocessing started in 2018 for atmosphere and expanded to land in late 2020 | [confirmed] |

Sources: [FIRMS FAQ](https://www.earthdata.nasa.gov/data/tools/firms/faq), [MODIS User's Guide sec. 3.1.4](https://www.earthdata.nasa.gov/s3fs-public/2023-09/MODIS_C6_C6.1_Fire_User_Guide_1.0.pdf)

- MOD14 Version 6 was decommissioned at LP DAAC on 31 July 2023, and MOD14 6.1 (DOI 10.5067/MODIS/MOD14.061) is current. This was seen only in a search-result summary of the LP DAAC catalog and was not opened. [Earthdata catalog MOD14 061](https://www.earthdata.nasa.gov/data/catalog/lpcloud-mod14-061-0) [unverified]
- **2026 change upstream:** MODIS Version 7.0 Level 1B calibrated radiance and geolocation products (MOD02/MYD02, MOD03/MYD03) were released in March 2026 (notice issued 27 March 2026). The Version 6.1 Level 1 collection was to be "decommissioned on September 30, 2026". The notice does not say whether or when MOD14/MYD14 or MCD14ML will be produced as Collection 7. [Earthdata notice](https://www.earthdata.nasa.gov/data/alerts-outages/version-7.0-modis-calibrated-radiances-geolocation-data-products-now-available) [confirmed; added by verifier]
- NASA plans a final MODIS v8.0 calibration for the last reprocessing after operations end. [LAADS MODIS-to-VIIRS transition](https://ladsweb.modaps.eosdis.nasa.gov/learn/modis-to-viirs-transition/) [confirmed; added by verifier]

**VIIRS 375 m**

- The current product is Collection 2. The user guide v1.2 (June 2025) calls C2 "the second major release" of VNP14IMG. C2 uses NASA Collection 2 Level 1B radiances and geolocation instead of the SDR inputs used in C1, which had spuriously calibrated "bad scans". It also uses new Level 1B quality flags that "virtually eliminate the spurious detections that were common for Collection 1". [VIIRS C2 User Guide](https://www.earthdata.nasa.gov/s3fs-public/2025-06/VIIRS_C2_AF-375m_User_Guide_1.2.pdf) [confirmed]
- The NRT DOIs carry the suffix .002 (Collection 2). [VNP14IMGTDL_NRT](https://modaps.modaps.eosdis.nasa.gov/services/about/products/viirs-land-c2-nrt/vnp14imgtdl_nrt.html) [confirmed]
- No dated FIRMS switch from VIIRS C1 to C2 (in NRT or archive) was found. [unverified]
- The VIIRS user guide history is v1.0 (May 2024), v1.1 (November 2024) and v1.2 (June 2025, updated for ML v3). [VIIRS C2 User Guide](https://www.earthdata.nasa.gov/s3fs-public/2025-06/VIIRS_C2_AF-375m_User_Guide_1.2.pdf) [confirmed]

### Archive start and end dates per sensor

| Sensor | FIRMS FAQ | FIRMS Archive Download | Other primary sources | Status |
|---|---|---|---|---|
| Terra MODIS | 1 Nov 2000 – present | MODIS C6.1: 1 Nov 2000 – present (Terra and Aqua combined) | ARSET Q&A Jan 2025: Terra from Nov 2000 | [confirmed] |
| Aqua MODIS | July 2002 – present; "high quality" from 4 July 2002 | (combined above) | ARSET Q&A: July 2002 | [confirmed] |
| S-NPP VIIRS | 20 Jan 2012 – 2 Nov 2026 | 20 Jan 2012 – 2 Nov 2026 | User guide: first detections 19 Jan 2012, effective start 20 Jan 2012. LP DAAC VNP14IMG.002 temporal extent: 2012-01-17. LP DAAC: delivery "ceased on November 2, 2026 (2026/306)". | [confirmed] |
| NOAA-20 VIIRS | 1 Apr 2018 – present | 1 Apr 2018 – present | LP DAAC VJ114IMG.002: 2018-01-01 to present. ARSET Q&A Jan 2025 gives both "01 April 2018" and "January 2020". LANCE VJ114IMGTDL_NRT page says "20 January 2012", an apparent copy error. | [confirmed]; see Conflicts |
| NOAA-21 VIIRS | 17 Jan 2024 – present | **1 March 2023 – present** | LP DAAC VJ214IMG.002: 2023-02-10. Earthdata VJ214IMG_NRT: 2024-01-10. ARSET Q&A: 17 Jan 2024 and "January 2024". FIRMS blog 8 Feb 2024: NOAA-21 "recently introduced". | [confirmed]; sources disagree |

Sources: [FIRMS FAQ](https://www.earthdata.nasa.gov/data/tools/firms/faq), [Archive Download](https://firms.modaps.eosdis.nasa.gov/download/), [VIIRS C2 User Guide](https://www.earthdata.nasa.gov/s3fs-public/2025-06/VIIRS_C2_AF-375m_User_Guide_1.2.pdf), [LP DAAC VNP14IMG.002](https://www.earthdata.nasa.gov/data/catalog/lpcloud-vnp14img-002), [LP DAAC VJ114IMG.002](https://www.earthdata.nasa.gov/data/catalog/lpcloud-vj114img-002), [LP DAAC VJ214IMG.002](https://www.earthdata.nasa.gov/data/catalog/lpcloud-vj214img-002), [VJ214IMG_NRT](https://www.earthdata.nasa.gov/learn/find-data/near-real-time/firms/vj214imgtdlnrt), [ARSET 2025 Q&A](https://www.earthdata.nasa.gov/s3fs-public/2026-01/arset-2026-advfirms-part1-qa.pdf), [FIRMS blog, NOAA-21 now available](https://wiki.earthdata.nasa.gov/spaces/FIRMS/blog/2024/02/08/343475617/NOAA-21+VIIRS+Active+Fire+Detection+Data+Now+Available)

- Known early MODIS gaps or low-count periods: 15 April 2001; 15 June – 3 July 2001; 19–28 March 2002. [FIRMS FAQ](https://www.earthdata.nasa.gov/data/tools/firms/faq) [confirmed]
- The FIRMS API offers standard-processing sources for all four records: MODIS_SP, VIIRS_SNPP_SP, VIIRS_NOAA20_SP and VIIRS_NOAA21_SP. [FIRMS API area page](https://firms.modaps.eosdis.nasa.gov/api/area/) [confirmed]
- The start date of SP data within each of those sources is not published on any open page. The `/api/data_availability` endpoint needs a MAP_KEY and was not queried. [unverified]

### Suomi NPP end in FIRMS (2026)

- The Earthdata blog was posted 27 October 2026 and last updated 3 November 2026. It says FIRMS production and delivery of S-NPP data "will cease at 13:00 Universal Time (UTC) on November 2, 2026". It says "Historical data will continue to be available" and tells API users to change VIIRS_SNPP_NRT or VIIRS_SNPP_SP to VIIRS_NOAA20_NRT or VIIRS_NOAA21_NRT. [Earthdata blog](https://www.earthdata.nasa.gov/news/blog/transitioning-from-suomi-npp-viirs-omps-what-firms-users-need-know) (same text at the [alternate URL](https://www.earthdata.nasa.gov/news/blog/transitioning-from-s-npp-viirs-omps-what-nasa-firms-users-need-know)) [confirmed]
- The FIRMS FAQ (fetched 2026-11-13) says production "ceased at 15:40 Universal Time (UTC) on November 2, 2026". [FIRMS FAQ](https://www.earthdata.nasa.gov/data/tools/firms/faq) [confirmed: present in page text. This was the researcher's unverified variant; it is now verified as being on the page.]
- LP DAAC says delivery of all S-NPP VIIRS products "ceased on November 2, 2026 (2026/306)". [LP DAAC VNP14IMG.002](https://www.earthdata.nasa.gov/data/catalog/lpcloud-vnp14img-002) [confirmed]
- An older Earthdata VIIRS I-band page says S-NPP "end-of-life is anticipated to occur on or before October 2026". [VIIRS I-band page](https://earthdata.nasa.gov/data/instruments/viirs/viirs-i-band-375-m-active-fire-data) [confirmed]

### MODIS (Terra, Aqua) status in 2026

- Earthdata notice of 2 May 2025: "In late 2026/early 2027, the Terra and Aqua platforms ... will begin shutting down operations". It also says "Both platforms are currently drifting out of their designed orbits, impacting crossing times". [Earthdata notice](https://www.earthdata.nasa.gov/data/alerts-outages/transition-from-modis-viirs) [confirmed]
- The researcher said this notice contains the morning-overpass statement. It does not; the statement is in the 27 October 2026 FIRMS blog. The blog says "Currently MODIS Terra provides the only morning overpass (approximately 3 hours before Aqua)" and "NASA is investigating alternatives". After Aqua ends, NOAA-20 and NOAA-21 VIIRS cover the afternoon orbit. [Earthdata blog](https://www.earthdata.nasa.gov/news/blog/transitioning-from-suomi-npp-viirs-omps-what-firms-users-need-know) [corrected: source]
- NASA Science, "Terra: the end of an era" (29 December 2025, editor's note updated 20 March 2026), projects end-of-science activities for Terra in February 2027 and Aqua in September 2027. The missions keep operating after those dates. Terra stopped inclination adjustments in 2020; its equator crossing time moved from 10:30 to 10:15 mean local time by fall 2022. [NASA Science](https://science.nasa.gov/science-research/earth-science/terra-the-end-of-an-era) [confirmed; added by verifier]
- CAMS (25 February 2026, secondary source) gives Terra MODIS data collection ending January 2027 and Aqua around September 2027. [CAMS](https://atmosphere.copernicus.eu/drifting-away-modis-cams-global-fire-assimilation-system) [confirmed (secondary)]
- NASA Science, 12 February 2026: Terra MODIS is still collecting science data. ASTER TIR was shut off on 16 January 2026 because of power limits. [NASA Science blog](https://science.nasa.gov/blogs/science-news/2026/02/12/terra-adjusts-instrument-operations-to-extend-mission-life) [confirmed; added by verifier]
- LAADS: "No follow-on MODIS-like instrument with an orbit at the Terra morning equatorial-crossing MLT exists" in current or planned NASA missions. [LAADS](https://ladsweb.modaps.eosdis.nasa.gov/learn/modis-to-viirs-transition/) [confirmed]
- No FIRMS-specific end-of-service date for MODIS was found. [unverified]

### Yearly per-country summary files

- The Archive Download page links "Download yearly summary by country [.csv]" to https://firms.modaps.eosdis.nasa.gov/country/. That page is rendered by JavaScript and its listing could not be read. [Archive Download](https://firms.modaps.eosdis.nasa.gov/download/) [confirmed (link only)]
- The underlying yearly ZIP files follow the pattern `https://firms.modaps.eosdis.nasa.gov/data/country/zips/{sensor}_{YYYY}_all_countries.zip`. Each contains per-country CSVs such as `viirs-snpp_2019_Afghanistan.csv`. This pattern comes from a third-party issue dated 13 May 2024 ([GitHub issue](https://www.github.com/mapme-initiative/mapme.biodiversity/issues/264)). The verifier checked it on 2026-11-13 with HTTP HEAD requests only (no download). The results [confirmed by HEAD; added by verifier]:

| Sensor prefix | Years that returned HTTP 200 (sampled) | Years that returned 404 (sampled) |
|---|---|---|
| `modis` | 2000, 2001, 2012, 2018, 2023, 2024, 2025 | 2026 |
| `viirs-snpp` | 2012, 2018, 2023, 2024, 2025 | 2000, 2001, 2026 |
| `viirs-jpss1` (NOAA-20) | 2018, 2023, 2024, 2025 | 2000, 2001, 2012, 2026 |
| `viirs-jpss2`, `viirs-noaa20`, `viirs-noaa21` | none | all sampled years |

- So yearly country summaries exist for MODIS, S-NPP and NOAA-20 and were not found for NOAA-21 under the guessed names. The current year (2026) is not yet available. Whether these files contain SP data, NRT data or a mix was not established. [unverified]

### API rate limits and day ranges

- "MAP_KEY limit is 5000 transactions / 10-minute interval." Larger requests, for example 7 days, may count as several transactions. [FIRMS API area page](https://firms.modaps.eosdis.nasa.gov/api/area/) [confirmed]
- DAY_RANGE is "1 .. 5". With a DATE the call returns DATE to DATE + DAY_RANGE − 1. Without a DATE it returns the most recent data. [FIRMS API area page](https://firms.modaps.eosdis.nasa.gov/api/area/) [confirmed]
- Archive Download provides data older than the last 7 days as SHP, CSV or JSON. [Archive Download](https://firms.modaps.eosdis.nasa.gov/download/) [confirmed]
- Web files for the last 24 h, 48 h and 7 days are updated every 60 minutes, and the map every 5 minutes. The last 2 months are downloadable as TXT. [FIRMS FAQ](https://www.earthdata.nasa.gov/data/tools/firms/faq) [confirmed]

### Citation and DOIs

| Item | Value | Source | Status |
|---|---|---|---|
| Image credit | "NASA FIRMS" | [FIRMS FAQ](https://www.earthdata.nasa.gov/data/tools/firms/faq) | [confirmed] |
| Acknowledgement | "We acknowledge the use of imagery from the NASA LANCE FIRMS" (FAQ). Product pages: "This dataset was provided by LANCE FIRMS operated by NASA ESDIS with funding provided by NASA Headquarters". | [FAQ](https://www.earthdata.nasa.gov/data/tools/firms/faq), [MCD14DL LANCE](https://modaps.modaps.eosdis.nasa.gov/services/about/products/c61-nrt/MCD14DL-NRT.html) | [confirmed] |
| MODIS algorithm paper | Giglio et al. 2003, doi:10.1016/S0034-4257(03)00184-6 | FAQ | [confirmed] |
| VIIRS 375 m algorithm paper | Schroeder et al. 2014, doi:10.1016/j.rse.2013.12.008 | FAQ | [confirmed] |
| Newer reference listed in FAQ | Xu et al. 2026, doi:10.1016/j.srs.2026.100366 ("Major improvements in spaceborne early fire detection and small-fire FRP retrieval...") | FAQ | [confirmed; added by verifier] |
| MODIS C6.1 NRT | 10.5067/FIRMS/MODIS/MCD14DL.NRT.0061 (replaced C6 10.5067/FIRMS/MODIS/MCD14DL.NRT.006) | [MCD14DL Earthdata](https://www.earthdata.nasa.gov/learn/find-data/near-real-time/firms/mcd14dl) | [confirmed] |
| S-NPP VIIRS NRT | 10.5067/FIRMS/VIIRS/VNP14IMGT_NRT.002 | [VNP14IMGTDL_NRT](https://modaps.modaps.eosdis.nasa.gov/services/about/products/viirs-land-c2-nrt/vnp14imgtdl_nrt.html) | [confirmed] |
| NOAA-20 VIIRS NRT | 10.5067/FIRMS/VIIRS/VJ114IMGT_NRT.002 | [VJ114IMGTDL_NRT](https://modaps.modaps.eosdis.nasa.gov/services/about/products/viirs-land-c2-nrt/vj114imgtdl_nrt.html) | [confirmed] |
| NOAA-21 VIIRS NRT (swath) | 10.5067/VIIRS/VJ214IMG_NRT.002. APA: "NASA VIIRS Land Science Team. (2024). VIIRS/JPSS2 Active Fires 6-Min L2 Swath 375m NRT" | [VJ214IMG_NRT](https://www.earthdata.nasa.gov/learn/find-data/near-real-time/firms/vj214imgtdlnrt) | [confirmed] |
| S-NPP standard L2 | 10.5067/VIIRS/VNP14IMG.002 | [LP DAAC](https://www.earthdata.nasa.gov/data/catalog/lpcloud-vnp14img-002) | [confirmed; added] |
| NOAA-20 standard L2 | 10.5067/VIIRS/VJ114IMG.002. "Giglio, Louis. (2024). VIIRS/JPSS1 Active Fires 6-Min L2 Swath 375m V002" | [LP DAAC](https://www.earthdata.nasa.gov/data/catalog/lpcloud-vj114img-002) | [confirmed; added] |
| NOAA-21 standard L2 | 10.5067/VIIRS/VJ214IMG.002 | [LP DAAC](https://www.earthdata.nasa.gov/data/catalog/lpcloud-vj214img-002) | [confirmed; added] |
| MODIS Terra L2 C6.1 | 10.5067/MODIS/MOD14.061 | search summary only | [unverified] |

- The MCD14DL Earthdata page's APA citation names a VIIRS NOAA-21 product, which looks like a page error. [MCD14DL Earthdata](https://www.earthdata.nasa.gov/learn/find-data/near-real-time/firms/mcd14dl) [confirmed]
- No DOIs were found for the ML monthly files themselves. [unverified]

### Observation geometry as stated by FIRMS and the guides

- MODIS swath is 2,330 km. Terra crosses the equator at about 10:30 a.m./p.m. and Aqua at about 1:30 p.m./a.m. mean local time. There are at least four MODIS observations a day at the equator, with more toward the poles. [FIRMS FAQ](https://www.earthdata.nasa.gov/data/tools/firms/faq) [confirmed]
- The VIIRS swath is about 3,060 km, with about 15% overlap between consecutive orbits at the equator and full global coverage every 12 h. S-NPP crosses at 1:30 pm and 1:30 am. Mid-latitudes get 3–4 looks a day. [VIIRS C2 User Guide sec. 7](https://www.earthdata.nasa.gov/s3fs-public/2025-06/VIIRS_C2_AF-375m_User_Guide_1.2.pdf) [confirmed; added]
- ARSET (January 2025): the five sensors together give 8–10 daily observations at equatorial to mid-latitudes and 15–20 at polar latitudes. [ARSET Q&A](https://www.earthdata.nasa.gov/s3fs-public/2026-01/arset-2026-advfirms-part1-qa.pdf) [confirmed; added]
- Confidence fields differ by sensor. MODIS gives 0–100%; VIIRS gives low, nominal or high only. [FIRMS FAQ](https://www.earthdata.nasa.gov/data/tools/firms/faq) [confirmed]

## Why these matter for combining the records

- Any monthly series built from FIRMS downloads will contain standard records for older months and NRT records for roughly the last 2–5 months. The version column (for example `6.1` versus `6.1NRT`) is the only per-row marker of which is which.
- NRT and standard rows differ in how the day/night flag is assigned and in whether a hotspot type is present. NRT can also have gaps and geolocation errors that standard processing fixes. A month's counts and its day/night split can therefore change when NRT is replaced.
- The VIIRS Type field was wrong in ML versions 1 and 2 until the May 2025 reprocessing. Files obtained before mid-2025 may filter static sources differently from current files.
- Each satellite has a different start and end. The NOAA-21 start date also depends on which source is used.
- Several records end in 2026–2027: S-NPP on 2 November 2026, and Terra and Aqua science data are projected to end around February and September 2027. The Terra and Aqua orbits are drifting, so overpass times are no longer the nominal ones.
- The upstream MODIS Level 1B moved to Version 7.0 in 2026, but FIRMS still labels MODIS as C6.1. A future change of collection label within the series is possible.

## Conflicts and unverified items

1. **URT latency.** The FAQ gives several figures: "within 5 minutes", "within 1-2 minutes", "within 1 minute" and "within minutes". The [API page](https://firms.modaps.eosdis.nasa.gov/api/area/) gives "less than 60 seconds". The [2022 article](https://www.earthdata.nasa.gov/learn/articles/firms-urt-data) gives about 25 s (MODIS) and about 50 s (VIIRS). The API page and article are more specific; the "5 minutes" figure reads as a conservative summary.
2. **RT latency.** The FAQ says "within 30 minutes" in its summary and "20-25 minutes" in its MODIS RT section. Ground-station processing is described as "30-60 minutes", and the EOSDIS definition is "within one hour". All are from the [FAQ](https://www.earthdata.nasa.gov/data/tools/firms/faq).
3. **NRT latency.** The FAQ says within 3 hours (best effort). The LANCE product pages say 30 minutes to 2 hours (typical). These are compatible: one is an upper bound, the other a typical range.
4. **SP lag.** The FAQ says 2–3 months. The LANCE pages say "usually after 2 months". The Archive Download page says "approximately a 5 month lag". The Archive Download page is the page where replacement actually happens, so 5 months is the safer planning value. All three pages were current on 2026-11-13.
5. **NOAA-21 start.** The FAQ and ARSET (January 2025) say 17 January 2024. The Archive Download page says 1 March 2023. The LP DAAC standard L2 product starts 2023-02-10, and the Earthdata NRT page says 2024-01-10. A plausible but unconfirmed explanation is that standard (SP) data reach back to 2023 while NRT starts in January 2024. The Archive Download page is the operational source for what can actually be downloaded.
6. **NOAA-20 start.** The FAQ, Archive Download and ARSET say 1 April 2018. ARSET elsewhere in the same document says "January 2020". LP DAAC L2 starts 2018-01-01. The LANCE VJ114IMGTDL_NRT page says 20 January 2012, which is impossible because NOAA-20 launched in 2017. 1 April 2018 is the FIRMS value.
7. **S-NPP end time on 2 November 2026.** The FAQ says 15:40 UTC; the [blog of 27 October 2026](https://www.earthdata.nasa.gov/news/blog/transitioning-from-suomi-npp-viirs-omps-what-firms-users-need-know) says 13:00 UTC. The FAQ (past tense, "ceased") was likely updated after the event and may be the more accurate figure. The researcher's "1 November 2026" variant was not found and remains unverified.
8. **S-NPP start.** The user guide gives first detections on 19 January 2012 and an effective start of 20 January 2012. LP DAAC's L2 extent starts 2012-01-17. The FIRMS FAQ also mentions 19 January 2012 as the start of routine production. FIRMS uses 20 January 2012.
9. **MODIS Collection 5 start.** The FAQ says "early 2007"; the user guide says production "commenced in mid-2006".
10. **Terra and Aqua end dates.** Earthdata (May 2025): shutdown begins "late 2026/early 2027". NASA Science (updated 20 March 2026): end of science in February 2027 (Terra) and September 2027 (Aqua). CAMS (February 2026, secondary): January 2027 (Terra) and around September 2027 (Aqua). NASA Science is the most recent primary source.
11. **VIIRS version strings.** The [attributes page](https://www.earthdata.nasa.gov/data/tools/firms/active-fire-data-attributes-modis-viirs) lists only C1 strings (1.0, 1.0NRT). The FAQ example uses 2.0, and all DOIs and guides are C2. The attributes page appears stale.
12. **Type attribute scope.** The attributes page says Type is MODIS-only, but the VIIRS C2 ML format includes Type.
13. **VIIRS ML collection token.** The guide's naming rule says CC = "02", but its example files use "C2".
14. **Unverified:**
    - the SP start date per API source;
    - the date FIRMS switched VIIRS from C1 to C2;
    - a quantified difference between NRT and SP counts;
    - DOIs for the ML files;
    - the MOD14 6.1 DOI and the 31 July 2023 decommissioning of V6 (search summary only);
    - the contents (SP or NRT) of the country ZIPs;
    - the NOAA-21 country-ZIP naming.

## Open questions

- When did standard-processing (_SP) data for NOAA-20 and NOAA-21 first become available in FIRMS, and how far back does each go? Does the 1 March 2023 NOAA-21 archive start reflect SP data? `/api/data_availability` (MAP_KEY required) would answer the first part.
- On what date did FIRMS move VIIRS 375 m NRT and archive from Collection 1 to Collection 2? Was any C1 data left in the archive?
- Will the MODIS fire products (MOD14/MYD14, MCD14ML) move to Collection 7 now that the Version 7.0 Level 1B products exist and the 6.1 Level 1 collection was due for decommissioning on 30 September 2026? Would FIRMS relabel its MODIS archive?
- How large are the differences in monthly NRT versus SP detection counts per sensor?
- Is there a NOAA-21 yearly country summary, and under what file name? Do the country files contain SP or NRT data for recent years?
- When will FIRMS stop MODIS NRT for Terra and Aqua, and will it publish a cutover time as it did for S-NPP?
- Are there citable DOIs for the ML monthly products (MCD14ML, Vxx14IMGML)?

## Sources

- FIRMS FAQ — https://www.earthdata.nasa.gov/data/tools/firms/faq
- FIRMS Archive Download — https://firms.modaps.eosdis.nasa.gov/download/ (mirror https://firms2.modaps.eosdis.nasa.gov/download/)
- FIRMS API, area endpoint — https://firms.modaps.eosdis.nasa.gov/api/area/
- FIRMS active fire data attributes (MODIS, VIIRS) — https://www.earthdata.nasa.gov/data/tools/firms/active-fire-data-attributes-modis-viirs
- LANCE MCD14DL C6.1 NRT product page — https://modaps.modaps.eosdis.nasa.gov/services/about/products/c61-nrt/MCD14DL-NRT.html
- Earthdata MCD14DL page — https://www.earthdata.nasa.gov/learn/find-data/near-real-time/firms/mcd14dl
- LANCE VNP14IMGTDL_NRT — https://modaps.modaps.eosdis.nasa.gov/services/about/products/viirs-land-c2-nrt/vnp14imgtdl_nrt.html
- LANCE VJ114IMGTDL_NRT — https://modaps.modaps.eosdis.nasa.gov/services/about/products/viirs-land-c2-nrt/vj114imgtdl_nrt.html
- LANCE VIIRS C2 NRT product index — https://modaps.modaps.eosdis.nasa.gov/services/about/products/viirs-c2-nrt/index.html
- Earthdata VJ214IMGTDL_NRT / VJ214IMG_NRT — https://www.earthdata.nasa.gov/learn/find-data/near-real-time/firms/vj214imgtdlnrt
- VIIRS Collection 2 375 m Active Fire Product User Guide v1.2 (June 2025) — https://www.earthdata.nasa.gov/s3fs-public/2025-06/VIIRS_C2_AF-375m_User_Guide_1.2.pdf
- MODIS Collection 6 and 6.1 Active Fire Product User's Guide v1.0 (May 2021) — https://www.earthdata.nasa.gov/s3fs-public/2023-09/MODIS_C6_C6.1_Fire_User_Guide_1.0.pdf
- LP DAAC / Earthdata catalog VNP14IMG.002 — https://www.earthdata.nasa.gov/data/catalog/lpcloud-vnp14img-002
- LP DAAC / Earthdata catalog VJ114IMG.002 — https://www.earthdata.nasa.gov/data/catalog/lpcloud-vj114img-002
- LP DAAC / Earthdata catalog VJ214IMG.002 — https://www.earthdata.nasa.gov/data/catalog/lpcloud-vj214img-002
- Earthdata blog, Transitioning from Suomi NPP VIIRS/OMPS (27 October 2026) — https://www.earthdata.nasa.gov/news/blog/transitioning-from-suomi-npp-viirs-omps-what-firms-users-need-know
- Earthdata notice, Transition from MODIS to VIIRS (2 May 2025) — https://www.earthdata.nasa.gov/data/alerts-outages/transition-from-modis-viirs
- Earthdata notice, Version 7.0 MODIS calibrated radiances and geolocation (March 2026) — https://www.earthdata.nasa.gov/data/alerts-outages/version-7.0-modis-calibrated-radiances-geolocation-data-products-now-available
- LAADS, MODIS to VIIRS Transition — https://ladsweb.modaps.eosdis.nasa.gov/learn/modis-to-viirs-transition/
- NASA Science, Terra: the end of an era — https://science.nasa.gov/science-research/earth-science/terra-the-end-of-an-era
- NASA Science blog, Terra adjusts instrument operations (12 February 2026) — https://science.nasa.gov/blogs/science-news/2026/02/12/terra-adjusts-instrument-operations-to-extend-mission-life
- Earthdata article, FIRMS URT data (2022) — https://www.earthdata.nasa.gov/learn/articles/firms-urt-data
- Earthdata VIIRS I-band 375 m active fire data page — https://earthdata.nasa.gov/data/instruments/viirs/viirs-i-band-375-m-active-fire-data
- FIRMS blog, NOAA-21 VIIRS Active Fire Detection Data Now Available (8 February 2024) — https://wiki.earthdata.nasa.gov/spaces/FIRMS/blog/2024/02/08/343475617/NOAA-21+VIIRS+Active+Fire+Detection+Data+Now+Available
- ARSET 2025 Advanced FIRMS training, Part 1 Q&A — https://www.earthdata.nasa.gov/s3fs-public/2026-01/arset-2026-advfirms-part1-qa.pdf
- CAMS, Drifting away from MODIS (25 February 2026; secondary) — https://atmosphere.copernicus.eu/drifting-away-modis-cams-global-fire-assimilation-system
- GitHub issue documenting the FIRMS country ZIP pattern (third party, 13 May 2024) — https://www.github.com/mapme-initiative/mapme.biodiversity/issues/264
- FIRMS country ZIP files (checked by HTTP HEAD only) — https://firms.modaps.eosdis.nasa.gov/data/country/zips/
