# MODIS active fire algorithm and product (MOD14/MYD14)

Verified 2026-11-13. "G16" means Giglio, Schroeder and Justice (2016), *The collection 6 MODIS active fire detection algorithm and fire products*, Remote Sensing of Environment 178:31-41, doi:10.1016/j.rse.2016.02.054. "UG" means the *MODIS Collection 6 and Collection 6.1 Active Fire Product User's Guide*, Version 1.0, May 2021 (Giglio, Schroeder, Hall, Justice). The text of both PDFs was extracted and checked line by line.

Status tags: [confirmed] = the linked page supports the statement as written; [corrected] = the researcher's version was wrong or incomplete and this is the fixed version; [unverified] = not confirmed on an opened page.

Terms used: MOD14 is the Terra Level 2 (swath) fire product, MYD14 the Aqua one. MCD14ML is the monthly ASCII fire-location list built from both, and MCD14DL is the near-real-time (NRT) list served by FIRMS. T4, T11 and T12 are brightness temperatures at 4, 11 and 12 um. ΔT = T4 − T11. ρ0.65, ρ0.86 and ρ2.1 are top-of-atmosphere reflectances. MAD is the mean absolute deviation. FRP is fire radiative power. MLT is mean local time of the equator crossing.

## Key facts

### Inputs and outline of the algorithm (C6, unchanged in C6.1)

