# Sources for the cross-field approaches: agreement statistics, control charts, conformal intervals, latent models, drift as sampling

Verified 2026-11-14. Each source below was reopened by the verifier unless it is marked "metadata only" (title, authors, venue and DOI confirmed through Crossref, no content read) or "snippet only" (content known only from a search-engine summary, so it is unconfirmed). This file supplies evidence. It does not choose the team's method.

## Answer

All eight approaches have real, citable foundations, and every DOI in the draft resolves to the paper it names. None of them has been used on MODIS or VIIRS hotspot counts in any source found. Three can be used as **diagnostics**: Bland-Altman limits of agreement on the log scale, control charts and conformal intervals. Each assumes independent or exchangeable units (units that can be swapped without changing their joint distribution). The hotspot record gives about 10 independent fire seasons, not 116 independent months. With 10 units, a limit of agreement is uncertain by about ±1.2 standard deviations of the differences, against ±0.32 with 116 independent units. An 80% conformal interval then delivers coverage with a standard deviation of about 0.11 from one calibration set to the next. Three other approaches cannot recover hotspots that MODIS never detected: capture-recapture with the Rasch model, empirical-Bayes smoothing and Poisson kriging. The orbit-drift idea has a precedent in the precessing TRMM orbit, which never reached Interior BC because its inclination was 35 degrees. NASA fire scientists have proposed using the Terra and Aqua drift in this way, in slides the verifier could not open. No published result was found.

## Evidence

### Methods

