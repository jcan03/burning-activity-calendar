# Reconciliation of the thirteen method topic files

Checked 2026-11-14 against t01–t13 in this folder and against `docs/harmonization-evidence.md` (called "the evidence file" below). The topic files were not edited. Sources were re-opened from the copies the verifiers saved under `dl/` (their text was checked to be the named paper) or fetched fresh on the web; each check says which.

Overall result: the thirteen files agree with each other far more than they disagree. No fabricated citation was found among 27 sources checked. The real disagreements are about **fit** (how much a method could do for the team, and at what cost), not about what the sources say. The most consequential one is diurnal correction of the Terra drift (section 2.1).

---

## Same method, different descriptions

### 1.1 Same source, described differently

| Source | Files | Difference | Re-check (source re-opened) | Verdict |
|---|---|---|---|---|
| Fu et al. 2020, *Remote Sens.* 12:2870 | evidence file; t04 | The evidence file says MODIS missed 65% of VIIRS fire pixels in forest. t04 gives "35% of MODIS fire pixels had no VIIRS pixel" and "MODIS commission errors about 65% at 2–4 MW". Read side by side these look like one 65% used two ways. | `dl/t04/fu2020.txt`, abstract and Sect. 3: "Among fire pixels detected by VIIRS, 65% and 83% were missed by MODIS in forests and low-biomass lands … omission rates by VIIRS for MODIS fire pixels were 35% and 53%". Separately: "MODIS commission error in forests were reduced from ≈65% when FRP per fire pixel reached 2–4 MW to less than 20% … 18–20 MW". | **Both right.** These are two different 65% figures: one for omission, one for commission. One small wording fix in t04: "Summed VIIRS FRP was 0.72 of MODIS FRP" is really the **slope of a linear fit** of paired VIIRS FRP on MODIS FRP (0.72; 0.73 and 0.70 in subsets), not a ratio of sums. Also, the 2.5 MW (nadir) and 17 MW (edge) limits that t04 attributes to Fu are figures Fu quotes from earlier work ("was reported to have"), not Fu's own measurement. |
| Zheng et al. 2026, *Remote Sens.* 18:1650 | t04, t08, t13, evidence file | t04 says the matching window was "one day" and also "within 5 minutes". t08 describes a priority-switch fusion. t13 says it is not transferable to Terra. | `dl/t04/zheng.txt`: footprint pairs are "near-synchronous" (within 5 minutes). The **probability-of-detection** test against 30 m Landsat fires (LFTA, North America, 2022–2024) used "a temporal window of 1 day". POD for fires under 30 MW: MODIS 26.76%, VIIRS 44.25%. Duplicates: under 8 s apart and over 30% footprint overlap. Minimum FRP 4.1 to more than 33.6 MW (MODIS), 1.4–2.2 MW (VIIRS). Slope 0.74 rises to 1.03. Fusion uses MODIS "when VIIRS data are unavailable". Terra transfer needs "independent MOD14-specific paired dataset and recalibration". | **All consistent.** The two windows belong to two different tests. Caveat that no file states: the POD reference years 2022–2024 fall in Aqua's drift period. |
| Remy and Kaiser 2014, *ACP* 14:13377 | t05, t08 | t05 says boreal coefficients are near 1 and infers a small morning-afternoon gap. t08 stresses that boreal fires are "much more irregular". | `dl/remy2014.txt`: r² "between 0.85 and 1" for Aqua and "generally … between 0.5 and 0.8" for Terra; at least 400 positive 0.5° cells; fitted 2003–2011. Forest regions show coefficients "close to 1 for both Aqua and Terra". Boreal fire events are "much more irregular in size and intensity". The stated aim is that emissions stay "independent of the number of satellites". | **Consistent.** t05's "small morning-afternoon gap" is the reviewer's inference, for FRP on a daily 0.5° grid. It is not a count result. |
| Andela et al. 2015, *ACP* 15:8831 | t05, t08 | t05 gives numbers. t08 says "good agreement only after aggregating". | `dl/andela2015.txt`, Table 3: daily r at 0.1° is 0.50 (persistence) against 0.27 (climatological), and hourly about 0.22. Table 2: climatological temperate-forest fire radiative energy (FRE) is 118% of SEVIRI. Both approaches improve sharply at 1° (daily 0.76 and 0.75). | **Both right.** One fact neither file states bears on section 2.1: Andela's per-day Gaussian for temperate forest is very narrow (σ 1.14 h, peak 13.31 h; Table 1). Gui's climatological curve is much wider (σ 2.81 h). |
| Giglio et al. 2025, *RSE* 331:115006 (VNP64A1) | t03, t08 | t03 gives numbers. t08 gives only the recommendation. | `dl/t03/vnp64val.txt`, Table 2: Boreal North America (BONA) Δ = 10.0%, median slope 1.07, r 0.974. "Simple concatenation of the MCD64A1 and VN[P64]A1 BA time series at local scales is not advisable for long-term [trend analyses]". | **Consistent.** |
| GFED5NRT, Chen et al. 2026, *ESSD* 18:7535 | t13; evidence file and r02 | t13 puts it in the "fitted calibration, then **priority fusion**" row. | Fetched fresh from essd.copernicus.org. Scalars relate VIIRS detections to GFED5 burned area "during the MODIS-VIIRS overlap period (2012–2022)". Scalars "are held fixed during the NRT extension". The combined product is "the arithmetic mean of the SNPP- and NOAA-20-based estimates", and "defaults to the remaining instrument" when one is missing. Evaluation is against GFED5 over the same 2012–2022. | **t13 mislabels the combination rule.** GFED5NRT averages the satellites with a fallback. It does not use a priority switch. Its other claims ("held fixed", in-sample evaluation) are confirmed. The evidence file has this right. |
| GFED3, Giglio et al. 2010, *Biogeosciences* 7:1171 | t03 | t03 gives "γ = 1.35 for Boreal North America" without naming the sensor. | `dl/t03/giglio2010.txt`, Table 1: 1.35 (r 0.94) is the **ATSR** factor. VIRS has none for BONA. The zero-cell caveat is confirmed. | Correct, but should say "ATSR". |
| Gibson et al. 2024 | t01 | t01 applies Gibson's 77% Moran's I critique to three method rows (sigmoid degradation, overlap regression and U-Net). | `dl/waikato.txt` (thesis reproduction): the 77% rise is measured for **DVNL, "described by Nechaev et al. (2021)"**, which is the U-Net product. | The number and quote are correct. Extending the critique to Li 2020's sigmoid product is t01's inference and should be labelled as such. |
| Wooster et al. 2021, *RSE* 267:112694 | t04, t05, t08 | t05 says "text blocked; not read". t04 and t08 read it. | `dl/t08v/wooster.txt` (NOAA repository manuscript, noaa/67728): "one aim being to derive transfer functions enabling data from multiple sensors to be combined into single time-series". | **Not a conflict of content.** The manuscript is open at https://repository.library.noaa.gov/view/noaa/67728, so t05's "not read" is just an access gap. |
| Sofiev and Kouznetsov 2026, *GMD* 19:10123 | t04 | t04 itself reports a mismatch between the abstract, the conclusions and the tables. | `dl/t04/sofiev.txt`: abstract "3.7 MW … nadir … clear-sky night", "daytime sideview … 40 MW". Conclusions "5.7 and 3.7 MW" (MODIS C6.1 day and night) and "3.7 and 0.7 MW" (VIIRS). Table: λ 4.44 and 4.43 MW km⁻², μ 0.52 and 1.01 MW. 128 and 177 TW become 88 and 106 TW, with a diurnal factor of 1.2. | **t04's description is accurate**, including its flag that the paper is internally inconsistent. |
| Hawbaker 2008 (t04) and Giglio, Csiszar and Justice 2006 JGR (t05) | t04, t05 | t04 says Hawbaker shows "Terra is less sensitive than Aqua", consistent with the team's Terra/Aqua day ratio of 0.72. t05 quotes Giglio 2006: in boreal North America, early-afternoon and midmorning fire activity are "about evenly matched". | Hawbaker dissertation (`dl/t04/hawbaker_diss.txt`): 50% detection at 105 ha (both), 195 ha (Aqua) and 334 ha (Terra), confirmed. Giglio 2006 (`dl/t05/giglio2006jgr.txt`): the "evenly matched" category covers boreal Siberia and North America, judged from overpass-corrected day-plus-night counts. The paper warns that at boreal latitudes the simple ratio "can potentially mute the apparent magnitude of the diurnal fire cycle". | **Not a contradiction, but t04's wording is wrong in kind.** Terra and Aqua carry the same instrument. Terra's lower daytime yield reflects its earlier overpass on the diurnal cycle, not lower sensor "sensitivity". This matters because the 2026 Terra problem is the same timing effect, made larger by drift. |

