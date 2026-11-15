# Shared definitions for the fourth follow-up (h01–h04)

The four analyses of the fourth follow-up and their cross-check all used the definitions below, so that their numbers can be compared directly. Where a working file says "the spec", it means this file. It was written by the AI assistant before the analyses were run, on 14 November 2026.

## Why this follow-up was run

The earlier hindcast showed that a calendar baseline built from converted MODIS years plus VIIRS years gives the right class more often than a short VIIRS-only baseline (84% against 66% of fire-season months on the whole box). Two things about that test did not match a method the team was considering:

1. **Classes.** The hindcast classed a month by its ratio to the calendar-month median, in five fixed bands. The method being considered classes a month by its rank among the same calendar month in other years.
2. **Current month.** The hindcast took the month being classed from Suomi NPP alone, which ended on 2 November 2026. The method being considered takes it from a combined VIIRS series.

The follow-up re-ran the hindcast with those two changes, separately and together, and repeated the real-record comparison with rank classes.

## Data

- The same 737,244 FIRMS hotspots as the earlier tests (box 49.0–52.5°N, 122.5–118.0°W), with the standard filter (`use`): vegetation-fire and near-real-time rows, without the fixed heat source near Kamloops.
- Months are keyed by local date.
- The 31 test circles at each radius are the same as in the earlier tests.
- The per-day availability flag is the one built in [f03](f03-availability-flag.md) (catalogue, outage list and count check). NOAA-20 is treated as available on 1 April to 4 June 2018, where the catalogue is silent but FIRMS has data.
- The stable-orbit period is February 2012 to December 2021, without February 2016, August 2020 and September 2020 (116 months). November 2026 is left out.

## Series (monthly, by local date)

| Code | Definition |
|---|---|
| `M` | Terra plus Aqua hotspots |
| `S` | Suomi NPP hotspots |
| `N20s` | NOAA-20 hotspots × 1.0245 |
| `N21s` | NOAA-21 hotspots × 1.0503 |
| `C` | Combined VIIRS. For each local day, the mean over the VIIRS satellites available that day of their scaled counts (Suomi NPP × 1, NOAA-20 × 1.0245, NOAA-21 × 1.0503). Days with no satellite available contribute 0. The days are summed over the month. Before April 2018 this is Suomi NPP on its available days. |
| `C2` | As `C`, using only NOAA-20 and NOAA-21: the configuration after 2 November 2026. Defined from March 2023. |
| `Csn20` | As `C`, using only Suomi NPP and NOAA-20. |

- **Conversion** of a MODIS month to VIIRS-equivalent is `M ÷ f`, with `f` the ratio of sums `M / S` over the years a test allows. On all 116 stable months `f` = 0.2425. Factors are always fitted on the whole box.
- **Fire season** is April to October. Tables are also split for May to September and June to September.

**Checks every analysis reproduced before starting:**

1. On the 116 stable months: `M` = 48,233, `S` = 198,916, ratio 0.2425.
2. `C` for the whole box: July 2022 = 629, August 2022 = 2,266, July 2023 = 4,753, July 2024 = 7,102, November 2024 = 690, August 2026 = 29,590 (the values from f03, to within about 1%).
3. Protocol B, whole box, ratio classes, 202 splits: design `U1` agrees with the truth in 84.4% of fire-season months and 79.7% of all months; design `SV` in about 66% and 65%.

## Class schemes

Every result is reported under both schemes.

- **`R5`, ratio classes.** The value divided by the baseline median for the same calendar month, in five classes cut at 0.5, 0.8, 1.25 and 2. A month can be classed only when the baseline median is at least 1. `R3` is the coarse version: below 0.5, 0.5 to 2, above 2.
- **`P5`, rank classes.** The baseline is the `n` values for the same calendar month in the other years; the month's own year is always left out. `pct` = (number of baseline values below the value + half the number equal to it) ÷ `n`. The class is the smaller of `floor(5 × pct)` and 4. The class is "uncertain", and counted as not classed, when 20% or more of the baseline values equal the value. `P3` is the coarse version, cut at 1/3 and 2/3.
- For rank results the analyses also report the mean absolute difference in `pct` from the truth, and how often a design agrees with the truth on whether the month is the highest on record.

Agreement rates are not comparable between the two schemes, because their classes have different base rates. What is comparable, within one scheme, is a design's agreement with the truth, the benchmark's agreement, the gain of the design over the benchmark, Cohen's kappa, and agreement within one class.

## Protocols

**Protocol B (mixed-era baseline).** A split assigns `k` of the ten stable years to a pretend MODIS era, in which only MODIS counts may be used, and the rest to a VIIRS era.

- **Truth:** the class of each VIIRS-era month against a baseline of `S` from all nine other years.
- **`U1`:** the baseline is the converted MODIS-era years plus `S` from the other VIIRS-era years.
- **`SV`, the benchmark:** the baseline is `S` from the other VIIRS-era years only.
- **Standard splits:** 202 with `k` = 5: the two chronological splits and 200 random ones, the same as in the earlier hindcast ([a01](a01-hindcast-box.md)).

**Protocol A (single-month conversion).** Leave one year out, fit the factor on the other nine, convert the held-out year's MODIS months, and class each converted value and the actual Suomi NPP value against a baseline of Suomi NPP counts from the other nine years.

**Intervals.** 95% intervals resample whole years (at least 1,000 draws). The standard deviation across splits is reported beside them, because months within a year are not independent and the splits reuse the same ten years.

**Units.** The whole box and the 31 circles at 100 km, with 50 km and 150 km where run time allowed.
