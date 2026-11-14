# Harmonization methods: a literature review of the options

Team reference for City of Kamloops & Co. It catalogues the methods that could be used to combine MODIS and VIIRS hotspots into one record, drawn from fire science, from sensor-fusion research, and from other fields that have joined records across a change of instrument. For each method it gives published precedent, what the team's own measurements say about it, and the effort involved. It sets out options and trade-offs. It does not rank them or choose one.

Compiled 2026-11-14. Thirteen families of methods were each reviewed by a researcher and then checked source by source by a verifier. A reconciliation pass compared the thirteen results, re-opened 27 of the sources that carry most weight, and filled two gaps. A second pass merged the results into one catalogue. The fifteen working files are in [harmonization-methods-research/](harmonization-methods-research/); the full entry for every method is in [_catalogue.md](harmonization-methods-research/_catalogue.md). The team's measurements are in [harmonization-evidence.md](harmonization-evidence.md).

**Later tests.** Several of the methods below were tested on the team's data after this catalogue was first compiled. The results are reported in [harmonization-tests.md](harmonization-tests.md) and summarised in [What the later tests found](#what-the-later-tests-found). Statements that the tests changed are corrected in place and listed, with their date and source, under [Changes since first compiled](#changes-since-first-compiled).

**The team's recommended method.** A separate piece of work on the same day produced [harmonization-research.md](harmonization-research.md), which recommends a method, and `harmonize.py`, which implements an interim version of it. How the results here bear on that method is set out in [harmonization-tests.md](harmonization-tests.md#how-this-relates-to-the-teams-recommended-method).

**Two facts frame everything below.**

1. **No published source harmonizes MODIS and VIIRS hotspot counts.** Every statement here about how a method would work on counts is the reviewers' reasoning from the method and the team's data, not a published result.
2. **No method restores fires that MODIS never detected.** Below about a 50 km radius, MODIS records nothing in a third or more of the months in which VIIRS saw fire. Every method leaves this unsolved.