### 1.2 Same method, different names

These are the same method under different names, sometimes with different variants. Merging them is the main simplification the review needs.

1. **Overlap scale factor (ratio of sums).** It appears as: "ratio of sums / ratio estimator" (t09); "regional multiplicative factor on overlap" (t03, GFED3); "per-cell ratio bias correction" (t02, Ocean Colour CCI); "chain-linking" and "mean splice" (t11); "single-satellite to constellation regression" (t05, t08, Remy and Kaiser); "overlap regression" (t01); "regression emulation toward a reference sensor" (t04, Wooster 2015); "fitted calibration" (t13); "rescale, then compute anomalies" (t12, ratio variant). t09 notes, and it is a standard result, that an intercept-only Poisson GLM with offset log(VIIRS) gives exactly the ratio of sums. t11's "count model with shared monthly activity" and t13's "small learned regression" are the same model with day/night terms added. **One method, about a dozen names.** The team already measured it (0.242; 0.34 day and 0.18 night).
2. **Geometric mean regression** (t02, "translation equations") is the same as **reduced or standardised major axis (RMA/SMA)** in t09.
3. **CDF matching** (t02, t12), **quantile mapping** (t03, t10) and **percentile matching** (t02) are one method. RHtests "quantile-matching adjustment" (t10) is a different, within-series breakpoint adjustment and should not be confused with them.
4. **Each sensor against its own history** appears as: "single reference satellite" (t03, INPE); "anomaly comparison / phase averaging" (t03, Ramoino); "z-score / percentile rank against own history" (t12); and "correct the old sensor only, use VIIRS separately" (t01). All assume the anomaly does not depend on the sensor. The team measured this as rank correlation 0.97, with 71% class agreement.
5. **Active cell-days** (t06), "union of cell-days / voting with k = 1" (t07) and "degradation to the old sensor's footprint" (t01's mapping) are one unit.
6. **Daily mean of the VIIRS satellites that have data** (evidence file) is the same as "equal-weight merging" (t02, Ocean Colour CCI), "inverse-variance weighting with near-equal weights" (t07) and "average-with-fallback" (GFED5NRT and GBBEPx in t08 and r02).
7. **Drift diagnosis against a stable reference** appears as: "drift diagnosis against a stable-geometry sensor" (t02, Nagol); "stability check as trend of the difference" (t02); "flag drifted years" (t03, Giglio and Roy); "pairwise sensor attribution" (t10, Menne and Williams logic); and "fixed-date step tests" (t10). All of these compute Terra-versus-VIIRS ratios over time. The evidence file's drift table already does this.
8. **Time-varying correction of the drift** appears as: "state-space model with time-varying factor" (t11); "structural time series with an intervention" (t11); "trend term after 2022" (t10); and "instrument/protocol term in a trend model" (t09, BBS). These are the same idea at different levels of flexibility.
9. **Diurnal adjustment by a fitted Gaussian** appears as: "bimodal Gaussian by land cover" (t05, Gui); "Gaussian adjustment factor" (t08, Zhang 2020); and "climatological Gaussian" (t05, Andela). "Observation-based diurnal correction" (t02, MSU) and "reference-sensor diurnal intercalibration" (t01, Ghosh) are the non-fire versions.
10. **Degrade the new sensor to the old** appears as: "observation operator / MODIS-equivalent from VIIRS" (t04); "spatial degradation plus saturation emulation" (t01); and "convolutional network, new to old" (t01). These are the same direction choice at three levels of machinery.
11. **Frequency–magnitude extrapolation below the detection limit** (t04, Sperling) is the fire version of the seismology "equivalent count above a common magnitude" (gap B below).
12. **Blocked validation** appears as: "year-out validation" (t01, Nechaev); "blocked cross-validation" (t10, Roberts); and "leave-one-season-out" (t13).
13. **Hurdle model P(MODIS > 0 | VIIRS)** (t09) is the formal version of the evidence file's "presence or absence only" fallback. The spatial Poisson hurdle in gap A is its spatial extension.
14. **Footprint matching** (t04) and "correction before fusion" (t08) describe the same Zheng/Fu pairing step.
15. **Triple collocation** appears in t02, t07, t11 and t12. All four files reject it for the same reason: the VIIRS satellites share errors and there are only two sensor families.

---

## Different judgements of fit

### 2.1 Diurnal correction of the Terra (and Aqua) drift: hours (t05) or days and context only (t01, t02, t08)

- **t05:** weight Terra daytime counts by a published Gaussian (Gui 2026, North American forest first mode, μ 14.57 h, σ 2.81 h). It takes hours with data in hand. t05's own check gives 0.37 predicted against 0.46 measured for 2026, and 0.74 against 0.77 for 2024.
- **t01, t02, t08:** a defensible correction needs a diurnal cycle fitted for Interior BC from geostationary data, which the team lacks. It takes days or more and is context only.

**Re-check.** The parameters are confirmed in `dl/mdpi_2026_18_52.pdf` / `dl/t05/mdpi.txt` (Table 1). σ is a standard deviation, and the curve is fitted to **min–max normalised hourly FRP**, not counts, for GOES-16 in 2018–2020. I recomputed the prediction for every drift year against the evidence file's measured Terra daytime fraction of expected:

| Year | Median Terra day time | Predicted by Gui curve | Measured (evidence file) | Measured ÷ predicted |
|---|---|---|---|---|
| 2022 | 11:04 | 0.96 | 0.95 | 0.99 |
| 2023 | 10:44 | 0.82 | 0.81 | 0.99 |
| 2024 | 10:32 | 0.74 | 0.77 | 1.04 |
| 2025 | 10:04 | 0.58 | 0.70 | 1.21 |
| 2026 | 09:20 | 0.37 | 0.46 | 1.25 |

(Baseline time 11:10. The calculation is mine and uses only the first Gaussian mode, as t05 did.)

**Which is better supported.** Each side is half right.
- t05 is right that a published curve gets the **direction and size of the 2022–2024 decline** almost exactly, with data in hand, in hours.
- The sceptical files are right that the correction is not reliable where it matters most. The curve **over-corrects 2025 and 2026 by 21–25%**, about the size of the single-month scatter. There are several reasons:
  - The normalised curve sets its minimum to zero, so it removes the night-time FRP floor and exaggerates the morning fall-off.
  - It describes FRP, not detections.
  - It is fitted at continental scale.
  - The result depends heavily on which published curve is used. Andela 2015's per-day temperate-forest Gaussian (σ 1.14 h, peak 13.31 h) predicts that a 09:20 pass sees about 1% of what an 11:10 pass sees, against a measured 46%.

The team's own evidence supports a third option that both camps mention but neither recommends outright: the drift factor is **measured directly** against NOAA-20, which kept its overpass time (0.95 down to 0.46). This is the "empirical" version (t10's trend term, t11's time-varying factor, t03's flag), and it needs no diurnal model. Its weakness is that it is fitted on the very years it corrects, so it cannot be validated independently until BC's 2026 fire records appear in April 2027.

