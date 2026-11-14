# Cross-check of the harmonization evidence files

Scope: the 14 topic files m01–m10, r01–r03 and q01, read in full. The quantities that differ between files, or are defined differently, were recomputed from the shared table. The scripts are `scripts/crosscheck_main.py` and `scripts/crosscheck_extra.py`. Their printed output is in `out/crosscheck_main_log.txt` and `out/crosscheck_extra_log.txt`, and their tables are in `out/crosscheck_*.csv`.

Recomputation conventions: rows of type 0, plus near-real-time rows, which have no type. Standard rows only for the stable period. November 2026 is left out. A month is masked when it overlaps a `gap` row for either sensor. The bootstrap resamples whole years (4,000 draws). All values are ratios of sums, MODIS divided by VIIRS, unless stated.

## Reconciled numbers

### 1. Terra+Aqua / Suomi NPP count ratio, stable-orbit period

| File | Value | Definition |
|---|---|---|
| m01 | 0.242 (0.237–0.268) | 116 UTC months, all calendar months; year-block interval |
| m07 | 0.242 (0.234–0.257) | Same 116 months; interval from resampling months |
| m02 | 0.243 (0.238–0.284) | 68 April–October months keyed by local date |
| m10 | 0.242 | 67 April–October months (zero months dropped) |
| m08 | about 0.25 | Circles of 50 km and larger, median across 31 circles |
| r03 | SNPP/Terra 7.66 and SNPP/Aqua 8.93 | Fire-season sums; equal to Terra/SNPP 0.131 and Aqua/SNPP 0.112 |
| Recomputed | **0.2424 (0.237–0.269)** for all 116 months; **0.2425 (0.238–0.284)** for 68 fire-season months | Yearly range 0.196–0.331 by calendar year and 0.192–0.404 by fire season |

**Value to use:** 0.242, with a year-block 95% interval of about 0.237–0.28. That is about 4.1 Suomi NPP hotspots per MODIS hotspot. The files agree on the value. They differ in the stated spread for two reasons. m07's month-bootstrap interval is narrower than the year-block one and should not be quoted. The yearly ranges also differ: 0.19–0.33 by calendar year (m07) against 0.19–0.40 by fire season (m01, m02, m10). The upper end is 2013's fire season (0.404).

m08 masks only February 2016 and says it is "the only outage in the period". That is wrong: the Aqua gap of 16 August to 2 September 2020 is also in the period. The effect is negligible: 0.2426 unmasked against 0.2425 masked. The two months hold 92 MODIS and 303 SNPP hotspots.

### 2. Day and night ratios, Terra+Aqua / Suomi NPP

| File | Day | Night | Definition |
|---|---|---|---|
| m01, m07 | 0.343 | 0.177 / 0.176 | All 116 months |
| m02, m10 | 0.339 | 0.184 | 68 fire-season months |
| m08 | 0.32–0.40 | 0.17–0.19 | Circles; 0.34 and 0.19 at 150 km |
| m05 | SNPP/MODIS 2.7 by day and 6.7 at night | | **Median of monthly ratios**, fire-season months with at least 20 hotspots on each side (31 and 23 months) |
| Recomputed | 0.343 (0.325–0.413) all months; 0.339 (0.323–0.435) fire season | 0.177 (0.124–0.187); 0.184 (0.155–0.191) | Year-block intervals |

**Value to use:** 0.34 by day and 0.18 at night, a ratio of about 1.9 between them. m05's 2.7 and 6.7 are medians of monthly ratios, not ratios of sums: 1/2.7 = 0.37 and 1/6.7 = 0.15. They should not be compared directly with the others. The night interval is lopsided because quiet years have very low night ratios (yearly minimum 0.03–0.05).

### 3. Aqua / Suomi NPP

| File | All | Day | Night | Yearly range (all) |
|---|---|---|---|---|
| m03 | 0.113 (117 months) | 0.202 | 0.055 | 0.100–0.155 (calendar years) |
| m02 | 0.112 (fire season) | | | 0.11–0.21 (fire seasons) |
| m10 | 0.112 | 0.201 | | 0.11–0.21 |
| m06 | 0.111 pooled; 0.130 median | 0.214 median | | 35 months with at least 10 hotspots in all four series |
| r03 | 1/8.93 = 0.112 | 1/4.98 = 0.201 | | |
| Recomputed | 0.1128 (0.109–0.130) all months; 0.1120 (0.109–0.136) fire season | 0.202 / 0.201 | 0.055 / 0.058 | 0.100–0.155 / 0.108–0.205 |

