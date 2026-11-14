# Harmonizing DMSP and VIIRS night-time lights: the closest remote-sensing analogue

## Summary

Night-time light (NTL) researchers had to join the Defense Meteorological Satellite Program Operational Linescan System (DMSP-OLS, 1992 to 2013; coarse, saturating, no on-board calibration) to the Visible Infrared Imaging Radiometer Suite Day/Night Band (VIIRS DNB, from 2012; finer, calibrated) with roughly one shared year. They used five families: degrading VIIRS to look like DMSP, regression in the overlap, pseudo-invariant features (places assumed not to change), machine-learning image translation, and corrections of the old sensor alone. The field split on direction: the NOAA Earth Observation Group made VIIRS DMSP-like because "there is no deterministic way to add detail" (Nechaev et al. 2021), while several groups made DMSP VIIRS-like with deep learning (Chen et al. 2021; Cheng et al. 2026), and economists showed that DMSP-like harmonized data re-import DMSP's spurious spatial autocorrelation (Gibson et al. 2024). No source opened applies any of these methods to fire hotspots; the lights products actually remove fires as noise. The transferable parts are the direction argument, year-out validation and the warning about inherited artefacts; the pixel-level machinery assumes continuous radiances at fixed places, which hotspot counts are not.

## Methods

| Method | How it works | Where used | Data needed | Main assumption | Known failure mode |
|---|---|---|---|---|---|
| Spatial degradation plus saturation emulation (new to old) | Aggregate VIIRS to DMSP's 30 arc-second grid with a Gaussian kernel window 5 VIIRS pixels wide, take ln(x+1), then map through a four-parameter sigmoid (a=6.5, b=57.4, c=−1.9, d=10.8) fitted on 2013. | [Li et al. 2020](https://doi.org/10.1038/s41597-020-0510-y), sigmoid form from [Zhao et al. 2020](https://doi.org/10.1109/TGRS.2019.2949797) | Paired co-registered rasters in an overlap year | One global curve links the sensors everywhere | No R² or error statistic reported; authors say values are reliable only above DN 20 and to be "cautious ... in rural areas"; 01:30 versus about 21:00 overpass named as an uncorrected factor |
| Overlap regression, functional forms | Fit linear, quadratic, power or sigmoid curves between sensors in the overlap, sometimes per region. | Li 2020; [Ghosh et al. 2021](https://doi.org/10.3390/rs13245004) (zero-intercept quadratic) | Paired values in overlap | Relationship is a fixed smooth function | Nechaev et al. 2021: sensors differ in "spatial resolution, dynamic range and saturation", so linear or polynomial links are "not always the case" |
| Invariant-region intercalibration between satellites of one series | Choose places assumed unchanged (Sicily; Mauritius, Puerto Rico, Okinawa), fit each satellite-year to a reference year; power function fitted best of five forms. | [Elvidge et al. 2009](https://doi.org/10.3390/en20300595) (as described by Wu); [Wu et al. 2013](https://doi.org/10.1080/01431161.2013.820365); [Zhao C. et al. 2022, CCNL](https://doi.org/10.1038/s41597-022-01540-x) | Repeated observations of stable targets | Truth at the invariant sites is constant | CCNL: "a global model for interannual correction may result in overcorrection in some regions"; GDP correlation in Japan fell from 0.57 to 0.20 |
| Automatic pseudo-invariant feature (PIF) selection | Pick stable pixels statistically (ridgeline of the reference-versus-target density plot; or Getis Gi* hot-spot statistic plus coefficient of variation). | [Zhang, Pandey and Seto 2016](https://doi.org/10.1109/TGRS.2016.2572724) (abstract); [Mukherjee et al. 2017](https://doi.org/10.1007/s40010-017-0444-8) (abstract) | Dense images, many pixels | Enough unchanged pixels exist | Result depends on which pixels are chosen |
| Reference-sensor diurnal intercalibration of drifted satellites | DMSP F15 and F16 drifted to pre-dawn; their data were reprocessed and matched to VIIRS degraded to DMSP units, using offshore Persian Gulf gas flares as targets with "no diurnal pattern". | Ghosh et al. 2021 | Reference sensor with in-flight calibration; diurnally constant targets | Targets do not vary with time of day | No numeric accuracy given for the intercalibration in the text read |
| Convolutional network, new to old | Residual U-Net trained on same-year VIIRS and DMSP F15 composites (2013 to 2019), tested on held-out years. | [Nechaev et al. 2021](https://doi.org/10.3390/rs13245026) | Several overlap years of paired images | Mapping is stable across years | Good fit (R² 0.96 to 0.99 test spots; 0.94 globally for 2015; Sicily sum of lights within 15%, worst in 2013), but output inherits DMSP blur (Gibson et al. 2024) |
| Deep-learning translation, old to new | Autoencoder or super-resolution networks, with vegetation index, Landsat or impervious-surface inputs, trained on 2013 and checked on 2012. | [Chen Z. et al. 2021](https://doi.org/10.5194/essd-13-889-2021); [Chen X. et al. 2024](https://doi.org/10.1038/s41597-024-04228-6); [Cheng et al. 2026](https://doi.org/10.5194/essd-18-3449-2026); [Tong et al. 2026](https://arxiv.org/abs/2603.16385) (preprint) | Paired images plus ancillary layers | Ancillary data supply the missing detail | Pre-2012 values are model output; pixel R² 0.87 (Chen 2021) and mean monthly 0.65 (Cheng 2026); weaker in Africa, South America and Oceania; Cheng 2026 uses April–December 2012 for both correction and "independent" validation |
| Correct the old sensor only | Fix top-coding (Pareto tail) or saturation and blooming within DMSP; use VIIRS separately after 2012. | [Gibson 2021](https://doi.org/10.1111/obes.12417); CCNL 2022 | Old sensor only | Users can live with a seam | Top-coding fix has "a modest effect" |

Critique common to the first, second and sixth rows: [Gibson et al. 2024](https://doi.org/10.1007/s41885-024-00152-6) found that making VIIRS DMSP-like raised Moran's I (a spatial autocorrelation statistic) by 77% for Philippine municipalities, "largely undoing gains in spatial precision", and that DMSP shows false zeros in about a quarter of municipalities.

## How each would map onto MODIS and VIIRS hotspots

All numbers below are from the team's harmonization-evidence.md. No source applies these methods to fire; the mappings are inferences.

**Degradation to the old sensor's footprint.** Equivalent: thin VIIRS hotspots into roughly 1 km MODIS-sized cells (active cell-days) before scaling. The team has already measured this: at 2 km the MODIS/VIIRS ratio rises from 0.24 to 0.65 and duplicates are removed, but single-month error improves only modestly (about 20% against 24–29%). The saturation-emulation step has no counterpart: hotspots fail at a detection floor (MODIS records nothing in 33–50% of VIIRS-fire months below about 50 km radius), not a brightness ceiling. Data available; effort: hours, mostly done. Gibson's warning carries over: a MODIS-equivalent series inherits MODIS's missed small fires.

**Overlap regression with chosen functional form.** Equivalent: a scale factor or curve fitted on 2012–2021. The team already tested this: the relationship is close to linear and a power law did not beat one factor out of sample, so Wu's finding that a power form wins for DMSP does not transfer. Splitting by day and night (0.34 and 0.18) is the "per region or per condition" variant. Fixes level; does not fix the 15–30% monthly scatter or the zero months. Effort: hours.

**Year-out validation design (from Nechaev 2021).** Equivalent: fit on nine stable-orbit years, test on the tenth, repeated. The team has about ten overlap years against the lights field's one, though only with Suomi NPP, and the record is dominated by 2017, 2018 and 2021. Gives an honest error figure for the submission. Effort: hours.

**Reference-sensor handling of orbit drift (from Ghosh 2021).** Equivalent: treat VIIRS (constant overpass times) as the calibrated reference and Terra's drift from about 11:15 to 09:20 as a time-of-day problem. Ghosh could intercalibrate only because flares lack a diurnal cycle; fire has a strong one, so a drift correction cannot be fitted on a "constant" target and would need a diurnal fire model the team lacks. What does carry over: do not fit factors on drift years, and judge drifted MODIS against NOAA-20, as the team did (Terra day ratio 0.070 in 2026 versus 0.127–0.212 before). Effort: hours for the check, days or more for a correction.

**Machine-learning translation (either direction).** Equivalent: learn MODIS detection from VIIRS hotspot attributes (fire radiative power, brightness temperature, scan, day/night). This needs labelled non-detections; FIRMS rows have no record of overpasses that saw nothing, no swath and no cloud mask, so "MODIS looked and missed" cannot be labelled. At monthly area level there are only about 116 overlap months. Effort: days or more; context only.

## Not applicable, and why

- Saturation and blooming correction: hotspots have no saturated ceiling to correct.
- Pseudo-invariant features: wildfire has no stable truth; the one persistent source (near Kamloops) is detected by VIIRS only, 921 rows and no MODIS rows.
- Inter-satellite calibration of the DMSP kind: VIIRS satellites already agree (NOAA-20 0.99, NOAA-21 0.97 of Suomi NPP).
- Super-resolution of the old sensor: there is no MODIS image to sharpen and no ancillary layer that predicts missed small fires.
- Cloud-weighted compositing (Li 2020): needs cloud-free observation counts the team does not have.

## Unconfirmed

- Zhang, Pandey and Seto 2016 and Mukherjee et al. 2017: bibliographic data confirmed; content from abstracts only (Mukherjee metadata re-check was rate-limited).
- Chen X. et al. 2024: citation confirmed from Crossref; method and accuracy not read.
- Tong et al. 2026: abstract only, not peer reviewed.
- Cheng et al. 2026: read through a summarizing fetch of the first 100,000 characters; the circularity point is my reading of Section 3.4 against the abstract.
- Chen Z. et al. 2021: read through a summarizing fetch; city R² is 0.94 in Section 4.2 and 0.95 in the abstract.
- Levin et al. 2020, [a review of night-light remote sensing](https://doi.org/10.1016/j.rse.2019.111443), is the likely best review entry point; only metadata confirmed, content not read.
- Not opened, so not used: Li and Zhou 2017 stepwise DMSP calibration; Wei et al. 2014 PIF paper; Tu et al. and Zheng et al. regressions (known only via Nechaev's introduction); Gibson et al. 2021, Journal of Development Economics.
- The web search budget for this run was exhausted during verification, so no further search for a fire application or a dedicated harmonization review was possible.

## Sources

- Chen X., Wang Z., Zhang F., Shen G., Chen Q. (2024). Scientific Data 11:1380. https://doi.org/10.1038/s41597-024-04228-6
- Chen Z., Yu B., Yang C., et al. (2021). Earth System Science Data 13:889–906. https://doi.org/10.5194/essd-13-889-2021
- Cheng H., Geng M., Li X., et al. (2026). Earth System Science Data 18:3449–3479. https://doi.org/10.5194/essd-18-3449-2026
- Elvidge C.D., Ziskin D., Baugh K.E., et al. (2009). A fifteen year record of global natural gas flaring derived from satellite data. Energies 2(3):595–622. https://doi.org/10.3390/en20300595
- Ghosh T., Baugh K.E., Elvidge C.D., et al. (2021). Extending the DMSP nighttime lights time series beyond 2013. Remote Sensing 13(24):5004. https://doi.org/10.3390/rs13245004
- Gibson J. (2021). Better night lights data, for longer. Oxford Bulletin of Economics and Statistics 83(3):770–791. https://doi.org/10.1111/obes.12417 (read as CSAE working paper WPS/2020-08)
- Gibson J., Jiang Y., Zhang X., Boe-Gibson G. (2024). Are disaster impact estimates distorted by errors in popular night-time lights data? Economics of Disasters and Climate Change. https://doi.org/10.1007/s41885-024-00152-6 (read as reproduced in Zhang X., 2024, PhD thesis, University of Waikato, https://researchcommons.waikato.ac.nz/bitstreams/dee5cd0f-9ca5-4cd4-9166-1e5a18fd1fa6/download)
- Levin N., Kyba C.C.M., Zhang Q., et al. (2020). Remote sensing of night lights: a review and an outlook for the future. Remote Sensing of Environment 237:111443. https://doi.org/10.1016/j.rse.2019.111443 (metadata only)
- Li X., Zhou Y., Zhao M., Zhao X. (2020). A harmonized global nighttime light dataset 1992–2018. Scientific Data 7:168. https://doi.org/10.1038/s41597-020-0510-y
- Mukherjee S., Srivastav S.K., Gupta P.K., et al. (2017). Proc. Natl. Acad. Sci. India Sect. A 87:721–731. https://doi.org/10.1007/s40010-017-0444-8 (abstract)
- Nechaev D., Zhizhin M., Poyda A., et al. (2021). Cross-sensor nighttime lights image calibration for DMSP/OLS and SNPP/VIIRS with residual U-Net. Remote Sensing 13(24):5026. https://doi.org/10.3390/rs13245026
- Tong Z., Zhou C., Tang F., et al. (2026). arXiv:2603.16385. https://arxiv.org/abs/2603.16385 (abstract)
- Wu J., He S., Peng J., Li W., Zhong X. (2013). Intercalibration of DMSP-OLS night-time light data by the invariant region method. International Journal of Remote Sensing 34(20):7356–7368. https://doi.org/10.1080/01431161.2013.820365
- Zhang Q., Pandey B., Seto K.C. (2016). A robust method to generate a consistent time series from DMSP/OLS nighttime light data. IEEE TGRS 54(10):5821–5831. https://doi.org/10.1109/TGRS.2016.2572724 (abstract)
- Zhao C., Cao X., Chen X., Cui X. (2022). A consistent and corrected nighttime light dataset (CCNL 1992–2013) from DMSP-OLS data. Scientific Data 9:424. https://doi.org/10.1038/s41597-022-01540-x
- Zhao M., Zhou Y., Li X., Zhou C., Cheng W., Li M., Huang K. (2020). Building a series of consistent night-time light data (1992–2018) in Southeast Asia by integrating DMSP-OLS and NPP-VIIRS. IEEE TGRS 58(3):1843–1856. https://doi.org/10.1109/TGRS.2019.2949797