### 2.2 Line fitting: geometric mean regression is "defensible" (t02) or "not applicable" (t09)

- **t02:** geometric mean regression is appropriate because both monthly counts are noisy. It cites the AVHRR/MODIS translation equations.
- **t09:** RMA/SMA and Deming regression answer a symmetric "true relationship" question. The team's task is **prediction** (MODIS-equivalent from VIIRS, or the reverse), and for prediction the Warton et al. 2006 review favours OLS, or here a ratio. Deming regression also needs an unknown error-variance ratio.

**Better supported: t09.** Warton et al. 2006 (`dl/t09/warton.txt`) is explicit that OLS bias "does not matter when the aim is to predict Y from X". The evidence file adds that fitted slopes are close to 1 and that a curve did not beat one factor out of sample, so the choice of line hardly matters. t02's point is useful only as a caution: a fitted OLS slope of MODIS on VIIRS is flattened by noise in VIIRS. That argues for a ratio of sums, which both files already favour.

### 2.3 Kalman / state-space: "Gaussian fails; days" (t07) or "count model in hours" (t11)

- **t07:** a Kalman filter assumes linear-Gaussian noise. That fails for heavy-tailed, mostly zero small-area counts (91% of fire-season months are empty at 10 km). Days or more.
- **t11:** a negative-binomial model with a shared monthly activity term and fixed sensor factors takes a few hours. A time-varying (random-walk) factor takes a day or more. A Gaussian dynamic factor model "can be run in hours" but is hard to justify.

