# Terra and Aqua platforms, orbits, drift and end of life

Verified 2026-11-13. Terms used below:
- **MLT** (mean local time) of equator crossing: the local mean solar time when the satellite crosses the equator.
- **Descending node**: the equator crossing while the satellite moves north to south. **Ascending node**: south to north.
- **IAM** (inclination adjust maneuver): a burn that keeps the orbit plane fixed relative to the Sun, and so holds the MLT.
- **DMU** (drag make-up maneuver): a burn that restores altitude lost to drag, and so holds the repeating ground track.
- **CEM** (constellation exit maneuver): a retrograde burn that lowers the orbit out of the 705 km constellation.
- **PLM** (perigee lowering maneuver): an end-of-mission burn that lowers perigee before the spacecraft is switched off for good (passivation).

Status tags: [confirmed] means the linked page supports the fact. [corrected] means the researcher's value was wrong or incomplete and the linked page gives the value shown. [unverified] means the fact could not be confirmed on a primary page.

## Key facts

### Launch, first light and start of the record

| Item | Terra (EOS AM-1) | Aqua (EOS PM-1) | Source / status |
|---|---|---|---|
| Launch | Saturday 18 Dec 1999, 18:57 GMT | 4 May 2002, 09:55 GMT | [MCST](https://mcst.gsfc.nasa.gov/index.php/some-information-about-modis) [confirmed] |
| Launch site and vehicle | Vandenberg AFB, Atlas-Centaur IIAS | Vandenberg (from the Aqua at 20 article) | [NASA Terra end of era](https://science.nasa.gov/science-research/earth-science/terra-the-end-of-an-era), [Earthdata Aqua at 20](https://www.earthdata.nasa.gov/learn/articles/aqua-at-20) [confirmed] |
| MODIS first light (nadir aperture door opened) | 24 Feb 2000, on A-side electronics | 24 Jun 2002, 23:22:48 GMT, on B-side electronics | [MCST](https://mcst.gsfc.nasa.gov/index.php/some-information-about-modis) [confirmed] |
| Final operational orbit reached | 24 Feb 2000, after 11 weeks of checkout and 8 ascent maneuvers | not checked | [NASA Terra end of era](https://science.nasa.gov/science-research/earth-science/terra-the-end-of-an-era) [confirmed] |
| Start of the daily fire product (MOD14A1 / MYD14A1 v6.1) in the catalog | 18 Feb 2000 | 4 Jul 2002 | [MOD14A1 v061](https://www.earthdata.nasa.gov/data/catalog/lpcloud-mod14a1-061), [MYD14A1 v061](https://www.earthdata.nasa.gov/data/catalog/lpcloud-myd14a1-061) [confirmed; added by verifier] |
| Electronics side in Nov 2026 | MODIS on A-side, cross-strapped to Formatter B | MODIS on B-side | [MCST Terra weekly 2026/311-317](https://mcst.gsfc.nasa.gov/iot/am1weekly20263112026317), [MCST Aqua weekly 2026/311-317](https://mcst.gsfc.nasa.gov/iot/pm1weekly20263112026317) [confirmed] |

- The catalog start date for MOD14A1 (18 Feb 2000) is earlier than Terra MODIS first light (24 Feb 2000). This is probably the first day of the first 8-day compositing period, not the first observation. That explanation is the verifier's inference. [confirmed date; explanation unverified]
- Terra alone covers about 2 years 4 months (24 Feb 2000 to 4 Jul 2002) before Aqua adds afternoon observations. This is computed from the dates above. [confirmed]

### Design life versus years in service

| Satellite | Design life | Years in service at 2026-11-13 | Source / status |
|---|---|---|---|
| Terra | 6 years ("planned as a six-year mission") | about 26.9 years | [NASA Terra end of era](https://science.nasa.gov/science-research/earth-science/terra-the-end-of-an-era) [corrected: the researcher said no Terra figure was found; the page gives six years] |
| Aqua | 6 years ("The design life was six years") | about 24.5 years | [Earthdata Aqua at 20](https://www.earthdata.nasa.gov/learn/articles/aqua-at-20), [NASA Aqua mission page](https://science.nasa.gov/mission/aqua/) [confirmed] |
| MODIS instrument (both) | 6 years | as above | [LAADS MODIS page](https://ladsweb.modaps.eosdis.nasa.gov/missions-and-measurements/modis/) [confirmed; added] |

### Nominal orbit (the maintained orbit, before drift)

| Parameter | Terra | Aqua | Source / status |
|---|---|---|---|
| Altitude | 705 km | 705 km | [Terra About](https://terra.nasa.gov/About), [Earthdata MODIS](https://www.earthdata.nasa.gov/data/instruments/modis), [Aqua at 20](https://www.earthdata.nasa.gov/learn/articles/aqua-at-20) [confirmed] |
| Orbit type | sun-synchronous, near-polar, circular | same | [LAADS MODIS page](https://ladsweb.modaps.eosdis.nasa.gov/missions-and-measurements/modis/) [confirmed] |
| Inclination | 98.5° (Terra About; Earthdata MODIS) **or** 98.2° (Terra Mission Director, 2022) | 98.2° | [Terra About](https://terra.nasa.gov/About), [Terra Constellation Exit Review, 2022](https://ntrs.nasa.gov/api/citations/20220006147/downloads/2022_Mantzarias_presentation_final_EOS%20Terra%20Constellation%20Exit%20Review.pptx.pdf), [eoPortal Aqua](https://www.eoportal.org/satellite-missions/aqua) [conflict; see below] |
| Period | 99 min ("14 complete orbits per day") | 98.8 min | [Terra About](https://terra.nasa.gov/About) [confirmed]; [eoPortal Aqua](https://www.eoportal.org/satellite-missions/aqua) (secondary) [confirmed on secondary only] |
| Repeat cycle | 16 days, 233 orbits | 16 days, 233 orbits | [Terra About](https://terra.nasa.gov/About) (16 days); [eoPortal Aqua](https://www.eoportal.org/satellite-missions/aqua), [eoPortal Terra](https://www.eoportal.org/satellite-missions/terra) (233 orbits; secondary) [confirmed on secondary only for 233] |
| Equator crossing | 10:30 a.m., descending node (southbound) | 1:30 p.m., ascending node (northbound) | [LAADS MODIS page](https://ladsweb.modaps.eosdis.nasa.gov/missions-and-measurements/modis/), [Terra About](https://terra.nasa.gov/About), [Aqua at 20](https://www.earthdata.nasa.gov/learn/articles/aqua-at-20) [confirmed] |
| MODIS swath | 2330 km cross-track by 10 km along-track at nadir | same | [LAADS MODIS page](https://ladsweb.modaps.eosdis.nasa.gov/missions-and-measurements/modis/), [Aqua status Nov 2023](https://assets.science.nasa.gov/content/dam/science/missions/aqua/AquaStatus_November.pdf) [confirmed; added] |
| Global coverage | every 1 to 2 days | same | [Aqua status Nov 2023](https://assets.science.nasa.gov/content/dam/science/missions/aqua/AquaStatus_November.pdf) [confirmed; added] |

- Consistency check by the verifier: 233 orbits in 16 days is 14.5625 orbits per day, a period of 98.9 min. For a circular orbit at 705 km the computed period is 98.88 min, and the sun-synchronous inclination is 98.21°. "14 complete orbits per day" on the Terra page means 14 whole orbits plus a fraction, so it does not contradict 233 per 16 days. eoPortal's "16 orbits per day" for Terra is wrong. [computed]
- Maintenance before drift: IAMs were done about once a year and held MLT "stable to within a few minutes" (10:30 Terra, 13:30 Aqua). DMUs were done "typically once every month or two" and kept a ground track that repeated on "a roughly 16-day cycle to within ±20 km". [Twedt et al., SPIE 2023](https://ntrs.nasa.gov/api/citations/20240001409/downloads/2023_SPIE_Twedt_MODIS_EV_orbit_drift_manuscript_v4.pdf) [confirmed]. The researcher's note that IAMs averaged "about four per year" was not found on the Project Scientist page in this check. Twedt says "roughly yearly". [unverified; Twedt contradicts it]

### Historical MLT while orbits were maintained

| Satellite | Period | MLT range | Source / status |
|---|---|---|---|
| Terra | Feb 2000 to Feb 2002 | between 10:30 and 10:45 (Project Scientist: "10:45 am during the first two years") | [Terra status Aug 2022](https://terra.nasa.gov/wp-content/uploads/2022/09/ESMO_TerraWebStatus_20220908_v2.pdf), [Terra Project Scientist](https://terra.nasa.gov/about/terras-orbit-changes/terra-orbital-drift-information/a-message-from-the-project-scientist) [confirmed; refined] |
| Terra | Feb 2002 to early 2021 | between 10:28 and 10:32 (operational box ±1 min around 10:30:00) | [Terra status Aug 2022](https://terra.nasa.gov/wp-content/uploads/2022/09/ESMO_TerraWebStatus_20220908_v2.pdf), [Terra Exit Review 2022](https://ntrs.nasa.gov/api/citations/20220006147/downloads/2022_Mantzarias_presentation_final_EOS%20Terra%20Constellation%20Exit%20Review.pptx.pdf) [confirmed; added] |
| Aqua | May 2002 to early 2023 | always between 13:30 and 13:45 (northbound) | [Aqua status Nov 2023](https://assets.science.nasa.gov/content/dam/science/missions/aqua/AquaStatus_November.pdf) [confirmed] |

### End of orbit maintenance, constellation exit and drift

| Event | Terra | Aqua | Source / status |
|---|---|---|---|
| Last IAM | 27 Feb 2020 (IAM 58; IAM 57 was 20 Feb 2020) | 18 Mar 2021 | [Twedt Table 1](https://ntrs.nasa.gov/api/citations/20240001409/downloads/2023_SPIE_Twedt_MODIS_EV_orbit_drift_manuscript_v4.pdf), [Terra Exit Review](https://ntrs.nasa.gov/api/citations/20220006147/downloads/2022_Mantzarias_presentation_final_EOS%20Terra%20Constellation%20Exit%20Review.pptx.pdf), [Aqua status Nov 2023](https://assets.science.nasa.gov/content/dam/science/missions/aqua/AquaStatus_November.pdf) [confirmed] |
| Last DMU | 28 Jul 2022 | 1 Dec 2021 | [Twedt Table 1](https://ntrs.nasa.gov/api/citations/20240001409/downloads/2023_SPIE_Twedt_MODIS_EV_orbit_drift_manuscript_v4.pdf), [NASA Aqua page](https://science.nasa.gov/mission/aqua/) ("December 2021") [confirmed] |
| Left the operational MLT box | Terra left ±1 min of 10:30 in March 2021 (actual; predicted April 2021) | Aqua passed its 13:45 science upper limit in Feb 2023 | [Terra Exit Review](https://ntrs.nasa.gov/api/citations/20220006147/downloads/2022_Mantzarias_presentation_final_EOS%20Terra%20Constellation%20Exit%20Review.pptx.pdf), [Terra Project Scientist](https://terra.nasa.gov/about/terras-orbit-changes/terra-orbital-drift-information/a-message-from-the-project-scientist), [Aqua status Nov 2023](https://assets.science.nasa.gov/content/dam/science/missions/aqua/AquaStatus_November.pdf) [confirmed] |
| Constellation exit | two retrograde CEMs on 12 Oct and 19 Oct 2022 (Morning Constellation) | free-drift, drag-down exit from the A-Train starting January 2022 (no exit burn) | [Twedt](https://ntrs.nasa.gov/api/citations/20240001409/downloads/2023_SPIE_Twedt_MODIS_EV_orbit_drift_manuscript_v4.pdf), [Earthdata Terra exit outage](https://www.earthdata.nasa.gov/data/alerts-outages/terra-constellation-exit-data-outage), [Aqua status Nov 2023](https://assets.science.nasa.gov/content/dam/science/missions/aqua/AquaStatus_November.pdf), [Aqua at 20](https://www.earthdata.nasa.gov/learn/articles/aqua-at-20) [confirmed] |
| MODIS data gap at exit | Terra acquisitions stopped 10 Oct 2022 and resumed 19 Oct 2022; use 19 to 21 Oct 2022 data with care | none (no burn) | [Earthdata Terra exit outage](https://www.earthdata.nasa.gov/data/alerts-outages/terra-constellation-exit-data-outage) [confirmed; added] |
| Size of the altitude drop at exit | about 5 km, about 5.5 km, 6 km, or 705 to 694 km (see conflicts) | not applicable | multiple sources [conflict] |
| Ground track left the ±20 km repeat box | within a few months after the CEMs (late 2022) | within a few months after the last DMU (early 2022) | [Twedt](https://ntrs.nasa.gov/api/citations/20240001409/downloads/2023_SPIE_Twedt_MODIS_EV_orbit_drift_manuscript_v4.pdf) [confirmed] |
| Direction of MLT drift | earlier in the morning | later in the afternoon | [Twedt](https://ntrs.nasa.gov/api/citations/20240001409/downloads/2023_SPIE_Twedt_MODIS_EV_orbit_drift_manuscript_v4.pdf), [LAADS transition](https://ladsweb.modaps.eosdis.nasa.gov/learn/modis-to-viirs-transition) [confirmed] |

- The MODIS Land news page gives an extra Aqua date: "In July 2021, Aqua began drifting to a later MLT." [MODIS Land news](https://modis-land.gsfc.nasa.gov/news.html) [confirmed; added]
- The Terra exit plan (May 2022) sets out the altitude history as mean height, defined as semi-major axis minus Earth radius: DMUs held about 699.4 km until October 2022. The planned exit went to 693.6 km in October 2022, with drift to 688.7 km by February 2026 and PLMs down to 675.5 km in March 2026. [Terra Exit Review](https://ntrs.nasa.gov/api/citations/20220006147/downloads/2022_Mantzarias_presentation_final_EOS%20Terra%20Constellation%20Exit%20Review.pptx.pdf) [confirmed as a 2022 plan; the PLM part did not happen, see status]
- A lower orbit gives narrower MODIS views and "slightly narrower swath widths". An earlier crossing gives longer shadows, which means a lower Sun elevation. NASA expected "minimal" impact on science. [Terra orbital drift information](https://terra.nasa.gov/about/terras-orbit-changes/terra-orbital-drift-information) [confirmed]
- Earthdata's 2021 plan expected Terra products after the exit to be "mostly … science quality except for reduced grid size". It also expected better spatial resolution but possible gaps in spatial sampling, and no strict 16-day repeat cycle. [Terra MODIS Acquisition Plan](https://www.earthdata.nasa.gov/data/alerts-outages/terra-modis-acquisition-plan-through-december-2025) [confirmed]
- Rough size of the swath effect, computed by the verifier and not from a source: the swath width scales roughly with altitude. A 10 to 20 km drop from 705 km narrows the 2330 km swath by roughly 1.5 to 3%, which is about 30 to 65 km. [computed; unverified]

### MLT drift: predictions and measured values

No primary page gives a year-by-year MLT table. NASA's Terra and Aqua pages show the values only as interactive plots. The table lists every dated value found.

| Date | Terra (descending MLT) | Aqua (ascending MLT) | Source / status |
|---|---|---|---|
| Mar 2021 | left 10:30 ±1 min (actual) | 13:30 to 13:45 | [Terra Exit Review](https://ntrs.nasa.gov/api/citations/20220006147/downloads/2022_Mantzarias_presentation_final_EOS%20Terra%20Constellation%20Exit%20Review.pptx.pdf) [confirmed] |
| Fall 2022 | 10:15 (predicted for late Sep 2022 or Oct 2022; NASA says it was reached by fall 2022) | — | [NASA Terra end of era](https://science.nasa.gov/science-research/earth-science/terra-the-end-of-an-era), [Terra acquisition plan](https://www.earthdata.nasa.gov/data/alerts-outages/terra-modis-acquisition-plan-through-december-2025) [confirmed] |
| Feb 2023 | — | passed 13:45 (actual) | [Aqua status Nov 2023](https://assets.science.nasa.gov/content/dam/science/missions/aqua/AquaStatus_November.pdf), [MODIS Land news](https://modis-land.gsfc.nasa.gov/news.html) [confirmed] |
| Dec 2025 to Mar 2026 | 9:00 predicted: "December 2025" (2021 plan, Project Scientist text), "Winter 2025/2026" (Project Scientist key-dates list), "February to March 2026" (Terra status Aug 2022), "17 February 2026" (Exit Review May 2022) | — | [Project Scientist](https://terra.nasa.gov/about/terras-orbit-changes/terra-orbital-drift-information/a-message-from-the-project-scientist), [Terra status Aug 2022](https://terra.nasa.gov/wp-content/uploads/2022/09/ESMO_TerraWebStatus_20220908_v2.pdf), [Terra Exit Review](https://ntrs.nasa.gov/api/citations/20220006147/downloads/2022_Mantzarias_presentation_final_EOS%20Terra%20Constellation%20Exit%20Review.pptx.pdf) [confirmed as predictions] |
| Aug 2026 | — | about 15:30 predicted (Aqua status Nov 2023) vs about 15:50 ("3:50 PM") predicted (2021 acquisition plan, MODIS Land news) | [Aqua status Nov 2023](https://assets.science.nasa.gov/content/dam/science/missions/aqua/AquaStatus_November.pdf), [MODIS Land news](https://modis-land.gsfc.nasa.gov/news.html) [confirmed as predictions] |
| Nov 2026 (NASA page) | 8:32 a.m. in page text; 9:59 in chart alt text | — | [Terra home](https://terra.nasa.gov/) [confirmed that the page shows both] |
| 13 Nov 2026 (computed from TLE) | about 8:33 descending | about 15:49 ascending | [CelesTrak TLE Terra](https://celestrak.org/NORAD/elements/gp.php?CATNR=25994&FORMAT=TLE), [CelesTrak TLE Aqua](https://celestrak.org/NORAD/elements/gp.php?CATNR=27424&FORMAT=TLE) [computed; added] |

- How the TLE values were computed: the TLEs have epochs 2026 day 317.59 (Terra) and 317.58 (Aqua), which is 13 Nov 2026 at about 14:00 UTC. Terra's TLE gives inclination 97.9265°, RAAN 1.0738° and 14.6120 revolutions per day. Aqua's gives 98.4491°, RAAN 290.0185° and 14.6228 revolutions per day. MLT of the ascending node is 12 h + (RAAN − right ascension of the mean Sun)/15, with mean-Sun right ascension 232.7°. The result is Terra 20:33 ascending, so 8:33 descending, and Aqua 15:49 ascending. The mean-motion altitudes (semi-major axis minus 6378 km) are about 689 km for Terra and 686 km for Aqua. Eccentricities are 0.00035 and 0.00011, so both orbits are still near-circular. The Terra result matches NASA's 8:32 text and not the 9:59 alt text. Aqua's 15:49 lies between the two August 2026 predictions. These are the verifier's computations from a non-NASA TLE distributor. [computed]
- Inclination has drifted since the last IAMs: Terra from about 98.2° to 97.93°, Aqua from 98.2° to 98.45° (from the TLEs above). [computed]

### Status on 2026-11-13

**MODIS acquiring on both satellites: yes.** The MCST weekly reports for mission days 2026/311 to 2026/317 (7 to 13 Nov 2026) give these statuses:
- Terra "is in Normal Mode", "PFM MODIS is in A-Side Nominal Science Mode", anomalies none, maneuvers none. [MCST Terra weekly](https://mcst.gsfc.nasa.gov/iot/am1weekly20263112026317) [confirmed; added, supersedes the researcher's July 2026 evidence]
- Aqua "is in Fine Pointing Normal Mode", "FM1 MODIS is in B-Side Nominal Science Mode", anomalies none, maneuvers none. [MCST Aqua weekly](https://mcst.gsfc.nasa.gov/iot/pm1weekly20263112026317) [confirmed; added]
- The MCST weekly report index lists Terra and Aqua reports for every week from late Aug through 13 Nov 2026. [MCST weekly index](https://mcst.gsfc.nasa.gov/iot/weekly-reports) [confirmed]

**Terra platform and instruments**
- Terra status page (last updated 13 Nov 2026): crossing time 8:32 AM MLT and altitude 693 km in the text, but 9:59 and 692 km in the chart alt text. Terra was lowered about 5 km in Oct 2022. No end-of-mission or passivation date is given. [Terra home](https://terra.nasa.gov/) [confirmed]
- MOPITT was put in safe mode on 4 Feb 2025 (terra.nasa.gov) or 1 Feb 2025 (NASA feature) and fully turned off on 9 Apr 2025. ASTER TIR was "permanently turned off" on 16 January; the page does not give the year. The statement that ASTER VNIR, one CERES, MISR and MODIS are still operating comes from the 2025 MOPITT banner and may predate Nov 2026. [Terra home](https://terra.nasa.gov/), [NASA Terra end of era](https://science.nasa.gov/science-research/earth-science/terra-the-end-of-an-era) [confirmed]
- On 26 Mar 2026 at about 20:00 UTC a Terra spacecraft anomaly put MODIS into standby. MODIS returned to science on 27 Mar 2026, with good data after about 19:23 UTC. Data in between are flagged questionable or bad. [Earthdata alert](https://www.earthdata.nasa.gov/data/alerts-outages/terra-modis-placed-standby-mode) [confirmed; this is the event behind the LAADS 31 Mar 2026 "Terra Data Anomaly" title]
- The Terra battery is degrading, which has forced power reductions. [NASA Terra end of era](https://science.nasa.gov/science-research/earth-science/terra-the-end-of-an-era) [confirmed]
- The 2022 exit plan scheduled PLMs from 25 Feb to 25 Mar 2026, once Terra reached 9:00 MLT, with end of mission in 2026. The Nov 2026 TLE shows a near-circular orbit at about 689 km, with no 655 km perigee, and MODIS is still in science mode. So the 2026 PLM plan was not carried out. [Terra Exit Review](https://ntrs.nasa.gov/api/citations/20220006147/downloads/2022_Mantzarias_presentation_final_EOS%20Terra%20Constellation%20Exit%20Review.pptx.pdf), [CelesTrak TLE](https://celestrak.org/NORAD/elements/gp.php?CATNR=25994&FORMAT=TLE) [confirmed plan; "not carried out" is the verifier's inference]
- The Project Scientist page says "there has not been an official passivation date set". [Project Scientist](https://terra.nasa.gov/about/terras-orbit-changes/terra-orbital-drift-information/a-message-from-the-project-scientist) [confirmed]

**Aqua platform and instruments**
- The NASA Aqua page (last updated 5 Oct 2026) says four of six instruments are returning data: AIRS, AMSU, CERES and MODIS. AMSR-E was off from March 2016 and HSB failed in Feb 2003. Aqua is in free drift, descending below the A-Train. The page gives no end date. [NASA Aqua](https://science.nasa.gov/mission/aqua/) [confirmed]
- The Aqua status of 30 Nov 2023 says power generation is the expected life-limiting factor. Of 132 solar array strings, 106 work (80.3% capability) and 26 had failed. Power margin was predicted to reach zero in August 2026. A 2023 reliability study gave a 95.8% probability that the bus would function past 2026. [Aqua status Nov 2023](https://assets.science.nasa.gov/content/dam/science/missions/aqua/AquaStatus_November.pdf) [confirmed]
- The Nov 2023 end-of-mission plan was instrument shutdown on 26 Aug 2026, PLMs in Sep to Oct 2026 and passivation on 4 Nov 2026. [Aqua status Nov 2023](https://assets.science.nasa.gov/content/dam/science/missions/aqua/AquaStatus_November.pdf) [confirmed as a plan]. **It was not carried out:** MODIS was in science mode on 7 to 13 Nov 2026 with no maneuvers, and the TLE of 13 Nov 2026 shows a near-circular orbit. [MCST Aqua weekly](https://mcst.gsfc.nasa.gov/iot/pm1weekly20263112026317) [confirmed]
- Aqua had earlier outages: an FMU/SSR anomaly from 22 Feb to 23 Mar 2022, and a power-controller anomaly that put it in safe mode on 31 Mar 2022, with instruments back by 15 Apr 2022. [Aqua status Nov 2023](https://assets.science.nasa.gov/content/dam/science/missions/aqua/AquaStatus_November.pdf) [confirmed; added]. A soft FMU/SSR reset on 22 Jul 2026 (day 203) stopped science until the start of day 204. [MCST Aqua weekly 2026/199-205](https://mcst.gsfc.nasa.gov/iot/pm1weekly20261992026205) [confirmed]

**Announced end dates (all projections; none carried out as of 2026-11-13)**

| Source (date) | Terra MODIS / Terra | Aqua MODIS / Aqua | Status |
|---|---|---|---|
| [Terra acquisition plan](https://www.earthdata.nasa.gov/data/alerts-outages/terra-modis-acquisition-plan-through-december-2025) (19 Oct 2021; editor's note of 4 Sep 2026 says Terra is still operating) | full product suite until end of mission in Dec 2025 (also on [MODIS Land news](https://modis-land.gsfc.nasa.gov/news.html)) | — | [confirmed; superseded] |
| [MODIS Land news](https://modis-land.gsfc.nasa.gov/news.html) (Aqua plan of Oct 2021) | — | full product suite until end of mission in Aug 2026 | [confirmed; superseded] |
| [Aqua at 20](https://www.earthdata.nasa.gov/learn/articles/aqua-at-20) (17 May 2022) | — | good-quality science "until August of 2026", if funded | [confirmed; superseded] |
| [Terra Exit Review](https://ntrs.nasa.gov/api/citations/20220006147/downloads/2022_Mantzarias_presentation_final_EOS%20Terra%20Constellation%20Exit%20Review.pptx.pdf) (May 2022) | PLMs Feb to Mar 2026; end of mission 2026; re-entry about 2069 | — | [confirmed; superseded] |
| [Aqua status](https://assets.science.nasa.gov/content/dam/science/missions/aqua/AquaStatus_November.pdf) (30 Nov 2023) | — | instruments off 26 Aug 2026; PLMs Sep to Oct 2026; passivation 4 Nov 2026 | [confirmed; superseded] |
| [LAADS MODIS to VIIRS transition PDF](https://ladsweb.modaps.eosdis.nasa.gov/learn/modis-to-viirs-transition/MODIS-VIIRS_Transition.pdf) (18 Apr 2025) | stop science collection "around January 2027" | "around August 2026"; final v8.0 reprocessing complete by Jan 2030 | [confirmed; added] |
| [Earthdata alert](https://www.earthdata.nasa.gov/data/alerts-outages/transition-from-modis-viirs) (2 May 2025) | platforms begin shutting down "in late 2026/early 2027"; then MODIS collection ends and final reprocessing follows | same | [confirmed] |
| [NASA Terra end of era](https://science.nasa.gov/science-research/earth-science/terra-the-end-of-an-era) (29 Dec 2025, updated 20 Mar 2026) | end of science Feb 2027 | end of science Sep 2027 | [confirmed] |
| [Military Aerospace](https://www.militaryaerospace.com/commercial-aerospace/article/55354691/nasa-seeks-commercial-partners-for-terra-aqua-aura-earth-science-satellite-operations) (3 Feb 2026, secondary; reports a NASA request for information on commercial operation of Terra, Aqua and Aura) | operations possible to Feb 2027 | to Sep 2027 | [confirmed on secondary; added] |
| [CAMS](https://atmosphere.copernicus.eu/drifting-away-modis-cams-global-fire-assimilation-system) (25 Feb 2026, secondary) | end collection Jan 2027 | around Sep 2027; then final v8.0 reprocessing | [confirmed on secondary] |
| [LAADS transition web page](https://ladsweb.modaps.eosdis.nasa.gov/learn/modis-to-viirs-transition) (undated, version 4.0.11) | no date; Terra and Aqua MODIS entering decommissioning (Phase F); "No follow-on MODIS-like instrument with an orbit at the Terra morning equatorial-crossing MLT exists" | no date | [confirmed] |

- The LAADS alerts list has an entry dated 6 Oct 2026: "Cessation of Suomi National Polar-orbiting Partnership (S-NPP) data to users on November 02, 2026". This concerns VIIRS, not Terra or Aqua, and only the title was seen. [LAADS alerts](https://ladsweb.modaps.eosdis.nasa.gov/alerts-and-issues/171807) [confirmed title only]

### Calibration context (MODIS Level 1B)
- The MODIS reflective solar bands span 412 to 2130 nm. Since Collection 6 their calibration has used desert targets for some visible bands. Collection 6.1 (Terra) and Collection 7 added ocean scenes and deep convective clouds. The researcher wrote that C6/6.1 uses all three for both satellites. In fact, C6 added desert only, and the ocean and deep-convective-cloud scenes were added in C6.1 for Terra and in C7. [Twedt](https://ntrs.nasa.gov/api/citations/20240001409/downloads/2023_SPIE_Twedt_MODIS_EV_orbit_drift_manuscript_v4.pdf) [corrected]
- Version 7.0 MODIS calibrated radiance and geolocation products were released with an issue date of 27 Mar 2026. This comes from a search summary of an Earthdata alert and the page was not opened. [unverified]

## Why these matter for combining the records

Terra observes in the morning on its southbound pass and Aqua in the early afternoon on its northbound pass. Fire activity follows a strong daily cycle, so detection counts depend on overpass time. Both overpass times held to within a few minutes from 2002 until 2021 (Terra) and early 2023 (Aqua). After that, Terra moved from 10:30 to about 8:33 and Aqua from 13:30 to about 15:49 by November 2026, so the post-drift MODIS record samples different times of day than the long baseline. The loss of the 16-day repeat ground track (2022) and the small altitude drops change view geometry and swath at a given place and date. Known gaps, such as 10 to 19 Oct 2022 for Terra, spring 2022 for Aqua and 26 to 27 Mar 2026 for Terra, affect monthly totals. Both satellites are projected to end science collection in 2027. No instrument continues the Terra morning orbit, so the morning series will end with no direct successor.

## Conflicts and unverified items

1. **Terra inclination.** 98.5° on [Terra About](https://terra.nasa.gov/About) and [Earthdata MODIS](https://www.earthdata.nasa.gov/data/instruments/modis), against 98.2° in the [Terra Mission Director's Constellation Exit Review (May 2022)](https://ntrs.nasa.gov/api/citations/20220006147/downloads/2022_Mantzarias_presentation_final_EOS%20Terra%20Constellation%20Exit%20Review.pptx.pdf). 98.2° is more authoritative: it comes from the flight operations team and matches the computed sun-synchronous inclination for 705 km (98.21°). 98.5° looks like a long-repeated nominal value.
2. **Terra altitude drop at the 2022 exit.** About 5 km ([NASA Terra end of era](https://science.nasa.gov/science-research/earth-science/terra-the-end-of-an-era), [Terra home](https://terra.nasa.gov/)). About 5.5 km ([Twedt 2023](https://ntrs.nasa.gov/api/citations/20240001409/downloads/2023_SPIE_Twedt_MODIS_EV_orbit_drift_manuscript_v4.pdf)). 6 km and 705 to 694 km ([Project Scientist](https://terra.nasa.gov/about/terras-orbit-changes/terra-orbital-drift-information/a-message-from-the-project-scientist), [2021 plan](https://www.earthdata.nasa.gov/data/alerts-outages/terra-modis-acquisition-plan-through-december-2025)). 699.4 to 693.6 km, which is 5.8 km of mean height ([Exit Review](https://ntrs.nasa.gov/api/citations/20220006147/downloads/2022_Mantzarias_presentation_final_EOS%20Terra%20Constellation%20Exit%20Review.pptx.pdf)). Twedt, written after the burns, is the best value for the actual change. The "705 km" figures are nominal altitudes, while 699.4 km is mean height above the equatorial radius, so the bases differ.
3. **Terra current values on [terra.nasa.gov](https://terra.nasa.gov/) (13 Nov 2026).** The text says 8:32 AM and 693 km; the chart alt text says 9:59 and 692 km. The verifier's TLE computation for 13 Nov 2026 (8:33) supports 8:32, so the alt text is stale.
4. **Terra last IAM.** 27 Feb 2020 ([Twedt](https://ntrs.nasa.gov/api/citations/20240001409/downloads/2023_SPIE_Twedt_MODIS_EV_orbit_drift_manuscript_v4.pdf), [Project Scientist](https://terra.nasa.gov/about/terras-orbit-changes/terra-orbital-drift-information/a-message-from-the-project-scientist), [Exit Review](https://ntrs.nasa.gov/api/citations/20220006147/downloads/2022_Mantzarias_presentation_final_EOS%20Terra%20Constellation%20Exit%20Review.pptx.pdf), [MODIS Land news](https://modis-land.gsfc.nasa.gov/news.html)) against "late 2020" in the [NASA Terra end-of-era feature](https://science.nasa.gov/science-research/earth-science/terra-the-end-of-an-era). The Exit Review also says "normal operations through October 2020". 27 Feb 2020 is authoritative because it comes from operations documents with the IAM number.
5. **Terra left 10:30 ±1 min.** "April 2021" (prediction, [Project Scientist](https://terra.nasa.gov/about/terras-orbit-changes/terra-orbital-drift-information/a-message-from-the-project-scientist)) against "March of 2021" (actual, [Exit Review May 2022](https://ntrs.nasa.gov/api/citations/20220006147/downloads/2022_Mantzarias_presentation_final_EOS%20Terra%20Constellation%20Exit%20Review.pptx.pdf)). The later document reports the actual date.
6. **Terra 9:00 MLT date.** Dec 2025; Winter 2025/2026; Feb to Mar 2026; 17 Feb 2026 (sources in the MLT table). The verifier's TLE computation gives about 8:33 in Nov 2026, so 9:00 was passed earlier in 2026 or before. The exact date is not confirmed.
7. **Aqua MLT in Aug 2026.** About 15:30 ([Aqua status Nov 2023](https://assets.science.nasa.gov/content/dam/science/missions/aqua/AquaStatus_November.pdf); a search summary says the May 2025 status gave 15:30 in July 2026) against about 15:50 ([2021 plan via MODIS Land news](https://modis-land.gsfc.nasa.gov/news.html)). The TLE gives 15:49 in mid-Nov 2026, which suggests the 2023 projection ran early. Neither is a measurement.
8. **Aqua end of mission.** Shutdown 26 Aug 2026 and passivation 4 Nov 2026 ([Aqua status Nov 2023](https://assets.science.nasa.gov/content/dam/science/missions/aqua/AquaStatus_November.pdf)); passivation 11 Nov 2026 per an Aug 2025 status (search summary only, [unverified]); "around August 2026" ([LAADS Apr 2025](https://ladsweb.modaps.eosdis.nasa.gov/learn/modis-to-viirs-transition/MODIS-VIIRS_Transition.pdf)); Sep 2027 ([NASA Dec 2025 feature](https://science.nasa.gov/science-research/earth-science/terra-the-end-of-an-era), [CAMS Feb 2026](https://atmosphere.copernicus.eu/drifting-away-modis-cams-global-fire-assimilation-system)). The latest NASA projection (Sep 2027) agrees with the Nov 2026 MCST report that MODIS is still in science mode.
9. **Terra end of MODIS.** Dec 2025 (2021 plan), 2026 (2022 Exit Review), Jan 2027 ([LAADS Apr 2025](https://ladsweb.modaps.eosdis.nasa.gov/learn/modis-to-viirs-transition/MODIS-VIIRS_Transition.pdf), CAMS), Feb 2027 ([NASA Dec 2025 feature](https://science.nasa.gov/science-research/earth-science/terra-the-end-of-an-era)). The NASA feature is the most recent primary source.
10. **MOPITT safe mode.** 1 Feb 2025 ([NASA feature](https://science.nasa.gov/science-research/earth-science/terra-the-end-of-an-era)) against 4 Feb 2025 ([terra.nasa.gov](https://terra.nasa.gov/)). Not resolved.
11. **Unverified:** Aqua period 98.8 min and 233 orbits per 16 days, and Terra 233 orbits. These were found only on eoPortal (secondary), but they agree with the verifier's orbital computation. [unverified on a primary page]
12. **Unverified:** "IAMs averaged about four per year" (researcher, citing the Project Scientist page). Not found in this check, and Twedt says "roughly yearly".
13. **Unverified:** the Wikipedia claim that "by June 2026 NASA predicted operation into September" (2026), which cites an aqua.nasa.gov announcements page that now redirects. Also unverified: a search-summary claim that NASA's Aqua page says data collection ends in "early Fall 2027"; the 5 Oct 2026 version of the page opened here does not say so.
14. **Unverified:** a 2023 Terra status presentation (MODIS Science Team, May 2023) reportedly gives end of science Feb 2027 and PLMs and passivation in Sep 2027. Seen only in a search summary; the PDF would not load.
15. **Wikipedia Aqua infobox** (inclination 98.1987°, period 99 min, perigee 702 km, apogee 703 km, epoch 2 Jun 2016). Uncited and secondary. Kept only as a snapshot. [unverified]

## Open questions

- There is no official year-by-year (or monthly) MLT and altitude table for either satellite. NASA shows these only in interactive plots on the Terra and Aqua home pages. A full series would have to come from historical TLEs or the flight dynamics ephemerides.
- The exact date Terra passed 9:00 MLT in 2025 or 2026, and whether its PLMs were cancelled or only postponed toward the Feb 2027 end of science.
- Whether NASA has set firm dates for Terra and Aqua instrument shutdown, PLMs and passivation in 2027, and whether the 2026 request for information on commercial operation changes them.
- The exact ASTER TIR shutdown year (16 January, probably 2026).
- How much the post-2022 orbit changes alter the MODIS swath edge and pixel size at each latitude. No primary quantification was found.
- The exact date Aqua left the A-Train volume: only "January 2022" (start of drag-down) was found.

## Sources

- MCST, Some information about MODIS: https://mcst.gsfc.nasa.gov/index.php/some-information-about-modis
- MCST weekly report index: https://mcst.gsfc.nasa.gov/iot/weekly-reports
- MCST Terra (AM-1) weekly 2026/311-317: https://mcst.gsfc.nasa.gov/iot/am1weekly20263112026317
- MCST Aqua (PM-1) weekly 2026/311-317: https://mcst.gsfc.nasa.gov/iot/pm1weekly20263112026317
- MCST Aqua (PM-1) weekly 2026/199-205: https://mcst.gsfc.nasa.gov/iot/pm1weekly20261992026205
- Terra home and status page: https://terra.nasa.gov/
- Terra About: https://terra.nasa.gov/About
- Terra orbital drift information: https://terra.nasa.gov/about/terras-orbit-changes/terra-orbital-drift-information
- Terra, A message from the Project Scientist: https://terra.nasa.gov/about/terras-orbit-changes/terra-orbital-drift-information/a-message-from-the-project-scientist
- Terra Summary (as of 31 Aug 2022): https://terra.nasa.gov/wp-content/uploads/2022/09/ESMO_TerraWebStatus_20220908_v2.pdf
- Mantziaras, EOS Terra Constellation Exit Review, MOWG May 2022 (NTRS): https://ntrs.nasa.gov/api/citations/20220006147/downloads/2022_Mantzarias_presentation_final_EOS%20Terra%20Constellation%20Exit%20Review.pptx.pdf
- NASA Science, Terra: The End of An Era (29 Dec 2025, updated 20 Mar 2026): https://science.nasa.gov/science-research/earth-science/terra-the-end-of-an-era
- NASA Science, Aqua mission page (updated 5 Oct 2026): https://science.nasa.gov/mission/aqua/
- Aqua Summary as of 30 Nov 2023: https://assets.science.nasa.gov/content/dam/science/missions/aqua/AquaStatus_November.pdf
- Earthdata, Aqua at 20 (17 May 2022): https://www.earthdata.nasa.gov/learn/articles/aqua-at-20
- Earthdata, MODIS instrument page: https://www.earthdata.nasa.gov/data/instruments/modis
- Earthdata alert, Terra MODIS Acquisition Plan Through December 2025 (19 Oct 2021): https://www.earthdata.nasa.gov/data/alerts-outages/terra-modis-acquisition-plan-through-december-2025
- Earthdata alert, Terra Constellation Exit Data Outage (Oct 2022): https://www.earthdata.nasa.gov/data/alerts-outages/terra-constellation-exit-data-outage
- Earthdata alert, Terra MODIS Placed in Standby Mode (26 Mar 2026): https://www.earthdata.nasa.gov/data/alerts-outages/terra-modis-placed-standby-mode
- Earthdata alert, Transition from MODIS to VIIRS (2 May 2025): https://www.earthdata.nasa.gov/data/alerts-outages/transition-from-modis-viirs
- Earthdata catalog, MOD14A1 v061: https://www.earthdata.nasa.gov/data/catalog/lpcloud-mod14a1-061
- Earthdata catalog, MYD14A1 v061: https://www.earthdata.nasa.gov/data/catalog/lpcloud-myd14a1-061
- LAADS DAAC, MODIS mission page: https://ladsweb.modaps.eosdis.nasa.gov/missions-and-measurements/modis/
- LAADS DAAC, MODIS To VIIRS Transition: https://ladsweb.modaps.eosdis.nasa.gov/learn/modis-to-viirs-transition
- LAADS DAAC, MODIS to VIIRS Transition for Atmospheric Science Products (18 Apr 2025, PDF): https://ladsweb.modaps.eosdis.nasa.gov/learn/modis-to-viirs-transition/MODIS-VIIRS_Transition.pdf
- LAADS DAAC alerts and issues: https://ladsweb.modaps.eosdis.nasa.gov/alerts-and-issues/171807
- MODIS Land Team news: https://modis-land.gsfc.nasa.gov/news.html
- Twedt et al., Impact of satellite orbit drift on MODIS Earth scene observations (SPIE 2023, NTRS): https://ntrs.nasa.gov/api/citations/20240001409/downloads/2023_SPIE_Twedt_MODIS_EV_orbit_drift_manuscript_v4.pdf
- CelesTrak GP element set, Terra (NORAD 25994): https://celestrak.org/NORAD/elements/gp.php?CATNR=25994&FORMAT=TLE
- CelesTrak GP element set, Aqua (NORAD 27424): https://celestrak.org/NORAD/elements/gp.php?CATNR=27424&FORMAT=TLE
- Secondary: eoPortal Aqua: https://www.eoportal.org/satellite-missions/aqua
- Secondary: eoPortal Terra: https://www.eoportal.org/satellite-missions/terra
- Secondary: Wikipedia, Aqua (satellite): https://en.wikipedia.org/wiki/Aqua_(satellite)
- Secondary: Copernicus CAMS, Drifting away from MODIS in the CAMS GFAS (25 Feb 2026): https://atmosphere.copernicus.eu/drifting-away-modis-cams-global-fire-assimilation-system
- Secondary: Military Aerospace, NASA seeks commercial partners for Terra, Aqua, Aura (3 Feb 2026): https://www.militaryaerospace.com/commercial-aerospace/article/55354691/nasa-seeks-commercial-partners-for-terra-aqua-aura-earth-science-satellite-operations
