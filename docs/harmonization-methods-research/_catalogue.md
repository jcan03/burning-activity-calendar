# Catalogue of candidate harmonization methods for MODIS and VIIRS hotspots

Compiled 2026-11-14 from thirteen topic files (t01 to t13 in this folder), checked against `docs/harmonization-evidence.md`. It lists methods and how well each carries over to the burning-activity calendar. It does not choose a method.

**How to read it.** The summary table lists all 55 methods. Entries follow, grouped by family. Methods the team could build in hours or a day get a full entry. Methods that need data the team lacks, or days of work, get a short "context" entry. The combinations at the end show how the pieces fit together. They are options, not a ranking.

**Codes for the team's five choices.** TR = target record (MODIS-equivalent or VIIRS-equivalent). UN = unit. SC = scaling. VC = combining the VIIRS satellites. MD = MODIS data since 2022.

**Two facts frame everything below.**
1. No source in any topic file harmonizes MODIS and VIIRS hotspot *counts*. Every statement about how a method would work on counts is the reviewers' inference, not a published result. Several topics ran out of search budget, so "no fire use found" is not proof that none exists.
2. No method in any family restores fires that MODIS never detected. Below about 50 km radius, MODIS records nothing in a third or more of the months in which VIIRS saw fire (16–50% at 10–100 km). Every method leaves this unsolved.

## Summary table

"Point rows" means the method can be built from FIRMS point rows alone (date, time, position, brightness, FRP, scan and track, confidence, day/night), with no cloud mask, swath data or record of empty passes. "Fire precedent" means a published fire product or study has used it (for any fire quantity, usually FRP or burned area, not counts).

| ID | Method | Family | Choices | Point rows | Fire precedent | Effort |
|---|---|---|---|---|---|---|
| U1 | Active cell-days | Unit | UN, VC | yes | no | hours (measured) |
| U2 | Same-pass duplicate removal | Unit | UN | yes (approx.) | yes | hours |
| U3 | Footprint-area union (FINN) | Unit | UN | yes | yes | hours |
| U4 | Spatio-temporal fire events from hotspots | Unit | UN, VC | yes | yes | hours to a day |
| U5 | Burned-area events and perimeters (context) | Unit | UN | no | yes | days or more |
| S1 | Overlap-fitted multiplicative factor (ratio of sums) | Scale | TR, SC | yes | yes | hours (measured) |
| S2 | Covariate-dependent factor (day/night, region, season) | Scale | SC, MD | yes | yes | hours |
| S3 | Count GLM with offset (Poisson, quasi-Poisson, NB) | Scale | SC | yes | no | hours |
| S4 | Binomial or beta-binomial share model | Scale | SC | yes | no | a day |
| S5 | Hurdle model, P(MODIS > 0) | Scale | SC, UN | yes | no | a day |
| S6 | Fitted curve (power, quadratic, sigmoid) | Scale | SC | yes | yes | hours |
| S7 | Symmetric regression (GMR, RMA, Deming) | Scale | SC | yes | no | hours |
| S8 | Quantile or CDF mapping | Scale | SC, TR | yes (large areas) | yes | a day |
| S9 | Detection-limit observation operator (MODIS-equivalent from VIIRS) | Scale | TR, SC | yes (approx.) | yes | hours to a day |
| S10 | Near-simultaneous footprint matching / event-level calibration | Scale | SC | yes (approx.) | yes | a day |
| S11 | Power-law extrapolation below the detection limit | Scale | TR, SC | yes | yes | hours |
| S12 | Tree ensembles with covariates | Scale | SC | yes | yes | a day |
| S13 | Image translation and spatiotemporal fusion (context) | Scale | TR | no | yes | days or more |
| S14 | Radiance-level and reference-imagery calibration (context) | Scale | SC | no | yes | days or more |
| T1 | Published diurnal-curve weighting | Sampling | MD | yes | yes | hours |
| T2 | Diurnal shape from the team's own detection times | Sampling | MD | yes | no | hours to a day |
| T3 | Geostationary or model-based diurnal and drift correction (context) | Sampling | MD | no | yes | days or more |
| T4 | Flag or exclude drifted sensor-years | Sampling | MD | yes | yes | hours |
| T5 | Monthly aggregation keyed by local date | Sampling | UN | yes | yes | hours |
| T6 | Observation-opportunity and cloud normalisation (context) | Sampling | SC | no | yes | a day or more |
| T7 | Overpass reconstruction from granule metadata or swath outlines | Sampling | VC, SC | no | yes | a day or more |
| T8 | Distinct detecting passes as a coverage proxy | Sampling | VC | yes | no | hours |
| C1 | Per-satellite scaling, daily mean of available satellites | Combination | VC | yes | yes | hours (measured) |
| C2 | Single reference satellite with fallback | Combination | VC, TR | yes | yes | hours |
| C3 | Inverse-variance weighting | Combination | VC | yes | no | hours |
| C4 | Union or k-of-n voting | Combination | VC, UN | yes | no | hours |
| C5 | Priority switch (preferred sensor, else rescaled second) | Combination | VC, TR | yes | yes | hours |
| C6 | Single-satellite to constellation regression | Combination | SC, VC | yes | yes | hours |
| C7 | Capture-recapture on cell-days | Combination | UN, VC | yes | no | hours to a day |
| C8 | Truth-free error estimation: triple collocation, latent class, occupancy, Dempster-Shafer (context) | Combination | VC | no | yes | days or more |
| C9 | Operational gridded fusion: observed-area Kalman, GOFER, HMS (context) | Combination | VC | no | yes | days or more |
| J1 | Chain-linking over a long overlap through an intermediate sensor | Join | SC, VC | yes | no | hours |
| J2 | Keep a documented seam (separate records) | Join | TR | yes | yes | hours |
| J3 | Integrated count model with shared monthly activity | Join | SC, VC, TR | yes | no | hours to a day |
| J4 | State-space model with time-varying factor or level shift | Join | MD, SC | yes | no | a day or more |
| J5 | Dynamic factor model with missing data | Join | SC | yes | no | hours |
| J6 | Reference chosen by stability or calibration confidence | Join | TR | yes | yes | hours |
| J7 | Same algorithm on both sensors plus regional intercalibration (context) | Join | TR | no | yes | days or more |
| E1 | Per-sensor standardised anomaly (z-score) | Expression | UN, TR | yes | yes | hours |
| E2 | Mean-based display: mean with min-max band, percent from mean | Expression | UN | yes | yes | hours |
| E3 | Ratio to the calendar-month median | Expression | UN | yes | no | hours |
| E4 | Empirical percentile rank with tie handling | Expression | UN | yes | no | hours |
| E5 | Fitted standardised index (SPI family) | Expression | UN | yes | no | a day |
| E6 | Rescale to a reference, then compute anomalies | Expression | TR, SC | yes | no | hours to a day |
| E7 | Fixed reference period with frozen parameters | Expression | UN | yes | yes | hours |
| V1 | Year-blocked cross-validation | Validation | all | yes | no | hours |
| V2 | Stability as the trend of the difference; drift diagnosis | Validation | MD, TR | yes | no | hours |
| V3 | Fixed-date step tests with pairwise attribution | Validation | MD, VC | yes | no | hours |
| V4 | Prediction intervals and ensemble records | Validation | SC | yes | no | hours to a day |
| V5 | Fusion vocabulary (levels, competitive and complementary sensors) | Validation | all | yes | no | hours |

Validation (V) methods change nothing in the record. They test or describe whatever the team builds, so they combine with every other method.

---

## Family U: the unit (what is counted)

Raw hotspot counts are the default and match the challenge wording ("number of hotspots"). FRP as a unit is already measured by the team as worse than counts once night passes are included, so it is not repeated here.