**Both are right about different models.** t11's quick model is a count GLM with one free parameter per month (item 1 in section 1.2), not a Kalman filter. t07's objection applies to t11's dynamic factor model and to a Gaussian random-walk factor, and t11 concedes both points. The evidence file supports t11 on the quick model: zero MODIS months are common, and a negative-binomial likelihood uses them where a log-ratio cannot.

### 2.4 Quantile mapping / CDF matching

| File | Judgement |
|---|---|
| t02 | Poorly defined for zero months. Large areas only. About a day. |
| t03 | The only feasible half of MRBA60. About a day. Upper quantiles rest on a handful of months. |
| t10 | Little to gain over one ratio. Calibration length "exceeds ten years" (Reiter 2016, abstract only). Hours to build, a day to validate. |
| t12 | Spreads tied zeros. A day or more. |

**Better supported: t10.** The evidence file's direct test (a power law did not beat one factor out of sample, and slopes are about 1) is the count analogue of asking whether quantile mapping adds anything beyond a ratio. All four files agree that quantile mapping cannot restore missed detections. The one public hackathon attempt (t10 Sources; PR confirmed to exist and to describe quantile mapping fitted on 2012–2020 and tested on 2021–2024) shows the method can be built. Its results were not checked.

### 2.5 Per-sensor anomalies: "well supported within the VIIRS era" (t03) or "breaks below 100 km" (t12)

- **t03:** a single reference satellite needs no cross-sensor factor. NOAA-20 and NOAA-21 match Suomi NPP to within 1–3%.
- **t12:** the z-scores used by dashboards break down for skewed counts. The GFW code labels a zero-variance baseline "normal". This is confirmed in `dl/t12v/components_widgets_utils_data.js`: `stdPeriodTotal > 0 ? (current − mean)/std : …`.

**Consistent once scoped.** t03's endorsement covers comparisons within the VIIRS era only. Both files say a month after 2012 compared with the years before 2012 still needs a bridge. The evidence file (71% and 44% class agreement; MODIS median zero below about 100 km) supports t12's warning for small areas.

