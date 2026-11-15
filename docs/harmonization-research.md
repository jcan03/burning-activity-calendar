# Harmonization research: findings and a recommended method

Research handoff for whoever owns the data and harmonization work. Compiled 14 November 2026. It recommends a method; it does not decide one.

**How it was produced.** 41 research agents covered 17 topics (9 literature, 8 analyses of the cached data). A second agent independently re-checked each topic's key claims. Three method proposals were then prototyped and scored on one common test, and a final critic looked for contradictions. A few numbers were re-run by hand afterwards and are marked "re-checked".

**Data used.** All 737,244 FIRMS hotspots in the box west −122.5, south 49.0, east −118.0, north 52.5, from 1 November 2000 to 14 November 2026 (`download_kamloops.py`, `build_db.py`). Standard data through 2025 unless stated.

Sensor facts are in [sensor-reference.md](sensor-reference.md). This file is about what to do with them.

## Recommended method

A VIIRS-equivalent, per-satellite monthly index, ranked by percentile.

1. **Filter rows.**
   - Keep `type` 0, 3 and empty (near-real-time). Drop `type` 1 and 2.
   - Drop every row within 0.4 km of 50.68872, −120.40745 (a static heat source west of Kamloops), including near-real-time rows.
   - Drop low confidence: MODIS below 30, VIIRS `l`.
   - No scan-angle, FRP or duplicate filters.
2. **Count per satellite, then divide by satellite-days.** For each month and each sensor family, rate = 30 × hotspots ÷ satellite-days in service. Satellite-days exclude known outages. Never add satellites together.
3. **Convert MODIS to VIIRS units with one factor, k.** k = sum of VIIRS rates ÷ sum of MODIS rates over February 2012 to December 2025, fitted once on the whole box. With the filters above k = 8.73.
4. **Build the index.** Before February 2012: MODIS rate × k. From February 2012: the VIIRS rate. MODIS is used after 2012 only to check the method.
5. **Rank each month against the same calendar month in other years** (percentile, five classes, plus a record marker). Rules that worked in testing: at least 8 baseline years; label the class "uncertain" when 20% or more of the baseline ties with the value; show "× median" only when the baseline median is at least 3.

**Flag rather than correct:** Terra-only months (2000-11 to 2002-06), MODIS-scaled months (before 2012-02), near-real-time months (VIIRS from 2026-08, MODIS from 2026-09), outage months (2022-07, 2022-08, 2022-10), partial months, and off-season months before 2012 (see "What MODIS cannot see").

**Three-sentence justification.** MODIS and VIIRS count fires at very different rates, and the number of satellites changed five times, so adding hotspots up makes recent years look busier than they were. We count hotspots per satellite, and convert the older MODIS record into VIIRS units with one factor measured on 14 years when both flew. Each month is then ranked against the same month in other years, so the calendar shows relative activity, not hectares.

## How well it works

Whole box, k fitted leaving out the year being predicted, comparing the index built from MODIS alone with the index built from VIIRS alone over 2012-02 to 2025-12.

| Measure | All months | June–September |
|---|---|---|
| Typical monthly error | about 1.4× | about 1.2× |
| Months within a factor of 1.5 | 55% | 67–69% |
| Months within a factor of 2 | 79% | 84–87% |
| Rank correlation (Spearman) | 0.95 | 0.99 (re-checked, k fitted on all years) |
| Percentile class: same class | 60–62% | – |
| Percentile class: within one class | 93–94% | – |

- **Quote the error as "within a factor of 2".** A ×/÷1.5 band covers only about half of months.
- **Quote k with its yearly range, 6.2 to 10.5.** A bootstrap interval (8.24–8.93) is far too narrow to be honest. k was 8.33 for 2012–2019 and 9.00 for 2020–2025.
- **k depends on the filters.** Without the confidence filter it is 8.27. In raw-count terms the same relationship is Suomi NPP : (Terra + Aqua) = 4.15, Suomi NPP : Aqua = 8.89, Suomi NPP : Terra = 7.78.
- **For the Terra-only months** a Terra-specific factor of 8.20 was fitted.
- **It checks out against known fires.** Top years are 2021, 2017, 2023, 2018 and 2003. The top month is July 2021. September 2003, June–August 2021 and summer 2023 rank as records or well above normal. Summer 2026 (June–September) ranks 2nd of 26 years, but August onward rests on near-real-time data.

