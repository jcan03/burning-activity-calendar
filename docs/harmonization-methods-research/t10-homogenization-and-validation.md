# Climate-record homogenization, quantile mapping, and how harmonized records are validated

## Summary

Climatology repairs long records that contain instrument changes in two ways. Homogenization detects step changes ("breakpoints") in a station's record by comparing it with neighbouring records, then adjusts the record by a constant or by a size-dependent amount. Bias correction by distribution mapping, chiefly quantile mapping (QM), rewrites one data set so that its cumulative distribution function (CDF) matches a reference over a shared calibration period. Neither has, as far as this review could find, been applied to fire hotspot counts in the peer-reviewed literature; the nearest fire use is quantile mapping of gridded MODIS fire radiative power (FRP) by Kaur et al. (2019), plus one unreviewed hackathon project. These methods were built for continuous variables, long calibration records and neighbours that share one signal, while the team has about ten overlap years, counts with many zeros at small areas, and a target sensor that detects fires the other cannot. They transfer better as validation tools (fixed-date step tests, pairwise sensor attribution, year-blocked hold-outs, ensemble uncertainty) than as correction tools.

## Methods

| Method | How it works | Where used | Data needed | Main assumption | Known failure mode |
|---|---|---|---|---|---|
| Pairwise homogenization (PHA) | Forms target-minus-neighbour difference series, tests each with the standard normal homogeneity test (SNHT), blames the series that breaks in most pairs, and adjusts by the median of at least three pairwise step estimates, each from neighbour segments homogeneous for 24 months either side. | US monthly temperature ([Menne and Williams 2009](https://doi.org/10.1175/2008JCLI2263.1)) | Several overlapping series of the same quantity | Neighbours share the true signal; breaks are mostly not simultaneous | Fewer than three estimates makes a shift "unadjustable"; adjustments are constant across calendar months (p. 1715–1716) |
| Relative homogenization, benchmarked | Candidate compared with neighbours "in a pairwise fashion or to a single composite reference"; precipitation breaks modelled as multiplicative. | 25 blind contributions to the HOME benchmark ([Venema et al. 2012](https://doi.org/10.5194/cp-8-89-2012)) | Network of stations | As above | Methods typically improve temperature, but "only the best ones improve precipitation data" (abstract) |
| Fixed-date versus unknown-date changepoint tests | When a change date is known, test the cumulative-sum (CUSUM) statistic at that date; when unknown, the maximum over all dates needs much larger critical values. | Review with worked climate examples ([Lund et al. 2023](https://doi.org/10.1175/JCLI-D-22-0954.1)) | One series, or a target-minus-reference series | Mean-shift model; autocorrelation, trend and seasonality modelled | Ignoring autocorrelation or trend produces spurious changepoints (Pitfalls 2–3); conclusions "not robust to small perturbations in assumptions" |
| Quantile-matching adjustment of shifts | After breaks are found, splits each segment into up to 20 ranked categories, takes differences of category means against the base segment, and fits a spline so each datum gets its own adjustment. | Environment Canada RHtests software ([Wang 2009 note](https://etccdi.pacificclimate.org/RClimDex/QMadj_Gaussian.pdf); [RHtests](https://github.com/ECCC-CDAS/RHtests)) | One long series; reference optional | Gaussian data after removing season and trend | Needs at least 5 data per category; with too few it falls back to one mean adjustment |
| Quantile mapping (QM) | Maps each value through the source CDF and the inverse target CDF fitted over a calibration period. | Climate-model precipitation ([Cannon et al. 2015](https://doi.org/10.1175/JCLI-D-14-00754.1)) | Overlapping samples of both series | Bias is stationary (p. 6941) | Inflates trends in extremes; defined only within the calibration range; "cannot add wet days" ([Lehner et al. 2023](https://doi.org/10.5194/ascmo-9-29-2023), Sects. 3.4, 4.3) |
| Detrended QM and quantile delta mapping (QDM) | Remove the trend (DQM) or carry each quantile's relative change (QDM) through the mapping. | Same as above | Same, plus a projection period | Designed to preserve a model's projected change | Solves a projection problem the team does not have |
| Stochastic bias correction | Adds randomization when the reference is at much finer scale than the corrected data. | [Maraun 2013](https://doi.org/10.1175/JCLI-D-12-00821.1) | As QM | — | Plain QM across a scale gap misrepresents structure, overcorrects drizzle and overestimates area-mean extremes |
| CDF matching onto a stable reference sensor | Rescales each sensor percentile by percentile, linearly, onto the sensor "expected to have the most stable climatology", chaining sensors in sequence. | ESA CCI Soil Moisture ([Gruber et al. 2019](https://doi.org/10.5194/essd-11-717-2019)) | Collocated continuous retrievals | Reference is stable | Preserves trend direction but "can change its magnitude"; may introduce spurious error correlations |
| QM of gridded FRP by view angle | Maps the CDF of off-nadir gridded FRP, with zero-FRP cells counted in the first bin, onto near-nadir FRP; validated against VIIRS in a different year. | MODIS fire ([Kaur et al. 2019](https://doi.org/10.3390/rs11101205)) | Gridded FRP including non-fire and zero cells and observed-area fraction (from the GFAS gridded product) | Same fire population sampled at all angles over a year | "False zero" cells cannot be corrected; 30% residual missing FRP at 0.1°, 6% at 1°; boreal forest overcorrected (corrected Aqua 422 MW against 382 MW for VIIRS) |
| Per-datum uncertainty and ensemble records | Give standard uncertainty, document error correlation and when uncertainty is invalid, validate uncertainty, and optionally publish an ensemble of plausible records. | [Merchant et al. 2017](https://doi.org/10.5194/essd-9-511-2017); HadCRUT5, 200 realisations covering homogenisation uncertainty ([Morice et al. 2021](https://doi.org/10.1029/2019JD032361); [Met Office](https://www.metoffice.gov.uk/hadobs/hadcrut5/)) | Error model or resampling | Error sources can be enumerated | Unquantified error sources must be described in words |
| Metrological harmonisation | Re-estimates each sensor's calibration parameters from sensor-to-sensor collocated "matches", with uncertainty. | Historical radiometers ([Mittaz et al. 2019](https://doi.org/10.1088/1681-7575/ab1705)) | Radiances and calibration data | Physical measurement model | Not possible from detection lists |
| Blocked cross-validation | Hold out whole blocks (for example years) rather than random rows. | Ecology review ([Roberts et al. 2017](https://doi.org/10.1111/ecog.02881)) | Any fitted model | Blocks are roughly independent | Random hold-outs give "serious underestimation of predictive error"; blocks can force extrapolation |

## How each would map onto MODIS and VIIRS hotspots

**Fixed-date step tests on log-ratio series.** Form monthly log(MODIS/Suomi NPP), log(NOAA-20/Suomi NPP) and log(NOAA-21/Suomi NPP), by day and night, for the whole box or areas of about 100 km radius or more, after removing the Kamloops static source (an additive term no ratio can remove). Test a step at April 2018, March 2023 and January 2022 with a regression on an "after date" indicator and autoregressive errors, as Lund et al. advise for known dates; use the unknown-date maximum test only to ask whether an unexpected break exists. For the drift, a trend term after 2022 fits the measured shape (Terra's daytime count at 0.95, 0.81, 0.77, 0.70 and 0.46 of expected in 2022–2026) better than a step. It detects problems but corrects nothing. Below about 50 km, MODIS has zero hotspots in a third or more of the months in which VIIRS saw fire, so log ratios are undefined; a count regression (Poisson or negative binomial with a period indicator) would be needed, which no source here tests. With 15–20% scatter between identical VIIRS instruments, only steps larger than about that size are detectable within a few years. Effort: hours.

**Pairwise sensor attribution.** Apply Menne and Williams' culprit logic to sensors: if Terra-versus-VIIRS breaks in 2023–2026 but Aqua-versus-VIIRS does not, the break belongs to Terra. The team's data already show this pattern for Terra by day. Before 2012 only Terra and Aqua exist, both MODIS, so a shared MODIS change would be invisible, the simultaneous-break case that Venema et al. found hardest. Effort: hours, if built with the step tests.

**Year-blocked hold-out of the overlap.** Leave-one-year-out over the stable-orbit years 2012–2021: fit the factor on nine years, predict the tenth, repeat. Add a time split (fit 2012–2016, test 2017–2021, then reverse); Cannon et al. validated on years on both sides of their calibration period. Score as log or relative error and compare with the VIIRS-to-VIIRS floor of ±15–20%. A residual step at 2012 can only be tested on held-out years, because the in-sample residual is zero by construction. The overlap is dominated by 2017, 2018 and 2021, so any split has high variance. The unreviewed project in the Sources fitted QM on 2012–2020, tested on 2021–2024 and ran a 2012 step test with placebo years, which shows the design is practical. Effort: hours.

**Ensemble uncertainty for a pre-2012 month.** Draw a factor from the year-resampling (0.242, interval 0.237–0.28), add a monthly residual drawn from the leave-one-year-out errors (median about 14% in large months, 23% in moderate, 30% over all fire-season months), add Poisson count noise, and report a median, an interval and the probability of each calendar class. This follows Merchant et al.'s ensemble idea and keeps the correlation of error across months of one year. Document what is not covered (Merchant recommendation 6): whether the ratio held before 2012, the Terra-only years 2000–2002 (Terra/Aqua is 0.72 by day and 2.2 at night), and the unstable night factor. It does not restore missed small-area detections. Effort: a day.

**Quantile mapping of monthly counts.** Fit the MODIS-to-VIIRS monthly count CDF on overlap months and map pre-2012 months through it. With about 70 fire-season months, Wang's 5-per-category rule allows up to 14 categories, but Reiter et al. found the critical calibration length "exceeds ten years in all experiments", with empirical QM most vulnerable. QM is monotone, so every MODIS zero maps to one value and missed detections are not restored. The team found that a power-law curve did not beat one factor out of sample, which leaves QM little to gain over a single ratio. Effort: hours to build, a day to validate.

## Not applicable, and why

- Metrological harmonisation needs radiances and calibration parameters; FIRMS gives only detections.
- Kaur et al.'s view-angle QM needs zero-FRP and observed-area information for each grid cell, which needs swath and cloud data the team does not have.
- DQM and QDM preserve a projected future trend, a problem the team does not have.
- PHA's full network adjustment needs many neighbours; the team has two to five sensors and only two before 2012.
- Stochastic bias correction addresses a scale gap in continuous fields, not missing detections.

## Unconfirmed

- GCOS Fire variable stability requirement: the GCOS website lists 0, 1 and 2% (goal, breakthrough, threshold) for active fires and FRP but gives no time basis; the underlying 2022 requirements document and GCOS-154 were not opened.
- Read as abstract or landing page only: Reiter et al. 2016, Gudmundsson et al. 2012, Wang et al. 2010, Lund and Reeves 2002, Gutiérrez et al. 2019 (VALUE). Morice et al. 2021 was not opened; its ensemble size comes from the Met Office page.
- Wang et al. 2010 recommending a separate test of zero-precipitation frequency: not confirmed.
- No peer-reviewed application of homogenization, changepoint tests or QM to fire counts, or of QM to integer counts, was found. The web search budget ran out during verification, so this negative result rests on the researcher's searches.
- Review papers not opened: Maraun 2016 (bias correction critique) and Ribeiro et al. 2016 (homogenization methods); bibliographic details confirmed only.
- Lund et al. 2023 was read as arXiv v1; journal details confirmed from Crossref.

## Sources

- Cannon, A. J., Sobie, S. R., Murdock, T. Q. (2015). J. Climate 28(17), 6938–6959. https://doi.org/10.1175/JCLI-D-14-00754.1
- GCOS. ECV Fire requirements page. https://gcos.wmo.int/site/global-climate-observing-system-gcos/essential-climate-variables/fire
- Gruber, A., Scanlon, T., van der Schalie, R., Wagner, W., Dorigo, W. (2019). Earth Syst. Sci. Data 11, 717–739. https://doi.org/10.5194/essd-11-717-2019
- Gudmundsson, L., et al. (2012). Hydrol. Earth Syst. Sci. 16, 3383–3390. https://doi.org/10.5194/hess-16-3383-2012 (abstract)
- Gutiérrez, J. M., et al. (2019). Int. J. Climatol. 39, 3750–3785. https://doi.org/10.1002/joc.5462 (abstract)
- Kaur, I., Hüser, I., Zhang, T., Gehrke, B., Kaiser, J. W. (2019). Remote Sens. 11(10), 1205. https://doi.org/10.3390/rs11101205
- Lehner, F., Nadeem, I., Formayer, H. (2023). Adv. Stat. Clim. Meteorol. Oceanogr. 9, 29–44. https://doi.org/10.5194/ascmo-9-29-2023
- Lund, R., Beaulieu, C., Killick, R., Lu, Q., Shi, X. (2023). J. Climate 36(23), 8041–8057. https://doi.org/10.1175/JCLI-D-22-0954.1 ; arXiv:2212.02674
- Lund, R., Reeves, J. (2002). J. Climate 15(17), 2547–2554. https://doi.org/10.1175/1520-0442(2002)015<2547:DOUCAR>2.0.CO;2 (metadata)
- Maraun, D. (2013). J. Climate 26(6), 2137–2143. https://doi.org/10.1175/JCLI-D-12-00821.1
- Maraun, D. (2016). Curr. Clim. Change Rep. 2, 211–220. https://doi.org/10.1007/s40641-016-0050-x (not opened)
- Menne, M. J., Williams, C. N. Jr. (2009). J. Climate 22, 1700–1717. https://doi.org/10.1175/2008JCLI2263.1
- Merchant, C. J., et al. (2017). Earth Syst. Sci. Data 9, 511–527. https://doi.org/10.5194/essd-9-511-2017
- Met Office. HadCRUT5. https://www.metoffice.gov.uk/hadobs/hadcrut5/
- Mittaz, J., Merchant, C. J., Woolliams, E. R. (2019). Metrologia 56, 032002. https://doi.org/10.1088/1681-7575/ab1705
- Morice, C. P., et al. (2021). J. Geophys. Res. Atmos. 126, e2019JD032361. https://doi.org/10.1029/2019JD032361 (not opened)
- Reiter, P., Gutjahr, O., Schefczyk, L., Heinemann, G., Casper, M. (2016). Meteorol. Z. 25(1), 85–96. https://doi.org/10.1127/metz/2015/0714 (abstract)
- Ribeiro, S., Caineta, J., Costa, A. C. (2016). Phys. Chem. Earth 94, 167–179. https://doi.org/10.1016/j.pce.2015.08.007 (not opened)
- Roberts, D. R., et al. (2017). Ecography 40, 913–929. https://doi.org/10.1111/ecog.02881
- Venema, V. K. C., et al. (2012). Benchmarking homogenization algorithms for monthly data. Clim. Past 8, 89–115. https://doi.org/10.5194/cp-8-89-2012
- Wang, X. L. (2008a). J. Appl. Meteor. Climatol. 47, 2423–2444. https://doi.org/10.1175/2008JAMC1741.1 (metadata)
- Wang, X. L. (2008b). J. Atmos. Oceanic Technol. 25, 368–384. https://doi.org/10.1175/2007JTECHA982.1 (metadata)
- Wang, X. L. (2009). A quantile matching adjustment algorithm for Gaussian data series. Environment Canada technical note. https://etccdi.pacificclimate.org/RClimDex/QMadj_Gaussian.pdf
- Wang, X. L., Chen, H., Wu, Y., Feng, Y., Pu, Q. (2010). J. Appl. Meteor. Climatol. 49(12), 2416–2436. https://doi.org/10.1175/2010JAMC2376.1 (metadata)
- Unreviewed: GitHub pull request "MODIS-to-VIIRS harmonisation (quantile mapping + LightGBM)", Adedamola18/nasa-flame-sense #2, merged October 2026. https://github.com/Adedamola18/nasa-flame-sense/pull/2
