# Machine-learning translation between sensors and spatiotemporal image fusion

## Summary

This family has two parts. The first is machine learning (ML), where a model learns from an overlap period to map one sensor's product onto another's. The second is spatiotemporal fusion (STF), which combines a coarse sensor that observes often with a fine sensor that observes rarely, to predict fine images on dates when only the coarse one exists. Almost all published uses are on continuous gridded fields such as reflectance, land surface temperature (LST) and night lights, and they train on thousands to tens of thousands of pixels or image patches. For fire, we found one STF study (coal-fire imagery), one deep-learning model that sharpens geostationary fire images to look like VIIRS (Visible Infrared Imaging Radiometer Suite) images, and two fire radiative power (FRP) "fusion" papers that use simple fitted calibrations, not ML. We found no study that uses ML or STF to make MODIS (Moderate Resolution Imaging Spectroradiometer) and VIIRS hotspot counts comparable. This is an absence result from a search cut short by the search budget. The team has about 116 stable-orbit overlap months. Its own data show the relationship is close to a single multiplicative factor. Only the smallest learned model, judged by blocked validation against a plain ratio, carries over.

## Methods

| Method | How it works | Where used | Data needed | Main assumption | Known failure mode |
|---|---|---|---|---|---|
| Deep sequence translation (transformer) | Learns a shared representation of daily MODIS and VIIRS reflectance per pixel and translates in both directions. | Hamdi et al. 2026, poster ([PDF](https://events.ecmwf.int/event/488/contributions/5783/attachments/3537/5975/Poster_Hamdi.pdf)): 40,000 global pixels, 2012–2023. | Dense paired daily time series with quality flags. | The bias is learnable from many pixels and stays stable after the overlap period. | The poster notes "location-dependent bias"; no test on extreme events (poster, not peer reviewed). |
| Unpaired image translation (CUT, contrastive unpaired translation network) | A generative network learns to make old-sensor images look like new-sensor images without matched pairs. | Tong et al. 2026, DMSP to VIIRS night lights ([arXiv:2603.16385](https://arxiv.org/abs/2603.16385)). | Thousands of image patches from the overlap year or years. | Image "style" learned in the overlap applies back to 1992. | Checkerboard and halo artefacts; held-out R² of 0.87 overall but 0.68 in bright urban cores. |
| Tree ensembles (random forest, gradient boosting such as XGBoost) | Regression trees, built separately for each date, predict fine-scale LST from fine and coarse inputs. | Haghshenas and Shamsoddini 2026 ([doi:10.32604/rig.2026.076139](https://doi.org/10.32604/rig.2026.076139)): RMSE (root-mean-square error) 1.87 K against 2.62 K for ESTARFM. | Image pairs on dates before and after the target date. | Training and prediction conditions are similar. | Transfer between sensors is asymmetric. Hengl et al. 2018: with few points and near-linear relations, simpler models can be more accurate. |
| Weighted-function STF (STARFM, spatial and temporal adaptive reflectance fusion model; ESTARFM, enhanced STARFM) | Predicts a fine pixel at a target date from neighbouring similar pixels in fine–coarse image pairs, weighted by spectral, temporal and spatial distance. | Gao et al. 2006 ([doi](https://doi.org/10.1109/TGRS.2006.872081)); coal fires with Landsat-8 and VIIRS, Ghosh et al. 2020 ([doi](https://doi.org/10.1016/j.jag.2020.102056)). | Co-registered continuous images of the same quantity from both sensors. | The coarse sensor records every change that matters. | Abrupt land-cover change between the input dates and the target date is the case that later hybrid methods were built to handle (Wu et al. 2021). |
| Unmixing and hybrid STF (for example FSDAF, flexible spatiotemporal data fusion) | Treats a coarse pixel's change as a mixture of fine land-cover classes, sometimes combined with weighting. | Reviewed in Wu et al. 2021 ([doi](https://doi.org/10.1109/MGRS.2021.3050782)). | Continuous images and a land-cover map. | Changes mix linearly. | "Challenged if land cover changes"; rarely applied to temperature. |
| Deep-learning STF | Neural networks learn the fine–coarse mapping from image pairs. | Bouaziz et al. survey ([arXiv:2412.16631](https://arxiv.org/abs/2412.16631)): benchmark of 51 MODIS–Landsat LST pairs. | Dozens or more image pairs. | Enough paired images exist. | "Limited high-resolution observations can make models prone to overfitting." |
| Learned fire super-resolution | An autoencoder maps GOES-17 fire images (2 km or coarser) to VIIRS-like 375 m fire area and brightness temperature. | Badhan et al. 2024 ([doi:10.3390/rs16040715](https://doi.org/10.3390/rs16040715)). | Geostationary imagery plus VIIRS points turned into grids; 5,869 patches. | VIIRS is the truth at each matched time. | Cannot remove false-positive noise; split was by patch, and I found no split by fire. |
| Fitted calibration, then priority fusion (non-ML baseline) | Fits a line or curve between sensors over the overlap, then uses the preferred sensor and fills gaps with the calibrated one. | Li et al. 2019 ([doi](https://doi.org/10.1016/j.atmosenv.2019.05.017)); Zheng et al. 2026 ([doi](https://doi.org/10.3390/rs18101650)); Chen et al. 2026 ([doi](https://doi.org/10.5194/essd-18-7535-2026)). | Near-simultaneous matched fires (Li, Zheng) or aggregate counts (Chen). | The fitted factor holds outside the overlap and on other platforms. | Zheng: not transferable to Terra. Chen: scalars "held fixed"; evaluation over the fitting years. |

## How each would map onto MODIS and VIIRS hotspots

**Small learned regression with blocked validation.** This is the reviewer's construction from the sources. No source applies it to fire counts. Steps: aggregate to area-months; fit MODIS count against Suomi NPP count with a day/night split, as a ratio, a log-linear model or a Poisson or negative-binomial generalized linear model (two to four parameters); hold out one fire season at a time, with 2017, 2018 and 2021 reported separately; compare with the plain ratio. It addresses the level difference (0.242 overall, 0.34 by day, 0.18 at night) and the day/night mix in small areas or quiet months. It does not remove the ±15–20% single-month scatter between identical VIIRS instruments. It does not restore the months, a third or more below about a 50 km radius, where MODIS recorded nothing. It does not correct Terra's 2026 drift (0.46 of the expected daytime count). The team has all the data it needs. Effort: hours. Roberts et al. 2017 support blocking the cross-validation by time. The team's finding that slopes are near 1 and that a power law did not beat one factor out of sample means the gain over a plain ratio may be nil.

**Tree ensemble with covariates (month, day/night share, area size, scan size).** Steps as above, with a random forest or boosting model. With roughly 10 independent seasons, the number of covariates exceeds what the data can pin down. Meyer and Pebesma 2021 show that ML predictions are reliable only when new data resemble the training data, so a record-breaking month lies outside that range. The team's evidence already shows that a scan-angle term and per-month factors do not help. Data: yes. Effort: about a day with proper validation. Defending it would be hard.

**Event-level calibration in the style of Li 2019 or Zheng 2026.** Steps: match near-simultaneous Aqua and Suomi NPP detections (about 13:30 local time for both) and fit a ratio against view angle. Zheng's reference is cloud-corrected VIIRS FRP, which uses clear-sky fractions within each footprint, and the team has no cloud mask. Zheng also says the coefficients should not be transferred to Terra. The team found that FRP bridges worse than counts and that scan-angle terms do not reduce monthly scatter. Effort: a day or more.

**What a judge would need to see** (the reviewer's inference from Roberts 2017 and Meyer and Pebesma 2021): the plain-ratio baseline on the same holdout; leave-one-season-out validation, not random folds; errors given separately for big and small months; a stated range of validity; a check on the post-2022 drift period; and a statement that months where MODIS saw nothing cannot be recovered.

## Not applicable, and why

- STARFM, ESTARFM and unmixing or hybrid STF: they need continuous co-registered images or swath data. Hotspots are sparse points with no record of non-detections, and the team's problem is detection sensitivity, not missing fine-scale dates.
- Deep-learning STF and CUT translation: they need thousands of image patches. The team has about 116 monthly values per area.
- Transformer translation (Hamdi): it needs dense daily reflectance series.
- GOES-to-VIIRS super-resolution: geostationary data do not reach back to 2000, and the team has no imagery.
- Formal domain adaptation: we found no application to event or count products.

## Unconfirmed

- An ML study that predicts MODIS-equivalent fire counts or burned area from VIIRS with covariates: none was found. Searching stopped when the shared web-search budget ran out.
- Hilker et al. 2009 ([doi](https://doi.org/10.1016/j.rse.2009.03.007)) is said to note that fusion was not designed for sub-pixel disturbance. I could not open it.
- The claim that tree ensembles cannot predict beyond the training range is standard, but no opened source states it in those words.
- Read as abstracts only: Gao 2006, Ghosh 2020, Haghshenas 2026 (no study area or failure modes), Hengl 2018, Roberts 2017, Meyer and Pebesma 2021, Zhu et al. 2018. The Meyer et al. 2018 cross-validation numbers were not re-verified.
- Tong 2026 is an unrefereed preprint and is internally inconsistent: the PDF abstract says R² above 0.95, the abstract page and held-out table say 0.87, and the overlap is given as 2012–2013 in one place and 2013 in another.
- The last 10,800 characters of Chen 2026 were not read.

## Sources

- Badhan, M., Shamsaei, K., Ebrahimian, H., Bebis, G., Lareau, N.P., Rowell, E. (2024). Remote Sensing 16(4):715. https://doi.org/10.3390/rs16040715 (author PDF read)
- Bouaziz, S., Hafiane, A., Canals, R., Nedjai, R. (2024, revised 2025). arXiv:2412.16631. https://arxiv.org/abs/2412.16631
- Chen, Y., van der Werf, G.R., et al. (2026). Earth System Science Data 18:7535–7555. https://doi.org/10.5194/essd-18-7535-2026
- Gao, F., Masek, J., Schwaller, M., Hall, F. (2006). IEEE Transactions on Geoscience and Remote Sensing 44(8):2207–2218. https://doi.org/10.1109/TGRS.2006.872081
- Ghosh, R., Gupta, P.K., Tolpekin, V., Srivastav, S.K. (2020). International Journal of Applied Earth Observation and Geoinformation 88:102056. https://doi.org/10.1016/j.jag.2020.102056
- Haghshenas, N., Shamsoddini, A. (2026). Revue Internationale de Géomatique 35:249–272. https://doi.org/10.32604/rig.2026.076139
- Hamdi, Z.M., Jung, M., Duveiller, G., et al. (2026). Poster, 5th ECMWF–ESA Machine Learning Workshop, Bologna, 13–17 April 2026. https://events.ecmwf.int/event/488/contributions/5783/attachments/3537/5975/Poster_Hamdi.pdf
- Hengl, T., Nussbaum, M., Wright, M.N., Heuvelink, G.B.M., Gräler, B. (2018). PeerJ 6:e5518. https://doi.org/10.7717/peerj.5518
- Li, F., Zhang, X., Roy, D.P., Kondragunta, S. (2019). Atmospheric Environment 211:274–287. https://doi.org/10.1016/j.atmosenv.2019.05.017
- Meyer, H., Pebesma, E. (2021). Methods in Ecology and Evolution 12:1620–1633. https://doi.org/10.1111/2041-210X.13650
- Meyer, H., Reudenbach, C., Hengl, T., Katurji, M., Nauss, T. (2018). Environmental Modelling & Software 101:1–9. https://doi.org/10.1016/j.envsoft.2017.12.001
- Roberts, D.R., Bahn, V., Ciuti, S., et al. (2017). Ecography 40:913–929. https://doi.org/10.1111/ecog.02881
- Tong, Z., Zhou, C., Tang, F., Tu, Y., Qin, T., Fang, K. (2026). arXiv:2603.16385. https://arxiv.org/abs/2603.16385
- Wu, P., Yin, Z., Zeng, C., et al. (2021). IEEE Geoscience and Remote Sensing Magazine 9(3):112–137. https://doi.org/10.1109/MGRS.2021.3050782 (read as arXiv:1909.09316)
- Zheng, Y., Ding, K., Xue, L., et al. (2026). Remote Sensing 18(10):1650. https://doi.org/10.3390/rs18101650
- Zhu, X., Cai, F., Tian, J., Williams, T.K.-A. (2018). Remote Sensing 10(4):527. https://doi.org/10.3390/rs10040527