### U1. Active cell-days
- **Does:** counts grid cells with at least one hotspot on each local date. It is the hotspot analogue of degrading the fine sensor to the coarse sensor's footprint (night-lights practice, t01) and of a common grid (HLS, t02).
- **Choices:** UN; VC (how cells are combined across satellites).
- **Data:** point rows only. Yes.
- **Precedent:** degradation to the old footprint is standard in night lights (Li et al. 2020, Sci. Data 7:168). No published cross-sensor test of cell-days for fire (t06). Fire precedent: no.
- **Evidence:** at 2 km the ratio rises from 0.24 to 0.65 (0.68 by day); daytime factor steady across years (0.62–0.85); grid size 1–5 km matters little; removes MODIS same-pass duplicates. Against: single-month median error about 20% against 24–29% for counts, intervals overlap; night ratio swings eightfold with activity; compresses large months (62,646 hotspots to 8,053 cell-days); every daytime series, cell-days included, is out of range in 2026 (0.626).
- **Cannot fix:** small-area zeros, Terra drift, the step when satellites are added if cells are pooled (union rises 1.24 and 1.37 times).
- **Effort:** hours, largely measured.
- **Justification:** "Counting cell-days at roughly MODIS pixel scale puts both sensors on a common spatial footprint, the approach used to join DMSP and VIIRS night lights; in our box it raises the MODIS/VIIRS ratio from 0.24 to 0.65 and holds steady by day."

### U2. Same-pass duplicate removal
- **Does:** removes detections from the same pass that overlap (Zheng et al. 2026: under 8 s apart and over 30% footprint overlap) before counting.
- **Choices:** UN.
- **Data:** position, scan and track are in rows. The 8 s rule needs second-level time stamps; FIRMS time precision is undocumented (t04, t08), so overlap alone would be used. Yes, approximately.
- **Precedent:** Zheng et al. 2026, Remote Sens. 18:1650 (FRP fusion). Fire: yes.
- **Evidence:** 21–23% of MODIS hotspots have a same-pass neighbour within half a pixel. U1 already removes these by another route.
- **Cannot fix:** level gap beyond duplicates, scatter, zeros, drift.
- **Effort:** hours.
- **Justification:** "MODIS scan overlap counts some fires twice; removing same-pass overlaps first follows the published MODIS-VIIRS fusion of Zheng et al. (2026)."

### U3. Footprint-area union (FINN v2.5)
- **Does:** gives each detection a nominal area (0.14 km² VIIRS, 1 km² MODIS), links detections whose 110% scan × track rectangles overlap, unions pairwise hulls per day, and sums the area.
- **Choices:** UN.
- **Data:** rows plus an optional tree-cover raster (or a fixed forest assumption). Yes.
- **Precedent:** Wiedinmyer et al. 2023, GMD 16:3873 ("the identity of the sensor is not relevant ... as long as the pixel size ... is correctly represented"). Fire: yes.
- **Evidence:** untested arithmetic (t06): summed MODIS nominal area ≈ 0.242 / 0.14 ≈ 1.7 times VIIRS before merging, so nominal areas over-correct MODIS. FINN itself still finds VIIRS raises global emissions by about 25%.
- **Cannot fix:** detection sensitivity, zeros, drift. Not a "number of hotspots".
- **Effort:** hours.
- **Justification:** "An area unit makes pixel size explicit, as the FINN emissions inventory does, but the arithmetic suggests it overshoots, so it would need its own overlap check."

### U4. Spatio-temporal fire events from hotspots
- **Does:** links hotspots within a distance and a time gap into fire events, then counts events per month. Published settings: DBSCAN eps 750–3000 m, MinPts 3–4 (Dastour et al. 2024); ST-DBSCAN eps 1450 m MODIS, 550 m VIIRS, 7 days, MinPts 2 (Deng et al. 2026); FEDS 5 km forest buffer, 5-day activity (Chen et al. 2022); Su and Yu 2026 preprint on FIRMS VIIRS CSVs; older MODIS rules (2.5 km/4 d, 1875 m/4 d, 11 km/1 d). A variant counts only events above a size floor.
- **Choices:** UN; VC (events must be built per satellite, then combined).
- **Data:** rows only. Yes.
- **Precedent:** fire, yes. Dastour et al. 2024 (Fire 7:355, northern Alberta and edge of BC) matched 96% of fires ≥ 100 ha with combined data, 94% VIIRS, 88% MODIS, but only 36–43% of 10–25 ha fires. Deng et al. 2026 found the event count jumped when NOAA-20 was added.
- **Evidence:** 2 to 16 detecting passes a day depending on the satellites flying implies steps if satellites are pooled. The Kamloops static source (about 31 Suomi NPP rows a year) would survive Su and Yu's 90-a-year mask as recurring events unless removed.
- **Cannot fix:** sensitivity and number-of-passes effects, zeros, untuned thresholds for BC.
- **Effort:** hours for code; a day or more to validate thresholds.
- **Justification:** "Events reduce pixel-size and duplicate effects and agree across sensors for large fires in nearby boreal Canada (Dastour et al. 2024), but they diverge for small fires."

### U5. Burned-area events and perimeters (context)
Global Fire Atlas (Andela et al. 2019), FIRED (Balch et al. 2020), GlobFire (Artés et al. 2019) and concave-hull perimeters (Bhuian et al. 2024). Choices: UN. They need MCD64A1 burned area (which ends with MODIS) or reference perimeters, not FIRMS rows. Fire precedent: yes. Use: FIRED's tuning of space-time windows against 13,741 MTBS perimeters is a model for how U4 thresholds could be justified. Effort: days or more.

---

## Family S: the scale (a conversion between sensors)

### S1. Overlap-fitted multiplicative factor (ratio of sums)
- **Does:** factor = MODIS total ÷ VIIRS total over an overlap window, applied as a multiplication to the other record. Fitted on a large region, not per small area.
- **Choices:** TR (the same factor works in either direction), SC.
- **Data:** monthly counts. Yes.
- **Precedent:** fire, yes. GFED3 regional slope γ (1.35 for Boreal North America ATSR, r = 0.94; Giglio et al. 2010, Biogeosciences 7:1171). SEVIRI-to-MODIS FRP regression with regional factors 1.46–2.06 (Wooster et al. 2015). GFED5NRT region-by-land-cover scalars (Chen et al. 2026). Outside fire: Ocean Colour CCI per-cell ratio over a gap-free window (Sathyendranath et al. 2019); survey ratio estimator (Knottnerus and Scholtus 2019).
- **Evidence:** ratio 0.242 (0.237–0.28) over 116 stable-orbit months; 0.234–0.244 in the three biggest years; season error about 10%; slopes near 1. Against: fire-season range 0.19–0.40 across years; single-month error 14% (large months) to 30% (all fire-season months); quiet months run 25–50% above busy ones.
- **Cannot fix:** single-month scatter, zeros (GFED3 states it "does not restore burned area to ... zero-fire-count grid cells"), drift, additive sources (remove Kamloops first).
- **Effort:** hours; already measured.
- **Justification:** "A multiplicative factor fitted over the 2012–2021 overlap on the whole region is how GFED3 merged ATSR and VIRS into the MODIS record; our data show the relation is proportional with slopes near 1."

### S2. Covariate-dependent factor
- **Does:** makes log(factor) depend on an observable covariate: day/night, region or land cover, season, size class.
- **Choices:** SC; MD (day/night separation isolates Terra by day).
- **Data:** rows carry a day/night flag for every sensor. Yes.
- **Precedent:** fire, yes: day and night factors in operational systems (r02); GFED3 and GFED5NRT by region. Fisheries diel effects on relative efficiency (Miller et al. 2023); per land-cover translation equations (Tsend-Ayush and Miura 2013: 1.25 needleleaf vs 1.10 broadleaf). Luo et al. 2024 (Nature 627:321) explains why night behaves differently: overnight burning is concentrated in large fires.
- **Evidence:** day 0.34, night 0.18. Splitting gave no measurable gain in monthly accuracy for the whole box; its value is avoiding bias when the day/night mix differs (small areas, quiet months, near-real-time rows). Night factor unstable (0.036–0.192 against NOAA-20 in 2018–2021). Calendar-month factors weak (June flips 0.30 to 0.52 with UTC vs local keying). A covariate seen only by MODIS cannot be used after 2027.
- **Cannot fix:** as S1.
- **Effort:** hours.
- **Justification:** "Detection limits differ about 2-fold by day and 10-fold at night between the sensors (t04), so a single factor is biased whenever the day/night mix changes; separate factors are standard practice in operational fire systems."

