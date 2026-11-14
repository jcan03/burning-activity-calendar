# Latent-state models and index splicing for series built from several sources

## Summary

This family treats each sensor's monthly hotspot count as a noisy, rescaled view of one unobserved ("latent") level of burning activity, and estimates each sensor's scale factor and noise from the months in which sensors overlap. It also covers the simpler way official statistics join index series across a change of method: rescale the new series to the old one over an overlap period ("chain-linking" or "splicing"). These methods are well established in economics, survey statistics, ecology and soil-moisture remote sensing. We found no published use with fire or other hazard counts from several satellites. The closest fire work fuses smoke optical depth, not counts. The ideas carry over to the team's problem, but none of them removes the main measured limits: missing MODIS detections at small areas, scatter between sensors in single months, and Terra's 2026 daytime drop. The extra things this family offers are a likelihood that handles counts and zero months, joint use of all overlaps, intervals, and, in the state-space form, a factor that can change over time.

## Methods

| Method | How it works | Where used | Data needed | Main assumption | Known failure mode |
|---|---|---|---|---|---|
| Dynamic factor model (DFM) with missing data, fitted by the expectation-maximisation (EM) algorithm | Each series equals a loading times one or a few shared latent factors plus its own noise. A Kalman smoother fills the factors and any missing cells, so a series that starts late or stops is just a run of missing values. | Euro-area GDP nowcasting and backdating ([Bańbura and Modugno 2014](https://doi.org/10.1002/jae.2306); [working paper](https://www.ecb.europa.eu/pub/pdf/scpwps/ecbwp1189.pdf)). Implemented in statsmodels `DynamicFactorMQ`. | Aligned monthly series. NaN where a sensor did not fly. | Gaussian, stationary series, standardised to mean 0 and variance 1. Noise independent across series. | Not designed for skewed, zero-heavy counts. The paper checks its GDP backdating only by eye ("seem to capture well", Figure 2). |
| Integrated hierarchical count model | One latent abundance per place and time. Each data source has its own Poisson or negative-binomial observation model with its own detection rate. | Wildlife counts plus distance sampling ([Gilbert et al. 2024](https://doi.org/10.1002/ecy.4326)). Review: [Zipkin and Saunders 2018](https://doi.org/10.1016/j.biocon.2017.10.017) (metadata only). | Counts per source, per place and per time step. | Sources are conditionally independent given the latent abundance. Detection ratios are stable. | Intervals are too narrow when sources share errors. The detection rate is confounded with abundance unless one source is fixed or overlaps exist. |
| Structural time series with an intervention (level shift) | A latent trend plus a one-off level shift at the method change. The shift is estimated from the series itself, from a parallel run, or from both. | Labour force survey redesigns in Australia ([Zhang, van den Brakel and Tam 2019](https://doi.org/10.1080/24754269.2019.1677085)) and the Netherlands ([van den Brakel and Krieg 2015](https://www150.statcan.gc.ca/n1/pub/12-001-x/2015002/article/14231-eng.htm)). | A long series spanning the break, ideally with a period of parallel running. | The break is a fixed shift, constant over time. | Shift and genuine change are confounded when there is no parallel run. |
| Triple collocation | With three products of the same quantity, the products' covariances give each one's scale and error variance without needing a reference truth. Weighted merging follows. | Soil moisture ([Kim, Dong and Sharma 2021](https://doi.org/10.3389/frwa.2021.693172); [Gruber et al. 2017](https://doi.org/10.1109/tgrs.2017.2734070)). | Three collocated series, usually anomalies with the seasonal cycle removed. | Errors are uncorrelated between products and with the truth. | Fails when products share error sources. Kim et al. note that this is why near-identical products are normally not put in one triplet. |
| Chain-linking with an overlap period | Rescale the new index by the ratio of new to old in a link period (one month, one quarter, or one year). Several changes multiply their link factors. | [Eurostat short-term statistics](https://ec.europa.eu/eurostat/statistics-explained/index.php?title=Short-term_business_statistics_and_(annual)_chain_linking); [ONS 2020](https://www.ons.gov.uk/economy/inflationandpriceindices/articles/chainlinkinginbusinessprices/2020-07-20). | An overlap period between the two series. | The ratio in the link period holds for all other periods. | A short link period carries its noise into the whole series. Link factors "stack multiplicatively" (ONS), so their errors compound. |
| Splicing over many link periods (movement, window, half and mean splice) | Choose which period(s) in a rolling overlap to link on. Mean splice uses the geometric mean over all link periods, which is the least-squares solution on log differences. | Consumer price indices at Statistics Netherlands ([Chessa 2023](https://www.isi-next.org/media/abstracts/ottawa-2023_772473ea5ae1bbe86bed356779241963.pdf)). | Repeated overlaps. | Same as chain-linking. | Movement splice is "sensitive to drift"; mean splice "may suffer from window censoring effects". Choosing the link period optimally helps little. |

## How each would map onto MODIS and VIIRS hotspots

**Chain-linking with a long overlap.** Steps: compute the NOAA-20/Suomi NPP and NOAA-21/Suomi NPP ratios and the Terra+Aqua/Suomi NPP ratio over the whole stable-orbit overlap (February 2012 to December 2021), then multiply the links. The team's measured scatter of 15–30% in single months rules out the Eurostat convention of linking on one month (December) or one quarter. A ratio of sums over many months is the count analogue of Chessa's mean splice. The errors compound, but the VIIRS links (0.99 and 0.97, within a few percent) add little to the MODIS link (0.242, interval 0.237–0.28). This method fixes the difference in level between sensors. It fixes neither the scatter in single months nor the small-area zeros nor Terra's drift. The team has all the data it needs. Effort: hours.

**Count model with a shared monthly activity (the simplest member of this family).** For the user's area, each count n(sensor s, day or night k, month m) follows a negative-binomial distribution with mean exp(a_m + b_sk). Here a_m is the log activity in month m and b_sk is a log factor for each sensor and time of day. Suomi NPP is fixed as the reference, so its factors are 0. Months in which a sensor did not fly simply have no rows. The ten factors would be fitted on the whole study box, where counts are large. With the factors held fixed, a_m for a small user area is a one-parameter fit per month (statsmodels `NegativeBinomial` with `offset`).

Over a fixed factor, it adds:
- likelihood-based intervals on each month;
- zero MODIS months used properly instead of an undefined ratio;
- day and night factors at no extra cost;
- all overlaps fitted at once.

It does not:
- remove chaining, because the MODIS factor is still identified only through Suomi NPP and NOAA-20 in 2012–2021;
- create the MODIS detections that are missing in a third or more of months below about 50 km, so before 2012 its intervals at small areas will be very wide;
- remove the additive Kamloops static source, which must be removed first;
- capture the activity dependence of the ratio (quiet months run 25–50% higher).

Treating the three VIIRS satellites as independent looks of the same fires ignores their measured ±15–20% shared scatter, so the intervals will be too narrow. This design is a synthesis from the ecological pattern, not a published fire method. Effort: a few hours. A Bayesian version with a smoothness prior on a_m would take about a day.

**State-space model with a time-varying factor.** This is a dynamic regression of log MODIS counts on log VIIRS counts, with the coefficient following a random walk. It is the only member of the family that could track Terra's daytime decline (0.95 of expected in 2022, 0.46 in 2026), because VIIRS overlaps the whole drift period. The intervention model of Zhang et al. is its one-break special case. statsmodels `UnobservedComponents` can put regression coefficients in the state vector, but its documentation describes recursive least squares, not a random walk. A random-walk factor would need custom state-space code. Logs need care for zero months. Effort: a day or more.

**Dynamic factor model on log(1 + count).** `DynamicFactorMQ` accepts NaN for sensors that were not flying and fits by EM. However, it standardises each series over its own window: Terra from 2000, NOAA-21 only from 2023. A late sensor's mean is therefore set by whichever fire years it happened to see (2017, 2018 and 2021 dominate the record). It also assumes stationarity, which a strongly seasonal series violates, and the many zeros at small areas break the Gaussian assumption. The team could produce a run in hours, but justifying it would be hard.

## Not applicable, and why

- **Latent Gaussian count factor model** ([Kim, Düker, Fisher and Pipiras, arXiv:2307.10454](https://arxiv.org/abs/2307.10454)): research code only, with particle filtering. It would take days.
- **Shrinkage (maximum a posteriori) version of the dynamic factor model** ([Spånberg 2022, arXiv:2207.01922](https://arxiv.org/abs/2207.01922)): adds priors to a model that already fits poorly here.
- **Triple collocation:** the three VIIRS satellites see the same fires with the same algorithm, which violates its independent-error assumption. It also needs anomaly fields that are not dominated by zeros.
- **Physics-informed fusion of satellite smoke data** ([Wei et al. 2022, arXiv:2206.11766](https://arxiv.org/abs/2206.11766)): it models continuous aerosol optical depth fields with an advection-diffusion model, not counts.
- **Hierarchical co-kriging for calibration between satellites** ([Cheng et al., arXiv:2004.01341](https://arxiv.org/abs/2004.01341)): it needs continuous radiance fields on a shared spatial grid.
- **Detection likelihoods for single fires** ([Haley et al. 2018, arXiv:1808.03318](https://arxiv.org/abs/1808.03318)): these need a fire-spread model, and per-pixel detections plus non-detections, which the FIRMS rows lack.

## Unconfirmed

- The search budget ran out during verification, so the gaps below could not be closed by further searching, and the search for fire applications could not be repeated.
- Zhang et al. 2019: the metadata and abstract were confirmed, but the full text was blocked (HTTP 403). The draft's page-226 quotation about working on a logarithmic scale is unconfirmed.
- Wei et al. 2022: abstract only. The specific satellites (GOES-16 and GOES-17), the Gibbs or forward-filtering backward-sampling scheme, and the journal submission are unconfirmed.
- Read as abstract or metadata only: Gilbert et al. 2024; Kim et al. 2023; Spånberg 2022; Haley et al. 2018; Cheng et al. 2020; Zipkin and Saunders 2018 (metadata only); Gruber et al. 2016, a triple-collocation review that is probably the best review for that method (metadata only, DOI [10.1016/j.jag.2015.09.002](https://doi.org/10.1016/j.jag.2015.09.002)).
- Graff et al. 2020 ([DOI](https://doi.org/10.1109/tgrs.2020.2968029)) uses Poisson regression on MODIS counts alone, not on several sensors. Only the abstract was read.
- Not opened, so dropped: Podschwit et al. 2018, Strebel 2022, Kéry 2024, the DynCount package, the Eurostat HICP manual (its link rules), and the R packages hicp and PriceIndices.
- No implementation was run, and none of these models has been tested on hotspot data.

## Sources

- Bańbura, M., Modugno, M. (2014). Maximum likelihood estimation of factor models on datasets with arbitrary pattern of missing data. *Journal of Applied Econometrics* 29(1), 133–160. https://doi.org/10.1002/jae.2306 (ECB Working Paper 1189, 2010: https://www.ecb.europa.eu/pub/pdf/scpwps/ecbwp1189.pdf)
- statsmodels documentation: DynamicFactorMQ, NegativeBinomial and UnobservedComponents. https://www.statsmodels.org/stable/
- Spånberg, E. (2022). arXiv:2207.01922.
- Kim, Y., Düker, M.-C., Fisher, Z. F., Pipiras, V. arXiv:2307.10454 (v3, 2025).
- Gilbert, N. A., et al. (2024). *Ecology*. https://doi.org/10.1002/ecy.4326
- Zipkin, E. F., Saunders, S. P. (2018). *Biological Conservation* 217, 240–250. https://doi.org/10.1016/j.biocon.2017.10.017
- Zhang, X., van den Brakel, J., Tam, S.-M. (2019). *Statistical Theory and Related Fields* 3(2), 224–238. https://doi.org/10.1080/24754269.2019.1677085
- van den Brakel, J. A., Krieg, S. (2015). *Survey Methodology* (Statistics Canada 12-001-X). https://www150.statcan.gc.ca/n1/pub/12-001-x/2015002/article/14231-eng.htm
- Kim, S., Dong, J., Sharma, A. (2021). *Frontiers in Water* 3. https://doi.org/10.3389/frwa.2021.693172
- Gruber, A., Dorigo, W., Crow, W., Wagner, W. (2017). *IEEE Transactions on Geoscience and Remote Sensing* 55(12), 6780–6792. https://doi.org/10.1109/tgrs.2017.2734070
- Gruber, A., et al. (2016). *International Journal of Applied Earth Observation and Geoinformation* 45, 200–211. https://doi.org/10.1016/j.jag.2015.09.002
- Eurostat Statistics Explained. Short-term business statistics and (annual) chain linking. (Link in the Methods table.)
- Office for National Statistics (2020). Chain linking in business prices. (Link in the Methods table.)
- Chessa, A. G. (2023). Controlling drift when extending index series of consumer price change over time. Statistics Netherlands, 64th ISI World Statistics Congress. (Link in the Methods table.)
- Wei, G., et al. (2022). arXiv:2206.11766. Cheng, S., et al. arXiv:2004.01341. Haley, J., et al. (2018). arXiv:1808.03318.
- Graff, C. A., et al. (2020). *IEEE Transactions on Geoscience and Remote Sensing* 58(7), 4837–4851. https://doi.org/10.1109/tgrs.2020.2968029
