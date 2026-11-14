# Does any refinement of the factor beat one all-hours factor?

## Answer

No. None of the six refinements labels months better than one all-hours factor (U1) by more than the spread, in either test, on the whole box or on the 100 km circles. In the mixed-era test the largest fire-season gain in the box is +0.3 points (U1G, interval −0.7 to +1.2). The split-to-split standard deviation of these differences is 1 to 5 points. The day and night split can be repaired only partly. A seasonal night factor (U2S) brings the fire season level with U1 (+0.1 points), but over all months it is still 4.7 points worse (−7.3 to −2.6). Using day and night factors only in April to October (U2F) is level with U1 over all months (−1.3, −2.9 to +0.4). U2F is the only design that removes the fire-season typical-month bias: the geometric mean of converted over actual is 0.98 (0.90 to 1.07), against 1.14 (1.03 to 1.26) for U1. It does this without a loss in classes that the tests can show. Its box point estimates are still 2 to 3 points lower, and losses of up to 5 to 9 points cannot be ruled out. No design removes the typical-month bias outside the fire season. There every design converts typical November-to-March months too low (U1: 0.66, 0.54 to 0.79), which contradicts the documents' statement that one factor runs high in quiet periods.

## Evidence

**Data.** All figures use standard rows with `use == True`, local-date months, the whole box, and the 116 stable-orbit months. MODIS is Terra plus Aqua, and the reference is Suomi NPP. The check numbers reproduce exactly: 48,233 MODIS and 198,916 Suomi NPP hotspots, ratio 0.2425 (0.343 by day, 0.177 at night). Every factor is a ratio of sums (MODIS over Suomi NPP) unless stated. It is fitted on the whole box, only on the years a test allows, and applied unchanged to circles.

**Designs.**
- U1: one all-hours factor.
- U2: separate day and night factors.
- U2S: as U2, with the night factor fitted separately for June to August and for the other months.
- U2F: day and night factors fitted on April to October and used there, plus an all-hours factor fitted on November to March. A variant that uses U1's factor in November to March gives results within 0.003 of U2F.
- U1M: separate all-hours factors for April to October and for November to March.
- U1Z: a size-dependent factor. ln(M+1) = a + b·ln(S+1) is fitted on box months (M = MODIS count, S = Suomi NPP count) and then inverted. The box month's MODIS count sets the factor, which ranges from 0.21 to 0.23 between 5 and 5,000 hotspots, against 0.2425 for U1.
- U1G: the geometric mean of the yearly ratios.

As an extension, I also tested U1Zf, which regresses ln(S+1) on ln(M+1) directly.

**Zeros, outages and unclassifiable months.**
- The months 2016-02, 2020-08 and 2020-09 are left out of every fit and score.
- Zero counts stay in all sums and medians.
- No box month is unclassifiable.
- At 100 km, every truth baseline median is at least 1. Each design classes 99.2% of circle-months.
- Scores use the months that every design can class.
- The geometric-mean bias leaves out months with zero actual counts (1 box month) and months where the converted value is zero. U1 has 1 of 67 such box months in the fire season, 3 of 48 in November to March, and 39 of 1,270 circle months with at least 10 Suomi NPP hotspots. A version that keeps zeros, the geometric mean of (converted+1)/(actual+1), is lower everywhere (for example, U1 in November to March: 0.58).

**Protocol B, exact agreement minus U1 (points).** These are the 202 splits defined in SPEC. Intervals are 95% from 2,000 resamples of the ten classed years. SD is the standard deviation of the difference across splits.