**Value to use:** 0.112–0.113, or about 8.9 Suomi NPP hotspots per Aqua hotspot. By day it is 0.20, about 5.0 per Aqua hotspot. At night it is 0.055, about 18 per Aqua hotspot. Every file agrees. The upper end of the yearly range depends on the period: 0.155 by calendar year, and 0.205 for the fire season, where 2020 counts only 5 months. m06's medians (0.130 and 0.214) are medians of monthly ratios on a filtered month set, not ratios of sums.

### 4. Terra / Aqua and Terra / Suomi NPP

m03 gives Terra/Aqua 0.715 by day and 2.22 at night for 2003–2021. r03 gives Aqua/Terra by day as 1.31 for 2003–2011 and 1.45 for 2012–2021, which is Terra/Aqua 0.76 and 0.69. These match m03's sub-period values: 0.74–0.75 before 2015 and 0.67–0.71 after. The recomputed Terra/SNPP values for the fire season are 0.131 all, 0.139 by day and 0.126 at night. They agree with m10 (0.139 and 0.126) and r03 (1/7.66).

### 5. Between VIIRS satellites

| Quantity | m02 | m03 | m04 | m05 | m09 | r03 |
|---|---|---|---|---|---|---|
| NOAA-20/SNPP | 0.99 pixels, 1.02 cell-days (2018–21 fire season) | 0.986 (88 months, 2018–26); day 0.962, night 0.999 | yearly 0.87–1.08 by day, 0.93–1.20 at night | median 0.98 (35 months) | 1/1.011 = 0.989 | 0.99 and 0.98 |
| NOAA-21/SNPP | – | 0.967; day 0.92 (29 common months) | – | – | 0.97 (14 months); 1/1.034 = 0.967 | 0.97; day 0.92 |
| Union/SNPP, cell-days | 1.23 (2 km, 2018–21) | – | – | – | 1.24 (5 km, two satellites); 1.37 (three) | – |
| Union/SNPP, pixels | 1.99 | – | – | – | 1.99 (two); 2.95 (three) | – |

**Values to use:** NOAA-20/SNPP about 0.99 (interval 0.94–1.02). NOAA-21/SNPP about 0.97 overall, and 0.92 by day. These rest on 4 seasons only. Single months scatter by ±15–20% between satellites (m03: 10th–90th percentile 0.80–1.19). There is no conflict between files.

### 6. Year the drift becomes visible

| Evidence | Terra | Aqua |
|---|---|---|
| Median local solar hour of fire-season hotspots (m04, recomputed) | Day 11.27 (2021), 11.07 (2022), 10.73 (2023), 9.34 (2026). First outside the stable 11.07–11.37 in **2023** | Day 12.95 (2021), 13.07 (2022), 13.15 (2023). Marginal in 2022, clear in **2023** |
| Day count ratio, observed over size-expected (m04) | 0.95, 0.81, 0.77, 0.70, 0.46 for 2022–2026. Correlation with overpass hour ρ = 0.64, p = 0.01 | No trend |
| Day count ratio, raw yearly (recomputed, against NOAA-20) | 0.148, 0.145, 0.131, 0.136 for 2022–25 (stable 0.127–0.212). **0.070 in 2026** | 0.253, 0.226, 0.236, 0.272; 0.184 in 2026 (stable 0.190–0.260) |
| Size-controlled shift, 2022–25 against 2012–21 (r03) | SNPP/Terra by day +12% (−13 to +43) | SNPP/Aqua by day −9% (−21 to +4) |
| m03 | Terra/Aqua by day 0.67 in 2020–21 against about 0.74 before: "fits an early drift effect" | – |
| sensor-reference, r02 (QFED) | Drift "began in 2020–2021"; Terra drifting since 2020 | Since 2022 |

