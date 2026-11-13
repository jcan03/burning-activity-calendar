# Suomi NPP, NOAA-20 and NOAA-21 platforms and orbits

Verified 2026-11-13. Status tags: [confirmed] means the linked page was opened and supports the statement; [corrected] means the researcher's value was wrong or imprecise and has been replaced (the old value is given under Conflicts); [unverified] means no opened page supports it.

Terms: **LTAN** is the local solar time at which the satellite crosses the equator heading north (ascending node). **S-NPP** is Suomi National Polar-orbiting Partnership. **JPSS** is the Joint Polar Satellite System; JPSS-1 became NOAA-20 and JPSS-2 became NOAA-21 once in orbit. **OSPO** is NOAA's Office of Satellite and Product Operations. **Primary / secondary / tertiary** are NOAA's operational priority roles (which satellite's products are prioritized and supported first).

## Key facts

### Launch, operations and design life

| Item | Suomi NPP | NOAA-20 (JPSS-1) | NOAA-21 (JPSS-2) |
|---|---|---|---|
| Launch date | 28 Oct 2011 ([LAADS VIIRS](https://ladsweb.modaps.eosdis.nasa.gov/missions-and-measurements/viirs/)) [confirmed] | 18 Nov 2017 ([LAADS VIIRS](https://ladsweb.modaps.eosdis.nasa.gov/missions-and-measurements/viirs/)) [confirmed] | 10 Nov 2022 ([NESDIS: NOAA-21 operational](https://www.nesdis.noaa.gov/news/noaa-21-operational); [WMO OSCAR NOAA-21](https://space.oscar.wmo.int/satellites/view/noaa_21)) [confirmed]. LAADS says 10 Nov 2021, which is wrong ([LAADS VIIRS](https://ladsweb.modaps.eosdis.nasa.gov/missions-and-measurements/viirs/)) |
| Launch time, vehicle, pad (secondary source) | 09:48:01.828 UTC, Delta II 7920-10C, Vandenberg SLC-2W ([Wikipedia: Suomi NPP](https://en.wikipedia.org/wiki/Suomi_NPP)) [confirmed, secondary] | 09:47:36 UTC, Delta II 7920-10C, Vandenberg SLC-2W ([Wikipedia: NOAA-20](https://en.wikipedia.org/wiki/NOAA-20)) [confirmed, secondary] | 09:49:00 UTC, Atlas V 401, Vandenberg SLC-3E ([Wikipedia: NOAA-21](https://en.wikipedia.org/wiki/NOAA-21)) [confirmed, secondary] |
| Commissioning / handover to NOAA operations | Commissioned March 2012; NOAA began using ATMS data 22 May 2012; operational control transitioned to NOAA, announced in an article last updated 4 Mar 2013 ([NOAA node 2295](https://noaa.gov/node/2295)) [confirmed] | Checkout ended mid-Feb 2018 and control passed to OSPO (search summary only) [unverified] | NASA handed operations to OSPO 30 Mar 2023 ([NESDIS handover](https://www.nesdis.noaa.gov/news/noaa-21-satellite-handover-celebrates-nasanoaa-operations-transition)); OSPO took over at 22:00 UTC 30 Mar 2023 ([OSPO 2023-04-03](https://ospo.noaa.gov/data/messages/2023/04/MSG_20230403_1614.html)) [confirmed] |
| "Operational" declaration | No single date; see row above [confirmed] | Declared operational "today" in a NESDIS article dated 31 May 2018 ([NESDIS: NOAA-20 operational](https://www.nesdis.noaa.gov/news/noaa-20-operational)); Wikipedia and a NESDIS 2018 review say 30 May 2018 ([Wikipedia: NOAA-20](https://en.wikipedia.org/wiki/NOAA-20)) [confirmed; 30 vs 31 May noted in Conflicts] | "Fully operational" announced 8 Nov 2023 after ten months of post-launch testing ([NESDIS: NOAA-21 operational](https://www.nesdis.noaa.gov/news/noaa-21-operational)) [confirmed] |
| Design life | 5 years on orbit, consumables for 7 ([Wikipedia: Suomi NPP](https://en.wikipedia.org/wiki/Suomi_NPP); [eoPortal Suomi NPP](https://eoportal.org/satellite-missions/suomi-npp)) [confirmed, secondary]. LAADS gives a generic 7-year VIIRS design life ([LAADS VIIRS](https://ladsweb.modaps.eosdis.nasa.gov/missions-and-measurements/viirs/)) [confirmed] | 7 years ([eoPortal JPSS-2](https://www.eoportal.org/satellite-missions/jpss-2)) [confirmed, secondary]; "JPSS satellites are designed to operate for seven years, with the potential for several more years" ([NESDIS: NOAA-21 primary](https://www.nesdis.noaa.gov/news/noaa-21-now-the-primary-satellite-the-jpss-fleet)) [confirmed] | At least 7 years ([eoPortal JPSS-2](https://www.eoportal.org/satellite-missions/jpss-2)) [confirmed, secondary]; WMO OSCAR end-of-life "≥2029" ([WMO OSCAR NOAA-21](https://space.oscar.wmo.int/satellites/view/noaa_21)) [confirmed] |
| First date in FIRMS 375 m archive | 20 Jan 2012 | 1 Apr 2018 | 1 Mar 2023 ([FIRMS download page](https://firms.modaps.eosdis.nasa.gov/download/)) [confirmed] |
| Last date in FIRMS 375 m archive | 2 Nov 2026 | present | present ([FIRMS download page](https://firms.modaps.eosdis.nasa.gov/download/)) [confirmed] |

### Orbit

All three satellites fly in the same orbital plane, a sun-synchronous polar orbit with an afternoon ascending node, and each crosses the equator 28 times a day (14 orbits) ([NESDIS handover](https://www.nesdis.noaa.gov/news/noaa-21-satellite-handover-celebrates-nasanoaa-operations-transition)) [confirmed].

| Parameter | Value and source | Status |
|---|---|---|
| Altitude, inclination, period, LTAN (NOAA operations page, last updated 5 Nov 2026) | S-NPP and NOAA-20 each: altitude 833 km, inclination 98.79°, period 101.44 min, LTAN 13:25:00; NOAA-21 not listed ([OSPO JPSS status](https://www.ospo.noaa.gov/operations/jpss/status.html)) | [confirmed] |
| Nominal design altitude / LTAN | JPSS designed as afternoon (1330 LTAN) sun-synchronous satellites at 824 km ([NASA NTRS JPSS paper](https://ntrs.nasa.gov/api/citations/20180001195/downloads/20180001195.pdf)) | [confirmed] |
| Programme orbit name | "Continuity of Weather Observations in 13:30 Local Time Ascending Node (LTAN)", all three plus JPSS-4 and JPSS-3 ([NOAA LEO Flyout Chart, July 2026](https://www.nesdis.noaa.gov/s3/2026-07/LEO-Flyout-Chart-2026_8_July.pdf)) | [confirmed] |
| NOAA-21 operational orbit as named by OSPO | "1325 PM ascending orbit" ([OSPO 2023-04-03](https://ospo.noaa.gov/data/messages/2023/04/MSG_20230403_1614.html)) | [confirmed] |
| WMO OSCAR | S-NPP 824 km, 13:25 ascending ([WMO OSCAR S-NPP](https://space.oscar.wmo.int/satellites/view/snpp)); NOAA-21 824 km, 13:30 ascending ([WMO OSCAR NOAA-21](https://space.oscar.wmo.int/satellites/view/noaa_21)) | [confirmed] |
| Generic VIIRS orbit (LAADS) | 830 km, 1:30 pm mean local solar time, 16-day repeat, 3000 km swath ([LAADS VIIRS](https://ladsweb.modaps.eosdis.nasa.gov/missions-and-measurements/viirs/)) | [confirmed] |
| Repeat cycle (primary) | ~1:30 PM ascending crossing with a 16-day repeat cycle ([VIIRS SDR User's Guide, NOAA TR NESDIS 142A, 2013](https://www.star.nesdis.noaa.gov/JPSS/documents/UserGuides/VIIRS_SDR_Users_Guide.pdf)); eoPortal adds "quasi 8-day" ([eoPortal Suomi NPP](https://eoportal.org/satellite-missions/suomi-npp)) | [confirmed] |
| VIIRS swath | 3060 km at nominal 829 km altitude, full daily coverage day and night ([VIIRS SDR User's Guide](https://www.star.nesdis.noaa.gov/JPSS/documents/UserGuides/VIIRS_SDR_Users_Guide.pdf)); LAADS rounds to 3000 km | [confirmed] |
| Secondary values (Wikipedia) | S-NPP perigee 833.7 km, apogee 834.3 km, 98.79°, 101.44 min; NOAA-20 perigee 824.3 km, apogee 833.0 km, 98.79°, 101.44 min; NOAA-21 833 km, 98.80°, 102.00 min (uncited) ([Wikipedia S-NPP](https://en.wikipedia.org/wiki/Suomi_NPP), [NOAA-20](https://en.wikipedia.org/wiki/NOAA-20), [NOAA-21](https://en.wikipedia.org/wiki/NOAA-21)) | [confirmed as what Wikipedia says; NOAA-21 period 102.00 min is inconsistent with the shared plane and 101.44 min of OSPO] |
| eoPortal values | S-NPP 824 km, 98.74°, 101 min, 16-day (quasi 8-day) repeat, "10:30 LTDN" ([eoPortal Suomi NPP](https://eoportal.org/satellite-missions/suomi-npp)); JPSS series 833 km, 98.75° ([eoPortal JPSS-2](https://www.eoportal.org/satellite-missions/jpss-2)) | [confirmed as stated; the 10:30 LTDN value is an error, see Conflicts] |

Note on latitude: in a sun-synchronous orbit the local overpass time is fixed only at the equator (13:25 to 13:30 ascending, about 01:25 to 01:30 descending). With a 3060 km swath the afternoon and night passes of one satellite overlap more and more toward the poles, so the number of looks per day rises with latitude: roughly one day and one night look near the equator, many more at high latitudes ([VIIRS SDR User's Guide](https://www.star.nesdis.noaa.gov/JPSS/documents/UserGuides/VIIRS_SDR_Users_Guide.pdf) gives the "global coverage with 12 hour revisit" statement; the latitude dependence is geometric reasoning, not quoted).

### Orbital phasing between the three satellites

One orbit is 101.44 min, so a half orbit is about 50.7 min and a quarter orbit about 25.4 min (arithmetic from the [OSPO JPSS status](https://www.ospo.noaa.gov/operations/jpss/status.html) period).

| Period | Arrangement | Source | Status |
|---|---|---|---|
| 2018 to Nov 2022 (two satellites) | NOAA-20 raised into "a half-orbit position relative to" S-NPP; primary and secondary "~50 minutes apart" | [NASA SVS 4613, JPSS ConOps constellation management](https://svs.gsfc.nasa.gov/4613) | [confirmed] |
| Planned three-satellite arrangement (stated 2018, 2022) | Primary and secondary ~50 min (half orbit) apart; tertiary about a quarter orbit between them. NESDIS (21 Nov 2022): NOAA-21 will fly "roughly 50 minutes, or half an orbit, ahead of NOAA-20"; S-NPP "will orbit between the two, about 25 minutes away from each" | [NASA SVS 4613](https://svs.gsfc.nasa.gov/4613); [NESDIS: JPSS-2 has a new name](https://www.nesdis.noaa.gov/node/10876) | [confirmed] |
| NASA SVS 5021 description | NOAA-21 placed "a quarter orbit ahead of Suomi-NPP"; NOAA-20 a quarter orbit behind (one passage says it moves ahead) S-NPP, notionally a year after NOAA-21 launch; page is internally inconsistent | [NASA SVS 5021](https://svs.gsfc.nasa.gov/5021) | [corrected: the page gives no minute values and contradicts itself] |
| Nov 2022 to 20 Mar 2024 | NOAA-21 a quarter orbit ahead of S-NPP while NOAA-20 still sat half an orbit from S-NPP; so NOAA-21 and NOAA-20 were not yet 180° apart. This is inferred from the above plus the rephasing notice; no page states the interim spacing in minutes | inference from [SVS 5021](https://svs.gsfc.nasa.gov/5021), [SVS 4613](https://svs.gsfc.nasa.gov/4613), [OSPO rephasing notice](https://www.ospo.noaa.gov/data/messages/2024/04/MSG_20240404_1604.html) | [unverified] |
| Rephasing, 20 Mar to 4 Apr 2024 | First burn 20 Mar 2024 17:20:45 to 17:23:56 UTC; NOAA-20 drifted at lower altitude (about 14 to 15 days per OSPO, about 16 days per Earthdata) to reach 180° separation from NOAA-21; final burn 4 Apr 2024 11:56:00 to 11:57:50 UTC "to complete the rephasing campaign" | [OSPO 2024-04-04](https://www.ospo.noaa.gov/data/messages/2024/04/MSG_20240404_1604.html); [Earthdata rephasing alert](https://earthdata.nasa.gov/data/alerts-outages/noaa-20-rephasing-campaign-scheduled-march-20-april-4-2024) | [confirmed] |
| From 4 Apr 2024 | NOAA-20 180° (half orbit, ~50 min) from NOAA-21, S-NPP between them about 25 min from each (until its data ended 2 Nov 2026) | Plan in [NESDIS node 10876](https://www.nesdis.noaa.gov/node/10876) plus the 180° target in [Earthdata rephasing alert](https://earthdata.nasa.gov/data/alerts-outages/noaa-20-rephasing-campaign-scheduled-march-20-april-4-2024). The CIRA blog that states it returned HTTP 403 | [confirmed for the 180° and plan; actual achieved spacing not stated on an opened page] |
| NASA blog statement | "The three satellites fly approximately 50 minutes apart" and an overpass "of approximately 1:30 p.m., Universal Coordinated Time (UTC)"; names NOAA-21 primary, "NOAA-22" secondary, S-NPP tertiary (dated 1 Nov 2024) | [Earthdata: From MODIS to VIIRS](https://earthdata.nasa.gov/news/blog/from-modis-viirs-continuing-legacy) | [confirmed as stated; contains three errors, see Conflicts] |

### Operational priority roles

| Effective date | Primary | Secondary | Tertiary | Source | Status |
|---|---|---|---|---|---|
| 30 Mar 2023 22:00 UTC | NOAA-20 | S-NPP | NOAA-21 | [OSPO 2023-04-03](https://ospo.noaa.gov/data/messages/2023/04/MSG_20230403_1614.html) | [confirmed] |
| 3 Nov 2023 00:00 UTC (notice 9 Nov 2023) | NOAA-20 | NOAA-21 | S-NPP | [OSPO 2023-11-09](https://www.ospo.noaa.gov/data/messages/2023/11/MSG_20231109_1630.html) | [confirmed] |
| 20 Mar 2024 12:00 UTC (notice 12 Mar 2024) | NOAA-21 | NOAA-20 | S-NPP (non-nominal issues handled best-effort in business hours) | [OSPO 2024-03-12](https://www.ospo.noaa.gov/data/messages/2024/03/MSG_20240312_1430.html) | [confirmed] |
| 2 Nov 2026 | NOAA-21 | NOAA-20 | none (S-NPP data ended) | [NESDIS cessation notice](https://www.nesdis.noaa.gov/news/cessation-of-suomi-national-polar-orbiting-partnership-s-npp-data-users-onafter-november-2-2026) | [confirmed] |

### Anomalies, safe modes and data gaps affecting VIIRS

| Satellite | Dates (UTC) | What happened | Source | Status |
|---|---|---|---|---|
| S-NPP | 26 Jul to 20 Aug 2022 | Spacecraft non-nominal at ~16:24:49 UTC 26 Jul 2022, all instruments safe mode; VIIRS land processing resumed 20 Aug 2022; data 26 Jul to 20 Aug "will not be recoverable"; NOAA approved VIIRS products for operations 29 Aug 2022 | [Earthdata: S-NPP recovers](https://www.earthdata.nasa.gov/data/alerts-outages/suomi-npp-recovers-from-safe-mode); start time from [CoastWatch](https://coastwatch.noaa.gov/cwn/news/2022-07-28/s-nppviirs-instrument-safe-mode.html) (not re-opened by verifier) | [confirmed; start time as reported by researcher] |
| S-NPP | early mission | NIR throughput loss traced to tungsten oxide on VIIRS rotating telescope mirrors | [Wikipedia: Suomi NPP](https://en.wikipedia.org/wiki/Suomi_NPP) | [confirmed, secondary] |
| S-NPP | 25 May 2024 (+11 days), Sep 2024, Nov 2024 | GPS anomalies degraded VIIRS geolocation; OSPO lists S-NPP GPS status Yellow in Nov 2026 | [Wikipedia: Suomi NPP](https://en.wikipedia.org/wiki/Suomi_NPP); [OSPO JPSS status](https://www.ospo.noaa.gov/operations/jpss/status.html) | [confirmed, secondary for dates] |
| S-NPP CrIS (not VIIRS) | 12 Jul 2021 MWIR loss; 23 Dec 2025 scan mirror failure | NOAA: "End of Operational Use occurred on December 23, 2025"; Wikipedia: recovery suspended 11 Feb 2026 | [NESDIS cessation notice](https://www.nesdis.noaa.gov/news/cessation-of-suomi-national-polar-orbiting-partnership-s-npp-data-users-onafter-november-2-2026); [Wikipedia](https://en.wikipedia.org/wiki/Suomi_NPP) | [confirmed] |
| NOAA-21 | Nov 2022 to 2 Feb 2023 | Solar array deployment problem after launch; Ka-band transmitter failure weeks later, backup Ka initialized 2 Feb 2023 | [Wikipedia: NOAA-21](https://en.wikipedia.org/wiki/NOAA-21) | [confirmed, secondary] (before FIRMS NOAA-21 start of 1 Mar 2023) |
| NOAA-20 | 3 Feb 2024 18:00 to 4 Feb 2024 15:57:19 | Second spacecraft command processor reset, all instruments safe; stored mission data unrecoverable; Mission Point Mode 04:12:52 on 4 Feb; VIIRS operational 15:57:19 on 4 Feb; VIIRS SDR/EDR re-enabled for users 9 Feb 16:30 | [OSPO 2024-02-20](https://ospo.noaa.gov/data/messages/2024/02/MSG_20240220_2351.html) | [confirmed] |
| NOAA-20 | 20 Feb 2024 ~14:00 to 21:10 | VIIRS command processor reset; about 8 to 10 h of VIIRS data lost | [OSPO 2024-02-20](https://ospo.noaa.gov/data/messages/2024/02/MSG_20240220_2351.html) | [confirmed; added] |
| NOAA-20 | 20 Mar to 4 Apr 2024 | Rephasing drift: L1 VIIRS held until evaluated, missing granules and degradation expected, all LP DAAC NOAA-20 VIIRS land products affected incl. VJ114IMG-type 375 m active fire, 750 m fire and daily 1 km fire | [Earthdata rephasing alert](https://earthdata.nasa.gov/data/alerts-outages/noaa-20-rephasing-campaign-scheduled-march-20-april-4-2024) | [confirmed] |
| NOAA-21 | 22 Jun 2024 04:24 to 09:33:57 | Anomaly put spacecraft in earthpoint, all instruments safe; Mission Pointing 07:49:52; VIIRS operational 09:33:57 (researcher had no start time; it is 04:24) | [OSPO 2024-06-22](https://ospo.noaa.gov/data/messages/2024/06/MSG_20240622_2205.html) | [corrected] |
| NOAA-21 | 18 Sep 2025 04:31 | VIIRS instrument problem, data lost on rev 14796; recovery update the same day | [OSPO 2025-09-18](https://ospo.noaa.gov/data/messages/2025/09/MSG_20250918_0527.html) | [confirmed] |
| NOAA-21 | 1 Oct 2025 19:09:10 | VIIRS instrument safe mode, data lost on rev 14989 (Fairbanks); recovery scheduled rev 14990 (20:43:53 to 20:55:40) | [OSPO 2025-10-01](https://ospo.noaa.gov/data/messages/2025/10/MSG_20251001_2050.html) | [confirmed] |
| NOAA-21 | 28 Jul 2026 05:42 to 29 Jul 2026 18:20:50 | Good M14 to M16 and I5 longwave IR data flagged poor quality; downstream products had no retrievals for 36 h 38 min; VIIRS data missed during the recovery are unrecoverable | [OSPO 2026-07-29](https://ospo.noaa.gov/data/messages/2026/07/MSG_20260729_1947.html) | [corrected: researcher omitted the 05:42 UTC 28 Jul start and duration] |
| NOAA-20 and NOAA-21 | 5 to 7 Nov 2026 | VIIRS data gaps on 5 and 6 Nov (both) and 7 Nov (NOAA-20); issued 9 Nov 2026, updated 10 Nov 2026; resolution TBD; no cause given | [Earthdata alert](https://www.earthdata.nasa.gov/data/alerts-outages/jpss1-noaa-20-jpss2-noaa-21-viirs-data-gaps-processing-delays-from-november-5) | [confirmed] |

### End of Suomi NPP data (2 November 2026)

- NOAA notice issued 3 Aug 2026 16:00 UTC: all S-NPP data (ATMS, CERES, OMPS Nadir and Limb, VIIRS) end at 13:00 UTC (8:00 AM EST) on 2 Nov 2026, HRD Direct Broadcast disabled, "Length of Outage: Permanent"; no reason given; users told to move to NOAA-21 (primary) and NOAA-20 (secondary) ([NESDIS cessation notice](https://www.nesdis.noaa.gov/news/cessation-of-suomi-national-polar-orbiting-partnership-s-npp-data-users-onafter-november-2-2026)) [confirmed].
- The same notice now lists Update #3 (30 Oct 2026 14:00 UTC) and Update #4 (2 Nov 2026 18:00 UTC), whose titles give the cessation as 2 Nov 2026 15:40 UTC and mention "Decommissioning"; the update texts are not on the page ([NESDIS cessation notice](https://www.nesdis.noaa.gov/news/cessation-of-suomi-national-polar-orbiting-partnership-s-npp-data-users-onafter-november-2-2026)) [confirmed].
- NASA LANCE: "Delivery of new science data from the Suomi NPP satellite ceased at 15:40 Universal Time (UTC) on November 2, 2026" (day 306) ([Earthdata LANCE transition blog](https://www.earthdata.nasa.gov/news/blog/transitioning-from-suomi-npp-noaa-20-noaa-21-what-lance-users-need-know)); same time on the [Earthdata S-NPP transition resources page](https://www.earthdata.nasa.gov/data/platforms/space-based-platforms/suomi-npp/transition-resources) [confirmed].
- The historical archive "will remain available" ([Earthdata transition resources](https://www.earthdata.nasa.gov/data/platforms/space-based-platforms/suomi-npp/transition-resources)) [confirmed]. The cessation is permanent ([NESDIS cessation notice](https://www.nesdis.noaa.gov/news/cessation-of-suomi-national-polar-orbiting-partnership-s-npp-data-users-onafter-november-2-2026)) [confirmed].
- NASA LDOPE land issue 1479, "SNPP Decommission 11/02/2026" (3 Aug 2026, updated 7 Oct 2026): SNPP L1B and "all downstream products" affected ([LDOPE issue 1479](https://landweb.modaps.eosdis.nasa.gov/displayissue?id=1479)) [confirmed; added].
- NOAA July 2026 flyout chart marks S-NPP "Tentatively scheduled for decommissioning and deorbiting" and shows it as on-orbit tertiary (non-operational) ending around late calendar 2026 ([NOAA LEO Flyout Chart](https://www.nesdis.noaa.gov/s3/2026-07/LEO-Flyout-Chart-2026_8_July.pdf)) [confirmed].
- Wikipedia: decommissioned 2 Nov 2026, deorbit "December 2026 (planned)" ([Wikipedia: Suomi NPP](https://en.wikipedia.org/wiki/Suomi_NPP)) [unverified: no primary source for the deorbit date]. WMO OSCAR lists S-NPP "Inactive", end-of-life 1 Nov 2026, and a note "Satellite retired on 1st Sept 2026" ([WMO OSCAR S-NPP](https://space.oscar.wmo.int/satellites/view/snpp)) [confirmed as stated; the 1 Sep date conflicts with all NOAA sources].
- OSPO's JPSS status page (updated 5 Nov 2026) still lists S-NPP with CrIS red, GPS yellow, others green, and no decommissioning text ([OSPO JPSS status](https://www.ospo.noaa.gov/operations/jpss/status.html)) [confirmed].
- Product naming for the switch: VNP prefix (S-NPP) becomes VJ1 (NOAA-20) or VJ2 (NOAA-21), e.g. VNP14IMG to VJ114IMG / VJ214IMG; file structure, CRS and HDF-EOS5/NetCDF-4 formats "remain largely consistent" ([Earthdata LANCE transition blog](https://www.earthdata.nasa.gov/news/blog/transitioning-from-suomi-npp-noaa-20-noaa-21-what-lance-users-need-know)) [confirmed].

### Status as of 13 November 2026

| Satellite | Status | Source | Status tag |
|---|---|---|---|
| Suomi NPP | No new data since 2 Nov 2026 15:40 UTC; decommissioning per NOAA update titles; deorbit tentative | see section above | [confirmed] |
| NOAA-20 | Secondary, all instruments green (OSPO page labels inconsistent between tables); VIIRS gaps 5 to 7 Nov 2026 | [OSPO JPSS status](https://www.ospo.noaa.gov/operations/jpss/status.html); [Earthdata alert](https://www.earthdata.nasa.gov/data/alerts-outages/jpss1-noaa-20-jpss2-noaa-21-viirs-data-gaps-processing-delays-from-november-5) | [confirmed] |
| NOAA-21 | Primary, all instruments green; VIIRS gaps 5 to 6 Nov 2026 | same | [confirmed] |

### Follow-on missions and VIIRS continuity

| Item | Value | Source | Status |
|---|---|---|---|
| Next launch | JPSS-4 (to be named NOAA-22), launch readiness 2027, carries ATMS, CrIS, VIIRS, OMPS plus Libera | [NESDIS JPSS page](https://www.nesdis.noaa.gov/our-satellites/currently-flying/joint-polar-satellite-system) | [confirmed] |
| JPSS-4 planned launch date | 1 Sep 2027 | [NOAA LEO update, CSPP Users' Conference, May 2026 (Zhou et al.)](https://www.ssec.wisc.edu/meetings/wp-content/uploads/sites/33/2026/06/2.5_Zhou.pdf) | [confirmed] |
| JPSS-3 | In long-term storage, planned launch "late in 2032" (so JPSS-4 flies before JPSS-3) | same | [confirmed] |
| JPSS-4 VIIRS change | Scan rate raised from 3.510 to 3.546 rad/s to correct scan-to-scan underlaps seen on JPSS-1 and JPSS-2 VIIRS | same | [confirmed] |
| Successor programme | NEON Series-1 notional first launch in the mid-2030s | same | [confirmed; added] |
| Mission-life projections (read from chart graphics, approximate) | NOAA-20: green (operational) to about end of 2029, then rising failure-risk bands to about 2033. NOAA-21: green to about 2028, risk bands to about 2032. JPSS-4: checkout late 2027, planned life to about 2035. JPSS-3: checkout about 2033, planned life to about 2038, then "End of PFO Program of Record (POR), no funding" around 2039. Estimates based on July 2025 reliability analyses | [NOAA LEO Flyout Chart, July 2026](https://www.nesdis.noaa.gov/s3/2026-07/LEO-Flyout-Chart-2026_8_July.pdf) (rendered and read by eye) | [confirmed for labels; years approximate to about half a year] |
| Continuity "through 2038" | Claimed from MDPI Remote Sensing 17(13):2146 (2025); page returned HTTP 403 | [MDPI](https://www.mdpi.com/2072-4292/17/13/2146) | [unverified]; consistent with the flyout chart's JPSS-3 bar ending about 2038 |

## Why these matter for combining the records

All three VIIRS instruments sample the same ~13:25 to 13:30 ascending and ~01:30 descending local times in the same plane, so they see the same part of the fire diurnal cycle as Aqua MODIS; differences between them are along-track timing (about 25 or 50 minutes apart), not local time of day. The number of VIIRS satellites contributing to a monthly count changes over time: one (S-NPP) from January 2012, two from April 2018 (FIRMS NOAA-20 start), three from March 2023 (FIRMS NOAA-21 start), and two again after 2 November 2026 15:40 UTC; each change alters how many overpasses, and therefore detections, a month can contain. The spacing between satellites changed in April 2024, which changes how often the same fire is seen twice within an hour. Known outages (S-NPP 26 Jul to 20 Aug 2022, NOAA-20 3 to 4 Feb and 20 Mar to 4 Apr 2024, NOAA-21 22 Jun 2024 and 28 to 29 Jul 2026, NOAA-20 and NOAA-21 5 to 7 Nov 2026) remove part of a month's observations. The S-NPP record is now closed at 2 Nov 2026, and the remaining VIIRS satellites carry projected end-of-life dates in the 2030s, with JPSS-4 (2027) and JPSS-3 (2032) planned to continue the same orbit.

## Conflicts and unverified items

1. **NOAA-21 launch year.** LAADS says 10 Nov 2021 ([LAADS VIIRS](https://ladsweb.modaps.eosdis.nasa.gov/missions-and-measurements/viirs/)); NESDIS ([NOAA-21 operational](https://www.nesdis.noaa.gov/news/noaa-21-operational)), WMO OSCAR and eoPortal say 10 Nov 2022. 2022 is correct; LAADS has a typo.
2. **NOAA-21 "operational" date.** OSPO took over operations on 30 Mar 2023 22:00 UTC ([OSPO 2023-04-03](https://ospo.noaa.gov/data/messages/2023/04/MSG_20230403_1614.html)); NESDIS announced "fully operational" on 8 Nov 2023 ([NESDIS](https://www.nesdis.noaa.gov/news/noaa-21-operational)). Both are primary NOAA sources describing different milestones (handover vs full operational status). The researcher's framing of Wikipedia vs OSPO is corrected: 8 Nov 2023 is also a NOAA statement.
3. **NOAA-20 operational date.** NESDIS article dated 31 May 2018 says "declared operational today" ([NESDIS](https://www.nesdis.noaa.gov/news/noaa-20-operational)); Wikipedia and a NESDIS 2018 review (search summary only) say 30 May 2018. Difference may be timezone/publication lag.
4. **S-NPP cessation time.** 13:00 UTC 2 Nov 2026 in the original NOAA notice (3 Aug 2026) and NASA alert ([Earthdata alert](https://www.earthdata.nasa.gov/data/alerts-outages/suomi-npp-observations-cease-november-2-2026), last updated 14 Oct 2026) versus 15:40 UTC in NOAA Updates #3/#4 titles and NASA LANCE ([LANCE blog](https://www.earthdata.nasa.gov/news/blog/transitioning-from-suomi-npp-noaa-20-noaa-21-what-lance-users-need-know)). 15:40 UTC is the later, final value. An earlier NESDIS URL and LDOPE used 1 Nov / day 305; Wikipedia says NOAA announced 1 Nov. WMO OSCAR's "retired on 1st Sept 2026" conflicts with all NOAA/NASA sources.
5. **S-NPP equator crossing.** eoPortal: 10:30 LTDN ([eoPortal](https://eoportal.org/satellite-missions/suomi-npp)). NOAA OSPO: LTAN 13:25:00 ([OSPO status](https://www.ospo.noaa.gov/operations/jpss/status.html)); NOAA chart: 13:30 LTAN; SDR User's Guide: ~1:30 PM ascending. The eoPortal value is an error (a 13:30 LTAN orbit descends at about 01:30).
6. **LTAN 13:25 vs 13:30.** OSPO operations (13:25:00), WMO OSCAR S-NPP (13:25) and OSPO's "1325 PM ascending orbit" vs programme name 13:30 (flyout chart, WMO NOAA-21, LAADS 1:30 pm). 13:25 is the operational value maintained by OSPO; 13:30 is the nominal programme label.
7. **Altitude.** 833 km (OSPO status, eoPortal JPSS, Wikipedia NOAA-21), 824 km (NTRS design, WMO OSCAR, eoPortal S-NPP, NOAA "512 miles"), 829 km (SDR guide nominal), 830 km (LAADS), perigee/apogee 824.3 to 834.3 km (Wikipedia). OSPO's current operational page (833 km) is most authoritative for present orbits; 824 km is the design value used in older documents.
8. **Inclination and period.** 98.79° and 101.44 min (OSPO for S-NPP and NOAA-20, Wikipedia); 98.80° and 102.00 min (Wikipedia NOAA-21, uncited); 98.75° (eoPortal JPSS); 98.74° (eoPortal S-NPP). OSPO is authoritative; NOAA-21 values not found on a primary page.
9. **NASA "From MODIS to VIIRS" blog (1 Nov 2024).** Says 1:30 p.m. "UTC" (should be local solar time), "NOAA-22" secondary (should be NOAA-20) and all three "approximately 50 minutes apart" (after April 2024 the primary and secondary are ~50 min apart with S-NPP ~25 min from each, per [NESDIS node 10876](https://www.nesdis.noaa.gov/node/10876)).
10. **NASA SVS 5021** says both that NOAA-20 will move "a quarter orbit ahead of S-NPP" and that it "will be a quarter orbit behind SNPP"; NESDIS node 10876 and the 180° rephasing target imply NOAA-20 is a quarter orbit from S-NPP on the opposite side from NOAA-21.
11. **Rephasing drift length.** About 16 days ([Earthdata](https://earthdata.nasa.gov/data/alerts-outages/noaa-20-rephasing-campaign-scheduled-march-20-april-4-2024)) vs 14 to 15 days ([OSPO](https://www.ospo.noaa.gov/data/messages/2024/04/MSG_20240404_1604.html)); burn dates 20 Mar and 4 Apr 2024 agree.
12. **S-NPP CrIS end of use.** 23 Dec 2025 (NOAA notice) vs 11 Feb 2026 (Wikipedia, recovery operations suspended). NOAA is authoritative for "end of operational use".
13. **JPSS-3 and JPSS-4 order and dates.** Older NOAA budget material (researcher, not re-opened) gave JPSS-3 earlier than JPSS-4; May 2026 NOAA slide gives JPSS-4 1 Sep 2027 then JPSS-3 late 2032. The 2026 NOAA slide is current. [old values unverified]
14. **Unverified:** S-NPP operational control date 22 Feb 2013 (search summary only); S-NPP deorbit in December 2026 (Wikipedia only); CIRA statement of achieved post-2024 spacing (HTTP 403); MDPI "continuity through 2038" (HTTP 403); exact interim NOAA-20 to NOAA-21 spacing Nov 2022 to Mar 2024; CoastWatch S-NPP safe mode start time (cited by researcher, not re-opened).

## Open questions

- The text of NOAA Updates #3 and #4 to the S-NPP cessation notice (decommissioning steps, passivation, deorbit plan and date) is not on any opened page.
- No source states why NOAA ended S-NPP delivery (age, CrIS loss, GPS problems, cost or planned retirement); the flyout chart footnote folds S-NPP costs into Polar Follow On.
- No primary page gives NOAA-21's current altitude, inclination and period (OSPO status table leaves NOAA-21 blank).
- Whether the S-NPP equator crossing time drifted in its final years (inclination maneuvers stopped?) was not found.
- Cause and resolution of the 5 to 7 Nov 2026 NOAA-20/NOAA-21 VIIRS gaps (alert still TBD as of 10 Nov 2026), and whether gaps will be filled in FIRMS archive data.
- Whether FIRMS's 1 Apr 2018 (NOAA-20) and 1 Mar 2023 (NOAA-21) archive start dates reflect product maturity or data availability; the reason is not stated on the download page.
- Exact end years on the July 2026 flyout chart are graphical only; a tabular source was not found.

## Sources

- NOAA NESDIS, Cessation of S-NPP data to users on/after November 2, 2026: https://www.nesdis.noaa.gov/news/cessation-of-suomi-national-polar-orbiting-partnership-s-npp-data-users-onafter-november-2-2026
- NOAA NESDIS, same notice at older "november-01" URL: https://www.nesdis.noaa.gov/news/cessation-of-suomi-national-polar-orbiting-partnership-s-npp-data-users-onafter-november-01-2026
- NASA Earthdata, Transitioning from Suomi NPP to NOAA-20/NOAA-21: what LANCE users need to know: https://www.earthdata.nasa.gov/news/blog/transitioning-from-suomi-npp-noaa-20-noaa-21-what-lance-users-need-know
- NASA Earthdata, Suomi NPP transition resources: https://www.earthdata.nasa.gov/data/platforms/space-based-platforms/suomi-npp/transition-resources
- NASA Earthdata alert, Suomi NPP observations to cease November 2, 2026: https://www.earthdata.nasa.gov/data/alerts-outages/suomi-npp-observations-cease-november-2-2026
- NASA LDOPE issue 1479, SNPP Decommission 11/02/2026: https://landweb.modaps.eosdis.nasa.gov/displayissue?id=1479
- NASA FIRMS archive download: https://firms.modaps.eosdis.nasa.gov/download/
- NOAA OSPO JPSS status: https://www.ospo.noaa.gov/operations/jpss/status.html
- NOAA OSPO message 2023-04-03 (NOAA-21 operational declaration): https://ospo.noaa.gov/data/messages/2023/04/MSG_20230403_1614.html
- NOAA OSPO message 2023-11-09 (NOAA-21 secondary): https://www.ospo.noaa.gov/data/messages/2023/11/MSG_20231109_1630.html
- NOAA OSPO message 2024-03-12 (NOAA-21 primary): https://www.ospo.noaa.gov/data/messages/2024/03/MSG_20240312_1430.html
- NOAA OSPO message 2024-04-04 (NOAA-20 rephasing burns): https://www.ospo.noaa.gov/data/messages/2024/04/MSG_20240404_1604.html
- NOAA OSPO message 2024-02-20 (NOAA-20 SCP reset): https://ospo.noaa.gov/data/messages/2024/02/MSG_20240220_2351.html
- NOAA OSPO message 2024-06-22 (NOAA-21 safe mode): https://ospo.noaa.gov/data/messages/2024/06/MSG_20240622_2205.html
- NOAA OSPO message 2025-09-18 (NOAA-21 VIIRS outage): https://ospo.noaa.gov/data/messages/2025/09/MSG_20250918_0527.html
- NOAA OSPO message 2025-10-01 (NOAA-21 VIIRS safe mode): https://ospo.noaa.gov/data/messages/2025/10/MSG_20251001_2050.html
- NOAA OSPO message 2026-07-29 (NOAA-21 VIIRS LWIR recovery): https://ospo.noaa.gov/data/messages/2026/07/MSG_20260729_1947.html
- NASA Earthdata alert, NOAA-20 rephasing campaign 20 Mar to 4 Apr 2024: https://earthdata.nasa.gov/data/alerts-outages/noaa-20-rephasing-campaign-scheduled-march-20-april-4-2024
- NASA Earthdata alert, Suomi NPP recovers from safe mode: https://www.earthdata.nasa.gov/data/alerts-outages/suomi-npp-recovers-from-safe-mode
- NASA Earthdata alert, NOAA-20 and NOAA-21 VIIRS data gaps from November 5: https://www.earthdata.nasa.gov/data/alerts-outages/jpss1-noaa-20-jpss2-noaa-21-viirs-data-gaps-processing-delays-from-november-5
- NOAA CoastWatch, S-NPP/VIIRS instrument in safe mode (researcher source, not re-opened): https://coastwatch.noaa.gov/cwn/news/2022-07-28/s-nppviirs-instrument-safe-mode.html
- NOAA, Operational control of Suomi NPP (4 Mar 2013): https://noaa.gov/node/2295
- NESDIS, NOAA-20 operational (31 May 2018): https://www.nesdis.noaa.gov/news/noaa-20-operational
- NESDIS, NOAA-21 operational (8 Nov 2023): https://www.nesdis.noaa.gov/news/noaa-21-operational
- NESDIS, NOAA-21 handover: https://www.nesdis.noaa.gov/news/noaa-21-satellite-handover-celebrates-nasanoaa-operations-transition
- NESDIS, JPSS-2 has a new name: NOAA-21 (21 Nov 2022): https://www.nesdis.noaa.gov/node/10876
- NESDIS, NOAA-21 now the primary satellite in the JPSS fleet: https://www.nesdis.noaa.gov/news/noaa-21-now-the-primary-satellite-the-jpss-fleet
- NESDIS, Joint Polar Satellite System: https://www.nesdis.noaa.gov/our-satellites/currently-flying/joint-polar-satellite-system
- NOAA LEO Flyout Chart, as of July 2026: https://www.nesdis.noaa.gov/s3/2026-07/LEO-Flyout-Chart-2026_8_July.pdf
- Zhou, Kalluri, Yienger, LEO Program Data Update for CSPP Users, CSPP User Conference May 2026: https://www.ssec.wisc.edu/meetings/wp-content/uploads/sites/33/2026/06/2.5_Zhou.pdf
- NASA SVS 4613, JPSS Concept of Operations: Constellation Management: https://svs.gsfc.nasa.gov/4613
- NASA SVS 5021, NOAA-21, NOAA-20 and Suomi NPP satellite orbits: https://svs.gsfc.nasa.gov/5021
- NASA Earthdata, From MODIS to VIIRS: continuing the legacy (1 Nov 2024): https://earthdata.nasa.gov/news/blog/from-modis-viirs-continuing-legacy
- LAADS DAAC, VIIRS: https://ladsweb.modaps.eosdis.nasa.gov/missions-and-measurements/viirs/
- NOAA TR NESDIS 142A, VIIRS SDR User's Guide v1.2 (10 Sep 2013): https://www.star.nesdis.noaa.gov/JPSS/documents/UserGuides/VIIRS_SDR_Users_Guide.pdf
- Trenkle and Driggers, Joint Polar Satellite System (NASA NTRS 20180001195): https://ntrs.nasa.gov/api/citations/20180001195/downloads/20180001195.pdf
- WMO OSCAR, Suomi NPP: https://space.oscar.wmo.int/satellites/view/snpp
- WMO OSCAR, NOAA-21: https://space.oscar.wmo.int/satellites/view/noaa_21
- eoPortal, Suomi NPP (secondary): https://eoportal.org/satellite-missions/suomi-npp
- eoPortal, JPSS-2 (secondary): https://www.eoportal.org/satellite-missions/jpss-2
- Wikipedia, Suomi NPP (secondary): https://en.wikipedia.org/wiki/Suomi_NPP
- Wikipedia, NOAA-20 (secondary): https://en.wikipedia.org/wiki/NOAA-20
- Wikipedia, NOAA-21 (secondary): https://en.wikipedia.org/wiki/NOAA-21
- CIRA VISIT blog, NOAA-21 designated primary (HTTP 403, not opened): https://rammb2.cira.colostate.edu/visit-blog/2024/05/03/noaa-21-designated-as-the-primary-satellite-of-the-jpss-constellation
- MDPI Remote Sensing 17(13):2146 (HTTP 403, not opened): https://www.mdpi.com/2072-4292/17/13/2146