### S3. Count GLM with an offset
- **Does:** models MODIS monthly count with log(VIIRS count) as an offset plus day/night; the intercept is the log factor. Quasi-Poisson or negative binomial (NB) handles overdispersion. With Poisson errors and only an intercept it equals S1. Also the "small learned regression" of t13.
- **Choices:** SC.
- **Data:** yes.
- **Precedent:** count regression (Zeileis et al. 2008); quasi-Poisson vs NB (Ver Hoef and Boveng 2007). Fire: no.
- **Evidence:** adds dispersion-aware intervals. NB weights small counts more, which may move the factor toward quiet months (25–50% higher ratio). Treats VIIRS as exact, but two identical VIIRS satellites differ ±15–20% in a month.
- **Cannot fix:** zeros, drift, scatter.
- **Effort:** hours.
- **Justification:** "The GLM is the statistical form of the ratio; it gives the same factor with intervals that respect count noise and overdispersion."

### S4. Binomial or beta-binomial share model
- **Does:** models MODIS's share of the monthly MODIS+VIIRS total, p = ρ/(1+ρ), with a random effect per month or beta-binomial variance.
- **Choices:** SC.
- **Data:** yes.
- **Precedent:** fisheries paired-tow calibration (Cadigan and Dowden 2010; Miller 2013). Fire: no.
- **Evidence:** keeps zero-MODIS months in the fit and is bounded. Its justification rests on simultaneous pairs; the team's pairs are a month of passes at different hours (MODIS about 11:15 and 13:30, VIIRS 12:40 and 02:10).
- **Cannot fix:** zeros (it models them, does not restore them), drift.
- **Effort:** a day.
- **Justification:** "Paired-gear calibration in fisheries handles the same problem of two instruments counting the same population with different efficiency."

### S5. Hurdle model for small areas
- **Does:** models separately whether MODIS records anything given the VIIRS count, and how many if so. A zero-inflated mixture is the alternative; t09 judges its "structural zero" class physically meaningless here.
- **Choices:** SC; UN (presence/absence).
- **Data:** yes.
- **Precedent:** Zeileis et al. 2008; Warton 2005 ("many zeros does not mean zero inflation"). Fire: no.
- **Evidence:** quantifies P(MODIS > 0 | VIIRS) by radius class, where MODIS misses 50% (10 km), 36% (25 km), 33% (50 km), 16% (100 km) of VIIRS fire months.
- **Cannot fix:** restores no detections.
- **Effort:** a day.
- **Justification:** "It states openly how often a converted MODIS-era month would read zero at the user's area size, instead of hiding that in an average factor."

### S6. Fitted curve (power, quadratic, sigmoid)
- **Does:** fits a non-linear curve between sensors over the overlap.
- **Choices:** SC.
- **Data:** yes.
- **Precedent:** night lights (power best for DMSP intercalibration, Wu et al. 2013; zero-intercept quadratic, Ghosh et al. 2021; sigmoid, Li et al. 2020). Fire: Wooster et al. 2015 found a power law "no more skilful than a linear formulation" for SEVIRI–MODIS FRP.
- **Evidence:** against. Fitted slopes close to 1; a power law did not beat one factor out of sample.
- **Cannot fix:** as S1.
- **Effort:** hours.
- **Justification:** mainly useful to cite as a tested and rejected alternative.

### S7. Symmetric regression (geometric mean, RMA/SMA, Deming, York)
- **Does:** fits a line allowing error in both sensors. Deming needs the ratio of error variances.
- **Choices:** SC.
- **Data:** yes.
- **Precedent:** MODIS vegetation-index translation equations (Tsend-Ayush and Miura 2013); VIIRS-to-MODIS NDVI (Benedict et al. 2021); instrument intercomparison (Wu and Yu 2018). Fire: no.
- **Evidence:** the task is prediction, where OLS or a ratio is the appropriate tool (Warton et al. 2006); the error-variance ratio is unknowable for counts; slopes near 1 leave little to gain.
- **Cannot fix:** as S1.
- **Effort:** hours.
- **Justification:** cite only if a judge asks why noise in VIIRS was not modelled.

### S8. Quantile or CDF mapping
- **Does:** maps each value through the source distribution and the inverse target distribution over a calibration period. Variants: chained linear CDF matching onto the most stable sensor (ESA CCI soil moisture, Gruber et al. 2019); RHtests quantile-matching adjustment (Wang 2009); back-cast with Random Forest then quantile mapping (MRBA60, Torres-Vázquez et al. 2026); stochastic correction across a scale gap (Maraun 2013); detrended QM and quantile delta mapping (Cannon et al. 2015).
- **Choices:** SC, TR.
- **Data:** yes for large areas; poorly defined where many months are zero.
- **Precedent:** fire, yes: Kaur et al. 2019 mapped off-nadir to near-nadir gridded MODIS FRP (needs zero-FRP and observed-area cells; overcorrected boreal forest, 422 MW against 382 MW VIIRS); MRBA60 burned area. Franquesa et al. 2025 rejected QM for a vegetation record because it reduced variability and trend consistency.
- **Evidence:** against. About 70 fire-season overlap months, below the critical calibration length that "exceeds ten years in all experiments" (Reiter et al. 2016); QM is monotone, so every MODIS zero maps to one value; a curve did not beat one factor; percentile-level analogue (per-sensor ranks) gives 71% class agreement.
- **Cannot fix:** zeros, drift; may change trend magnitude (Gruber et al. 2019).
- **Effort:** hours to build, a day to validate.
- **Justification:** "Distribution matching is standard in climate records, but with ten overlap years, zero-heavy counts and a near-proportional relation it adds risk without measured gain."