**Reconciled:** the documented orbit drift starts in 2020–2022. In this box it first moves the local time of detections in **2023**: the Terra hotspot hours for 2020 and 2021 (11.37 and 11.27) are still inside the stable range. A count effect is **gradual from 2022–2023 for Terra daytime only**, roughly −10% to −25% against size-expected values in 2023–2025. It is **unmistakable only in 2026**, at about half of expected. No file shows a clear count effect for Aqua or for either night pass through 2025. m03's reading of 2020–21 as early drift is not supported by the overpass hours. It is equally explained by busy years (2017 also gave 0.65).

### 7. Agreement between sensor-own anomaly classes

| File | Exact class agreement | Within one class | Set |
|---|---|---|---|
| m05 | 71% (kappa 0.63, 0.49–0.77) | 98% | Whole box, 48 fire-season months, median floor 10 |
| m05 | 66–68% | 93–94% | Whole box, no floor (116 or 68 months) |
| m05 | 13 of 16 (81%) | 100% | 2022–2025, whole box |
| m08 | 0.57 / 0.59 / 0.73 | 0.80 / 0.84 / 0.93 | Circles of 50 / 100 / 150 km; chance level 0.20–0.24 |

These are consistent: agreement falls as the area shrinks. The whole box (about 390 km north to south and 320 km east to west) is larger than the 150 km circle. m05's own warning carries the weight: in near-normal months (0.5 to 2 times the median), agreement is 11 of 25 (44%).

### 8. Overpass times quoted in m10

m10 explains the night frp difference by Terra's night pass "at about 22:30 local time" and Suomi NPP's "01:30 pass". In this box the data put them at about 21:45 (21.65–21.93 h, 2016–2021) and 02:10 (1.85–2.30 h) local solar time (m04, m09, recomputed). The m10 times are wrong, but its reasoning survives with the correct times: Terra's night pass is about 4.4 hours earlier than VIIRS's.

### 9. The Kamloops static source

m08 says the persistent cell at 50.69°N, 120.41°W "has no static-source type". m07 shows, and the recomputation confirms, that FIRMS labels it type 2 from 2015: 345 rows in 2015–2021 and 366 rows in 2022–2026, against type 0 for 72 rows in 2012–2014 and for 33 and 47 rows later. Every row is at night, and MODIS has no rows there. m08 removed type 1–3 rows before counting, so it saw only the rows mislabelled as type 0. **m07 is correct.** The two files agree on what matters: the site adds about 2.6 SNPP hotspots a month, and it dominates small circles around Kamloops.

### 10. Suomi NPP in 2026

m04 uses only September and October 2026 for SNPP, "because SNPP has gaps from April to August". m09 says the listed gaps overstate the loss. The recomputation supports m09. Ratios of SNPP to NOAA-20 are 1.016 in July 2026 (18,067 / 17,781) and 0.964 in August (28,290 / 29,348). On the listed gap days of 10–17 July and 3–6 August, SNPP still recorded 324 and 5,303 hotspots, against 779 and 6,319 for NOAA-20. Masking under the outage rule is conservative but discards usable months. m04's switch to NOAA-20 as the 2026 reference is still sound. Both references give Terra daytime about 0.065–0.070 for 2026.

## Conflicting conclusions

**C1. Do day and night factors improve on one factor?** m03, m04, m06, m08, m05 and m10 say yes: split by day and night. m01 says the split "did not measurably improve" leave-one-year-out error (gain 4.9 points, −2.4 to 10.1), and that day and night yearly ratios are not steadier (CV 0.20 by day and 0.33 at night, against 0.23 combined).
*Recomputed.* On 47 fire-season months where both sensors have at least 10 daytime hotspots, the SD of the monthly log ratio is 0.35 for all-hours pixels and **0.45 for daytime pixels**. The leave-one-year-out median error is 28.7% for all hours and 24.0% by day. The bootstrap intervals overlap. m06 (Aqua 0.35 against 0.42) and m10 (0.50 against 0.56) found the same.
*Assessment.* Two separate claims are both true. The day and night ratios clearly differ, about 0.34 against 0.18. One factor is therefore biased whenever the day/night mix of a month differs from the baseline mix, for example in a small area, a quiet month, or near-real-time rows whose `daynight` follows a different rule. But splitting adds no measurable accuracy for whole-box monthly totals: the monthly scatter of daytime ratios is as large as or larger than that of all hours. m03's "more stable than one factor" holds for the day factor's year-to-year spread (m03 and m10: Aqua day CV 0.16), not for monthly prediction error. The case for splitting rests on bias under a changing mix, and on drift (C3), not on precision.

