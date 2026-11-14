# Correcting for overpass time, the daily fire cycle, observation opportunity and cloud

## Summary

This family of methods adjusts satellite fire observations for when a sensor looks (its local overpass time against the daily, or diurnal, fire cycle), how often it looks (the number of overpasses, which rises with latitude), and whether it could see the ground (cloud). All of them have been used for fire: NASA's gridded MODIS (Moderate Resolution Imaging Spectroradiometer) fire product corrects counts for overpasses and cloud, the Global Fire Emissions Database version 5 (GFED5) applies a cosine-of-latitude factor, and emissions systems scale fire radiative power (FRP, the heat output a sensor measures) to a daily total with Gaussian diurnal curves built from geostationary satellites. Almost every diurnal correction was built and tested for FRP or fire radiative energy (FRE, FRP integrated over time), not for detection counts, and none is specific to Interior British Columbia (BC) conifer forest. The count corrections that need pixels observed or cloud fraction cannot be computed from FIRMS (Fire Information for Resource Management System) point rows, which record only detections. What can be done from the rows is descriptive (the local solar time of each hotspot) or approximate (weighting by a published curve), and no source tests either at the scale of one month and a user-selected area.

## Methods

| Method | How it works | Where used | Data needed | Main assumption | Known failure mode |
|---|---|---|---|---|---|
| Bimodal Gaussian diurnal curve by land cover | Fits two Gaussian peaks to hourly geostationary FRP; scales Visible Infrared Imaging Radiometer Suite (VIIRS) day and night FRP to any hour (Eqs. 3-5). North American forest: peaks 14.57 h (width 2.81 h) and 19.59 h (0.55 h). | [Gui et al. 2026](https://doi.org/10.3390/rs18010052), GOES-16, 12-62°N, 2018-2020 | Local time of each observation, curve parameters, day and night values | One shape per land cover for a whole continent | No accuracy stated for the fit; built for FRP; authors say a single Gaussian "fails to accurately reproduce the diurnal patterns" |
| Climatological Gaussian versus persistence | Models FRP between MODIS looks either as a Gaussian per land cover (peak hour refitted daily) or by carrying the last value forward | [Andela et al. 2015](https://doi.org/10.5194/acp-15-8831-2015), Africa and Mediterranean, SEVIRI geostationary data | Overpass times, night baseline, land cover | Shape is stable by land cover | Hourly correlation with truth about 0.2 at 0.1°; temperate forest FRE overestimated by 18%; persistence beat the curve at 0.1° daily (r 0.50 against 0.27) |
| Single-satellite regression | Regresses Terra-only or Aqua-only daily FRP on the merged Terra-plus-Aqua field per region, then applies it where only one exists | [Remy and Kaiser 2014](https://doi.org/10.5194/acp-14-13377-2014), Global Fire Assimilation System (GFAS), Terra-only 2000-2002 | A period with both sensors | Relationship fitted in 2003-2011 holds elsewhere in time | Terra fits weaker (r² 0.5-0.8 against 0.85-1 for Aqua); boreal coefficients near 1 for FRP |
| Terra-only coefficients | Separate burned-area coefficients fitted from Terra alone for 2001-2002 | [Chen et al. 2023, GFED5](https://doi.org/10.5194/essd-15-5227-2023), Sect. 2.4.4 | As above | As above | Checked only at large scales (supplement not opened) |
| Overpass-corrected count | Fire pixels × days × area ratio × expected equatorial pixels ÷ all pixels observed in the cell that month | [Giglio, Csiszar and Justice 2006](https://doi.org/10.1029/2005JG000142), Eq. 1; MOD14CMQ/MYD14CMQ layer `CorrFirePix` | Total pixels observed (`TotalPix`) | Fire density per observed pixel is representative | No accuracy given; counts "biased at high latitudes owing to nonuniform spatial and temporal sampling" |
| Cloud-corrected count | Overpass-corrected count ÷ (1 − cloud fraction) | Same, Eq. 3; layer `CloudCorrFirePix` | Cloud pixels per cell | Fire density under cloud equals clear sky | Overcorrects: about +20% counts with no change in seasonality; correlation with burned area "almost uniformly lower" ([Giglio et al. 2006, ACP](https://doi.org/10.5194/acp-6-957-2006)) |
| Cosine-of-latitude factor | Multiplies MODIS active-fire area by cos(latitude) to normalise to equatorial overpass frequency | GFED5, Sect. 2.2.2 | Latitude | Coverage scales with cos(latitude) | Only matters across latitudes; applied to gridded active-fire area, not raw counts |
| Daily equatorial coverage | c_eq = w ÷ (π R_E sin γ) × (24 h ÷ T), from swath w, inclination γ, period T | Giglio et al. 2006 ACP, Eq. 4, to compare sensors | Orbit and swath constants | Equator stands for all latitudes | A comparison tool, not a correction |
| Nadir-equivalent looks and "observability" | Counts looks per place from swath geometry, masks cloud, normalises by a geostationary diurnal cycle against an ideal hourly system | [Hyer et al. 2015 poster](https://espo.nasa.gov/sites/default/files/documents/Hyer.pdf) (not peer reviewed) | Swath geometry, cloud mask, diurnal climatology | Diurnal climatology applies | Authors: observability "in many locations is near zero"; "simple scaling of observed fires is unlikely to work when observability is this low" |
| Overpass reconstruction from granule metadata | Uses per-granule footprint files to list every pass, including passes with no fire | [Luo et al. 2024](https://doi.org/10.1038/s41586-024-07028-5) (data statement: MODIS and VIIRS geoMeta products "for reconstructing overpasses") | geoMeta daily files from LAADS (MODIS from 2000, VIIRS from 2012) | Footprint equals usable view | Method details not read; cloud still unknown |

## How each would map onto MODIS and VIIRS hotspots

**What is published on the drift.** NSIDC states that Terra reached 10:15 AM mean local time in October 2022 and would reach 9:00 AM around December 2025, and that Aqua would reach 3:50 PM around August 2026. The MODIS fire lead's May 2025 slides list diurnal sampling, pixel size, scan gaps and bow-tie overlap as affected and say the impact on fire products is "under active investigation" (Giglio 2025). The closest measured precedent is in a different sensor, the Advanced Very High Resolution Radiometer (AVHRR): a drift of up to about 5 hours produced "a ∼90% decline in the number of observed fires", and the authors conclude that correction "is essential even over short time periods" (Weber and Wunderle 2019, abstract). The team's Terra daytime figures are, as far as was found, the only count measurement for 2022-2026. A pre-drift Siberian comparison found more Terra than Aqua counts and 17% higher Aqua FRP (Mokhov and Sitnov, preprint), and Giglio et al. 2006 (JGR) found Terra and Aqua "about evenly matched" in boreal North America, though they warn that at boreal latitudes the overlapping look times "can potentially mute the apparent magnitude of the diurnal fire cycle".

**Local solar time and a published curve.** Steps: compute local solar time (UTC time plus longitude ÷ 15 hours) for each daytime hotspot, then weight Terra and Aqua counts by the ratio of a Gaussian at a reference time to the Gaussian at the observed time. With Gui's forest first mode (14.57 h, 2.81 h), the weight is 0.48 at Terra's 11:10, 0.18 at 09:20 and 0.81 at the VIIRS time of about 12:45 (my arithmetic). That predicts Terra daytime at 0.37 of its stable level in 2026; the team measured 0.46, and 0.77 against a predicted 0.74 in 2024. It would address the drift of Terra by day and of Aqua (now 14:51), which the evidence identifies as the main 2026 problem. It would not fix the 15-30% single-month scatter, the night ratio (0.18, unstable), or MODIS months with zero hotspots. The data are in hand, but the curve is for FRP, a continental domain and 2018-2020, and it multiplies Terra 2026 counts by about 2.7, amplifying noise. Effort: hours.

**A curve built from the team's own record.** Steps: histogram VIIRS and MODIS detection times in the box for 2012-2021 and use that as the shape. It is closer to the place and the unit (counts), but every point comes from a satellite overpass, so it samples only about four local times a day and cannot see the hours between. No published method does this for counts. Effort: hours to a day.

**Single-satellite regression.** The team's ratio factors fitted over the stable-orbit period are this method in count form. Remy and Kaiser support the idea, and their boreal result (coefficients near 1) suggests a small morning-afternoon gap for intense forest fires, but it was for FRP on a daily 0.5° grid. A factor cannot be fitted on drift years without a stable reference, which here is VIIRS. Effort: hours.

**Day and night split.** Supported qualitatively: Luo et al. found 99% of overnight burning events in fires over 1,000 ha, and Giglio et al. 2006 (JGR) note that boreal fires burn for days to weeks. This explains why the night ratio swings with fire size but gives no conversion factor. Effort: hours.

**Gridded corrected counts from NASA.** The MOD14CMQ/MYD14CMQ files give `CorrFirePix`, `CloudCorrFirePix`, `TotalPix` and `MeanCloudFraction` per 0.25° cell per month ([MODIS Collection 6/6.1 user guide](https://modis-fire.umd.edu/files/MODIS_C6_C6.1_Fire_User_Guide_1.0.pdf), Table 9). The team does not have them; they cover MODIS only (no VIIRS equivalent was found), and a 0.25° cell (about 28 by 18 km at 50°N) is coarser than a 10 km circle. Effort: a day.

**Overpass list from geoMeta or FIRMS swath outlines.** This is the only source found for passes that saw nothing. LAADS lists daily geoMeta files for Terra and Aqua (2000-2026) and Suomi NPP, NOAA-20 and NOAA-21 (2012-2026); downloading them requires an Earthdata login, and their contents were not inspected. FIRMS added swath outlines to its map viewer in June 2026; the announcement says they show "when/if that location was or will be observed" but warns against using them at swath edges and gives no archive range or download. Either would let a month be divided by passes over the area, but not by clear-sky passes. Effort: a day or more.

**Distinct detecting passes as a stand-in.** Counting distinct satellite-time clusters with at least one hotspot measures detections, not looks. The team already uses it as a daily availability flag for VIIRS. As a coverage normaliser it fails exactly where it is needed: a quiet month and a missed pass look the same, and below 50 km radius MODIS sees nothing in a third or more of fire months. No published method found. Effort: hours.

## Not applicable, and why

- Overpass-corrected counts computed from FIRMS rows: need all pixels observed, which rows do not hold.
- Cloud correction: needs cloud fraction, and overcorrects even where it is available.
- Cosine-of-latitude factor: a near-constant across a 49-52.5°N box, so it cancels against the same area's own history.
- Persistence models and FRE integration: give energy between looks, not monthly counts.
- Hourly geostationary blends such as [Li et al. 2022](https://doi.org/10.1016/j.rse.2022.113237): need GOES data and days of work; context only.
- Nadir-equivalent looks: need swath geometry and cloud masks.

## Unconfirmed

- Giglio 2007, Remote Sensing of Environment 108:407-421 (doi:10.1016/j.rse.2006.11.018): Crossref confirms the citation; the text could not be opened (403), so its reported peak times (13:00-18:30) and its warning about spurious AVHRR trends are not used.
- Wooster et al. 2021, the most recent general review of satellite active-fire sensing (doi:10.1016/j.rse.2021.112694): confirmed by Crossref, text blocked; not read.
- Freeborn et al. 2011 (MODIS sampling and FRE, doi:10.1016/j.rse.2010.09.017), Freeborn et al. 2022 (night-time fire across the conterminous United States, doi:10.1016/j.rse.2021.112777) and Li et al. 2022: citations confirmed, text not opened; no numbers used.
- Weber and Wunderle 2019: abstract only, via Crossref.
- Luo et al. 2024: abstract, data statement and figure captions read; methods not read.
- Balch et al. 2022, Vermote et al. 2009, Ellicott et al. 2009, Roberts et al. 2009, Mu et al. 2011, Zhang et al. 2012: not opened.
- No peer-reviewed measurement of the 2022-2026 drift effect on MODIS fire counts was found; web searching ran out before a final check.

## Sources

- Andela N, Kaiser JW, van der Werf GR, Wooster MJ (2015). Atmos. Chem. Phys. 15:8831-8846. https://doi.org/10.5194/acp-15-8831-2015
- Chen Y et al. (2023). GFED5. Earth Syst. Sci. Data 15:5227-5259. https://doi.org/10.5194/essd-15-5227-2023
- Giglio L, Csiszar I, Justice CO (2006). J. Geophys. Res. 111:G02016. https://doi.org/10.1029/2005JG000142
- Giglio L, van der Werf GR, Randerson JT, Collatz GJ, Kasibhatla P (2006). Atmos. Chem. Phys. 6:957-974. https://doi.org/10.5194/acp-6-957-2006
- Giglio L, Schroeder W, Hall JV, Justice CO (2021). MODIS Collection 6 and 6.1 Active Fire Product User's Guide v1.0. https://modis-fire.umd.edu/files/MODIS_C6_C6.1_Fire_User_Guide_1.0.pdf
- Giglio L (2025). Terra/Aqua Orbit-Drift Update, LANCE User Working Group. https://landweb.modaps.eosdis.nasa.gov/data/filePost/LANCE_UWG_Orbit_Drift_Giglio_202505.pdf
- Gui L et al. (2026). Remote Sens. 18:52. https://doi.org/10.3390/rs18010052
- Hyer EJ et al. (2015). SEAC4RS poster. https://espo.nasa.gov/sites/default/files/documents/Hyer.pdf
- LAADS DAAC geoMeta archive. https://ladsweb.modaps.eosdis.nasa.gov/archive/geoMeta/ and https://ladsweb.modaps.eosdis.nasa.gov/archive/geoMetaVIIRS/
- Luo K, Wang X, de Jong M, Flannigan M (2024). Nature 627:321-327. https://doi.org/10.1038/s41586-024-07028-5
- Mokhov II, Sitnov SA. Siberian forest fires 2000-2019, arXiv preprint 2206.09240.
- NASA Earthdata (25 June 2026). New FIRMS Data Product: Satellite Swath Outlines. https://www.earthdata.nasa.gov/news/blog/new-firms-data-product-satellite-swath-outlines
- NSIDC. MODIS data, "Ongoing changes in Terra and Aqua orbits". https://nsidc.org/data/modis
- Remy S, Kaiser JW (2014). Atmos. Chem. Phys. 14:13377-13390. https://doi.org/10.5194/acp-14-13377-2014
- Weber H, Wunderle S (2019). Remote Sens. 11:467. https://doi.org/10.3390/rs11040467