### S9. Detection-limit observation operator (MODIS-equivalent from VIIRS)
- **Does:** treats the detection limit as linear in pixel area, D = λA + μ (day: 4.44A + 0.52 MW; night: 4.43A + 1.01 MW from Sofiev's tables), with a logistic soft threshold. VIIRS FRP is summed into roughly 1 km cells per pass and scored to give the expected MODIS count. A cheaper cross-check: the share of VIIRS hotspots above about 5 MW by day, compared with the measured ratio.
- **Choices:** TR (MODIS-equivalent; continues past 2027 with no drift model), SC.
- **Data:** FRP and day/night are in rows. MODIS pixel area must be assumed (no MODIS pixel exists where only VIIRS looked); no cloud state; overpass timing differs. Yes, approximately. The grid-cell version with a cloud term needs cloud flags: no.
- **Precedent:** Sofiev and Kouznetsov 2026, GMD 19:10123 (Aqua vs Suomi NPP 2020: totals 128 and 177 TW became 88 and 106 TW; a diurnal factor of 1.2 closed the remaining 20%). Validated on FRP totals only, never counts. Fire: yes.
- **Evidence:** gives a physical reason for 0.34 by day and 0.18 at night (gap about 2-fold by day, 10-fold at night). VIIRS stands in only for Aqua's time, not Terra's. FRP bridges worse than counts at night, and a threshold on FRP brings that noise into the count. Published MODIS limits differ by definition (2.5–8 MW at nadir; 10–50 MW off nadir).
- **Cannot fix:** adds nothing to the MODIS history; the Kamloops source must be removed first.
- **Effort:** hours for a rough version; a day with a hindcast against actual Aqua counts 2012–2021 (a suggested test, not published).
- **Justification:** "A MODIS-equivalent count can be emulated from VIIRS using published detection limits (Sofiev and Kouznetsov 2026), which explains the measured ratio physically, though the operator has been validated only on FRP totals."

### S10. Near-simultaneous footprint matching and event-level calibration
- **Does:** pairs Aqua and Suomi NPP detections within about 5 minutes, sums VIIRS pixels inside each MODIS footprint, and fits a ratio (optionally against view angle). Li et al. 2019 and Zheng et al. 2026 then priority-fuse (see C5).
- **Choices:** SC.
- **Data:** footprints are approximate (pixel centres only); time precision undocumented. Yes, approximately.
- **Precedent:** Fu et al. 2020 (summed VIIRS FRP 0.72 of MODIS; 35% of MODIS forest pixels had no VIIRS match, including MODIS false detections); Zheng et al. 2026. Fire: yes.
- **Evidence:** Zheng's reference is cloud-corrected VIIRS FRP (team has no cloud mask); Zheng says coefficients should not be transferred to Terra; scan-angle terms did not reduce the team's monthly scatter.
- **Cannot fix:** Terra, drift, zeros.
- **Effort:** a day or more.
- **Justification:** useful to calibrate a local detection limit for S9, not as a monthly conversion.

### S11. Power-law extrapolation below the detection limit
- **Does:** fits a power law to the FRP frequency distribution above MODIS's limit and extends it below to estimate missed FRP or fires (VIIRS-equivalent direction).
- **Choices:** TR, SC.
- **Data:** yes.
- **Precedent:** Sperling et al. 2020 (about 35% of FRP missed by Aqua in cerrado); Kumar et al. 2011. Fire: yes.
- **Evidence:** corrects FRP totals, not counts; fitted only in tropical and savanna systems; log-log least squares is biased (Clauset et al. 2009); cannot fill months with zero MODIS detections.
- **Effort:** hours.
- **Justification:** at most a cross-check on the size of the MODIS shortfall.

### S12. Tree ensembles with covariates
- **Does:** random forest or boosting predicts one sensor's count from the other's plus covariates (month, day/night share, area size, scan).
- **Choices:** SC.
- **Data:** yes.
- **Precedent:** MRBA60 Random Forest back-cast (fire, burned area); LST downscaling (Haghshenas and Shamsoddini 2026). Fire: yes.
- **Evidence:** about 10 independent seasons cannot support several covariates; record months lie outside the training range (Meyer and Pebesma 2021); scan-angle and per-month terms already failed in the team's tests. Use of AI tools must be declared under the challenge rules.
- **Effort:** a day with proper validation.
- **Justification:** hard to defend against a plain ratio on the same hold-out.

### S13. Image translation and spatiotemporal fusion (context)
Residual U-Net, VIIRS to DMSP (Nechaev et al. 2021); autoencoder or super-resolution, DMSP to VIIRS (Chen Z. et al. 2021; Cheng et al. 2026); unpaired CUT network (Tong et al. 2026, preprint); transformer translation of reflectance (Hamdi et al. 2026, poster); STARFM and ESTARFM (Gao et al. 2006; coal fires, Ghosh et al. 2020); unmixing and hybrid fusion (Wu et al. 2021 review); deep-learning fusion (Bouaziz et al. survey); GOES-17 to VIIRS fire super-resolution (Badhan et al. 2024, fire); saturation emulation (Li et al. 2020). Choices: TR. All need dense paired images or continuous fields; hotspot rows have no non-detections. Point rows: no. Effort: days or more. Transferable parts: Nechaev's year-out validation (see V1) and the direction argument "there is no deterministic way to add detail", which applies to restoring small fires MODIS missed. Gibson et al. 2024 warn that degrading to the old sensor re-imports its artefacts (DMSP false zeros), the analogue of a MODIS-equivalent record inheriting missed small fires.

### S14. Radiance-level and reference-imagery calibration (context)
Invariant-region intercalibration (Wu et al. 2013; CCNL, Zhao C. et al. 2022); automatic pseudo-invariant features (Zhang, Pandey and Seto 2016); bandpass adjustment and BRDF view-angle normalisation (HLS, Claverie et al. 2018); metrological harmonisation (Mittaz et al. 2019); pixel-degradation simulation (Sperling et al. 2020; Schroeder et al. 2014, fire); probability of detection against ASTER or Landsat (Morisette et al. 2005; Hawbaker et al. 2008, fire: 50% detection at 105 ha for Terra+Aqua, 195 ha Aqua, 334 ha Terra). Choices: SC. Need radiances, stable targets or coincident fine imagery. Point rows: no. Effort: days or more. Use: Hawbaker's Terra-less-sensitive-than-Aqua result is consistent with the team's Terra/Aqua day ratio of 0.72; wildfire has no invariant sites, and the only persistent source (Kamloops) is seen by VIIRS only.

---

## Family T: the sampling (time of day, number of looks, cloud)

### T1. Published diurnal-curve weighting
- **Does:** computes local solar time for each daytime hotspot and weights Terra and Aqua counts by the ratio of a diurnal curve at a reference time to the curve at the observed time. Gui et al. 2026 (Remote Sens. 18:52) fitted North American forest from GOES-16 FRP: peaks at 14.57 h (width 2.81 h) and 19.59 h (0.55 h).
- **Choices:** MD.
- **Data:** time and longitude are in rows. Yes.
- **Precedent:** fire, yes (FRP, continental, 2018–2020; no accuracy stated for the fit).
- **Evidence:** t05's arithmetic gives weights 0.48 at Terra's 11:10, 0.18 at 09:20, 0.81 at VIIRS's 12:45. That predicts Terra day at 0.37 of its stable level in 2026 (measured 0.46) and 0.74 in 2024 (measured 0.77). It would multiply Terra 2026 day counts by about 2.7, amplifying noise.
- **Cannot fix:** night ratio, scatter, zeros. Curve is for FRP, not counts, and not for Interior BC.
- **Effort:** hours.
- **Justification:** "A published forest diurnal curve roughly reproduces the measured fall in Terra's daytime count as its overpass moved from about 11:15 to 09:20, which supports attributing the fall to sampling, not to fire."

### T2. Diurnal shape from the team's own detection times
- **Does:** histograms VIIRS and MODIS detection times in the box (2012–2021) as the curve shape.
- **Choices:** MD.
- **Data:** yes.
- **Precedent:** none found. Fire: no.
- **Evidence:** closer in place and unit, but samples only about four local times a day and cannot see the hours between.
- **Effort:** hours to a day.
- **Justification:** weak on its own; possible as a check on T1.

### T3. Geostationary or model-based diurnal and drift correction (context)
Geostationary diurnal adjustment factors (Zhang et al. 2020, Himawari-8 + VIIRS; Andela et al. 2015, where hourly correlation was about 0.2 at 0.1° and persistence beat the curve); SST adjustment to a fixed local time (Merchant et al. 2019); observation-based diurnal correction across co-orbiting satellites (Po-Chedley et al. 2015); orbit-drift correction families validated by simulated drift (Julien and Sobrino 2022); reference-sensor intercalibration of drifted satellites using targets with no diurnal cycle (Ghosh et al. 2021). Choices: MD. Need hourly geostationary fire data (GOES-West covers BC, but the team does not hold it) or diurnally constant targets, which fire is not. Point rows: no. Fire precedent: yes. Effort: days or more. Use: Weber and Wunderle 2019 found AVHRR drift of up to about 5 hours caused "a ∼90% decline in the number of observed fires" (abstract), a precedent for the size of the Terra effect.

### T4. Flag or exclude drifted sensor-years
- **Does:** tests whether a record moves with sensor geometry and excludes or flags years that do, instead of correcting them. Giglio and Roy 2024 used a rank correlation of at least 0.5 with solar zenith angle; their finding was that geometric fixes "often merely shifted the problems". Includes the rule of not fitting factors on drift years and of diagnosing drift against a stable-geometry sensor (Nagol et al. 2014).
- **Choices:** MD.
- **Data:** overpass times are in rows. Yes.
- **Precedent:** fire, yes: Giglio and Roy 2024 (Nat. Commun. 15:2079); GFED5 stops fitting in 2022; QFED says "Terra is increasingly underestimating fire activity".
- **Evidence:** Terra day at 0.95, 0.81, 0.77, 0.70, 0.46 of expected in 2022–2026; Terra day vs NOAA-20 0.070 in 2026 against 0.127–0.212 before; day+night total held through 2025 (partly Terra night rising); Aqua shows no clear count effect through 2025. VIIRS is flying through all drift years, so drift-period MODIS is not needed for the record itself.
- **Cannot fix:** gives a rule, not a correction; MODIS-only months are not affected (drift starts after VIIRS).
- **Effort:** hours.
- **Justification:** "Following Giglio and Roy (2024), drift-affected sensor-years are flagged rather than modelled, because corrections tend to move the artefact elsewhere, and VIIRS covers those years."

### T5. Monthly aggregation keyed by local date
- **Does:** sums to calendar months, keyed by local date, so sampling bias in the daily fire cycle averages out.
- **Choices:** UN (time step).
- **Data:** yes.
- **Precedent:** TRMM VIRS restricted to monthly totals in GFED3 (Giglio et al. 2010). Fire: yes.
- **Evidence:** keying by UTC moved 455 Terra hotspots from 30 June 2021 into July; June's factor flips 0.30 to 0.52 between keyings.
- **Cannot fix:** a systematic overpass shift.
- **Effort:** hours.
- **Justification:** "Monthly totals keyed by local date avoid Terra's evening pass falling into the next UTC day."

### T6. Observation-opportunity and cloud normalisation (context)
MOD14CMQ overpass-corrected count `CorrFirePix` and cloud-corrected count (Giglio, Csiszar and Justice 2006); cosine-of-latitude factor (GFED5); daily equatorial coverage (Giglio et al. 2006 ACP); nadir-equivalent looks and observability (Hyer et al. 2015 poster). Choices: SC. Need all pixels observed or cloud fractions; available only as external 0.25° MODIS files with no VIIRS equivalent found. Cloud correction overcorrects (about +20% counts, lower correlation with burned area). Cosine of latitude is nearly constant across 49–52.5°N and cancels against the same area's history. Point rows: no. Fire precedent: yes. Effort: a day or more.

### T7. Overpass reconstruction from granule metadata or swath outlines
- **Does:** lists every pass over an area, including passes with no fire, from LAADS geoMeta files (MODIS from 2000, VIIRS from 2012) or the FIRMS swath outlines added in June 2026.
- **Choices:** VC (a true per-day availability flag), SC (divide by passes).
- **Data:** external download with Earthdata login; contents not inspected; FIRMS warns against swath edges and gives no archive range. Point rows: no.
- **Precedent:** Luo et al. 2024 data statement. Fire: yes.
- **Evidence:** the only source found for empty passes; would supply the per-day availability flag that C1 needs (the published outage list is insufficient). Gives no cloud information.
- **Effort:** a day or more.
- **Justification:** "Granule footprints give the number of looks independent of whether fire was found."

### T8. Distinct detecting passes as a coverage proxy
- **Does:** counts distinct satellite-time clusters with at least one hotspot.
- **Choices:** VC.
- **Data:** yes.
- **Precedent:** none. Fire: no.
- **Evidence:** already used by the team as a VIIRS availability flag. As a normaliser it cannot tell a quiet month from a missed pass, which fails at small areas. Deriving it from a larger area than the user's is the workaround t08 suggests.
- **Effort:** hours.
- **Justification:** defensible only as an availability flag derived over a large area.

---

## Family C: combining sensors flying together

### C1. Per-satellite scaling, daily mean of available satellites, monthly sum
- **Does:** scales NOAA-20 and NOAA-21 to Suomi NPP, averages the satellites with data each day, sums over the month.
- **Choices:** VC.
- **Data:** rows plus a per-day availability flag (derived; see T7, T8). Yes.
- **Precedent:** fire, yes: GFED5NRT and GBBEPx process each satellite then average with fallback (r02); Li et al. 2022. Outside fire: Ocean Colour CCI equal weights per sensor. Principle that output must not depend on how many satellites flew: Remy and Kaiser 2014.
- **Evidence:** strongest choice in the evidence. Factors 1.011 and 1.034. Departs from a complete month by under 1% (median), 1.5–11% worst in simulated outages. Summing gives 1.99 and 2.95 times; a plain monthly mean is about 30% low in real outage months (July–August 2022). November 2026 drops to two satellites on 2 November.
- **Cannot fix:** the ±15–20% single-month scatter between identical instruments.
- **Effort:** hours; measured.
- **Justification:** "Each VIIRS satellite is scaled to Suomi NPP and the available satellites are averaged daily, as GFED5NRT and GBBEPx do, so the record does not step when NOAA-20 and NOAA-21 join or Suomi NPP ends."

### C2. Single reference satellite with fallback
- **Does:** every comparison uses one designated satellite; others are a fallback or ignored. The break when the reference changes is accepted.
- **Choices:** VC, TR.
- **Data:** yes.
- **Precedent:** fire, yes: INPE Programa Queimadas (NOAA-12 then Aqua; the 2002 switch "caused the discontinuity"; plan to move to Suomi NPP, which has now ended, gives no method); FEDS and Su and Yu use Suomi NPP only.
- **Evidence:** one reference with monthly fallback errs 6–12% in fallback months. Suomi NPP has ended, so a VIIRS reference must now be NOAA-20 (0.99 of Suomi NPP, overlaps stable-orbit MODIS only 2018–2021). INPE's own reference (Aqua) is drifting.
- **Cannot fix:** pre-2012 bridge.
- **Effort:** hours.
- **Justification:** "Using one satellite throughout is the INPE approach and avoids combination rules, at the cost of an accepted break when the reference ends."

### C3. Inverse-variance weighting
- **Does:** weighted mean of estimates already on a common scale, weights 1/variance. The covariance-intersection caveat: with correlated errors, do not report the fused uncertainty below that of one satellite.
- **Choices:** VC.
- **Data:** yes.
- **Precedent:** Durrant-Whyte 2001; Khaleghi et al. 2013. Fire: no.
- **Evidence:** VIIRS satellites agree within a few percent, so weights barely differ from C1's equal weights; their errors are correlated.
- **Effort:** hours.
- **Justification:** supplies the theory behind C1's equal weighting.

### C4. Union or k-of-n voting
- **Does:** a cell-day counts if k of n sensors flag it (k = 1 is the union). The optimal Chair–Varshney rule needs each detector's detection and false-alarm rates.
- **Choices:** VC, UN.
- **Data:** yes (optimal weights: no).
- **Precedent:** Chair and Varshney 1986. Fire: no.
- **Evidence:** union of 5 km cell-days steps up 1.24 and 1.37 times when satellites are added, more in quiet years. Stable only with a fixed sensor set.
- **Effort:** hours.
- **Justification:** documents why a union was not used.

### C5. Priority switch
- **Does:** uses the preferred sensor where it has data, otherwise a rescaled second sensor.
- **Choices:** VC, TR.
- **Data:** yes.
- **Precedent:** fire FRP fusions (Li et al. 2019; Li et al. 2022; Zheng et al. 2026). None tests continuity across the switch.
- **Evidence:** after 2012 it reduces to "use VIIRS"; before 2012 there is no VIIRS to prefer. In effect it is S1 plus a switch date.
- **Effort:** hours.
- **Justification:** "Published fire fusions prefer VIIRS wherever it exists and rescale the other sensor elsewhere."

### C6. Single-satellite to constellation regression
- **Does:** fits, over years when all sensors flew, the relation of a reduced sensor set to the full set, and applies it when only the reduced set flew. Count analogue: Terra-only (2000–2002) to Terra+Aqua, and MODIS to VIIRS.
- **Choices:** SC, VC.
- **Data:** yes.
- **Precedent:** fire, yes: GFAS Terra-only 2000–2002 (Remy and Kaiser 2014, FRP; Terra r² 0.5–0.8 vs Aqua 0.85–1; boreal coefficients near 1; fitted only where ≥ 400 positive cells per region); GFED5 Terra-only coefficients for 2001–2002 (Chen et al. 2023).
- **Evidence:** Terra/Aqua is 0.72 by day and 2.2 at night (2003–2021); including Terra-only years in a baseline changed 8% of fire-season labels. Must be fitted on the box, outside drift years.
- **Cannot fix:** zeros, drift; untested on counts.
- **Effort:** hours.
- **Justification:** "The 2000–2002 Terra-only years are brought to the Terra+Aqua level with a factor fitted when both flew, as GFAS and GFED5 do."

### C7. Capture-recapture on cell-days
- **Does:** from cell-days found by sensor A only, B only and both, estimates the total including those neither found (Lincoln–Petersen N = n1·n2/m; log-linear models for more lists).
- **Choices:** UN, VC.
- **Data:** yes.
- **Precedent:** epidemiology (Chao et al. 2001). Fire: no.
- **Evidence:** t07 illustration from the 1.24 union: each VIIRS satellite about 76% complete, assuming independence, which identical instruments violate (bias low). MODIS-only cell-day overlap with VIIRS has not been measured. Overlaps too few below about 50 km.
- **Cannot fix:** the MODIS–VIIRS gap; it estimates what was missed.
- **Effort:** hours for two lists; a day for three or more.
- **Justification:** a truth-free estimate of completeness, useful as context for how much even VIIRS misses.

### C8. Truth-free error estimation (context)
Triple and extended collocation (Gruber 2016; Brennan et al. 2019 on burned area, fire); categorical triple collocation and latent-class models (Pierdicca et al. 2018; Hui–Walter; Dawid–Skene); occupancy models (MacKenzie et al. 2002); Dempster–Shafer combination (Khaleghi et al. 2013). Choices: VC. All need independent errors across three or more systems, or recorded non-detections. The five sensors form two error-correlated families, and a cell-day without a hotspot may have been cloudy or not overpassed. Zero months must be dropped, which drops most small-area months. Point rows: no in practice. Effort: days or more.

### C9. Operational gridded fusion (context)
GFAS observed-area weighting with a scalar Kalman filter through cloud gaps (Kaiser et al. 2012); GOFER per-pixel combination of GOES-East and West confidence (Liu et al. 2024; IoU 0.77 vs 0.67/0.75); NOAA HMS analyst review; FRP and burned-area fusion (Boschetti and Roy 2009). Choices: VC. Need observed area, cloud masks, geostationary data or analysts. Point rows: no. Fire precedent: yes. Use: HMS warns that adding or removing satellites "can introduce large variation in system performance", which supports C1.

---

## Family J: the join in time

### J1. Chain-linking over a long overlap through an intermediate sensor
- **Does:** rescales each new series to the old over a link period and multiplies successive link factors. A ratio of sums over many months is the count analogue of mean splicing (the least-squares solution on log differences).
- **Choices:** SC, VC.
- **Data:** yes.
- **Precedent:** Eurostat, ONS 2020, Chessa 2023 (price indices); Ocean Colour CCI bridged VIIRS to SeaWiFS through MODIS-Aqua. Fire: no.
- **Evidence:** NOAA-21 never overlaps stable-orbit MODIS; NOAA-20 only for four years. Links 1.011, 1.034 and 0.242. VIIRS links add little error. Linking on one month or quarter (the Eurostat convention) would carry the 15–30% scatter into the whole series. Every MODIS factor goes through Suomi NPP, which has ended.
- **Cannot fix:** scatter, zeros, drift.
- **Effort:** hours.
- **Justification:** "NOAA-21 is linked to MODIS through Suomi NPP over long overlaps, as Ocean Colour CCI linked VIIRS through MODIS-Aqua; the VIIRS links are within a few percent."

### J2. Keep a documented seam
- **Does:** keeps each sensor era as its own record (for example VIIRS-only from 2012, MODIS shown separately), correcting only within each, and accepting a visible break.
- **Choices:** TR.
- **Data:** yes.
- **Precedent:** Gibson 2021 for night lights; INPE accepts its 2002 break; Giglio et al. 2025 advise against concatenating MODIS and VIIRS burned area at local scale. Fire: yes.
- **Evidence:** the team lists the VIIRS-only record from 2012 as a small-area fallback. The challenge asks for history "from the early 2000s", so a seam alone does not meet it.
- **Effort:** hours.
- **Justification:** "Where the records cannot be joined locally, they are shown separately, as the MODIS and VIIRS burned-area authors advise."

### J3. Integrated count model with shared monthly activity
- **Does:** each count n(sensor, day/night, month) ~ NB with mean exp(a_m + b_sk). Suomi NPP fixed as reference; sensor factors b fitted on the whole box; then a_m fitted per month for the user's area with b held fixed. Months a sensor did not fly have no rows.
- **Choices:** SC, VC, TR (a_m is a sensor-free activity level).
- **Data:** yes.
- **Precedent:** integrated ecological count models (Gilbert et al. 2024, abstract only). Fire: no.
- **Evidence:** uses zero MODIS months properly; likelihood intervals; day/night at no cost; all overlaps at once. Still chained through Suomi NPP; intervals too narrow because VIIRS satellites share ±15–20% scatter; does not capture the 25–50% activity dependence.
- **Cannot fix:** zeros (intervals become very wide pre-2012 at small areas), drift, Kamloops source.
- **Effort:** a few hours; a day for a Bayesian version with smoothing.
- **Justification:** "Each sensor is treated as a noisy view of one monthly activity level with its own detection factor, the integrated-model approach used for multi-source wildlife counts."

### J4. State-space model with a time-varying factor or level shift
- **Does:** a latent level plus a sensor factor that either shifts once at a known break (intervention) or drifts as a random walk. The general Kalman form (t07) is the same idea with Gaussian noise.
- **Choices:** MD, SC.
- **Data:** yes.
- **Precedent:** labour-force survey redesigns (Zhang, van den Brakel and Tam 2019; van den Brakel and Krieg 2015). Fire: no (Mandel et al. 2008 assimilates into a fire-spread model, not counts).
- **Evidence:** the only member that could track Terra's decline (0.95 to 0.46) because VIIRS overlaps the whole drift. Counts are zero-heavy (91% of fire-season months empty at 10 km); random-walk factor needs custom code.
- **Effort:** a day or more.
- **Justification:** "A time-varying factor lets drift-period MODIS be used while estimating its declining efficiency against VIIRS."

### J5. Dynamic factor model with missing data
- **Does:** each series = loading × shared latent factors + noise; Kalman smoother fills missing cells (statsmodels `DynamicFactorMQ`).
- **Choices:** SC.
- **Data:** yes.
- **Precedent:** GDP nowcasting (Bańbura and Modugno 2014). Fire: no.
- **Evidence:** standardises each series over its own window, so a late sensor's mean depends on which fire years it saw (2017, 2018, 2021 dominate); assumes Gaussian, stationary series.
- **Effort:** hours to run; hard to justify.
- **Justification:** not recommended by its own topic file.

### J6. Reference chosen by stability or calibration confidence
- **Does:** selects as anchor the sensor with the most stable sampling or the most trusted calibration, not necessarily the newest. Pinzon and Tucker 2014 show an older, partly overlapping sensor can be the reference.
- **Choices:** TR.
- **Data:** none beyond overpass times. Yes.
- **Precedent:** ESA CCI soil moisture and SST (Gruber et al. 2019; Merchant et al. 2019). Fire, yes: QFED moving its anchor to NOAA-20; INPE uses Aqua.
- **Evidence:** VIIRS times constant (about 12:40 and 02:10) while Terra moved from about 11:15 to 09:20 and Aqua to 14:51; MODIS ends 2027; area burned favours neither sensor; the challenge says "either alternative is fine if properly justified".
- **Effort:** hours (an argument, not a computation).
- **Justification:** "Climate data records anchor to the most stable sensor; VIIRS overpass times have not moved, while MODIS times have moved two hours."

### J7. Same algorithm on both sensors plus regional intercalibration (context)
MCD64A1 to VNP64A1 (Giglio et al. 2025: Boreal North America VIIRS +10.0%, slope 1.07); WF_ABBA to GOES-16 FDC algorithm lineage. Choices: TR. Need radiances and the detection code. Point rows: no. Fire precedent: yes. Use: the authors' statement that "simple concatenation ... at local scales is not advisable" matches the team's area-size limit.

---

## Family E: how the result is expressed

### E1. Per-sensor standardised anomaly (z-score)
- **Does:** (current − mean) / standard deviation over the same period in earlier years of the same sensor; labels at ±1 and ±2 SD. Ramoino et al. 2013 compared ATSR and MODIS by residuals from each sensor's own seasonal cycle.
- **Choices:** UN, TR (no cross-sensor factor).
- **Data:** yes.
- **Precedent:** fire, yes: Global Forest Watch (VIIRS from 2012, MODIS from 2001, never mixed); ATSR World Fire Atlas.
- **Evidence:** rank correlation 0.97 between sensors; same class in 71% of fire-season months, 44% of near-normal months; never more than one class apart in 98%. Counts are skewed (one year like 2017 inflates the SD). GFW code labels a month "normal" when SD is zero, which happens at 10 km in most months. Terra 2026 day drop biases MODIS-vs-MODIS anomalies.
- **Cannot fix:** a current VIIRS month still has no pre-2012 history without a bridge.
- **Effort:** hours.
- **Justification:** "Comparing each sensor only with its own history, as Global Forest Watch does, avoids any cross-sensor factor."

### E2. Mean-based display: mean with min-max band, percent from mean
- **Does:** plots the current value against the mean and the range of reference years, or reports percent above or below the calendar-month mean.
- **Choices:** UN.
- **Data:** yes.
- **Precedent:** fire, yes: EFFIS in Copernicus ESOTC 2025; INPE statistics page and Infoqueima ("27% below the June mean for 2010–2024").
- **Evidence:** one extreme year sets the band; the mean is dominated by 2017, 2018, 2021; percent is undefined when the mean is zero.
- **Effort:** hours.
- **Justification:** "This is how EFFIS and INPE present current fire activity against history."

### E3. Ratio to the calendar-month median
- **Does:** current month ÷ median of the same calendar month in baseline years.
- **Choices:** UN.
- **Data:** yes.
- **Precedent:** challenge wording ("the historical median"). Fire: no published use found.
- **Evidence:** undefined below about 100 km radius, where the MODIS median is zero for most months.
- **Effort:** hours.
- **Justification:** matches the challenge request directly.

### E4. Empirical percentile rank with tie handling
- **Does:** ranks the month among baseline months; tied zeros get the mid-rank or a random value within their step (randomised quantile residuals, Dunn and Smyth 1996). Converting the rank to a normal score (Farahmand and AghaKouchak 2015) adds nothing for short tied records.
- **Choices:** UN.
- **Data:** yes.
- **Precedent:** not in fire. Fire: no.
- **Evidence:** rank agreement 0.97, class agreement 71%; coarse with 10–14 years; zeros produce ties; changing baseline years changes 8–21% of labels.
- **Effort:** hours.
- **Justification:** "A rank is robust to the skew of fire counts and does not need a fitted distribution."

### E5. Fitted standardised index (SPI family)
- **Does:** fits a gamma to non-zero values of one calendar month, adds the zero share q as H(x) = q + (1 − q)G(x), converts to a normal score.
- **Choices:** UN.
- **Data:** yes.
- **Precedent:** drought monitoring (WMO 2012; Stagge et al. 2015; Pieper et al. 2020). Fire: no.
- **Evidence:** WMO asks for 20–30+ years; Pieper et al. limit zeros to 34%; VIIRS has 14 years and small areas exceed the zero limit.
- **Effort:** a day.
- **Justification:** cite as considered and rejected for record length.

### E6. Rescale to a reference, then compute anomalies
- **Does:** maps each sensor onto the reference sensor over the overlap (ratio or CDF matching), then computes one anomaly series. Multi-sensor soil-moisture and vegetation records do this; none reviewed blends raw per-sensor anomalies.
- **Choices:** TR, SC.
- **Data:** yes.
- **Precedent:** ESA CCI soil moisture (Gruber et al. 2019); Reichle and Koster 2004; Franquesa et al. 2025 (rejected QM for this step). Fire: no.
- **Evidence:** the only option in this family giving one baseline before 2012. Inherits 14–30% monthly scatter and drift; CDF matching spreads tied zeros.
- **Effort:** hours with a ratio; a day or more with CDF matching.
- **Justification:** "Established multi-sensor climate records rescale every sensor to one reference before computing anomalies."

### E7. Fixed reference period with frozen parameters
- **Does:** fits baseline statistics once on fixed years and reuses them, so past labels do not change.
- **Choices:** UN.
- **Data:** yes.
- **Precedent:** Franquesa et al. 2025 (1981–2023). Fire: INPE's fixed 2010–2024 mean is close to this; t12 marks the method itself as non-fire. Marked yes in the table on the INPE basis.
- **Evidence:** changing baseline years changes 8–21% of labels. Future VIIRS months come from NOAA-20 and NOAA-21 (0.99 and 0.97 of Suomi NPP).
- **Effort:** hours.
- **Justification:** "A frozen baseline makes a month's label reproducible."

---

## Family V: validation and uncertainty (supports any method)

### V1. Year-blocked cross-validation
- **Does:** leave-one-year-out over 2012–2021, plus a split (fit 2012–2016, test 2017–2021, and reverse); score log or relative error against the plain ratio and against the VIIRS-to-VIIRS floor (±15–20%); report 2017, 2018 and 2021 separately.
- **Precedent:** Roberts et al. 2017 (random hold-outs give "serious underestimation of predictive error"); Nechaev et al. 2021 year-out tests; Cannon et al. 2015. An unreviewed October 2026 hackathon project used a 2012–2020 / 2021–2024 split with placebo step tests. Fire: no peer-reviewed use.
- **Evidence:** about ten independent years; high variance because three years dominate. A residual step at 2012 is testable only on held-out years.
- **Effort:** hours.
- **Justification:** "Every factor is scored on fire seasons it was not fitted on."

### V2. Stability as the trend of the difference; drift diagnosis
- **Does:** reports the bias and per-year trend of log(MODIS/VIIRS) over 2012–2021 with an interval, and the drift years separately; maps the spurious trend of a drifting sensor against a stable one.
- **Precedent:** SST CCI (Merchant et al. 2019); Julien and Sobrino 2022; Nagol et al. 2014. Fire: no.
- **Evidence:** the team's Terra-vs-NOAA-20 table already is this diagnostic.
- **Effort:** hours.
- **Justification:** "Stability is shown as the trend of the inter-sensor difference, the standard climate-data-record metric."

### V3. Fixed-date step tests with pairwise attribution
- **Does:** tests a step in log-ratio series at known dates (April 2018, January 2022, March 2023) with autoregressive errors (Lund et al. 2023: fixed-date tests are more powerful); blames the sensor whose pairs break (pairwise homogenization, Menne and Williams 2009). Benchmarked homogenization (Venema et al. 2012) shows only the best methods improve intermittent precipitation, the nearest analogue to counts.
- **Evidence:** usable at about 100 km radius or more; only steps larger than about the 15–20% VIIRS scatter are detectable within a few years. Before 2012 only Terra and Aqua exist, so a shared MODIS change is invisible. A trend after 2022 fits Terra's decline better than a step.
- **Effort:** hours.
- **Justification:** "Known sensor changes are tested as fixed-date breaks and attributed by which sensor pairs break."

### V4. Prediction intervals and ensemble records
- **Does:** draws the factor from year resampling (0.237–0.28), adds a monthly residual from hold-out errors (14%, 23%, 30% by month size), adds Poisson noise, and reports a median, interval and the probability of each calendar class. Optionally publishes an ensemble of plausible records.
- **Precedent:** Merchant et al. 2017; HadCRUT5 200-member ensemble; ciTools simulation intervals. Fire: no.
- **Evidence:** one factor applied to every year "induces correlation" (Miller et al. 2023), so factor error does not average out over a converted baseline median.
- **Effort:** hours to a day.
- **Justification:** "Pre-2012 months carry an interval and a class probability that include factor, monthly and count uncertainty."

### V5. Fusion vocabulary
- **Does:** names the problem: hotspots are decision-level outputs; the sensors are competitive (same quantity) with a complementary part (different times and pixel sizes); data-level fusion is impossible without radiances.
- **Precedent:** Beddar-Wiesing and Bieshaar 2020; Khaleghi et al. 2013. Fire: no.
- **Effort:** none beyond writing.
- **Justification:** frames the write-up in standard sensor-fusion terms, which the user asked to consider.

---

## What combines and what excludes

**Mutually exclusive (pick one of each group):**
- VIIRS combination rule: C1 daily mean, C2 single reference, C4 union, or summing (rejected by evidence). C3 justifies C1; C5 reduces to C1 plus a switch.
- Form of the MODIS–VIIRS conversion: S1 ratio, S3 GLM, S6 curve, S7 symmetric line, S8 quantile mapping, S12 trees. S2 (covariates) sits on top of S1 or S3. J3 replaces S3 + J1 with one joint model.
- Treatment of drift-period MODIS: T4 flag or exclude, T1 diurnal weighting, or J4 time-varying factor. T4 can follow T1 as a check.
- Route to a pre-2012 baseline: per-sensor anomalies (E1, E4) with no conversion, or conversion to one record (S family + E6). J2 (seam) excludes a single baseline. The two routes can be run together, one as a cross-check on the other.
- Direction: S9 and S1 applied downward give a MODIS-equivalent record; S1 applied upward and S11 give a VIIRS-equivalent record. Most other methods work in either direction.

**Dependencies:**
- Remove additive sources (the Kamloops site) before any multiplicative factor (S1–S3, J1, J3, S9).
- Any unit (U1, U3, U4) must be built per satellite and combined by C1, not pooled or unioned, or it steps at 2018 and 2023.
- C1 needs a per-day availability flag (T7, or T8 derived over a large area).
- Factors (S1–S8, C6, J1) must be fitted on the stable-orbit window and on a large area, not the user's circle.
- T5 (local-date months) applies to everything.
- V1–V5 combine with anything.

## Combinations the literature and the evidence would support

Listed from simplest to most elaborate. They are options with trade-offs, not a ranking. The target record (MODIS- or VIIRS-equivalent) can be chosen independently in B to E; J6 supplies the argument either way.

### A. Per-sensor anomalies, no conversion
**Pieces:** T5 local-date months; C1 for VIIRS; E1 or E4 (or E3 where the median is non-zero) computed per sensor against its own history; E7 frozen baselines; T4 flag Terra-by-day from 2023; small-area fallbacks from the evidence (enclosing area, season, presence/absence). V5 for framing.
**Claims:** each month is judged only against the same sensor's history, as Global Forest Watch does; no cross-sensor factor is needed; month order agrees across sensors (rank correlation 0.97).
**Leaves unsolved:** a current VIIRS month has VIIRS history only from 2012; linking it to 2000–2011 assumes anomalies are sensor-independent, supported only by 71% class agreement (44% near normal) and no published precedent; MODIS ends in 2027; changing baseline years changes 8–21% of labels; zeros below about 100 km.
**Effort:** hours.

### B. One overlap factor, joined through Suomi NPP
**Pieces:** remove the Kamloops source; T5; C1 (1.011, 1.034); S1 with S2 day/night (0.34, 0.18), fitted on the box over February 2012 to December 2021; J1 chain to NOAA-20 and NOAA-21; C6 for Terra-only 2000–2002; T4 (do not fit on drift years; use VIIRS where it exists); J6 to argue the anchor; E3 or E4 against one baseline (E6); E7; V1 and V2.
**Claims:** the GFED3 / Ocean Colour CCI design applied to counts; relation is proportional with slopes near 1; about 10% error on a season; no step at 2018, 2023 or November 2026.
**Leaves unsolved:** single-month error 14–30%; months MODIS missed at small areas; activity dependence (quiet months 25–50% higher); no independent check of pre-2012 months except yearly BC fire records.
**Effort:** hours; most numbers are already measured.

### C. B with stated uncertainty and small-area honesty
**Pieces:** B, with S3 (NB GLM with offset) or J3 (integrated count model) in place of the plain ratio; S5 hurdle by radius class; V4 prediction intervals reported as class probabilities; V3 step tests at 2018, 2022 and 2023 on the box.
**Claims:** each converted month carries an interval and a probability of each class; the app can say how often a converted month would read zero at the chosen radius.
**Leaves unsolved:** everything B leaves; intervals are too narrow where VIIRS satellites share errors; the GLM treats VIIRS as exact.
**Effort:** about a day.

### D. B or C on a pixel-size-neutral unit
**Pieces:** B (or C) with U1 daytime 2 km cell-days (factor 0.65 all hours, 0.68 by day), or U2 duplicate removal before counting; built per satellite and averaged by C1; raw counts kept as the headline figure because of the challenge wording.
**Claims:** the sensors move closer in level, MODIS same-pass duplicates go, and the daytime factor is steadier across years (0.62–0.85).
**Leaves unsolved:** single-month gain is modest (about 20% vs 24–29%); night cell-days swing eightfold; large months are compressed; not "number of hotspots"; daytime cell-days are out of range in 2026 too.
**Effort:** hours on top of B.

### E. B or C with a physical model of sampling and detection
**Pieces:** C, plus T1 (published forest diurnal curve) to keep drift-period Terra day counts, or J4 (time-varying factor against VIIRS); plus S9 (detection-limit emulator) as a physical cross-check of the day and night factors, and as the route to a MODIS-equivalent record after 2027 if that target is chosen; V1 hindcast of emulated vs actual Aqua counts 2012–2021.
**Claims:** the factors and the Terra decline are explained by detection limits and overpass time, not only fitted.
**Leaves unsolved:** the curve is for FRP over a continent (predicted 0.37 vs measured 0.46 in 2026) and multiplies Terra 2026 counts by about 2.7; the emulator has been validated only on FRP totals and needs assumed MODIS pixel areas and no cloud state; J4 needs custom code and struggles with zero months; small-area zeros remain.
**Effort:** a day for the T1 and S9 cross-checks; days or more for J4 or a validated emulator.

## Where the topic files disagree

- Quantile or CDF mapping: t02, t03 and t10 (plain QM) rate it low; t10 (chained onto a stable reference) and t12 (rescale then anomaly) rate it medium. t12 also cites Franquesa et al. 2025 rejecting QM for harmonization.
- Diurnal correction: t05 rates weighting by a published curve (Gui et al. 2026) medium and hours; t02 rates diurnal adjustment low and days because the team cannot derive a cycle; t08 rates it medium but days because it needs geostationary data. The difference is whether a continental FRP curve may stand in for a local count curve.
- Single-satellite to constellation regression (Remy and Kaiser 2014): high in t08, medium in t05.
- Triple collocation effort: hours in t11, days or more in t02 and t07 (all rate it low).
- Giglio et al. 2025 burned-area intercalibration: low in t03 (cannot rerun the algorithm), medium in t08 (expert backing for overlap calibration).
- FEDS object tracking: medium in t06 (runs on hotspot points); not applicable in t08 (outputs perimeters, not counts).
- Overlap regression with a chosen functional form: high in t01; t02 rates translation equations medium because slopes near 1 add little over a ratio.
- Sofiev and Kouznetsov 2026: the abstract and conclusions give detection limits (3.7 MW night nadir, 40 MW day side view; 5.7 and 3.7 MW) that do not match the paper's tables (about 5.0 and 5.4 MW at 1 km²). t04 uses the tables.
- Published MODIS detection limits differ by definition: 2.5 MW (Fu), 4.1 MW (Zheng), about 5 MW (Sofiev), 5–8 MW (Sperling) at nadir; 10–50 MW off nadir (Freeborn 2014).
- INPE reference history: FAQ questions 7 and 38 give different end dates for NOAA-12 as reference (t03); t12 could not confirm which satellite fed INPE's series before Aqua.
- Tong et al. 2026 (preprint) is internally inconsistent: R² above 0.95 in the PDF abstract vs 0.87 in the held-out table, and overlap given as 2012–2013 and as 2013 (t13).
- Liu et al. 2024 (GOFER) describe the two-satellite combination as the minimum in one passage and the average in another (t08).

## Gaps

- No published method, fire or otherwise, harmonizes MODIS and VIIRS hotspot counts; every count-level mapping here is inference.
- No count-level validation of any detection-limit emulator (S9) exists.
- No diurnal fire curve for counts in Interior BC conifer forest; the closest is a continental FRP curve.
- No cross-sensor test of active cell-days, fire events or per-sensor anomalies in the literature.
- Contents of LAADS geoMeta files and FIRMS swath outlines were not inspected; their usefulness as an availability flag is untested.
- FIRMS acquisition-time precision is undocumented, which limits same-pass duplicate rules and footprint matching.
- Event-clustering thresholds have not been tuned or tested for Interior BC.
- The overlap of MODIS-only and VIIRS cell-days (needed for capture-recapture) has not been measured.
- Remy and Kaiser's single-satellite regression has not been tested on counts; treatment of the 2000–2002 Terra-only years is open.
- Several sources were read as abstracts only, and most topics exhausted their search budget, so "not found" results are incomplete.
