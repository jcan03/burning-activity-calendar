# Can the factor be trusted before 2012, where it is actually applied?

## Answer

Partly. Before 2012 the main evidence is about order, not size. Converted MODIS years rank against BC area burned about as well as Suomi NPP years do (Spearman 0.88 over 2003–2025). Across the 2012 join, year pairs agree 84% of the time, against 89% within each era. BC area burned cannot confirm the level of the converted history. The raw MODIS relationship to area burned shows no detectable change between 2003–2011 and 2012–2021 (era factor 0.83, 95% interval 0.50–1.27), but that test could only detect a change of about twofold, against the ±10% precision claimed for the factor. The joined series shows converted pre-2012 years about 1.6 times above VIIRS years of equal area burned (step 0.61, 0.39–0.91). About a third of that step, in log terms, comes from the factor being a ratio of sums dominated by big years. In 2012–2021 the factor overstated the six smaller seasons by about 27% and was unbiased in the three big ones, and seven of the nine pre-2012 seasons are small. MODIS was internally stable from 2003 to 2021 (Terra/Aqua trend +0.2% a year, −0.4 to +1.0). The Terra-only years 2001–2002 are untested against area burned: depending on the reference line, they sit inside it or at the lower edge of its 95% band.

## Evidence

Common basis: standard rows (`stream == SP`), `use == True`, local-date months, fire season April to October summed by year. Area burned is `area_km2` for the calendar year. The factor f = 0.2425 is the Terra+Aqua to Suomi NPP ratio of sums over the 116 stable months (year bootstrap 0.237–0.270), which reproduces the specification's check. All intervals are 95%. "Bootstrap" means resampling whole years, separately within each era.

**Zero, outage and unclassifiable months.** No calendar classes are used here, so no month is unclassifiable. Zero months are kept as zeros in sums: 4 stable months have no MODIS hotspots and 1 has no Suomi NPP hotspots, and no yearly sum is zero. The Aqua outage (August–September 2020) falls in a fire season, so 2020 is dropped from every Terra+Aqua and Aqua fit (9 years after 2012). Terra gaps in 2002-03, 2003-12 and 2016-02 fall outside the fire season. The 2001 Terra gap (15 April, and 15 June to 3 July) is adjusted by days (see 3). Suomi NPP's 2022 gap is filled with NOAA-20 × 0.995.

**1. Raw MODIS against area burned.** The model is ln count = a + b·ln area + era. The era factor is exp(era); below 1 means fewer hotspots per km² after 2012. The detectable change is the size the test finds 80% of the time at the 5% level.

| Series (pre / post years) | Era factor | Bootstrap 95% | p | Slopes differ, p | Detectable change |
|---|---|---|---|---|---|
| Terra+Aqua (9 / 9, no 2020) | 0.83 | 0.50–1.27 | 0.46 | 0.04 | ×2.1 |
| Terra (9 / 10) | 0.72 | 0.40–1.17 | 0.26 | 0.05 | ×2.3 |
| Aqua (9 / 9) | 0.82 | 0.49–1.26 | 0.44 | 0.04 | ×2.1 |
| Terra+Aqua, also without 2011 | 0.88 | 0.52–1.34 | 0.61 | 0.09 | ×2.1 |
| Terra+Aqua, also without 2021 | 0.77 | 0.45–1.18 | 0.30 | 0.12 | ×2.1 |

The three sensor rows share the same fires, so they are not independent confirmations. The steeper slope after 2012 depends on the end years and is not robust.

**2. Step at 2012 in the joined series.** The joined series is MODIS/f for 2003–2011 and Suomi NPP from 2012. The model adds a step for 2012 onward.

| Series and years | Step | 95% interval | p |
|---|---|---|---|
| Joined, 2003–2025 (23 years) | 0.61 | 0.38–0.97 (OLS), 0.39–0.91 (bootstrap) | 0.04 |
| Joined, 2003–2021 (19) | 0.62 | 0.36–1.08 | 0.09 |
| Joined, 2003–2021 without 2020 (18) | 0.70 | 0.42–1.18 | 0.16 |
| MODIS only, no join, same 18 years | 0.83 | 0.49–1.41 | 0.46 |
| Joined, factor = geometric mean of yearly ratios (0.282) | 0.71 | 0.44–1.13 | 0.14 |
| Joined, without 2011 (22) | 0.65 | 0.41–1.03 | 0.07 |

The step the 23-year test could detect is ×1.9. Comparing rows 3 and 4 splits the step. About 0.83 of it is in MODIS itself, as fewer hotspots per km² later, whether real or instrumental. About 0.84 is the conversion. Leave-one-year-out yearly conversion errors over 2012–2021 (9 years) average +0.15 in log (sd 0.20). They are +0.24 (×1.27) for the six years with under 2,000 MODIS hotspots and −0.03 for the three large years. Seven of the nine pre-2012 seasons have under 2,000 MODIS hotspots. Leaving 2020 in or out alone moves the step between 0.62 and 0.70.

