# What has the MODIS orbit drift done to the relationship since 2022?

## Answer

Both MODIS satellites now observe this box at very different local times. By 2026 the median daytime hotspot time had moved from about 11.2 h to 9.3 h for Terra and from 12.9 h to 14.9 h for Aqua. The night passes moved by similar amounts. The VIIRS times did not move. The only large break in the count relationship is Terra daytime in 2026. Its ratio to NOAA-20 was 0.070 (7 months, 1,120 / 16,017 hotspots, month-bootstrap 95% interval 0.049–0.083), against a stable-orbit range of 0.123–0.267. That is about half of what a 2012–2021 factor predicts for a year of that size. Terra daytime was inside the stable range in 2022–2025. After adjusting for fire-year size, however, it fell steadily (0.95, 0.81, 0.77, 0.70 and 0.46 of the expected value in 2022–2026), in step with the earlier pass. So the 2026 drop is the end of a gradual decline, not a sudden step. Aqua daytime, Aqua night and Terra night show no departure that the spread can distinguish from noise and fire-year size.

## Evidence

**Terms.** *Ratio* means the sum of MODIS hotspots divided by the sum of VIIRS reference hotspots over the fire-season months (April to October) that are not masked, computed separately for the `daynight` labels D and N. This is a ratio of sums, not a mean of monthly ratios. A month is *masked* when it overlaps an outage-list `gap` for either sensor. *Stable range* means the minimum and maximum of the yearly ratios: 10 years (2012–2021) against Suomi NPP (SNPP), and only 4 years (2018–2021) against NOAA-20. A new year drawn from the same distribution falls outside a 10-year range with probability 2/11, about 18%.

**Overpass time.** The table shows the annual median local solar hour of fire-season hotspots. The stable figure is the range of the 10 annual medians for 2012–2021. Interquartile widths stay at 0.2–1.0 h throughout.

| | Stable 2012–21 | 2022 | 2023 | 2024 | 2025 | 2026 | First year outside |
|---|---|---|---|---|---|---|---|
| Terra D | 11.07–11.37 | 11.07 | 10.73 | 10.53 | 10.07 | 9.34 | 2023 |
| Terra N | 21.45–21.93 | 21.58 | 21.27 | 21.15 | 20.65 | 20.02 | 2023 |
| Aqua D | 12.78–13.05 | 13.07 | 13.15 | 13.52 | 14.25 | 14.85 | 2022 (by 0.02 h), clearly 2023 |
| Aqua N | 2.07–2.42 | 2.32 | 2.52 | 2.95 | 3.47 | 4.20 | 2023 |

VIIRS annual medians stayed within 12.6–13.0 h (day) and 1.85–2.30 h (night) for SNPP (2012–2026), NOAA-20 (2018–2026) and NOAA-21 (2023–2026). The standard deviation across years is 0.03–0.12 h, and the means before and after 2022 differ by at most 0.05 h.

**Count ratios.** The table gives yearly ratios. 2022 has 4 months against SNPP and 6 against NOAA-20. The 2026 SNPP value uses only September and October, because SNPP has gaps from April to August. The 2026 values below therefore use NOAA-20.

| Series | Stable range (SNPP, 10 yr) | Stable range (NOAA-20, 4 yr) | 2022 | 2023 | 2024 | 2025 | 2026 (NOAA-20) |
|---|---|---|---|---|---|---|---|
| Terra D | 0.123–0.267 | 0.127–0.212 | 0.167 | 0.127 | 0.133 | 0.126 | **0.070** [0.049–0.083] |
| Terra N | 0.070–0.137 | 0.066–0.129 | 0.131 | 0.120 | **0.149** | **0.143** | 0.137 [0.123–0.160] |
| Aqua D | 0.190–0.318 | 0.190–0.263 | 0.276 | 0.198 | 0.239 | 0.252 | 0.184 [0.181–0.272] |
| Aqua N | 0.000–0.063 | 0.000–0.062 | 0.051 | 0.059 | 0.054 | 0.042 | 0.041 [0.012–0.047] |

The 2022–2025 values in this table are SNPP ratios, and bold marks a value outside the 10-year SNPP range. Against SNPP, 3 of 20 drift-period cells fall outside, which is about the 3.6 expected by chance. Against NOAA-20, Terra N in 2025 and Aqua D in 2025 are outside the narrow 4-year range, but both move back inside once the `partial` outage months are also masked (0.121 and 0.258). Neither result is robust.

