# Sources for the cross-field approaches: thinning, rarefaction, inverse problems, box counting, completeness

## Answer

All five borrowed ideas have real, citable foundations, and every one fits the hotspot problem only as an analogy. The analogy breaks at the same place each time: VIIRS is not a complete or noise-free "truth", and MODIS hotspots are not a random subset of VIIRS hotspots. If each hotspot were kept at random with the measured ratio of 0.242 (binomial thinning), months with 1,000 to 10,000 VIIRS hotspots would scatter by only about 1 to 4% (median absolute error). The team measures about 14% in the largest months and about 30% over all fire-season months. Two identical VIIRS instruments also differ by ±15 to 20%. So random detection loss explains almost none of the monthly scatter. The only published limit on extrapolation found is 2 to 3 times the reference sample, and it is for species richness, not counts (Colwell et al. 2012; Chao et al. 2014). Lifting MODIS to VIIRS level is a 4.1-fold step (8.8-fold for Aqua alone, 18-fold for Aqua at night), so it falls outside even that analogous limit. No study was found that applies thinning, rarefaction, unfolding, box counting or injection-recovery to hotspot counts. The nearest fire precedents are forward mappings of fire radiative power (FRP), not of counts (Li et al. 2020; Sofiev and Kouznetsov 2026).

## Evidence

**Terms.** *Binomial thinning* keeps each of X events independently with probability p. *Rarefaction* compares samples after cutting the larger one down to a common size. *Unfolding* estimates the true distribution by inverting the detector response. *Forward folding* passes a model through the detector response and compares the result with data in observed space. *Box counting* counts the grid cells that contain at least one point, at several cell sizes. *Completeness* is the fraction of real events a detector records. *Horvitz-Thompson (HT)* estimates a total by weighting each observed unit by 1/(its inclusion probability).

