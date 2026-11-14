# Published comparisons and harmonization of MODIS and VIIRS active-fire records

Verified 2026-11-14. Every source below was opened by the verifier unless marked "unconfirmed".

## Answer

No peer-reviewed study was found that builds one continuous MODIS-plus-VIIRS hotspot-count series, or reports a VIIRS-to-MODIS count ratio, for Canadian or boreal forest. Published count comparisons vary widely by product, biome and scan angle: VIIRS 750 m gave about 1.26 times Aqua MODIS detections near nadir and 1.7 times off nadir (global, 2013), while VIIRS 375 m gave about 4.8 times Aqua-plus-Terra MODIS in Punjab cropland; Northeast Asian omission rates imply roughly 1.9 (forest) to 2.8 (low-biomass land) or more. Fire radiative power (FRP, the heat output of the fire in megawatts) is the unit with the most cross-sensor work: summed MODIS FRP runs 20 to 50% below VIIRS depending on grid size, and large boreal fire clusters are the named exception, where VIIRS FRP is about 47% lower. Every published join uses VIIRS as the reference and conditions its correction on scan angle, grid size or region and land cover; none uses one global factor. No study quantifies how the post-2020 MODIS orbit drift changes detection counts, and NASA documents give no merging method.

## Evidence

Terms: *pixel count* is the number of flagged fire pixels; *VZA* is the satellite view zenith angle (0 at nadir, largest at the swath edge); *omission* means a fire seen by one sensor and missed by the other.

