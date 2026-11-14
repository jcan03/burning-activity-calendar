# Harmonization evidence: what the Interior BC data and the literature show

Team reference for City of Kamloops & Co. It gathers the evidence needed to choose how to combine MODIS and VIIRS hotspots: measurements from the team's own FIRMS data, what published studies and operational fire systems do, a check against British Columbia's fire records, and what the challenge material requires. It sets out what the evidence supports for each choice. It does not make the choice.

Compiled 2026-11-14. Ten questions were answered from the data by an analyst and then re-run and independently recomputed by a reviewer. Three outside-evidence topics were researched and then verified against their sources. One pass extracted requirements from the challenge material, and a final pass reconciled numbers that differed between topics. The fifteen working files are in [harmonization-evidence-research/](harmonization-evidence-research/). Sensor facts are in [sensor-reference.md](sensor-reference.md).

**Later tests.** Tests run after this document was first compiled are reported in [harmonization-tests.md](harmonization-tests.md). They changed several statements here. Each correction is made in place and listed, with its date and source, under [Changes since first compiled](#changes-since-first-compiled).

**The team's recommended method.** A separate piece of work on the same day produced [harmonization-research.md](harmonization-research.md), which recommends a method, and `harmonize.py`, which implements an interim version of it. How the results here bear on that method is set out in [harmonization-tests.md](harmonization-tests.md#how-this-relates-to-the-teams-recommended-method).

**The data.** Every FIRMS hotspot from 1 November 2000 to 14 November 2026 in the box 49.0–52.5°N, 122.5–118.0°W: 737,244 rows from Terra, Aqua, Suomi NPP, NOAA-20 and NOAA-21. The box is about 390 km by 320 km, centred near Kamloops.

**Terms used throughout.**

- **Ratio** means MODIS count divided by VIIRS count, as a ratio of sums over the months named, unless stated otherwise.
- **Stable-orbit period** means February 2012 to December 2021, when Terra and Aqua held their overpass times and Suomi NPP was flying. **Drift period** means January 2022 onward.
- **Fire season** means April to October.
- **Active cell-day** means one grid cell on one local date with at least one hotspot.
- Intervals in brackets are 95% intervals from resampling whole years.

## At a glance

1. **Suomi NPP records about 4.1 hotspots for every Terra-plus-Aqua hotspot** in this box (ratio 0.242, interval 0.237–0.28). The ratio is 0.34 by day and 0.18 at night.
2. **A single month scatters widely around that ratio.** One factor predicts a monthly MODIS count from VIIRS with a median error of about 14% in the largest fire months, 23% in moderate ones and 30–33% over all fire-season months.
3. **The three VIIRS satellites are interchangeable for counts.** NOAA-20 runs at 0.99 of Suomi NPP and NOAA-21 at 0.97. Even so, two identical instruments differ by ±15–20% in a single month, which sets a floor on what any method can resolve.
4. **Counting active grid cells narrows the gap in level more than in scatter.** At 2 km the ratio rises from 0.24 to 0.65. The year-to-year spread halves only for daytime cells. For a single month the gain is modest.
5. **Each sensor ranks months almost identically against its own history** (rank correlation 0.97), but they give the same five-class label in only 68–69% of fire-season months (71% in the first compilation; see [Changes since first compiled](#changes-since-first-compiled)), and less often still in near-normal months (44% on the first definition).
6. **The orbit drift is established only for 2026, and in counts mainly for Terra by day.** Terra's daytime count is at about half its expected level in 2026 (0.41–0.61 across five methods), and British Columbia's provisional 2026 fire records confirm that loss. A gradual decline in 2022 to 2025 is weak evidence: the raw ratio to NOAA-20 shows none. The day-plus-night MODIS total held through 2025 and sits at the bottom of its range in 2026.
7. **Small areas are the hardest problem.** Below about a 50 km radius, MODIS records nothing in a third or more of the months in which VIIRS saw fire, and no harmonization can restore those detections.
8. **One static heat source near Kamloops adds a constant to VIIRS only.** It contributes about 2.6 Suomi NPP hotspots a month, always at night, and MODIS has never detected it. It is likely the pulp mill at Mission Flats.
9. **Fire radiative power is not a better bridge than counts.** It is worse whenever night passes are included.
10. **Scan-angle filters and broad static-source filters are not worth their cost** for a monthly calendar.
11. **No published study or operational system joins raw MODIS and VIIRS hotspot counts into one series,** and none gives a count ratio for Canadian forest. Practice in fire radiative power and burned area uses factors fitted over an overlap period, split by day and night or by region.
12. **BC's own fire records do not favour either sensor.** Every sensor ranks years by area burned about equally well (rank correlation 0.84–0.89).
13. **The challenge leaves the method open** but requires that it be justified, that it continue through NOAA-20 and NOAA-21, and that any use of AI tools be declared.

## Reconciled numbers

Where topic files gave different values, the cross-check recomputed them. These are the values to use. Detail: [_cross-check.md](harmonization-evidence-research/_cross-check.md).

| Quantity | Value | Computed from |
|---|---|---|
| Terra+Aqua / Suomi NPP, all hours | 0.242 (0.237–0.28) | 116 months, stable-orbit period |
| Range of that ratio across fire seasons | 0.20–0.41 | 10 years, with 2020 (the Aqua outage year) kept |
| Terra+Aqua / Suomi NPP, day | 0.34 (0.32–0.41) | Same |
| Terra+Aqua / Suomi NPP, night | 0.18 (0.12–0.19) | Same |
| Aqua / Suomi NPP, all hours | 0.113 (0.109–0.130) | 117 months |
| Aqua / Suomi NPP, day and night | 0.20 and 0.055 | Same |
| Terra / Aqua, day and night | 0.72 and 2.2 | 2003–2021 |
| NOAA-20 / Suomi NPP | 0.99 (0.94–1.02) | April 2018 – July 2026 |
| NOAA-21 / Suomi NPP | 0.97 overall, 0.92 by day | 2023–2026, four seasons |
| Single-month scatter between two VIIRS satellites | ±15–20% | 10th–90th percentile 0.80–1.19 |
| Terra+Aqua / Suomi NPP in 2 km active cell-days | 0.65 all hours, 0.68 by day | 68 fire-season months |
| Sum of two, then three, VIIRS satellites against one | 1.99 and 2.95 times | 2018 onward; 2023 onward |
| Union of 5 km cell-days from two, then three, satellites | 1.24 and 1.37 times | Same |

## What the evidence says for each choice

### Target record: MODIS-equivalent or VIIRS-equivalent

Detail: [m01](harmonization-evidence-research/m01-ratio-stability.md), [m03](harmonization-evidence-research/m03-like-for-like-pairs.md), [m08](harmonization-evidence-research/m08-spatial-scale.md), [r01](harmonization-evidence-research/r01-published-methods.md), [r02](harmonization-evidence-research/r02-operational-systems.md).

| Consideration | Evidence |
|---|---|
| Size of the conversion | The same factor serves both directions. Converting VIIRS down to MODIS-equivalent discards about three quarters of the hotspots. Converting MODIS up multiplies Aqua counts by about 5 by day and about 18 at night. |
| Missing detections | For circles of 10–100 km radius, MODIS records nothing in 16–50% of the months in which Suomi NPP saw fire. Neither direction can restore them. |
| Stability over time | VIIRS overpass times stayed constant on all three satellites (about 12:40 and 02:10 local solar time). MODIS times have moved two hours. A VIIRS-equivalent record needs no model of future MODIS drift. |
| After MODIS ends | A MODIS-equivalent record would have to be produced from VIIRS alone after 2027. |
| Independent check | Area burned does not favour either sensor. |
| Precedent | Split. Studies that correct fire radiative power pixel by pixel use VIIRS as the reference. Long-running emissions systems kept a MODIS-era reference and are now moving to VIIRS (NASA's QFED is moving its anchor to NOAA-20). |
| Challenge author | "Either alternative is fine if properly justified." |

**Strength of evidence.** The size of the conversion is well measured (about ±10%). The case for either direction rests on continuity and drift arguments, not on a measured difference in accuracy.

### Unit: counts, active cells, fire radiative power or anomalies

Detail: [m02](harmonization-evidence-research/m02-grid-units.md), [m05](harmonization-evidence-research/m05-anomaly-agreement.md), [m06](harmonization-evidence-research/m06-scan-angle.md), [m10](harmonization-evidence-research/m10-frp-as-unit.md).

| Unit | For | Against |
|---|---|---|
| Raw hotspot counts | Matches the challenge wording ("number of hotspots"). One factor of 0.242 holds in the three biggest fire years (0.234–0.244). | Monthly error of about 14–30% depending on month size. Carries MODIS scan-overlap duplicates: 21–23% of hotspots have a neighbour from the same pass within half a pixel. |
| Active cell-days (2 km) | Brings the sensors much closer in level (0.65). By day the factor is steady across years (range 0.62–0.85) and does not depend on activity. Removes overlap duplicates without discarding data. Grid size between 1 and 5 km makes little difference. | For single months the gain is small: median error about 20% against 24–29% for counts, with overlapping intervals. Compresses large months (62,646 hotspots become 8,053 cell-days). At night the ratio swings eightfold with activity. |
| Fire radiative power | By day, Aqua and Suomi NPP are already on the same scale (ratio 1.01). | Worse than counts in 99% of resamples when night is included. Not mentioned in the challenge. NOAA-21 runs 12–18% above NOAA-20 per hotspot. |
| Each sensor against its own history | No cross-sensor factor needed when a month and its baseline come from the same sensor. Month order is preserved (rank correlation 0.97). The sensors are never more than one class apart in 98% of months. | Exact class agrees in 68–69% of fire-season months (71% in the first compilation) and in 44% of near-normal ones on the first definition. Over the 28 months that either sensor calls near normal (0.5 to 2 times the median), the later tests find the five classes agree in 21%. A baseline before 2012 still needs MODIS, so current VIIRS months still need a bridge. Changing the baseline years changes 8–21% of labels, about as much as changing the sensor. |

No published study or operational system tests active cells or per-sensor anomalies for this purpose. The literature is silent on them, not negative.

**Strength of evidence.** Strong that counts beat fire radiative power. Moderate that daytime cell-days beat counts over a season, weak for a single month. Moderate for anomaly agreement at the scale of the whole box, weak below 100 km.

### Scaling: one factor, split factors or a curve

Detail: [m01](harmonization-evidence-research/m01-ratio-stability.md), [m03](harmonization-evidence-research/m03-like-for-like-pairs.md), [m07](harmonization-evidence-research/m07-filter-sensitivity.md).

| Form | Evidence |
|---|---|
| One factor | Defensible for large months and for season totals (about 10% error on a season). |
| Separate day and night factors | The two clearly differ (0.34 against 0.18). Splitting gave no measurable gain in monthly accuracy for the whole box. Its value is in avoiding bias when a month's day-to-night mix differs from the baseline, as in a small area, a quiet month, or near-real-time rows. The night factor is unstable from year to year. **Later result:** in class terms the split matches one factor in the fire season (83% against 84% agreement with the all-VIIRS class) and is 7 points worse over all months (73% against 80%), because the night factor is seasonal. It is 0.18–0.19 in July and August but 0.03–0.12 in March to May and September to December, so one pooled night factor of 0.177 converts quiet-month MODIS counts too low. Single-month error in the fire season was 4–5 points lower with the split in three computations, but every interval overlapped. A follow-up test found that a night factor fitted separately for June to August is still 4.7 points worse than one factor over all months, and that day and night factors used only in April to October are level with one factor over all months (−1.3 points, −2.9 to +0.4) and remove its fire-season bias, though a loss of a few points cannot be ruled out. Detail: [harmonization-tests.md](harmonization-tests.md#does-a-converted-record-give-the-right-class), [Refinements of the factor](harmonization-tests.md#refinements-of-the-factor). |
| A factor per calendar month | Weak. The only gain appeared when winter months were included. Each factor rests on 9 or 10 months, and June's flips from 0.30 to 0.52 depending on whether months are keyed by UTC or local date. No operational system uses seasonal factors. |
| A fitted curve | Not supported. Fitted slopes are close to 1, and a power law did not beat one factor out of sample. Quiet fire-season months do run 25–50% above busy ones, but that is smaller than the month-to-month scatter. |
| Scan-angle filter or weighting | Not supported. Keeping only near-nadir pixels discards 27–37% of hotspots and does not reduce the monthly spread. |

Whatever the form, an additive source such as the Kamloops static site has to be removed first, because no scale factor can remove a constant.

**Strength of evidence.** Strong that the relationship is multiplicative and close to linear. Moderate that the day and night ratios differ, but weak that splitting improves monthly accuracy: the later tests find it level with one factor in the fire season and worse over all months. Weak for seasonal factors and curves.

### Combining two or three VIIRS satellites

Detail: [m09](harmonization-evidence-research/m09-overpass-and-multi-viirs.md), [m03](harmonization-evidence-research/m03-like-for-like-pairs.md).

| Rule | Behaviour |
|---|---|
| Sum the satellites | Doubles, then triples, the count at April 2018 and March 2023, and adds the static source once per satellite. |
| Union of active cells | Steps up by 1.24 and then 1.37 times at the same dates, and by more in quiet years. |
| Monthly mean, including a satellite with an outage | About 30% too low in real outage months (July and August 2022). |
| Maximum across satellites | Biased upward, by more with each added satellite. |
| One reference satellite with a monthly fallback | Errs by 6–12% in fallback months. |
| Daily mean of the satellites that have data, each scaled to Suomi NPP, then summed over the month | Departs from a complete month by under 1% in the median, and by 1.5–11% at worst in simulated outages. |

- The scale factors to Suomi NPP are 1.011 for NOAA-20 and 1.034 for NOAA-21, from dropping whole months with outages. Re-estimated with outage days masked one by one, they are 1.0245 (1.014–1.047) and 1.0503 (1.030–1.083). Detail: [Availability flag and the combined VIIRS series](harmonization-tests.md#availability-flag-and-the-combined-viirs-series).
- The daily-mean rule needs a per-day availability flag. The published outage list is not enough: on several listed Suomi NPP gap days in 2026 the satellite still recorded thousands of hotspots.
- **A flag can be built from NASA's open granule catalogue.** The catalogue lists every MODIS and VIIRS scene over the box, including passes that found no fire (124,636 scenes for the five sensors, no login). Compared day by day with the team's rows, it found Suomi NPP gaps missing from the outage list (30 May to 3 June, 10 to 15 July and 24 to 28 July 2024), Terra gaps (13 to 15 May 2025, 5 to 10 March 2026) and NOAA-21 gaps (10 to 14 January 2026). These dates are UTC days; by local date the Terra gaps are 12 to 15 May 2025 and 4 to 9 March 2026. It also contradicts four listed gaps: Suomi NPP has scenes and hotspots on 11 to 20 August 2022, Suomi NPP has scenes on 3 of the 5 listed days of 2 to 6 November 2024, and Terra has scenes on 15 April 2001 and on 26 and 27 March 2026. A check of daily counts against the other VIIRS satellites found a loss the catalogue cannot see: NOAA-20 recorded no hotspots on 19 to 22 July 2023 with normal scenes. The unlisted 2024 gaps explain a dip in the fire-season ratio of Suomi NPP to NOAA-20, which was 0.88 with every day kept and 0.99 after dropping the days with no scene. No other year from 2018 to 2025 moves by more than 0.001 when whole UTC days are dropped. A follow-up that masked days by local date and also masked the NOAA-20 loss of July 2023 gives 0.994 for 2024 and 1.028 for 2023 (1.064 unmasked), and a yearly range of 0.93 to 1.07. Detail: [w03](harmonization-tests-research/w03-data-availability.md), [_cross-check.md](harmonization-tests-research/_cross-check.md), [f03](harmonization-tests-research/f03-availability-flag.md).
- **Limits of that flag.** It records scenes, not data quality. It shows a missing day or night pass as a half-day loss, but it cannot see a loss inside a scene: Aqua's failure of 16 August to 2 September 2020 still shows normal scenes. A count check against the other VIIRS satellites finds such a loss only when it is large and the fire is busy. Its catalogue of science-quality scenes misses days on which FIRMS has near-real-time rows (Suomi NPP, 4 and 5 August 2026 by UTC date). It lists only 14 NOAA-20 scenes over the box between 1 April and 4 June 2018, although FIRMS has NOAA-20 rows from 1 April 2018. The near-real-time catalogue keeps only about 7 days, so the current month may lack a flag.
- **Re-done with the flag.** A follow-up applied the flag day by day. The combined daily-mean series stays level through every real outage month and at each change in the number of satellites (0.980 of Suomi NPP alone in April to October 2018, 1.008 in March to October 2023). Against it, a plain monthly mean is 34% low in July 2022 and 28% low in August 2022, in line with the figure of about 30% above. Detail: [Availability flag and the combined VIIRS series](harmonization-tests.md#availability-flag-and-the-combined-viirs-series).
- GFED5NRT and NOAA's GBBEPx both process each satellite separately and then average, falling back to whichever is available.
- November 2026 goes from three satellites to two on 2 November.

**Strength of evidence.** Strong. This is the best-supported choice of the five.

### MODIS data since 2022

Detail: [m04](harmonization-evidence-research/m04-drift-effect.md), [r03](harmonization-evidence-research/r03-bc-fire-record.md).

Median local solar time of fire-season hotspots in the box:

| | 2012–2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|---|
| Terra, day | 11:04–11:22 | 11:04 | 10:44 | 10:32 | 10:04 | 09:20 |
| Aqua, day | 12:47–13:03 | 13:04 | 13:09 | 13:31 | 14:15 | 14:51 |
| VIIRS, day (all three) | 12:36–13:00 | unchanged | | | | |

Fire-season ratios against NOAA-20:

| Series | Range in 2018–2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|---|
| Terra, day | 0.127–0.212 | 0.148 | 0.145 | 0.131 | 0.136 | **0.070** |
| Terra+Aqua, day | 0.318–0.462 | 0.384 | 0.371 | 0.366 | 0.408 | **0.254** |
| Terra+Aqua, night | 0.036–0.192 | **0.194** | 0.184 | 0.170 | 0.176 | 0.178 |
| Terra+Aqua, all hours | 0.205–0.304 | 0.260 | 0.240 | 0.229 | 0.252 | **0.203** |
| Terra+Aqua, daytime 2 km cell-days | 0.657–0.762 | 0.742 | 0.753 | 0.730 | **0.790** | **0.626** |

Bold marks a value outside the earlier range. That range covers only four years, so a value just outside it (0.194, 0.790, 0.203) is weak evidence. The 2026 daytime values are far outside it.

- **Only 2026 is established for Terra by day.** Its raw daytime ratio to NOAA-20, relative to the pooled 2018 to 2021 value of 0.138, is 1.07, 1.05, 0.95, 0.98 and 0.51 in 2022 to 2026. The years 2018 to 2021 alone span 0.92 to 1.53 on that scale, so 2022 to 2025 lie inside the earlier range and show no decline. Five methods that differ in size model and VIIRS reference put the 2026 level at 0.41 to 0.61 of normal (about half).
- **The gradual decline appears only after a size adjustment.** Allowing for the size of each fire year with a model fitted on 2012 to 2021, Terra's daytime count was 0.95, 0.81, 0.77, 0.70 and 0.46 of its expected value in 2022 to 2026 (0.91, 0.87, 0.81, 0.71 and 0.50 in a later computation). The later test warns that this adjustment fits small years poorly (stable small years scatter between 0.6 and 1.6), and its 2022 to 2025 contrast (0.87) equals its own placebo contrast (0.87) for 2020 and 2021 against 2018 and 2019. The gradual decline is therefore weak evidence.
- **The day-plus-night total held through 2025,** partly because Terra's day counts fell while its night counts rose. Nothing guarantees that cancellation continues. A control chart on the all-hours Terra-plus-Aqua ratio never signalled; one on Terra's daytime ratio signalled in September 2025.
- **Every daytime-only series is out of range in 2026,** including daytime active cells.
- **Aqua and both night passes show no clear count effect through 2025.** In 2026 Aqua's night pass, now near dawn, is at 0.70 (0.60 to 0.82) of normal.
- **BC's fire records show no loss specific to MODIS in 2022–2025.** Hotspots per square kilometre burned fell about 10% for MODIS and VIIRS alike.
- **BC's provisional 2026 fire records confirm the 2026 loss.** The current-season layer puts 2026 second of 27 years for area burned in the box (645 incidents, about 410,000 ha, behind 2021). Measured against that area, Terra's daytime yield in 2026 is 0.41 to 0.45 of its 2021 and 2023 levels, while NOAA-20's is 0.74 to 0.93. Final 2026 records are due in April 2027. Detail: [a09](harmonization-tests-research/a09-drift-curve.md), [a10](harmonization-tests-research/a10-diagnostics.md), [w03](harmonization-tests-research/w03-data-availability.md).
- **Operational systems avoid fitting on drift years.** GFED5 stops in 2022 for this reason, and QFED says "Terra is increasingly underestimating fire activity".

**Strength of evidence.** Strong for Terra by day in 2026, now confirmed independently by BC's provisional fire records. Weak for a gradual decline in 2023–2025 (rated moderate in the first compilation). Weak, with only four years, for "no effect" on Aqua and on the combined total.

## Findings that apply whatever is chosen

### Area size

Detail: [m08](harmonization-evidence-research/m08-spatial-scale.md). Values are medians over 31 circles of each radius, for the stable-orbit period, comparing Terra plus Aqua with Suomi NPP.

| Radius | Fire-season months with no hotspot from either sensor | Months MODIS missed, of those where VIIRS saw fire | Months per year with at least 10 MODIS hotspots |
|---|---|---|---|
| 10 km | 91% | 50% | 0.1 |
| 25 km | 69% | 36% | 0.8 |
| 50 km | 27% | 33% | 2.5 |
| 100 km | 3% | 16% | 4.5 |
| 150 km | 0% | 6% | 6.3 |

Count scaling is marginal at 50 km and usable from about 100 km. A class against the monthly median can be computed for every fire-season month only from about 100 km, because the MODIS median is zero for most months below that. The data support several fallbacks for smaller areas: the anomaly of an enclosing larger area, a season in place of a month, presence or absence only, or the VIIRS-only record from 2012.

### Other findings

- **Month boundaries.** Terra's evening pass falls after midnight UTC. Keying months by UTC date moved 455 MODIS hotspots from 30 June 2021 into July. Keying by local date avoids this.
- **The Kamloops static source.** A fixed night-time heat source near 50.69°N, 120.41°W, about 6 km from Kamloops, accounts for 921 VIIRS rows and no MODIS rows in 26 years. FIRMS labels it a static source only from 2015. It is up to 17% of the VIIRS count in a quiet fire-season month, and it dominates a 10 km circle around Kamloops. It is likely the Kruger pulp mill at 2005 Mission Flats Road, whose location in Canada's pollutant registry is 0.4 km away; no source confirms this. See [Static and recurring sources](harmonization-tests.md#static-and-recurring-sources). Detail: [m07](harmonization-evidence-research/m07-filter-sensitivity.md).
- **Filters.** Keeping only `type` 0 changes almost nothing and would remove real lakeshore fire pixels. A broad persistent-location mask removes real burning, including November pile burns. Dropping low-confidence rows moves the day and night ratios in opposite directions, so it has to be applied the same way across the whole record.
- **November burns.** November has at least 10 MODIS hotspots in 9 or 10 of 10 years at 50–100 km, outside the usual fire season.
- **Near-real-time rows.** They have no `type`. The delivered day and night label matches one rule, "night when the sun is more than 85 degrees from vertical", for every one of the 737,244 rows, standard and near-real-time, on all five sensors. No near-real-time row lies between 83.6 and 96.5 degrees of sun angle, the range where the 85-degree rule and an orbit-direction rule would disagree, so the data cannot yet tell the two rules apart. The choice changes no count in August to October 2026 and no July 2026 class. Detail: [a06](harmonization-tests-research/a06-daynight-rule.md).
- **Looks per day.** On busy days each VIIRS satellite detects fire in about two daytime and two night-time passes over the box, and each MODIS in about 1.3 and 1. Summed over the satellites flying, that is about 2 detecting passes a day with Terra alone, 5 with Aqua, 8 with Suomi NPP, 13 with NOAA-20 and 16 with NOAA-21.

## What others have done

Detail: [r01](harmonization-evidence-research/r01-published-methods.md), [r02](harmonization-evidence-research/r02-operational-systems.md).

| Source | What it did | Result |
|---|---|---|
| [Csiszar et al. 2014](https://directreadout.sci.gsfc.nasa.gov/publications_documents/Csiszar_et_al_2014_JGR.pdf) | VIIRS 750 m against Aqua MODIS counts, global | VIIRS 26% higher near nadir, 70% higher off nadir |
| [Vadrevu and Lasko 2018](https://pmc.ncbi.nlm.nih.gov/articles/PMC6108185/) | VIIRS 375 m against Terra+Aqua counts, Punjab cropland | About 4.8 times |
| [Fu et al. 2020](https://api.crossref.org/works/10.3390/rs12182870) | Aqua against Suomi NPP at near-simultaneous passes, Northeast Asia | MODIS missed 65% of VIIRS fire pixels in forest and 83% on low-biomass land |
| [Li et al. 2018](https://repository.library.noaa.gov/view/noaa/49896) | Fire radiative power, MODIS against VIIRS | Comparable, except large boreal fires, where VIIRS is about 47% lower |
| [Li et al. 2020](https://repository.library.noaa.gov/view/noaa/42501/noaa_42501_DS1.pdf) | Fire radiative power by grid size and view angle, Africa | MODIS 14–50% lower, rising toward the swath edge |
| [Zheng et al. 2026](https://mdpi-res.com/d_attachment/remotesensing/remotesensing-18-01650/article_deploy/remotesensing-18-01650.pdf) | Corrects MODIS fire radiative power to VIIRS by view angle, global | Slope improves from 0.74 to 1.03 |
| [Chen et al. 2026 (GFED5NRT)](https://essd.copernicus.org/articles/18/7535/2026/) | Converts VIIRS counts to burned area, calibrated to a MODIS-based record over 2012–2022 | Up to 224 regional factors; averages Suomi NPP and NOAA-20 |
| [Copernicus GFAS](https://atmosphere.copernicus.eu/drifting-away-modis-cams-global-fire-assimilation-system) | Bias-corrects VIIRS fire radiative power to match the MODIS-only version | Development factors 1.23 by day, 0.46 at night |
| [FINN v2.5](https://gmd.copernicus.org/articles/16/3873/2023/gmd-16-3873-2023.html) | Gives each detection an area and merges overlapping footprints | No bias factor; "the identity of the sensor is not relevant" |
| NASA's gridded MODIS product | Corrects counts for the number of overpasses and for cloud | Needs the count of all pixels observed, which FIRMS rows lack |
| CWFIS, EFFIS, GWIS, Global Forest Watch | Display hotspots from several sensors | No harmonization |

Four families of approach are in use: a regression factor against a reference over an overlap period; converting detections to an area before combining; normalising by observation opportunity; and a switch date with a calibration overlap. None of the published factors applies to hotspot counts or to Interior BC without refitting.

## Check against British Columbia's fire records

Detail: [r03](harmonization-evidence-research/r03-bc-fire-record.md). Source: BC Wildfire Service historical fire incident locations (Open Government Licence – British Columbia), 30,028 dated incidents in the box for 2000–2025.

| Sensor | Years | Rank correlation of fire-season hotspots with area burned |
|---|---|---|
| Terra | 2001–2025 | 0.84 (0.60–0.96) |
| Aqua | 2003–2025 | 0.88 (0.68–0.97) |
| Suomi NPP | 2012–2025 | 0.89 (0.52–1.00) |
| NOAA-20 | 2018–2025 | 0.98 (0.73–1.00) |

- Hotspot counts grow more slowly than area burned (a tenfold larger year has about five times the hotspots), so small years have many hotspots per square kilometre.
- The ratio between sensors is much steadier than hotspots per square kilometre burned. Bridging the sensors through their overlap is better supported than calibrating each one to area burned.
- Only yearly comparisons are reliable. Area is recorded against the discovery date, and large fires burn for weeks.

## What the challenge material requires

Detail: [q01](harmonization-evidence-research/q01-requirements.md). Checked on 14 November 2026; the author had posted nothing new since 13 November.

| Topic | What the material says |
|---|---|
| Quantity shown | "A calendar of burning activity showing the number of hotspots detected", compared with "the historical median". Anomalies against multi-year averages are listed as optional. |
| How far back | "From the early 2000s to the present". |
| Target record | "Either alternative is fine if properly justified." |
| Continuity | The author wants solutions that "extend into the future", through NOAA-20 and NOAA-21. |
| Time step | Monthly "seems like a solid approach"; weekly "could be interesting, provided it is feasible". |
| Day and night, minimum area | Not mentioned. |
| Judging | Five criteria: Impact, Creativity, Validity, Relevance, Presentation. Validity asks for a project "grounded in scientific principles". One global award is "Best Use of Science". |
| Use of AI tools | The submission guide calls AI "SI". It says code and data "must acknowledge SI generation in descriptive text and metadata", and that SI should not be used to "come up with your idea of how to solve the challenge". |
| Demo | A video of 30 seconds or less, or up to seven slides. |

## Where the analyses disagreed

The cross-check found eight places where topic files drew different conclusions. The ones that bear on the choice:

| Question | Resolution |
|---|---|
| Do separate day and night factors help? | The factors differ, but splitting does not improve monthly accuracy for the whole box. The case for splitting rests on bias when the day-to-night mix changes, and on drift. The later tests add that in class terms the split matches one factor in the fire season and is 7 points worse over all months, because the night factor is seasonal. A follow-up found that no repaired split, seasonal night factor included, labels months better than one factor. |
| Are daytime active cells the stable unit? | True over a season. For a single month the gain is modest. |
| Should drift-period MODIS be kept as day plus night, or split? | The combined total held through 2025; every daytime series is out of range in 2026. Both readings are right for different years. |
| Is there precedent for the target? | Split, as described above. One topic file mislabelled GFED5NRT as VIIRS-referenced; it calibrates VIIRS to a MODIS-based record. |
| Does the ratio depend on activity? | Mildly. Quiet fire-season months run 25–50% above busy ones. The later tests measured it differently and found converted quiet fire-season months and small seasons about 15–27% above actual VIIRS counts (15% in a typical month, 23% in a calendar-month median, 27% in a small season). A follow-up found the opposite outside the fire season: a typical November-to-March month converts about a third low (0.66 times actual, 0.54–0.79). |

## What is still missing

Items marked "Answered" were tested after this document was first compiled; the answer and a link follow. Items marked "Open" remain.

1. **Partly answered.** A comparison of complete candidate methods on the same months, scored out of sample. On the whole box, a mixed baseline with MODIS years scaled by one factor gave the all-VIIRS class in 84% of fire-season months against 66% for a short VIIRS-only baseline, over 202 splits of the ten stable years. Day and night split factors, thinning and 2 km cell-days were scored on the same splits. See [harmonization-tests.md](harmonization-tests.md#does-a-converted-record-give-the-right-class). A follow-up tested a baseline of the real length: on the stable years a converted era of the real composition gives the right class in 87% of fire-season months, but on the real 24-year baseline 39% of box fire-season labels differ from a VIIRS-only baseline, against about 22% expected from the change of length alone. See [A baseline of the real length](harmonization-tests.md#a-baseline-of-the-real-length). Still open: whether that excess is real burning before 2012 or a conversion level that is too high.
2. **Partly answered.** Results at the area sizes a user would select. Counts scaled by one factor, random thinning and shrinking toward the box were scored on 31 circles at each of 25, 50, 100 and 150 km. Converted history is supported without qualification from about 100 km and is borderline at 50 km. See [harmonization-tests.md](harmonization-tests.md#user-sized-areas). Follow-ups scored split factors on 100 km circles (no better than one factor) and measured how often a change of VIIRS satellite changes a 100 km circle's label (14–23% of fire-season circle-months). Open: active cells at circle scale, and the combined VIIRS series as the current month inside the class test.
3. **Partly answered.** A direct calibration against MODIS. Fitted directly against NOAA-20 over April 2018 to December 2021 the factor is 0.242 (0.234–0.269, 43 months), the same as through Suomi NPP. See [harmonization-tests.md](harmonization-tests.md#is-the-factor-stable-and-where-can-it-be-trusted). Open: NOAA-21 against MODIS, which has no stable-orbit overlap.
4. **Partly answered.** An independent check of the 2026 Terra decline. BC's provisional 2026 records confirm it (Terra's daytime yield 0.41–0.45 of its 2021 and 2023 levels). See [harmonization-tests.md](harmonization-tests.md#the-orbit-drift). Open: the final 2026 records, due in April 2027.
5. **Answered, with limits.** A per-day availability flag for each satellite. NASA's open granule catalogue supplies one; it cannot see a loss inside a scene and keeps near-real-time scenes for only about 7 days. See [harmonization-tests.md](harmonization-tests.md#new-data-found). A follow-up applied it throughout and re-estimated the scale factors (1.0245 for NOAA-20 and 1.0503 for NOAA-21). See [Availability flag and the combined VIIRS series](harmonization-tests.md#availability-flag-and-the-combined-viirs-series). Open: the flag for the current month.
6. **Partly answered.** The effect of the near-real-time day and night rule on current-month counts. The delivered labels match the 85-degree rule and the rule changes no count in August to October 2026. See [harmonization-tests.md](harmonization-tests.md#the-day-and-night-label). Open: which rule the near-real-time rows follow, and whether they differ from standard rows in anything besides the label.
7. **Open.** Whether the Terra-only years (2000–2002) need separate treatment. Including them in a baseline changed 8% of fire-season labels. The later tests found 2001 and 2002 at or below the edge of the range expected from area burned, and did not test them further. See [harmonization-tests.md](harmonization-tests.md#is-the-factor-stable-and-where-can-it-be-trusted).
8. **Answered.** A screen for other static sources. Two independent searches found only the Kamloops site and two weak Suomi NPP-only sources that have not appeared since 2016. See [harmonization-tests.md](harmonization-tests.md#static-and-recurring-sources).

## Changes since first compiled

Each correction was made in place above, on 2026-11-14, from the later tests in [harmonization-tests.md](harmonization-tests.md) and its working files in [harmonization-tests-research/](harmonization-tests-research/). The reconciled values are in [_cross-check.md](harmonization-tests-research/_cross-check.md).

| Date | Statement | First compilation | Now | Source |
|---|---|---|---|---|
| 2026-11-14 | Same five-class label from each sensor's own history, fire-season months ("At a glance", the unit table) | 71% | 68–69%. The first figure included a month's own year in its baseline and keyed months by UTC date. The later tests leave the year out and key by local date. | [a11](harmonization-tests-research/a11-latent-models.md), [a01](harmonization-tests-research/a01-hindcast-box.md), [_cross-check.md](harmonization-tests-research/_cross-check.md) |
| 2026-11-14 | Strength of evidence for a gradual Terra daytime decline in 2023–2025 | Moderate | Weak. Only 2026 is established (about half of normal). The raw ratio to NOAA-20 shows no decline in 2022 to 2025. The decline appears only after a size adjustment that fits small years poorly. | [a09](harmonization-tests-research/a09-drift-curve.md), [a06](harmonization-tests-research/a06-daynight-rule.md), [_cross-check.md](harmonization-tests-research/_cross-check.md) |
| 2026-11-14 | Independent check of the 2026 Terra loss | None until April 2027 | BC's provisional 2026 records confirm it (yield 0.41–0.45 of the 2021 and 2023 levels). Final records still due in April 2027. | [w03](harmonization-tests-research/w03-data-availability.md) |
| 2026-11-14 | Day and night label of near-real-time rows | Assigned by orbit direction | Delivered labels match the 85-degree sun-angle rule for every row. The data cannot yet tell the rules apart. | [a06](harmonization-tests-research/a06-daynight-rule.md) |
| 2026-11-14 | Outage list and the availability flag for combining VIIRS satellites | Flag needed; list imperfect | Added that the open granule catalogue supplies a flag, with its limits. It showed the 2024 dip in the Suomi NPP to NOAA-20 ratio to be unlisted outage days (0.88 becomes 0.99). | [w03](harmonization-tests-research/w03-data-availability.md), [_cross-check.md](harmonization-tests-research/_cross-check.md) |
| 2026-11-14 | Day and night split | No measurable gain for the whole box | Added: matches one factor in the fire season and is 7 points worse over all months in class terms, because the night factor is seasonal. | [a01](harmonization-tests-research/a01-hindcast-box.md), [_cross-check.md](harmonization-tests-research/_cross-check.md) |
| 2026-11-14 | Range of the fire-season ratio across years | 0.19–0.40 | 0.20–0.41, with 2020 kept. The statement that the top is 2013 was dropped because it was not rechecked. | [_cross-check.md](harmonization-tests-research/_cross-check.md), [a07](harmonization-tests-research/a07-box-counting.md) |
| 2026-11-14 | Single-month error of one factor, fire season | About 30% | 30–33%, depending on direction of conversion and sensor set | [_cross-check.md](harmonization-tests-research/_cross-check.md) |
| 2026-11-14 | "What is still missing" | Eight open items | Each item marked answered, partly answered or open, with a link | [harmonization-tests.md](harmonization-tests.md#what-is-still-missing) |
| 2026-11-14 | Availability flag: listed gaps it contradicts, and its limits | Two listed gaps contradicted; "cannot see partial losses"; NOAA-20 scenes "only from June 2018"; "not yet re-done with the flag" | Four listed gaps contradicted, and a NOAA-20 loss inside scenes on 19–22 July 2023 added. The flag sees half-day losses but not a loss inside a scene. The catalogue lists 14 NOAA-20 scenes over the box between 1 April and 4 June 2018. The flag has now been applied day by day: masked scale factors 1.0245 and 1.0503, and a combined series that stays level through outages. | [f03](harmonization-tests-research/f03-availability-flag.md); catalogue files |
| 2026-11-14 | Day and night split; "Does the ratio depend on activity?" | No test of a seasonal night factor; converted quiet months run high | A seasonal night factor is still 4.7 points worse over all months, and no repaired split beats one factor. Converted quiet months run high only in the fire season; a typical November-to-March month is about a third low. | [f02](harmonization-tests-research/f02-factor-refinements.md) |
| 2026-11-14 | "What is still missing", items 1, 2 and 5 | Real-length baseline, split factors at circle scale, and the flag applied throughout listed as open | Answered by the follow-up tests, with what remains open stated | [f01](harmonization-tests-research/f01-real-length-baseline.md), [f02](harmonization-tests-research/f02-factor-refinements.md), [f03](harmonization-tests-research/f03-availability-flag.md) |
| 2026-11-14 | What the Kamloops static source is ("At a glance" point 8; "Other findings") | The facility was not identified | Likely the Kruger pulp mill at 2005 Mission Flats Road, 0.4 km from the source. This is the team's judgment from position and persistence, not a test result, and no source confirms it. | [harmonization-tests.md](harmonization-tests.md#static-and-recurring-sources), [w03](harmonization-tests-research/w03-data-availability.md#6-the-fixed-heat-source) |

Two figures were not recomputed on the later definitions: the rank correlation of 0.97 and the share of months within one class (98%).

## How this was produced

| File | Question |
|---|---|
| [m01-ratio-stability.md](harmonization-evidence-research/m01-ratio-stability.md) | How stable is the VIIRS-to-MODIS count ratio? |
| [m02-grid-units.md](harmonization-evidence-research/m02-grid-units.md) | Does counting active grid cells bring the sensors together? |
| [m03-like-for-like-pairs.md](harmonization-evidence-research/m03-like-for-like-pairs.md) | How do the cleanest sensor pairs compare? |
| [m04-drift-effect.md](harmonization-evidence-research/m04-drift-effect.md) | What has the orbit drift done since 2022? |
| [m05-anomaly-agreement.md](harmonization-evidence-research/m05-anomaly-agreement.md) | Do the sensors rank months the same way? |
| [m06-scan-angle.md](harmonization-evidence-research/m06-scan-angle.md) | How much do pixel size and scan position matter? |
| [m07-filter-sensitivity.md](harmonization-evidence-research/m07-filter-sensitivity.md) | How sensitive are results to filters? |
| [m08-spatial-scale.md](harmonization-evidence-research/m08-spatial-scale.md) | Does the relationship hold for a user-sized area? |
| [m09-overpass-and-multi-viirs.md](harmonization-evidence-research/m09-overpass-and-multi-viirs.md) | How should several VIIRS satellites be combined? |
| [m10-frp-as-unit.md](harmonization-evidence-research/m10-frp-as-unit.md) | Is fire radiative power a better unit than counts? |
| [r01-published-methods.md](harmonization-evidence-research/r01-published-methods.md) | Published comparisons and joins |
| [r02-operational-systems.md](harmonization-evidence-research/r02-operational-systems.md) | How operational systems bridge the sensors |
| [r03-bc-fire-record.md](harmonization-evidence-research/r03-bc-fire-record.md) | Check against BC fire records |
| [q01-requirements.md](harmonization-evidence-research/q01-requirements.md) | What the challenge material requires |
| [_cross-check.md](harmonization-evidence-research/_cross-check.md) | Reconciled numbers and conflicting conclusions |

- **AI assistance.** The measurements, literature search and this write-up were produced with AI agents (Claude) on 14 November 2026: 28 agents ran the analyses and checks, and the results were aggregated into this document. The choice of harmonization approach is left to the team.
- **AI assistance in the corrections.** The corrections listed under "Changes since first compiled" were made on 14 November 2026 by AI agents (Claude), from the later tests in [harmonization-tests.md](harmonization-tests.md), which were themselves produced with AI agents. Each changed statement was checked against a working file named in that section. A final review by an AI agent the same day carried the results of the three follow-up tests (f01 to f03) into this document and re-checked the outage dates against the catalogue files.
- **Limits of the whole exercise.** One box, ten stable-orbit years dominated by three large fire seasons (2017, 2018, 2021), and four drift years. Only Suomi NPP overlaps MODIS in stable orbit. Literature sources read as abstracts only are marked in their topic files.
- **Scripts and tables.** The topic files name the scripts and result tables behind each number. Those are kept outside version control with the cached data.