**C2. Daytime active cell-days as the stable unit.** m02 says daytime 2 km cell-days halve the year-to-year spread (CV 0.20 to 0.10), so that "one factor works".
*Recomputed at month level* (local-date months, 47 common months). The SD of the log ratio is 0.45 for daytime cell-days, against 0.39 for all-hours cell-days, 0.35 for all-hours pixels and 0.45 for daytime pixels. The median leave-one-year-out error is 20.0% for daytime cell-days, against 23.4%, 28.7% and 24.0%. Over all 64–67 non-zero months, the SDs are 0.51–0.58 for every unit.
*Assessment.* m02's gain is real at the level of a year or season. At the level of a month it shrinks to a modest gain in median error (about 20% against 24–29%) with overlapping intervals. m02 is right on level and activity-independence: daytime cell-days give a factor near 0.68 with a median month equal to the sum. It overstates how much more trustworthy a single month becomes.

**C3. Should a drift-period MODIS series be day-plus-night or split by day and night?** r03 says a combined day-plus-night factor held through 2022–2025, and a day/night split "would carry the drift error". m04 says "a day-plus-night total hides the problem; any unit should keep D and N separate".
*Recomputed, fire-season yearly ratios.*

| Series | Stable range | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|---|
| Terra+Aqua all hours / SNPP | 0.192–0.404 (2012–21) | 0.264 | 0.226 | 0.260 | 0.254 | – |
| Terra+Aqua all hours / NOAA-20 | 0.205–0.304 (2018–21) | 0.260 | 0.240 | 0.229 | 0.252 | **0.203** |
| Terra+Aqua day / NOAA-20 | 0.318–0.462 | 0.384 | 0.371 | 0.366 | 0.408 | **0.254** |
| Terra+Aqua night / NOAA-20 | 0.036–0.192 | 0.194 | 0.184 | 0.170 | 0.176 | 0.178 |
| Terra day / NOAA-20 | 0.127–0.212 | 0.148 | 0.145 | 0.131 | 0.136 | **0.070** |
| Aqua all hours / NOAA-20 | 0.107–0.153 | 0.124 | 0.110 | 0.102 | 0.116 | **0.088** |
| Terra+Aqua daytime 2 km cell-days / NOAA-20 | 0.657–0.762 | 0.742 | 0.753 | 0.730 | 0.790 | **0.626** |

*Assessment.* Both files are right about different things. The all-hours Terra+Aqua total did hold through 2025, and in 2026 it is at the bottom edge of the range (0.203). That is about 14% below the comparable large years, 2017 and 2021 (0.234–0.237). The holding is partly cancellation: Terra's day ratio fell while its night ratio rose. Nothing guarantees the cancellation will continue as the drift goes on. Any day-only unit, including m02's preferred daytime cell-days, is out of range in 2026. m02's statement that there is "no evidence for a separate drift-period factor" covers only 2022–2025. m04 is better supported for 2026, and for any daytime-based unit. r03 is better supported for the combined total in 2022–2025. m05's finding that drift did not change the anomaly labels in 2022–2025 rests on the same all-hours total, and was not tested for 2026.

**C4. Is there precedent for the target record?** r01 says "every published join (Vadrevu 2018, Zheng 2026, Chen 2026) treats VIIRS as the reference and adjusts MODIS". r02 says GFED5NRT (Chen 2026), GFAS and GBBEPx calibrate VIIRS to a MODIS-era reference, with only QFED 3.3 moving its anchor to NOAA-20.
*Assessment.* r02 is correct about Chen 2026: GFED5NRT fits VIIRS counts to MODIS-based GFED5 burned area. That is a MODIS-era target, and r01 mislabels it. Zheng 2026 does correct MODIS frp to VIIRS. The precedent is split. Research papers that correct frp at pixel level use VIIRS as the reference. Operational long-term systems keep MODIS-era continuity, and they are moving to VIIRS anchors as MODIS ends.

