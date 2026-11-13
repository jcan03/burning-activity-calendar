# VIIRS instrument specifications and scan geometry

Verified 2026-11-13. The Visible Infrared Imaging Radiometer Suite (VIIRS) flies on Suomi NPP (S-NPP), NOAA-20 (JPSS-1) and NOAA-21 (JPSS-2). All three units share one design. Unit-to-unit differences are listed separately below. Every PDF cited here was opened and its text extracted for checking.

Abbreviations used below:
- **I-band:** imagery band, 375 m at nadir.
- **M-band:** moderate-resolution band, 750 m at nadir.
- **DNB:** Day/Night Band.
- **RSB:** reflective solar band.
- **TEB:** thermal emissive band.
- **NEdT:** noise-equivalent temperature difference.
- **HSI:** horizontal sampling interval, the ground distance between adjacent samples.
- **FRP:** fire radiative power.
- **SRF/RSR:** spectral response function, also called relative spectral response.
- **CFPA:** cold focal plane assembly.
- **MWIR/LWIR:** mid-wave and long-wave infrared.

## Key facts

### Band set

- VIIRS has 22 spectral bands covering 0.402–12.49 µm, in three groups:
  - 16 M-bands at 750 m nadir resolution: 11 RSB and 5 TEB.
  - 5 I-bands at 375 m: I1–I3 are RSB and I4–I5 are TEB.
  - One panchromatic DNB (0.500–0.900 µm), which keeps 750 m resolution across the whole scan.

  Six of the 11 reflective M-bands are dual-gain. [L1B UG 2021](https://ladsweb.modaps.eosdis.nasa.gov/api/v2/content/archives/Document%20Archive/Science%20Data%20Product%20Documentation/NASA_VIIRS_L1B_UG_August_2021.pdf) [confirmed]
- The dual-gain bands are M1–M5, M7 and M13. M13 is the only dual-gain thermal band. [Wolfe et al. 2013](https://ntrs.nasa.gov/api/citations/20140010285/downloads/20140010285.pdf); [Xiong et al. 2016](https://pmc.ncbi.nlm.nih.gov/articles/PMC7430510) [confirmed]
- Older engineering papers count 17 M-bands because they list M16A and M16B separately. M16 is formed by time-delay integration of these two detector sets. [Wolfe et al. 2013](https://ntrs.nasa.gov/api/citations/20140010285/downloads/20140010285.pdf); [Lin et al. 2011](https://ntrs.nasa.gov/api/citations/20110022523/downloads/20110022523.pdf) [confirmed]
- The DNB uses four CCD arrays in three gain stages (high, mid and low). The L1B guide gives a near-constant pixel size of 742 m. Wolfe et al. give 764 m along track and 773 m along scan over the 3000 km swath, using 32 aggregation modes. [L1B UG](https://ladsweb.modaps.eosdis.nasa.gov/api/v2/content/archives/Document%20Archive/Science%20Data%20Product%20Documentation/NASA_VIIRS_L1B_UG_August_2021.pdf); [Wolfe 2013](https://ntrs.nasa.gov/api/citations/20140010285/downloads/20140010285.pdf) [confirmed]
- **NOAA-20 unit only:** detector 29 of band I3 is "extremely noisy". The L1B products keep its calibrated values rather than replacing them with fill, and the pixel-level "Noisy_Detector" flag marks it. This applies to Collections C2 and C2.1. [L1B UG](https://ladsweb.modaps.eosdis.nasa.gov/api/v2/content/archives/Document%20Archive/Science%20Data%20Product%20Documentation/NASA_VIIRS_L1B_UG_August_2021.pdf) [confirmed, added]

### Fire-relevant bands: design specification

The specification values below come from Xiong et al. 2016, Table 1. The centre wavelengths come from the NOAA-21 SDR requirements table. Radiances are in W m⁻² sr⁻¹ µm⁻¹. Ttyp and Tmax are the typical and maximum scene temperatures in the specification.

| Band | Range (µm) | Centre (nm) | Nadir res. | Gain | Ltyp / Ttyp | Lmax / Tmax | Spec SNR / NEdT | Status |
|---|---|---|---|---|---|---|---|---|
| I1 | 0.600–0.680 | 640 | 375 m | single | 22 | 718 | SNR 119 | [confirmed] |
| I2 | 0.846–0.885 | 865 | 375 m | single | 25 | 349 | SNR 150 | [confirmed] |
| I3 | 1.580–1.640 | 1610 | 375 m | single | 7.3 | 72.5 | SNR 6 | [confirmed] |
| I4 | 3.550–3.930 | 3740 | 375 m | single | 270 K | 353 K | 2.5 K | [confirmed] |
| I5 | 10.50–12.40 | 11450 | 375 m | single | 210 K | 340 K | 1.5 K | [confirmed] |
| M5 | 0.662–0.682 | 672 | 750 m | dual | – | – | – | [confirmed, added] |
| M7 | 0.846–0.885 | 865 | 750 m | dual | – | – | – | [confirmed, added] |
| M11 | 2.225–2.275 | 2250 | 750 m | single | 0.12 (Xiong) / 1.0 (NOAA-21 table) | 31.8 | SNR 10 (Xiong) / 90 (NOAA-21 table) | [confirmed; sources conflict] |
| M12 | 3.660–3.840 | 3700 | 750 m | single | 270 K | 353 K | 0.396 K | [confirmed] |
| M13 high gain | 3.973–4.128 | 4050 | 750 m | dual | 300 K | 343 K | 0.107 K | [confirmed] |
| M13 low gain | 3.973–4.128 | 4050 | 750 m | dual | 380 K | 634 K | 0.423 K | [confirmed] |
| M15 | 10.263–11.263 | 10763 | 750 m | single | 300 K | 343 K | 0.07 K | [confirmed] |
| M16 | 11.538–12.488 | 12013 | 750 m | single | 300 K | 340 K | 0.072 K | [confirmed] |

Sources for the table: [Xiong et al. 2016, Remote Sens. 8(2):84](https://pmc.ncbi.nlm.nih.gov/articles/PMC7430510), [NOAA-21 VIIRS Validated Maturity Review (dated 8/3/2023)](https://www.star.nesdis.noaa.gov/JPSS/documents/AMM/N21/NOAA-21_VIIRS_Validated.pdf) and [L1B UG](https://ladsweb.modaps.eosdis.nasa.gov/api/v2/content/archives/Document%20Archive/Science%20Data%20Product%20Documentation/NASA_VIIRS_L1B_UG_August_2021.pdf).

- The NOAA-21 table gives a maximum field of view of 0.4 km at nadir and 0.8 km at edge of scan for the I-bands, and 0.8 km and 1.6 km for the M-bands. The DNB is 0.8 km at both. These are specification maxima, not sampling intervals. [NOAA-21 review](https://www.star.nesdis.noaa.gov/JPSS/documents/AMM/N21/NOAA-21_VIIRS_Validated.pdf) [confirmed]

### Fire-relevant bands: operational behaviour in the fire products

- **I4 saturation.** In the 375 m algorithm, I4 is the primary detection channel. It is single-gain, and its nominal saturation brightness temperature is 367 K. [Schroeder et al. 2014](https://directreadout.sci.gsfc.nasa.gov/publications_documents/Schroeder_et_al_2014b_RSE.pdf); [375 m UG v1.2](https://www.earthdata.nasa.gov/s3fs-public/2025-06/VIIRS_C2_AF-375m_User_Guide_1.2.pdf) [confirmed]
- **I4 saturation scenarios.** The 375 m guide describes three:
  1. Nominal saturation, where the pixel is assigned 367 K.
  2. Fold-over, where the digital number wraps around and the pixel shows an abnormally low temperature. These pixels are identified using I5.
  3. Mixing of saturated and unsaturated native pixels during onboard aggregation, which produces spurious Level 1 radiances. The input data carry no quality flag for this case.

  These scenarios limit I4-based FRP. The fire-pixel I4 brightness temperature (FP_T4) has a typical range of about 208–367 K. [375 m UG v1.2](https://www.earthdata.nasa.gov/s3fs-public/2025-06/VIIRS_C2_AF-375m_User_Guide_1.2.pdf) [confirmed]
- **I5.** I5 is single-gain with a saturation temperature of 380 K. The fire-pixel I5 brightness temperature (FP_T5) has a typical range of about 205–380 K. [Schroeder 2014](https://directreadout.sci.gsfc.nasa.gov/publications_documents/Schroeder_et_al_2014b_RSE.pdf); [375 m UG](https://www.earthdata.nasa.gov/s3fs-public/2025-06/VIIRS_C2_AF-375m_User_Guide_1.2.pdf) [confirmed]
- **I1–I3.** These bands are used for cloud, sun-glint and water discrimination. They operate only during the daytime part of the orbit. [Schroeder 2014](https://directreadout.sci.gsfc.nasa.gov/publications_documents/Schroeder_et_al_2014b_RSE.pdf) [confirmed]
- **I4 versus M13 placement.** The I4 band sits about 0.3 µm shorter than M13. This gives I4 about three times more reflected solar signal than M13. [Schroeder 2014](https://directreadout.sci.gsfc.nasa.gov/publications_documents/Schroeder_et_al_2014b_RSE.pdf) [confirmed]
- **Daytime saturation flag.** Algorithm QA bit 16 is the daytime pixel saturation condition: BT5 ≥ 325 K OR BT4 = 367 K OR DBT45 < 0. [375 m UG](https://www.earthdata.nasa.gov/s3fs-public/2025-06/VIIRS_C2_AF-375m_User_Guide_1.2.pdf) [confirmed]
- **FRP in the 375 m product.** FRP comes from co-located 750 m M13 radiance. All 375 m fire pixels that fall within one 750 m pixel share the same fractional FRP. M13 saturation is extremely rare. When it happens, the 375 m pixel can still be detected, but its FRP is set to zero. [375 m UG](https://www.earthdata.nasa.gov/s3fs-public/2025-06/VIIRS_C2_AF-375m_User_Guide_1.2.pdf) [confirmed]
- **Channels used by the 750 m VNP14 algorithm.** The algorithm uses six channels:

  | Channel | MODIS heritage band | Use |
  |---|---|---|
  | M5 | 1 | Cloud, glint and false-alarm tests |
  | M7 | 2 | Cloud, glint and false-alarm tests |
  | M11 | 7 | Glint and false-alarm tests |
  | M13 | 21/22 | Fire detection and characterization |
  | M15 | 31 | Detection, cloud and false-alarm tests |
  | M16 | 32 | Cloud masking |

  M13 assigns low or high gain dynamically depending on pixel radiance. Its saturation temperature is about 659 K, compared with 500 K for MODIS band 21. [VNP14 750 m ATBD v1.0, Sept 2017](https://LPDAAC.USGS.GOV/documents/133/VNP14_ATBD.pdf) [confirmed, added]
- **750 m product heritage.** The 750 m VNP14 product is an adaptation of the Collection 6 MODIS MOD14/MYD14 algorithm, and its performance is "more comparable" to Aqua MODIS MYD14. The 375 m VNP14IMG product is a separate algorithm. Both products are generated independently for each VIIRS unit. [375 m UG](https://www.earthdata.nasa.gov/s3fs-public/2025-06/VIIRS_C2_AF-375m_User_Guide_1.2.pdf) [confirmed]

### Scan geometry and orbit context

- VIIRS is a whiskbroom scanning radiometer with a 112.56° cross-track field of view, which is ±56.28°. The L1B guide gives a nominal altitude of 829 km (515 mi) and a swath of 3060 km (1901.4 mi). [L1B UG](https://ladsweb.modaps.eosdis.nasa.gov/api/v2/content/archives/Document%20Archive/Science%20Data%20Product%20Documentation/NASA_VIIRS_L1B_UG_August_2021.pdf) [confirmed]
- Wolfe et al. 2013 describe the S-NPP orbit as having:
  - 840 km mean altitude
  - 98.7° inclination
  - 101.5 min period
  - ascending equator crossing at 13:30 ±10 min local time

  [Wolfe 2013](https://ntrs.nasa.gov/api/citations/20140010285/downloads/20140010285.pdf) [confirmed, added]
- **Granule and coverage.** A Level 2 granule covers 6 minutes, which is about 202 scans. Each I-band scan has 32 detector rows and 6400 samples per row, and the swath is about 3060 km wide. Consecutive orbits overlap by about 15% at the equator, giving global coverage every 12 h. S-NPP equator crossings are at 13:30 and 01:30 local time. Mid-latitudes get 3–4 looks per day. [375 m UG](https://www.earthdata.nasa.gov/s3fs-public/2025-06/VIIRS_C2_AF-375m_User_Guide_1.2.pdf) [confirmed]
- **Detectors.** Each M-band has 16 detectors and each I-band has 32. The detectors are optically rectangular, with the smaller dimension along scan. [Wolfe 2013](https://ntrs.nasa.gov/api/citations/20140010285/downloads/20140010285.pdf) [confirmed]
- **Rotating telescope.** The telescope rotates continuously with a half-angle mirror. NOAA-21 on-orbit values:
  - average scan period about 1.789730 s
  - Earth-view scan time about 0.563798 s
  - scan rate about 3.510688 rad/s, defined as 2π divided by the scan period

  These are stable and consistent with the pre-launch values. The source is the NOAA-21 SDR Validated Maturity Review, presented 3 August 2023. [NOAA-21 review](https://www.star.nesdis.noaa.gov/JPSS/documents/AMM/N21/NOAA-21_VIIRS_Validated.pdf) [corrected: the review is dated 3 Aug 2023, not July 2023; its performance table is "as of 7/14/2023"]
- **Pre-launch geometry parameters.** Lin et al. assumed a scan rate of 3.531 rad/s, an unaggregated angular sampling interval of 155.83 µrad and a track angular sampling interval of 455.5 µrad. [Lin et al. 2011](https://ntrs.nasa.gov/api/citations/20110022523/downloads/20110022523.pdf) [confirmed, added]

### Along-scan aggregation zones

| Zone | Aggregation | Scan angle (Schroeder 2014) | Scan angle (VNP14 ATBD 2017) | I-band samples | Status |
|---|---|---|---|---|---|
| 1 (nadir) | 3 native samples to 1 | 0 to ±31.72° | 0 to 31.59° | 1184 | [confirmed] |
| 2 | 2 to 1 | ±31.72 to ±44.86° | 31.59 to 44.68° | 736 | [confirmed] |
| 3 (edge) | 1 to 1 | ±44.86 to ±56.28° | 44.68 to 56.06° | 1280 | [confirmed] |

- Before aggregation, a native I-band sample is about 125 × 375 m at nadir. The three zones total 6400 I-band samples. [Schroeder 2014](https://directreadout.sci.gsfc.nasa.gov/publications_documents/Schroeder_et_al_2014b_RSE.pdf); [VNP14 ATBD](https://LPDAAC.USGS.GOV/documents/133/VNP14_ATBD.pdf) [confirmed]
- Aggregation is done onboard for the single-gain bands. For the dual-gain bands (M1–M5, M7, M13) it is done during ground processing to match, so unaggregated raw data records remain available. Aggregation limits pixel growth along scan to roughly the growth along track, giving a maximum of about 2 times the nadir size at end of scan. [Wolfe 2013](https://ntrs.nasa.gov/api/citations/20140010285/downloads/20140010285.pdf); [L1B UG](https://ladsweb.modaps.eosdis.nasa.gov/api/v2/content/archives/Document%20Archive/Science%20Data%20Product%20Documentation/NASA_VIIRS_L1B_UG_August_2021.pdf) [confirmed]

### Pixel dimensions (horizontal sampling interval)

These are nominal I-band HSI values from Lin et al. 2011, Table 1. They assume 824 km altitude, an Earth radius of 6378 km and a scan rate of 3.531 rad/s. The paper states that M-band HSIs are twice the I-band values; the M-band columns below were calculated from that statement.

| Position | I scan (m) | I track (m) | M scan (m, 2×) | M track (m, 2×) | Status |
|---|---|---|---|---|---|
| Nadir | 385 | 367 | 770 | 734 | [confirmed] |
| End of 3×1 zone (31.72°) | 577 | 443 | 1154 | 886 | [confirmed] |
| Start of 2×1 zone | 385 | 443 | 770 | 886 | [confirmed] |
| End of 2×1 zone (44.86°) | 644 | 556 | 1288 | 1112 | [confirmed] |
| Start of 1×1 zone | 322 | 556 | 644 | 1112 | [confirmed] |
| End of scan (56.28°) | 822 | 807 | 1644 | 1614 | [confirmed] |

Source: [Lin, Wolfe, Nishihama 2011, NPP VIIRS Geometric Performance Status](https://ntrs.nasa.gov/api/citations/20110022523/downloads/20110022523.pdf).

- Schroeder et al. give the effective I-band footprint as 383 × 360 m at the sub-satellite point and 795 × 784 m at 56.28°. [Schroeder 2014](https://directreadout.sci.gsfc.nasa.gov/publications_documents/Schroeder_et_al_2014b_RSE.pdf) [confirmed]
- The area ratio between edge and nadir is about 4.5× with the Schroeder values (about 623,000 vs 138,000 m²). The researcher's figure of "2.2× nadir" was linear, not area. This is a calculation, not a quoted value. [corrected: the area ratio is about 4.5×; the linear growth is about 2× per axis]

### Bow-tie deletion

- **I-bands.** Fill values replace the 4 outermost rows of each scan (2 at each end) in zone 2, and the 8 outermost rows (4 at each end) in zone 3. This removes about 50% of the data redundancy in the SDR and produces a striped pattern. [Schroeder 2014](https://directreadout.sci.gsfc.nasa.gov/publications_documents/Schroeder_et_al_2014b_RSE.pdf) [confirmed]
- **M-bands.** Readings from "one and two detectors from the top and bottom of the arrays are not transmitted" in the 2×1 and 1×1 zones. For the I-bands the same passage says "two and four detectors". Read together with Schroeder's per-end I-band counts, this means 1 (zone 2) and 2 (zone 3) M-band detectors are deleted at each end. Lin et al. use the same wording ("trim 1 (2) and 2 (4) M (I) band detectors at the scan edges"). [Wolfe 2013](https://ntrs.nasa.gov/api/citations/20140010285/downloads/20140010285.pdf); [Lin 2011](https://ntrs.nasa.gov/api/citations/20110022523/downloads/20110022523.pdf) [confirmed; the per-end reading is consistent with Schroeder]
- **Fire mask handling.** In VNP14IMG, fire mask class 1 marks bow-tie-deleted pixels. Residual bow-tie pixels that are still present in the input are processed. Fire pixels found there go to fire mask classes 7–9 and are flagged in algorithm QA bit 22 ("Residual bowtie pixel"). [375 m UG](https://www.earthdata.nasa.gov/s3fs-public/2025-06/VIIRS_C2_AF-375m_User_Guide_1.2.pdf) [confirmed]

### Record start and unit histories

- **S-NPP.** VIIRS was first deployed on S-NPP in October 2011. NOAA-20 launched in 2017 and NOAA-21 in 2022. The first VIIRS active fires were detected on 19 January 2012. The 375 m products are VNP14IMG (S-NPP), VJ114IMG (NOAA-20) and VJ214IMG (NOAA-21). [375 m UG](https://www.earthdata.nasa.gov/s3fs-public/2025-06/VIIRS_C2_AF-375m_User_Guide_1.2.pdf) [confirmed]
- **NOAA-21 launch.** NOAA-21 launched on 10 November 2022. Key VIIRS events:

  | Date | Event |
  |---|---|
  | 5 Dec 2022 | Nadir aperture door opened |
  | 8 Feb 2023 | Cryoradiator cooler door opened |
  | 23 Feb 2023 | Mid-mission outgassing #1 |
  | 3 Mar 2023 | CFPA set point changed from 82 K to 80 K |
  | 26 Feb 2024 | Mid-mission outgassing #2 |
  | 22 Jun 2024 | Spacecraft safe mode |
  | 1 Oct 2025 | Spacecraft safe mode |

  [Angal et al., SPIE 2026](https://ntrs.nasa.gov/api/citations/20260008550/downloads/SPIE26_N21TEB_Angal_revD_assubmitted.pdf) [confirmed, added]
- **NOAA-21 safe mode, 22 June 2024.** The impact began at 04:24Z. VIIRS returned to its operational state at 09:33:57 UTC, and VIIRS products were cleared for operations at 16:45 UTC the same day. [NOAA OSPO 2024-07-08](https://ospo.noaa.gov/data/messages/2024/07/MSG_20240708_1626.html) [confirmed, added]
- **NOAA-21 VIIRS safe mode, 1 October 2025.** The data outage began at 19:09:10 UTC with the end listed as TBD. A closing notice was not found. [NOAA OSPO 2025-10-01](https://ospo.noaa.gov/data/messages/2025/10/MSG_20251001_2050.html) [confirmed, added]
- **NOAA-21 short outage, 18 September 2025.** A separate instrument issue on this date was recovered the same day. [NOAA OSPO](https://ospo.noaa.gov/data/messages/2025/09/MSG_20250918_0915.html) [unverified: seen in search results only, not opened]
- **NOAA-21 LWIR anomaly, July 2026.** From 05:42 UTC on 28 July 2026, LWIR data (M14–M16 and I5) were anomalous, and users were told to use caution until 20:10 UTC on 29 July. There is a data gap from 16:42 to 18:18 UTC on 29 July 2026. The issue was resolved on 31 July 2026, and data from 28 July onward was judged good. [Earthdata alert](https://www.earthdata.nasa.gov/data/alerts-outages/viirs-noaa-21-data-anomaly) [confirmed, added]
- **S-NPP anomaly, March 2026.** Data after 17:45 UTC on 9 March 2026 was to be used with caution. VIIRS data from 18:00 UTC on 9 March to 08:12 UTC on 13 March 2026 is hidden and unprocessed because of "unrecoverable geolocation errors". The spacecraft was nominal again at 17:17 UTC on 12 March, and products were cleared on 16 March 2026. [Earthdata alert](https://www.earthdata.nasa.gov/data/alerts-outages/suomi-npp-data-imagery-caution-advised) [confirmed, added]
- **S-NPP end of data.** NOAA NESDIS announced the permanent end of S-NPP science data delivery, including VIIRS. The original date was 1 November 2026 13:00 UTC, later revised to 2 November 2026 13:00 UTC. According to an Earthdata update on 2 November, delivery actually ended at 15:40 UTC on 2 November 2026. NOAA's announcement also covers decommissioning of the satellite. Users are directed to NOAA-21 (primary) and NOAA-20 (secondary). NASA continues to archive and distribute the S-NPP record. [NOAA NESDIS notice](https://www.nesdis.noaa.gov/news/cessation-of-suomi-national-polar-orbiting-partnership-s-npp-data-users-onafter-november-2-2026); [Earthdata reminder, updated 10 Nov 2026](https://www.earthdata.nasa.gov/data/alerts-outages/reminder-new-suomi-npp-observations-cease-november-2-2026); [Earthdata notice](https://www.earthdata.nasa.gov/data/alerts-outages/suomi-npp-observations-cease-november-2-2026) [confirmed, added]
- **Current NOAA-20 and NOAA-21 outage.** An active outage was issued on 9 November 2026. Both satellites have VIIRS data gaps on 5–6 November 2026, and NOAA-20 also has a gap on 7 November 2026. These gaps are delaying downstream products, and the resolution is TBD. [Earthdata alert](https://www.earthdata.nasa.gov/data/alerts-outages/jpss1-noaa-20-jpss2-noaa-21-viirs-data-gaps-processing-delays-from-november-5) [confirmed, added]

### Unit-to-unit differences in fire-relevant bands

- **NOAA-21 M13.** The M13 spectral response of NOAA-21 differs from that of NOAA-20. The maturity review states that "Fire measurements would be hotter on NOAA-21 (BT21 > BT20)" and that this "May affect saturation level". Fire-user feedback from STAR in the same review reported:
  - the NOAA-21 product is very similar to S-NPP and NOAA-20
  - I4 saturation and folding appear as usual
  - M13 radiances shift a bit because of the SRF shift

  [NOAA-21 review](https://www.star.nesdis.noaa.gov/JPSS/documents/AMM/N21/NOAA-21_VIIRS_Validated.pdf) [confirmed]
- **S-NPP versus NOAA-20.** The two units have identical designs, with small RSR differences in most bands. In thermal emissive bands M13 and M16, the RSR-induced bias is larger than 0.02 K for all six test atmospheres, and its atmospheric dependence is below 0.06 K. NOAA-20 TEB striping is expected to be about 20% less than on S-NPP. [Lin & Cao 2019, IEEE JSTARS 12(10)](https://repository.library.noaa.gov/view/noaa/45210/noaa_45210_DS1.pdf) [confirmed]
- **NOAA-21 on-orbit NEdT versus specification.** The values below are as of 14 July 2023. NOAA-21 TEB NEdTs are comparable to NOAA-20 and S-NPP. [NOAA-21 review](https://www.star.nesdis.noaa.gov/JPSS/documents/AMM/N21/NOAA-21_VIIRS_Validated.pdf) [confirmed]

  | Band | On-orbit NEdT (K) | Specification (K) |
  |---|---|---|
  | I4 | 0.41 | 2.5 |
  | I5 | 0.35 | 1.5 |
  | M12 | 0.15 | 0.396 |
  | M13 | 0.04 | 0.107 |
  | M15 | 0.02 | 0.07 |
  | M16 | 0.02 | 0.072 |

- **S-NPP NEdT trend.** Measured at the blackbody temperature of about 292 K, S-NPP NEdT stayed stable at 0.14–0.18 K for the I-bands and 0.03–0.06 K for the M-bands. Some detectors are consistently noisier than the rest of their band: I5 detector 2, M12 detector 16 and M16A detector 9. [Xiong 2016](https://pmc.ncbi.nlm.nih.gov/articles/PMC7430510) [confirmed]
- **NOAA-21 MWIR gain, 2023 review.** MWIR gains had been "continuously degrading since mid-Match [sic]". Band-averaged degradation reached about 2.5%, and more than 4% for some I4 and M12 detectors. The impact on NEdT and SDRs was negligible at that point. LWIR degradation has been below 0.4% since the CFPA was set to 80 K. [NOAA-21 review](https://www.star.nesdis.noaa.gov/JPSS/documents/AMM/N21/NOAA-21_VIIRS_Validated.pdf) [confirmed]
- **NOAA-21 MWIR gain, SPIE 2026 paper.** The researcher's statement that the SPIE paper "confirms MWIR degrading again since mid-March 2023" is not what the extracted text says. The paper attributes gain loss to ice contamination in the dewar. The two outgassing events (23 Feb 2023 and 26 Feb 2024) appear as discontinuities, and gains are stable within each of three periods through April 2026. NEdT for all TEB stays well within specification. M12 and M13 calibration uncertainty is out of specification at cold scenes: M13 reaches 6.82% (0.93 K) against a 0.85 K specification. At 270 K both bands are compliant (M13 0.13 K). [Angal et al., SPIE 2026](https://ntrs.nasa.gov/api/citations/20260008550/downloads/SPIE26_N21TEB_Angal_revD_assubmitted.pdf) [corrected]

## Why these matter for combining the records

- **Pixel size by scan angle.** VIIRS I-band pixels grow only about 2× per axis, or about 4.5× in area, from nadir to the swath edge. They also change size in steps at about 31.7° and 44.9° scan angle. MODIS 1 km pixels grow much more. Detection sensitivity and FRP per pixel therefore depend on scan angle differently for the two sensors.
- **Saturation.** The 375 m product saturates often in I4 at 367 K, so it takes FRP from the 750 m M13 band (saturating near 634–659 K). FRP in the 375 m product is effectively on a 750 m footing, and is shared out among its 375 m pixels.
- **Duplicate detections.** Residual bow-tie overlap can report one fire twice in adjacent scans. Algorithm QA bit 22 identifies these pixels.
- **Units are not identical.** NOAA-21's M13 spectral response differs, and fire temperatures read hotter on NOAA-21. The S-NPP to NOAA-20 difference is about 0.02 K.
- **Record breaks.** The S-NPP VIIRS record ends on 2 November 2026. There are documented gaps, including 9–13 March 2026 (S-NPP), 22 June 2024 and 1 October 2025 (NOAA-21 safe modes), and 5–7 November 2026 (NOAA-20 and NOAA-21). These affect monthly counts in those months.

## Conflicts and unverified items

- **Swath width.** Three values appear:
  - 3060 km in the NASA L1B guide (2021) and the 375 m UG v1.2 (2025)
  - about 3000 km in Schroeder 2014 and Wolfe 2013
  - about 3040 km in Xiong 2016

  The NASA product guides are the current reference for the products. The other figures are rounded or older.
- **Altitude.** Three values are used in geometry:
  - 829 km in the L1B guide
  - 824 km in Lin 2011, used for the HSI table
  - 840 km mean altitude in Wolfe 2013

  These lead to slightly different footprints: 385 × 367 m at nadir and 822 × 807 m at the edge (Lin), versus 383 × 360 m and 795 × 784 m (Schroeder).
- **Zone boundaries.** Schroeder 2014 gives 31.72°, 44.86° and 56.28°. The VNP14 ATBD (2017) gives 31.59°, 44.68° and 56.06°. Neither source explains the difference. The 56.28° value agrees with the 112.56° field of view in the L1B guide, so the Schroeder and L1B set is better supported.
- **I4 and I5 maximum temperatures.** The design Tmax is 353 K for I4 and 340 K for I5 (Xiong 2016). The operational saturation values are 367 K for I4 and 380 K for I5 (Schroeder 2014; 375 m UG 2025). The operational values describe the data users actually receive.
- **M13 saturation.** The design low-gain Tmax is 634 K (Xiong 2016). The VNP14 ATBD (2017) gives an operational saturation of about 659 K.
- **M11 specification.** Xiong 2016 gives Ltyp 0.12, Lmax 31.8 and SNR 10. The NOAA-21 SDR table gives Ltyp 1.0 and SNR 90. The two may be different specification points; this is not resolved.
- **M13 gain labels.** The NOAA-21 table lists M13 Ttyp as "380, 300 (LG, HG)" and NEdT as "0.107, 0.423 (LG, HG)". The NEdT order looks swapped relative to Xiong 2016, which gives high gain 0.107 K and low gain 0.423 K. Xiong is used here.
- **DNB pixel size.** The L1B guide gives 742 m. Wolfe 2013 gives 764 m along track and 773 m along scan.
- **M-band count.** Engineering papers count 17 M-bands (M16A and M16B separately). The product guides count 16.
- **Scan rate.** Lin 2011 used 3.531 rad/s as a pre-launch assumption. The NOAA-21 on-orbit average is 3.510688 rad/s (2023).
- **CIRA Quick Guide.** The researcher's VIIRS Active Fire Quick Guide (CIRA, 2022) was not opened. Its band wavelengths are supported here by the primary L1B guide and the NOAA-21 table instead.
- **Unverified:** the 18 September 2025 NOAA-21 outage was seen only in search results. A closing notice for the 1 October 2025 NOAA-21 safe mode was not found.

## Open questions

- No measured I4 or I5 saturation temperatures specific to NOAA-20 or NOAA-21 were found. The NOAA-21 review says only that saturation and folding appear "as usual" and that the M13 SRF shift "may affect saturation level".
- The size of the NOAA-21 versus NOAA-20 M13 brightness-temperature offset for fire scenes is not quantified in any primary source opened.
- The source does not give the duration of, or the data recovered after, the 1 October 2025 NOAA-21 VIIRS safe mode.
- The 750 m user guide (Giglio et al. 2024) was not located. Channel use for the 750 m product is taken from the 2017 ATBD.
- No NOAA-20 VIIRS instrument anomaly affecting the fire bands was found for 2025–2026, only ground and data delays.
- The source of the small differences in zone-boundary angles (31.59 vs 31.72°, and so on) is not documented.

## Sources

- [NASA VIIRS Level-1B Product User Guide, August 2021 (LAADS)](https://ladsweb.modaps.eosdis.nasa.gov/api/v2/content/archives/Document%20Archive/Science%20Data%20Product%20Documentation/NASA_VIIRS_L1B_UG_August_2021.pdf)
- [VIIRS (VNP14IMG, VJ114IMG, VJ214IMG) 375 m Active Fire Product User's Guide, Collection 2, v1.2, June 2025](https://www.earthdata.nasa.gov/s3fs-public/2025-06/VIIRS_C2_AF-375m_User_Guide_1.2.pdf)
- [VIIRS 750 m Active Fire Detection and Characterization ATBD 1.0, September 2017 (LP DAAC)](https://LPDAAC.USGS.GOV/documents/133/VNP14_ATBD.pdf)
- [Schroeder et al. 2014, The New VIIRS 375 m active fire detection data product, Remote Sensing of Environment 143:85–96](https://directreadout.sci.gsfc.nasa.gov/publications_documents/Schroeder_et_al_2014b_RSE.pdf)
- [Wolfe et al. 2013, Suomi NPP VIIRS prelaunch and on-orbit geometric calibration and characterization, JGR Atmospheres 118](https://ntrs.nasa.gov/api/citations/20140010285/downloads/20140010285.pdf)
- [Lin, Wolfe, Nishihama 2011, NPP VIIRS Geometric Performance Status (SPIE)](https://ntrs.nasa.gov/api/citations/20110022523/downloads/20110022523.pdf)
- [Xiong et al. 2016, Assessment of S-NPP VIIRS On-orbit Radiometric Calibration and Performance, Remote Sensing 8(2):84](https://pmc.ncbi.nlm.nih.gov/articles/PMC7430510)
- [NOAA STAR, Validated Maturity Science Review for NOAA-21 VIIRS SDR, 3 Aug 2023](https://www.star.nesdis.noaa.gov/JPSS/documents/AMM/N21/NOAA-21_VIIRS_Validated.pdf)
- [Lin & Cao 2019, Effects of VIIRS detector-level and band-averaged RSR differences in the TEBs, IEEE JSTARS 12(10)](https://repository.library.noaa.gov/view/noaa/45210/noaa_45210_DS1.pdf)
- [Angal et al. 2026, On-Orbit Calibration Assessment of NOAA-21 VIIRS Thermal Emissive Bands (SPIE)](https://ntrs.nasa.gov/api/citations/20260008550/downloads/SPIE26_N21TEB_Angal_revD_assubmitted.pdf)
- [NOAA NESDIS: Cessation of S-NPP data to users on/after November 2, 2026](https://www.nesdis.noaa.gov/news/cessation-of-suomi-national-polar-orbiting-partnership-s-npp-data-users-onafter-november-2-2026)
- [NASA Earthdata: Suomi NPP Observations to Cease on November 2, 2026](https://www.earthdata.nasa.gov/data/alerts-outages/suomi-npp-observations-cease-november-2-2026)
- [NASA Earthdata: Reminder, new Suomi NPP observations cease November 2, 2026 (updated 10 Nov 2026)](https://www.earthdata.nasa.gov/data/alerts-outages/reminder-new-suomi-npp-observations-cease-november-2-2026)
- [NASA Earthdata: Suomi NPP data imagery caution advised (March 2026)](https://www.earthdata.nasa.gov/data/alerts-outages/suomi-npp-data-imagery-caution-advised)
- [NASA Earthdata: VIIRS NOAA-21 Data Anomaly (July 2026)](https://www.earthdata.nasa.gov/data/alerts-outages/viirs-noaa-21-data-anomaly)
- [NASA Earthdata: NOAA-20 and NOAA-21 VIIRS data gaps from November 5, 2026](https://www.earthdata.nasa.gov/data/alerts-outages/jpss1-noaa-20-jpss2-noaa-21-viirs-data-gaps-processing-delays-from-november-5)
- [NOAA OSPO: NOAA-21 VIIRS data loss, safe mode, 1 Oct 2025](https://ospo.noaa.gov/data/messages/2025/10/MSG_20251001_2050.html)
- [NOAA OSPO: NOAA-21 recovery notices, June–July 2024](https://ospo.noaa.gov/data/messages/2024/07/MSG_20240708_1626.html)