### 2.6 Day/night split: presented as clearly needed (t02, t04, t09) or qualified (evidence file)

- **t09** calls the fit "good … split by day and night" and cites diel effects in Miller et al. 2023. Confirmed in `dl/t09v/miller2023.txt`: "diel effects were important for all but one species".
- **t04** says ratios "have to be split" because the detection limits differ about tenfold.
- **The evidence file** measured that splitting gave no gain in monthly accuracy for the whole box. Its value is in avoiding bias when the day/night mix shifts (small areas, quiet months, near-real-time rows), and the night factor is unstable.

**Better supported: the evidence file's qualified version.** The literature explains *why* day and night differ. It does not show that splitting improves a monthly count for the box.

### 2.7 Event and cluster units: applicable with care (t06) or not applicable (t08)

- **t08** rejects object tracking (FEDS) and GOFER because they output perimeters.
- **t06** proposes simplified spatio-temporal events, built per satellite and then combined, in hours.

**Better supported: t06**, because it addresses the counting use and t08 does not consider it. t06's own warning is backed by the evidence file: pooled units step up by 1.24 and 1.37 times when satellites are added. Events must therefore be built per satellite.

### 2.8 Priority switch: "not applicable" (t08) or listed as a usable baseline (t13)

**Better supported: t08.** After 2012 VIIRS is always present, so a priority switch reduces to "use VIIRS" and does not bridge the record. t13's row is useful only as the fitted-calibration step, which is item 1 in section 1.2.

---

## Citation spot-checks

27 sources were checked. The emphasis was on sources that carry weight and on those that the files read only as abstracts. **No source was fabricated and no DOI failed.** Every DOI below resolved on Crossref to the stated title and authors.