**C5. Seasonal factors.** r01 says "a seasonal or a view-angle-dependent factor" has published support. r02 says "no system uses seasonal factors". m01 found that calendar-month factors gave the only gain that excluded zero, 5.6 points over all months, but no clear gain in fire-season months, and the June factor flips with UTC against local dating. m08 found November's ratio matches the summer ratio.
*Assessment.* Li 2018 reports that the frp difference varies by season, but nobody implements seasonal count factors. The local evidence for them is weak and fragile. r02 and m01/m08 are better supported.

**C6. Does the ratio depend on activity?** m01's answer says there is "no consistent sign that the ratio changes with activity" (slope 0.94–1.09). Yet m01's own fire-season thirds fall from 0.31 to 0.28 to 0.24, and its Poisson slope is 0.96 (0.93–0.98), which excludes 1. m08 finds 0.35–0.37 in the quietest third of months against 0.24 in the busiest, at 100–150 km. m04 finds daytime ratios 0.03–0.04 lower per tenfold increase in year size. m02, m06 and m10 find daytime slopes below 1 (0.87–0.93) and night slopes above 1 (1.04–1.19).
*Assessment.* There is a mild activity effect in fire-season months, with quiet months about 25–50% higher than busy ones. It is the sum of a sub-unity day slope and a super-unity night slope, so the pooled slope near 1 hides it. m08 and m01's thirds are better supported than m01's summary sentence. The effect is smaller than the month-to-month scatter.

**C7. Is the VIIRS daytime offset worth correcting?** m03 reports SNPP about 8% above NOAA-20 and NOAA-21 by day in 2023–26 and calls correcting it a judgement call. m09 recommends scale factors of 1.011 for NOAA-20 and 1.034 for NOAA-21 (all hours). These do not contradict each other. The all-hours factors are within 1–4% of 1 and below the ±15–20% single-month scatter. The day-only offset matters only if day and night are carried separately.

**C8. frp scale against the literature.** Locally, Aqua frp by day is about equal to Suomi NPP's (1.01; year range 0.62–1.17; m10). r01 and r02 cite MODIS frp 20–50% below VIIRS, VIIRS nearly double Aqua after correction (Andela), and the GFAS factors of VIIRS × 1.23 by day and × 0.46 at night. These do not conflict with the local data. GFAS used the VIIRS 750 m product and the others used other regions. r01 itself cites the large-boreal-fire exception, where VIIRS frp is about 47% lower (Li 2018), which fits Interior BC. None of these factors carries over to this box.

## Evidence by choice

### (a) Target record: MODIS-equivalent or VIIRS-equivalent

- **Level:** VIIRS (SNPP) records 4.1 times the hotspots of Terra+Aqua, 8.9 times Aqua's, about 3 times by day and about 5.4 times at night. Both directions need the same factor. Converting VIIRS to MODIS-equivalent removes about three quarters of the counts, which makes quiet months noisier (m01). Converting MODIS to VIIRS-equivalent multiplies MODIS by 5 (day) to 18 (night) for Aqua (m03).
- **Detection:** at user scales (10–100 km circles), MODIS records nothing in 16–50% of the months in which SNPP saw fire (m08). No direction of conversion can restore those detections.
- **Stability over time:** VIIRS overpass times are constant across all three satellites (12.6–13.0 h and 1.85–2.30 h local solar; m04, m09). MODIS times move 2 hours by 2026. A VIIRS-equivalent target needs no model of future MODIS drift (m04), and q01 requires continuity through NOAA-20 and NOAA-21. A MODIS-equivalent record would have to be produced from VIIRS alone after 2027.
- **Independent check:** every sensor ranks years by BC burned area about equally well (Spearman 0.84–0.89; r03), so the burned-area record does not favour either target.
- **Precedent:** split (C4). The challenge author accepts either "if properly justified" (q01).
- **Strength:** the level numbers are strong, with a year-block interval about ±10%. The case for a direction rests on continuity and drift arguments, not on a measured difference in accuracy.

### (b) Unit: counts, active cell-days, frp or anomalies