| Method | Canonical source (link) | Core idea | Main assumption | Known pitfall | Use on fire or satellite data | Is the proposed mapping sound? |
|---|---|---|---|---|---|---|
| Binomial thinning; integer-valued autoregressive (INAR) models | Steutel and van Harn 1979, [doi:10.1214/aop/1176994950](https://doi.org/10.1214/aop/1176994950) (metadata only). Review: Serrao et al. 2026, [MethodsX 16:103805](https://pmc.ncbi.nlm.nih.gov/articles/PMC12876620/) | α∘X = sum of X Bernoulli(α). An independently thinned Poisson process is Poisson, so the expected kept count is pλ. | Independent retention, constant p, Poisson parent | The rate and p cannot be separated without fully reported data: the likelihood "is constant over the level curves of πλ" (Stoner et al. 2019). In INAR, α is carry-over between periods, not detection. | None found | **"Thin VIIRS at 0.242": sound as an expected value only.** Binomial noise is far below the measured scatter (table below). |
| Rarefaction and extrapolation | Colwell et al. 2012, [doi:10.1093/jpe/rtr044](https://doi.org/10.1093/jpe/rtr044); Chao et al. 2014, [doi:10.1890/13-0133.1](https://doi.org/10.1890/13-0133.1) | Interpolate down or extrapolate up from one reference sample along a single curve | Individuals are exchangeable random draws from one sampling process | Extrapolating richness is "reliable, at most, only up to a tripling ... or more conservatively, a doubling" (Colwell). For q=0, "no more than double" (Chao). | None found | **Direction supported; formulas do not transfer.** Rarefying VIIRS down is interpolation. Lifting MODIS up is 4.1×. MODIS is a biased sample, not a random one. |
| Unfolding versus forward folding | Cowan 2002, [IPPP Durham](https://www.ippp.dur.ac.uk/old/statistics/proceedings/cowan.pdf); Cranmer et al. 2022, [SciPost Phys. 12, 037](https://doi.org/10.21468/SciPostPhys.12.1.037) | ν = Rμ, where R is the response matrix. Unfolding inverts R and needs regularisation, which "necessarily introduces some bias". Folding pushes a model through R. | R is known and "independent of the true distribution but this is not exact" (Cranmer, fn. 3) | Folded results "cannot be compared with the results of other experiments" (Cowan). MicroBooNE's forward-folding approach was later "discouraged" (Gardiner 2024) | Observation operator for FRP: Sofiev and Kouznetsov 2026. VIIRS-based adjustment of MODIS FRP: Li et al. 2020 | **"MODIS-equivalent as forward folding": right in direction, loose in detail.** What gets folded is VIIRS data, not a model. R is a single scalar, depends on activity and drifts after 2022. |
| Box counting, scale-area curves, occupancy downscaling | Kunin 1998, [Science 281:1513](https://doi.org/10.1126/science.281.5382.1513) (metadata only); He and Gaston 2000, [Am. Nat. 156:553](https://eprints.whiterose.ac.uk/1446/1/gaston.k.j22.pdf); Groom et al. 2018, [doi:10.1111/2041-210X.13078](https://doi.org/10.1111/2041-210X.13078) | Occupied cells as a function of cell size. Under a Poisson pattern, p_occ = 1 − e^(−m), where m is the mean number per cell. A negative-binomial form adds an aggregation parameter k. | A fixed spatial pattern, with sampling that is complete at every grain | "None of these models are suitable for downscaling if used individually" (Groom) | Nothing on hotspot counts versus pixel size. Burned area: small fires add about 35% globally, with "close agreement" in boreal forests (Randerson et al. 2012) | **"Separate pixel size from sensitivity": partly sound.** A common grid removes footprint effects. Occupancy theory has no term for sensitivity. |
| Completeness and selection functions | Christiansen et al. 2020, [AJ 160:159](https://doi.org/10.3847/1538-3881/abab0b); Horvitz and Thompson 1952, [doi:10.1080/01621459.1952.10483446](https://doi.org/10.1080/01621459.1952.10483446) (metadata only); Thomas et al. 2010, [doi:10.1111/j.1365-2664.2009.01737.x](https://doi.org/10.1111/j.1365-2664.2009.01737.x) (metadata only) | Inject known signals, measure the fraction recovered, and weight observed events by 1/p | A known truth, and p > 0 for every unit | Eddington bias: "a threshold in some property which has a noisy correlation with the property of interest" (Lovisari and Maughan 2022). HT variance is large when some inclusion probabilities are "relatively tiny" (Zong et al. 2019) | MODIS detection curves against Landsat or ASTER: Hawbaker et al. 2008 (82% of fires ≥18 ha detected, 50% detection at 105 ha); Giglio et al. 2016 | **"MODIS detection curve with VIIRS as the reference": sound as P(MODIS \| VIIRS), not as completeness.** |

**Thinning test (item 6 of the team's open questions).** These figures are my arithmetic, with V the monthly Suomi NPP hotspot count and p = 0.242.

| V | Binomial thinning, sd of M/V | Same, median absolute error | Both sensors independent Poisson, sd | Two identical Poisson sensors, sd |
|---|---|---|---|---|
| 100 | 17.7% | 11.9% | 22.7% | 14.1% |
| 1,000 | 5.6% | 3.8% | 7.2% | 4.5% |
| 10,000 | 1.8% | 1.2% | 2.3% | 1.4% |
| 62,646 (largest month) | 0.7% | 0.5% | 0.9% | 0.6% |

The measured values are a median error of about 14% in the largest months and ±15 to 20% between identical VIIRS instruments. Both are 10 to 30 times the Poisson prediction for busy months. Most of the scatter therefore comes from sampling: overpass timing, cloud cover and clustered fires.

**Fire-specific facts, checked in the source text.**
- Giglio et al. 2016 measured MOD14 Collection 6 omission against ASTER. Overall omission was 86.2%. It was under 10% for reference fires of 140 or more ASTER pixels, and it levels off at about 5% above about 250 ASTER pixels. Fire size is "extremely skewed toward small fires".
- Sofiev and Kouznetsov 2026 report that MODIS pixel area runs from 1 to 9.66 km². The FRP detection limit is linear in pixel area (correlation above 0.999): 3.7 MW at nadir on a clear night and up to 40 MW for a daytime side view, against 0.5 MW for VIIRS at night. They are "aware of only one study" of detection versus pixel size (Maier et al. 2013, not opened).
- Li et al. 2020 compared Aqua and Suomi NPP detections made within ±5 minutes of each other over Africa. Even then, "fires sensed by one sensor (e.g., VIIRS) could be missed by the other sensor (e.g., MODIS), and vice versa." MODIS FRP was at least 42.8% low, and the shortfall varied with grid size (0.05° to 5°) and view angle.
- Schroeder et al. 2014 found that the 375 m VIIRS algorithm detected 3 times as many daytime fire pixels as the 750 m product, and 25 times as many at night. This mixes a change of algorithm with a change of pixel size.

## What this implies

- The team can cite these fields for the logic of each step. It cannot claim that any one of them validates a hotspot method, because no published use on hotspot counts was found.
- Scaling by 0.242 can be presented as an expected-value conversion. A "thinned" VIIRS series cannot be presented as a simulation of MODIS, because random thinning reproduces less than a tenth of the observed monthly scatter in busy months.
- The VIIRS-to-MODIS direction can be called interpolation. The 2-to-3-fold limit is borrowed from species richness, so it should be cited as an analogy, not as a rule for counts.
- Calling the MODIS-equivalent record "forward folding" is fair only with the cost stated. The result is tied to one response that changes over time and ends in 2027. Months in which MODIS saw nothing (16 to 50% of months in 10 to 100 km circles) cannot be recovered in either direction.
- A common grid can be claimed to remove pixel-footprint effects. The team's ratio is flat between 1 and 5 km cells and sits at 0.65 at 2 km. The remaining gap cannot be attributed to sensitivity alone, because occupancy theory cannot separate sensitivity from clustering. Scan-angle strata within MODIS are a cleaner test of pixel size.
- A VIIRS-referenced detection curve estimates P(MODIS | VIIRS). Fires that VIIRS also misses are absent from it, and HT weights cannot restore events whose detection probability is zero.

## Limits

- Several canonical works were checked only through catalogue metadata, not read: Steutel and van Harn 1979, Weiß 2008, Scotto et al. 2015, Kunin 1998, Hui et al. 2009, Gotelli and Colwell 2001, Horvitz and Thompson 1952, Thomas et al. 2010, Schroeder et al. 2008, Maier et al. 2013, Eddington 1913, Malmquist 1922 and Roteta et al. 2019.
- The thinning theorem was read only in Wikipedia (citing Chiu and Stoyan 2013). The textbook downloads failed.
- The content of the community discussions that discouraged MicroBooNE's forward folding (Gardiner's reference 75) is unknown.
- The Poisson table compares standard deviations with the team's median errors. It shows orders of magnitude, not a fitted model.
- "Nothing found" rests on a few targeted searches per topic.
- The rarefaction mapping was inferred, because the team documents describe none.

## Sources

- Chao A, Gotelli NJ, Hsieh TC, et al. (2014) Rarefaction and extrapolation with Hill numbers. *Ecological Monographs* 84:45–67. doi:10.1890/13-0133.1. Full text read.
- Christiansen JL, et al. (2020) Measuring transit signal recovery in the Kepler pipeline IV. *AJ* 160:159. doi:10.3847/1538-3881/abab0b. arXiv text read.
- Colwell RK, Chao A, Gotelli NJ, et al. (2012) *J. Plant Ecology* 5:3–21. doi:10.1093/jpe/rtr044. Full text read.
- Cowan G (2002) A survey of unfolding methods for particle physics. Proc. Advanced Statistical Techniques in Particle Physics, Durham. https://www.ippp.dur.ac.uk/old/statistics/proceedings/cowan.pdf. Full text read; the year comes from the conference listing.
- Cranmer K, Kraml S, Prosper HB (eds.) et al. (2022) Publishing statistical models. *SciPost Phys.* 12:037. doi:10.21468/SciPostPhys.12.1.037. arXiv v1 read.
- Gardiner S (2024) Mathematical methods for neutrino cross-section extraction. arXiv:2401.04065v2. Read; no journal version found.
- Giglio L, Schroeder W, Justice CO (2016) *RSE* 178:31–41. doi:10.1016/j.rse.2016.02.054. Full text read.
- Groom QJ, Marsh CJ, Gavish Y, Kunin WE (2018) *Methods Ecol. Evol.* doi:10.1111/2041-210X.13078. Read.
- Hawbaker TJ, et al. (2008) *RSE* 112:2656–2664. doi:10.1016/j.rse.2007.12.008. USGS abstract read.
- He F, Gaston KJ (2000) *American Naturalist* 156:553–559. Read.
- Hogg DW, Turner EL (1998) *PASP* 110:727. doi:10.1086/316173. Read.
- Li F, Zhang X, Kondragunta S (2020) *Remote Sensing* 12:1561. doi:10.3390/rs12101561. Full text read.
- Lovisari L, Maughan BJ (2022) arXiv:2202.07673. Bias section read.
- Randerson JT, et al. (2012) *JGR Biogeosciences* 117:G04012. doi:10.1029/2012JG002128. Abstract read.
- Schroeder W, Oliva P, Giglio L, Csiszar IA (2014) *RSE* 143:85–96. doi:10.1016/j.rse.2013.12.008. Read.
- Serrao V, Poojari S, Kamath A (2026) *MethodsX* 16:103805. doi:10.1016/j.mex.2026.103805. Read. Its reference list misdates Steutel and van Harn as 2007.
- Sofiev M, Kouznetsov R (2026) *Geosci. Model Dev.* 19:10123–10142. doi:10.5194/gmd-19-10123-2026. Full text read.
- Stoner O, Economou T, Drummond G (2019) *JASA*. doi:10.1080/01621459.2019.1573732. arXiv text read.
- Barwell LJ, et al. (2014) *Diversity and Distributions*. doi:10.1111/ddi.12203. Abstract read.
- Zong X, Zhu R, Zou G (2019) *Survey Methodology* 45(1). Statistics Canada 12-001-X. Read.
- Wikipedia, "Poisson point process", section on thinning. Secondary source.