| # | Source (file) | How checked | Claim | Result |
|---|---|---|---|---|
| 1 | Fu et al. 2020 (t04, evidence) | `dl/t04/fu2020.txt` | 65%/83% omission; 35%; commission about 65% at 2–4 MW; slope 0.72 | Pass. Wording on slope noted in 1.1. |
| 2 | Zheng et al. 2026 (t04, t08, t13) | `dl/t04/zheng.txt` | POD 26.8/44.3%; minimum FRP; 8 s and 30%; 0.74 to 1.03; Terra caveat | Pass |
| 3 | Gui et al. 2026, *Remote Sens.* 18:52 (t05) | `dl/t05/mdpi.txt`; Crossref | 14.57 h, 2.81 h, 19.59 h, 0.55 h; "fails to accurately" | Pass. Crossref dates the issue 24 Dec 2025, volume 18 (2026). |
| 4 | Remy and Kaiser 2014 (t05, t08) | `dl/remy2014.txt` | r² ranges; 400 cells; boreal irregular; coefficients near 1 | Pass |
| 5 | Andela et al. 2015 (t05, t08) | `dl/andela2015.txt` | r 0.50 against 0.27; about 0.2 hourly; +18% temperate forest | Pass |
| 6 | Giglio et al. 2010, GFED3 (t03) | `dl/t03/giglio2010.txt` | γ 1.35, r 0.94; zero-cell caveat | Pass (the factor is ATSR's) |
| 7 | Giglio et al. 2025, VNP64A1 (t03, t08) | `dl/t03/vnp64val.txt`; Crossref | +10.0%, slope 1.07; "not advisable" | Pass |
| 8 | Hawbaker et al. 2008 (t04) | dissertation text | 105, 195 and 334 ha | Pass. Interpretation noted in 1.1. |
| 9 | Kaur et al. 2019 (t10) | `dl/t10/qmfrp.txt` | 422 against 382 MW; −30% residual at 0.1°; about 6% at 1° | Pass. The text: "At 1° and 2° resolution, the FRP bias which cannot be corrected in the last viewing angle bin is around 6% and 9%". |
| 10 | Dastour et al. 2024 (t06) | `dl/t06/dastour.txt` | 96/94/88% of 173 fires ≥100 ha; 36–43% at 10–25 ha | 96% (166/173) and 42.86% confirmed. 94% (163/173) and 88% (152/173) match the table fractions. The 36% end was not traced. |
| 11 | Miller et al. 2023 (t09) | `dl/t09v/miller2023.txt` | diel effects for all but one of ten species; "induces correlation" | Pass |
| 12 | Giglio et al. 2006 *ACP* (t05) | `dl/giglio2006acp.txt` | "almost uniformly lower"; tendency to overcorrect | Pass. The "+20%" figure was not located in this pass. |
| 13 | Sofiev and Kouznetsov 2026 (t04) | `dl/t04/sofiev.txt`; Crossref | coefficients; TW totals; inconsistency flagged | Pass |
| 14 | Torres-Vázquez et al. 2026, MRBA60 (t03) | `dl/t03/mrba60.txt`; Crossref (published 25 Jul 2026) | RF per biome and season; 2019–2024; quantile mapping; "29% lower global BA" | Pass |
| 15 | Gibson et al. 2024 (t01) | `dl/waikato.txt` | Moran's I +77%; "largely undoing gains" | Pass. Scope noted in 1.1. |
| 16 | Wooster et al. 2021 (t08) | `dl/t08v/wooster.txt` | "transfer functions …" quote | Pass |
| 17 | NOAA HMS page (t08) | fetched ospo.noaa.gov | "can introduce large variation in system performance"; "coarse indicator only" | Pass |
| 18 | Brennan et al. 2019 (t07) | fetched bg.copernicus.org | triple collocation on three burned-area products; "lower bound"; zero periods dropped | Pass |
| 19 | Weber and Wunderle 2019 (t05; abstract only) | Crossref abstract (MDPI page returned 403) | about 5 h drift; about 90% decline; correction essential | Pass |
| 20 | GitHub PR nasa-flame-sense #2 (t10) | fetched github.com | exists; QM plus LightGBM; fit 2012–2020, test 2021–2024; placebo years | Pass. Merged 20 Oct 2026 into a feature branch, not the default branch. |
| 21 | Haghshenas and Shamsoddini 2026 (t13; abstract only) | Crossref plus techscience.com abstract | RMSE 1.87 K (XGBoost) against 2.62 K (ESTARFM) for MODIS; asymmetric transfer | Pass. The paper is about **Sentinel-3 as an alternative to MODIS**, which t13 does not say. |
| 22 | Csiszar et al. 2006 (t04; abstract only) | abstract via manuscript.isc.ac record | about 60 (Siberia) against about 45 (Brazil); smoke | Pass. The unit is a **contiguous ASTER fire cluster** size, not any fire pixels. |
| 23 | Chen et al. 2026, GFED5NRT (t13) | fetched essd.copernicus.org | scalars held fixed; in-sample evaluation | Pass. Combination rule mislabelled; see 1.1. |
| 24 | Sathyendranath et al. 2019, OC-CCI (t02) | `dl/t02/sath.txt` | equal weight per sensor; 2003–2007 reference; running averages later | Pass ("each sensor available was given equal weight") |
| 25 | Gruber et al. 2019 (t02, t10, t12) | `dl/gruber2019.txt` | "most stable climatology"; "can change its magnitude"; spurious error correlations | Pass |
| 26 | GFW widget code (t12) | `dl/t12v/components_widgets_utils_data.js` | zero SD handled as 0 | Pass |
| 27 | Ramoino et al. 2013 (t03) and INPE FAQ (t03) | `dl/t03/arino_dtu.txt`; fetched INPE FAQ | geometric ratio about 9 at the equator; "Esta transição causou a descontinuidade…" | Pass. The INPE FAQ also says VIIRS detects "about ten times more" fire pixels than MODIS and that INPE will "adjust carefully". No file reports this figure. It is a coarse national claim against the team's measured 4.1. |

DOIs resolved on Crossref with matching titles and authors: Haghshenas 2026, MRBA60, Csiszar 2006, Cheng 2026, Chen 2026, Gui 2026, Sofiev 2026, Deng 2026, Giglio 2025, and Zhang, van den Brakel and Tam 2019.

**Failures found:** none of fabrication. Errors of description:
- t13 calls GFED5NRT a priority fusion.
- t04 frames Terra versus Aqua as a difference in sensitivity.
- t03 does not name the sensor behind γ = 1.35.
- t04 calls Fu's 0.72 regression slope a ratio of sums.
- t01 extends Gibson's critique beyond the product it measured, without saying so.

---

## Gaps filled

### Gap A: Small-area estimation and empirical-Bayes shrinkage (no file covers it)

Why it matters most: the evidence file names small areas as "the hardest problem". MODIS records nothing in 33–50% of VIIRS fire months below about 50 km. Its proposed fallbacks (the enclosing area, a season, presence or absence) are hard switches. Survey statistics and disease mapping have a standard method for exactly this case: estimates for areas with few counts, made reliable by pulling them toward a larger-area estimate in proportion to how little data they have.

**What it is.**
- **Global empirical Bayes (Poisson–gamma) rate smoothing**, from disease mapping (Clayton and Kaldor 1987; Marshall 1991). The GeoDa documentation (fetched, https://geodacenter.github.io/workbook/3b_rates/lab3b.html) gives the working formulas:
  - smoothed value = w·(own rate) + (1 − w)·(reference rate)
  - w = σ² / (σ² + μ/P)
  - P is the "population at risk", and σ² and μ are estimated from all areas.

  The page explains the problem it fixes: "the precision of the rate as an estimate for underlying risk is inversely proportional to the population at risk". It also gives the edge case: when the estimated σ² is negative it is set to 0, and every area takes the reference value.
- **Area-level (Fay–Herriot) models.** Fay and Herriot 1979, *JASA* 74:269–277, doi:10.1080/01621459.1979.10482505. Metadata confirmed through Crossref; text not read. A regression-plus-random-effect version of the same shrinkage.
- **Fire applications found.**
  - Boubeta, Lombardía, Marey-Pérez and Morales (arXiv:2012.00069; abstract read): area-level Poisson mixed models with temporal and SAR(1) spatial random effects, with a real application to **forest fire counts in Galicia, 2007–2008**, and bootstrap MSE.
  - Kasin and Papastathopoulos (arXiv:2007.00137, 2020; abstract read): a **spatial Poisson hurdle** model for monthly wildfire counts, fitted by empirical Bayes with a Laplace approximation. It has a separate spatial effect for occurrence and for positive counts.
  - A 2026 *Environmental and Ecological Statistics* paper on municipal wildfire counts from satellite detections, using INLA (doi:10.1007/s10651-026-00723-8). Seen only as a search summary; the page redirected to a login. Unconfirmed.
- **No source applies shrinkage to cross-sensor hotspot harmonization.**

**How it would map onto the team's problem** (inference, untested):
- "P" becomes the expected count for the small area, for example its VIIRS count or its baseline mean.
- "Rate" becomes the area's own MODIS/VIIRS ratio or its anomaly.
- "Reference" becomes the enclosing box's value.

A 10 km circle with a handful of hotspots then takes almost the box's ratio or anomaly, and a 100 km circle keeps nearly its own. This replaces the evidence file's hard 50 km and 100 km cut-offs with a continuous, published weight that has a standard justification.

What it does not do: it does not restore missed MODIS detections, because shrinkage trades variance for bias toward the region. Its σ² estimate needs many areas, which the team can get by tiling the box with circles, as m08 already did with 31 circles per radius.

Effort: hours for global empirical Bayes, which is a few lines of arithmetic. A day or more for the spatial or Fay–Herriot versions.

### Gap B: Catalogue completeness thresholds and detection-efficiency correction (seismology and lightning)

Why it matters: t04 found "no count-level validation of any emulator", and t09 found no count calibration in fire work. Seismology and lightning networks have exactly that: long **event-count** catalogues whose detection sensitivity changed as networks were upgraded. They are the closest count-level analogue in the review, and no file mentions them.

**What it is.**
- **Magnitude of completeness, M_c(t).** The magnitude above which essentially all events in a space-time volume are recorded. Estimation methods are maximum curvature, b-value stability and K-S distance (SeismoStats documentation, fetched, citing Wiemer and Wyss 2000, Woessner and Wiemer 2005, and Clauset et al. 2009).
- **Counts across network changes.** Cui and Atkinson 2016, *Seismological Research Letters* 87(4), doi:10.1785/0220150268. Full text read from a downloaded PDF, `dl/gap/alberta.txt`.
  - They mapped M_c for seven periods from 1985 to 2015 as stations were added.
  - They counted only events above each period's M_c.
  - They converted to a common basis "to normalize the count … as M_c is changing in time and space", using an assumed Gutenberg–Richter law: N(M≥3) = N(M≥M_c(t)) × 10^(M_c(t)−3), with b = 1.
- **Time-varying completeness inside the model.** Mizrahi, Nandan and Wiemer 2021, *JGR Solid Earth*, doi:10.1029/2021JB022379. Full text, `dl/gap/mizrahi.txt`. They generalise from a binary complete/incomplete threshold to "a magnitude-dependent detection probability − embracing incompleteness instead of avoiding it". Data below the threshold are used instead of discarded.
- **Lightning.** Kaplan and Lau 2021, *ESSD* 13:3219 (fetched). They divide WWLLN stroke counts by published relative detection-efficiency maps. Raw counts rose from 35.7 million (2005) to about 222 million (2014) as the network was built out. The correction "reduces this artificial trend", but "the years 2010–2012 … should be treated with caution". The network "tended to be saturated at high lightning densities", and it misses mainly weak strokes.

**How it would map onto the team's problem** (inference, untested):
- FRP plays the role of magnitude.
- The common-threshold form counts, from both sensors, only hotspots above an FRP at which both are near-complete. Sofiev's limits suggest about 5 MW at 1 km² by day for MODIS, and more at the swath edge.
- The resulting counts should then be comparable without a scale factor, apart from pixel-size splitting of one fire into several VIIRS pixels.
- The Cui–Atkinson form converts each sensor's above-threshold count to a common reference threshold with a fitted frequency–FRP slope. This is t04's frequency–magnitude method, now with a count-level precedent.

Limits that carry over:
- The evidence file finds FRP a poor bridge at night, so a night-time FRP threshold inherits that noise.
- FRP thresholds rise with scan angle (Zheng: 4.1 to more than 33.6 MW), so a single threshold is not "complete" across the MODIS swath.
- The method discards most VIIRS hotspots by design.
- The lightning case shows that correction lowers an artificial trend but does not fully remove it.

Effort: hours for a threshold test on the 2012–2021 overlap, checking whether the above-threshold MODIS/VIIRS ratio is closer to 1 and steadier than 0.242.

---

## Gaps remaining

1. **A diurnal cycle of fire detections for western Canada from GOES-West or GOES-East.** It would settle section 2.1. No file found a boreal or montane count-based cycle. Gui 2026 is FRP at continental scale, and Andela 2015 covers Europe and Africa. Giglio 2007 (*RSE* 108:407) and Freeborn et al. 2022 (night-time fire, CONUS) were identified but not opened.
2. **Any peer-reviewed measurement of the 2022–2026 drift effect on MODIS fire counts.** This review's search again found only the Giglio May 2025 LANCE slides ("under active investigation") and a 2022 MODIS science-team presentation on exploiting the drift. The team's own drift table appears to be the only count measurement.
3. **Independent third references.** Sentinel-3 SLSTR night-time fire (Xu et al. 2020, metadata only in t08) and Landsat active fire (used by Zheng 2026 for POD) could serve as a check on both sensors in Interior BC. Nobody assessed whether either is downloadable as points for the box.
4. **Hierarchical Bayesian spatial count models (INLA, BYM) for satellite fire counts.** Seen only in a search summary (gap A). These are the full form of gap A and of t11's count model.
5. **Temporal disaggregation and benchmarking (Denton, Chow–Lin).** A standard method for reconciling a monthly indicator with an annual benchmark, here BC area burned (r03). Not covered, and probably low value given r03's finding that bridging through the overlap beats calibrating to area burned.
6. **The modifiable areal unit problem and change of support.** The scale dependence the team measured in m08 has its own literature. No file connects to it.
7. **Point-process thinning** as a null model: randomly thin VIIRS points at the measured ratio to see how much monthly scatter thinning alone produces. Not covered. It would tell the team how much of the 15–30% scatter is irreducible counting noise.
8. **Unresolved items carried over from the files:**
   - FIRMS acquisition-time precision (t04 and t08 both assume hours and minutes only; unconfirmed).
   - Whether later Ocean Colour CCI versions switched reference sensor (t02).
   - The NSIDC projection of Aqua at 15:50 against the team's median Aqua hotspot time of 14:51. These measure different things (equator crossing against fire-detection time) and no file reconciled them.
   - The "+20%" cloud-correction figure attributed to Giglio et al. 2006 ACP (t05) was not located in this pass.

**Count of methods.** The thirteen tables hold 114 method rows. After merging the duplicates in section 1.2, about 84 distinct methods remain. This is approximate, because some rows are variants rather than duplicates.

### Sources added by this reconciliation

- Boubeta M., Lombardía M.J., Marey-Pérez F., Morales D. (2020). Area-level spatio-temporal Poisson mixed models for predicting domain counts and proportions. arXiv:2012.00069. https://arxiv.org/abs/2012.00069 (abstract)
- Clayton D., Kaldor J. (1987). Empirical Bayes estimates of age-standardized relative risks for use in disease mapping. *Biometrics* 43(3):671. https://doi.org/10.2307/2532003 (metadata only)
- Cui L., Atkinson G.M. (2016). Spatiotemporal variations in the completeness magnitude of the Composite Alberta Seismicity Catalog. *Seismological Research Letters* 87(4). https://doi.org/10.1785/0220150268 (full text)
- Fay R.E., Herriot R.A. (1979). Estimates of income for small places: an application of James-Stein procedures to census data. *JASA* 74(366a):269–277. https://doi.org/10.1080/01621459.1979.10482505 (metadata only)
- GeoDa Center. Rate maps and rate smoothing (empirical Bayes). https://geodacenter.github.io/workbook/3b_rates/lab3b.html
- Kaplan J.O., Lau K.H.-K. (2021). The WGLC global gridded lightning climatology and time series. *ESSD* 13:3219–3237. https://essd.copernicus.org/articles/13/3219/2021/
- Kasin J.A., Papastathopoulos I. (2020). A spatial Poisson hurdle model with application to wildfires. arXiv:2007.00137. https://arxiv.org/abs/2007.00137 (abstract)
- Mizrahi L., Nandan S., Wiemer S. (2021). Embracing data incompleteness for better earthquake forecasting. *JGR Solid Earth*. https://doi.org/10.1029/2021JB022379 (full text)
- SeismoStats documentation, Estimate magnitude of completeness. https://seismostats.readthedocs.io/v1.0.0rc2/user/estimate_mc.html
- INPE Programa Queimadas, Perguntas Frequentes (re-fetched for the "about ten times" statement). https://terrabrasilis.dpi.inpe.br/queimadas/portal/pages/secao_informacoes/faq/
- Unconfirmed (search summary only): a 2026 *Environmental and Ecological Statistics* article on Italian municipal wildfire counts with INLA, https://doi.org/10.1007/s10651-026-00723-8
