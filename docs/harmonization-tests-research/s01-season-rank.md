# In a small area, does classing a season in place of a month help?

## Answer

Yes. Classing June to September as a whole, in place of a single month, raises the share of periods that can be classed at all and keeps the accuracy of the class. In 50 km circles the share that can be classed rises from 60% of months to 96% of summers, and the converted baseline gives the true class in 84% of them, against 78% for months. A summer in a 50 km circle behaves much as a single month does in a 100 km circle (97% classable, 81% right). In 25 km circles the share rises from 25% to 61%, but 39% of summers still cannot be classed. The converted baseline keeps its gain over a short VIIRS-only baseline at every radius: about 25 points at 25 and 50 km. On the real record, with the app's own rules, the share of 2001–2025 periods that get a class rises from 23% to 56% at 25 km, from 55% to 99% at 50 km, and from 93% to 100% at 100 km.

A season gives one label a year where months give four, so it is a fallback beside the monthly calendar, not a replacement.

## Evidence

**Basis.** The class test of [h00](h00-definitions.md) (Protocol B), on the same monthly counts as [h01](h01-rank-classes-hindcast.md): Terra plus Aqua (`M`) and Suomi NPP (`S`), standard rows, the `use` filter, local-date months, the whole box and the same 31 circles at 25, 50, 100 and 150 km. A period is either one calendar month or a season, whose value is the sum of its months.

- **Years.** The nine stable years 2012–2021 without 2020. Aqua was out in August and September 2020, and a season total needs every one of its months.
- **Splits.** All 126 ways of taking four of the nine years as the pretend MODIS era. That leaves five VIIRS-era years, so the benchmark has four years, as in the earlier tests.
- **Factor.** Fitted on the whole box, on the VIIRS-era years of each split.
- **Truth.** The class of a VIIRS-era period against Suomi NPP in the other eight years.
- **Converted baseline.** The four converted MODIS-era years plus Suomi NPP in the other four VIIRS-era years.
- **Benchmark.** Suomi NPP in the other four VIIRS-era years only.
- **Classes.** Rank classes and ratio classes as defined in h00. Under rank classes a period gets no class when 20% or more of its baseline ties with it. Under ratio classes it gets none when the baseline median is below 1.
- **Scoring.** Agreement is the share of periods whose truth can be classed that a design gives the same class. A period a design cannot class counts as a miss.
- **Intervals.** 95%, resampling the nine years (4,000 draws). The standard deviation across the 126 splits is given beside them.

**Checks before starting.** The harness reproduced the published numbers on the standard protocol (ten years, 202 splits, months) before anything was changed:

| Check | Published | Reproduced |
|---|---|---|
| 116 stable months: `M`, `S`, ratio | 48,233, 198,916, 0.2425 | 48,233, 198,916, 0.2425 |
| Box, fire season, ratio classes: converted, benchmark, gain | 84.4%, 66.1%, +18.2 | 84.4%, 66.1%, +18.2 |
| Box, all months, ratio classes: converted | 79.7% | 79.7% |
| Box, fire season, rank classes | 86.2%, 60.3%, +25.9 | 86.2%, 60.3%, +25.9 |
| 100 km, fire season, ratio classes | 77.4%, 66.7%, +10.6 | 77.4%, 66.7%, +10.6 |
| 100 km, fire season, rank classes | 73.9%, 56.8%, +17.0 | 73.9%, 56.8%, +17.0 |
| 50 km, ratio classes, share classable: truth, converted, benchmark | 67%, 55%, 66% | 66.6%, 55.3%, 65.9% |
| 25 km, the same | 22%, 17%, 29% | 22.4%, 17.1%, 29.3% |

**1. Rank classes, June to September.** "Right, of all periods" is the share of every circle-period, classable or not, that the design gives the true class.