**How far to trust it.** No fabricated citation was found among the 27 sources re-opened, and every DOI checked resolved to the stated paper. Several sources were read as abstracts only, and most topics used up their search budget, so "none found" is not proof that none exists. Five errors of description in the working files are listed under [Corrections to the working files](#corrections-to-the-working-files).

## At a glance

1. **The literature offers 57 distinct methods in seven groups:** those that change the unit, the scale, the sampling, the combination of sensors flying together, the join in time, the way the result is expressed, and the validation.
2. **48 of the 57 can be built from FIRMS point rows, most of them in hours.** The other nine need radiances, cloud masks, swath coverage or geostationary data that the team does not have.
3. **The most common design in fire science is a multiplicative factor fitted over an overlap period on a large region.** GFED3 merged two older sensors into the MODIS record this way. The team has already measured its factor (0.242).
4. **The same idea appears under about a dozen names** across fields: ratio estimator, overlap regression, chain-linking, mean splice, bias correction to a reference, single-satellite regression.
5. **Sensor-fusion research mostly addresses a different problem.** It combines sensors that fly at the same time. That helps with the three VIIRS satellites. It does not, on its own, join a record across a change in the sensor mix, which the product authors say needs calibration over an overlap.
6. **Most fusion theory needs what hotspot rows lack:** continuous measurements, known independent errors, and a record of looks that found nothing.
7. **Two established practices exist for expressing "now against history" without converting units:** Global Forest Watch compares each sensor only with its own history, and Brazil's INPE keeps every comparison inside one reference satellite and accepts a break when the reference changes.
8. **Correcting the Terra drift with a published daily fire curve works for 2022–2024 and over-corrects 2025–2026** (by 21–25% in the first computation, and by 26% and 37% in the later test). The alternative in the literature is to flag drifted years, not correct them.
9. **Several attractive methods fail on the length of the record.** Quantile mapping, fitted standardised indices and machine-learning models all need more independent years than the ten available.
10. **Two fields outside remote sensing have count-level precedents:** fisheries, which converts catches between survey vessels, and seismology, which compares earthquake counts across network upgrades.

## Sensor fusion: what applies and what does not

Detail: [t07](harmonization-methods-research/t07-data-fusion-theory.md), [t08](harmonization-methods-research/t08-fire-fusion-products.md), [t13](harmonization-methods-research/t13-machine-learning-and-spatiotemporal-fusion.md).

**The vocabulary.** Sensor-fusion research sorts fusion by level: raw data, extracted features, or decisions. A hotspot is a decision: each agency's algorithm has already thresholded the measurement into "fire here". Fusion at the data level is not possible without the radiances. The research also sorts sensors by role. The five fire sensors are competitive (they measure the same quantity) with a complementary part (different times of day and pixel sizes).

**Two questions that fusion treats differently.**

| Question | What the literature offers |
|---|---|
| Combining sensors that fly at the same time, to get the best estimate of one month | Well developed. Average the satellites, weighted by reliability, with a fallback when one is missing. GFED5NRT and NOAA's GBBEPx do this for VIIRS. Emissions systems require that the result not depend on how many satellites flew ([Remy and Kaiser 2014](https://acp.copernicus.org/articles/14/13377/2014/)). |
| Joining a record across time when the sensor mix changes | Not solved by fusion alone. The authors of the MODIS and VIIRS burned-area products say it needs calibration over an overlap period, and that "simple concatenation ... at local scales is not advisable" (Giglio et al. 2025). NOAA's Hazard Mapping System warns that adding or removing satellites "can introduce large variation in system performance". |

**Fusion ideas and their fit.**

| Idea | Needs | Fit to hotspot rows |
|---|---|---|
| Weighted averaging of redundant sensors (inverse-variance, best linear unbiased estimate) | Estimates on a common scale | Fits the three VIIRS satellites. They agree within a few percent, so the weights are nearly equal. |
| Voting or union across detectors | A fixed set of detectors | A union steps up 1.24 and then 1.37 times as satellites are added. |
| Capture-recapture (estimating events all detectors missed) | Independent detectors | Cheap to try on grid cells. Identical instruments are not independent, so it under-estimates what was missed. |
| Kalman filter or state-space model | Roughly Gaussian noise, or custom count code | A count version with a time-varying sensor factor is the one model that could track Terra's decline. A day or more of work. |
| Triple collocation (sensor errors without a truth reference) | Three systems with independent errors | Rejected by all four topics that examined it. The five sensors form two families whose errors are shared. |
| Evidence combination (Dempster-Shafer), occupancy and latent-class models | Recorded non-detections | Not available: a cell with no hotspot may have been cloudy or not overpassed. |
| Operational fire fusion (observed-area weighting, geostationary gap-filling, analyst review) | Observed area, cloud masks, geostationary data | Context only. |
| Spatiotemporal image fusion (the STARFM family) and deep-learning translation | Dense paired images | Context only. One fire use was found (coal-fire imagery). |
| Machine-learning translation between sensors | Thousands of training samples | The team has about 116 overlap months and ten independent fire seasons. Only the smallest model survives, and it is the count regression listed below. |

The parts that do transfer from the image-fusion and machine-learning literature are a validation design (hold out whole years) and an argument about direction: a model can degrade a fine sensor to look like a coarse one, but "there is no deterministic way to add detail" in the other direction.

## The methods

Each table lists the methods in one group. **Rows** means the method can be built from FIRMS point rows alone. **Fire** means a published fire product or study has used it, for any fire quantity (usually fire radiative power or burned area, not counts). Methods marked "context" need data the team lacks or days of work; they are listed for the precedent or the argument they supply.

### Changing the unit

Detail: [t06](harmonization-methods-research/t06-fire-events-and-area-units.md), [t01](harmonization-methods-research/t01-nighttime-lights.md).

| ID | Method | Rows | Fire | Effort | What the review found |
|---|---|---|---|---|---|
| U1 | Active cell-days: grid cells with at least one hotspot per day | Yes | No | Hours | The hotspot version of degrading a fine sensor to a coarse footprint, as done for night-time lights. Measured: the ratio rises from 0.24 to 0.65 at 2 km. The single-month gain is modest. Later test: over the ten stable years, daytime 2 km cell-days gain as much over their own short baseline as counts do, and neither win nor lose at box scale. The ratio depends on the definition (0.654 for the union of Terra and Aqua, 0.74 with each sensor and pass counted separately, in fire-season months). |
| U2 | Remove same-pass duplicates before counting | Approx. | Yes | Hours | Used by Zheng et al. 2026. 21–23% of MODIS hotspots have a same-pass neighbour. Cell-days remove these by another route. |
| U3 | Footprint-area union: give each detection a nominal area and merge overlaps | Yes | Yes | Hours | The FINN emissions inventory does this ("the identity of the sensor is not relevant"). Rough arithmetic suggests nominal areas over-correct MODIS to about 1.7 times VIIRS. Untested. |
| U4 | Fire events: link hotspots close in space and time, count events | Yes | Yes | Hours to a day | Published thresholds exist. A northern Alberta study ([Dastour et al. 2024](https://doi.org/10.3390/fire7100355)) matched 94% of fires of 100 ha or more with VIIRS and 88% with MODIS, but under half of 10–25 ha fires. Event counts step up when satellites are pooled. Thresholds are untuned for BC. |
| U5 | Burned-area events and perimeters (context) | No | Yes | Days | Global Fire Atlas, FIRED, GlobFire. Need burned-area products or reference perimeters. |

### Changing the scale: a conversion between sensors

Detail: [t09](harmonization-methods-research/t09-count-calibration-statistics.md), [t04](harmonization-methods-research/t04-detection-limits.md), [t10](harmonization-methods-research/t10-homogenization-and-validation.md), [t03](harmonization-methods-research/t03-fire-record-transitions.md).

| ID | Method | Rows | Fire | Effort | What the review found |
|---|---|---|---|---|---|
| S1 | One multiplicative factor fitted over the overlap, on a large region | Yes | Yes | Hours | The standard design. GFED3 merged ATSR and VIRS into the MODIS record with regional factors, and states it "does not restore" cells with zero counts. Measured: 0.242, about 10% error on a season, 14–30% on a month. Later test: scaled-up MODIS years give the all-VIIRS class in 84% of fire-season months against 66% for a short VIIRS-only baseline, but the factor runs about 15% high in a typical fire-season month and 27% high for a small season, and about a third low in a typical November-to-March month. No refinement of the factor gave better labels. |
| S2 | Factor that depends on a covariate (day or night, region, season) | Yes | Yes | Hours | Operational fire systems split by day and night; fisheries finds the same for day and night catches. Measured: 0.34 and 0.18, no gain in whole-box monthly accuracy, but protection when the day-to-night mix shifts. Calendar-month factors are weak. Later test: with day and night factors the class agrees as often as with one factor in the fire season (83% against 84%) and 7 points less often over all months (73% against 80%), because the night factor is seasonal (0.18–0.19 in July and August, 0.03–0.12 in other months). A follow-up found a seasonal night factor still 4.7 points worse over all months, and day and night factors used only in April to October level with one factor over all months, with a possible loss of a few points. |
| S3 | Count regression with an offset (Poisson, quasi-Poisson, negative binomial) | Yes | No | Hours | With only an intercept it equals S1. It adds intervals that respect count noise. It treats VIIRS as exact, though two VIIRS satellites differ by ±15–20% in a month. Later test of its intervals: a negative binomial interval with one dispersion covered the true value in 94–100% of held-out months of 10 or more predicted hotspots, but was about twice as wide as needed in large months. |
| S4 | Share model (binomial or beta-binomial) | Yes | No | A day | Fisheries paired-tow practice. Keeps zero-MODIS months in the fit. Assumes simultaneous pairs, which a month of passes at different hours is not. Later test: the binomial is rejected everywhere. A beta-binomial fits much better (overdispersion about 0.06), which means the kept share varies by about ±43% from month to month, and its intervals covered the true count 72–79% of the time for a nominal 90%. |
| S5 | Hurdle model: whether MODIS records anything, then how much | Yes | No | A day | States how often a converted month would read zero at a given area size. Restores nothing. Not tested as a hurdle model. A related beta-binomial table says a MODIS month with no hotspots is consistent with up to 6 Suomi NPP hotspots at 50 km and 17 at 100 km (90th percentile), and held out at 92% and 90% coverage. |
| S6 | Fitted curve (power, quadratic, sigmoid) | Yes | Yes | Hours | Used for night-time lights. The team's data reject it: slopes are near 1 and a power law did not beat one factor. A fire study of another sensor pair found the same. |
| S7 | Symmetric regression (major axis, Deming) | Yes | No | Hours | Answers "what is the true relationship", not "what would the other sensor have counted". For prediction, a ratio is the appropriate tool. |
| S8 | Quantile or distribution mapping | Large areas | Yes | A day | Standard in climate records. Needs more than ten calibration years; the team has about 70 fire-season overlap months. Every zero maps to one value. A 2025 vegetation record rejected it for reducing variability. |
| S9 | Detection-limit model: sum VIIRS into 1 km cells and keep those above MODIS's detection limit | Approx. | Yes | Hours to a day | Published limits (Sofiev and Kouznetsov 2026) give a physical reason for the day and night ratios. Validated only on fire radiative power totals, never on counts. A route to a MODIS-equivalent record after MODIS ends. Later test on counts: the published formula did no better than one factor, and a fitted detection curve was worse over all 117 months (median error 0.37 against 0.30). The power at which Aqua detects half the time is not a fixed property: about 12 MW in a single 1 km cell, 55–70 MW using the surrounding 3 km by 3 km, and 8–47 MW between years by day. |
| S10 | Pair near-simultaneous detections by footprint | Approx. | Yes | A day | Used by Fu et al. 2020 and Zheng et al. 2026. Needs footprints and timing finer than FIRMS rows give. Authors say coefficients do not transfer to Terra. |
| S11 | Extend the size distribution below the detection limit | Yes | Yes | Hours | Corrects fire radiative power totals in savanna systems. Cannot fill months with no MODIS detection. |
| S12 | Tree-based models with covariates | Yes | Yes | A day | Ten independent seasons cannot support several covariates, and record fire months lie outside the training range. |
| S13 | Image translation and spatiotemporal fusion (context) | No | Yes | Days | Need dense paired images. |
| S14 | Calibration from radiances or reference imagery (context) | No | Yes | Days | Need radiances, stable targets or coincident fine imagery. Wildfire has no invariant sites. |
| X1 | Common completeness threshold: count only hotspots above a fire radiative power at which both sensors detect nearly everything | Yes | No | Hours | Added by the reconciliation pass, from seismology (earthquake counts compared above a "magnitude of completeness" across network upgrades). Discards half or more of the VIIRS hotspots and inherits the noise of fire radiative power at night. Later test: by day, for 1 km cells, a 20 MW threshold raises the ratio from 0.43 to 0.69 and steadies it across years (coefficient of variation 0.13 to 0.09), but half of Suomi NPP's cells are discarded and single-month error does not improve. At night it helps in large months and leaves too few records in most others. |

### Correcting the sampling: time of day, number of looks, cloud

Detail: [t05](harmonization-methods-research/t05-sampling-corrections.md), [t02](harmonization-methods-research/t02-long-term-record-continuity.md).

| ID | Method | Rows | Fire | Effort | What the review found |
|---|---|---|---|---|---|
| T1 | Weight counts by a published daily fire curve | Yes | Yes | Hours | A 2026 curve for North American forest reproduces Terra's daytime decline in 2022–2024 almost exactly and over-corrects 2025–2026. Later test: the over-correction is 26% and 37% in 2025 and 2026 (measured divided by predicted 1.26 and 1.37), and the curve wrongly predicts a gain for Aqua by day. A curve with the published width but a free peak fits at 13.4 h (12.7–13.8) against the published 14.57 h. See [Where the reviewers disagreed](#where-the-reviewers-disagreed). |
| T2 | Daily curve from the team's own detection times | Yes | No | Hours to a day | Samples only about four local times a day. |
| T3 | Geostationary or model-based drift correction (context) | No | Yes | Days | Needs hourly geostationary fire data. A later check found GOES-West fire data reachable, but its pixels over the box are about 2.3 by 4.2 km and it saw 14–30 fire pixels at about 20:00 UTC on 23 July 2024, a day when NOAA-20 recorded 905 hotspots; days of work. An earlier sensor's orbit drift of about five hours caused "a ∼90% decline in the number of observed fires" (Weber and Wunderle 2019, abstract only). |
| T4 | Flag or exclude drifted sensor-years | Yes | Yes | Hours | In a critique of a long burned-area record from drifting satellites, [Giglio and Roy 2024](https://doi.org/10.1038/s41467-024-46168-0) found that geometric corrections "often merely shifted the problems". GFED5 stops in 2022 because of the MODIS drift. VIIRS covers every drift year. Later test: only Terra by day has a clear drift arc (about 0.50 of normal in 2026); for Aqua by day, Aqua at night and Terra's evening pass the data support flagging only. |
| T5 | Monthly totals keyed by local date | Yes | Yes | Hours | Measured: keying by UTC moved 455 Terra hotspots across a month boundary. |
| T6 | Normalise by observation opportunity and cloud (context) | No | Yes | A day or more | Needs the count of all pixels observed and cloud fractions. The published cloud correction tends to over-correct. |
| T7 | Reconstruct every overpass from granule metadata or swath outlines | No | Yes | A day or more | The only source found for passes that saw nothing. Later test: NASA's open granule catalogue lists every scene over the box (124,636 for the five sensors, no login) and gives a per-day flag. It sees half-day losses but not a loss inside a scene, and its near-real-time part keeps only about 7 days. |
| T8 | Count distinct passes with detections as a coverage stand-in | Yes | No | Hours | Usable as an availability flag over a large area. Cannot tell a quiet month from a missed pass. |

### Combining sensors that fly together

Detail: [t08](harmonization-methods-research/t08-fire-fusion-products.md), [t07](harmonization-methods-research/t07-data-fusion-theory.md).

| ID | Method | Rows | Fire | Effort | What the review found |
|---|---|---|---|---|---|
| C1 | Scale each satellite, average those with data each day, sum over the month | Yes | Yes | Hours | GFED5NRT and GBBEPx precedent. Measured: within 1% of a complete month in the median. The best-supported choice in the evidence. Later test: the per-day flag it needs can be built from the granule catalogue. Unlisted Suomi NPP outage days had lowered its fire-season 2024 ratio to NOAA-20 from 0.985 to 0.881. Applied day by day, the flag keeps the combined series level through every real outage month and at each change in the number of satellites. |
| C2 | One reference satellite, others as fallback | Yes | Yes | Hours | INPE's rule. Its 2002 change of reference "caused the discontinuity" in its series. Suomi NPP, the natural VIIRS reference, has ended. |
| C3 | Inverse-variance weighting | Yes | No | Hours | Reduces to nearly equal weights. Supplies the theory behind C1. |
| C4 | Union or voting | Yes | No | Hours | Stable only with a fixed set of sensors. Measured steps of 1.24 and 1.37 times. |
| C5 | Priority switch: preferred sensor, else a rescaled second | Yes | Yes | Hours | Used in fire radiative power fusion. After 2012 it reduces to "use VIIRS". |
| C6 | Regression from one satellite to the full set | Yes | Yes | Hours | GFAS and GFED5 treat the Terra-only years (2000–2002) this way. Later test on counts: a Terra to Terra-plus-Aqua factor of 1.90 fits well on 2003–2011, but 2001 and 2002 sit at or below the edge of the range expected from BC area burned. |
| C7 | Capture-recapture on cell-days | Yes | No | Hours to a day | Estimates how much even VIIRS misses. Biased low for identical instruments. Not run on the data; the later source check found that the unseen count cannot be identified, so only lower bounds exist. |
| C8 | Error estimation without a truth reference (context) | No | Yes | Days | See the fusion section above. |
| C9 | Operational gridded fusion (context) | No | Yes | Days | See the fusion section above. |

### Joining the record in time

Detail: [t11](harmonization-methods-research/t11-latent-state-and-splicing.md), [t02](harmonization-methods-research/t02-long-term-record-continuity.md).

| ID | Method | Rows | Fire | Effort | What the review found |
|---|---|---|---|---|---|
| J1 | Chain-link through an intermediate sensor over a long overlap | Yes | No | Hours | The ocean-colour climate record linked VIIRS to an older sensor through MODIS. Here NOAA-21 never overlaps stable-orbit MODIS, so it links through Suomi NPP. Linking on a single month would carry the monthly scatter into the whole series. Later test: the MODIS factor fitted directly against NOAA-20 is 0.242 (0.234–0.269) and chained through Suomi NPP 0.246, but the two share their months, so they are not independent confirmation. |
| J2 | Keep a documented seam: separate records | Yes | Yes | Hours | Advised for night-time lights and for MODIS and VIIRS burned area at local scale. On its own it does not give history "from the early 2000s". |
| J3 | One count model with a shared monthly activity level and a factor per sensor | Yes | No | Hours to a day | The approach used for wildlife counts from several sources. Uses zero months properly and all overlaps at once. Its intervals are too narrow, because the VIIRS satellites share errors. |
| J4 | State-space model with a factor that shifts or drifts | Yes | No | A day or more | Used when labour-force surveys are redesigned. The only method that could keep drift-period Terra by estimating its decline against VIIRS. Not tested as a model. The nearest later tests are control charts, which flagged Terra's daytime loss early, and a fitted daily curve (see T1). |
| J5 | Dynamic factor model with missing data | Yes | No | Hours | Not recommended by its own topic file: it assumes Gaussian, stationary series. |
| J6 | Choose the reference by stability | Yes | Yes | Hours | Climate records anchor to the sensor with the most stable sampling, not the newest. VIIRS times have not moved; MODIS times have moved two hours. NASA's QFED is moving its anchor to NOAA-20. |
| J7 | Same algorithm on both sensors, then regional calibration (context) | No | Yes | Days | How NASA joined MODIS and VIIRS burned area. Boreal North America: VIIRS 10% higher. |

### Expressing the result

Detail: [t12](harmonization-methods-research/t12-anomaly-indices-and-dashboards.md).

| ID | Method | Rows | Fire | Effort | What the review found |
|---|---|---|---|---|---|
| E1 | Standardised anomaly against the same sensor's history | Yes | Yes | Hours | Global Forest Watch practice: VIIRS from 2012 and MODIS from 2001, never mixed. Skewed counts inflate the spread, and its code labels a month "normal" when the baseline never varies. |
| E2 | Mean with a minimum-to-maximum band, or percent from the mean | Yes | Yes | Hours | How the European system and INPE present current activity. Dominated here by 2017, 2018 and 2021. |
| E3 | Ratio to the calendar-month median | Yes | No | Hours | Matches the challenge wording. Undefined below about 100 km, where the MODIS median is zero for most months. Later test: a converted baseline can class 17% of fire-season circle-months at 25 km, 55% at 50 km and 99.9% at 100 km. Converted fire-season calendar-month medians run about 23% above the actual Suomi NPP medians. |
| E4 | Percentile rank | Yes | No | Hours | Robust to skew. Coarse with 10–14 years, and zeros tie. |
| E5 | Fitted standardised index, as in drought monitoring | Yes | No | A day | Guidance asks for 20–30 years and no more than about a third zeros. |
| E6 | Rescale to a reference, then compute anomalies | Yes | No | Hours to a day | What multi-sensor climate records do. The only route in this group to one baseline before 2012. |
| E7 | Fixed reference period with frozen parameters | Yes | Yes | Hours | Makes a month's label reproducible. Measured: changing the baseline years changes 8–21% of labels. |
| X2 | Shrink a small area's value toward its enclosing region, in proportion to how little data it has | Yes | Yes | Hours | Added by the reconciliation pass, from disease mapping and small-area statistics; applied to forest-fire counts in Galicia. It would replace hard area cut-offs with a continuous weight. Not applied anywhere to cross-sensor harmonization. Later test: shrinking a circle toward the whole box lowered agreement at every radius, but that test cannot reward it, because the answer is defined on the very count being classed. Untested in a fair form. |

### Validating whatever is built

Detail: [t10](harmonization-methods-research/t10-homogenization-and-validation.md).

| ID | Method | Effort | What it does |
|---|---|---|---|
| V1 | Cross-validation by whole years | Hours | Scores each factor on fire seasons it was not fitted on, against the plain ratio and against the ±15–20% floor between two VIIRS satellites. Random hold-outs give "serious underestimation of predictive error". |
| V2 | Stability as the trend of the difference between sensors | Hours | The standard climate-record measure. The team's Terra-against-NOAA-20 table already is one. Later test: double-mass curves are straight through the stable years (slope 0.242 against Suomi NPP); the only clear later bend is Terra by day against NOAA-20. |
| V3 | Step tests at known dates | Hours | Tests for a break at April 2018, January 2022 and March 2023, and attributes it by which sensor pairs break. Later test: with whole years as the unit, only steps of about 20% between the VIIRS satellites, or 30–50% for MODIS series, are detectable; no step was significant. |
| V4 | Prediction intervals and class probabilities | Hours to a day | Combines factor, monthly and count uncertainty for each converted month. One factor applied to every year "induces correlation", so its error does not average out. |
| V5 | Fusion vocabulary | Writing only | Frames the write-up in standard sensor-fusion terms. |

## What the later tests found

Detail: [harmonization-tests.md](harmonization-tests.md) and its verdict table, and [_cross-check.md](harmonization-tests-research/_cross-check.md). All tests used the team's own FIRMS data for the box 49.0–52.5°N, 122.5–118.0°W. "Class" means the five-class label of a month against the calendar-month median. Methods without a catalogue ID are marked "none". Catalogue methods not listed here, including J4 and C7, were not run as models; see their rows above.

| ID | Method | What the tests found | Working file |
|---|---|---|---|
| U1 | Active cell-days | Over the ten stable years, 2 km daytime cell-days gain as much over their own short baseline as counts do, and neither win nor lose at box scale. The ratio is 0.654 for the union of Terra and Aqua and 0.74 with each sensor and pass counted separately, in fire-season months. | [a01](harmonization-tests-research/a01-hindcast-box.md), [a07](harmonization-tests-research/a07-box-counting.md) |
| S1 | One multiplicative factor | Scaled-up MODIS years give the all-VIIRS class in 84% of fire-season months against 66% for a short VIIRS-only baseline (gain 18 points, 14 to 23); fitted directly against NOAA-20 the factor is 0.242 (0.234–0.269). It runs about 15% high in a typical fire-season month and 27% high for a small season, and about a third low in a typical November-to-March month (0.66 times actual, 0.54–0.79). On the real 24-year baseline, 39% of box fire-season labels differ from a VIIRS-only baseline, against about 22% from the change of length alone. | [a01](harmonization-tests-research/a01-hindcast-box.md), [a04](harmonization-tests-research/a04-factor-stability.md), [f01](harmonization-tests-research/f01-real-length-baseline.md), [f02](harmonization-tests-research/f02-factor-refinements.md) |
| S2 | Factor split by day and night | Level with one factor in the fire season (83% against 84%) and 7 points worse over all months (73% against 80%), because the night factor is seasonal; the day factor fell 23% and the night factor rose 46% between the two halves of the decade. A seasonal night factor is still 4.7 points worse over all months (−7.3 to −2.6). Day and night factors used only in April to October are level with one factor over all months (−1.3, −2.9 to +0.4) and remove its fire-season bias, though losses of 5 to 9 points are not excluded in the box. | [a01](harmonization-tests-research/a01-hindcast-box.md), [a04](harmonization-tests-research/a04-factor-stability.md), [f02](harmonization-tests-research/f02-factor-refinements.md) |
| S6 | Fitted curve, as a size-dependent factor | A log-scale curve between monthly MODIS and Suomi NPP counts, inverted so the month's MODIS count sets the factor, was no better than one factor (−1.7 points in the box fire season, −2.0 in 100 km circles) and runs higher in a typical fire-season month (1.27 against 1.14). | [f02](harmonization-tests-research/f02-factor-refinements.md) |
| S3 | Count regression, intervals | A negative binomial interval with one dispersion covered the true value in 94–100% of held-out months of 10 or more predicted hotspots, but was about twice as wide as needed in large months and covered only 45% under 10 hotspots. | [a04](harmonization-tests-research/a04-factor-stability.md) |
| S4, S5 | Share model; hurdle model | The binomial share model is rejected. A beta-binomial with overdispersion about 0.06 fits, but its intervals covered 72–79% for a nominal 90%. Its zero table (a MODIS-zero month is consistent with up to 6 Suomi NPP hotspots at 50 km and 17 at 100 km) held out at 90–92%. A hurdle model was not fitted. | [a03](harmonization-tests-research/a03-thinning-model.md) |
| S9 | Detection-limit model | The published formula did no better than one factor; a fitted detection curve was worse over all months (median error 0.37 against 0.30). The 50% detection power is not fixed: about 12 MW, 55–70 MW or 8–47 MW depending on how it is measured. | [a08](harmonization-tests-research/a08-completeness.md) |
| X1 | Common completeness threshold | By day a 20 MW threshold raises the 1 km cell ratio from 0.43 to 0.69 and steadies it across years, but discards half of Suomi NPP's cells and does not cut single-month error. | [a08](harmonization-tests-research/a08-completeness.md) |
| X2 | Shrinkage toward the region | Lowered agreement at every radius, but the test cannot reward it because the answer is defined on the classed count. Untested in a fair form. | [a02](harmonization-tests-research/a02-hindcast-circles.md) |
| T1 | Published daily fire curve | Over-corrects Terra by day by 26% and 37% in 2025 and 2026, and wrongly predicts a gain for Aqua. A curve with a free peak fits at 13.4 h (12.7–13.8) against the published 14.57 h and predicts 2025 and 2026 within 3–4%, but the 2026 interval is 0.69–1.72 and rests on one decisive year. | [a09](harmonization-tests-research/a09-drift-curve.md) |
| T4 | Flag drifted sensor-years | Only Terra by day has a clear drift arc (about 0.50 of normal in 2026, 0.41–0.61 across five methods); for the other three MODIS passes the data support flagging only. BC's provisional 2026 records confirm the Terra loss. | [a09](harmonization-tests-research/a09-drift-curve.md), [w03](harmonization-tests-research/w03-data-availability.md) |
| C1 | Daily mean of satellites with data | The per-day availability flag it needs can be built from NASA's open granule catalogue. Unlisted Suomi NPP outage days had lowered the fire-season 2024 ratio to NOAA-20 from 0.985 to 0.881. The flag sees half-day losses but not a loss inside a scene, and the current month may lack one. Applied day by day, it keeps the combined series level through every real outage month (a plain monthly mean is 34% and 28% low in July and August 2022), and the masked scale factors to Suomi NPP are 1.0245 for NOAA-20 and 1.0503 for NOAA-21. A NOAA-20 current month changes about one fire-season box label in seven against Suomi NPP's own. | [w03](harmonization-tests-research/w03-data-availability.md), [_cross-check.md](harmonization-tests-research/_cross-check.md), [f03](harmonization-tests-research/f03-availability-flag.md) |
| C7 | Capture-recapture on cell-days | Not run. The source check found the unseen count cannot be identified, so only lower bounds exist, and the three VIIRS satellites are not independent lists. | [w02](harmonization-tests-research/w02-crossfield-sources-b.md) |
| J4 | State-space model with a drifting factor | Not run. Control charts, the nearest tool tested, flagged Terra's daytime loss in September 2025 (CUSUM) and July 2026 (EWMA and single month); a chart on the all-hours total never signalled. | [a10](harmonization-tests-research/a10-diagnostics.md) |
| E1 | Anomaly against the same sensor's history | Each sensor's own-history five-class label agrees with the other sensor's in 68% of 68 fire-season months (59–76), against 71% in the first compilation; three coarse classes agree in 79%. | [a11](harmonization-tests-research/a11-latent-models.md), [_cross-check.md](harmonization-tests-research/_cross-check.md) |
| E3 | Ratio to the calendar-month median | A converted baseline can class 17% of fire-season circle-months at 25 km, 55% at 50 km and 99.9% at 100 km. Converted fire-season calendar-month medians run about 23% above the actual Suomi NPP medians. | [a02](harmonization-tests-research/a02-hindcast-circles.md), [a04](harmonization-tests-research/a04-factor-stability.md) |
| V1 | Cross-validation by whole years | Used for all class tests (202 splits of the ten years). The splits reuse the same years, so their spread understates uncertainty; with ten calibration seasons, delivered interval coverage itself varies (SD about 0.11 at 80%). | [a01](harmonization-tests-research/a01-hindcast-box.md), [w02](harmonization-tests-research/w02-crossfield-sources-b.md) |
| V2 | Stability as a trend | The all-hours factor is steady at a fixed day and night mix (0.243 in 2012–2016, 0.240 in 2017–2021). Double-mass curves are straight through the stable years; the only clear bend is Terra by day against NOAA-20, from 0.140 to about 0.07. | [a04](harmonization-tests-research/a04-factor-stability.md), [a10](harmonization-tests-research/a10-diagnostics.md) |
| V3 | Step tests at known dates | No step was significant at April 2018, January 2022 or March 2023. Suomi NPP against NOAA-20 shows +0.3% (−7 to +8) at March 2023. With whole years as the unit, only steps of about 20% between the VIIRS satellites, or 30–50% for MODIS series, are detectable. | [a04](harmonization-tests-research/a04-factor-stability.md) |
| V4 | Prediction intervals and class probabilities | Intervals from held-out-year errors, grouped by predicted count, covered 90–92% for 10 or more predicted hotspots; none is honest under 10 (55%). They leave out the factor's shared error across years. Class probabilities were not tested. | [a04](harmonization-tests-research/a04-factor-stability.md) |
| none | Thinning (keep each VIIRS hotspot with the measured MODIS-to-VIIRS ratio, by expectation or at random) | By expectation it gives the same class as scaling up in 11,705 of 11,706 cases. Random thinning is 2 points worse with a binomial draw and 9–12 points worse with a beta-binomial draw, and classes fewer small-area months. Random loss of hotspots explains 15% of the monthly variance (10–25) and thinning whole fire-days 40% (29–61). | [a01](harmonization-tests-research/a01-hindcast-box.md), [a02](harmonization-tests-research/a02-hindcast-circles.md), [a03](harmonization-tests-research/a03-thinning-model.md) |
| none | Box counting and the pixel and sensitivity split | The factor splits exactly into a pixel-size part (2.56 Suomi NPP hotspots per occupied 1 km cell) and a remaining part (0.62 MODIS hotspots per such cell), which carries about two thirds of the day-to-night difference. No cell-based link beat the plain ratio of counts. | [a07](harmonization-tests-research/a07-box-counting.md) |

## What combines and what excludes

**Pick one from each group:**

| Decision | Alternatives |
|---|---|
| Rule for combining VIIRS satellites | C1 daily mean; C2 single reference; C4 union. C3 justifies C1. |
| Form of the MODIS-to-VIIRS conversion | S1 ratio; S3 count regression; S6 curve; S7 symmetric line; S8 quantile mapping; S12 trees. S2 sits on top of S1 or S3. J3 replaces S3 and J1 with one model. |
| Treatment of MODIS since 2022 | T4 flag or exclude; T1 daily-curve weighting; J4 time-varying factor. |
| Route to a baseline before 2012 | Per-sensor anomalies (E1, E4) with no conversion; or conversion to one record (the S group with E6). The two can be run together as a cross-check. J2, a seam, rules out a single baseline. |
| Direction | Downward to MODIS-equivalent (S1, S9); upward to VIIRS-equivalent (S1, S11). |

**Dependencies:**

- An additive source, such as the Kamloops static site, has to be removed before any multiplicative factor.
- Any new unit (U1, U3, U4) has to be built per satellite and combined by C1. Pooling or taking a union creates steps at 2018 and 2023.
- C1 needs a per-day availability flag (T7, or T8 over a large area).
- Factors have to be fitted on the stable-orbit years and on a large area, not on the user's circle.
- Local-date months (T5) and the validation methods apply to everything.

## Five combinations the literature and the evidence would support

These run from simplest to most elaborate. They are options with trade-offs, not a ranking. The target record can be chosen independently in B to E.

| | Pieces | What it claims | What it leaves unsolved | Effort |
|---|---|---|---|---|
| **A. Per-sensor anomalies, no conversion** | T5, C1, E1 or E4 per sensor, E7, T4 | Each month is judged only against the same sensor's history, as Global Forest Watch does. Month order agrees across sensors (rank correlation 0.97). | A current VIIRS month has VIIRS history only from 2012. Linking it to 2000–2011 assumes anomalies do not depend on the sensor, which the data support only in part (68–69% class agreement in fire-season months, 71% in the first compilation; 44% near normal on the first definition). No published precedent for that link. | Hours |
| **B. One overlap factor, joined through Suomi NPP** | Remove the static source; T5; C1; S1 with S2; J1; C6 for 2000–2002; T4; J6; E3 or E4 on one baseline; V1, V2 | The GFED3 and ocean-colour design applied to counts. The relation is proportional. About 10% error on a season. No step at 2018, 2023 or November 2026. | Single-month error of 14–30%. Months MODIS missed at small areas. Quiet months run 25–50% above busy ones. | Hours; mostly measured |
| **C. B with stated uncertainty** | B, with S3 or J3 in place of the plain ratio; S5 by area size; V3; V4 | Each converted month carries an interval and a probability of each class. The app can say how often a converted month would read zero at the chosen radius. | Everything B leaves. Intervals too narrow where VIIRS satellites share errors. | About a day |
| **D. B or C on a unit less tied to pixel size** | B or C with U1 daytime cell-days, or U2 | The sensors move closer in level, same-pass duplicates go, and the daytime factor is steadier across years. | A modest single-month gain. Night cells swing eightfold. Large months are compressed. Not literally "number of hotspots". | Hours on top of B |
| **E. B or C with a physical model** | C, plus T1 or J4 to keep drift-period Terra; S9 as a physical check on the factors | The factors and the Terra decline are explained by detection limits and overpass time, not only fitted. | The daily curve over-corrects 2025–2026. The detection model is validated only on fire radiative power. J4 needs custom code. | A day for the checks; days for J4 |

**What the tests showed for each combination's central claim.** This is a report of results, not a ranking. Sources are the working files linked in [What the later tests found](#what-the-later-tests-found).

- **A.** The claim that months can be judged against the same sensor's history rests on agreement between sensors. In the 68 fire-season months of the stable years, each sensor's own-history five-class label matched the other's in 68% (59–76); three coarse classes matched in 79%. Agreement rates across schemes with different numbers of classes are not comparable. The rank correlation of 0.97 was not recomputed on the later definitions ([a11](harmonization-tests-research/a11-latent-models.md)).
- **B.** The claim of a proportional relation with no step held on the data tested: the factor fitted directly against NOAA-20 is 0.242, the all-hours factor is steady at a fixed day and night mix, and no step was significant at April 2018, January 2022 or March 2023, though steps under about 20% (VIIRS pair) or 30–50% (MODIS series) could not be detected. Scaled-up MODIS years gave the all-VIIRS class in 84% of fire-season months, and a single converted month in 69% (61–77) with a median error of 33%. The factor runs about 15–27% high in quiet fire-season months and small seasons, and about a third low in typical November-to-March months. On the real 24-year baseline, 39% of box fire-season labels differ from a VIIRS-only baseline, against about 22% from the change of length alone, and the data cannot tell real pre-2012 burning from a conversion level that is too high ([a01](harmonization-tests-research/a01-hindcast-box.md), [a04](harmonization-tests-research/a04-factor-stability.md), [f01](harmonization-tests-research/f01-real-length-baseline.md), [f02](harmonization-tests-research/f02-factor-refinements.md)).
- **C.** The claim of an honest interval for each converted month held for months of 10 or more predicted hotspots (coverage 90–92%) and failed below that (55%). Beta-binomial intervals covered 72–79% for a nominal 90%. The zero table held out at 90–92%. Class probabilities were not tested ([a04](harmonization-tests-research/a04-factor-stability.md), [a03](harmonization-tests-research/a03-thinning-model.md)).
- **D.** The claim that a unit less tied to pixel size helps: daytime 2 km cell-days gain as much over their own short baseline as counts do, and neither win nor lose at box scale; no cell-based link beat the plain ratio in leave-one-year-out prediction ([a01](harmonization-tests-research/a01-hindcast-box.md), [a07](harmonization-tests-research/a07-box-counting.md)).
- **E.** The claim that physical models explain the drift and the factors: the published daily curve over-corrects Terra by day by 26% and 37% in 2025 and 2026, while a curve with a free peak at 13.4 h fits Terra by day with a wide 2026 interval (0.69–1.72) and one decisive year. The published detection-limit formula did no better than one factor on counts. J4 was not run ([a09](harmonization-tests-research/a09-drift-curve.md), [a08](harmonization-tests-research/a08-completeness.md)).

## What other fields did with the same problem

| Field | Their problem | What they did | Lesson stated |
|---|---|---|---|
| Night-time lights ([t01](harmonization-methods-research/t01-nighttime-lights.md)) | An old, coarse, less sensitive sensor (1992–2013) and VIIRS (from 2012), with a one-to-two-year overlap | Mostly degraded VIIRS to look like the old sensor, then calibrated over the overlap | Degrading to the old sensor re-imports its artefacts. One critique found that a harmonized product largely undid the gains of the new sensor. |
| Ocean colour and soil moisture climate records ([t02](harmonization-methods-research/t02-long-term-record-continuity.md)) | Several sensors of different sensitivity over decades | Corrected every sensor to one reference over a gap-free window; weighted sensors equally; matched distributions onto the most stable sensor | Matching distributions "can change" the size of a trend. |
| Vegetation records ([t02](harmonization-methods-research/t02-long-term-record-continuity.md)) | A change of sensor, and orbit drift on older satellites | Translation equations between sensors, fitted by land cover; drift corrections tested on simulated drift | Translation equations differ by land cover. |
| Fire: GFED, burned area, INPE ([t03](harmonization-methods-research/t03-fire-record-transitions.md)) | A change of fire sensor, and orbit drift | Regional overlap factors (GFED3); same algorithm on both sensors plus calibration (burned area); one reference satellite (INPE); flagging drifted years | Joining does not restore what the weaker sensor missed. Corrections for drift "often merely shifted the problems". INPE says VIIRS detects "about ten times more" fire pixels than MODIS nationally and that it will "adjust carefully"; it gives no method. |
| Fisheries surveys ([t09](harmonization-methods-research/t09-count-calibration-statistics.md)) | A change of survey vessel or net | Paired tows; conversion factors by size class and time of day, with a share model | Day and night effects mattered for nine of ten species. Applying one factor to every year "induces correlation" in the converted series, so its error does not average out. |
| Seismology and lightning ([_reconcile](harmonization-methods-research/_reconcile.md)) | Event counts across network upgrades | Count only events above the size at which detection is complete, or divide by detection efficiency | Correction reduces an artificial trend but does not fully remove it. |
| Labour-force surveys ([t11](harmonization-methods-research/t11-latent-state-and-splicing.md)) | A survey redesign mid-series | A state-space model with a level shift at the redesign | The shift can be estimated from a parallel run of old and new designs, from the series itself, or from both. |

## Where the reviewers disagreed

The topic files agree on what the sources say. They differ on fit.

**Correcting the Terra drift with a published daily fire curve.** One topic rated it feasible in hours; three rated it days of work and context only. The reconciliation pass recomputed the prediction of the published curve ([Gui et al. 2026](https://doi.org/10.3390/rs18010052)) against the team's measured Terra daytime level:

| Year | Median Terra daytime pass | Predicted by the curve | Measured | Measured ÷ predicted |
|---|---|---|---|---|
| 2022 | 11:04 | 0.96 | 0.95 | 0.99 |
| 2023 | 10:44 | 0.82 | 0.81 | 0.99 |
| 2024 | 10:32 | 0.74 | 0.77 | 1.04 |
| 2025 | 10:04 | 0.58 | 0.70 | 1.21 |
| 2026 | 09:20 | 0.37 | 0.46 | 1.25 |

Each side is half right. The curve gets 2022–2024 almost exactly. It over-corrects 2025 and 2026 by 21–25% in this first computation. The later test used a different size model and VIIRS reference and found 26% and 37% (measured divided by predicted 1.26 and 1.37, with prediction intervals 0.59–2.45 and 0.92–1.97), so the size of the over-correction is uncertain within roughly a factor of 2 ([a09](harmonization-tests-research/a09-drift-curve.md), [_cross-check.md](harmonization-tests-research/_cross-check.md)). The same test fitted the peak freely and found 13.4 h (12.7–13.8) against the published 14.57 h. The result depends heavily on which published curve is used: a narrower curve from another study would predict about 1% where 46% was measured. The curve describes fire radiative power over a continent, not counts in Interior BC. A third option, measuring the drift factor directly against NOAA-20, needs no curve but is fitted on the years it corrects.

**Other differences.**

| Method | The difference | Better supported |
|---|---|---|
| Symmetric regression | "Defensible because both counts are noisy" against "not applicable to prediction" | Not applicable. The slopes are near 1, so the choice of line hardly matters. |
| Kalman or state-space models | "Gaussian assumptions fail; days" against "a count model in hours" | Both, about different models. The quick one is a count regression, not a Kalman filter. |
| Quantile mapping | Rated low by three topics, medium by two | Low. The team's test that a curve did not beat one factor is its count analogue. |
| Day and night split | "Clearly needed" in three topics | The qualified version in the evidence: the literature explains why day and night differ, but does not show that splitting improves a monthly total. |
| Fire events as a unit | "Applicable with care" against "not applicable" | Applicable, if built per satellite. |

## Corrections to the working files

The reconciliation pass found five errors of description. The working files are kept as written; read them with these corrections.

| File | As written | Correct |
|---|---|---|
| t13 | GFED5NRT is a "priority fusion" | It averages the satellites, with a fallback when one is missing. |
| t04 | Terra is "less sensitive" than Aqua | They carry the same instrument. Terra's lower daytime yield comes from its earlier overpass. |
| t04 | Summed VIIRS fire radiative power was 0.72 of MODIS (Fu et al. 2020) | 0.72 is the slope of a fitted line, not a ratio of sums. |
| t03 | A factor of 1.35 for boreal North America in GFED3 | Correct, but it is the factor for the ATSR sensor. |
| t01 | One critique's 77% figure applied to three methods | It was measured for one product, the deep-learning one. |

## What is still missing

Items marked "Answered" were tested after this catalogue was first compiled; the answer and a link follow. Items marked "Open" remain.

1. **Open, partly addressed.** A daily cycle of fire detections for western Canada from geostationary data. It would settle the disagreement over drift correction. A cycle fitted to the team's own data peaks at 13.4 h (12.7–13.8) against the published 14.57 h, but no independent daily cycle has been used to check it. GOES-West data are reachable and are days of work. No published count-based cycle for Canadian forest was found. See [harmonization-tests.md](harmonization-tests.md#the-orbit-drift) and [New data found](harmonization-tests.md#new-data-found).
2. **Open.** Any peer-reviewed measurement of the effect of the 2022–2026 drift on MODIS fire counts. The team's own table is still the only count measurement found. BC's provisional 2026 fire records now confirm the 2026 Terra daytime loss independently (yield 0.41–0.45 of the 2021 and 2023 levels). See [harmonization-tests.md](harmonization-tests.md#the-orbit-drift).
3. **Answered.** A count-level test of the detection-limit model (S9) and of a common completeness threshold (X1). The published formula did no better than one factor and a fitted detection curve was worse (error 0.37 against 0.30); a threshold steadied daytime cell ratios but discarded half of Suomi NPP's cells and did not cut single-month error. See [harmonization-tests.md](harmonization-tests.md#approaches-borrowed-from-other-fields).
4. **Partly answered.** A cross-sensor test of active cells, fire events or per-sensor anomalies. The team tested cell-days (no gain or loss at box scale) and own-history classes (68% agreement) on its own data; the literature still has none, and fire events were not tested. See [harmonization-tests.md](harmonization-tests.md#does-a-converted-record-give-the-right-class).
5. **Open.** An independent third reference for both sensors in Interior BC. Sentinel-3 fire radiative power needs an account and Landsat 8 and 9 active fire is usable only as a spot check, both later; BC's provisional 2026 area burned served as an independent check for Terra only. See [harmonization-tests.md](harmonization-tests.md#new-data-found).
6. **Answered.** How much monthly scatter random thinning alone produces: 15% of the variance in the box (10–25) when single hotspots are lost at random, 22–28% in 50 and 100 km circles, and 40% (29–61) when whole fire-days are lost. About a fifth of the scatter is irreducible by any factor. See [harmonization-tests.md](harmonization-tests.md#how-much-of-the-scatter-can-any-method-remove).
7. **Answered, with limits.** The contents of the granule metadata as a source for a per-day availability flag. NASA's open granule catalogue lists every scene over the box and gives the flag; it sees half-day losses but not a loss inside a scene, and keeps near-real-time scenes for about 7 days. A follow-up applied it day by day ([f03](harmonization-tests-research/f03-availability-flag.md)). FIRMS swath outlines are a map layer only, with no download. See [harmonization-tests.md](harmonization-tests.md#new-data-found).
8. **Answered.** The precision of FIRMS acquisition times: whole minutes, and apparently the time of the pixel, not of the scene. See [harmonization-tests.md](harmonization-tests.md#new-data-found).
9. **Open.** Event thresholds tuned for Interior BC.

## Changes since first compiled

Each change was made in place above, on 2026-11-14, from the later tests in [harmonization-tests.md](harmonization-tests.md) and its working files in [harmonization-tests-research/](harmonization-tests-research/).

| Date | Statement | First compilation | Now | Source |
|---|---|---|---|---|
| 2026-11-14 | Over-correction of Terra by day by the published daily curve ("At a glance", T1, "Where the reviewers disagreed") | 21–25% in 2025–2026 | 26% and 37% in 2025 and 2026 in the later test, which used a different size model and VIIRS reference. The size is uncertain within roughly a factor of 2. | [a09](harmonization-tests-research/a09-drift-curve.md), [_cross-check.md](harmonization-tests-research/_cross-check.md) |
| 2026-11-14 | Peak of the daily fire curve | Published peak of 14.57 h used | A curve with the published width and a free peak fits at 13.4 h (12.7–13.8) | [a09](harmonization-tests-research/a09-drift-curve.md) |
| 2026-11-14 | Same five-class label from each sensor's own history (combination A) | 71% | 68–69%. The first figure included a month's own year in its baseline and keyed months by UTC date. | [a11](harmonization-tests-research/a11-latent-models.md), [_cross-check.md](harmonization-tests-research/_cross-check.md) |
| 2026-11-14 | S9 and X1 | Untested (X1); validated only on fire radiative power (S9) | Tested on counts; results in the S9 and X1 rows | [a08](harmonization-tests-research/a08-completeness.md) |
| 2026-11-14 | X1 | Discards most VIIRS hotspots | Discards half or more of the VIIRS cells by day | [a08](harmonization-tests-research/a08-completeness.md) |
| 2026-11-14 | C6 | Untested on counts | A Terra to Terra-plus-Aqua factor of 1.90 fits 2003–2011; 2001 and 2002 sit at or below the edge of the range expected from area burned | [a05](harmonization-tests-research/a05-pre2012-check.md) |
| 2026-11-14 | T7 | External download; contents not inspected | The granule catalogue was downloaded and gives a per-day flag, with limits | [w03](harmonization-tests-research/w03-data-availability.md) |
| 2026-11-14 | S2 | No gain in whole-box monthly accuracy | Added: level with one factor in the fire season and 7 points worse over all months in class terms | [a01](harmonization-tests-research/a01-hindcast-box.md) |
| 2026-11-14 | V3 | Only steps larger than about 15–20% are detectable | About 20% between the VIIRS satellites and 30–50% for MODIS series, with whole years as the unit | [a04](harmonization-tests-research/a04-factor-stability.md) |
| 2026-11-14 | "What is still missing" | Nine open items | Each item marked answered, partly answered or open, with a link | [harmonization-tests.md](harmonization-tests.md#what-is-still-missing) |
| 2026-11-14 | Bias of one factor (S1, combination B, "What the later tests found") | Runs about 15–27% high in quiet months and small seasons | High only in the fire season; a typical November-to-March month converts about a third low. Added the real-length baseline result. | [f01](harmonization-tests-research/f01-real-length-baseline.md), [f02](harmonization-tests-research/f02-factor-refinements.md) |
| 2026-11-14 | S2 and S6 | A seasonal night factor not tested; no later result for S6 | A seasonal night factor is still 4.7 points worse over all months; a fire-season-only split is level over all months; a size-dependent curve was no better than one factor | [f02](harmonization-tests-research/f02-factor-refinements.md) |
| 2026-11-14 | T7, C1 and "What is still missing" item 7 | The flag cannot see partial losses | It sees half-day losses but not a loss inside a scene. Added the flag applied day by day, the masked scale factors and the label change from a change of satellite. | [f03](harmonization-tests-research/f03-availability-flag.md) |

The 44% agreement in near-normal months quoted in combination A is from the first definition and was not recomputed.

## How this was produced

| File | Family of methods |
|---|---|
| [t01-nighttime-lights.md](harmonization-methods-research/t01-nighttime-lights.md) | Joining the old and new night-time light sensors |
| [t02-long-term-record-continuity.md](harmonization-methods-research/t02-long-term-record-continuity.md) | Continuing long-term satellite records across sensors |
| [t03-fire-record-transitions.md](harmonization-methods-research/t03-fire-record-transitions.md) | How fire records have been carried across sensor changes |
| [t04-detection-limits.md](harmonization-methods-research/t04-detection-limits.md) | Detection limits, omission and sensor emulation |
| [t05-sampling-corrections.md](harmonization-methods-research/t05-sampling-corrections.md) | Overpass time, the daily fire cycle, observation opportunity and cloud |
| [t06-fire-events-and-area-units.md](harmonization-methods-research/t06-fire-events-and-area-units.md) | Fire events, clusters and area-based units |
| [t07-data-fusion-theory.md](harmonization-methods-research/t07-data-fusion-theory.md) | Multi-sensor data fusion theory |
| [t08-fire-fusion-products.md](harmonization-methods-research/t08-fire-fusion-products.md) | Multi-sensor fusion as practised for active fire |
| [t09-count-calibration-statistics.md](harmonization-methods-research/t09-count-calibration-statistics.md) | Statistical calibration of counts when an instrument changes |
| [t10-homogenization-and-validation.md](harmonization-methods-research/t10-homogenization-and-validation.md) | Climate-record homogenization, quantile mapping and validation |
| [t11-latent-state-and-splicing.md](harmonization-methods-research/t11-latent-state-and-splicing.md) | Latent-state models and index splicing |
| [t12-anomaly-indices-and-dashboards.md](harmonization-methods-research/t12-anomaly-indices-and-dashboards.md) | Anomaly indices and existing fire dashboards |
| [t13-machine-learning-and-spatiotemporal-fusion.md](harmonization-methods-research/t13-machine-learning-and-spatiotemporal-fusion.md) | Machine learning and spatiotemporal image fusion |
| [_catalogue.md](harmonization-methods-research/_catalogue.md) | Full entry for each of the 55 catalogued methods |
| [_reconcile.md](harmonization-methods-research/_reconcile.md) | Reconciliation, citation spot-checks and the two gaps filled |

- **AI assistance.** The literature search, verification and this write-up were produced with AI agents (Claude) on 14 November 2026: 28 agents searched, verified and catalogued, and the results were aggregated into this document. The Space Apps submission guide requires that such use be acknowledged, and says AI should not be used to come up with the idea of how to solve the challenge. This document therefore lists options and their trade-offs; the choice of method is the team's.
- **AI assistance in the corrections.** The section "What the later tests found" and the corrections listed under "Changes since first compiled" were written on 14 November 2026 by AI agents (Claude), from the later tests in [harmonization-tests.md](harmonization-tests.md), which were themselves produced with AI agents. Each change was checked against a working file named in the table that reports it. A final review by an AI agent the same day carried the results of the three follow-up tests (f01 to f03) into this document. The choice of method is still the team's.
- **Sources.** The working files cite about 230 distinct links. Each topic file ends with its source list and marks what was read as an abstract only.