| Method | Canonical source | Core idea | Main assumption | Known pitfall | Use on fire or satellite data | Is the proposed mapping sound? |
|---|---|---|---|---|---|---|
| Bland-Altman limits of agreement (LoA) | Bland & Altman 1986, Lancet (read via [author's copy](https://www-users.york.ac.uk/~mb55/meas/ba.htm)) | Bias ± 2 SD of paired differences. On logs, the limits become ratio limits. | Independent pairs. Differences roughly Normal. A tolerance is set in advance. | The 2007 paper says that treating repeated pairs as independent makes the limits "too narrow". Autocorrelation must be checked (read). | None found for hotspot counts. | Yes, as a diagnostic on scaled log counts. Count fire seasons as the units. Zero months cannot be logged. |
| Passing-Bablok regression | Passing & Bablok 1983, J Clin Chem Clin Biochem (metadata only) | Rank-based (non-parametric) slope and intercept. Swapping the axes does not change the result. | Linear relationship, high correlation (MedCalc manual, read) | Small samples give wide intervals that favour a false "agree". At least 30–50 samples are advised. | None found | Weak. The record has about 10 independent seasons. |
| Lin's concordance correlation (CCC) | Lin 1989, Biometrics (metadata only) | Penalises the correlation for shifts in location and scale | Paired data | It rises with the spread between subjects. A heterogeneous sample can look concordant (Haber et al. 2010, read, citing Atkinson & Nevill 1997). | None found | Poor. Monthly counts span orders of magnitude, so the CCC would be inflated. |
| Double-mass curve | Searcy & Hardison 1960, USGS WSP 1541-B (read) | Cumulative record plotted against a cumulative pattern. A change in slope means the proportionality changed. | The pattern averages many records. Years are independent. | Ignore breaks shorter than 5 years. Adjust only for a documented cause (USGS). With long-range dependence, slope ratios of ±0.25 to ±0.40 arise by chance (Koutsoyiannis 2010, read). | None found | It is a picture only. The 5-year rule would ignore the one-year 2026 Terra break. |
| Shewhart, CUSUM and EWMA charts | Page 1954; Roberts 1959 (metadata only); Lucas & Saccucci 1990 (read) | Signal when a monitored statistic leaves its in-control limits. The average run length (ARL) is the expected number of samples before a signal. | Known in-control parameters. Independent Normal data. | Estimating the limits from a reference period changes performance (Jensen et al. 2006, abstract read). Effects of autocorrelation and overdispersion are snippet only. | Landsat change detection (Brooks et al. 2014, metadata only). None found for calibration of fire sensors. | Sound as an alarm only. It does not convert counts. |
| Split conformal prediction and jackknife+ | Vovk, Gammerman & Shafer 2005 (book, metadata only); Angelopoulos & Bates 2023 (review, read); Barber et al. 2021 (read) | Calibrate an interval from held-out residuals | Exchangeable calibration and test units | Coverage is guaranteed only on average. With few calibration points it varies widely. Jackknife+ guarantees only 1 − 2α, where α is the allowed miss rate. | One wildfire preprint (arXiv:2207.13250, peer review unconfirmed) | Sound only if fire seasons are exchangeable. The drift years 2022–2026 are not. |
| Rasch model and capture-recapture | Darroch et al. 1993 (metadata only); Fienberg et al. 1999 (read); Mao et al. 2017 (read) | Logit of detection = individual effect + list effect. Conditioning on how often each individual was seen removes the unseen count from the likelihood. | Lists independent given the individual. Additive effects. | The odds of being unseen cannot be identified, so only lower bounds can be estimated (Mao et al.). | None found | No. The three VIIRS satellites are near-identical, so they are not independent lists. Detection depends on fire size by sensor, which breaks the additive form. |
| Hidden Markov model (HMM) | Rabiner 1989 (metadata only); Zucchini et al. 2016 (not opened) | Latent regime chain. Each month's counts depend on the current regime. | Stationary emissions. Missing values carry no information. | Information criteria often pick too many states (Pohle et al. 2017, abstract read). | Drought classes: Mallya et al. 2013 (metadata only). Fire: only loosely related preprints. | Possible. Each sensor still needs its own scale inside the model, so the harmonization factor returns. |
| Empirical-Bayes smoothing and Poisson kriging | Clayton & Kaldor 1987 (metadata only); Goovaerts 2006 and Berke 2004 (read) | Shrink unstable small-area rates towards a mean, or krige counts weighted by population | Poisson counts with a known denominator | Berke: empirical Bayes "cannot achieve variance homogeneity entirely" and its error map "neglects the error from the first step". Goovaerts: kriged empirical-Bayes rates can be "over-smoothed". | None found | Sound for damping noisy small-area colours. It cannot restore missed detections. |
| Diurnal cycle from a drifting or precessing orbit | Giglio 2007, RSE (metadata only; content snippet only) | Overpass times that change let one orbit sample many hours of the day | Fire regime stable while the sampling changes | Drift confounds the hour of observation with year-to-year change. Weber & Wunderle 2019 (abstract via API): a drift of about 5 h coincided with a decline of about 90% in observed AVHRR fires in Europe. | TRMM VIRS (tropics). AVHRR drift artifacts (Giglio & Roy 2024, read). | Plausible in principle. The Terra and Aqua shift is only about 2 h. |

### Numbers recomputed from the cited formulas (`v02b_numbers.py`)

| Quantity | n = 10 | n = 26 | n = 116 | Source of formula |
|---|---|---|---|---|
| 95% half-width of one LoA, in units of the SD of differences | ±1.24 | ±0.70 | ±0.32 | Bland, sizemeth.htm: SE ≈ √(3s²/n), with a t multiplier |
| Split-conformal coverage at α = 0.2, given the calibration set: mean (SD) | 0.82 (0.11) | 0.82 (0.07) | 0.80 (0.04) | Beta(n+1−l, l) with l = ⌊(n+1)α⌋ (Angelopoulos & Bates) |
| Chance that delivered coverage falls below 0.70 at α = 0.2 | 0.15 | 0.07 | ≈0 | Same |

At α = 0.1, fewer than 9 calibration points give an unbounded interval. The Beta result applies to split conformal, not to jackknife+.

### Where the analogies break against the team's measurements

- **Agreement.** Two identical VIIRS instruments differ by ±15–20% in a single month. That is a floor on repeatability, and no tolerance can sensibly be tighter. The ratio ranges 0.19–0.40 across 10 fire seasons, so seasons are the natural units.
- **Double-mass curve.** Terra's daytime ratio is outside its earlier range only in 2026 (0.070 against 0.127–0.212). The USGS rule would ignore a break that lasts less than 5 years, even though the cause is documented.
- **Rasch and empirical-Bayes smoothing.** MODIS records nothing in 16–50% of the months in which VIIRS saw fire (circles of 10–100 km radius). Neither method creates detections.
- **Drift as sampling.** Terra's median daytime hotspot time moved from 11:04 to 09:20, and Aqua's from 12:47–13:03 to 14:51, over 2022–2026. TRMM's precessing orbit swept all hours about every 46 days. The Terra and Aqua drift covers about 2 hours, once.

## What this implies

- The team could cite Bland-Altman on the log scale, a control chart or a conformal interval as a check on whatever conversion it uses. It should then state the effective sample size as fire seasons, not months.
- The team could not claim a coverage or false-alarm guarantee for 2022–2026. Exchangeability and an in-control state are exactly what the drift breaks.
- The team could not claim that capture-recapture, smoothing or kriging estimates the fires MODIS missed. The unseen count is not identifiable.
- An HMM or a drift-based diurnal model would be a new application with no precedent found. It would carry the harmonization factor inside it.

## Limits

- Lin 1989, Passing-Bablok 1983, Giglio 2007, Jensen et al. 2006 and Mallya et al. 2013 were not read in full. Their content here is metadata, abstract or snippet level.
- The 2022 MODIS Science Team slides by Giglio, Roy and Randerson, with a section titled "Terra and Aqua Orbital Drift Enables Novel Fire Science", are known only from search summaries. The server refused the connection.
- The interval widths and coverage figures are computed from published formulas. They are not published values and not fitted to the team's data.
- "None found" reflects limited searches. It is not proof of absence.

## Sources

- Bland JM, Altman DG (1986). Lancet 1:307–310. Author's reproduction: https://www-users.york.ac.uk/~mb55/meas/ba.htm. Sample size: https://www-users.york.ac.uk/~mb55/meas/sizemeth.htm (both read).
- Bland JM, Altman DG (2007). Agreement between methods of measurement with multiple observations per individual. J Biopharm Stat 17:571–582. doi:10.1080/10543400701329422 (read).
- Passing H, Bablok W (1983). J Clin Chem Clin Biochem 21:709–720. doi:10.1515/cclm.1983.21.11.709 (metadata only). MedCalc manual: https://www.medcalc.org/en/manual/passing-bablok-regression.php (read).
- Lin LI (1989). Biometrics 45:255–268. doi:10.2307/2532051 (metadata only). Haber M, Gao J, Barnhart HX (2010). J Data Sci 8:457–469. https://pmc.ncbi.nlm.nih.gov/articles/PMC2907262 (read).
- Searcy JK, Hardison CH (1960). USGS WSP 1541-B. doi:10.3133/wsp1541b (read). Koutsoyiannis D (2010). IPC10, Coimbra. https://www.itia.ntua.gr/en/docinfo/1002/ (read).
- Page ES (1954). Biometrika 41:100–115. doi:10.1093/biomet/41.1-2.100. Roberts SW (1959). Technometrics 1:239–250. doi:10.1080/00401706.1959.10489860 (both metadata only). Lucas JM, Saccucci MS (1990). Technometrics 32:1–12. doi:10.1080/00401706.1990.10484583 (read).
- Jensen WA et al. (2006). J Qual Technol 38:349–364. doi:10.1080/00224065.2006.11918623 (abstract read). Brooks EB et al. (2014). IEEE TGRS 52:3316–3332. doi:10.1109/TGRS.2013.2272545 (metadata only).
- Angelopoulos AN, Bates S (2023). Found Trends Mach Learn 16:494–591. doi:10.1561/2200000101 (read). Barber RF et al. (2021). Ann Stat 49:486–507. doi:10.1214/20-AOS1965 (read). Barber RF et al. (2023). Ann Stat 51:816–845. doi:10.1214/23-AOS2276 (read). Dunn R et al. (2023). JASA 118:2491–2502. doi:10.1080/01621459.2022.2060112 (abstract read). Vovk V et al. (2005). Springer. doi:10.1007/b106715 (metadata only). Xu C et al. arXiv:2207.13250 (abstract read).
- Darroch JN et al. (1993). JASA 88:1137–1148. doi:10.1080/01621459.1993.10476387 (metadata only). Fienberg SE et al. (1999). JRSS A 162:383–405. doi:10.1111/1467-985X.00143 (read). Mao CX et al. (2017). Ann Inst Stat Math 69:705–716. doi:10.1007/s10463-016-0561-1 (read).
- Rabiner LR (1989). Proc IEEE 77:257–286. doi:10.1109/5.18626 (metadata only). Pohle J et al. (2017). JABES 22:270–293. doi:10.1007/s13253-017-0283-8 (abstract read). Mallya G et al. (2013). J Hydrol Eng 18:834–845. doi:10.1061/(ASCE)HE.1943-5584.0000699 (metadata only).
- Clayton D, Kaldor J (1987). Biometrics 43:671–681. doi:10.2307/2532003 (metadata only). Goovaerts P (2006). Int J Health Geogr 5:52. doi:10.1186/1476-072X-5-52 (read). Berke O (2004). Int J Health Geogr 3:18. doi:10.1186/1476-072X-3-18 (read).
- Giglio L (2007). Remote Sens Environ 108:407–421. doi:10.1016/j.rse.2006.11.018 (metadata only). NASA GPM, TRMM satellite page: https://gpm.nasa.gov/missions/TRMM/satellite (read: "inclination of 35 degrees", precession period about 46 days).
- Weber H, Wunderle S (2019). Remote Sens 11:467. doi:10.3390/rs11040467 (abstract read via the Semantic Scholar API). Giglio L, Roy DP (2024). Nat Commun 15. doi:10.1038/s41467-024-46168-0 (read). Andela N et al. (2015). Atmos Chem Phys 15:8831–8846. doi:10.5194/acp-15-8831-2015 (abstract read).
- Giglio L (2025). LANCE UWG orbit-drift slides: https://landweb.modaps.eosdis.nasa.gov/data/filePost/LANCE_UWG_Orbit_Drift_Giglio_202505.pdf. LDOPE note: https://landweb.modaps.eosdis.nasa.gov/displayissue?id=1254 (both read).
- Scripts: `scripts/v02b_doicheck.py` (Crossref check of 47 DOIs) and `scripts/v02b_numbers.py` (LoA and conformal arithmetic).