| Radius | Period | Truth can be classed | Converted: same class | Benchmark: same class | Gain, points (interval; SD across splits) | Converted within one class | Right, of all periods: converted, benchmark |
|---|---|---|---|---|---|---|---|
| 25 km | Month | 25.3% | 91.0% | 66.2% | +24.8 (18.9 to 32.9; 8.8) | 99.7% | 23.0%, 16.7% |
| 25 km | Season | 61.3% | 81.2% | 56.7% | +24.5 (17.5 to 30.8; 12.9) | 96.4% | 49.8%, 34.8% |
| 50 km | Month | 59.9% | 78.4% | 56.7% | +21.7 (18.2 to 25.4; 8.7) | 93.1% | 47.0%, 34.0% |
| 50 km | Season | 96.4% | 83.8% | 58.4% | +25.4 (19.3 to 31.8; 16.2) | 97.4% | 80.8%, 56.3% |
| 100 km | Month | 97.3% | 80.7% | 57.8% | +22.9 (17.6 to 28.1; 12.5) | 96.5% | 78.5%, 56.3% |
| 100 km | Season | 100% | 90.4% | 61.0% | +29.4 (18.9 to 39.1; 18.4) | 99.9% | 90.4%, 61.0% |
| 150 km | Month | 99.2% | 84.5% | 60.2% | +24.3 (17.3 to 31.7; 15.5) | 98.8% | 83.8%, 59.7% |
| 150 km | Season | 100% | 96.8% | 61.0% | +35.8 (23.7 to 46.5; 23.1) | 100% | 96.8%, 61.0% |
| Box | Month | 100% | 89.7% | 61.3% | +28.5 (17.7 to 38.5; 16.7) | 99.6% | 89.7%, 61.3% |
| Box | Season | 100% | 94.4% | 61.3% | +33.2 (15.9 to 48.4; 26.3) | 100% | 94.4%, 61.3% |

There are 279 circle-seasons at each radius (31 circles, nine years) and 1,116 circle-months.

**2. Other windows, rank classes, season against month.** Each cell gives the share whose truth can be classed, then the converted baseline's agreement.

| Radius | May to September: month | May to September: season | April to October: month | April to October: season |
|---|---|---|---|---|
| 25 km | 23.9%, 91.2% | 72.0%, 76.5% | 32.9%, 82.8% | 100%, 80.6% |
| 50 km | 55.5%, 76.9% | 96.8%, 85.6% | 63.2%, 74.7% | 100%, 82.8% |
| 100 km | 96.6%, 78.8% | 100%, 89.6% | 97.5%, 77.0% | 100%, 84.5% |

The gain over the benchmark is between 20.8 and 28.9 points for every season in this table.

An April-to-October season in a small circle is a different quantity from a summer. The median Suomi NPP count of a 50 km circle is 203 hotspots for April to October and 28 for June to September, so in an ordinary year most of the longer season is spring and autumn burning.

**3. Ratio classes, June to September.**

| Radius | Period | Truth can be classed | Converted can class | Converted: same class | Benchmark: same class | Gain, points (interval) |
|---|---|---|---|---|---|---|
| 25 km | Month | 10.6% | 8.1% | 54.7% | 66.0% | −11.3 (−15.4 to −7.6) |
| 25 km | Season | 74.2% | 64.7% | 71.9% | 69.3% | +2.6 (0.2 to 4.8) |
| 50 km | Month | 66.8% | 57.5% | 71.2% | 71.4% | −0.2 (−2.7 to 2.2) |
| 50 km | Season | 100% | 99.9% | 90.4% | 76.7% | +13.7 (8.9 to 18.5) |
| 100 km | Month | 100% | 99.9% | 82.5% | 74.8% | +7.7 (3.5 to 11.7) |
| 100 km | Season | 100% | 100% | 92.5% | 77.4% | +15.0 (7.7 to 22.7) |

Under ratio classes the converted baseline does not beat the benchmark for single summer months at 25 or 50 km. For a season it is level at 25 km and ahead by 13.7 points at 50 km.

**4. How often MODIS records nothing when Suomi NPP saw fire, June to September.**