- **Raw counts:** the stable factor is 0.242 (0.237–0.28). Single months scatter with an SD of the log ratio of 0.35–0.51 depending on the month set. The leave-one-year-out median error is about 14% for large months, 23% at a VIIRS count of at least 80, and 29–31% across all fire-season months (m01, m10, recomputed). The challenge wording names "number of hotspots" (q01).
- **Active cell-days (2 km):** the level is closer to parity: 0.65 all hours and 0.68 by day. By day the yearly CV halves (0.10, against 0.20 for pixels), the median month equals the sum, and there is no activity dependence (m02). At month level the gain is small: median error 20% against 24–29%, with overlapping intervals (C2). The unit removes MODIS overlap duplicates (m06: 21–23% of hotspots have a neighbour within half a pixel). It compresses big months (62,646 pixels become 8,053 cell-days). The union of satellites must not be taken (m02, m09). In 2026 the daytime cell-day ratio is out of range (C3).
- **frp:** worse than counts whenever night is included. Leave-one-year-out RMSE of the log is 0.66 against 0.50; frp is worse in 99% of resamples. By day it cannot be told apart from counts (0.60 against 0.63) (m10). Its only advantage is that Aqua by day sits at parity with SNPP (1.01). It is not in the challenge wording (q01). NOAA-21 frp per hotspot runs 12–18% above NOAA-20 (m03).
- **Sensor-own anomalies:** month order is preserved: Spearman 0.97 (0.94–0.99) on 48 floored fire-season months. The exact class agrees in 71% (kappa 0.63) of months, but in only 44% of near-normal months (m05). Labels change with the baseline years (8–21% of months) about as often as with the sensor. Agreement is 0.57–0.59 at 50–100 km circles, and the calendar-month MODIS median is zero for most fire-season months at 50 km and below (m08). A day-only anomaly would carry the 2026 Terra decline as a false fall in fire (m04). Neither r01 nor r02 found a precedent for anomalies or cell-days: the literature is silent on them, not negative.
- **Strength:** the ranking of counts against frp is strong. Cell-days against counts is moderate at season level and weak at month level. The anomaly agreement is moderate at box scale and weak below 100 km.

### (c) Scaling: one factor, day/night or seasonal factors, or a curve

- **One factor:** 0.242. It is defensible for large months and season totals (error about 10% for a season and about 14% for big months; m01).
- **Day and night factors:** 0.34 and 0.18. They clearly differ, but give no measurable gain in whole-box monthly accuracy (C1). They protect against changes in the day/night mix and against drift that differs by pass (C3). The night factor is unstable from year to year: the yearly range is 0.03–0.19 for Terra+Aqua and 0.006–0.062 for Aqua.
- **Seasonal factors:** weak (C5). The gain is significant only over all months (5.6 points, 0.6–13.2), the factors rest on 9–10 months each, and they are sensitive to UTC against local dating.
- **Curve or activity factor:** log-log slopes are 0.96–1.07 pooled, below 1 by day and above 1 at night. Quiet months run 25–50% higher than busy ones (C6). A fitted power law did not beat one factor out of sample (m01). m08 supports an activity factor only at 100 km and above.
- **Scan angle:** no filter or weighting. A near-nadir filter discards 27–37% of hotspots and does not reduce the monthly spread (m06).
- **Static source:** mask the Kamloops site before any scaling. It adds a constant 2.6 SNPP hotspots a month, never seen by MODIS, and up to 17% of a quiet month (m07). No scale factor can remove an additive offset.
- **Floor:** two identical VIIRS instruments still differ by ±15–20% in a single month (m03, m09). No scaling can make month-to-month differences smaller than that meaningful.
- **Strength:** strong that the form should be multiplicative and near-linear. Moderate for splitting by day and night. Weak for seasonal factors and curves.

### (d) Combining two or three VIIRS satellites