| Source | What was compared | Method | Numbers reported (and what they come from) |
|---|---|---|---|
| [Csiszar et al. 2014, JGR Atmos. 119](https://directreadout.sci.gsfc.nasa.gov/publications_documents/Csiszar_et_al_2014_JGR.pdf), doi:10.1002/2013JD020453 | VIIRS 750 m (operational IDPS product, built on MODIS Collection 4) vs Aqua MODIS; global, 15 Feb to 15 Jun 2013 | Pixel counts binned by scan angle | VIIRS about 26% more detections within the central zone (about ±31° scan) and 70% more outside it |
| [Schroeder et al. 2014, RSE 143:85-96](https://earthdata.nasa.gov/s3fs-public/imported/Schroeder_et_al_2014b_RSE.pdf), doi:10.1016/j.rse.2013.12.008 | VIIRS 375 m vs VIIRS 750 m; global, August 2013 | Co-registered pixel counts, day and night separately | 375 m gave 3 times the day pixels and 25 times the night pixels. MODIS only discussed qualitatively (Brazil case) |
| [VIIRS C2 375 m User Guide v1.2, June 2025](https://www.earthdata.nasa.gov/s3fs-public/2025-06/VIIRS_C2_AF-375m_User_Guide_1.2.pdf) (Schroeder, Giglio, Hall) | VNP14IMG vs VNP14 (750 m); global, all of 2021 | Pixel counts, day and night | About 3 times more day and 17 times more night pixels; 53% (day) and 85% (night) of 375 m pixels unmatched. States VNP14 "is more comparable to the 1-km Aqua MODIS fire product" and that 375 m vs MODIS differences are "further magnified" by MODIS tropical gaps and off-nadir pixel growth |
| [Fu et al. 2020, Remote Sens. 12(18):2870](https://api.crossref.org/works/10.3390/rs12182870), doi:10.3390/rs12182870 | Aqua MYD14 vs Suomi NPP VNP14IMG; Northeast Asia, 2012-2017 | Near-simultaneous overpasses, duplicates removed, forest vs low-biomass land | MODIS missed 65% (forest) and 83% (low-biomass) of VIIRS fire pixels; VIIRS missed 35% and 53% of MODIS pixels. Monthly total FRP lower from MODIS; for fires both saw, VIIRS FRP lower (abstract only) |
| [Vadrevu and Lasko 2018, Remote Sens. 10(7):978](https://pmc.ncbi.nlm.nih.gov/articles/PMC6108185/), doi:10.3390/rs10070978 | MCD14ML Aqua+Terra vs VNP14IMG; Punjab, India | Annual counts and monthly FRP; Gaussian peak fit of monthly VIIRS FRP sum on MODIS FRP sum, 70/30 split | VIIRS 87,702 fires/yr (mean of 2012-2016) vs MODIS 18,270 (mean of 2003-2016), about 4.8; Aqua alone 13,489, about 6.5. Mean per-pixel FRP Aqua 16.10 MW vs VIIRS 5.25 MW; summed FRP VIIRS 2.25 times MODIS (abstract says 2.5). Monthly FRP r² 0.98; fit r² 0.93 |
| [Li, Zhang, Kondragunta, Csiszar 2018, JGR Atmos. 123(9):4545-4563](https://repository.library.noaa.gov/view/noaa/49896), doi:10.1029/2017JD027823 | MODIS (Aqua, Terra) vs Suomi NPP VIIRS FRP | Fire clusters, continental sums, 1° grids (abstract only) | Cluster FRP "very comparable" except large boreal forest fires, where VIIRS is about 47% smaller; continental sums correlated, VIIRS slightly larger, difference varies by season; 1° grids differ about 20% in fire-prone regions. MODIS depends strongly on VZA, VIIRS does not |
| [Li, Zhang, Kondragunta 2020, Remote Sens. 12(10):1561](https://repository.library.noaa.gov/view/noaa/42501/noaa_42501_DS1.pdf), doi:10.3390/rs12101561 | Aqua MYD14 vs VNP14IMG FRP; Africa, 2017 | 44 days with daytime overpasses within ±5 min; RMA regression; seven grids 0.05° to 5°; median VIIRS/MODIS ratio vs VZA | Daily MODIS FRP at least 42.8% low (Pearson r above 0.95). MODIS low by 14-31% at 0.25°, 40-50% at 0.5°, 69-130% at 5° (rising with VZA); up to about 60% more at swath edge than nadir for grids above 1°. Swath gaps cut monthly MODIS FRP 12.5% |
| [Zheng et al. 2026, Remote Sens. 18(10):1650](https://mdpi-res.com/d_attachment/remotesensing/remotesensing-18-01650/article_deploy/remotesensing-18-01650.pdf), doi:10.3390/rs18101650 | Aqua MYD14 vs VNP14IMG FRP; global, 2012-2024 | Footprint matching, cloud correction, VZA-binned empirical correction, fusion; 90/10 split | Pixel FRP slope 0.74 before, 1.03 after; continental daily totals RMA slope 0.70 before, 0.92 after. MODIS minimum detectable FRP rises about 8.2-fold nadir to edge (4.1 to over 33.6 MW); VIIRS about 1.6-fold. Fused product has about 3.8 times the fire pixels of MODIS |
| [Chen et al. 2026, ESSD 18:7535-7555](https://essd.copernicus.org/articles/18/7535/2026/), doi:10.5194/essd-18-7535-2026 (GFED5NRT) | VIIRS 375 m counts calibrated to MODIS-based GFED5 burned area, 2012-2022 | Region-by-land-cover "effective fire area" factors (up to 224), scan-angle weights | Global burned-area Taylor skill score 0.88 temporal, 0.94 spatial; regional spatial 0.62-0.95. SNPP and NOAA-20 combined as arithmetic mean, fallback to the one available |
| [Sofiev and Kouznetsov 2026, GMD 19:10123-10142](https://egusphere.copernicus.org/preprints/2026/egusphere-2026-89/), doi:10.5194/gmd-19-10123-2026 | MODIS C6.1 and VIIRS FRP detection limits | Analytical observation operator (abstract only) | Powerful-fire detection probability 78% MODIS, 88% VIIRS globally. MODIS limit 3.7 MW at nadir by night, up to 40 MW day side view; VIIRS 0.5 MW at night |
| [Schiks, Wotton, Martell 2024, Fire 7(1):26](https://api.crossref.org/works/10.3390/fire7010026), doi:10.3390/fire7010026 | MODIS, VIIRS and combined; 37 Ontario boreal fires | Kriging of detections to day of burning (abstract only) | Combined data dated about half of each fire's area to within one day. No count ratio |
| [Loboda, O'Neal, Yang 2017](https://drum.lib.umd.edu/handle/1903/20226) (slide deck, not peer reviewed) | MODIS vs VIIRS; 2014 Northwest Territories fires | Not stated in record | MODIS, "even from a single satellite", gave "more comprehensive coverage of on-going burning"; "strong potential for calibration" |

Product-team statements: the 750 m product is "a replica of the MODIS Collection 6 algorithm" and "provides continuity" with MODIS; the 375 m product only "resembles" MOD14/MYD14 ([NASA VIIRS Land](https://viirsland.gsfc.nasa.gov/Products/NASA/FireESDR.html)). A 2019 NOAA-20 review reports "good consistency of detection rates between Suomi NPP and NOAA-20" without numbers ([Csiszar 2019](https://www.star.nesdis.noaa.gov/JPSS/documents/AMM/N20/Land_ActiveFires_Iband_Beta_Provisional.pdf)). GFED5 ends in 2022 "when orbital drift-induced changes surpassed the thresholds" for science products (Chen 2026); CAMS added VIIRS on 4 December 2025 but quantifies no drift effect ([CAMS](https://atmosphere.copernicus.eu/drifting-away-modis-cams-global-fire-assimilation-system)).

## What this implies for the approach

- **Target record.** Every published join (Vadrevu 2018, Zheng 2026, Chen 2026) treats VIIRS as the reference and adjusts MODIS. None reduces VIIRS 375 m to MODIS-equivalent; NASA's suggestion for MODIS-like VIIRS is the 750 m product, which is not in FIRMS.
- **Unit.** Raw count ratios span about 1.3 to 6.5 across products, biomes and scan angles, and Fu 2020 shows a forest-versus-open-land difference. FRP sums agree better at coarse grids but disagree for large boreal fires. No study tests active cells per day or per-sensor anomalies; the literature is silent, not negative, on both.
- **Scaling.** Every fitted correction depends on scan angle, grid size, land cover or season. One factor has no published support; a seasonal or a view-angle-dependent factor does.
- **Combining VIIRS satellites.** Only GFED5NRT does this: arithmetic mean of per-satellite estimates, fallback to whichever exists. NOAA-20 vs Suomi NPP consistency is asserted qualitatively only. No NOAA-21 comparison found.
- **MODIS since 2022.** GFED5 stops at 2022 for drift. Zheng 2026 warns that Aqua-calibrated coefficients should not be applied to Terra because overpass time changes fire activity sampled; by the same logic a drifted overpass time changes the relationship (inference, not tested in any paper).

## Limits

- Fu 2020, Li 2018, Sofiev 2026 and Schiks 2024 were read as abstracts only; their methods and full tables are unconfirmed.
- The Fu 2020 ratios (1.9 forest, 2.8 low-biomass) are the verifier's arithmetic (matched share of MODIS divided by matched share of VIIRS). If several VIIRS pixels match one MODIS pixel, the true ratios are higher, so treat them as lower bounds.
- The Vadrevu 4.8 ratio divides averages over different years (VIIRS 2012-2016, MODIS 2003-2016).
- Li 2020 states the share of grids with VIIRS-only fire (34%) at 5° in its results and at 0.5° in its discussion.
- No source gives a MODIS-vs-VIIRS count ratio by day and night, by season, or for Interior British Columbia. Absence claims rest on several searches, not proof.
- Unconfirmed (not opened): Oliva and Schroeder 2015; Vadrevu et al. 2024 (Atmosphere) night-fire shares; a NASA page claiming VIIRS sees 3-4 times more fires than MODIS; a "300% at scan edge" MODIS FRP figure; a 2018 *Fire* paper on sub-canopy smouldering in the North American boreal forest (403); an AGU 2019 abstract on viewing-geometry correction of fire time series (405).

## How it was computed

No analysis script; this is a literature check. PDFs were downloaded to the scratchpad folder `verify-r01` and converted with `pdftotext`, then searched for each number in the draft. Abstract-only sources were read through publisher, Crossref or repository record pages. The only arithmetic is the Fu 2020 ratio (0.65/0.35 and 0.47/0.17).

## Sources

- Csiszar et al. 2014: https://directreadout.sci.gsfc.nasa.gov/publications_documents/Csiszar_et_al_2014_JGR.pdf
- Schroeder et al. 2014: https://earthdata.nasa.gov/s3fs-public/imported/Schroeder_et_al_2014b_RSE.pdf
- VIIRS C2 375 m User Guide v1.2: https://www.earthdata.nasa.gov/s3fs-public/2025-06/VIIRS_C2_AF-375m_User_Guide_1.2.pdf
- VNP14/VNP14IMG User Guide v1.1 (2017): https://ladsweb.modaps.eosdis.nasa.gov/api/v2/content/archives/Document%20Archive/Science%20Data%20Product%20Documentation/VNP14_Active-Fire_UG_2017.pdf
- Fu et al. 2020: https://api.crossref.org/works/10.3390/rs12182870
- Vadrevu and Lasko 2018: https://pmc.ncbi.nlm.nih.gov/articles/PMC6108185/
- Li et al. 2018: https://repository.library.noaa.gov/view/noaa/49896
- Li et al. 2020: https://repository.library.noaa.gov/view/noaa/42501/noaa_42501_DS1.pdf
- Zheng et al. 2026: https://mdpi-res.com/d_attachment/remotesensing/remotesensing-18-01650/article_deploy/remotesensing-18-01650.pdf
- Chen et al. 2026: https://essd.copernicus.org/articles/18/7535/2026/
- Sofiev and Kouznetsov 2026: https://egusphere.copernicus.org/preprints/2026/egusphere-2026-89/
- Schiks et al. 2024: https://api.crossref.org/works/10.3390/fire7010026
- Loboda et al. 2017: https://drum.lib.umd.edu/handle/1903/20226
- NASA VIIRS Land fire product page: https://viirsland.gsfc.nasa.gov/Products/NASA/FireESDR.html
- NASA VIIRS fire validation page: https://viirsland.gsfc.nasa.gov/Val/Fire_Val.html
- NOAA-20 375 m beta review (2019): https://www.star.nesdis.noaa.gov/JPSS/documents/AMM/N20/Land_ActiveFires_Iband_Beta_Provisional.pdf
- CAMS on MODIS drift: https://atmosphere.copernicus.eu/drifting-away-modis-cams-global-fire-assimilation-system
