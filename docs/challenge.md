# Challenge reference: Harmonization of MODIS and VIIRS Hot Spots

Team reference for City of Kamloops & Co. Compiled from the official challenge page (details and Resources tab; last published 2026-11-13), the author video and its auto-generated transcript, [discussion #1879](https://github.com/nasa/spaceapps/discussions/1879), and FIRMS API notes checked 2026-11-13. Quotes are from those sources. The last section is a team proposal, not part of the challenge text.

| | |
|---|---|
| Page | [Harmonization of MODIS and VIIRS Hot Spots](https://www.spaceappschallenge.org/2026/challenges/modis-and-viirs-hot-spots/) |
| Video | [Challenge briefing](https://www.youtube.com/watch?v=tEPHsiZtuvk) (`tEPHsiZtuvk`) |
| Author | Marina Compagnucci, CONAE (Argentinian Space Agency), Teófilo Tabanera Space Center, Córdoba |
| Difficulty | Advanced, Intermediate |
| Subject tags | Earth Science, Software |
| Photo credit | The National Commission on Space Activities of Argentina (CONAE) |

## The ask

> "Your challenge is to build a web application that harmonizes these records into a burning activity calendar based on active fire hotspots, enabling early warning and emergency responders, scientists, and land managers to examine historical fire patterns, unusual conditions, and critical periods within a selected area of interest."

Satellites have tracked active-fire hotspots for more than two decades, but the record is split across sensors "whose data cannot be compared directly."

The page says the work can be approached in two parts:

1. **Harmonize MODIS and VIIRS hotspots** "so that by the end of that phase the sensor of origin no longer matters and the patterns, trends, and anomalies become the focus."
2. **A web application** that takes the harmonized hotspots as input. A user could select a region and a date range, then download analytics and visualizations of fire activity.

The author video states the same split, and says a team may approach the challenge differently.

## Why the records differ

MODIS (Terra and Aqua) has more than two decades of observations and is approaching the end of its operational life. VIIRS is the replacement. The records "cannot be directly compared without harmonization, since MODIS and VIIRS have different spatial resolutions, sensitivities, and observation schedules."

In the video, the author says that without a way to compare them, "almost 10 years of historical information will be lost." The video uses a July 2026 fire in Chilecito, La Rioja, Argentina, as the worked example: hotspots to watch the event while waiting for a satellite pass, then imagery for burned-area detail. The transcript is auto-generated.

Burning activity here means wildfires in natural vegetation and forest, plus anthropogenic fires (agriculture, land-clearing, waste disposal, industrial activity). Thermal sensors also detect urban fires, volcanoes, and gas flares. Active-fire detection uses mid-infrared and thermal infrared, where combustion is strongest.

The page's example of what a consistent calendar should make obvious: "which month and years had the highest fire activity, and compare the burning activity of the current month against the historical median for a selected area."

## Features the challenge describes

**Objective (stated as the challenge):**

> "develop a harmonized burning activity calendar based on active fire hotspots in a web application, combining the extensive historical series of MODIS with the continuity and greater detail of VIIRS to provide a consistent time series of hotspot activity."

**Calendar and comparison.** A calendar of the number of hotspots "from the early 2000s to the present," showing which periods of the year see more fires, which years had more burning, and "how a current fire compares with previous ones."

**Area and dates.** Through the app, "a user could select a region and a specific date range, then download analytics and visualizations of fire activity." The video says a user might "choose a specific day, a particular region" and then follow some analytics.

**Time step.** The page frames the comparison by month (current month vs historical median; color across months). The author later called monthly data a solid approach. See [Author clarifications](#author-clarifications).

**Color.** "you could consider how color ramps might represent similarities and differences in the number of detected hotspots across months, providing an accessible and intuitive way to visualize fire activity."

**Download.** "A downloadable CSV File of hot spots detected during a search would be another useful output."

**Suggested data path on the page:** "You may consider harmonizing NASA Earthdata FIRMS hotspots."

### Optional (not required)

The page labels these "You may (but are not required to) consider":

- Audience can include early warning and emergency responders, scientists, land managers, and firefighters.
- An interactive app, for example a map where users draw the area of interest, or an option to enter latitude and longitude.
- Accessible color ramps.
- A burning calendar.
- A few key figures, such as historical comparisons (anomalies against multi-year averages) and the number of fires detected and reported.

The page says more resources may be added before the hackathon begins.

## Author clarifications

From the challenge author (`m-compagnucci`, 2026-11-13) in [nasa/spaceapps discussion #1879](https://github.com/nasa/spaceapps/discussions/1879). An earlier comment in that thread is explicitly not a judge's answer; use the author's reply.

| Question | Author's answer |
|---|---|
| MODIS-equivalent or VIIRS-equivalent record? | "Either alternative is fine if properly justified." |
| Is the standard FIRMS archive acceptable, or are swath products expected? | "Yes, it is acceptable since FIRMS is the suggested NASA resource for the challenge." |
| Include NOAA-20 and NOAA-21 for continuity? | "Yes, it makes sense to look for solutions that extend into the future—therefore, NOAA-20 and NOAA-21 satellites that are still active." |
| Who is it for, and what time step? | Audience is the list under Potential Considerations. Daily data "generally exhibit high variability that could blur underlying patterns." "Monthly data seems like a solid approach, and weekly data could be interesting, provided it is feasible." A weekly calendar still has to stay easy to visualize. |
| Is Google Earth Engine acceptable for datasets such as `MOD14A1`? | "Yes it is acceptable, but keep in mind to use NASA suggested resources during the challenge solving process." |

The question assumed FIRMS stopped new Suomi NPP data on 2 November 2022. The author did not confirm that date. The FIRMS archive download page, checked 2026-11-13, lists VIIRS S-NPP 375 m coverage as 20 January 2012 – 2 November 2026. Include NOAA-20 and NOAA-21 anyway, as the author asked.

## Official resources and links

The Resources tab (as published 2026-11-13) contains one NASA resource, plus this disclaimer:

> "NASA does not endorse any non-U.S. Government entity and is not responsible for information contained on non-U.S. Government websites. For non-U.S. Government websites, participants must comply with any data use parameters of that specific website."

**[FIRMS — Fire Information for Resource Management System](https://www.earthdata.nasa.gov/data/tools/firms)** (the tab's wording): global near real-time satellite imagery, active fire/hotspots, and related products "to identify the location, extent, and intensity of wildfire activity," for the fire management community and the public.

The video also says to use the NASA FIRMS website and resources from CONAE and other agencies. It does not name those other URLs.

| Resource | URL |
|---|---|
| Challenge page | https://www.spaceappschallenge.org/2026/challenges/modis-and-viirs-hot-spots/ |
| Author video | https://www.youtube.com/watch?v=tEPHsiZtuvk |
| Author Q&A | https://github.com/nasa/spaceapps/discussions/1879 |
| FIRMS (Earthdata) | https://www.earthdata.nasa.gov/data/tools/firms |
| FIRMS FAQ | https://www.earthdata.nasa.gov/data/tools/firms/faq |
| FIRMS API index | https://firms.modaps.eosdis.nasa.gov/api/ |
| Area API docs | https://firms.modaps.eosdis.nasa.gov/api/area/ |
| MAP_KEY signup | https://firms.modaps.eosdis.nasa.gov/api/map_key/ |
| Data availability API | https://firms.modaps.eosdis.nasa.gov/api/data_availability/ |
| Python tutorial | https://firms.modaps.eosdis.nasa.gov/content/academy/data_api/firms_api_use.html |
| Archive download UI | https://firms.modaps.eosdis.nasa.gov/download/ |

## FIRMS data essentials

Checked 2026-11-13. No MAP_KEY was requested for these checks. Open CSV checks used HTTP HEAD and a Range request for the header row.

### MAP_KEY

- Free key, requested by email at the [map key page](https://firms.modaps.eosdis.nasa.gov/api/map_key/). This is not an Earthdata login.
- Required for the API and map services (area, data availability, WMS/WFS).
- Limit: **5000 transactions per 10-minute window**, then it resets. Larger transactions may count as multiple requests.
- Status: `https://firms.modaps.eosdis.nasa.gov/mapserver/mapkey_status/?MAP_KEY=...`
- Tutorial example: a 1-day world VIIRS NOAA-20 area query used 36 transactions; a data-availability query used 5.

In this repo the key belongs only in a git-ignored `.env` as `FIRMS_MAP_KEY`. See [AGENTS.md](../AGENTS.md).

### Area API

Recommended for an area of interest. URL:

```text
GET https://firms.modaps.eosdis.nasa.gov/api/area/csv/{MAP_KEY}/{SOURCE}/{AREA_COORDINATES}/{DAY_RANGE}/{DATE}
```

- `AREA_COORDINATES`: `west,south,east,north` or `world`. Maximum box is `-180,-90,180,90`.
- `DAY_RANGE`: 1–5. Days start at `DATE`, or the most recent days if `DATE` is omitted.
- `DATE`: optional `YYYY-MM-DD`. Historical dates are supported.
- **SP** = standard processing (science-quality, multi-month lag). **NRT** may include RT/URT.

| Source code | Sensor |
|---|---|
| `MODIS_NRT`, `MODIS_SP` | MODIS |
| `VIIRS_SNPP_NRT`, `VIIRS_SNPP_SP` | VIIRS Suomi NPP |
| `VIIRS_NOAA20_NRT`, `VIIRS_NOAA20_SP` | VIIRS NOAA-20 |
| `VIIRS_NOAA21_NRT`, `VIIRS_NOAA21_SP` | VIIRS NOAA-21 |
| `LANDSAT_NRT` | Landsat, US/Canada only |

### Country API — down, and a poor fit for Canada

The API index marks country and countries as "Feature currently not available." Live checks on 2026-11-13:

- `/api/countries/` and `/api/countries/?format=html` → HTTP 400 "Invalid API call."
- `/api/country/` → HTTP 400 "Invalid API call."

When it is up, the documented call is `/api/country/csv/{MAP_KEY}/{SOURCE}/{COUNTRY_CODE}/{DAY_RANGE}/{DATE}` with `DAY_RANGE` 1–10. The docs say it is "Not recommended for large countries such as USA, China, Canada, Russia" because of timeout risk.

For British Columbia, use an Area API bounding box or clip the yearly country CSVs. Do not rely on the country endpoint.

### Open yearly Canada CSVs (no key)

These need no MAP_KEY and no Earthdata login.

- MODIS: `https://firms.modaps.eosdis.nasa.gov/data/country/modis/{YEAR}/modis_{YEAR}_Canada.csv`
- VIIRS S-NPP: `https://firms.modaps.eosdis.nasa.gov/data/country/viirs-snpp/{YEAR}/viirs-snpp_{YEAR}_Canada.csv`
- VIIRS NOAA-20 (2018–2025): `https://firms.modaps.eosdis.nasa.gov/data/country/viirs-jpss1/{YEAR}/viirs-jpss1_{YEAR}_Canada.csv`

Confirmed sizes (bytes): MODIS Canada 2023 = 26,472,607; 2024 = 12,052,143; 2025 = 12,749,281. MODIS Canada 2000 and 2001 were also probed. VIIRS S-NPP Canada 2023 = 140,649,416. The same notes point at VIIRS S-NPP Canada 2024 and 2025 when those files are present. MODIS collection coverage on the download page starts 1 November 2000.

MODIS 2023 Canada header:

```text
latitude,longitude,brightness,scan,track,acq_date,acq_time,satellite,instrument,confidence,version,bright_t31,frp,daynight,type
```

**Corrected 2026-11-14.** This section first said that NOAA-20 and NOAA-21 yearly country paths returned 404 and that only MODIS and VIIRS S-NPP have open per-country archives. NOAA-20 files do exist, for 2018 to 2025, under the prefix `viirs-jpss1`; the path tried earlier used a different prefix. For example, `data/country/viirs-jpss1/2023/viirs-jpss1_2023_Canada.csv` is 138,176,145 bytes. NOAA-21 has no country files. Sources: the [country file index](https://firms.modaps.eosdis.nasa.gov/data/country/yearly_summary_files.txt) and a header-only request, both on 2026-11-14; [sensor-reference.md](sensor-reference.md), "FIRMS data". For NOAA-21, use the Area API (MAP_KEY, 5-day pages) or a custom request in the Archive Download UI.

### Archive coverage

Stated on the [download page](https://firms.modaps.eosdis.nasa.gov/download/) on 2026-11-13. The page offers "Download yearly summary by country [.csv]" and custom requests that are emailed when ready.

| Product | Coverage stated |
|---|---|
| Landsat 30 m | 20 June 2022 – present |
| MODIS Collection 6.1 | 1 November 2000 – present |
| VIIRS S-NPP 375 m | 20 January 2012 – 2 November 2026 |
| VIIRS NOAA-20 375 m | 1 April 2018 – present |
| VIIRS NOAA-21 375 m | 1 March 2023 – present |

The download UI has an email login and an Earthdata OAuth login (`/oauth/login?redirect=/api/auth/login/download/ed/`). That login is for managing MAP_KEYs and, likely, custom archive requests.

Swath products (MOD14 / VNP14IMG and similar) and the UMD burned-area SFTP are separate products and need their own credentials. The author said the standard FIRMS archive is acceptable.

### Earthdata login — not needed for the path above

Not required to request a MAP_KEY, to call the Area API with a MAP_KEY, or to download the open yearly country CSVs.

Likely or optional for custom area orders in the download UI and for LP DAAC swath products. Swath products are outside this path if the team stays on FIRMS.

## Proposed direction (proposed, not final)

Working proposal for this team. It is not required by the challenge text, and it is not a final decision.

- A burning-activity calendar for Kamloops / Interior British Columbia.
- A Streamlit web app.
- Pre-cached data, so the demo runs offline.
- A simple harmonization method, written down and justified. The author said a MODIS-equivalent or a VIIRS-equivalent record is fine if properly justified.

The proposal is aimed at the features in [Features the challenge describes](#features-the-challenge-describes): an area of interest and a date range, a monthly step from the early 2000s to the present, a comparison of the current period with the history of that area, an accessible color ramp, and a downloadable CSV of the hotspots in the search.