### Limits that should be stated

- **A simpler baseline scores the same.** MODIS × 4.15 spliced with Suomi NPP counts alone matched or slightly beat this method on agreement (typical error 0.44 against 0.48 in log2 units). The per-satellite method is preferred for other reasons: it still works after Suomi NPP ended on 2 November 2026, it handles outages, and a fourth VIIRS satellite needs only a table entry. Justify it on continuity, not accuracy.
- **Quiet months run low before 2012.** In the typical month the VIIRS-based value is about 1.16× the MODIS-based one. In June–September the bias is slightly the other way (re-checked: −0.12 in log2 units). The gap comes from quiet months, where VIIRS sees small fires that MODIS misses. Other ways of fitting k do not fix it: the median of monthly ratios gives 9.57, months with 30 or more MODIS hotspots give 8.49, June–September alone 8.86.
- **Small areas are noisy.** Within 50 km of Kamloops the typical error is about 2×, 19% of months are tie-uncertain, and the MODIS-based index is zero in half of months. Within 25 km, 53% of months are uncertain. k fitted per area is close to the global one (8.65–9.64), so the cause is small counts, not k. Below about 50 km radius (8,000 km²) show ranks only, with a warning.
- **Near-real-time bias cannot be tested** with the cached data, so recent months stay provisional.

## What the evidence says

### Never sum the satellites

- The total of all sensors is 1.0× the MODIS total until January 2012, then 5.0× (2012–18), 9.3× (2018–23) and 13.8× (2023–25).
- With a naive sum, 59% of months since March 2023 land in the top fifth. With the per-satellite index it is 18–21%.
- FIRMS does not remove repeats between satellites, and each VIIRS satellite counts about the same: April 2023 to December 2025 gave Suomi NPP 49,121, NOAA-20 48,504 (0.99×) and NOAA-21 47,712 (0.97×).

### One factor is good enough for a relative calendar

- Per-calendar-month factors and log-log fits barely beat one pooled factor (typical error 0.32–0.47 in log2 units across all variants).
- The ratio is flat once a month has about 30 MODIS hotspots, and higher in near-empty months.
- It is the same across the four quadrants of the box (3.89–4.38 in Suomi NPP : MODIS terms).
- There is a weak upward trend (about +1.2% to +1.8% a year) and no visible step when the MODIS orbits began to drift.

### Alternatives that were tested and did not help

| Idea | Result |
|---|---|
| Grid cells × days instead of pixels | The VIIRS : MODIS ratio settles near 1.8 at 2 km and never reaches 1. It varies more from year to year than raw counts, and still grows 1.30× and 1.47× as satellites are added. |
| Summed fire radiative power | Noisier than counts (spread 0.45 against 0.27), and the ratio fell from 1.4–1.7 to 0.85–1.07 after 2021. |
| Regrouping VIIRS into 1 km "MODIS-like" pixels | Worse: about 30–35% typical error in fire months against about 20% for raw counts. |
| Keeping only near-nadir detections | Discards 43% of rows and does not steady the ratio. |
| Separate day and night factors | Aqua's night ratio swings from 16 to 98 by year. |
| Fire-days or fire events as the unit | Fire-days saturate in peak season (correlation 0.84 against 0.999 for counts). The event threshold was tuned on the same data. |
| Bootstrap uncertainty on each calendar cell | Classes barely depend on k, so almost nothing is flagged. |

### What MODIS cannot see

