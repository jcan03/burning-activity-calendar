# Sensor reference: MODIS and VIIRS facts for hotspot harmonization

Team reference for City of Kamloops & Co. It collects the sensor, satellite, orbit, product and FIRMS facts the team needs before choosing how to combine MODIS and VIIRS hotspots into one record. It states facts only and does not recommend a method.

Compiled 2026-11-13 from web research. Fourteen topics were researched, each was re-checked against primary sources by a second agent, and a final pass reconciled the places where topics disagreed. The fifteen working files are in [sensor-research/](sensor-research/), each with its full source list and a status tag on every fact. Each section below links to its file.

How to read the values:

- A linked source means the page was opened on 2026-11-13 and supports the value.
- **Computed** means the value was derived during this research (for example from published orbital elements) and is not printed by any source.
- **Unconfirmed** means no primary page could be found for it.
- Where sources disagree, the value to use is given here and the disagreement is listed in [Disagreements between sources](#disagreements-between-sources).

## At a glance

The facts that bear most on combining the records. Each is expanded and sourced in the sections below.

1. **The sensor mix changes five times.** One sensor from November 2000, two from July 2002, three from January 2012, four from April 2018, five from March 2023, and four again since 2 November 2026.
2. **Suomi NPP has ended.** Its data stopped permanently at 15:40 UTC on 2 November 2026, after five multi-day gaps earlier in 2026.
3. **The MODIS orbits are no longer the documented ones.** Terra's daytime crossing has moved from 10:30 to about 08:33 and Aqua's from 13:30 to about 15:49. The drift began in 2020–2021. Both instruments are still operating, with end of science projected for February and September 2027.
4. **Terra is the only morning observer.** All three VIIRS satellites observe at about 13:30, close to Aqua's original time. Nothing replaces Terra's morning pass.
5. **A hotspot is a flagged pixel, and the pixels differ in size.** A MODIS pixel covers about 7 times the area of a VIIRS 375 m pixel at nadir and about 15 times at the swath edge. MODIS pixels grow about 9.7 times across the swath and VIIRS pixels about 4.5 times.
6. **Each sensor over-counts differently.** MODIS re-observes the same ground in overlapping scans off nadir, and FIRMS files keep those duplicates. VIIRS deletes most of its overlap on board.
7. **Looks per day depend on latitude and on the number of satellites.** One MODIS has daily gaps between 30°S and 30°N. One sensor sees mid-latitudes three to four times a day and high latitudes six to eight times.
8. **The two FIRMS products use different algorithms.** The confidence columns are on different scales with different meanings, and VIIRS "high" means a saturated pixel.
9. **Fire radiative power is measured differently.** MODIS uses its own 4 µm band at 1 km. The VIIRS 375 m product borrows the 750 m M13 band and splits the value among pixels.
10. **A MODIS-like VIIRS product exists outside FIRMS.** The VIIRS 750 m product runs a port of the MODIS algorithm on every VIIRS satellite, and NASA describes its performance as comparable to Aqua MODIS.
11. **The newest months of any download are near-real-time rows.** They lack the `type` column, assign `daynight` by a different rule, and are replaced by standard data after two to five months. The `version` column tells them apart.
12. **Open yearly Canada files exist for three of the four records.** MODIS 2000–2025, Suomi NPP 2012–2025 and NOAA-20 2018–2025 need no key. NOAA-21 has no country files.
13. **The versions in the archive are consistent.** MODIS is Collection 6 or 6.1 throughout, which differ by 0.001% in counts. VIIRS is Collection 2 throughout.
14. **There are multi-week gaps.** Terra in June 2001, March 2002 and October 2022; Aqua in August 2020 and April 2022; Suomi NPP in July and August 2022.
15. **NASA publishes no method for combining the sensors.** Its guides advise against time steps shorter than about eight days for MODIS and against near-real-time data for time series.

## Which sensors were flying when

Five sensors feed the FIRMS hotspot record. Each row is a period bounded by a satellite joining or leaving. Dates are those of the FIRMS archive. Detail: [sensor-research/_cross-check.md](sensor-research/_cross-check.md).

| Period (UTC) | Sensors with hotspots in FIRMS | Number | Notes |
|---|---|---|---|
| 1 Nov 2000 – 3 Jul 2002 | Terra MODIS | 1 | Morning and late-evening passes only. Terra MODIS observed from 24 Feb 2000, but the fire location product is not distributed before November 2000. |
| 4 Jul 2002 – 19 Jan 2012 | Terra MODIS, Aqua MODIS | 2 | Both orbits held at 10:30 and 13:30 to within a few minutes. |
| 20 Jan 2012 – 31 Mar 2018 | Terra, Aqua, Suomi NPP VIIRS | 3 | First 375 m data. |
| 1 Apr 2018 – 28 Feb 2023 | Terra, Aqua, Suomi NPP, NOAA-20 VIIRS | 4 | The Terra and Aqua orbits begin to drift inside this period (2020–2022). |
| 1 Mar 2023 – 2 Nov 2026 15:40 | Terra, Aqua, Suomi NPP, NOAA-20, NOAA-21 VIIRS | 5 | The NOAA-21 start is 1 Mar 2023 on the FIRMS archive download page and 17 Jan 2024 in the FIRMS FAQ. See [Disagreements between sources](#disagreements-between-sources). |
| 2 Nov 2026 15:40 – present | Terra, Aqua, NOAA-20, NOAA-21 | 4 | Suomi NPP data ended permanently. November 2026 is split by this change. |

Projected next changes: Terra end of science about February 2027, Aqua about September 2027, and the launch of JPSS-4 (a fourth VIIRS) planned for 1 September 2027.

## Satellites and orbits

Detail: [terra-aqua-platforms.md](sensor-research/terra-aqua-platforms.md), [jpss-platforms.md](sensor-research/jpss-platforms.md).

All five satellites fly sun-synchronous, near-polar orbits, so each crosses the equator at a fixed local solar time. The crossing time is given for the daytime pass. The night pass crosses twelve hours later.

| | Terra | Aqua | Suomi NPP | NOAA-20 | NOAA-21 |
|---|---|---|---|---|---|
| Instrument | MODIS | MODIS | VIIRS | VIIRS | VIIRS |
| Launch | 18 Dec 1999 | 4 May 2002 | 28 Oct 2011 | 18 Nov 2017 | 10 Nov 2022 |
| Instrument first light | 24 Feb 2000 | 24 Jun 2002 | | | |
| FIRMS record starts | 1 Nov 2000 | 4 Jul 2002 | 20 Jan 2012 | 1 Apr 2018 | 1 Mar 2023 (archive page) |
| FIRMS record ends | running | running | 2 Nov 2026, 15:40 UTC | running | running |
| Design life | 6 years | 6 years | 5 years (secondary sources) | 7 years | 7 years |
| Maintained altitude | 705 km | 705 km | 833 km (824 km design) | 833 km | 833 km |
| Inclination | 98.2° | 98.2° | 98.79° | 98.79° | 98.72° (computed) |
| Period | 98.9 min | 98.9 min | 101.44 min | 101.44 min | 101.44 min (computed) |
| Repeat cycle | 16 days, 233 orbits | 16 days, 233 orbits | 16 days | 16 days | 16 days |
| Maintained daytime crossing | 10:30, southbound | 13:30, northbound | 13:25–13:30, northbound | same | same |
| Crossing on 13 Nov 2026 (computed) | about 08:33 | about 15:49 | not applicable | about 13:32 | about 13:24 |
| Altitude on 13 Nov 2026 (computed) | about 689 km | about 686 km | about 827 km | about 827 km | about 827 km |
| Status on 13 Nov 2026 | science mode | science mode | data ended | operating (NOAA secondary) | operating (NOAA primary) |

Sources: [MCST](https://mcst.gsfc.nasa.gov/index.php/some-information-about-modis), [LAADS MODIS](https://ladsweb.modaps.eosdis.nasa.gov/missions-and-measurements/modis/), [OSPO JPSS status](https://www.ospo.noaa.gov/operations/jpss/status.html) (updated 5 Nov 2026), [FIRMS archive download](https://firms.modaps.eosdis.nasa.gov/download/), [FIRMS FAQ](https://www.earthdata.nasa.gov/data/tools/firms/faq). The 13 November 2026 values were computed from [CelesTrak](https://celestrak.org/NORAD/elements/gp.php?CATNR=25994&FORMAT=TLE) orbital elements and are good to a few minutes.

### Terra and Aqua orbit drift

Both satellites held their crossing times for about two decades and then stopped the maneuvers that hold them. This is the largest change inside the MODIS record.

| Event | Terra | Aqua |
|---|---|---|
| Crossing time while maintained | 10:30–10:45 until Feb 2002, then 10:28–10:32 | 13:30–13:45 |
| Last maneuver holding crossing time | 27 Feb 2020 | 18 Mar 2021 |
| Last maneuver holding altitude and ground track | 28 Jul 2022 | 1 Dec 2021 |
| Left its maintained crossing-time range | March 2021 | February 2023 (passed 13:45) |
| Left its constellation | Two lowering burns, 12 and 19 Oct 2022, about 5.5 km | Free drift downward from January 2022, no burn |
| Direction of drift | Earlier in the morning | Later in the afternoon |
| Crossing time on 13 Nov 2026 (computed) | about 08:33 | about 15:49 |

- The 16-day repeating ground track (held to ±20 km) was lost within months of the last altitude maneuver on each satellite. Source: [Twedt et al. 2023](https://ntrs.nasa.gov/api/citations/20240001409/downloads/2023_SPIE_Twedt_MODIS_EV_orbit_drift_manuscript_v4.pdf).
- NASA publishes no year-by-year table of crossing time. The Terra and Aqua pages show it only as plots. Dated values found: Terra reached 10:15 by fall 2022, and Aqua passed 13:45 in February 2023.
- A lower orbit gives slightly narrower swaths and slightly smaller pixels. No primary source quantifies the effect on the fire product. The MODIS fire team describes the effect of drift on fire counts as under investigation.

### End of the MODIS missions

Both MODIS instruments were producing data on 13 November 2026 ([MCST Terra weekly report](https://mcst.gsfc.nasa.gov/iot/am1weekly20263112026317), [MCST Aqua weekly report](https://mcst.gsfc.nasa.gov/iot/pm1weekly20263112026317)). Earlier plans to shut Aqua down in August 2026 and to lower Terra's orbit in early 2026 were not carried out.

- The newest NASA projection is end of science in **February 2027 for Terra** and **September 2027 for Aqua** ([NASA Science, updated 20 Mar 2026](https://science.nasa.gov/science-research/earth-science/terra-the-end-of-an-era)). These are projections and no shutdown dates are set.
- No MODIS-like instrument exists at Terra's morning crossing time. All VIIRS satellites fly the afternoon orbit ([LAADS MODIS to VIIRS transition](https://ladsweb.modaps.eosdis.nasa.gov/learn/modis-to-viirs-transition)).

### The three VIIRS satellites

- All three fly in one orbital plane and so observe at the same local solar time, close to Aqua's original 13:30. They differ in when they pass along the orbit.
- From 2018 to 2022, NOAA-20 flew half an orbit (about 50 minutes) from Suomi NPP.
- NOAA-21 joined a quarter orbit from Suomi NPP. Between 20 March and 4 April 2024, NOAA-20 was moved to sit half an orbit from NOAA-21, with Suomi NPP between them about 25 minutes from each ([OSPO notice](https://www.ospo.noaa.gov/data/messages/2024/04/MSG_20240404_1604.html)).
- The FIRMS FAQ gives the NOAA-20 crossing as about 12:40. That figure confuses the along-orbit offset with local time. NOAA lists 13:25 for the plane.
- **Suomi NPP data ended at 15:40 UTC on 2 November 2026**, permanently, by NOAA decision ([NESDIS notice](https://www.nesdis.noaa.gov/news/cessation-of-suomi-national-polar-orbiting-partnership-s-npp-data-users-onafter-november-2-2026), [FIRMS FAQ](https://www.earthdata.nasa.gov/data/tools/firms/faq)). No reason is given. The archive stays available.
- Follow-ons: JPSS-4 (to be NOAA-22) is planned for launch on 1 September 2027, and JPSS-3 late in 2032. NOAA's July 2026 chart shows VIIRS coverage in this orbit planned into the late 2030s ([NOAA LEO update, May 2026](https://www.ssec.wisc.edu/meetings/wp-content/uploads/sites/33/2026/06/2.5_Zhou.pdf)).

## Instruments

Detail: [modis-instrument.md](sensor-research/modis-instrument.md), [viirs-instrument.md](sensor-research/viirs-instrument.md).

### Side by side

| | MODIS | VIIRS |
|---|---|---|
| Spectral bands | 36, from 0.405 to 14.385 µm | 22, from 0.402 to 12.49 µm |
| Resolution groups at nadir | 250 m (2 bands), 500 m (5), 1 km (29) | 375 m imagery "I" bands (5), 750 m moderate "M" bands (16), one day/night band |
| Scanner | Two-sided rotating scan mirror | Rotating telescope |
| Scan angle range | ±55° | ±56.28° |
| Swath width | 2330 km | about 3060 km |
| Detectors per scan, fire bands | 10 per 1 km band (a scan is 10 km along track at nadir) | 32 per I band, 16 per M band |
| Granule | 5 minutes; 1354 samples × 2030 lines at 1 km | 6 minutes; 6400 I-band samples per row, about 202 scans |
| Fire pixel at nadir | 1.00 × 1.00 km | 0.385 × 0.367 km (I band) |
| Fire pixel at swath edge | 4.82 × 2.00 km | 0.82 × 0.81 km (I band) |
| Pixel area growth, nadir to edge | about 9.7 times | about 4.5 times |
| Control of along-scan growth | None | Three aggregation zones (3, 2, then 1 native samples per pixel) |
| Overlap between successive scans | Kept in the data; up to about 50% at the swath edge | Mostly deleted on board |
| Design life | 6 years | 7 years |

Sources: [LAADS MODIS](https://ladsweb.modaps.eosdis.nasa.gov/missions-and-measurements/modis/), [MODIS C6/C6.1 Fire User's Guide](https://earthdata.nasa.gov/s3fs-public/2023-09/MODIS_C6_C6.1_Fire_User_Guide_1.0.pdf), [VIIRS L1B User's Guide](https://ladsweb.modaps.eosdis.nasa.gov/api/v2/content/archives/Document%20Archive/Science%20Data%20Product%20Documentation/NASA_VIIRS_L1B_UG_August_2021.pdf), [Lin et al. 2011](https://ntrs.nasa.gov/api/citations/20110022523/downloads/20110022523.pdf), [Schroeder et al. 2014](https://directreadout.sci.gsfc.nasa.gov/publications_documents/Schroeder_et_al_2014b_RSE.pdf).

### Channels used for fire

| Role | MODIS (1 km) | VIIRS 375 m product | VIIRS 750 m product |
|---|---|---|---|
| Mid-infrared fire channel | Band 22, 3.96 µm, high gain. Saturates near 329 K (Terra, measured). Noise 0.07 K. | I4, 3.74 µm (3.55–3.93). Saturated pixels carry 367 K. Noise specification 2.5 K, about 0.4 K on orbit. | M13, 4.05 µm (3.97–4.13), dual gain. Saturates near 634 K (design) to 659 K (product documents). |
| Mid-infrared, high range | Band 21, 3.96 µm, low gain. Saturates near 500 K (design), 478 K measured on Terra. Noise 0.20 K. | None. I4 has a single gain. | The low-gain state of M13. |
| Thermal background channel | Band 31, 11.03 µm. Saturates near 392 K on Terra; lower on Aqua. Noise 0.05 K. | I5, 11.45 µm (10.5–12.4). Saturates at 380 K. | M15, 10.76 µm |
| Cloud, glint and false-alarm tests | Bands 1, 2, 7, 32 | I1, I2, I3 (daytime only) | M5, M7, M11, M16 |

Sources: [Xiong & Chen](https://ntrs.nasa.gov/api/citations/20110015244/downloads/20110015244.pdf), [MCST calibration table](https://mcst.gsfc.nasa.gov/calibration/information), [Xiong et al. 2016](https://pmc.ncbi.nlm.nih.gov/articles/PMC7430510), [VIIRS 375 m Active Fire User's Guide v1.2](https://www.earthdata.nasa.gov/s3fs-public/2025-06/VIIRS_C2_AF-375m_User_Guide_1.2.pdf), [VNP14 ATBD](https://LPDAAC.USGS.GOV/documents/133/VNP14_ATBD.pdf).

- MODIS bands 21 and 22 have the same spectral response. Band 22 has about 25 times the gain, so it is more sensitive and saturates sooner.
- VIIRS I4 sits about 0.3 µm shorter than M13 and receives about three times more reflected sunlight.
- VIIRS I4 saturates at a far lower temperature than MODIS band 21. Besides plain saturation at 367 K, I4 can "fold over", where a very hot pixel reports an abnormally low temperature. The product detects these using I5.
- Because I4 saturates, the 375 m product takes fire radiative power from the co-located 750 m M13 band, not from I4.

### How pixel size changes across the swath

MODIS 1 km pixel, from the formulas in the fire user's guide (computed):

| Scan angle | Along scan | Along track | Area |
|---|---|---|---|
| 0° (nadir) | 1.00 km | 1.00 km | 1.00 km² |
| 18° | 1.13 km | 1.06 km | 1.19 km² |
| 34° | 1.58 km | 1.24 km | 1.95 km² |
| 55° (edge) | 4.82 km | 2.00 km | 9.66 km² |

VIIRS 375 m pixel, nominal values at 824 km altitude ([Lin et al. 2011](https://ntrs.nasa.gov/api/citations/20110022523/downloads/20110022523.pdf)). The 750 m values are twice these.

| Position | Scan angle | Along scan | Along track |
|---|---|---|---|
| Nadir (zone 1, three samples averaged) | 0° | 385 m | 367 m |
| End of zone 1 | 31.72° | 577 m | 443 m |
| Start of zone 2 (two samples averaged) | 31.72° | 385 m | 443 m |
| End of zone 2 | 44.86° | 644 m | 556 m |
| Start of zone 3 (no averaging) | 44.86° | 322 m | 556 m |
| End of scan | 56.28° | 822 m | 807 m |

- Half of all MODIS observations are taken at view angles where the pixel area is at least 50% larger than at nadir ([Sayer et al. 2015](https://amt.copernicus.org/articles/8/5277/2015/amt-8-5277-2015.pdf)).
- The MODIS along-scan response is triangular. Each sample takes about 75% of its signal from its own nominal pixel and 25% from its two neighbours, so one fire can register in two adjacent pixels ([Tan et al. 2006](https://sites.bu.edu/cliveg/files/2013/09/tanbin03.pdf)).
- Successive MODIS scans overlap by about 6% at 18°, 19% at 34° and 50% at the swath edge (computed). MODIS keeps these overlapping lines. VIIRS deletes the outermost rows of each scan in zones 2 and 3 before downlink, which removes about half of the redundancy.
- Orbit decay has shrunk the MODIS pixel. It was about 970 m along scan at nadir by spring 2025, and gaps between scans have opened at nadir ([Giglio, May 2025](https://landweb.modaps.eosdis.nasa.gov/data/filePost/LANCE_UWG_Orbit_Drift_Giglio_202505.pdf)).

### Differences between units of the same instrument

| Units | Documented difference |
|---|---|
| Terra vs Aqua MODIS | Aqua's thermal bands saturate at lower temperatures than Terra's (no table published; one abstract gives about 340 K against 380 K for bands 31 and 32). |
| Terra vs Aqua MODIS | Over a warm ocean target, 2000–2020, Terra minus Aqua brightness temperature: band 21 −0.15 K, band 22 +0.45 K, band 31 −0.31 K ([Pérez Díaz et al. 2021](https://ntrs.nasa.gov/api/citations/20210013903/downloads/Terra%20and%20Aqua%20MODIS%20thermal%20emissive%20bands%20paper.pdf)). |
| Terra MODIS | Electronic crosstalk affects some mid-infrared detectors, including band 21 detectors 1 and 9 and band 22 detector 8. It grew after the February 2016 safe mode. Collection 6.1 does not correct it for the fire bands. |
| Terra MODIS before November 2000 | Crosstalk, dead detectors and band 21 miscalibration. Fire location data for this period are not distributed. |
| Suomi NPP vs NOAA-20 VIIRS | Same design. Spectral response differences cause brightness-temperature biases of a few hundredths of a kelvin in M13 ([Lin & Cao 2019](https://repository.library.noaa.gov/view/noaa/45210/noaa_45210_DS1.pdf)). |
| NOAA-21 VIIRS | The M13 spectral response differs from NOAA-20. NOAA's review says fire measurements "would be hotter on NOAA-21" and that this may affect the saturation level ([NOAA-21 maturity review, 2023](https://www.star.nesdis.noaa.gov/JPSS/documents/AMM/N21/NOAA-21_VIIRS_Validated.pdf)). |
| NOAA-20 VIIRS | Detector 29 of band I3 is very noisy and is flagged, not removed. |
| All three VIIRS | No brightness-temperature offsets between units have been published for I4 or I5, the two bands the 375 m detection uses. |

## Earth coverage and overpass timing

Detail: [coverage-overpass.md](sensor-research/coverage-overpass.md).

### Coverage

| | One MODIS | One VIIRS |
|---|---|---|
| Swaths of consecutive orbits at the equator | A gap of about 350 km | An overlap of about 350 km (about 15%) |
| Latitudes with daily gaps | Between about 30°S and 30°N | None |
| Full global coverage | Every 1 to 2 days | Every 12 hours |

Sources: [FIRMS swath outlines post, June 2026](https://www.earthdata.nasa.gov/news/blog/new-firms-data-product-satellite-swath-outlines), [FIRMS FAQ](https://www.earthdata.nasa.gov/data/tools/firms/faq), [VIIRS 375 m User's Guide](https://www.earthdata.nasa.gov/s3fs-public/2025-06/VIIRS_C2_AF-375m_User_Guide_1.2.pdf).

### Observations per day

No source publishes a table of overpasses per day by latitude. These are the sourced anchor points.

| Configuration | Where | Observations per day |
|---|---|---|
| One MODIS | Equator | Less than one day pass and one night pass on some days |
| Terra plus Aqua | Equator | At least four for almost every area |
| One VIIRS | Equator | One day pass and one night pass |
| One VIIRS | Mid-latitudes | Three to four |
| One MODIS or one VIIRS | High latitudes | Six to eight |
| One MODIS | Poles | Nearly fifteen |

- Swaths of consecutive orbits, about 100 minutes apart, overlap more toward the poles. One sensor can therefore see the same fire twice in 100 minutes, and the count of one persistent fire rises with latitude.
- The three VIIRS satellites share one orbital plane, so two or three of them multiply the single-satellite number of looks at about the same local time. No source gives the combined count.
- NASA's own gridded MODIS fire product corrects raw pixel counts "for multiple satellite overpasses and missing observations", because raw counts are biased at high latitudes ([Giglio et al. 2006](https://dataserver-coids.inpe.br/queimadas/queimadas/Publicacoes-Impacto/material3os/2006_Giglio_etal_GlobalDistribuiton_JGR_DE3os.pdf)). FIRMS point data carry no such correction.
- NASA does not distribute a daily gridded MODIS fire summary, because "at most latitudes a single MODIS instrument simply does not sample the Earth's surface adequately in time periods shorter than about 8 days" (fire user's guide, section 8.6.2). Its gridded summaries are 8-day and monthly.

### Local time of observation

| Satellite | Day pass (maintained orbit) | Night pass (maintained orbit) | Day pass, November 2026 |
|---|---|---|---|
| Terra | about 10:30 | about 22:30 | about 08:33 (computed) |
| Aqua | about 13:30 | about 01:30 | about 15:49 (computed) |
| Suomi NPP | about 13:30 | about 01:30 | ended |
| NOAA-20, NOAA-21 | about 13:25–13:30 | about 01:25–01:30 | about 13:24–13:32 (computed) |

- These are equator crossing times. The local solar time of a pixel also varies across the swath, by roughly ±40 minutes for MODIS and ±55 minutes for VIIRS at the equator, and by more at higher latitudes. These figures are geometric estimates made during this research.
- Terra is the only morning observer in the record.

### The daily fire cycle

- Fire activity peaks in the afternoon. In a seven-year tropical and subtropical study, peak burning time fell between about 13:00 and 18:30 local time ([Giglio 2007](https://dataserver-coids.inpe.br/queimadas/queimadas/Publicacoes-Impacto/material3os/2006_Giglio_GlobalDetection_UMaryland_DE3os.pdf)).
- About 90% of MODIS fire pixels in the tropics and subtropics come from daytime passes.
- The share of Terra plus Aqua fire pixels that come from Aqua varies by region (July 2002 to June 2005): nearly 100% in tropical broadleaf forest, about 75% across much of Africa and Southeast Asia, and about even in boreal forests of Siberia and North America and in central Eurasia ([Giglio et al. 2006](https://dataserver-coids.inpe.br/queimadas/queimadas/Publicacoes-Impacto/material3os/2006_Giglio_etal_GlobalDistribuiton_JGR_DE3os.pdf)).
- At boreal latitudes the local-time windows of Terra and Aqua overlap, so the paper cautions that the Terra-to-Aqua ratio is not a consistent measure of the daily cycle there.
- No source gives one global Terra-to-Aqua ratio, and no source compares NOAA-20 or NOAA-21 counts against Suomi NPP.

## What a hotspot count means

Detail: [pixel-geometry.md](sensor-research/pixel-geometry.md).

- A FIRMS hotspot is the centre point of one pixel that the algorithm flagged as containing at least one fire or other heat source. It is not the location of the fire itself, and it says nothing direct about the size of the fire ([FIRMS FAQ](https://www.earthdata.nasa.gov/data/tools/firms/faq)).
- A small intense fire and a broad cooler fire each produce one hotspot per pixel they occupy.

### Footprint ratio

| Position in swath | MODIS pixel area | VIIRS 375 m pixel area | Ratio |
|---|---|---|---|
| Nadir | 1.00 km² | 0.138 km² | about 7 |
| Swath edge | 9.66 km² (at 55°) | 0.623 km² (at 56.28°) | about 15 |

One fire front that MODIS reports as one or two pixels can appear as many adjoining VIIRS pixels. Because the two footprints grow at different rates across the swath, the ratio between the sensors' counts for the same fire depends on where in each swath the fire was seen. These ratios are computed from the sourced footprints.

### Smallest detectable fire

| Sensor | Documented sensitivity |
|---|---|
| MODIS | Routinely detects flaming and smouldering fires of about 1000 m². Under very good conditions (near nadir, little smoke, uniform surface), flaming fires of about 100 m². Under rare pristine conditions, about 50 m². (Fire user's guide, section 8.3.2.) |
| VIIRS 375 m | "Much higher sensitivity to fires of relatively small size" than the coarser products. See [Fire detection algorithms](#fire-detection-algorithms) for figures. |
| VIIRS 750 m | Performs more like Aqua MODIS than like the 375 m product. |

### Duplicate and extra pixels

- **MODIS scan overlap.** Off nadir, successive MODIS scans re-observe the same ground, which "artificially inflat[es] the number of off-nadir fire pixels" ([Csiszar et al. 2014](https://directreadout.sci.gsfc.nasa.gov/publications_documents/Csiszar_et_al_2014_JGR.pdf)). Nothing in the FIRMS files removes these.
- **MODIS along-scan response.** A fire's signal reaches halfway into each neighbouring pixel along the scan, so one fire can flag two adjacent pixels. No source says how often.
- **VIIRS overlap deletion.** VIIRS removes most scan overlap on board. Some "residual bow-tie" pixels remain and are flagged in the Level 2 swath file (quality bit 22). The FIRMS CSV has no quality field, so they cannot be removed there.
- **VIIRS count steps.** VIIRS counts plotted against scan angle show steps at the two aggregation boundaries, because pixel size changes abruptly there.
- **Advice in the FIRMS FAQ.** It says the gridded Level 2G products "account for overlapping satellite orbits to avoid double-counting fire detections" and are better suited to quantitative analysis than the point files.

### Documented count comparisons

These are the comparisons printed in the product documentation. Cross-calibration studies were out of scope for this research.

| Comparison | Period and area | Result |
|---|---|---|
| VIIRS 375 m vs VIIRS 750 m | Global, 2021, Collection 2 | About 3 times more daytime and 17 times more night-time fire pixels in the 375 m product |
| VIIRS 750 m vs Aqua MODIS | Global, 15 Feb – 15 Jun 2013 | VIIRS 750 m gave about 26% more detections within ±31° of nadir and about 70% more beyond it |
| Terra MODIS, Suomi NPP 375 m, Aqua MODIS | Lower Mekong, 1 March 2016, daytime | 606, 9,643 and 361 fire pixels |
| Same | Same day, night-time | 58, 4,608 and 22 fire pixels |

Sources: [VIIRS 375 m User's Guide, section 7 and Figure 4](https://www.earthdata.nasa.gov/s3fs-public/2025-06/VIIRS_C2_AF-375m_User_Guide_1.2.pdf), [Csiszar et al. 2014](https://directreadout.sci.gsfc.nasa.gov/publications_documents/Csiszar_et_al_2014_JGR.pdf). The Mekong figures are one day in one region.

The VIIRS guide adds that differences between the 375 m product and Aqua MODIS "are further magnified due to MODIS coverage gaps along the tropics" and MODIS pixel growth away from nadir.

### Geolocation accuracy

| Sensor | Error at nadir (root mean square) | Share of fire pixel |
|---|---|---|
| Terra MODIS | 43 m along track, 45 m along scan | about 5% |
| Aqua MODIS | 46 m along track, 53 m along scan | about 5% |
| Suomi NPP VIIRS | 70 m along track, 60 m along scan | about 15–20% |
| NOAA-20 VIIRS | 55 m along track, 49 m along scan | about 15% |
| NOAA-21 VIIRS | within 70 m | about 20% |

Sources: [Lin et al. 2019](https://mcst.gsfc.nasa.gov/sites/default/files/meetings_files/06_MODIS_GEO_Lin.pdf), [Wolfe et al. 2013](https://ntrs.nasa.gov/api/citations/20140010285/downloads/20140010285.pdf), [LAADS VJ203MOD](https://ladsweb.modaps.eosdis.nasa.gov/missions-and-measurements/products/VJ203MOD).

- Both products use terrain-corrected geolocation.
- Near-real-time locations are usually within 100 m of the final ones. After a spacecraft maneuver or severe space weather they can be off by several kilometres, typically for under 2 hours, but for up to 12 hours on Aqua ([FIRMS FAQ](https://www.earthdata.nasa.gov/data/tools/firms/faq)).
- At night, a tall superheated plume over a very large fire can be detected and placed beside the fire, toward the swath edge. The algorithm cannot separate these from surface fire pixels.

## Fire detection algorithms

Detail: [modis-fire-algorithm.md](sensor-research/modis-fire-algorithm.md), [viirs-fire-algorithm.md](sensor-research/viirs-fire-algorithm.md).

FIRMS distributes two different algorithms: the MODIS 1 km algorithm and the VIIRS 375 m algorithm. A third, the VIIRS 750 m algorithm, is a port of the MODIS one. FIRMS does not distribute it, but NASA produces it for every VIIRS satellite.

| | MODIS 1 km (MOD14 / MYD14) | VIIRS 375 m (VNP14IMG / VJ114IMG / VJ214IMG) | VIIRS 750 m (VNP14 / VJ114 / VJ214) |
|---|---|---|---|
| In FIRMS | Yes | Yes | No (Earthdata only) |
| Reference | [Giglio et al. 2016](https://www.earthdata.nasa.gov/s3fs-public/imported/Giglio2016_C6_Fire.pdf) | [Schroeder et al. 2014](https://directreadout.sci.gsfc.nasa.gov/publications_documents/Schroeder_et_al_2014b_RSE.pdf), [ATBD](https://viirsland.gsfc.nasa.gov/PDF/VIIRS_activefire_375m_ATBD.pdf) | [ATBD](https://viirsland.gsfc.nasa.gov/PDF/VIIRS_activefire_750m_ATBD.pdf) |
| Current version | Collection 6.1 | Collection 2 | Collection 2 |
| Approach | Contextual tests against the surrounding background, plus one absolute test | Fixed-threshold tests plus contextual tests | "Essentially identical" to MODIS Collection 6 |
| Absolute test, day | 4 µm temperature above 360 K | Saturated I4 (367 K) with supporting tests | As MODIS |
| Absolute test, night | 4 µm temperature above 320 K | I4 above 320 K | As MODIS |
| Day candidate threshold | Dynamic per scan position: background mean + 5 K, limited to 300–330 K | 325–330 K, set from the median of a 501 × 501 pixel window | As MODIS |
| Night candidate threshold | Same dynamic form | I4 above 295 K and I4 − I5 above 10 K | As MODIS |
| Background window | Grows to 21 × 21 pixels | Grows from 11 × 11 to 31 × 31 pixels | As MODIS |
| Night defined as solar zenith angle | 85° or more | 90° or more | 85° or more |
| Confidence output | 0–100% | Low, nominal, high | 0–100% |
| Fire radiative power from | The 4 µm band (21 or 22) | Co-located 750 m M13, split equally among the 375 m fire pixels inside it | M13 |
| Processes water pixels | Yes, since Collection 6 | Yes | Yes |

### Confidence

The two confidence fields measure different things and do not map onto each other.

| | MODIS | VIIRS 375 m |
|---|---|---|
| Scale | 0–100% | Low, nominal, high |
| How it is derived | Geometric mean of up to five scores: how far the pixel stands above its background, and how many neighbouring pixels are cloud or water | From which test detected the pixel |
| Low | Below 30% | Daytime pixels usually linked to sun glint or water, with an I4 anomaly under 15 K |
| Nominal | 30% to under 80% | Free of daytime sun glint, with an anomaly over 15 K, day or night |
| High | 80% or more | Saturated pixels, day or night |

- VIIRS "high" means the pixel saturated. It does not mean "most certain".
- At night, VIIRS low-confidence pixels occur only in the South Atlantic region described below. FIRMS removes them from its near-real-time data.
- NASA says of MODIS confidence that "there is no way to establish an optimal cutoff a priori". The user's guide notes that some highly questionable pixels still score as nominal, and that users wanting fewer false alarms may keep only nominal and high.

### Fire radiative power

| | MODIS | VIIRS 375 m |
|---|---|---|
| Method | Mid-infrared radiance method of Wooster et al. (2003) | Same method |
| Band | 21 or 22 (3.96 µm) | M13 (4.05 µm) at 750 m |
| Coefficient | 3.0 × 10⁻⁹ W m⁻² sr⁻¹ µm⁻¹ K⁻⁴ | 2.88 × 10⁻⁹ |
| Atmospheric correction | None | None |
| Units | MW per pixel | MW per pixel |
| When the band saturates | Band 21 takes over from band 22 | Fire radiative power is set to zero (rare) |

- Several 375 m fire pixels inside one 750 m pixel carry equal shares of one value.
- M13 partly overlaps a carbon dioxide absorption band. The VIIRS algorithm document says atmospheric loss "may double" relative to MODIS and "could lead to systematic underestimation of VIIRS FRP values compared to coincident MODIS data".
- MODIS changed method at Collection 6. For the same fire pixels, mean values fell about 16% from Collection 5 (56.9 to 47.7 MW). The whole archive now uses the Collection 6 method.
- FIRMS says the VIIRS 375 m product gained M13-based values "starting in 2015". No source says whether the Collection 2 reprocessing carries them back to 2012.

### Detection performance

| Measure | MODIS (Collection 6, Terra, near nadir) | VIIRS 375 m (Suomi NPP, August 2013) |
|---|---|---|
| Daytime false alarm rate | 1.2% globally (2.4% in Collection 5) | Under 1.2% for nominal and high confidence |
| Night-time false alarm rate | None found | Negligible outside the South Atlantic region |
| Missed fires | 86% of all fires visible to a 30 m sensor; under 10% for large fires | Not published as a rate |
| Low-confidence share | Not published | About 10% of fire pixels; confirmed false alarms among them peaked near 40% over eastern China |
| Smallest fire detected in a test | See [Smallest detectable fire](#smallest-detectable-fire) | A bonfire of 1.25 m radius at about 1000 K, at night, 32.7° off nadir |

- The MODIS validation used a 30 m sensor on Terra itself, so it covers Terra only and only pixels within 8.55° of nadir. No Collection 6 validation of Aqua or of off-nadir pixels is published.
- MODIS detection probability by region ranges from 7% to 26% of all fires, driven by typical fire size.
- VIIRS detects better at night than by day because night backgrounds are more uniform.
- VIIRS I4 saturated in about 8% of daytime fire pixels and 1% of night-time ones in the August 2013 sample.

### Known artifacts

| Artifact | MODIS | VIIRS 375 m |
|---|---|---|
| Sun glint | Rejection tests, widened in Collection 6 | Pixels in glint are excluded or downgraded to low confidence |
| Bright or hot surfaces | False alarms at desert edges | False alarms from large metal roofs and bright urban surfaces by day |
| Small forest clearings | About 35% false alarms in the Amazon in Collection 5; a new test in Collection 6 reduces them | Not reported |
| South Atlantic Anomaly | Not reported | Radiation noise produces false night-time detections between about 110°W and 11°E, 7°N and 55°S. A filter removes most and also removes some real small fires and gas flares. |
| Cloud | An internal mask that misses small clouds and cloud edges | A deliberately lenient mask, so fires under thin cloud are kept |
| Persistent sources over water | Processed and labelled offshore | Must persist or stand out in M13, or they are removed |

Neither point product records cloud cover or missed observations. The MODIS guide states that the absence of a hotspot may be due to cloud, a coverage gap or a mask error, and that "severe temporal and spatial biases may arise in any MODIS fire time series analysis employing time intervals shorter than about eight days."

### Version history that affects the record

| Product | Versions | What it means for the archive |
|---|---|---|
| MODIS | Collection 5 (from 2006), Collection 6 (from 2015), Collection 6.1 (land from late 2020; FIRMS near-real-time from April 2021) | The whole archive was reprocessed with Collection 6. Collection 6.1 made no change to the fire algorithm. In a one-month test the global totals differed by 0.001%, and NASA says the two "may be freely intermixed". |
| MODIS | Collection 7 | The Level 1 inputs moved to version 7.0 in 2026 and version 6.1 inputs were due to be withdrawn on 30 September 2026. No Collection 7 fire product has been released, and version 6.1 fire files were still being produced in November 2026. |
| VIIRS 375 m | Collection 1, then Collection 2 (archive released April 2024) | Collection 1 had "bad scan" files with lines of false detections, most often in 2012. Collection 2 uses new inputs and quality flags that "virtually eliminate" them. The Collection 2 archive covers the full record. |
| VIIRS 375 m | Monthly location files, version 3 (May 2025) | Versions 1 and 2 often mislabelled static heat sources as vegetation fires. Version 3 fixed this and all files were reprocessed. |
| VIIRS 375 m | Across satellites | NASA produces the product "independently for each VIIRS sensor". No source states that the code and thresholds are identical for the three satellites, and no satellite-specific caveat is listed. |

## FIRMS data

Detail: [firms-csv-schema.md](sensor-research/firms-csv-schema.md), [firms-processing-streams.md](sensor-research/firms-processing-streams.md), [firms-confidence-type-quality.md](sensor-research/firms-confidence-type-quality.md).

### Columns, side by side

Column names and values as they appear in FIRMS CSV files. The headers were read from small country files on the FIRMS server and from FIRMS tutorial output.

| Column | MODIS | VIIRS 375 m | Notes |
|---|---|---|---|
| `latitude`, `longitude` | Centre of the 1 km pixel | Centre of the 375 m pixel | Degrees, WGS84. Not the fire's own position. |
| `brightness` / `bright_ti4` | `brightness`: band 21 or 22 temperature, K | `bright_ti4`: I4 temperature, K | Different wavelengths (3.96 and 3.74 µm). VIIRS values stop at 367 K. |
| `bright_t31` / `bright_ti5` | `bright_t31`: band 31, K | `bright_ti5`: I5, K | Different wavelengths (11.0 and 11.45 µm). |
| `scan`, `track` | About 1.0–4.8 and 1.0–2.0 km | About 0.3–0.8 km for both | Actual pixel size across and along the track. MODIS has one decimal place, VIIRS two. The ranges are expected values from the pixel geometry, not read from a full file. |
| `acq_date` | `YYYY-MM-DD` | Same | UTC date. |
| `acq_time` | `HHMM` | Same | UTC. Zero-padded text in country files (`0130`). FIRMS tutorials parse it as an integer (`3` means 00:03). |
| `satellite` | `Terra`, `Aqua` | `N` (Suomi NPP), `N20`, `N21` | Documentation says `T` and `A`; the files say `Terra` and `Aqua`. |
| `instrument` | `MODIS` | `VIIRS` | |
| `confidence` | Integer 0–100 | `l`, `n`, `h` | See [Confidence](#confidence). |
| `version` | `6.1NRT` for near-real-time; `6.2`, `6.03` or `61.03` in standard country files | `2.0NRT`, `2.0RT`, `2.0URT` for near-real-time; `2` for standard | The only per-row marker of near-real-time versus standard data. |
| `frp` | MW | MW | Computed differently. See [Fire radiative power](#fire-radiative-power). |
| `daynight` | `D`, `N` | `D`, `N` | Assigned by different rules in near-real-time and standard data (below). |
| `type` | 0–3, standard files only | 0–3, standard files only | Absent from near-real-time files. |

Sources: [FIRMS attributes page](https://www.earthdata.nasa.gov/data/tools/firms/active-fire-data-attributes-modis-viirs), [FIRMS API tutorial](https://firms.modaps.eosdis.nasa.gov/content/academy/data_api/firms_api_use.html), [country file index](https://firms.modaps.eosdis.nasa.gov/data/country/yearly_summary_files.txt).

- **Time of day.** Local solar time is not in the file. It has to be worked out from `acq_time` and longitude. The UTC date and the local date differ for part of each day at most longitudes.
- **Meaning of `acq_time`.** NASA does not say whether it is the time of the pixel or the start of the granule. Observed MODIS values are not multiples of five minutes, which suggests pixel or scan time. That reading is an inference.
- **MODIS version strings.** `6.2` appears in country files for 2000–2017, `6.03` for 2018–2022 and `61.03` for 2023–2025. They are undocumented. One reading is collection plus location-file version, which would make the 2000–2022 country files Collection 6. Given the 0.001% difference between Collections 6 and 6.1, this has little practical effect.
- **Documentation lag.** The FIRMS attributes page still lists VIIRS versions as `1.0NRT` and `1.0`. Current files carry the Collection 2 strings above.

### Near-real-time and standard data

| | Near-real-time (NRT) | Standard (science quality) |
|---|---|---|
| Source | NASA LANCE, within about 3 hours | Monthly location files from the University of Maryland fire team: MCD14ML for MODIS, VNP14IMGML, VJ114IMGML and VJ214IMGML for VIIRS |
| Detection algorithm | Same as standard | Same as near-real-time |
| Geolocation | Predicted orbit data; usually within 100 m of final | Final orbit data |
| Gaps | Processing interruptions can leave gaps | Missing granules are filled; data degraded by maneuvers are removed |
| `type` column | Absent | Present |
| `daynight` rule | Orbit direction: ascending is day, descending is night | Solar zenith angle: above 85° is night |
| API source names | `MODIS_NRT`, `VIIRS_SNPP_NRT`, `VIIRS_NOAA20_NRT`, `VIIRS_NOAA21_NRT` | `MODIS_SP`, `VIIRS_SNPP_SP`, `VIIRS_NOAA20_SP`, `VIIRS_NOAA21_SP` |

- **Lag.** Standard data replace near-real-time data after "approximately a 5 month lag" according to the archive download page, 2–3 months according to the FAQ, and about 2 months according to the LANCE product pages. A June 2025 API example showed standard data ending 4–5 months before the query date. The most recent months of any download are therefore near-real-time rows.
- **Faster streams.** Real-time (`RT`) and ultra-real-time (`URT`) rows come from direct-broadcast stations and cover the United States and Canada only. They are removed once the matching near-real-time rows arrive or after 6 hours. They appear inside the `_NRT` API sources, so a recent query over Canada can include them.
- **NASA's advice.** The MODIS guide says near-real-time locations "should not be used for time series analyses or long-term studies". The VIIRS guide says scientific studies "should favor" the standard data.
- **Count differences.** No source quantifies how much near-real-time and standard counts differ.

### What is available, by sensor

| Sensor | FIRMS archive | Yearly country CSVs, no key needed | API standard source |
|---|---|---|---|
| MODIS (Terra and Aqua together) | 1 Nov 2000 – present | 2000–2025, prefix `modis` | `MODIS_SP` |
| VIIRS Suomi NPP | 20 Jan 2012 – 2 Nov 2026 | 2012–2025, prefix `viirs-snpp` | `VIIRS_SNPP_SP` |
| VIIRS NOAA-20 | 1 Apr 2018 – present | 2018–2025, prefix `viirs-jpss1` | `VIIRS_NOAA20_SP` |
| VIIRS NOAA-21 | 1 Mar 2023 – present (archive page) | None | `VIIRS_NOAA21_SP` |

- **NOAA-20 country files exist.** They are published under the prefix `viirs-jpss1`, for example `https://firms.modaps.eosdis.nasa.gov/data/country/viirs-jpss1/2023/viirs-jpss1_2023_Canada.csv` (138 MB). This was checked on 2026-11-13 with header-only requests and against the [country file index](https://firms.modaps.eosdis.nasa.gov/data/country/yearly_summary_files.txt). It corrects the note in [challenge.md](challenge.md) that NOAA-20 country paths return 404; the path tried there used a different prefix.
- **NOAA-21 has no country files.** The index contains none, and the `viirs-jpss2` path returns 404.
- **2026 is not published yet.** The 2025 files were last updated on 10 October 2026.
- **Country files carry standard data.** Sampled rows have standard version strings and a `type` column.
- **Canada file sizes.** MODIS files run from under 1 MB to 26 MB a year. Suomi NPP and NOAA-20 files run from 4 MB to 141 MB a year; 2023 is the largest.
- **Archive requests.** The archive download tool serves data older than 7 days as CSV, shapefile or JSON.
- **API limits.** 5000 transactions per 10 minutes per key, and 1 to 5 days per request.

### The type column

| Value | Meaning | How it is assigned |
|---|---|---|
| 0 | Presumed vegetation fire | The default for land |
| 1 | Active volcano | |
| 2 | Other static land source | MODIS: detected on 16 or more days in a calendar year, or inside an urban area in the land cover map. The VIIRS rule is not documented. |
| 3 | Offshore | Every detection over water |

- Static and non-vegetation sources are not removed from the location files. They are only labelled.
- The MODIS guide says some static sources remain unlabelled.
- Near-real-time rows have no type, so the most recent months cannot be filtered this way.
- VIIRS files produced before the May 2025 reprocessing often labelled static sources as type 0.

### What NASA says about combining the sensors

- The FIRMS FAQ gives no count comparison between MODIS and VIIRS and no guidance on combining them in a time series.
- It describes the 375 m data as complementing MODIS, showing "good agreement in hotspot detection", with "a greater response over fires of relatively small areas" and "improved nighttime performance".
- It says of confidence that it "should be used with caution as it is likely that it will vary in terms of meaning in different parts of the world."
- A NASA training session (January 2025) puts the five sensors together at 8–10 observations a day from the equator to mid-latitudes and 15–20 at polar latitudes.

## Outages and gaps

Detail: [outages-gaps.md](sensor-research/outages-gaps.md). All dates are UTC. The table lists every gap of about a day or longer that was found. Shorter partial-day losses are in the detail file.

| Sensor | Dates | Length | Cause | Listed by FIRMS as missing |
|---|---|---|---|---|
| Terra MODIS | 15 Apr 2001 | 1 day | Not found | Yes |
| Terra MODIS | 15 Jun – 3 Jul 2001 | about 18 days | Power supply failure | Yes |
| Terra MODIS | 19 – 28 Mar 2002 | about 10 days | Spacecraft safe mode | Yes |
| Terra MODIS | 16 – 24 Dec 2003 | about 6–8 days | Spacecraft safe mode | No |
| Terra MODIS | 22 Aug 2006 | Unknown | Instrument doors closed by mistake | No |
| Terra MODIS | 18 – 24 Feb 2016 | about 6 days | Safe mode during a maneuver | No |
| Terra MODIS | 15 – 17 Mar 2022 | about 2 days degraded | Radiation upset; later reprocessed | No |
| Terra MODIS | 10 – 21 Oct 2022 | about 10–13 days | Constellation exit burns | Not known |
| Terra MODIS | 26 – 27 Mar 2026 | about 23.5 hours | Command load expired | Not known |
| Aqua MODIS | 16 Aug – 2 Sep 2020 | about 17 days, sparse coverage only | Data formatter failure | Not known |
| Aqua MODIS | 22 Feb – 23 Mar 2022 | Loss not stated | Formatter and recorder anomaly | Not known |
| Aqua MODIS | 31 Mar – 16 Apr 2022 | about 17 days | Spacecraft safe mode | Not known |
| Suomi NPP VIIRS | 26 Jul – 20 Aug 2022 | about 25 days | Spacecraft safe mode; not recoverable | Not known |
| Suomi NPP VIIRS | 2 – 6 Nov 2024 | about 3.9 days | GPS anomaly | Not known |
| Suomi NPP VIIRS | 3 – 8 Jul 2025 | Partial | Wildfire near the Fairbanks ground station | Not known |
| Suomi NPP VIIRS | 9 – 13 Mar 2026 | about 3.6 days | Geolocation errors | Not known |
| Suomi NPP VIIRS | 28 Apr – 1 May 2026 | about 3 days | Spacecraft anomaly | Not known |
| Suomi NPP VIIRS | 1 – 2 Jun 2026 | about 1.5 days | Spacecraft anomaly | Not known |
| Suomi NPP VIIRS | 10 – 17 Jul 2026 | about 6.7 days | Spacecraft anomaly | Not known |
| Suomi NPP VIIRS | 3 – 6 Aug 2026 | about 3.6 days | Spacecraft anomaly | Not known |
| Suomi NPP VIIRS | 2 Nov 2026, 15:40 | Permanent | End of data | Yes |
| NOAA-20 VIIRS | 3 – 4 Feb 2024 | about 22 hours | Processor reset | Not known |
| NOAA-20 VIIRS | 20 Feb 2024 | about 8–10 hours | Instrument processor reset | Not known |
| NOAA-20 VIIRS | 20 Mar – 4 Apr 2024 | Scattered gaps | Orbit rephasing | Not known |
| NOAA-20 VIIRS | 3 – 8 Jul 2025 | Partial | Fairbanks wildfire | Not known |
| NOAA-21 VIIRS | 22 Jun 2024 | about 5 hours | Spacecraft safe mode | Not known |
| NOAA-21 VIIRS | 1 Oct 2025 | Unknown; end not found | Instrument safe mode | Not known |
| NOAA-21 VIIRS | 29 Jul 2026 | 96 minutes | Thermal band anomaly | Not known |
| NOAA-20 and NOAA-21 | 27 Oct 2026 | Unknown | Raw data gaps | Not known |
| NOAA-20 and NOAA-21 | 5 – 7 Nov 2026 | Unknown; still open on 13 Nov | Not stated | Not known |

- **The FIRMS list is incomplete.** The FAQ names only the three early Terra gaps. The FIRMS missing-data table it links to could not be read during this research, so it is not known which later events FIRMS counts as missing.
- **Suomi NPP's last year.** Its 2026 record has five separate multi-day gaps before the end in November.
- **More small gaps since July 2023.** Terra and Aqua moved to reduced-staffing operations on 7 July 2023 and no longer replay recorded data to fill gaps, so partial-day gaps are more frequent.
- **Changes that leave no gap.** Terra's October 2022 orbit lowering, the continuing drift of both MODIS orbits, and calibration table changes on Suomi NPP from May 2026 alter the data without removing any.
- **Combined products during the Aqua 2020 gap.** NASA built its Terra-plus-Aqua land products from Terra alone for 16 August to 2 September 2020.

## Calibration and instrument health

Detail: [calibration-lifetime.md](sensor-research/calibration-lifetime.md).

### Years in service

| Instrument | Design life | In service on 13 Nov 2026 |
|---|---|---|
| Terra MODIS | 6 years | 26.9 years |
| Aqua MODIS | 6 years | 24.5 years |
| Suomi NPP VIIRS | 5 years (unconfirmed on a primary page) | 15.0 years, to the end of data |
| NOAA-20 VIIRS | 7 years | 9.0 years |
| NOAA-21 VIIRS | 7 years | 4.0 years |

### Stability of the fire bands

| Instrument | Finding | Source |
|---|---|---|
| Terra and Aqua MODIS, band 31 | Change of about 0.003 K per year over 2000–2020, described as negligible | [Pérez Díaz et al. 2021](https://ntrs.nasa.gov/api/citations/20210013903/downloads/Terra%20and%20Aqua%20MODIS%20thermal%20emissive%20bands%20paper.pdf) |
| Terra and Aqua MODIS, bands 21 and 22 | About 0.04 K per year against an ocean reference (0.074 for Aqua band 21), or roughly 0.8 K over the mission. Measured at about 300 K, not at fire temperatures. | Same |
| Terra MODIS after the February 2016 safe mode | Bands 27–30 changed by up to 25%. MCST found "no observable impact" on the other thermal bands, which include the fire bands. | [MCST recovery summary](https://mcst.gsfc.nasa.gov/sites/default/files/news/MCST_Terra_MODIS_Safe_Mode_Recovery.pdf) |
| Terra MODIS after June 2001 | A power-supply failure moved the instrument to its A-side electronics. "Significant striping" in bands 21 and 22 followed, with "some degradation of the fire products". | [Justice et al. 2002](https://gis-lab.info/docs/justice02_the_modis_fire_products.pdf) |
| Terra MODIS, blackbody | The calibration blackbody set point changed from 290 K to 285 K in April 2020. Aqua has always used 285 K. | [Chang et al. 2021](https://ntrs.nasa.gov/api/citations/20220000138/downloads/2021_Chang_SPIE_TEB_ScanCopy.pdf) |
| Suomi NPP VIIRS | Mid-infrared gain change within 0.5% after six years. I5 gain fell about 1.8%. Noise was unchanged. | [Xiong et al. 2019](https://ntrs.nasa.gov/api/citations/20190000314/downloads/20190000314.pdf) |
| NOAA-20 VIIRS | Ice on the detector window reduced I5 gain after launch. Heating on 12 March 2018 restored it. Stable since, with I5 changing about 0.3% per year. | Same |
| NOAA-21 VIIRS | Ice contamination caused gain loss. Heating on 23 February 2023 and 26 February 2024 appears as steps in the gain record. Noise stays within specification. | [Angal et al. 2026](https://ntrs.nasa.gov/api/citations/20260008550/downloads/SPIE26_N21TEB_Angal_revD_assubmitted.pdf) |
| NOAA-21 VIIRS, M13 | M13 differs from the other two units by 0.23–0.31 K (from a paper abstract). NOAA's own fire product shows fire radiative power up to about 10% higher on NOAA-21. That figure is for NOAA's product, not NASA's. | [NOAA-21 fire product readme](https://www.star.nesdis.noaa.gov/JPSS/documents/AMM/N21/NOAA-21_Active_Fires_Provisional_Readme.pdf) |

- Both instruments calibrate their thermal bands on every scan against an on-board blackbody, so slow gain drift has little effect on the calibrated values.
- No source documents a change in MODIS or VIIRS fire detection counts caused by instrument ageing.
- NOAA-20 and NOAA-21 fire data in FIRMS start after the first heating event on each satellite.

### Spectral differences between the sensors

| | MODIS bands 21 and 22 | VIIRS I4 | VIIRS M13 |
|---|---|---|---|
| Range | 3.929–3.989 µm | 3.55–3.93 µm | 3.973–4.128 µm |
| Width | 0.06 µm | 0.38 µm | 0.155 µm |
| Documented effect | Reference | About three times more reflected sunlight than M13, which reduces contrast between fires and bright surfaces by day | Overlaps a carbon dioxide absorption band, so atmospheric loss "may double" relative to MODIS |

| | MODIS band 31 | VIIRS I5 | VIIRS M15 |
|---|---|---|---|
| Range | 10.78–11.28 µm | 10.5–12.4 µm | 10.26–11.26 µm |
| Width | 0.5 µm | 1.9 µm | 1.0 µm |

No source publishes a brightness-temperature conversion between MODIS band 21 or 22 and VIIRS I4.

## Upstream products and file formats

Detail: [upstream-products.md](sensor-research/upstream-products.md).

FIRMS points are extracts of NASA's standard fire products. These are the products behind them and the alternatives to them.

| Product | Sensor | What it is | Format | Starts | Where |
|---|---|---|---|---|---|
| MOD14, MYD14 (v061) | Terra, Aqua | Level 2 swath, 1 km, 5-minute granules; fire mask, quality bits and a fire pixel table | HDF4 | 24 Feb 2000; 4 Jul 2002 | LP DAAC |
| MOD14A1, MYD14A1 (v061) | Terra, Aqua | Daily 1 km grid on sinusoidal tiles: fire mask, maximum fire radiative power | HDF-EOS2 | 18 Feb 2000; 4 Jul 2002 | LP DAAC, Earth Engine |
| MOD14A2, MYD14A2 (v061) | Terra, Aqua | 8-day 1 km grid | HDF-EOS2 | Same | LP DAAC, Earth Engine |
| MOD14CMQ, MYD14CMQ | Terra, Aqua | Monthly 0.25° global grid with counts corrected for overpasses and cloud; static sources removed | HDF4 | Nov 2000; Jul 2002 | University of Maryland SFTP |
| MCD14ML (version 03) | Terra and Aqua | Monthly list of every fire pixel; the source of FIRMS standard MODIS data | Fixed-width text | Nov 2000 | University of Maryland SFTP |
| MCD14DL | Terra and Aqua | FIRMS near-real-time points | Text, shapefile, KML | Rolling | FIRMS |
| VNP14IMG, VJ114IMG, VJ214IMG (v002) | Suomi NPP, NOAA-20, NOAA-21 | Level 2 swath, 375 m, 6-minute granules | NetCDF-4 | 17 Jan 2012; 1 Jan 2018; 10 Feb 2023 | LP DAAC |
| VNP14IMGML, VJ114IMGML, VJ214IMGML (version 03) | Same | Monthly list of every 375 m fire pixel; the source of FIRMS standard VIIRS data | CSV | As above | University of Maryland SFTP |
| VNP14IMGTDL_NRT, VJ114IMGTDL_NRT, VJ214IMGTDL_NRT | Same | FIRMS near-real-time points | Text, shapefile, KML | Rolling | FIRMS |
| VNP14, VJ114, VJ214 (v002) | Same | Level 2 swath, 750 m, MODIS-style algorithm | NetCDF-4 | As the 375 m products | LP DAAC |
| VNP14A1, VJ114A1, VJ214A1 (v002) | Same | Daily 1 km grid built to match MOD14A1 | HDF-EOS5 | As above | LP DAAC |

- **Columns FIRMS drops.** The monthly VIIRS files carry fields that FIRMS CSVs lack: scan position (`Sample`), view angle, pixel area, solar angle, glint angle, background temperatures and M13 radiance. The monthly MODIS file carries `sample` (scan position, 0–1353) in place of scan and track.
- **Level 2 only.** Per-pixel quality bits, including the VIIRS residual overlap flag and the MODIS flag for which 4 µm band was used, exist only in the swath files.
- **Gridded MODIS-like VIIRS.** The VIIRS daily 1 km grids appear to be built from the 750 m product, not the 375 m one. This is inferred from their sample range.
- **Earth Engine.** `MODIS/061/MOD14A1`, `MODIS/061/MYD14A1`, `MODIS/061/MOD14A2`, `MODIS/061/MYD14A2` and `NASA/VIIRS/002/VNP14A1` are science-quality grids. `FIRMS`, `NASA/LANCE/SNPP_VIIRS/C2` and `NASA/LANCE/NOAA20_VIIRS/C2` are rasters of near-real-time points and are labelled not science quality. No Earth Engine dataset was found for NOAA-21 fire data.
- **Burned area is a different measurement.** MCD64A1 and VNP64A1 map which 500 m cells burned in a month and on which day, from surface change after the fire. Active-fire products count detections at overpass time.
- **University of Maryland server.** The monthly location files and gridded summaries are on `fuoco.geog.umd.edu` (SFTP), which needs its own login.

## Disagreements between sources

The cross-check found these places where primary sources disagree. Detail and the full list: [_cross-check.md](sensor-research/_cross-check.md).

| Item | Values found | Value used here | Why |
|---|---|---|---|
| NOAA-21 start in FIRMS | 1 Mar 2023 (archive download page); 17 Jan 2024 (FAQ) | Unresolved | Both pages said this on 13 Nov 2026. The likely reading, unconfirmed, is that near-real-time data start in January 2024 and the archive was later back-filled with standard data. The `version` column of 2023 rows would show which. |
| Suomi NPP end | 13:00 UTC and 15:40 UTC on 2 Nov 2026 | 15:40 UTC | 13:00 was the planned time; 15:40 is reported after the event. |
| Lag before standard data replace near-real-time | About 2 months; 2–3 months; about 5 months | Up to about 5 months | The archive download page, where the replacement happens, says 5. |
| NOAA-20 and NOAA-21 crossing time | About 12:40 (FIRMS FAQ); 13:25 (NOAA operations); 13:30 (programme name) | 13:25–13:30 | The FAQ figure confuses the along-orbit offset with local time. |
| VIIRS altitude | 824, 829, 830, 833, 840 km | 833 km operational, 824 km design | Different altitude definitions. |
| VIIRS swath | 3000, 3040, 3060 km | About 3060 km | The others are rounded. |
| VIIRS aggregation zone boundaries | 31.72° and 44.86°; 31.59° and 44.68° | Unresolved | No source defines the angle. The difference is under 0.2°. |
| Terra and Aqua end dates | Dec 2025 to Feb 2027 for Terra; Aug 2026 to Sep 2027 for Aqua | Feb 2027 and Sep 2027 | The newest NASA statement. Both were still operating on 13 Nov 2026. |
| Terra altitude drop in October 2022 | 5, 5.5, 6 and 11 km | About 5.5 km | The post-event calibration team paper. |
| MODIS band 21 noise | 2.00 K (LAADS); 0.20 K (MCST) | 0.20 K | The LAADS value is a decimal error. |
| VIIRS M13 saturation | 634 K; about 659 K | About 659 K for the product | 634 K is the design value. |
| VIIRS I4 saturation | 353 K, about 358 K, 367 K | 367 K in the data | Specification, onset of saturation, and the value assigned to saturated pixels. |
| VIIRS version strings | `1.0NRT`, `1.0` (attributes page); `2.0NRT`, `2` (files) | The file values | The page is out of date. |
| MODIS satellite code | `T`, `A` (documentation); `Terra`, `Aqua` (files) | The file values | Observed in FIRMS files. |
| MODIS standard version string | `6.1` (documentation); `6.2`, `6.03`, `61.03` (files) | Unresolved | Undocumented. |
| Night-time ratio of 375 m to 750 m detections | 25, 20 and 17 times | 17 times | The Collection 2 figure; the others are earlier versions. |

## What could not be established

- A table of observations per day by latitude for each sensor combination. Only anchor points are published.
- A measured history of Terra and Aqua crossing time and altitude for 2020–2026. Only plots and computed snapshots exist.
- The size of the effect of orbit drift on MODIS fire counts. NASA describes it as under investigation.
- Whether NOAA-21 rows for March 2023 to January 2024 in the FIRMS archive are standard data.
- Whether VIIRS fire radiative power for 2012–2015 in the Collection 2 archive uses M13.
- Brightness-temperature offsets between the three VIIRS units for I4 and I5, and whether NASA's fire code is identical across them.
- Which input version feeds the MODIS fire product after 30 September 2026, and whether a Collection 7 fire product will replace Collection 6.1.
- Firm end dates for Terra and Aqua data, and for MODIS in FIRMS.
- How much near-real-time and standard counts differ.
- Which outages FIRMS counts as missing data, beyond the three early Terra gaps.
- How the VIIRS `type` values for volcanoes and static sources are assigned.
- The lengths of several outages (listed as unknown in [Outages and gaps](#outages-and-gaps)).

## Principal sources

| Source | Covers |
|---|---|
| [MODIS Collection 6 and 6.1 Active Fire Product User's Guide](https://earthdata.nasa.gov/s3fs-public/2023-09/MODIS_C6_C6.1_Fire_User_Guide_1.0.pdf) (v1.0, May 2021) | MODIS products, formats, pixel geometry, known problems |
| [Giglio, Schroeder and Justice 2016](https://www.earthdata.nasa.gov/s3fs-public/imported/Giglio2016_C6_Fire.pdf) | MODIS Collection 6 algorithm and validation |
| [VIIRS Collection 2 375 m Active Fire Product User's Guide](https://www.earthdata.nasa.gov/s3fs-public/2025-06/VIIRS_C2_AF-375m_User_Guide_1.2.pdf) (v1.2, June 2025) | VIIRS 375 m product, formats, known issues |
| [Schroeder, Oliva, Giglio and Csiszar 2014](https://directreadout.sci.gsfc.nasa.gov/publications_documents/Schroeder_et_al_2014b_RSE.pdf) | VIIRS 375 m algorithm |
| [VIIRS 375 m algorithm document](https://viirsland.gsfc.nasa.gov/PDF/VIIRS_activefire_375m_ATBD.pdf) and [750 m algorithm document](https://viirsland.gsfc.nasa.gov/PDF/VIIRS_activefire_750m_ATBD.pdf) | Thresholds, fire radiative power, artifacts |
| [FIRMS FAQ](https://www.earthdata.nasa.gov/data/tools/firms/faq) | Availability, latency, interpretation |
| [FIRMS attributes page](https://www.earthdata.nasa.gov/data/tools/firms/active-fire-data-attributes-modis-viirs) | Column definitions |
| [FIRMS archive download](https://firms.modaps.eosdis.nasa.gov/download/) and [country file index](https://firms.modaps.eosdis.nasa.gov/data/country/yearly_summary_files.txt) | Archive coverage and open files |
| [Twedt et al. 2023](https://ntrs.nasa.gov/api/citations/20240001409/downloads/2023_SPIE_Twedt_MODIS_EV_orbit_drift_manuscript_v4.pdf) | Terra and Aqua orbit drift |
| [Giglio, LANCE user working group, May 2025](https://landweb.modaps.eosdis.nasa.gov/data/filePost/LANCE_UWG_Orbit_Drift_Giglio_202505.pdf) | Effects of drift on MODIS fire data |
| [NASA Science, "Terra: The End of an Era"](https://science.nasa.gov/science-research/earth-science/terra-the-end-of-an-era) | Terra and Aqua end dates |
| [NOAA OSPO JPSS status](https://www.ospo.noaa.gov/operations/jpss/status.html) and [NESDIS Suomi NPP notice](https://www.nesdis.noaa.gov/news/cessation-of-suomi-national-polar-orbiting-partnership-s-npp-data-users-onafter-november-2-2026) | VIIRS satellite orbits and status |
| [MCST](https://mcst.gsfc.nasa.gov/) weekly reports and calibration pages | MODIS instrument status and calibration |
| [Giglio, Csiszar and Justice 2006](https://dataserver-coids.inpe.br/queimadas/queimadas/Publicacoes-Impacto/material3os/2006_Giglio_etal_GlobalDistribuiton_JGR_DE3os.pdf) | Terra and Aqua sampling and the daily fire cycle |

The working files in [sensor-research/](sensor-research/) list every source used: about 265 distinct links.