| Radius | Period | Suomi NPP recorded nothing | MODIS recorded nothing, of periods where Suomi NPP saw fire | Median count: Suomi NPP, MODIS |
|---|---|---|---|---|
| 25 km | Month | 72.4% | 42.5% | 0, 0 |
| 25 km | Season | 35.8% | 34.6% | 2, 0 |
| 50 km | Month | 41.8% | 31.2% | 1, 0 |
| 50 km | Season | 6.1% | 9.9% | 28, 9 |
| 100 km | Month | 9.2% | 15.5% | 14, 5 |
| 100 km | Season | 0% | 0% | 114, 43 |

At 25 km the limit is the fire itself: Suomi NPP recorded nothing in 36% of circle-summers, and the median summer has two hotspots.

**5. The real record, with the app's own rules.** This used `harmonize.py` as it stands after the outage days were added and the factor was fitted on 2012–2021 (factor 8.64): its filters, its per-satellite index and its ranking rule (the same period in the other years of 2001–2025, at least eight of them, no class when 20% or more tie). A summer's value is the mean of its four monthly index values. Share of June-to-September periods given a class, mean over the 31 circles:

| Radius | Months, 2001–2025 | Summers, 2001–2025 | Months, 2012–2025 | Summers, 2012–2025 |
|---|---|---|---|---|
| 25 km | 22.9% | 55.9% | 29.1% | 66.6% |
| 50 km | 54.6% | 99.2% | 62.5% | 99.3% |
| 100 km | 93.1% | 100% | 95.2% | 100% |
| 150 km | 100% | 100% | 100% | 100% |

The app's six preset areas (7,000 to 20,000 km²) can class every summer of 2001–2025. By month they class 68% (Kamloops area), 91% (Okanagan Valley), 57% (Shuswap), 56% (Nicola Valley), 70% (Fraser Canyon) and 58% (South Cariboo) of June-to-September months.

**6. Cross-checks.**

- A separate script recomputed, straight from the hotspot table and without the harness, the numbers that do not depend on the splits: the share of circle-periods whose truth can be rank-classed, and how often MODIS has nothing when Suomi NPP saw fire, for months and seasons at 25, 50 and 100 km. Every value matched to 0.1 point.
- The app's `summer_table` was compared with the separate ranking in the real-record script, over the 124 circles and six presets and every year from 2001 to 2026. No class differed.

## What this implies

- The team can say that in an area about 100 km across, a summer can be classed almost always, and that the converted baseline gives it the right class about as often as it does a month in an area twice as wide.
- A summer class is a sound fallback where months cannot be classed. It does not replace the months: it gives one label a year.
- The window matters. June to September is where the two sensors see the same fires. A longer season in a small area is mostly spring and autumn burning, which MODIS largely misses.
- At 25 km a summer class helps but does not solve the problem. About four summers in ten still cannot be classed.

## Limits

- One analyst ran this test. The checks above stand in for the independent reviewer that the earlier tests had; no second analyst re-ran it.
- Nine seasons per circle, and 279 circle-seasons per radius. The circles overlap and share their years, and the 126 splits reuse the same nine years, so the intervals are too narrow. The standard deviation across splits is 9 to 26 points.
- With eight baseline years, one place in rank moves a season a whole class under rank classes.
- The benchmark has four years. A real VIIRS-only baseline has 14, and the gain over that is still unmeasured, as for months.
- 2020 is left out, which removes one of the smallest fire seasons.
- Only Suomi NPP was used as the period being classed.

## How it was computed

Scripts and outputs are in `data/harmonization-analysis/round6/`, outside version control with the cached data.

- `scripts/s01_hindcast.py`: the checks and the class test (sections 1 to 4). It reads the monthly cube built for h01 and copies h01's classing function. Output: `out/s01_hindcast_summary.csv`, `out/s01_modis_zero.csv`.
- `scripts/s02_real_record.py`: the real record with the app's rules (section 5) and the comparison with `harmonize.summer_table`. Output: `out/s02_real_record_units.csv`, `out/s02_real_record_summary.csv`.
- `scripts/s03_crosscheck.py`: the separate recomputation from `round3/data/hotspots_v2.parquet`.
