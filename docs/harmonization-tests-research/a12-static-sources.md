# A screen for static and recurring non-wildfire sources across the box

## Answer

Across the whole box, the Kamloops site is the only fixed heat source that VIIRS sees year after year. It has 712 dates in all 15 years from 2012 to 2026, every row is at night, its median power is 1.0 MW, and MODIS has never detected it. Two other weak, low-power night sources were seen only by Suomi NPP: S137 (50.815°N, 121.650°W; 42 dates, 2012–2016) and S133 (50.661°N, 120.061°W; 12 dates, 2013–2016). Neither has appeared since 2016. A second, independent search used a different grid and gave the same three sites. Kamloops is not a constant: 80% of its dates fall in June to September and it is almost never detected from November to February. In a quiet summer month near it, it makes up most of the Suomi NPP count: 87% (81–93%) within 25 km and 69% (62–77%) within 50 km. November and March–April burning is spread across valleys, not fixed points, and the south-west corner holds only 1–2% of it. These sources barely move the MODIS-to-VIIRS ratio for the whole box, but they halve the quiet-month ratio in a circle around Kamloops.

## Evidence

Terms used below. A **date** is a distinct local date on which a place had at least one hotspot. The **top-year share** is the fraction of a place's dates that fall in its busiest year: high means one fire year, low means spread over many years. A **quiet month** is defined in each table. Intervals are 95% ranges from resampling whole years (1,000 draws). All VIIRS rows were used for the search, including rows with `use == False`. The share and ratio tables use the standard filter.

**Check numbers reproduced** (standard filter, standard rows, 116 stable months): MODIS 48,233 and Suomi NPP 198,916, a ratio of 0.2425 (0.343 by day and 0.177 at night).

**1. Candidate fixed sources.** The search used 500 m cells, with each cell's dates pooled over its 3 × 3 neighbours (1.5 km). It covered all three VIIRS satellites, 2012 to October 2026. Values are for rows within 1 km of each site (1.5 km for Kamloops).

| Site | Lat, lon | Dates (rows) | Years | Night share | Median power (MW) | Satellites (dates) | MODIS ever, within 1.5 km | FIRMS type |
|---|---|---|---|---|---|---|---|---|
| K136 Kamloops | 50.688, −120.408 | 712 (921) | 15, 2012–2026; top year 10% | 100% | 1.0 | SNPP 445, NOAA-20 307, NOAA-21 135 | 0 | 2: 711; 0: 152; empty (near-real-time): 58 |
| S137 | 50.815, −121.650 | 42 (43 night rows) | 2012–2016; 15, 13 and 11 dates in 2013–15 | 100% | 0.34 | SNPP only | 0 | 0 |
| S133 | 50.661, −120.061 | 12 (12) | 2013–2016 | 100% | 0.44 | SNPP only | 0 | 0 |

All three peak at about 02:00 local time and are concentrated in June to September (80%, 95% and 92% of dates). The type label is unreliable even at Kamloops. Type-0 rows continue after FIRMS began labelling the site type 2 in June 2015: 70 such rows from 2016 to 2026, as well as 82 from 2012–2015. The other 31 type-2 rows in the archive are MODIS fire pixels of 7.7–407 MW in 2018–2023 and 2026. **Places that recur but are not fixed:** a Revelstoke-area place at 50.97, −118.33 (18 dates in 10 years, day and night, 4 MW, March–April and October–November, also seen by MODIS). There are also about a dozen day-only places near Hope and the Fraser Valley (5–24 dates each, 13:00 local, 2–4 MW, seen by all VIIRS satellites). Other night places with 9–12 dates are episodic, for example 49.26, −120.75, where 8 of 9 dates are in November.

**How the list changes with thresholds** (sites are counted as local maxima at least 3 km apart; maximum top-year share 0.5):

| Minimum dates / years | Sites, any hour | Sites, ≥ 80% night | Night sites named |
|---|---|---|---|
| 20 / 8 | 1 | 1 | Kamloops |
| 10 / 8 | 7 | 1 | Kamloops |
| 10 / 5 | 44 | 5 | Kamloops, S137, plus 3 sites with 10–12 dates (Revelstoke 50.99, −118.28; 49.26, −120.75; 52.49, −120.87) |
| 10 / 3 | 95 | 12 | as above, plus episodic sites |
| 5 / 3 | 603 | 115 | mostly fire-year places |

A grid shifted by 250 m gives 613, 96, 44 and 4 sites in the matching rows. With eight or more years required, Kamloops is the only night site at every date threshold. Every loosening adds places whose dates cluster in the 2017, 2018, 2021 and 2023 fire years.

**MODIS-only screen, 2000–2011** (added by the reviewer). This used 1 km cells pooled over 3 km. With at least 10 dates, 5 years and a top-year share of 0.4 or less, 38 cells pass, and none has a night majority. The top site has 23 dates. All of them are fire places of 7–56 MW, among them the Revelstoke place (50.99, −118.20; 19 dates, 7 years, all daytime).

**2. Kamloops share of the monthly Suomi NPP count.** Months run from 2012-02 to 2026-10, less 10 outage months, which leaves 167 months in 15 years. "Rest" means the circle count under the standard filter. Months with a total of zero are kept and add zero to both sums.