**3. Terra-only period.** The Terra to Terra+Aqua factor is 1.904 (1.88–1.95), fitted on the 2003–2011 fire seasons at all hours. Its leave-one-year-out yearly error has sd 3.5% (median 1.8%). In July–October 2002, with both satellites flying, the actual ratio was 2.01. The 2001 gap days held a median of 0.5% of Terra's fire-season hotspots in 2003–2011 (up to 10% in 2004), so the coverage is 0.995.

| Year | Terra hotspots | VIIRS-equivalent (95%) | Area km² | Against Terra's 2003–11 line: predicted (95% band), log residual | Against the joined 2003–25 line: log residual |
|---|---|---|---|---|---|
| 2001 | 229 | 1,808 (1,138–2,872) | 30.7 | 467 (251–870), −0.71 | −0.45 |
| 2002 | 200 | 1,571 (989–2,496) | 46.7 | 553 (300–1,020), −1.02 | −0.85 |

Both years fall below every reference line. They fall at or below the 95% band of the line fitted in the era where the factor is used, and inside the band of lines that pool post-2012 years. Quiet years after 2012 also run low (2012: 2.9 Terra hotspots per km², 2020: 1.9), so this is not proof of an instrument problem. It does mean area burned does not validate these two years.

**4. Terra/Aqua ratio by calendar year, 2003–2021** (gap months removed for both sensors).

| Hours | 2003–11 | 2012–21 | Trend per year (bootstrap 95%) | Yearly range |
|---|---|---|---|---|
| Day | 0.745 | 0.698 | −0.1% (−0.6 to +0.6) | 0.65–0.89 |
| Night | 2.19 | 2.24 | +0.2% (−5.0 to +5.1) | 1.6–10.8 |
| All | 1.06 | 1.15 | +0.2% (−0.4 to +1.0) | 0.88–1.22 |

**5. Ranks.** Spearman correlation of the joined series with area burned over 2003–2025 is 0.88 (0.64–0.97). Within 2003–2011 it is 0.92 and within 2012–2025 it is 0.89. The six largest seasons by area (2021, 2017, 2023, 2003, 2018, 2009) are the top six of the joined series, with only 2003 and 2018 swapped. Of the 126 pairs with one year on each side of 2012, 84% are ordered the same way as area burned. In 19 of the 20 mismatched pairs the pre-2012 year is ranked too high, mostly the small years 2007, 2008 and 2011. On the same 81 pairs against 2012–2021, MODIS alone with no join agrees 86% of the time and the joined series 83%.

**6. Joined series.** The series is saved in `out/a05-pre2012-check_joined_series.csv`. Intervals for converted years are ±t(8 degrees of freedom) × the leave-one-year-out sd, about ×0.63 to ×1.59, with the Terra step added in quadrature for 2001–2002. They are not shifted for the small-year bias. A column using the geometric-mean factor, which gives values 14% lower, is included as a sensitivity.

**Against the earlier evidence.** The earlier evidence gives a fire-season ratio range of 0.19–0.40. Here it is 0.23–0.41, because 2020 is dropped: 2020 is 0.23 as recorded and 0.20 with the Aqua-gap months removed from both sensors. The earlier statement that one factor holds in the three biggest years (0.234–0.244) agrees with the near-zero error found here for large years. The earlier statement that small years have many hotspots per km² is the same pattern seen in the step here. The earlier finding that every sensor ranks years about equally well (0.84–0.89) agrees with 0.88 here.

## What this implies

- The team can claim that converted 2003–2011 history puts years in the right order relative to the VIIRS years, with modest loss (84% against 89% pair agreement).
- The team cannot claim that BC area burned validates the absolute level of converted pre-2012 counts. The check can only see changes of about twofold.
- For small and moderate seasons before 2012, a ratio-of-sums factor plausibly overstates VIIRS-equivalent counts by about 25%. That is enough to tilt current quiet months toward "below normal" when judged against a baseline that includes those years. This rests on six years.
- The steadiness of Terra relative to Aqua supports MODIS being consistent with itself before 2012. It cannot rule out a change common to both instruments.
- Showing 2001–2002 rests only on the Terra-to-Terra+Aqua step (±4%). Area burned neither supports nor clearly contradicts those years. November–December 2000 cannot be tested.
- Nothing here tests a single month before 2012.

## Limits

- There are only 9–10 years per era, and area burned is yearly, recorded by discovery date, and leaves out prescribed and industrial burns, which may dominate hotspots in quiet years.
- Hotspots per km² can change for real reasons, such as fire type or burning practice, so a step cannot be assigned to the instrument alone.
- The size-dependent bias comes from six small and three large years.
- Fire-season totals were used throughout; months were not tested.

## How it was computed

- `scripts/a05_prep.py`, `a05_main.py` and `a05_extra.py` are the analyst's scripts. Re-run from a clean start, they reproduced every table exactly.
- `scripts/a05-pre2012-check_review.py` is an independent recomputation from the parquet file. It covers the era fits, step decomposition, leave-one-year-out errors by year size, 2001 coverage by gap days, Terra/Aqua trends and cross-era pair concordance. It uses 4,000 year-block resamples. Its output is in `out/a05-pre2012-check_*.csv` and `_review_log.txt`.
- `scripts/a05-pre2012-check_terra0102.py` tests 2001–2002 against several Terra count–area lines.
- `scripts/a05-pre2012-check_joined.py` writes the corrected joined series.