**Activity level.** Ratios depend on how large the fire year is. In stable years, a year ten times larger has a daytime ratio 0.03 lower for Terra and 0.04 lower for Aqua (r = −0.41 and −0.72). Two tests control for this:

1. *Fitted expectation.* A line fitted to the 10 stable SNPP years predicts 0.151 for Terra D at the 2026 size. The observed 0.070 is 0.46 of that. Small years make the residual standard deviation large (0.047), so the shortfall is only z = −1.7 on this test alone. Across all 15 years, observed/expected for Terra D tracks the overpass hour (Spearman ρ = +0.64, p = 0.01). There is no such link for Terra N (ρ = −0.34, p = 0.22), Aqua D (ρ = 0.03) or Aqua N (ρ = −0.04).
2. *Big months only* (at least 1,000 reference daytime hotspots, which also controls for month mix). Terra D was 0.108–0.274 in 11 stable months against SNPP and 0.121–0.213 in 5 against NOAA-20. In July 2026 it was 0.049 (285 / 5,836) and in August 2026 0.083 (793 / 9,554). Both are below every stable big month. Aqua D in those months was 0.180 and 0.183, at the bottom edge of its stable 0.178–0.330. Aqua N was 0.031 and 0.047, inside its stable 0.018–0.074.

**Night share.** Terra's night share was 0.80 in 2026, against 0.19–0.65 in stable years. Terra minus SNPP was +0.147 in 2026, against at most +0.005 before. This change comes from the fall in daytime counts. Night share also varies strongly with fire-year size, so on its own it is a poor indicator of drift.

**Checks that changed nothing.** Keeping the non-vegetation rows of types 1–3 (2,804 of 711,962 rows) to match the near-real-time rows, which carry no type, changes the ratios by at most 0.004. Grouping months by local date instead of UTC date moves 29 rows and leaves 2026 unchanged. The coverage holes between the standard and near-real-time files (Terra 30 Aug – 7 Sep 2026, Aqua 30–31 Aug) fall on days when NOAA-20 had only 13 hotspots. Using standard rows only for 2026 (April to July) gives Terra D 0.051.

## What this implies for the approach

- **MODIS since 2022 (choice e):** a single stable-orbit factor would overstate Terra daytime by about 2× in 2026, and probably by 20–30% in 2024–2025. Truncating Terra daytime, giving it a time-varying factor, or carrying it only as a flagged series are all supported. Aqua and the night passes show no measurable bias yet. Aqua's night pass is now at about 04:12, and 2026 sits 34% below expectation (z = −1.8), so this is a watch item.
- **Unit (b):** a day-plus-night total hides the problem. For Terra in 2026 the total ratio stays inside its range because the night ratio rises slightly as the day ratio falls. Any unit should keep D and N separate. Anomalies against each sensor's own history would carry the Terra daytime decline into the record as a false decline in fire activity.
- **Scaling (c):** factors need to be split by day and night, and they depend on fire-year size. A single constant is the weakest choice.
- **Target record (a):** VIIRS times are constant, so a VIIRS-equivalent target avoids having to model MODIS time drift going forward.
- **Combining VIIRS (d):** NOAA-20 to SNPP ratios were 0.87–1.08 by day and 0.93–1.20 by night in 2018–2025. That is close enough for NOAA-20 to stand in for SNPP as the 2026 reference, but not identical.

## Limits

- Fire activity is clustered in a few large fires, and the intervals resample months, so they are optimistic.
- The stable baseline includes tiny years (47–400 MODIS daytime hotspots). The ranges are therefore wide, and changes under roughly 20–30% in any single year cannot be detected.
- The link between the earlier Terra pass and lower counts rests on timing alone. No VIIRS morning pass exists to test the diurnal cycle directly.
- The size adjustment uses year size only. Fire location and fire type are not controlled.
- Nothing here predicts 2027, when both satellites are near the end of science operations.

## How it was computed

The independent recomputation is `scripts/m04-drift-effect_review.py`, with output in `out/m04-drift-effect_review.log` and `out/m04-drift-effect_*.csv`. It reproduces every analyst table to the third decimal. Its steps:

1. Filter to 2012-01 to 2026-10, months April to October, type 0 plus near-real-time rows.
2. Compute annual quantiles of local solar hour.
3. Compute masked ratios of sums, with a 4,000-draw bootstrap over months.
4. Run variants: partial outages masked, all types kept, August–September 2026 masked.
5. Run the big-month test.
6. Fit the size regression and test its residuals against overpass hour.

The analyst scripts are `scripts/m04_drift.py`, `m04_drift_followup.py` and `m04_check.py`. They were re-run cleanly.
