# Anomaly and percentile indices, and how existing fire dashboards compare the present with history

## Summary

These methods express a month relative to its own record instead of converting one sensor's units into another's. Examples are a standardised anomaly (z-score: the departure from the mean divided by the standard deviation), a percentile rank, a ratio to the calendar-month median, and a drought-style standardised index made by fitting a probability distribution. The drought literature behind the last of these assumes long records and few zeros. The multi-sensor soil-moisture and vegetation records reviewed here do not blend raw per-sensor anomalies. They first rescale every sensor to a reference and then compute anomalies. Fire dashboards use the simple forms. Global Forest Watch (GFW) classifies a period by standard deviations from the mean of earlier years. Brazil's national space research institute (INPE) and the European Forest Fire Information System (EFFIS) show the current value against a mean and a minimum-to-maximum range. None of the dashboards reviewed merges MODIS (Moderate Resolution Imaging Spectroradiometer) and VIIRS (Visible Infrared Imaging Radiometer Suite) hotspot counts into one baseline. These methods fit the team's whole-box scale reasonably well. They break down below about 100 km radius, where most MODIS months are zero.

## Methods

| Method | How it works | Where used | Data needed | Main assumption | Known failure mode |
|---|---|---|---|---|---|
| Z-score against the same period in earlier years | (current − mean) / standard deviation, labelled as unusually low, low, normal, high or unusually high at ±1 and ±2 standard deviations | GFW fire-alert widget (source code, [wri/gfw](https://github.com/wri/gfw)) | Counts per period for each year | Counts are roughly symmetric and the variance is meaningful | Skewed counts. In the GFW code a standard deviation of zero returns 0, which is labelled "normal". |
| Mean with a minimum-to-maximum band | Current value plotted against the mean and the range of the reference years | EFFIS through the 2025 European State of the Climate report (ESOTC); INPE statistics page | Same | The reference years are comparable with the current year | One extreme year sets the band. The band widens as years are added. |
| Ratio or percent difference from the calendar-month mean | "27% below the June mean (2010–2024)" | INPE June 2026 bulletin | Same | The mean is a fair norm | Undefined when the mean is zero. The mean is dominated by a few big years. |
| Ratio to the calendar-month median | The current month divided by its median | Required wording of the challenge. No fire use found. | Same | The median is non-zero | The median is zero for small areas. |
| Empirical percentile rank (with mid-rank or randomised ties) | Rank the month among the baseline months. Tied zeros get the mid-rank, or a random value inside their probability step. | Randomised quantile residuals ([Dunn and Smyth 1996](https://doi.org/10.1080/10618600.1996.10474708), not opened). No fire use found. | Same | The baseline years can be exchanged | Coarse with 10–14 years. Cannot go beyond the observed extremes. |
| Nonparametric standardised indicator | Empirical plotting position, then inverse normal | [Farahmand and AghaKouchak 2015](https://doi.org/10.1016/j.advwatres.2014.11.012) (metadata only) | Same | Same as a percentile | Same as a percentile |
| Standardised index from a fitted distribution (SPI family; SPI is the Standardized Precipitation Index) | Fit a gamma or similar distribution to the non-zero values of one calendar month, add the share of zeros q as H(x) = q + (1 − q)G(x), then convert to a normal score | Drought monitoring ([WMO 2012](https://www.droughtmanagement.info/literature/WMO_standardized_precipitation_index_user_guide_en_2012.pdf); [Stagge et al. 2015](https://doi.org/10.1002/joc.4267); [Pieper et al. 2020](https://doi.org/10.5194/hess-24-4541-2020)) | Same, 20–30 years or more | A continuous, smooth distribution | Unstable tails with short records. Pieper et al. compute the index only where zeros are below 34%. |
| Rescale to a reference, then compute anomalies | Match each sensor's cumulative distribution function (CDF matching) or a ratio over the overlap to a reference, then compute anomalies or merge | ESA CCI soil moisture ([Gruber et al. 2019](https://doi.org/10.5194/essd-11-717-2019)); [Reichle and Koster 2004](https://doi.org/10.1029/2004GL020938); Iberian vegetation index ([Franquesa et al. 2025](https://doi.org/10.5194/essd-17-5885-2025)) | An overlap period | The overlap represents the whole record | Franquesa et al. rejected quantile mapping because it reduced variability and trend consistency. Where sensors do not overlap, the method assumes no trend across the gap. |
| Fixed reference period with frozen parameters | Fit once on a fixed set of years and reuse the parameters for new months | Franquesa et al. 2025 (1981–2023) | Same | The climate and the sensors in the reference period are stable | Mixes sensors of different quality within one reference distribution |

ESA CCI is the European Space Agency's Climate Change Initiative.

## How each would map onto MODIS and VIIRS hotspots

**Z-score, as GFW does it.** For each area and calendar month, compute the mean and standard deviation over the same sensor's earlier years, then label the month at ±1 and ±2 standard deviations. GFW shows each dataset only against its own history, back to 2012 for VIIRS and 2001 for MODIS. The steps are simple, and nothing beyond the team's point rows is needed. This method avoids the 4.1-to-1 level difference between the sensors. It does not avoid Terra's 2026 daytime drop to about half of its expected level when a MODIS month is compared with MODIS history. Fire-season counts are heavily skewed, so one year such as 2017 or 2021 inflates the standard deviation. Where every baseline month is zero, as at a 10 km radius in 91% of fire-season months, the GFW code labels a non-zero month "normal". Effort: hours.

**Percentile rank or ratio to the median.** Rank the current month among the same calendar month in the baseline years, using a mid-rank convention for ties. The team has measured that each sensor ranks months almost identically against its own history (rank correlation 0.97). They give the same five-class label in only 71% of fire-season months, and in 44% of near-normal months. Changing the baseline years changes 8–21% of labels. The MODIS median is zero for most months below about 100 km radius. There the median ratio is undefined, and the percentile rank collapses to a few tied classes. The team's measured fallbacks for small areas are an enclosing larger area, a season, presence or absence, or the VIIRS-only record. Effort: hours.

**Standardised index from a fitted distribution.** Fit a gamma distribution to the non-zero monthly counts, with a zero fraction q. The requirement of 20–30 or more years in the WMO guide is not met by VIIRS (14 years) or by stable-orbit MODIS (2000/2002 to 2021). Small areas exceed the 34% zero limit that Pieper et al. used. The index would add the precision of a fitted model without adding information, since the team's data are discrete and skewed. Effort: about a day.

**Rescale, then compute anomalies (overlap ratio or CDF matching).** Scale MODIS months to VIIRS using the 2012–2021 overlap, then compute one anomaly series reaching back to 2000. This is the only option here that gives one baseline before 2012. It inherits the measured monthly scatter of 14–30% and the drift problem. It cannot restore the 16–50% of months that MODIS missed at 10–100 km. CDF matching of zero-heavy counts spreads tied zeros across a range of values. The team has the overlap data. Effort: a ratio takes hours. CDF matching takes about a day or more.

**Fixed reference period with frozen parameters.** Freeze the baseline statistics so that past labels stop changing each month. Suomi NPP ended on 2 November 2026, so future VIIRS months will come from NOAA-20 and NOAA-21. The team measured them at 0.99 and 0.97 of Suomi NPP. Effort: hours.

**Options for a baseline before 2012, and what each assumes.** (1) Compare MODIS months with MODIS history. This assumes MODIS is stable, which is false for Terra by day in 2026, and MODIS ends in 2027. (2) Compare VIIRS months with VIIRS history from 2012. This has no history before 2012. (3) Use per-sensor anomalies spliced or averaged across sensors. This assumes the anomaly does not depend on the sensor. That assumption is supported only by the team's 0.97 rank correlation and 71% class agreement, with no published precedent found. (4) Rescale, then use one baseline. This assumes the overlap ratio holds across time, activity level and area size. (5) Fall back to a larger area. This assumes the larger area's anomaly describes the small area.

## Not applicable, and why

- Seasonal-cycle removal by a moving window, as for soil-moisture anomalies, assumes a continuous daily field. Hotspots are sparse events.
- Weighting by triple collocation needs three independent, collocated estimates and many samples. Gruber et al. did not merge before 2007 because the method is susceptible to small samples.
- The spatial-window CDF estimate of Reichle and Koster assumes a continuous field that is similar between neighbours. It is untested for fire counts.
- The 30-year standard climatological normal is impossible with these records.

## Unconfirmed

- The content of Farahmand and AghaKouchak 2015 (the Gringorten plotting position) and of Dunn and Smyth 1996 was not read. Only the bibliographic metadata were confirmed through Crossref.
- For Wu et al. 2005 ([doi:10.1002/joc.1142](https://doi.org/10.1002/joc.1142)), only the metadata were confirmed. I could not re-open the abstract that the draft cited.
- Stagge et al. 2015 was read only as its abstract (through Crossref).
- Which satellite feeds INPE's reference series before Aqua, given that the series starts in 1998, is not confirmed. So is whether INPE changed its reference after Aqua began to drift.
- I could not render the Canadian Wildland Fire Information System (CWFIS) reports or the NASA FIRMS (Fire Information for Resource Management System) country pages, which are built with JavaScript. Their baselines and statistics are unknown. The 10-year averages reported in search summaries are not verified.
- The GFW logic comes from the public front-end code on GitHub (develop branch, fetched 14 November 2026). The live site may differ.
- I found no published application of SPI-style, percentile or z-score indices to hotspot counts in a peer-reviewed paper. I also found no source on blending snow anomalies. Web search ran out partway through this verification.

## Sources

- Dunn, P. K., Smyth, G. K. (1996). Randomized quantile residuals. *J. Comput. Graph. Stat.* 5(3), 236–244. https://doi.org/10.1080/10618600.1996.10474708
- EFFIS data in Copernicus Climate Change Service, *European State of the Climate 2025*, Wildfires, Fig. S6.3 ("the average for the 2006–2024 reference period and the minimum to maximum range"). https://climate.copernicus.eu/esotc/2025/wildfires
- Farahmand, A., AghaKouchak, A. (2015). *Adv. Water Resour.* 76, 140–145. https://doi.org/10.1016/j.advwatres.2014.11.012
- Franquesa, M., et al. (2025). Near-real-time vegetation monitoring and historical database (1981–present) for the Iberian Peninsula and the Balearic Islands. *Earth Syst. Sci. Data* 17, 5885–5902. https://doi.org/10.5194/essd-17-5885-2025
- Garcia, R., Pivetta, M. (2019). Como monitorar o fogo. *Pesquisa FAPESP* 284. https://revistapesquisa.fapesp.br/como-monitorar-o-fogo/ (INPE uses Aqua's afternoon pass. The article says counts are valid "para intervalos maiores que 10 dias".)
- Global Wildfire Information System (GWIS) applications page ("the average of the last 10 years"; separate counts of MODIS and VIIRS thermal anomalies; the Country Profile covers 2002–2019 and uses MCD64A1 and GlobFire). https://gwis.jrc.ec.europa.eu/applications
- GFW fire-alerts widget code: `components/widgets/utils/data.js` (`getPeriodVariance`, `getStatsData`) and `components/widgets/fires/fires-alerts/selectors.js`. https://github.com/wri/gfw
- Gruber, A., Scanlon, T., van der Schalie, R., Wagner, W., Dorigo, W. (2019). *Earth Syst. Sci. Data* 11, 717–739. https://doi.org/10.5194/essd-11-717-2019
- INPE (2026). Boletim Infoqueima, June 2026. https://www.gov.br/inpe/pt-br/assuntos/ultimas-noticias/boletim-infoqueima-apresenta-panorama-das-queimadas-e-do-risco-de-fogo-no-brasil-em-junho-de-2026
- INPE country statistics page (series from 1998; the current year is compared with the minimum, mean and maximum, which exclude the current year). https://data.inpe.br/queimadas/estatisticas/?tipo=paises&item=brasil
- Pieper, P., Düsterhus, A., Baehr, J. (2020). *Hydrol. Earth Syst. Sci.* 24, 4541–4565. https://doi.org/10.5194/hess-24-4541-2020
- Reichle, R. H., Koster, R. D. (2004). Bias reduction in short records of satellite soil moisture. *Geophys. Res. Lett.* 31(19). https://doi.org/10.1029/2004GL020938
- Ruiz, S., Lyons, K. (2020). GFW blog on wildfire trends. https://globalnaturewatch.org/blog/data-and-tools/wildfire-trends-gfw-fire-data/
- Stagge, J. H., Tallaksen, L. M., Gudmundsson, L., Van Loon, A. F., Stahl, K. (2015). *Int. J. Climatol.* 35(13), 4027–4040. https://doi.org/10.1002/joc.4267
- WMO (2012). *Standardized Precipitation Index User Guide*, WMO-No. 1090 (prepared with M. Svoboda, M. Hayes, D. Wood). https://www.droughtmanagement.info/literature/WMO_standardized_precipitation_index_user_guide_en_2012.pdf
- Wu, H., Hayes, M. J., Wilhite, D. A., Svoboda, M. D. (2005). *Int. J. Climatol.* 25(4), 505–520. https://doi.org/10.1002/joc.1142
