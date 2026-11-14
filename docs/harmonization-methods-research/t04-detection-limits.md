# Detection-limit, omission and sensor-emulation approaches

## Summary

These methods reconcile a sensitive sensor with a less sensitive one. They do it by modelling what each sensor can and cannot detect. Sometimes they go further and simulate what the coarse sensor would have recorded when looking at the same fires. The coarse sensor here is MODIS (Moderate Resolution Imaging Spectroradiometer, 1 km pixels). The sensitive one is VIIRS (Visible Infrared Imaging Radiometer Suite, 375 m pixels). Fire radiative power (FRP, the heat a fire gives off, in megawatts, MW) has been used this way in several published studies. The clearest is an observation operator by Sofiev and Kouznetsov (2026). It applies MODIS detection limits to VIIRS fire pixels, but it was validated only on FRP totals and never on hotspot counts. The detection limits it needs are published and can be applied to FIRMS (Fire Information for Resource Management System) point rows. However, the method also needs MODIS scan geometry, cloud state and overpass timing, and the rows contain none of these. No method in this family can recreate fires that MODIS never recorded. For the team the fit is partial: these methods give a physical explanation of the measured MODIS/VIIRS ratio, and a rough "MODIS-equivalent from VIIRS" can be built in hours. Its accuracy for counts is untested.

## Methods