- NOAA-20/SNPP is 0.99 and NOAA-21/SNPP is 0.97 (0.92 by day), consistent across m02, m03, m05, m09 and r03. Single months scatter by ±15–20%.
- Summing satellites doubles or triples counts (1.99 and 2.95), and it adds the static source once per satellite (m07). Taking the union of cell-days inflates the count by 1.24 to 1.37 times, more in quiet years (m02, m09). Both create steps at April 2018 and March 2023, so a baseline must not be compared against a sum or a union.
- A daily mean over the satellites with data, scaled to SNPP (NOAA-20 × 1.011, NOAA-21 × 1.034), departs from its complete-month value by under 1% in the median and 1.5–11% at the 90th percentile in simulated outages. A naive monthly mean collapses about 30% in real outage months (July and August 2022), the max is biased upward, and a monthly reference fallback errs by 6–12% (m09).
- Precedent: GFED5NRT and GBBEPx average per satellite and fall back to whichever is available (r01, r02).
- The outage list overstates SNPP's 2026 gaps (reconciled number 10). An in-data availability check is needed.
- SNPP ended on 2 November 2026, so November 2026 changes from three satellites to two in mid-month (q01).
- **Strength:** strong. This is the best-supported choice in the set.

### (e) MODIS data since 2022

- The overpass hours move from 2023 (number 6). Terra's daytime count ratio declines gradually, to roughly 0.75–0.9 of expected in 2023–2025, then falls to about half in 2026 (0.070 against NOAA-20, stable 0.127–0.212). Aqua by day is at the bottom edge in 2026 (0.184). The night passes are inside their ranges (m04, recomputed).
- The all-hours Terra+Aqua total holds through 2025 and is at the bottom edge in 2026 (0.203 against 0.205–0.304). Every daytime-only series, in pixels or cell-days, is out of range in 2026 (C3).
- The independent burned-area record shows no MODIS-specific loss in 2022–2025. The size-controlled shift is −1% (−21 to +23) for SNPP/Terra and +5% for SNPP/Aqua. Hotspots per km² fell about 10% for MODIS and VIIRS alike (r03). The record has no 2026 data yet.
- Anomaly labels agree in 13 of 16 months in 2022–2025 (m05). Scan-position mix is unchanged (m06). Pass counts per day are unchanged (m09).
- Operational precedent avoids fitting on drift years: GFED5 stops in 2022, QFED fits on 2024, and GBBEPx fits on 2016–17 (r02).
- **Strength:** strong for Terra by day in 2026. Moderate for a gradual Terra daytime decline in 2023–2025. Weak, given only four years and wide intervals, for "no effect" on the combined total and on Aqua.

## Still missing

1. **A month-level, out-of-sample comparison of the full candidate pipelines on the same months.** One example: all-hours counts with one factor, against a day/night split, against daytime cell-days, scored on the same months by leave-one-year-out error. The pieces exist in m01, m02, m10 and here, but on different month sets and keys. This could change the unit choice (b), because C2 suggests the gain from cell-days is modest.
2. **Results at user scale for the shortlisted units.** m08 tested raw counts and anomalies on circles only. Cell-days, the day/night split and the VIIRS daily-mean rule were never tested at 25–100 km. This would affect (b) and (c), and the minimum area the app should allow.
3. **A 2026 burned-area check.** BC data for 2026 will not be published until April 2027. Without it, the 2026 Terra decline cannot be checked independently of VIIRS. This affects (e).
4. **The calibration factor for NOAA-20 or NOAA-21 against MODIS directly.** Every MODIS factor here goes through Suomi NPP, and the overlap with MODIS in stable orbit is SNPP only. NOAA-20 overlaps stable-orbit MODIS only in 2018–2021, 4 years, and NOAA-21 not at all. Since SNPP has ended, this bears on (a) and (d).
5. **Whether the outage list or in-data availability should define masked days.** 2026 shows the list overstates gaps. A per-day availability flag is needed to implement m09's rule. This affects (d).
6. **Near-real-time `daynight` rule effects.** The current month comes from near-real-time rows that classify day and night by orbit direction. Nobody measured how much that moves day/night counts compared with standard rows. This matters if (c) uses day/night factors.
7. **Pre-2012 behaviour.** No file tests whether the Terra-only period (2000–2002) or 2002–2011 needs different treatment beyond m05's baseline-sensitivity result (8–21% of labels change). This bears on how far back the calendar can claim comparability.
8. **Other static or industrial sources** outside the Kamloops site. m07 screened the box, but m08 did not screen other circles, and weak sources may sit below detection.