- The algorithm runs on each 1-km pixel in native, unprojected swath geometry. It uses T4, T11 and T12 from the 1-km channels and, by day only, ρ0.65, ρ0.86 and ρ2.1 aggregated to 1 km. Every pixel ends up in one of five classes: missing data, cloud, non-fire, fire or unknown. The product itself uses a larger set of classes that maps onto these five. [G16 §3, Fig. 1](https://www.earthdata.nasa.gov/s3fs-public/imported/Giglio2016_C6_Fire.pdf) [confirmed]
- The processing steps run in this order: pixels without valid data become missing data; land/water masking using the C6 MOD03/MYD03 1-km land/sea mask (coast pixels are counted but never processed); cloud masking; potential-fire screening; background characterization; tentative detection; rejection tests; then confidence and FRP. [G16 §3.1-3.8](https://www.earthdata.nasa.gov/s3fs-public/imported/Giglio2016_C6_Fire.pdf) [confirmed]

| Band | Centre (um) | Purpose in algorithm (G16 Table 1) |
|---|---|---|
| 1 | 0.65 | Sun glint and coastal false-alarm rejection; cloud masking |
| 2 | 0.86 | Bright surface, sun glint and coastal rejection; cloud masking |
| 7 | 2.1 | Sun glint and coastal rejection |
| 21 | 4.0 | High-range (saturates near 500 K) fire channel |
| 22 | 4.0 | Low-range fire channel |
| 31 | 11.0 | Fire detection, cloud masking, forest clearing rejection |
| 32 | 12.0 | Cloud masking |

Source: [G16 Table 1](https://www.earthdata.nasa.gov/s3fs-public/imported/Giglio2016_C6_Fire.pdf) [confirmed]. The 500 K saturation figure for band 21 is from memory and is [unverified]. Bit 2 of the Level 2 "algorithm QA" layer records whether the 4-um value came from band 21 or band 22. [UG Table 4](https://earthdata.nasa.gov/s3fs-public/2023-09/MODIS_C6_C6.1_Fire_User_Guide_1.0.pdf) [confirmed]

### Cloud mask (C6)

- A pixel counts as daytime when its solar zenith angle is below 85°. A daytime pixel is cloud if (ρ0.65 + ρ0.86 > 1.2) or (T12 < 265 K) or (ρ0.65 + ρ0.86 > 0.7 and T12 < 285 K) or (water pixel and ρ0.86 > 0.25 and T12 < 300 K). The fourth condition is new in C6 and applies to water only. A nighttime pixel is cloud if T12 < 265 K. The thresholds were adjusted slightly for C6 because the C5 mask sometimes classed thick smoke as cloud. The mask catches larger, cooler clouds but "consistently miss[es] small clouds and cloud edges". [G16 §3.2](https://www.earthdata.nasa.gov/s3fs-public/imported/Giglio2016_C6_Fire.pdf) [confirmed]
- The UG warns that the internal cloud mask often fails at cloud edges and on thin cirrus, is likely to mislabel snow and sometimes desert as cloud, and should not be used as a general-purpose cloud mask. [UG FAQ 8.4.7](https://earthdata.nasa.gov/s3fs-public/2023-09/MODIS_C6_C6.1_Fire_User_Guide_1.0.pdf) [confirmed]

### Potential-fire screening: C5 fixed versus C6 dynamic thresholds

| Item | Collection 5 and earlier | Collection 6 / 6.1 |
|---|---|---|
| Condition (day) | T4 > T4*, ΔT > ΔT*, ρ0.86 < 0.35 | same form |
| Condition (night) | T4 > T4*, ΔT > ΔT* (no reflectance test) | same form |
| T4* | fixed 310 K by day, 305 K at night | mean(T4)_j + 5 K, limited to 300-330 K (land only) |
| ΔT* | fixed 10 K | mean(ΔT)_j + 5 K, limited to 10-35 K (land only) |
| Water pixels | fixed | C5 fixed values still used |

Source: [G16 §3.3](https://www.earthdata.nasa.gov/s3fs-public/imported/Giglio2016_C6_Fire.pdf) [confirmed]

- In C6 the thresholds are set separately for each of the 1354 sample positions j (0-1353) in a scan. A MODIS scan is 10 lines of 1354 1-km samples. The means use cloud-free and glint-free land pixels in a window 301 samples by 30 lines centred on j. That window covers about 306 km × 30 km at nadir and about 740 km × 33 km at the scan edge. Pixels with T4 > 360 K by day or > 320 K at night are left out of the means. A mean draws on at most 9030 pixels; if fewer than 2000 are available, the C5 fixed thresholds are used instead. The method compensates for the longer atmospheric path at larger scan angles. [G16 §3.3](https://www.earthdata.nasa.gov/s3fs-public/imported/Giglio2016_C6_Fire.pdf) [confirmed]
- Example: in the Terra granule of 5 March 2003 at 14:15 UTC over South America, 77% of land pixels had a C6 T4* below 310 K and almost every land pixel had ΔT* above 10 K. Potential-fire pixels fell from 49,620 (C5) to 4057 (C6). [G16 §3.3, Fig. 3](https://www.earthdata.nasa.gov/s3fs-public/imported/Giglio2016_C6_Fire.pdf) [confirmed]
- Example of smoke-covered fires: the C6 dynamic thresholds together with the higher 0.86-um threshold added 95 large-fire pixels, an increase of nearly 44% over C5. The text calls the location "central Siberia". The Fig. 4 caption identifies the scene as an **Aqua** granule over northern Russia on 22 July 2014 at 05:20 UTC. [G16 §3.3, Fig. 4](https://www.earthdata.nasa.gov/s3fs-public/imported/Giglio2016_C6_Fire.pdf) [corrected: platform and date added; the researcher did not say it was Aqua]

### Background characterization

- The background is taken from a window around each potential fire pixel that grows up to 21 × 21 pixels. New in C6: valid background pixels must match the candidate pixel's land/water state, so land and water are never mixed. Statistics are computed as listed in G16 Table 2: means and MADs of T4, T11 and ΔT; the mean T4 and MAD (δ′4) of rejected background-fire pixels; and the counts Nv (valid pixels), Nf (background fires), Nc (coast pixels), Nw (water pixels) and NL (land pixels). L4 (mean 4-um radiance), mean ρ0.86 (day only), Nc and NL are new in C6. [G16 §3.4, Table 2](https://www.earthdata.nasa.gov/s3fs-public/imported/Giglio2016_C6_Fire.pdf) [confirmed]

### Detection tests (unchanged from C5)

| Test | Condition |
|---|---|
| (1) absolute | T4 > 360 K (320 K at night) |
| (2) | ΔT > mean ΔT + 3.5 δΔT |
| (3) | ΔT > mean ΔT + 6 K |
| (4) | T4 > mean T4 + 3 δ4 |
| (5) | T11 > mean T11 + δ11 − 4 K |
| (6) | δ′4 > 5 K |

Source: [G16 §3.5, Eqs. 1-6](https://www.earthdata.nasa.gov/s3fs-public/imported/Giglio2016_C6_Fire.pdf) [confirmed]

- **Day:** a pixel is a tentative fire if test 1 passes, or if tests 2-4 pass together with test 5 or test 6. **Night:** a pixel is a fire if test 1 passes or tests 2-4 pass. The night result is final only for **land** pixels. Water pixels, by day and by night, and daytime land pixels still go through the rejection tests. [G16 §3.5](https://www.earthdata.nasa.gov/s3fs-public/imported/Giglio2016_C6_Fire.pdf) [corrected: the researcher said the night result was final without restricting this to land]
- If no background can be characterized, only test 1 is applied, and a pixel that fails it is classed "unknown". This is rare: 0.001% of all MODIS land pixels, Terra and Aqua combined, over 2005-2009. That figure comes from the **Collection 5** swath product. [G16 §3.5](https://www.earthdata.nasa.gov/s3fs-public/imported/Giglio2016_C6_Fire.pdf) [corrected: the researcher did not say the statistic is from C5]

### Rejection tests (false-alarm screening)

| Test | Applies to | Rule | C6 status |
|---|---|---|---|
| Sun glint | land and water tentative fires | reject if θg < 2°; or θg < 10° and ρ0.65 > 0.1 and ρ0.86 > 0.2 and ρ2.1 > 0.12; or θg < 15° and (Naw + Nw) > 0 | two angle thresholds raised in C6 |
| Desert boundary | land | as in Giglio et al. 2003 §2.2.7 | unchanged since introduced in C4 |
| Land-pixel coastal | land | uses ρ0.86, ρ2.1 and NDVI of background (Giglio et al. 2003 §2.2.8) | retained |
| Forest clearing | daytime land | reject if T11 > mean T11 + 3.7 δ11 and ρ0.86 > 0.28 and T4 < 325 K | new in C6, tuned on 65 Amazon ASTER scenes |
| Water-pixel coastal | water | reject if NL + Nc > 0 and test 1 not passed | new in C6 |

Source: [G16 §3.6.1-3.6.5](https://www.earthdata.nasa.gov/s3fs-public/imported/Giglio2016_C6_Fire.pdf) [confirmed]. θg is the angle between the surface-to-satellite vector and the specular reflection direction. Naw is the number of water pixels among the 8 neighbours. G16 notes that the third glint rule "effectively renders the detection of offshore gas flares impossible in the presence of sun glint". [confirmed]

### Fire mask classes (Level 2 SDS "fire mask", 8-bit)

| Class | Meaning |
|---|---|
| 0 | not processed (missing input data) |
| 1 | not processed (obsolete; not used since Collection 1) |
| 2 | not processed (other reason) |
| 3 | non-fire water pixel |
| 4 | cloud (land or water) |
| 5 | non-fire land pixel |
| 6 | unknown (land or water) |
| 7 | fire, low confidence (land or water) |
| 8 | fire, nominal confidence (land or water) |
| 9 | fire, high confidence (land or water) |

Source: [UG §5.1.1, Table 3](https://earthdata.nasa.gov/s3fs-public/2023-09/MODIS_C6_C6.1_Fire_User_Guide_1.0.pdf) [confirmed]. Since C6, cloud, unknown and fire classes can occur over water. To separate land from water, use bits 0-1 of the 32-bit "algorithm QA" SDS (00 water, 01 coast, 10 land). Bit 4 is the day/night algorithm flag. [UG §5.1.2, §5.1.4 Table 4](https://earthdata.nasa.gov/s3fs-public/2023-09/MODIS_C6_C6.1_Fire_User_Guide_1.0.pdf) [confirmed]

### Detection confidence

- Confidence C (0-100%) is a heuristic. It is the geometric mean of up to five sub-confidences. S(x; α, β) is a linear ramp: 0 when x ≤ α and 1 when x ≥ β. Daytime land values: C1 = S(T4; mean T4, 360 K); C2 = S(z4; 3.0, 6); C3 = S(zΔT; 3.5, 6); C4 = 1 − S(Nac; 0, 4), where Nac is the number of adjacent cloud pixels; C5 = 1 − S(Naw; 0, 4). Here z4 = (T4 − mean T4)/δ4 and zΔT = (ΔT − mean ΔT)/δΔT. At night the 360 K in C1 becomes 320 K, and C4 and C5 are dropped. For daytime fires over water, C5 is dropped. The parameters "have been adjusted for Collection 6". [G16 §3.7, Eqs. 10-15](https://www.earthdata.nasa.gov/s3fs-public/imported/Giglio2016_C6_Fire.pdf) [confirmed]

| Confidence class | Range of C | Fire mask class |
|---|---|---|
| low | 0% ≤ C < 30% | 7 |
| nominal | 30% ≤ C < 80% | 8 |
| high | 80% ≤ C ≤ 100% | 9 |

Source: [UG FAQ 8.4.3, Table 11](https://earthdata.nasa.gov/s3fs-public/2023-09/MODIS_C6_C6.1_Fire_User_Guide_1.0.pdf) [confirmed]. C is stored in the L2 "FP confidence" SDS and in the MCD14ML "conf" column (0-100). [UG Table 10](https://earthdata.nasa.gov/s3fs-public/2023-09/MODIS_C6_C6.1_Fire_User_Guide_1.0.pdf) [confirmed]

- The FIRMS FAQ says MODIS confidence runs from 0 to 100%, that users choose their own cutoff, and that "there is no way to establish an optimal cutoff a priori". It does not give the 30/80 class boundaries in the part that was read. [FIRMS FAQ](https://www.earthdata.nasa.gov/data/tools/firms/faq) [confirmed]
- History of the confidence score: in C4, highly questionable pixels that should have scored near 0% often scored 50% or more. A C5 adjustment partly fixed this, and a second minor adjustment was made for C6, but some highly questionable pixels are still classed nominal. Users who want fewer false alarms may keep only the nominal and high classes and treat low-confidence pixels as non-fire land. [UG §7.2.2, §5.1.3](https://earthdata.nasa.gov/s3fs-public/2023-09/MODIS_C6_C6.1_Fire_User_Guide_1.0.pdf) [confirmed]

### Fire radiative power (FRP)

- Since C6, FRP ≈ (A_pix σ / (a τ4)) (L4 − mean L4). L4 is the 4-um radiance of the fire pixel and mean L4 the background radiance. A_pix is the pixel area, which depends on scan angle. σ = 5.6704 × 10⁻⁸ W m⁻² K⁻⁴. For MODIS, a = 3.0 × 10⁻⁹ W m⁻² sr⁻¹ um⁻¹ K⁻⁴ when radiance is in W m⁻² sr⁻¹ um⁻¹. τ4 is set to 1 in the Level 2 product, so no atmospheric correction is applied. [G16 §3.8, Eq. 16](https://www.earthdata.nasa.gov/s3fs-public/imported/Giglio2016_C6_Fire.pdf) [confirmed]. FRP is reported in MW for each pixel ("pixel-integrated"). [MODAPS MCD14DL page](https://modaps.modaps.eosdis.nasa.gov/services/about/products/c61-nrt/MCD14DL-NRT.html), [UG Table 10](https://earthdata.nasa.gov/s3fs-public/2023-09/MODIS_C6_C6.1_Fire_User_Guide_1.0.pdf) [confirmed]
- **Method change at C6:** the empirical retrieval of Kaufman et al. (1998), used through C5, was replaced by the Wooster et al. (2003, 2012) MIR-radiance method. For about 240,000 Terra and Aqua fire pixels detected in both collections (1-10 August 2005), mean FRP was 56.9 MW in C5 and 47.7 MW in C6, an average drop of about 16%. Pixels above about 500 MW occasionally rose by up to a few percent. [G16 §3.8, Fig. 6](https://www.earthdata.nasa.gov/s3fs-public/imported/Giglio2016_C6_Fire.pdf) [confirmed]
- C6.1 left FRP unchanged because the thermal bands were not recalibrated. [UG §2.1](https://earthdata.nasa.gov/s3fs-public/2023-09/MODIS_C6_C6.1_Fire_User_Guide_1.0.pdf) [confirmed]
- **Units history:** the C4 L2 "FP power" SDS held power per unit area even though its units attribute said "megawatts". Those values must be multiplied by pixel area in km² to get MW. From C5 onward the product stores FRP in MW. [UG FAQ 8.4.5](https://earthdata.nasa.gov/s3fs-public/2023-09/MODIS_C6_C6.1_Fire_User_Guide_1.0.pdf) [confirmed]
- **Pixel area:** nominally 1 km², growing away from nadir. The UG gives formulas for the along-scan and along-track dimensions with Re = 6378.137 km, h = 705 km, s = 0.0014184397 and scan angle θ = s × (sample − 676.5) radians. [UG FAQ 8.4.6](https://earthdata.nasa.gov/s3fs-public/2023-09/MODIS_C6_C6.1_Fire_User_Guide_1.0.pdf) [confirmed]. FIRMS supplies the actual pixel size as the "scan" and "track" attributes. [FIRMS FAQ](https://www.earthdata.nasa.gov/data/tools/firms/faq), [MODAPS MCD14DL](https://modaps.modaps.eosdis.nasa.gov/services/about/products/c61-nrt/MCD14DL-NRT.html) [confirmed]

### Detection limits and validation

- **Smallest detectable fire (UG):** about 1000 m² for both flaming and smoldering fires as a matter of routine; under very good conditions (near nadir, little or no smoke, fairly uniform surface) flaming fires one tenth that size, about 100 m²; under pristine and extremely rare conditions flaming fires of about 50 m². There is no upper limit on the size or temperature of a detectable fire. Detection of understory fires beneath canopy is "unknown but probably very low". Fires in unexposed coal seams are generally not detected. [UG FAQ 8.3.2, 8.3.4, 8.3.5](https://earthdata.nasa.gov/s3fs-public/2023-09/MODIS_C6_C6.1_Fire_User_Guide_1.0.pdf) [confirmed]. The FIRMS FAQ repeats the 1000 m² figure. [FIRMS FAQ](https://www.earthdata.nasa.gov/data/tools/firms/faq) [confirmed]
- **Stage 3 ASTER validation (Terra only, near nadir):** 2466 ASTER scenes, each 60 × 60 km, within ±8.55° of nadir in a MODIS swath about 2300 km wide. Scenes were sampled in three periods (2001-2002, 2003-2004 and 2005-2006) on a grid of about 640 equal-area cells 900 km across; 140 scenes were acquired at night. The abstract describes the sample as "more than 2500" images. ASTER can see fires down to about 4 m² at 900 K. [G16 §4](https://www.earthdata.nasa.gov/s3fs-public/imported/Giglio2016_C6_Fire.pdf) [confirmed]
- **Omission error, C6:** 86.2% over fires of all sizes seen by ASTER. Below 10% for reference fires of 140 or more 30-m ASTER fire pixels, levelling off at about 5% above about 250 ASTER fire pixels per MODIS pixel. For clusters under 100 ASTER pixels, low tree cover (<20%) and high tree cover (>60%) differ by about 9% absolute, with more omission at low tree cover. C6 detects large fire clusters (>300 ASTER pixels) in tree cover above 60% better than C5, mostly in boreal regions with thick smoke. [G16 §5.1, Fig. 8](https://www.earthdata.nasa.gov/s3fs-public/imported/Giglio2016_C6_Fire.pdf) [confirmed]
- **Commission error:** the global daytime rate was 1.2% in C6 and 2.4% in C5. None was found at night (838 MOD14 fire pixels among about 500,000 night pixels sampled), so false alarms are confined to daytime. False-alarm rates rise with tree cover. Industrial heat sources were not counted as commission errors. [G16 §5.1, Fig. 9](https://www.earthdata.nasa.gov/s3fs-public/imported/Giglio2016_C6_Fire.pdf) [confirmed]
- **Regional results (14 GFED regions):** C6 probability of detection ranges from 7% in the Middle East to 26% in Australia and New Zealand, driven by median fire size. Compared with C5: about +3% absolute in Boreal North America and Boreal Asia, +1% in Equatorial Asia and Central Asia, −1% in NH South America, and little or no change in the other nine regions. Commission error fell by about 5% absolute in Equatorial Asia and SH South America and by about 1% in Central Asia, NH South America and Temperate North America. [G16 §5.2](https://www.earthdata.nasa.gov/s3fs-public/imported/Giglio2016_C6_Fire.pdf) [confirmed]
- **Earlier C5 Amazon result:** about 35% commission error from small forest clearings (Schroeder et al. 2008), which led to the C6 forest-clearing test. [G16 §2](https://www.earthdata.nasa.gov/s3fs-public/imported/Giglio2016_C6_Fire.pdf) [confirmed]
- **Coverage of validation:** the ASTER validation covers Terra only, because ASTER flies on Terra, and near-nadir pixels only. Independent non-ASTER validation of C5 Terra and Aqua is cited (de Klerk 2008; Hawbaker et al. 2008). No C6 validation of Aqua or of off-nadir pixels is given. [UG §6.1-6.2](https://earthdata.nasa.gov/s3fs-public/2023-09/MODIS_C6_C6.1_Fire_User_Guide_1.0.pdf) [confirmed]

### Known problems and caveats

- **Before November 2000 (Terra):** dead detectors, switched off to reduce crosstalk, cause striping and missed small and large fires. Severe band-21 miscalibration in February-March 2000 can flag whole scan lines as fire. CMG and fire-location products (including MCD14ML) are not distributed before November 2000; L2 and tiled L3 are. G16 advises starting time series in November 2000. Terra MODIS was also inoperable for part of September 2000. [UG §7.2.1, FAQ 8.3.3, 8.3.10-8.3.11](https://earthdata.nasa.gov/s3fs-public/2023-09/MODIS_C6_C6.1_Fire_User_Guide_1.0.pdf); [G16 §6](https://www.earthdata.nasa.gov/s3fs-public/imported/Giglio2016_C6_Fire.pdf) [confirmed]
- **Aqua FMU outage:** a failure of the formatter-multiplexer unit on 16 August 2020 stopped regular science telemetry for about two weeks, 16 August to 2 September 2020. Only partial Direct Broadcast coverage exists for that period. [UG §7.2.4](https://earthdata.nasa.gov/s3fs-public/2023-09/MODIS_C6_C6.1_Fire_User_Guide_1.0.pdf) [confirmed]
- **Terra MODIS standby, 2026:** at about 20:00 UTC on 26 March 2026 (DOY 085) a Terra anomaly put MODIS into standby. It returned to science mode on 27 March 2026. Data from 2026-085 20:00 UTC to 2026-086 19:23 UTC are flagged questionable or bad, and data after that are safe. The FIRMS MODIS NRT product and MOD14 NRT are among the products affected. [Earthdata alert, updated 31 Mar 2026](https://www.earthdata.nasa.gov/data/alerts-outages/modis-terra-placed-standby-mode) [confirmed; added]
- **Calibration-maneuver striping (C5 only):** a bug in the C5 L1B code produced false thermal radiances during lunar roll maneuvers, giving stripes of fire pixels across the swath in up to about 20 scans. Some of these reached the C5 CMG and MCD14ML products. The bug was fixed in late 2009 and is absent from C6. [UG §7.3.2](https://earthdata.nasa.gov/s3fs-public/2023-09/MODIS_C6_C6.1_Fire_User_Guide_1.0.pdf) [confirmed]
- **Small forest clearings:** persistent C5 false alarms in the Amazon, reduced in C6 by the new rejection test. [UG §7.3.1](https://earthdata.nasa.gov/s3fs-public/2023-09/MODIS_C6_C6.1_Fire_User_Guide_1.0.pdf) [confirmed]
- **Desert boundary false alarms:** these occur near sharp radiometric transitions at the edges of hot, arid, sparse or barren areas. [G16 §3.6.2](https://www.earthdata.nasa.gov/s3fs-public/imported/Giglio2016_C6_Fire.pdf) [confirmed]
- **Static sources:** some non-fire static sources are still not flagged in the MCD14ML type field. Version 3 of the file improved this. [UG §7.2.3](https://earthdata.nasa.gov/s3fs-public/2023-09/MODIS_C6_C6.1_Fire_User_Guide_1.0.pdf) [confirmed; added]
- **Binning caveat:** "severe temporal and spatial biases may arise in any MODIS fire time series analysis employing time intervals shorter than about eight days." Fire-location files carry no record of cloud or missing data, so a missing detection may be due to cloud, a gap in coverage or a land/sea-mask error. [UG §7.1.1](https://earthdata.nasa.gov/s3fs-public/2023-09/MODIS_C6_C6.1_Fire_User_Guide_1.0.pdf) [confirmed]

### Collection history

| Collection | Dates and notes | Source |
|---|---|---|
| 1 | first Terra products after launch | UG §3.1.4 [confirmed] |
| 3 | first reprocessing, June 2001 (no Collection 2); first Aqua version | UG §3.1.4 [confirmed] |
| 4 | reprocessing began December 2002, ended December 2006; desert-boundary test added | UG §3.1.4; G16 §3.6.2 [confirmed] |
| 5 | production began mid-2006 | UG §3.1.4; G16 §2 [confirmed] |
| 6 | "fourth major reprocessing". UG: Tier-1 production began **February 2015**. G16: reprocessing "commenced in May 2015". Production through 31 Dec 2021 | UG §3.1.4; G16 abstract, §1 [confirmed; dates conflict] |
| 6.1 | mini-reprocessing begun in 2018 for atmosphere, extended to land in late 2020. No change to the fire algorithm. FIRMS NRT switched to C6.1 in April 2021 | UG §2.1, §3.1.4; MODAPS; FIRMS FAQ [confirmed] |

Links: [UG](https://earthdata.nasa.gov/s3fs-public/2023-09/MODIS_C6_C6.1_Fire_User_Guide_1.0.pdf), [G16](https://www.earthdata.nasa.gov/s3fs-public/imported/Giglio2016_C6_Fire.pdf), [MODAPS MCD14DL](https://modaps.modaps.eosdis.nasa.gov/services/about/products/c61-nrt/MCD14DL-NRT.html), [FIRMS FAQ](https://www.earthdata.nasa.gov/data/tools/firms/faq)

- **Changes from C5 to C6 (UG list of 14):** (1) processing extended to oceans and large water bodies to catch offshore gas flares; (2) fewer false alarms from small forest clearings; (3) better detection of small fires; (4) wider sun-glint rejection; (5) slightly better cloud masking; (6) slight change to the confidence calculation; (7) FRP by the Wooster et al. (2003) method; (8) expanded L2 fire-pixel table; (9) more granule metadata; (10) simpler date layer in the L3 daily product; (11) simpler QA layer in the L3 8-day and daily products; (12) 0.25° CMG products; (13) better removal of static sources from CMG; (14) new hot-spot "type" and day/night flag in MCD14ML. [UG §2.2](https://earthdata.nasa.gov/s3fs-public/2023-09/MODIS_C6_C6.1_Fire_User_Guide_1.0.pdf) [confirmed]
- **C6 compared with C6.1:** the UG says the two "may be freely intermixed". The only differences come from recalibrated bands 1 and 2, which mostly affect the cloud class. One-day sample (8 July 2009): 18 of 17,610 fire-class pixels (0.1%) changed class. One-month sample (January 2020, 17,825 granules): 99.64% of granules had identical fire counts, the largest difference in any granule was 3 pixels, and global totals were 404,057 (C6) and 404,052 (C6.1), a 0.001% difference. [UG §2.1, Table 1, Fig. 1](https://earthdata.nasa.gov/s3fs-public/2023-09/MODIS_C6_C6.1_Fire_User_Guide_1.0.pdf) [confirmed; one-day sample date added]
- **Whole-archive reprocessing:** G16 says "the entire MODIS archive has been reprocessed" with C6 and is distributed by LP DAAC. Periodic reprocessing is the EOS approach to producing consistent long-term records. [G16 §1, §6](https://www.earthdata.nasa.gov/s3fs-public/imported/Giglio2016_C6_Fire.pdf) [confirmed]. MOD14 V061 is listed as HDF4, 1 km, covering 2000-02-24 to the present, status ACTIVE, DOI 10.5067/MODIS/MOD14.061. [Earthdata catalog MOD14 061](https://www.earthdata.nasa.gov/data/catalog/lpcloud-mod14-061) [confirmed; added]. The MODIS Land news page says C6.1 land reprocessing was finished for all products by August 2023. [MODIS Land news](https://modis-land.gsfc.nasa.gov/news.html) [confirmed]

### NRT and standard fire lists (FIRMS)

- C6.1 MCD14DL NRT replaced C6 (DOI 10.5067/FIRMS/MODIS/MCD14DL.NRT.006) in April 2021. The C6.1 DOI is 10.5067/FIRMS/MODIS/MCD14DL.NRT.0061. C6.1 contains "no updates to the science algorithm". Version labels are 6.1URT (ultra real-time), 6.1RT (real-time) and 6.1NRT. Standard MCD14ML records replace NRT records "usually after 2 months", though the Known Issues section of the same page says a "3-month lag". NRT locations usually differ from standard by less than 100 m, but by up to several km around spacecraft maneuvers and space-weather events. EOSDIS recommends the standard product. [MODAPS MCD14DL](https://modaps.modaps.eosdis.nasa.gov/services/about/products/c61-nrt/MCD14DL-NRT.html) [confirmed]. The FIRMS FAQ gives the standard-product lag as "2-3 month[s]" and says NRT data arrive within 3 hours of observation. [FIRMS FAQ](https://www.earthdata.nasa.gov/data/tools/firms/faq) [confirmed; added]
- The **"type" attribute is in the standard MCD14ML only, not in FIRMS NRT downloads.** [MODAPS MCD14DL](https://modaps.modaps.eosdis.nasa.gov/services/about/products/c61-nrt/MCD14DL-NRT.html); [FIRMS FAQ](https://www.earthdata.nasa.gov/data/tools/firms/faq) [confirmed; added]
- **MCD14ML columns (version 2 and later):** YYYYMMDD and HHMM (UTC); sat (T or A); lat and lon (degrees, pixel centre); T21 and T31 (K); sample (0-1353); FRP (MW); conf (%, 0-100); type (0 presumed vegetation fire, 1 active volcano, 2 other static land source, 3 offshore); dn (D or N). Types 0-2 apply to land only, and every water detection is type 3. Type 2 covers hot spots detected on 16 or more days in any calendar year, plus detections in urban areas as mapped by C6 MCD12Q1. File names follow MCD14ML.YYYYMM.CCC.VV.txt, with version "03" current. Version 1 had no dn column and one fewer decimal place in lat/lon. [UG §5.5, Table 10, §5.5.1-5.5.2](https://earthdata.nasa.gov/s3fs-public/2023-09/MODIS_C6_C6.1_Fire_User_Guide_1.0.pdf) [confirmed; version details added]
- Overpass times quoted by FIRMS: Terra about 10:30 and 22:30 MLT, Aqua about 13:30 and 01:30 MLT. These are the nominal design values; both orbits have since drifted (see below). [FIRMS FAQ](https://www.earthdata.nasa.gov/data/tools/firms/faq) [confirmed]

### Orbit drift and mission end (status at 2026-11-13)

| Item | Terra | Aqua |
|---|---|---|
| Last orbit maintenance | last inclination maneuver February 2020 | all MLT-maintenance maneuvers completed 18 March 2021 |
| Drift | 10:30 MLT reached about 10:15 by October 2022, about 9:00 by about December 2025 | began July 2021; past 1:45 (page says "AM", which must mean PM) by February 2023; about 3:50 PM by about August 2026 |
| Constellation exit | October 2022, lowered to 694 km | exit began January 2022 |
| Latest status found | operating "from its lower altitude", editor's note 4 Sep 2026 | Fine Pointing Normal Mode, MODIS B-side Nominal Science Mode, no anomalies (15-21 Aug 2026) |

Sources: [Terra acquisition plan alert, updated 4 Sep 2026](https://www.earthdata.nasa.gov/data/alerts-outages/terra-modis-acquisition-plan-through-december-2025) [confirmed]; [Aqua acquisition plan, LAADS, last updated 26 Oct 2021](https://ladsweb.modaps.eosdis.nasa.gov/alerts-and-issues/200068) [confirmed]; [MCST Aqua weekly report 2026/227-233](https://mcst.gsfc.nasa.gov/iot/pm1weekly20262272026233) [confirmed; added]. The Terra alert does not state the pre-drift 705 km altitude; that value comes from the UG pixel-area formula (h = 705 km). The "27 February 2020" date the researcher mentioned was not found [unverified]. The Aqua alert also says products are "mostly expected to be science quality except for reduced grid size". [confirmed]

- **Projected end-of-science dates by source:** NASA Science (published 29 Dec 2025, updated 20 Mar 2026): Terra February 2027, Aqua September 2027, limited by fuel and battery. [NASA Science](https://science.nasa.gov/science-research/earth-science/terra-the-end-of-an-era/) [confirmed]. Copernicus CAMS (25 Feb 2026): NASA plans to end Terra MODIS data collection in January 2027 and Aqua around September 2027; CAMS is switching GFAS to VIIRS (750 m) and Sentinel-3 for the morning orbit. [CAMS](https://atmosphere.copernicus.eu/drifting-away-modis-cams-global-fire-assimilation-system) [confirmed; added]. Earthdata (2 May 2025): Terra and Aqua will "begin shutting down operations" in late 2026 or early 2027, and "the final reprocessing of MODIS data will take place" afterward, with no date given. [Earthdata transition alert](https://www.earthdata.nasa.gov/data/alerts-outages/transition-from-modis-viirs) [confirmed]. Older plans gave December 2025 for Terra and August 2026 for Aqua. [MODIS Land news](https://modis-land.gsfc.nasa.gov/news.html) [confirmed]
- **FIRMS (27 Oct 2026):** S-NPP VIIRS production in FIRMS stopped at 13:00 UTC on 2 November 2026, and historical S-NPP data remain available. Terra MODIS is described as "the only morning overpass (approximately 3 hours before Aqua)". NASA is "investigating alternatives to maintain fire detections in the morning orbit" for when Terra ends. When Aqua ends, NOAA-20 and NOAA-21 VIIRS cover the afternoon. No MODIS end date is given. [FIRMS blog](https://www.earthdata.nasa.gov/news/blog/transitioning-from-suomi-npp-viirs-omps-what-firms-users-need-know) [confirmed; added. This replaces the researcher's reliance on a URL slug for the S-NPP date]

### Collection 7 and the product after MODIS

- **GOFC Fire IT meeting, 17-18 Sep 2024 (Giglio et al.):** the current MOD14/MYD14 collection is 6.1. "Collection 7 planned for 2024 2025 (likely optimistic)", tied to new MODIS/VIIRS land products, cross-calibration of Aqua MODIS with S-NPP and NOAA-20 VIIRS, IT security mandates, the GitLab transition and cloud migration. The Terra and Aqua end-of-life plan was then "extended through ∼2026". VIIRS active fire products are at Collection 2, with "No date yet for Collection 3". The 750 m VNP14 was "retained for continuity (more like MODIS)". A C7 beta was shown for MCD64A1 burned area only. [GOFC 2024 slides](https://gofcgold.org/sites/default/files/2024-11/Giglio_GOFC_2024_NASA_Fire.pdf) [confirmed: WebFetch failed on a certificate error, so the PDF was retrieved with curl and its text read]
- **MODIS Collection 7 Level 1:** MCST says C7 L1B reprocessing was completed in early 2025, with forward processing from July 2025 (Terra code 7.0.20 from 19 Jul 2025; Aqua 7.0.19 from 15 Jul 2025). [MCST L1B status](https://mcst.gsfc.nasa.gov/level-1b-product-information-and-status) [confirmed; added]. Earthdata announced V7.0 L1B (250 m, 500 m, 1 km) and MOD03/MYD03 geolocation as available (issued 27 Mar 2026). The geolocation now uses a dynamic yearly land-water mask. **The V6.1 Level 1 collection was to be decommissioned on 30 September 2026.** [Earthdata V7.0 alert](https://www.earthdata.nasa.gov/data/alerts-outages/version-7.0-modis-calibrated-radiances-geolocation-data-products-now-available) [confirmed; added]
- The MODIS Land news page (last updated 13 Nov 2025) says land C7 reprocessing was "planned to begin in summer of 2025", that C7 uses an annual land/water mask, and that all C7 products will be netCDF4. It has no fire-specific item. [MODIS Land news](https://modis-land.gsfc.nasa.gov/news.html) [confirmed]
- No page was found announcing the release of a C7 MOD14/MYD14. The Earthdata catalogue still lists MOD14 V061 as ACTIVE. [Earthdata catalog MOD14 061](https://www.earthdata.nasa.gov/data/catalog/lpcloud-mod14-061) [confirmed]
- G16 states that the MODIS C6 algorithm is the baseline for the NASA S-NPP VIIRS 750 m active fire product. [G16 §6](https://www.earthdata.nasa.gov/s3fs-public/imported/Giglio2016_C6_Fire.pdf) [confirmed]

## Why these matter for combining the records

The MODIS fire record changed in algorithm, not just calibration, at the C5-to-C6 step. Potential-fire thresholds became dynamic, a forest-clearing test was added and FRP fell by about 16% on average. A record mixing collections would therefore contain steps, which is why the reprocessed C6/C6.1 archive is the record to use. C6 and C6.1 fire output is essentially identical (0.001% difference in monthly counts).

Detection probability depends strongly on fire size and on scan angle (pixel area grows away from nadir). False alarms occur only by day. The internal cloud mask treats cloud edges, snow and smoke differently from VIIRS. Each of these makes counts depend on the fire-size mix, viewing geometry and time of day, as well as on the number of fires.

The FIRMS NRT records lack the static-source "type" field and have looser geolocation than standard MCD14ML. The two kinds of list are therefore not interchangeable for a long series.

The consistent MODIS record starts in November 2000 and is Terra-only until Aqua data begin in mid-2002. It has known gaps: September 2000 (Terra), 16 August to 2 September 2020 (Aqua) and 26-27 March 2026 (Terra). Both orbits have drifted since 2020-2021, with Terra moving earlier and Aqua later in local time. The local time of observation therefore changes across the record, and with it the stage of the daily fire cycle sampled and the solar geometry. Solar geometry also varies with latitude for a given local time. Both MODIS instruments are expected to stop in early to late 2027, and a final reprocessing, possibly C7 in netCDF4, may later replace the C6.1 archive.

## Conflicts and unverified items

1. **Start of Collection 6:** G16 (published 2016) says the C6 land reprocessing "commenced in May 2015". The UG (May 2021) says C6 Tier-1 production, including active fire, "commenced in February 2015". The UG is the later operational document, but the difference is probably production start versus land-reprocessing start; it does not affect the science. [G16](https://www.earthdata.nasa.gov/s3fs-public/imported/Giglio2016_C6_Fire.pdf); [UG](https://earthdata.nasa.gov/s3fs-public/2023-09/MODIS_C6_C6.1_Fire_User_Guide_1.0.pdf)
2. **Start of Collection 6.1:** the UG says the C6.1 mini-reprocessing was "initiated in 2018" (atmosphere) and for land in late 2020. MCST says C6.1 L1B "was released to the public on September 1, 2017". FIRMS NRT switched in April 2021, and land reprocessing was complete by August 2023. These are different milestones (L1B release, land reprocessing, NRT switch, completion) and do not affect fire science content. [UG](https://earthdata.nasa.gov/s3fs-public/2023-09/MODIS_C6_C6.1_Fire_User_Guide_1.0.pdf); [MCST](https://mcst.gsfc.nasa.gov/level-1b-product-information-and-status); [MODAPS](https://modaps.modaps.eosdis.nasa.gov/services/about/products/c61-nrt/MCD14DL-NRT.html); [MODIS Land news](https://modis-land.gsfc.nasa.gov/news.html)
3. **End of Terra and Aqua:** the MODIS Land news page (stale) gives December 2025 (Terra) and August 2026 (Aqua). The 2024 GOFC slides say "through ∼2026". The Earthdata alert of 2 May 2025 says shutdown begins late 2026 or early 2027. CAMS (25 Feb 2026) gives January 2027 for Terra and about September 2027 for Aqua. NASA Science (updated 20 Mar 2026) gives February 2027 for Terra and September 2027 for Aqua. The NASA Science page is the most recent NASA statement and is the more authoritative; CAMS is a secondary report of NASA plans.
4. **NRT-to-standard lag:** the MODAPS page says "usually after 2 months" in one place and "3-month lag" in another. The FIRMS FAQ says "2-3 month lag". [MODAPS](https://modaps.modaps.eosdis.nasa.gov/services/about/products/c61-nrt/MCD14DL-NRT.html); [FIRMS FAQ](https://www.earthdata.nasa.gov/data/tools/firms/faq)
5. **Aqua crossing time typo:** the LAADS alert says "exceed a 1:45 AM MLT crossing in February 2023", but the same page describes the drift from 1:30 toward 3:50 PM, so the daytime crossing ("PM") is almost certainly meant. [LAADS](https://ladsweb.modaps.eosdis.nasa.gov/alerts-and-issues/200068)
6. **ASTER scene count:** the G16 abstract says "more than 2500" ASTER images, while §4 gives 2466 scenes. Section 4 is the specific value. [G16](https://www.earthdata.nasa.gov/s3fs-public/imported/Giglio2016_C6_Fire.pdf)
7. **Siberian smoke example:** G16's text says "central Siberia". The Fig. 4 caption says northern Russia, Aqua, 22 July 2014.
8. **Date S-NPP stopped in FIRMS:** the FIRMS blog (27 Oct 2026) says 13:00 UTC on 2 November 2026. A search summary of the Earthdata alert history said product delivery would end on 1 November 2026; that alert page was not opened. [unverified for 1 Nov] [FIRMS blog](https://www.earthdata.nasa.gov/news/blog/transitioning-from-suomi-npp-viirs-omps-what-firms-users-need-know)
9. **Unverified:** that Terra's last inclination maneuver was on 27 February 2020 (only "February 2020" is confirmed). That band 21 saturates near 500 K (from memory). A 2026 GMD paper giving MODIS C6.1 FRP detection limits of 3.7 MW (nadir, clear night) to 40 MW (daytime, off-nadir) was seen only in the researcher's search summary and not opened.
10. **Terra pre-drift altitude:** the Terra alert gives only the lowered 694 km, not 705 km. The 705 km comes from the UG pixel-area formula.

## Open questions

- Will MOD14/MYD14 get a Collection 7, or will the "final reprocessing" announced for after the end of MODIS be called C7? With what algorithm changes, format (C7 land products are announced as netCDF4) and date? No fire-specific C7 page was found as of 2026-11-13.
- The V6.1 Level 1B collection was due for decommissioning on 30 Sep 2026, while MOD14 V061 is still listed as ACTIVE. Is C6.1 fire forward processing (and FIRMS MODIS NRT) still fed by C6.1 L1B, by C7 L1B, or by something else? Does C7 L1B change the thermal-band calibration used for fire detection?
- Will FIRMS keep serving MODIS C6.1 after Terra and Aqua stop, and will the archive be swapped for a reprocessed version?
- There is no published quantitative C6 validation for Aqua MYD14 or for off-nadir pixels; only C5-era independent studies are cited.
- What are the current (November 2026) equator-crossing times of Terra and Aqua? The latest published projections are for December 2025 and August 2026, and no newer measured values were found.
- Did Terra MODIS have further anomalies after March 2026? Only the 26-27 March 2026 standby and the 4 Sep 2026 "remains operational" note were found.

## Sources

- Giglio, Schroeder, Justice (2016), The collection 6 MODIS active fire detection algorithm and fire products, RSE 178:31-41 — https://www.earthdata.nasa.gov/s3fs-public/imported/Giglio2016_C6_Fire.pdf
- Giglio, Schroeder, Hall, Justice, MODIS Collection 6 and Collection 6.1 Active Fire Product User's Guide v1.0 (May 2021) — https://earthdata.nasa.gov/s3fs-public/2023-09/MODIS_C6_C6.1_Fire_User_Guide_1.0.pdf
- MODAPS, MCD14DL NRT product page (C6.1) — https://modaps.modaps.eosdis.nasa.gov/services/about/products/c61-nrt/MCD14DL-NRT.html
- NASA Earthdata, FIRMS Frequently Asked Questions — https://www.earthdata.nasa.gov/data/tools/firms/faq
- NASA Earthdata catalog, MOD14 V061 — https://www.earthdata.nasa.gov/data/catalog/lpcloud-mod14-061
- Giglio et al., NASA Fire Products Update, 2024 GOFC Fire IT Meeting — https://gofcgold.org/sites/default/files/2024-11/Giglio_GOFC_2024_NASA_Fire.pdf
- MODIS Land Team news — https://modis-land.gsfc.nasa.gov/news.html
- MCST, Level 1B product information and status — https://mcst.gsfc.nasa.gov/level-1b-product-information-and-status
- Earthdata alert, Version 7.0 MODIS calibrated radiances and geolocation products now available — https://www.earthdata.nasa.gov/data/alerts-outages/version-7.0-modis-calibrated-radiances-geolocation-data-products-now-available
- Earthdata alert, Terra MODIS acquisition plan through December 2025 (updated 4 Sep 2026) — https://www.earthdata.nasa.gov/data/alerts-outages/terra-modis-acquisition-plan-through-december-2025
- LAADS alert, Aqua MODIS acquisition plan through August 2026 — https://ladsweb.modaps.eosdis.nasa.gov/alerts-and-issues/200068
- Earthdata alert, MODIS Terra placed in standby mode (March 2026) — https://www.earthdata.nasa.gov/data/alerts-outages/modis-terra-placed-standby-mode
- MCST, Aqua MODIS weekly instrument operations report 2026/227-233 — https://mcst.gsfc.nasa.gov/iot/pm1weekly20262272026233
- NASA Science, Terra: The End of An Era (editor's note, updated 20 Mar 2026) — https://science.nasa.gov/science-research/earth-science/terra-the-end-of-an-era/
- Earthdata alert, Transition from MODIS to VIIRS (2 May 2025) — https://www.earthdata.nasa.gov/data/alerts-outages/transition-from-modis-viirs
- Earthdata blog, Transitioning from Suomi NPP VIIRS/OMPS: what FIRMS users need to know (27 Oct 2026) — https://www.earthdata.nasa.gov/news/blog/transitioning-from-suomi-npp-viirs-omps-what-firms-users-need-know
- Copernicus CAMS, Drifting away: MODIS and the CAMS Global Fire Assimilation System (25 Feb 2026; secondary source for NASA plans) — https://atmosphere.copernicus.eu/drifting-away-modis-cams-global-fire-assimilation-system