| Design | Box, Apr–Oct | Box, all months | Box, Nov–Mar | Circles, Apr–Oct | Circles, all months |
|---|---|---|---|---|---|
| U1 exact agreement | 84.4% | 79.7% | 73.1% | 77.4% | 74.4% |
| U2 | −1.3 (−4.8, +2.0); SD 4.5 | **−6.9 (−10.2, −3.9)** | **−14.9 (−21.3, −7.7)** | +0.7 (−0.6, +1.8) | **−1.9 (−3.4, −0.6)** |
| U2S | +0.1 (−3.6, +3.3); SD 4.6 | **−4.7 (−7.3, −2.6)** | **−11.4 (−16.2, −6.2)** | −0.4 (−1.8, +0.9) | −0.9 (−2.0, +0.3) |
| U2F | −2.0 (−5.3, +1.3); SD 5.2 | −1.3 (−2.9, +0.4) | −0.4 (−2.0, +1.5) | +0.6 (−0.7, +1.8) | +0.4 (−0.4, +1.0) |
| U1M | +0.1 (−0.3, +0.5); SD 1.1 | −0.1 (−0.9, +0.8) | −0.4 (−2.0, +1.5) | +0.1 (0.0, +0.1) | 0.0 (−0.1, +0.1) |
| U1Z | −1.7 (−3.7, +0.2); SD 4.7 | −1.3 (−3.0, +0.4) | −0.7 (−4.0, +2.6) | **−2.0 (−2.6, −1.5)** | **−0.7 (−1.1, −0.3)** |
| U1G | +0.3 (−0.7, +1.2); SD 2.5 | −0.5 (−1.8, +0.6) | −1.5 (−4.2, +1.1) | **+0.3 (+0.1, +0.5)** | −0.1 (−0.4, +0.1) |
| U1Zf (extension) | **−2.6 (−4.6, −1.1)** | +0.2 (−1.4, +2.2) | **+4.3 (+0.1, +9.0)** | **−0.9 (−1.4, −0.3)** | **+0.6 (0.0, +1.1)** |

Bold marks intervals that exclude zero. The circle intervals are narrow because all 31 circles share the same ten years. In the reversed chronological split (2017–2021 as the MODIS era), U2F loses 8.6 points in the box fire season, and U2S and U2 each lose 2.9.

**Protocol A, box (leave one year out).** The typical-month bias is the geometric mean of converted over actual. Agreement means the same five-class label as the actual value, against a baseline of the other nine Suomi NPP years.

| Design | Median abs. error, Apr–Oct | Bias, Apr–Oct | Bias, Nov–Mar | Bias, all months | Agreement minus U1, Apr–Oct (points) |
|---|---|---|---|---|---|
| U1 | 0.33 | 1.14 (1.03–1.26) | 0.66 (0.54–0.79) | 0.91 (0.83–1.00) | 0 (U1: 69%) |
| U2 | 0.28 | 0.99 (0.91–1.07) | 0.52 (0.43–0.62) | 0.76 (0.71–0.82) | −2.9 (−8.8, +2.9) |
| U2S | 0.34 | 1.07 (1.00–1.15) | 0.60 (0.50–0.72) | 0.85 (0.79–0.91) | −2.9 (−9.4, +4.3) |
| U2F | 0.29 | 0.98 (0.90–1.07) | 0.67 (0.54–0.80) | 0.84 (0.77–0.91) | −2.9 (−8.8, +2.9) |
| U1M | 0.33 | 1.14 (1.03–1.26) | 0.67 (0.54–0.80) | 0.92 (0.83–1.01) | 0.0 |
| U1Z | 0.33 | 1.27 (1.16–1.41) | 0.73 (0.60–0.85) | 1.01 (0.92–1.11) | −1.5 (−7.8, +4.4) |
| U1G | 0.32 | 1.07 (0.97–1.19) | 0.62 (0.51–0.74) | 0.86 (0.78–0.95) | **−5.9 (−10.6, −1.4)** |

In the circles, U2F's fire-season bias is 0.93 (0.86 to 1.01) against 1.05 for U1. Its agreement is +3.4 points (+0.6 to +6.0) over U1. U1Z's error is worse in the circles (0.39 against 0.34).

**Why the typical month is high in the fire season and low in winter.** The table splits box months into thirds by their Suomi NPP count. The ratios are ratios of sums.

| Season, size third | MODIS / Suomi NPP | Day ratio | Night ratio |
|---|---|---|---|
| Apr–Oct, smallest | 0.345 | 0.58 | 0.12 |
| Apr–Oct, largest | 0.242 | 0.34 | 0.19 |
| Nov–Mar, smallest | 0.120 | 0.24 | 0.03 |
| Nov–Mar, largest | 0.251 | 0.38 | 0.09 |