| Circle | Quiet definition | Months (zero-total) | Pooled share | Interval |
|---|---|---|---|---|
| 25 km | rest ≤ 20 | 155 (31) | 54% | 44–65% |
| 25 km | June–September and rest ≤ 20 | 49 (2) | 87% | 81–93% |
| 25 km | November–March | 70 (22) | 4.1% | 2.5–6.2% |
| 50 km | rest ≤ 20 | 126 (10) | 39% | 30–47% |
| 50 km | June–September and rest ≤ 20 | 47 (1) | 69% | 62–77% |
| 50 km | November–March | 70 (6) | 0.5% | 0.3–0.8% |
| Box | fire-season months with rest ≤ 36 (the m07 definition) | 20 of 116 stable | 17.5% | — |
| Box | rest ≤ 300 | 78 of 116 stable | 3.1% | — |

Kamloops adds on average 2.6 Suomi NPP rows per stable month. By calendar month the average is 0 in December and January, 0.1 in November, 1.6 in April, 8.7 in July and 0.7 in October. S137, measured over 2013–2016 only (4 years, so its interval is weak), was 95% (86–100%) of the June–September count within 25 km and 20% (12–25%) of quiet months within 50 km.

**3. November and March–April by sub-region.** Data: Suomi NPP, standard filter. November covers 13 Novembers from 2012 to 2025, without 2024, with 18,823 hotspots. March–April covers 14 years with 2,230 hotspots. Sub-regions are equal thirds of the box in latitude and in longitude.

| Area | November share (interval) | November day share | March–April share (interval) | March–April day share |
|---|---|---|---|---|
| South-centre | 24.8% (20.7–29.2) | 48% | 16.6% (13.0–21.3) | 70% |
| South-east | 18.8% (17.1–20.3) | 49% | 9.1% (5.7–13.2) | 60% |
| Centre-centre | 16.9% (14.1–19.1) | 60% | 13.3% (10.3–16.8) | 60% |
| North-west | 8.0% (6.5–9.7) | 71% | 32.5% (28.0–37.5) | 53% |
| South-west third | 5.0% (3.7–6.9) | 62% | 4.0% (2.7–5.7) | 78% |
| SW corner (lat < 49.6, lon < −121.5) | 1.9% (0.9–3.3) | 67% | 2.8% (1.6–4.3) | 91% |
| SW corner (lat < 49.4) | 1.1% (0.5–2.2) | 60% | 2.6% (1.6–3.9) | 90% |

November is 54% daytime (55% in the 10 stable Novembers), against 36% in June to September. Only 0.5% of November hotspots fall in 2 km cells that were active in 5 or more of the 13 Novembers.

**4. MODIS/Suomi NPP ratio in quiet months** (116 stable months, standard rows, year-block intervals):

| Months selected by | Months | All hours, standard filter | All hours, Kamloops added back | Night, standard | Night, Kamloops added back |
|---|---|---|---|---|---|
| Box Suomi NPP ≤ 300 (analyst) | 78 | 0.239 (0.198–0.275) | 0.232 | 0.080 (0.059–0.093) | 0.075 |
| Box MODIS ≤ 67 (same number of months) | 78 | 0.216 (0.189–0.237) | 0.210 | 0.081 (0.058–0.098) | 0.076 |
| Calendar November–April | 58 | 0.239 (0.217–0.261) | 0.238 | 0.079 (0.065–0.093) | 0.079 |

In the 25 km Kamloops test circle the quiet-month ratio falls from 0.180 to 0.083 when the static rows are added back, with months selected on Suomi NPP (107 months, only 43 MODIS hotspots). With the same number of months selected on MODIS it falls from 0.129 to 0.066. At 50 km it falls from 0.210 to 0.118, or from 0.141 to 0.091.

## What this implies

- One fixed source, Kamloops, adds counts to VIIRS only, and it does so at different rates in different months. Removing its rows handles this. Subtracting a monthly constant would over-correct in winter and under-correct in July. The existing `static_site` flag catches all 921 rows, but a type filter does not: 210 rows would remain.
- S137 and S133 behave like Kamloops (night, below 0.5 MW, summer, one place) but stopped in 2016. Removing them changes only circles within about 25 km of them, in 2012–2016.
- Nothing else in the box looks like a fixed source. A mask based on persistence would mainly remove places that burned in several fire years and valley-scale November burning. Under the challenge, that is burning activity.
- The low quiet-season night ratio (about 0.08, against 0.18 for all months) holds whichever way the months are selected, and the static sources do not cause it. The all-hours quiet ratio depends on the selection (0.216 to 0.239).

## Limits

- Sources too weak or too cloudy to reach about 5 dates are not found. Before 2012 only MODIS could be searched, and MODIS cannot see sources of the Kamloops kind.
- None of the sources is identified. Whether S137 and S133 stopped or merely fell below detection cannot be told from the data.
- Shares in quiet months near Kamloops rest on 15 years, and those near S137 on 4 years. The S137 intervals are not reliable.
- The sub-regions are arbitrary thirds of the box. Only Suomi NPP was used for sections 3 and 4.

## How it was computed

The analyst's scripts `a12_cells.py`, `a12_sources.py`, `a12_shares.py`, `a12_regions.py`, `a12_regions2.py`, `a12_ratios.py` and `a12_final.py` were re-run from a clean start, and all 14 output files were byte-identical. Reviewer scripts: `scripts/a12-static-sources_review.py` does the independent neighbourhood-pooled search with a shifted grid, the threshold sweep, the MODIS 2000–2011 screen, the shares (computed both with near-real-time rows and with standard rows only), the regions, and the quiet ratios under three selections. `scripts/a12-static-sources_review_mask.py` writes `out/a12_rev_fixed_source_mask.csv`. Outputs are in `out/a12_rev_*.csv`, with the log in `out/a12_rev_log.txt`.