- 62% of VIIRS fire events have no MODIS counterpart, but they are tiny (median 2 hotspots, 1 day) and hold about 6% of VIIRS hotspots.
- By season, the share of VIIRS hotspots with no MODIS hotspot nearby is 1–5% in June–September, 20–33% in October–November and 49–66% in December–April.
- December–April counts jump 5 to 8 times between the MODIS-only years and the VIIRS years.
- So summer is comparable across the whole record, and the off-season before 2012 is not. Two workable options: rank October–April months against 2012 onward only, or flag them as reduced comparability.
- The likely cause is small pile and agricultural burning. That is an inference from season and fire size, not a mapped fact.

### Filters

- **One static source matters.** The site at 50.68872, −120.40745 has 921 VIIRS rows, all at night, about 1 MW, and no MODIS detections. In quiet years it is roughly 55–80% of VIIRS hotspots within 25 km of Kamloops. 58 of its rows are near-real-time and carry no `type`, so a `type` filter alone misses them. It is likely the pulp mill at 2005 Mission Flats Road, 0.4 km from the site, though no source confirms it; see [harmonization-tests.md](harmonization-tests.md#static-and-recurring-sources).
- **Do not filter on `type = 0` alone.** That drops every near-real-time row (all of August 2026 onward) and 2,062 `type` 3 rows, 94% of which fall on heavy fire days.
- **The confidence filter is hygiene.** It removes 8.7% of MODIS and 3.7% of VIIRS rows and moves the ratio by about 5%. VIIRS `l` is a daytime-only class, and VIIRS `h` means a saturated pixel (5% of rows), not higher quality.
- **The data are otherwise clean.** There are no exact duplicate rows, and 0.22% of rows have `frp` = 0.

### Timing, gaps and drift

- **Orbit drift shows from 2023.** Terra's daytime detections moved from about 11.1–11.4 h local solar time to 10.06 h in 2025, and Aqua's from 12.8–13.1 h to 14.25 h. VIIRS stayed at 12.7–13.0 h. NASA says the effect on fire products is under investigation, so flag it and do not correct it.
- **Outages visible in the data:** Suomi NPP has no detections from 27 July to 10 August 2022, and Terra has a gap on 12–20 October 2022. Other documented outages cannot be seen in this box.
- **Suomi NPP ended on 2 November 2026.** NOAA-20 is the natural reference afterwards.

### Time step

- **Monthly is the finest step that holds up.** Weekly classes from the two sensors agree 70% of the time for the whole box and 34% within 50 km of Kamloops.
- **Daily values are indicative only (re-checked).** MODIS × k and VIIRS agree within a factor of 2 on 52% of days (62% in June–September). On 48% of days with VIIRS hotspots, MODIS has none. In busy months the top three days hold about 43% of the month's hotspots.
- The VIIRS satellites agree better with each other day to day: Suomi NPP and NOAA-20 are within a factor of 2 on 83% of days.
- NASA's MODIS guide (section 8.4.1) warns of "severe temporal and spatial biases" for intervals shorter than about eight days.

## What the literature adds

- **No published conversion was found** between MODIS and VIIRS 375 m hotspot counts. The factor has to be derived from the overlap and justified.
- **Published long records scale a derived quantity over the overlap years**, per region or biome: GFED5 uses per-region scalars from 2012–2022, and QFED regresses fire power against Aqua. FINN v2.5 applies no factor and gives each detection its own footprint (0.14 km² for VIIRS, 1 km² for MODIS).
- **A ratio of overlap-period means has precedent.** A 2025 AVHRR/MODIS/VIIRS vegetation-index record used it and rejected quantile normalization because it reduced variability and trend consistency.
- **MODIS sensitivity falls across its swath.** One 2026 study puts the smallest detectable fire at about 4.1 MW at nadir and over 33.6 MW at the swath edge, against 1.4 to 2.2 MW for VIIRS. The sensors agree for intense fires and differ mostly for small ones.
- **NASA's designed continuity product is the VIIRS 750 m one**, a replica of the MODIS algorithm. It is not what the FIRMS 375 m files contain.

### Cite with care

- Schroeder 2014's "3× by day and 25× at night" compares VIIRS 375 m with VIIRS 750 m, not with MODIS.
- The Punjab "4.8×" figure compares different periods and was not opened.
- Fu 2020 and Li 2018 were seen as abstracts only.
- The "not advisable" wording attributed to Giglio 2025 was not confirmed. The safe wording is that its authors expect regional statistical calibration to be needed.
- The Global Fire Atlas and FIRED event methods are single-sensor and tuned on burned-area data elsewhere.

## Judging notes

- Five criteria, each scored 1 to 5: impact, creativity, validity, relevance, presentation. Validity is "scientific soundness, technical feasibility, and usability".
- The demo is a video of at most 30 seconds or at most 7 slides. Going over makes the project ineligible for global judging.
- One validity figure does most of the work: MODIS-based against VIIRS-based monthly index over the overlap, with the ratio and its range, beside the naive-sum staircase.
- The submission form has an AI-use field. Confirm its wording in a browser; the guides were read through a proxy.

## Sources

Opened and confirmed by a second reader unless noted.

| Source | Used for |
|---|---|
| [Zheng et al. 2026](https://mdpi-res.com/d_attachment/remotesensing/remotesensing-18-01650/article_deploy/remotesensing-18-01650.pdf) | MODIS and VIIRS detection limits across the swath |
| [Schroeder et al. 2014](https://directreadout.sci.gsfc.nasa.gov/publications_documents/Schroeder_et_al_2014b_RSE.pdf) | VIIRS 375 m sensitivity and commission errors |
| [Loboda et al. 2017](https://drum.lib.umd.edu/handle/1903/20226) | MODIS and VIIRS coverage of large boreal fires ("initial results") |
| [GFED5 near-real-time, ESSD 2026](https://essd.copernicus.org/articles/18/7535/2026/) | Per-region scaling over the 2012–2022 overlap |
| [FINN v2.5, GMD 2023](https://gmd.copernicus.org/articles/16/3873/2023/) | Combining sensors by footprint with no factor |
| [QFED slides, CEOS](https://ceos.org/document_management/Virtual_Constellations/AC-VC/Meetings/AC-VC-22/Presentations/AC-VC_5.17_Collow_version1.pdf) | Aqua fire power runs lower than VIIRS |
| [NASA VIIRS fire products](https://viirsland.gsfc.nasa.gov/Products/NASA/FireESDR.html) | The 750 m product as the MODIS-continuity product |
| [Iberian NDVI record, ESSD 2025](https://essd.copernicus.org/articles/17/5885/2025/) | Ratio of overlap means as accepted practice |
| [NASA note on Terra and Aqua drift](https://landweb.modaps.eosdis.nasa.gov/displayissue?id=1254) | Drift effects "under active investigation" |
| [MODIS fire user guide](https://earthdata.nasa.gov/s3fs-public/2023-09/MODIS_C6_C6.1_Fire_User_Guide_1.0.pdf) | Sections 4.4–4.5 (near-real-time), 8.4.1 (eight-day warning), 8.4.2 (confidence) |
| [FIRMS static-source mask note](https://wiki.earthdata.nasa.gov/spaces/FIRMS/blog/2025/2) | Masking static sources by location |
| [Space Apps judging guide](https://www.spaceappschallenge.org/resources/judging-awards-guide) and [submission guide](https://www.spaceappschallenge.org/resources/project-submission-guide/) | Criteria and demo limits (read through a proxy) |
| [2021](https://en.wikipedia.org/wiki/2021_British_Columbia_wildfires) and [2003](https://en.wikipedia.org/wiki/2003_Okanagan_Mountain_Park_Fire) BC wildfire pages | Dates and sizes of the fires used as sanity checks |

## Not done

- No comparison with burned area. BC Wildfire Service perimeters and Canada's NBAC are free, but were not downloaded.
- The effect of orbit drift on counts is not quantified.
- Nothing here was tested outside this box.
- A pandas prototype of the method (about 190 lines) and its test script exist outside the repository. They are not committed.