| Method | How it works | Where used | Data needed | Main assumption | Known failure mode |
|---|---|---|---|---|---|
| Probability of detection against reference imagery | Fine-resolution fire maps (ASTER, the Advanced Spaceborne Thermal Emission and Reflection Radiometer, 30 m; or Landsat 30 m) are compared with MODIS fire flags. A logistic regression then gives detection probability against fire size or pixel area. | [Morisette et al. 2005](https://doi.org/10.1175/EI141.1) (Brazil). [Csiszar et al. 2006](https://doi.org/10.1109/TGRS.2006.875941) (Siberia; 50 % detection at about 60 ASTER fire pixels, against about 45 in Brazil). [Schroeder et al. 2011](https://www.isprs.org/proceedings/2011/ISRSE-34/211104015Final00178.pdf). [Hawbaker et al. 2008](https://doi.org/10.1016/j.rse.2007.12.008) (United States; 50 % detection at 105 ha for Terra and Aqua together, 195 ha for Aqua, 334 ha for Terra). [Zheng et al. 2026](https://doi.org/10.3390/rs18101650) (detection of fires under 30 MW: MODIS 26.8 %, VIIRS 44.3 %). | Coincident reference imagery | The reference sees every fire | Results depend on the region. Heavy smoke hides flaming fires (Csiszar 2006). Zheng used a matching window of one day. |
| Pixel detection limit and observation operator | The detection limit is linear in pixel area: D = λA + μ. A logistic curve gives the expected observed FRP. The MODIS operator is applied to each VIIRS fire pixel, and the reverse. | [Sofiev & Kouznetsov 2026](https://doi.org/10.5194/gmd-19-10123-2026). Aqua against Suomi NPP, 2020: totals of 128 and 177 TW became 88 and 106 TW after the operators, a 20 % gap that a diurnal factor of 1.2 closed. | Pixel FRP, pixel area (from scan angle), day or night | Limits fitted to histograms of detected FRP stand in for true detection | Validated on granule FRP totals only. The paper's abstract (3.7 MW at night at nadir, 40 MW in a daytime side view) and conclusions (5.7 and 3.7 MW) do not match its tables (about 5.0 and 5.4 MW at 1 km²). |
| Grid-cell operator with a cloud term | A cell's detection limit is set by its strongest pixel and rises steeply when less than about 30 % of the cell was observed clear. | Sofiev & Kouznetsov 2026, Eqs. 8 to 11 | As for the pixel operator, plus the fraction of each cell flagged clear or cloudy | The pixel state flags are known | Needs cloud and missing-data flags |
| Footprint matching | All VIIRS pixels inside a MODIS footprint, within 5 minutes, are summed and compared. | [Fu et al. 2020](https://doi.org/10.3390/rs12182870) (Northeast Asia). Zheng et al. 2026 (global, with corrections binned by view zenith angle, VZA). | Swath geolocation, acquisition time to the second, pixel size | The overlap is computed correctly | Summed VIIRS FRP was 0.72 of MODIS FRP (Fu). In forest, 35 % of MODIS fire pixels had no VIIRS pixel. |
| Frequency-magnitude extrapolation | A power law is fitted to the frequency distribution of FRP above the detection limit and extended below it to estimate what was missed. | [Sperling et al. 2020](https://doi.org/10.3390/fire3020011) (cerrado; about 35 % of FRP missed by Aqua). [Kumar et al. 2011](https://doi.org/10.1029/2011JD015676). Freeborn et al. 2008 (SEVIRI, the geostationary Spinning Enhanced Visible and Infrared Imager, against MODIS). | FRP of detected pixels | FRP follows a single power law below the limit | Least-squares fits on log-log plots give biased exponents and do not test the power-law form ([Clauset et al. 2009](https://doi.org/10.1137/070710111)). Sperling's data show a possible break near 10 MW. |
| Regression emulation toward a reference sensor | Summed FRP from one sensor in grid cells is regressed onto the reference sensor's sums, using only the reference's central swath. | [Wooster et al. 2015](https://doi.org/10.5194/acp-15-13217-2015) (SEVIRI to MODIS in 5° cells; regional factors 1.46 to 2.06) | Coincident gridded sums | A stable ratio for each region | A power-law form was "no more skilful than a linear formulation" (Wooster 2015). |
| Pixel-degradation simulation | Fine imagery is degraded to coarser pixels and the detection algorithm is run again. | Sperling et al. 2020 (50 m airborne data degraded to 1 km). [Schroeder et al. 2014](https://doi.org/10.1016/j.rse.2013.12.008) (simulated fires for VIIRS) | Radiances | The fine data represent the scene | Not possible with hotspot rows |

Published limits differ by definition. The 50 % point of a logistic fit gives about 5 MW for MODIS at 1 km² (Sofiev; Sperling gives 5 to 8 MW). The smallest FRP actually observed gives 4.1 MW at nadir and more than 33.6 MW at the swath edge for MODIS, against 1.4 to 2.2 MW for VIIRS (Zheng). Fu quotes 2.5 MW at nadir and 17 MW at the edge for MODIS. For MODIS Collection 5, Freeborn et al. (2014) report about 10 MW beyond a 33° scan angle and about 50 MW at the swath edges. From Sofiev's table coefficients, VIIRS at nadir is about 2.3 MW by day and 0.54 MW at night. That makes the gap between the sensors about 2-fold by day and about 10-fold at night.

## How each would map onto MODIS and VIIRS hotspots

**Pixel operator ("MODIS-equivalent from VIIRS").**

*Steps:* group VIIRS rows by satellite, date and acquisition time; snap them to cells of about 1 km; sum FRP in each cell; and score each cell with Sofiev's logistic curve. The limits are D = 4.44A + 0.52 MW by day and 4.43A + 1.01 MW at night, where A is the MODIS pixel area. Summing the scores gives an expected count.

*What it would fix:* it gives a physical reason for the measured day and night ratios of 0.34 and 0.18 (0.20 and 0.055 for Aqua against Suomi NPP). It also continues past 2027 without needing a model of the MODIS orbit drift.

*What it would not fix:*
- FIRMS rows hold no scan angle for a MODIS pixel that does not exist, so A has to be assumed, for example 1 km² at nadir or drawn from the `scan` values in MODIS rows.
- They hold no cloud mask and no record of where MODIS looked. The MODIS Collection 6 guide warns that fire-pixel lists contain "no information about cloud cover or missing data" ([Giglio et al. 2018](https://modis-fire.umd.edu/files/MODIS_C6_Fire_User_Guide_B.pdf)).
- VIIRS passes at about 12:40 and 02:10 local time, so it can stand in only for Aqua. Terra flew near 11:00, and since 2023 its daytime pass has drifted to 09:20. Emulating it needs a diurnal model.
- Summed VIIRS FRP is lower than MODIS FRP (slope 0.72).
- The team found that FRP bridges the sensors worse than counts once night passes are included. A threshold on FRP brings that noise into the count.

*Testing:* the team has all the data needed for a rough version. It could be tested by comparing emulated and actual Aqua counts for 2012 to 2021. That test is a suggestion and has not been published.

*Effort:* hours for a rough version, and a day with the hindcast test.

**Frequency-magnitude cross-check.** Take the share of VIIRS hotspots with FRP above a MODIS-level limit (about 5 MW by day) and compare it with the measured count ratio. This needs only FRP, which the rows have, and an empirical exceedance curve, so no power-law fit is required. It checks the method and does not correct anything. The ratios have to be split by day and night, because the limits differ about 10-fold between them. Effort: hours.

**Footprint matching for calibration.** Pair Aqua and Suomi NPP rows that fall within 5 minutes of each other, using the row positions and the `scan` and `track` pixel sizes. Use the pairs to check the limit D in the Interior. FIRMS says `scan` and `track` "reflect actual pixel size". It does not give the precision of the acquisition time, so the 8-second duplicate rule cannot be applied. Footprints would be approximate because FIRMS gives only pixel centres. Fu's 35 % of MODIS pixels with no VIIRS match includes MODIS false detections: in forest, MODIS commission errors were about 65 % at 2 to 4 MW. Effort: a day.

**What none of these fixes.** Below a radius of about 50 km, MODIS recorded nothing in a third or more of the months in which VIIRS saw fire. An emulator turns VIIRS months into similarly sparse MODIS-like months, so the comparison becomes like for like. It adds no information to the MODIS history. Going the other way, from MODIS to VIIRS-equivalent, would need extrapolation below the detection limit. That extrapolation can scale totals up, but it cannot fill a month in which MODIS recorded nothing. The emulator also cannot reproduce the Kamloops static source, which appears only in VIIRS, so that source must be removed first.

## Not applicable, and why

- Validation against reference imagery: the team has no ASTER or Landsat fire maps. These studies are useful only as a sanity check. Hawbaker's result that Terra is less sensitive than Aqua agrees with the team's day ratio of Terra to Aqua (0.72).
- The grid-cell operator with its cloud term: it needs a retrieved-area fraction for each cell, and the team has no cloud mask.
- Pixel-degradation simulation: it needs radiances.
- The geostationary regression in the style of SEVIRI: in practice it is the overlap-period ratio already measured by the team, and it adds nothing new.
- The VIIRS 750 m product, which uses an algorithm built to match MODIS: it is not distributed in FIRMS (see r01).

## Unconfirmed

- Read only as abstracts or records: Csiszar et al. 2006 (index record and search summary), Kumar et al. 2011 (repository record), and the Hawbaker 2008 journal article (the dissertation chapter was read in full).
- Sofiev's coefficient tables disagree with the abstract and conclusions. The table coefficients are used above. The constant A₀ in the slope (Eq. 6) was not found in the tables, so slope values were not computed. The unit printed in Table 3 looks like a typographical error, but this is not confirmed.
- Not opened, and seen only as citations: Schroeder et al. 2010 and Roberts & Wooster 2008 (a 9 to 11 MW threshold, cited by [Laurent et al. 2019](https://doi.org/10.5194/bg-16-275-2019)); Schultz et al. 2008 (7 to 10 MW for MODIS Collection 4, cited by Sofiev); and Maier et al. 2013 (about 55 MW at the edge for Collection 5, cited by Sofiev).
- The precision of FIRMS acquisition times is not documented on the attribute page.
- The review by [Wooster et al. 2021](https://doi.org/10.1016/j.rse.2021.112694) was read only for its omission section, which names cloud or smoke, fires not burning at overpass, and FRP below the limit. No count-level validation of any emulator was found.

## Sources

- Clauset A., Shalizi C.R., Newman M.E.J. 2009. SIAM Review 51:661–703. https://doi.org/10.1137/070710111 (abstract)
- Csiszar I., Morisette J.T., Giglio L. 2006. IEEE TGRS 44(7):1757–1764. https://doi.org/10.1109/TGRS.2006.875941 (abstract)
- Freeborn P.H. et al. 2008. EGU2008-A-06196. https://meetings.copernicus.org/www.cosis.net/abstracts/EGU2008/06196/EGU2008-A-06196.pdf
- Freeborn P.H., Wooster M.J., Roberts G., Xu W. 2014. Remote Sens. 6:1890–1917. https://doi.org/10.3390/rs6031890
- Fu Y. et al. 2020. Remote Sens. 12(18):2870. https://doi.org/10.3390/rs12182870
- Giglio L., Schroeder W., Hall J.V., Justice C.O. 2018. MODIS C6 Active Fire User's Guide Rev. B. https://modis-fire.umd.edu/files/MODIS_C6_Fire_User_Guide_B.pdf
- Hawbaker T.J. et al. 2008. RSE 112(5):2656–2664. https://doi.org/10.1016/j.rse.2007.12.008. Dissertation: https://geoserver.silvis.forest.wisc.edu/geodata/LabDocuments/PhD6-Dissertations/Hawbaker_Todd_Dissertation_2008.pdf
- Kumar S.S., Roy D.P., Boschetti L., Kremens R. 2011. JGR 116:D19303. https://doi.org/10.1029/2011JD015676 (abstract)
- Laurent P. et al. 2019. Biogeosciences 16:275–288. https://doi.org/10.5194/bg-16-275-2019
- Li F., Zhang X., Kondragunta S. 2020. Remote Sens. 12:1561. https://doi.org/10.3390/rs12101561
- Morisette J.T. et al. 2005. Earth Interactions 9(9). https://doi.org/10.1175/EI141.1
- NASA Earthdata. FIRMS Active Fire Data Attributes. https://www.earthdata.nasa.gov/data/tools/firms/active-fire-data-attributes-modis-viirs
- Schroeder W., Csiszar I., Giglio L., Ellicott E., Justice C. 2011. ISRSE-34. https://www.isprs.org/proceedings/2011/ISRSE-34/211104015Final00178.pdf
- Schroeder W., Oliva P., Giglio L., Csiszar I. 2014. RSE 143:85–96. https://doi.org/10.1016/j.rse.2013.12.008
- Sofiev M., Kouznetsov R. 2026. Geosci. Model Dev. 19:10123–10142. https://doi.org/10.5194/gmd-19-10123-2026
- Sperling S., Wooster M.J., Malamud B.D. 2020. Fire 3(2):11. https://doi.org/10.3390/fire3020011
- Wooster M.J. et al. 2015. Atmos. Chem. Phys. 15:13217–13239. https://doi.org/10.5194/acp-15-13217-2015
- Wooster M.J. et al. 2021. RSE 267:112694. https://doi.org/10.1016/j.rse.2021.112694
- Zheng Y. et al. 2026. Remote Sens. 18(10):1650. https://doi.org/10.3390/rs18101650
