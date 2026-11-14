# How do the cleanest sensor pairs compare?

## Answer

In the stable-orbit period (February 2012 to December 2021, 117 months), Aqua MODIS recorded 0.113 hotspots for every Suomi NPP VIIRS hotspot. That figure blends two very different ratios: 0.20 by day and 0.055 by night. The year-to-year swing in the combined ratio (0.10 to 0.155) is mostly a change in the share of fire activity seen at night. Terra recorded 0.72 of Aqua's daytime hotspots and 2.2 times its night hotspots (2003–2021). The day ratio is steady across years, and the night ratio is not. The three VIIRS satellites agree on monthly hotspot counts to within about 2–4% overall and about 0% at night. By day, Suomi NPP ran about 8% above both NOAA satellites in 2023–2026. Single months scatter by about ±20% even between two VIIRS satellites. NOAA-21 fire radiative power per hotspot runs about 15% higher than NOAA-20's, so the satellites are interchangeable for counts but not for fire radiative power.

## Evidence

Common rules: standard (science-quality) rows only, type 0 (vegetation fire) only. Ratios are first sensor ÷ second sensor. "Ratio of sums" means total hotspots of A ÷ total of B over the unmasked months. Every month that overlaps a `gap` or `partial` row in `outages.csv` for either sensor is masked. The month key is the UTC month. Two kinds of 95% interval are given. "Month CI" comes from a bootstrap that resamples single months. "Year CI" comes from a bootstrap that resamples whole calendar years, which respects the fact that months within one fire season are correlated. The year CI is the honest one.

**Table 1. Ratio of sums by pair (all months in window, zero months included in sums)**

| Pair, window | Months used (masked) | Day/night | Hotspots A / B | Ratio | Month CI | Year CI | Range of yearly ratios |
|---|---|---|---|---|---|---|---|
| P1 Aqua/SNPP, 2012-02 to 2021-12 | 117 (2) | all | 22,458 / 199,086 | 0.113 | 0.106–0.125 | 0.109–0.130 | 0.100–0.155 (10 yr) |
| | | day | 15,888 / 78,642 | 0.202 | 0.193–0.220 | 0.194–0.232 | 0.189–0.275 |
| | | night | 6,570 / 120,444 | 0.055 | 0.039–0.061 | 0.026–0.059 | 0.006–0.062 |
| P2 Terra/Aqua, 2003-01 to 2021-12 | 224 (4) | all | 37,367 / 33,433 | 1.12 | 1.04–1.19 | 1.05–1.16 | 0.88–1.22 (19 yr) |
| | | day | 17,510 / 24,506 | 0.715 | 0.69–0.75 | 0.69–0.76 | 0.65–0.89 |
| | | night | 19,857 / 8,927 | 2.22 | 2.00–2.62 | 2.06–2.78 | 1.6–10.8 |
| P3 NOAA-20/SNPP, 2018-04 to 2026-07 | 88 (12) | all | 184,933 / 187,632 | 0.986 | 0.94–1.01 | 0.94–1.02 | 0.92–1.13 (9 yr) |
| | | day | 64,803 / 67,351 | 0.962 | 0.89–1.01 | 0.90–1.00 | 0.89–1.12 |
| | | night | 120,130 / 120,281 | 0.999 | 0.97–1.04 | 0.96–1.05 | 0.94–1.19 |
| P4 NOAA-21/NOAA-20, 2023-04 to 2026-07 | 35 (5) | all | 64,071 / 65,080 | 0.984 | 0.91–1.04 | 0.88–1.03 | 0.87–1.04 (4 yr) |
| | | day | 21,409 / 20,813 | 1.03 | 0.93–1.10 | 0.89–1.07 | 0.84–1.07 |
| | | night | 42,662 / 44,267 | 0.964 | 0.90–1.02 | 0.87–1.01 | 0.87–1.02 |

