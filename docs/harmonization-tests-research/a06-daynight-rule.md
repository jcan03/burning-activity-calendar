# One day-and-night rule for every row

## Answer

In this file the delivered `daynight` label is exactly "night when the solar zenith angle exceeds 85 degrees" for all 737,244 rows, standard and near-real-time, on all five sensors. The solar zenith angle is the angle between the sun and the vertical; 90 degrees is the horizon. The near-real-time rows (August to October 2026) show no difference, but that test cannot tell the rules apart: no near-real-time row lies between 83.6 and 96.5 degrees, so the documented sun-angle rule, an orbit-direction rule and a pass-based rule all give the same labels there. A pass-based label (the overpass's local solar hour: 06:00 to 18:00 is day) differs from the sun-angle rule for only 10 hotspots in 26 years, all from one Terra evening pass on 24 July 2026. Under either label, Terra's 2026 daytime ratio to NOAA-20 is about half its 2018–2021 level: 0.069 to 0.070 against 0.138, or 0.50 of normal (0.35–0.55). The labelling rule does not explain the halving. The real risk is ahead: both of MODIS's twilight passes, Terra's evening pass and Aqua's dawn pass, now sit only a few degrees above the 85-degree line in summer.

## Evidence

**Agreement of the delivered label with the 85-degree rule** (all rows, both streams). These numbers were recomputed with a separate solar formula (the Michalsky/Astronomical Almanac formula). It differs from the analyst's NOAA formula by at most 0.009 degrees, and it reproduces solar noon to within 30 seconds at Kamloops on 21 June, Greenwich on 3 November and 0°N 0°E on 11 February.

| Stream | Sensor | Rows | Differ | Largest zenith labelled D | Smallest zenith labelled N |
|---|---|---|---|---|---|
| Standard | Terra | 50,899 | 0 | 84.43 | 85.34 |
| Standard | Aqua | 44,479 | 0 | 82.98 | 85.31 |
| Standard | Suomi NPP | 277,080 | 0 | 80.27 | 90.70 |
| Standard | NOAA-20 | 208,385 | 0 | 78.99 | 90.86 |
| Standard | NOAA-21 | 66,141 | 0 | 79.99 | 91.83 |
| Near-real-time | all five | 90,260 | 0 | 83.55 (Aqua) | 96.51 |

The threshold is therefore pinned between 84.43 and 85.31 degrees. Only MODIS rows ever fall near it. VIIRS has no row between 80.3 and 90.7 degrees.

**Current months (Aug–Oct 2026, `use` rows).** All three rules give identical day and night counts in every sensor-month: 0 of 88,650 near-real-time rows move. Examples: August NOAA-20 has 9,554 day and 19,783 night hotspots; October Suomi NPP has 419 and 340; October Terra has 30 and 42. No sensor-month mixes standard and near-real-time rows. August 2026 is still standard for Terra and Aqua but near-real-time for VIIRS.

**Sun-angle rule against pass label** (`use` rows, to October 2026). A pass is a run of one sensor's rows with no gap over 20 minutes. There are 20,104 passes, and every pass falls entirely on one side of the 06/18 cut.

| Sensor and pass | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|
| Terra evening pass, rows (differing) | 2,708 (0) | 914 (0) | 466 (0) | 4,444 (10) |
| Aqua afternoon pass | 2,258 (0) | 807 (0) | 453 (0) | 2,957 (0) |
| Aqua dawn pass | 1,293 (0) | 325 (0) | 120 (0) | 1,315 (0) |

All 10 differing rows come from Terra on 24 July 2026 at 03:11–03:12 UTC (19:07 local solar time, zenith 82.9–84.4). They are labelled D by the sun and N by the pass. No June row differs in any year. Before 2026, no row of any sensor differs.

**How close the twilight passes are** (summer, fire rows):

| | Median pass hour | Smallest zenith | Share of rows under 90° | Detecting passes with a row under 88° |
|---|---|---|---|---|
| Terra evening, July 2024 | 21.2 | 90.1 | 0% | 0 of 34 (Jun–Aug) |
| Terra evening, July 2026 | 20.1 | 82.9 | 39% | 13 of 50 (Jun–Aug) |
| Aqua dawn, July 2024 | 3.0 | 90.9 | 0% | 0 of 20 (Jun–Aug) |
| Aqua dawn, July 2026 | 4.2 | 85.9 | 39% | 7 of 45 (Jun–Aug) |

**Drift ratios under each label.** These are NOAA-20 ratios for the fire season (April to October), keyed by local-date month, from `use` rows, as ratios of sums. Months that overlap an outage of either sensor were dropped: Terra 2022-10, and for Aqua 2020-08, 2020-09 and 2022-04. Months with zero MODIS hotspots were kept as zeros: 4 for Terra by day and 15 for Terra by night, over 2018–2026. The interval on the baseline comes from resampling whole years, 2018–2021, 5,000 draws. With only four years this interval is coarse and unstable. The analyst's two runs on identical inputs gave 0.117 and 0.097 as the lower bound for Terra+Aqua at night.

| Series | Baseline 2018–21 (interval) | 2018–2025 range | 2026, delivered/sun label | 2026, pass label | 2026 relative to baseline (interval) |
|---|---|---|---|---|---|
| Terra day | 0.138 (0.128–0.201) | 0.127–0.212 | 0.070 (1,120/16,017) | 0.069 (1,110/16,017) | 0.50 (0.35–0.55) |
| Terra night | 0.127 (0.084–0.129) | 0.072–0.136 | 0.137 | 0.138 | 1.08 |
| Terra+Aqua day | 0.340 (0.318–0.451) | 0.318–0.462 | 0.254 | 0.253 | 0.75 (0.56–0.80) |
| Terra+Aqua night | 0.188 (0.117–0.191) | 0.048–0.193 | 0.178 | 0.178 | 0.95 |
| Aqua day | 0.202 (0.191–0.253) | 0.190–0.272 | 0.184 | 0.184 | 0.91 |

The 2026 values rest on 7 fire-season months. Terra's 2026 daytime ratio is below each of the eight years 2018–2025. The 2026 Terra daytime ratio mixes streams, so it was also split by stream:

- Both sensors standard, April–July: 0.050 (294/5,935), against 0.128 for April–July 2018–2021, or 0.39 of normal.
- August, with Terra standard and NOAA-20 near-real-time: 0.083.
- Both near-real-time, September–October: 0.062 (33/528).

The 10 relabelled rows change no class in July 2026. That covers the whole box (Terra or Terra+Aqua, day or night, against 2003–2021 or 2012–2021 medians) and 124 test circles × 4 series. Of those 496 circle cases, 225 were unclassifiable because their baseline median was below 1, and 0 of the remaining 271 changed.

## What this implies

- The team can say that one labelling rule now covers every row. Recomputing the label from each hotspot's time and position, with the 85-degree rule, reproduces every delivered label. A pass-based rule reproduces all but 10. Either rule removes any dependence on whether a row is standard or near-real-time.
- The team cannot claim to have shown that the near-real-time stream really uses the sun-angle rule. The file contains no near-real-time row in the zenith range where the rules would disagree, and no orbit-direction flag.
- For current months (August–October 2026) the choice of rule changes no day or night count. It would start to matter in June–August, when the two MODIS twilight passes approach 85 degrees.
- The two rules behave differently as the orbits keep drifting. Under the sun-angle rule, parts of Terra's evening pass and Aqua's dawn pass would move from the night series to the day series in summer. A pass-based rule keeps each pass in one series, but its "night" pass is then partly in daylight. Neither keeps the MODIS night series like the VIIRS 02:10 pass.
- The finding that Terra's daytime count fell to about half in 2026 holds under every label tested and in every stream subset (0.39–0.50 of normal). The finding is about counts, not labels. Because the baseline has only four NOAA-20 years, "about half" should be stated with its range, roughly a third to a little over half.

## Limits

- Only one pass, on 24 July 2026, shows any disagreement. The claim that more will follow in 2027 extrapolates from the drift and has not been measured. Terra and Aqua may also stop operating.
- The near-real-time label may have been recomputed upstream before it reached this file. The file cannot show how FIRMS sets that label.
- The NOAA-20 baseline has four years, so its intervals are weak. Suomi NPP has only 2 usable fire-season months in 2026.
- No calendar classes were computed beyond July 2026. Months in other years are untouched because no row before 2026 differs.
- The 06:00/18:00 cut is a choice. Only 84 rows lie within an hour of it, and no pass straddles it.

## How it was computed

- `scripts/a06-daynight-rule_review.py` (the reviewer's independent recomputation) runs in about 15 seconds. It does five things: Michalsky solar zenith with checks; the spec check (116 months; MODIS 48,233 and Suomi NPP 198,916 hotspots; 0.2425 overall, 0.343 by day, 0.177 at night); label agreement by stream and sensor; its own pass grouping (20-minute gaps, circular mean hour); and drift ratios with a year bootstrap and stream splits. Tables are `out/a06-daynight-rule_rev_*.csv` and the log is `out/a06-daynight-rule_rev_log.txt`.
- `scripts/a06-daynight-rule_review_cmp.py` compares the two zenith formulas and the twilight-pass margins. `scripts/a06-daynight-rule_review_class.py` runs the July 2026 class-change check on the box and circles.
- The analyst's scripts (`a06_sza.py`, `a06_main.py`, `a06_pass.py`, `a06_drift.py`, `a06_bounds.py`) were re-run from a clean start and reproduce their draft.