Small fire-season months have a high ratio, so one factor converts them too high. Small winter months have a low ratio, so they are converted too low. Neither a season factor (U1M) nor a single size curve (U1Z) can follow two opposite slopes.

**Robustness 1: how far the factors move.** The test fits each half of the decade separately and converts the same 116 MODIS months with each fit. The table gives the implied all-hours factor, MODIS total over converted total, with an interval from 1,000 resamples within each half.

| Design | U1 | U2 | U2S | U2F | U1M | U1Z | U1G |
|---|---|---|---|---|---|---|---|
| 2017–21 / 2012–16 | 0.84 (0.77–0.92) | 1.18 (1.06–1.38) | 0.89 (0.85–0.97) | 0.96 (0.91–1.11) | 0.77 (0.67–0.89) | 0.83 (0.56–1.15) | 0.83 (0.73–0.93) |

The day factor falls from 0.424 to 0.328 in every split design. Split by season, the night factors hardly move: 0.198 against 0.192 in June to August, and 0.100 against 0.101 in other months.

**Robustness 2: converted 2003–2011 totals.** The MODIS input is 22,540 box hotspots, with 2003-12 left out because of a Terra gap. U1 converts them to 92,956 VIIRS-equivalent hotspots. The other designs, as a ratio to U1 with intervals from 1,000 refits on resampled years:

| Design | Ratio to U1 | Change if fitted on 2017–21 instead of 2012–16 |
|---|---|---|
| U2 | 0.93 (0.92–1.15) | −9% |
| U2S | 1.03 (1.01–1.08) | +13% |
| U2F | 0.97 (0.95–1.04) | +8% |
| U1M | 1.00 (0.97–1.02) | +26% |
| U1Z | 1.09 (0.99–1.32) | +18% |
| U1G | 0.94 (0.88–1.03) | +21% |
| U1 | 1 | +19% |

Before 2012 the mix is different. Night is 33% of MODIS hotspots in 2003–2011, against 44% in the overlap years, and November to March holds 25% of them, against 10%.

## What this implies

- The team can say that, on ten overlap years, no refinement of the factor gave better calendar labels than one all-hours factor.
- The team cannot claim that splitting by day and night improves labels. U2F can be described as removing the fire-season typical-month bias with no class loss that the tests can show. It cannot be described as harmless, because its box point estimates are 2 to 3 points worse.
- Any statement that converted quiet months run high should be limited to April to October. Typical November-to-March months run about 25 to 35% low under every design.
- The choice of fit years moves converted pre-2012 totals by 8 to 26%. That is more than the choice of design moves them (within 10% of U1, except U1Z).
- The off-season undershoot matters more before 2012, when a quarter of MODIS hotspots fall in November to March.

## Limits

- The test rests on ten overlap years. Protocol B's intervals resample the classed years but do not refit the factors, so they understate the uncertainty from fitting on five years. Differences smaller than the split SD (1 to 5 points in the box) are not established.
- The circle intervals do not cover where the circles are placed.
- The truth is a nine-year Suomi NPP median, not a 24-year mixed baseline.
- Nothing can check the 2003–2011 totals.
- Only two forms of U1Z were tested.
- The current month is Suomi NPP only. NRT rows and the drift years were not tested.

## How it was computed

- The analyst's `f02_build.py`, `f02_run.py`, `f02_scoreB.py`, `f02_A.py`, `f02_A_offseason.py` and `f02_robust.py` were re-run from empty outputs. Every output file came out byte-identical.
- `f02-factor-refinements_review.py` is an independent rewrite that does not use the analyst's functions. It recomputes the check numbers, all designs plus the variants U2Fa and U1Zf, Protocols B and A, the size-third ratios, the halves and the 2003–2011 totals. It runs in under 20 seconds.
- Its tables are `f02_review_B.csv`, `f02_review_A.csv`, `f02_review_A_paired.csv`, `f02_review_month_ratios.csv`, `f02_review_halves.csv` and `f02_review_2003_2011.csv`.