Masked months: P1 2020-08 and 2020-09 (Aqua). P2 2003-12 and 2016-02 (Terra), plus 2020-08 and 2020-09 (Aqua). P3 2022-07, 2022-08, 2024-02 to 2024-04, 2024-11, 2025-07 and 2026-03 to 2026-07. P4 2024-02 to 2024-04, 2025-07 and 2025-10. P4 also starts at 2023-04 because NOAA-21 data begin on 2 March 2023. Adding March 2023 back changes nothing (0.985). Keeping the partial-loss months and masking only full gaps changes no ratio by more than 0.001.

**Table 2. Single-month ratios, months with at least 20 hotspots from both sensors**

| Pair | Day/night | Eligible months (share of B's hotspots) | Median [10th–90th percentile] | Mean of monthly ratios | Log-log slope (95% CI) | Quiet / busy half |
|---|---|---|---|---|---|---|
| P1 | all | 45 (98%) | 0.120 [0.088–0.175] | 0.131 | 0.95 (0.90–1.01) | 0.119 / 0.113 |
| P1 | day | 44 (97%) | 0.214 [0.165–0.307] | 0.227 | 0.95 (0.88–1.02) | 0.211 / 0.202 |
| P1 | night | 15 (88%) | 0.057 [0.027–0.086] | 0.059 | 1.01 (0.84–1.18) | 0.049 / 0.061 |
| P2 | day | 82 (95%) | 0.76 [0.60–0.96] | 0.76 | 0.97 (0.93–1.00) | 0.76 / 0.71 |
| P2 | night | 29 (96%) | 1.97 [1.46–5.12] | 2.64 | 0.86 (0.73–0.97) | 2.96 / 1.99 |
| P3 | all | 73 (99.9%) | 0.97 [0.80–1.19] | 1.00 | 0.99 (0.97–1.00) | 1.04 / 0.985 |
| P4 | all | 30 (99.9%) | 0.95 [0.77–1.18] | 0.95 | 1.02 (0.99–1.05) | 0.94 / 0.99 |

The log-log slope is the slope of log(A) against log(B) across eligible months; a slope of 1 means the ratio does not depend on how busy a month is. The quiet and busy halves split the eligible months at the median count of sensor B. The threshold of 20 drops many months, mostly winter months (for P1 night, 102 of 117 are dropped), but the dropped months hold only 0.1–12% of sensor B's hotspots. Across thresholds of 5, 10, 20, 50 and 100, the median moves within 0.214–0.217 for P1 day, within 0.971–0.981 for P3 and within 0.925–0.974 for P4. The P1 night median moves within 0.037–0.061. The mean of monthly ratios sits above the ratio of sums for P1 (0.131 against 0.113). The two summaries are not interchangeable.

**Day/night composition.** By day, Aqua sees 0.20 per SNPP hotspot; by night, 0.055 (day ÷ night = 3.7, year CI 3.3–7.5). Across the 10 years, the all-rows P1 ratio correlates at −0.84 with SNPP's night share, which ranges from 39% to 65%. For Terra/Aqua by day, the sub-period ratios are 0.74 (2003–08), 0.75 (2009–14), 0.71 (2015–19) and 0.67 (2020–21), with no significant yearly trend (p = 0.84). The all-rows rise to 1.16 after 2015 comes from busier night seasons, not a change in the day ratio.

**Table 3. The three VIIRS satellites on the same 29 unmasked months (2023-04 to 2026-07; month CI)**

| | All | Day | Night |
|---|---|---|---|
| NOAA-20/SNPP | 0.98 (0.88–1.10) | 0.91 (0.81–1.03) | 1.02 (0.91–1.15) |
| NOAA-21/NOAA-20 | 0.985 (0.89–1.06) | 1.01 (0.90–1.11) | 0.97 (0.88–1.05) |
| NOAA-21/SNPP | 0.967 (0.91–0.99) | 0.92 (0.87–0.95) | 0.99 (0.92–1.03) |

**Same-day comparison** (local solar days in unmasked months on which both satellites recorded at least one hotspot; CI from a bootstrap over days):

| Pair | Shared days (A only / B only) | Count ratio | FRP ratio | FRP ratio without top 5 days | Median FRP per hotspot, A / B (MW) |
|---|---|---|---|---|---|
| NOAA-20/SNPP | 1,262 (197 / 180) | 0.986 (0.96–1.02) | 0.99 (0.90–1.09) | 0.99 | 4.18 / 4.12 |
| NOAA-21/NOAA-20 | 519 (72 / 87) | 0.968 (0.91–1.02) | 1.18 (0.96–1.42) | 1.10 | 4.75 / 4.06 |
| NOAA-21/SNPP | 455 (87 / 78) | 0.945 (0.89–1.00) | 1.12 (0.96–1.28) | 1.07 | 4.56 / 4.00 |

FRP is fire radiative power. On shared days, the median daily NOAA-21 FRP ratio is 1.12 against both other satellites. The NOAA-21/NOAA-20 FRP ratio on shared days swings from 0.73 to 1.33 between years, and the five biggest days hold 32% of all FRP. Even on the same day, the daily count ratio has a 10th–90th percentile range of 0.5–2.

## What this implies for the approach

- **Unit and scaling:** A single MODIS-to-VIIRS count factor mixes a day factor of about 0.20 with a night factor of about 0.055. Its value then depends on each month's night share. Factors split by day and night are more stable than one factor. The night factors (P1 night and Terra/Aqua night) are unstable from year to year, and they rest on 15 and 29 usable months. Slopes near 1 for the main relationships do not justify a fitted curve over a simple ratio.
- **Target record:** Going from MODIS to VIIRS multiplies MODIS counts by about 5 by day and about 18 by night. Any MODIS-era month inherits a single-month error of about −25% to +45% (P1 day, 10th–90th percentile 0.165–0.307 around a median of 0.214).
- **Combining VIIRS satellites:** For counts, the three satellites can be pooled or swapped with an adjustment of 0–4% overall. That is smaller than the ±20% single-month scatter between satellites with identical instruments. A daytime offset of about 8% (Suomi NPP higher, 2023–2026) is the largest systematic difference. Whether to correct it is a judgement call, given the 4-year record. For FRP, NOAA-21 should not be treated as interchangeable without about a 10–15% adjustment.
- **The ±20% floor:** Two satellites with identical instruments and the same overpass time still disagree by ±20% in a single month. A calendar should not present month-to-month differences smaller than that as real, whatever harmonization is chosen.
- **MODIS since 2022:** The Terra/Aqua day ratio was already lower in 2020–21 (0.67 against about 0.74 before). That fits an early drift effect but also matches other busy years (0.65 in 2017). Using 2020–21 inside the stable baseline is therefore a mild risk.

## Limits

- Hotspot counts only. There is no spatial matching of individual hotspots, and no unit other than counts and FRP sums was tested.
- NOAA-21 overlaps the others for 4 seasons (29–35 usable months). The year CIs for P4 and the triangle rest on 4 resampled years and are rough.
- P1 and P2 totals are dominated by 2021, which holds 50% of SNPP's P1 hotspots and 32% of Aqua's P2 hotspots. Leaving out any one year moves P1 within 0.112–0.118 and P2 within 1.08–1.12.
- Months are UTC. Terra's night pass (about 21:45 local, 05:45 UTC the next day) can shift the last evening of a month into the next UTC month. This is a small effect that was not corrected.
- The cause of NOAA-21's higher FRP was not established.

## How it was computed

`scripts/m03_pairs.py` (the analyst's script) was re-run unchanged and reproduced every draft number. `scripts/m03-like-for-like-pairs_review.py` is independent. It filters standard type-0 rows, builds masks from `outages.csv`, and builds monthly counts per sensor, UTC month and day/night. From these it computes ratios of sums, month and year-block bootstraps (4,000 resamples), leave-one-year-out ranges, threshold sensitivity (5–100), log-log slopes with bootstrap CIs, a gap-only masking sensitivity, the VIIRS triangle on common months, and same-day count and FRP ratios. The outputs are `out/m03-like-for-like-pairs_review_*.csv`, with the printed log in `out/m03-like-for-like-pairs_review_log.txt`.
