# Harmonization tests: what holds up on the Interior BC data

Team reference for City of Kamloops & Co. It reports tests of the questions left open by [harmonization-evidence.md](harmonization-evidence.md) and trials of approaches borrowed from other fields, all run on the team's own FIRMS data. It says what each test shows and how strong the result is. It does not choose the team's method.

Compiled 2026-11-14. Eleven analyses were each run by an analyst and then re-run and independently recomputed by a reviewer. Two further topics (longer-shot models and data availability) were each handled by a single agent with no second reviewer. The sources behind the borrowed approaches were researched and then verified. A final pass reconciled numbers that differed between topics. Three follow-up tests, on questions this document first listed as missing, were then run by an analyst and re-run and recomputed by a reviewer in the same way; they are reported under [Follow-up tests](#follow-up-tests). The nineteen working files are in [harmonization-tests-research/](harmonization-tests-research/).

**The data.** The same 737,244 FIRMS hotspots as before (box 49.0–52.5°N, 122.5–118.0°W, November 2000 to November 2026), with three changes: months are keyed by local date, the fixed heat source near Kamloops is removed, and only vegetation-fire rows and near-real-time rows are kept. On the 116 stable-orbit months this gives a MODIS-to-Suomi-NPP ratio of 0.2425 (0.343 by day, 0.177 at night), which every analysis reproduced before starting.

**The main test.** The real calendar will judge a VIIRS month against a baseline in which the early years come from MODIS and the later years from VIIRS. The ten years when both flew in stable orbit (2012–2021) allow that to be imitated with the answer known. Five of the ten years are treated as a pretend MODIS era, in which only MODIS counts may be used. Each design builds a mixed baseline and assigns each remaining month one of five classes by its ratio to the calendar-month median. The answer it is scored against is the class the same month gets from a baseline of Suomi NPP counts in all the other years. This is repeated over 202 different splits of the years. The benchmark each design has to beat is a short baseline that uses the VIIRS years only and ignores MODIS.

**Terms.** "Converted" means MODIS counts divided by the overlap factor, giving VIIRS-equivalent hotspots. "Fire season" means April to October. Intervals in brackets are 95% intervals from resampling whole years.

## At a glance

1. **A converted MODIS-era baseline gives the right calendar class in about five fire-season months out of six** on the whole box (84%), against 66% for a short VIIRS-only baseline. The converted baseline is worth having.
2. **A single converted month is much less reliable than the baseline it helps build.** One month converted on its own gets the right class 69% of the time, with a typical error of about a third.
3. **The direction of conversion does not matter.** Scaling MODIS up and thinning VIIRS down give the same class in 11,705 of 11,706 cases. Random thinning is slightly worse and does not fix the problem of zero months in small areas.
4. **No refinement of the factor beat one all-hours factor.** A day-and-night split matches one factor in the fire season and is 7 points worse over all months, because the night factor is seasonal. A seasonal night factor is still 4.7 points worse over all months. Using day and night factors only in April to October is level with one factor over all months and removes one factor's fire-season bias, but a loss of a few points in class cannot be ruled out.
5. **About 100 km radius is where converted history is supported without qualification.** At 50 km it is borderline. At 25 km a VIIRS-only baseline does better, and only 22% of fire-season months can be classed at all.
6. **About a fifth of the monthly scatter between MODIS and VIIRS is irreducible,** and up to half in smaller areas. In a single month, converted MODIS is less than half as precise as a second VIIRS satellite.
7. **The factor survives the end of Suomi NPP.** Fitted directly against NOAA-20 it is 0.242, the same as through Suomi NPP.
8. **Before 2012, the order of years is supported and the level is not.** Converted years rank against BC area burned as well as VIIRS years do, but the factor runs about 15–27% high in quiet fire-season months and small seasons, and most seasons before 2012 were small. In typical November-to-March months it runs about 25–35% low instead.
9. **On the real 24-year baseline, about two in five fire-season labels in the box differ from a VIIRS-only baseline** (39%), against about one in five expected from the change of length alone. The excess pushes months lower, mainly in spring and autumn. The data cannot tell real pre-2012 burning from a conversion level about 1.6 times too high. On the stable years, a converted baseline of the real composition still gives the right class in 87% of fire-season months.
10. **Only the 2026 loss in Terra's daytime count is established** (about half of normal). The gradual decline over 2022–2025 reported earlier is weak. BC's provisional 2026 fire records confirm the 2026 loss independently.
11. **The delivered day and night label follows one rule for every row,** standard and near-real-time. No relabelling is needed now.
12. **The Kamloops site is the only persistent fixed heat source in the box.** It makes up most of the VIIRS count near Kamloops in a quiet summer month.
13. **NASA's open granule catalogue gives a per-day availability flag for each satellite.** It sees whole-day and half-day losses but not losses inside a scene. It found outages missing from the outage list used so far, and four listed gaps that are wrong or too wide. With it, the daily mean of the VIIRS satellites stays level through every real outage month.
14. **Changing satellite changes labels on its own.** A current month taken from NOAA-20 instead of Suomi NPP gets a different class in about one fire-season month in seven on the box (13.5%), and in 14–23% of 100 km circle-months, even with a perfect conversion.
15. **Of the approaches borrowed from other fields, the useful ones are diagnostics and explanations, not converters.** None beat one factor at predicting counts.

## How this relates to the team's recommended method

A separate piece of work on the same day produced [harmonization-research.md](harmonization-research.md), which recommends a method, and `harmonize.py`, which implements an interim version of it. That method counts hotspots per satellite per 30 days, converts MODIS to VIIRS units with one factor fitted on the whole box, and ranks each month by percentile against the same calendar month in other years. It used the same 737,244 rows.

- **Where the two agree.** Both find about 4.1 Suomi NPP hotspots for every Terra-plus-Aqua hotspot (4.15 there; 1 ÷ 0.2425 = 4.12 here). Both find that satellites must not be summed, that one factor fitted on the whole box is good enough, that the fixed heat source near Kamloops has to be removed by location, that the orbit drift should be flagged, and that areas below about 50 km radius are too noisy.
- **What this document adds.** That file lists a comparison with area burned and a measure of the drift's effect on counts as not done. Both are here: see [Is the factor stable, and where can it be trusted?](#is-the-factor-stable-and-where-can-it-be-trusted) and [The orbit drift](#the-orbit-drift). Also here are the test against a short VIIRS-only baseline, the baseline of the real length, the label noise from the change of satellite, and the availability flag from NASA's granule catalogue.
- **Gaps missing from `harmonize.py`.** Its outage table lacks whole-day gaps that the catalogue shows (UTC days): Suomi NPP on 30 May – 3 June, 10–15 July and 24–28 July 2024; Terra on 13–15 May 2025 and 5–10 March 2026; NOAA-21 on 10–14 January 2026. NOAA-20 also recorded no hotspots on 19–22 July 2023 although its scenes were normal. These change the satellite-days that the method divides by. Detail: [f03](harmonization-tests-research/f03-availability-flag.md).
- **May and September.** `harmonize.py` ranks May to September against every year from 2001, and other months against VIIRS years only. The real-length baseline test found converted 2003–2011 medians of 3.9 times the VIIRS-era median in May and 1.7 times in September, though each interval includes 1. Those are the two months of its mixed baseline where the level before 2012 matters most. Detail: [f01](harmonization-tests-research/f01-real-length-baseline.md).
- **Differences in definitions.** That method drops low-confidence rows and keeps `type` 3 rows. The tests here keep `type` 0 and near-real-time rows and apply no confidence filter. It ranks by percentile in five equal classes; the tests here class a month by its ratio to the calendar-month median. Agreement rates from the two are therefore not directly comparable.
- **One citation.** That file says the "not advisable" wording attributed to Giglio et al. 2025 was not confirmed. The methods review found it in the paper's text; see [the reconciliation file](harmonization-methods-research/_reconcile.md).

## Does a converted record give the right class?

Detail: [a01](harmonization-tests-research/a01-hindcast-box.md), [a02](harmonization-tests-research/a02-hindcast-circles.md).

### Whole box

Share of months given the same five-class label as the all-VIIRS answer, pooled over 202 splits:

| Design | Fire season | All months | Note |
|---|---|---|---|
| Scale MODIS up with one factor | 84% | 80% | Within one class in 97–98% of months |
| Scale MODIS up with day and night factors | 83% | 73% | Labels 5.6 points too many months above normal over the year |
| Thin VIIRS down by expectation | 84% | 80% | Same label as scaling up in all but one case |
| Thin VIIRS down at random | 82% | 77% | 9–12 points worse again when the thinning rate is allowed to vary by month |
| Short VIIRS-only baseline (benchmark) | 66% | 65% | |

- **Gain over the benchmark:** 18 points in the fire season (14 to 23) and 15 over all months (10 to 20). One factor wins in 94–95% of the splits.
- **Robust to the factor.** Refitting the factor without the year being classed changes agreement by at most 0.4 points. Shifting it by −20% or +25% costs 0 to 5 points.
- **Active cell-days** (2 km, daytime) gain as much over their own short baseline as counts do. They neither win nor lose at this scale.
- **A single month converted on its own** (fit on nine years, convert the tenth) gets the right class in 69% of fire-season months (61–77), with a median error of 33%.

### User-sized areas

Fire-season months, 31 circles per radius. "Classed" means the baseline median is at least one hotspot, so a ratio to normal exists. The last two columns count a month a design cannot class as a miss.

| Radius | Months with a known answer | Converted baseline can class | VIIRS-only baseline can class | Converted minus VIIRS-only, exact class | Converted minus VIIRS-only, three coarse classes |
|---|---|---|---|---|---|
| 25 km | 22% | 17% | 29% | −3 points (−3.5 to −2.4) | −5 points |
| 50 km | 67% | 55% | 66% | +3 points (1 to 4) | +1 point (−1 to 2) |
| 100 km | 100% | 99.9% | 98% | +11 points (8 to 13) | +8 points (6 to 11) |
| 150 km | 100% | 100% | 100% | +20 points (15 to 25) | +13 points (8 to 16) |

- On months that both designs can class, the converted baseline is ahead at every radius, by 10 to 20 points. What changes with radius is how many months it has to refuse.
- **The feared bias is small.** Zeros in the MODIS era were expected to make later VIIRS months look above normal. In the months most exposed to it, the converted baseline labels 2 to 3 points too many months above normal. The rule that a month is classed only when its baseline median is at least one hotspot is what keeps it small.
- **Random thinning does not help here.** It classes fewer months than scaling up (13% against 17% at 25 km, 39% against 55% at 50 km) and agrees less often. Thinning moves VIIRS onto MODIS's sparse scale, so medians that were zero stay zero.
- **Shrinking a circle toward the whole box lowered agreement at every radius,** but this test cannot reward it: the answer is defined on the very count being classed, so any move toward the region moves away from the answer. Its value as context for a user is untested.

How often MODIS records nothing in a month when Suomi NPP saw fire:

| Radius | When Suomi NPP had at least 1 hotspot | When Suomi NPP had at least 10 |
|---|---|---|
| 25 km | 40% | 4% |
| 50 km | 32% | 2% |
| 100 km | 15% | 3% |
| 150 km | 4% | 0.3% |

What a MODIS month with no hotspots is consistent with ([a03](harmonization-tests-research/a03-thinning-model.md)):

| Radius | Share of MODIS-zero months in which Suomi NPP also had none | Suomi NPP hotspots, 90th percentile | In the fire season |
|---|---|---|---|
| 50 km | 52% | 6 | 4 |
| 100 km | 17% | 17 | 9 |

## How much of the scatter can any method remove?

Detail: [a03](harmonization-tests-research/a03-thinning-model.md), [a10](harmonization-tests-research/a10-diagnostics.md).

| Source of monthly scatter in the MODIS-to-VIIRS ratio | Share of the variance, whole box |
|---|---|
| Random loss of single hotspots | 15% (10–25) |
| The difference between two identical VIIRS satellites | about 18–20% |
| Random loss of whole fire-days (all hotspots in one 2 km cell on one day) | 40% (29–61); 64% in the fire season; 47% at 100 km; 70% at 50 km |

About a fifth is irreducible by any factor, and up to half at the size of a user's circle. The rest is real month-to-month change in the ratio, part of it tied to the size of the month.

Agreement in a single fire-season month, as multiples of the true VIIRS count:

| | Typical bias | 95% of months fall between | Median error | Within 25% |
|---|---|---|---|---|
| Converted MODIS, one factor | 1.15 | 0.42 and 3.1 times | 32% | 29% of months |
| A second VIIRS satellite (NOAA-20 against Suomi NPP) | 1.02 | 0.66 and 1.57 times | 10% | 70% of months |

Converted MODIS is right on average and in rank order. In a single month its spread is about 2.3 times that of a second VIIRS satellite, at every size of month.

## Is the factor stable, and where can it be trusted?

Detail: [a04](harmonization-tests-research/a04-factor-stability.md), [a05](harmonization-tests-research/a05-pre2012-check.md).

| Question | Result |
|---|---|
| Does it carry over to NOAA-20? | Yes. Fitted directly on April 2018 to December 2021 it is 0.242 (0.234–0.269). Chained through Suomi NPP it is 0.246. |
| Is there a step or trend between VIIRS satellites? | No. Suomi NPP against NOAA-20 shows no step at March 2023 and no trend. A dip in 2024 was Suomi NPP outage days missing from the outage list; with those removed the ratio is 0.99. A high 2023 value (1.064) was a NOAA-20 loss on 19–22 July 2023; with a day mask it is 1.028, and the yearly series runs 0.93–1.07. |
| Is the all-hours factor stable through 2012–2021? | Yes, at a fixed mix of day and night: 0.243 in 2012–2016 and 0.240 in 2017–2021. The raw value fell from 0.281 to 0.237 because the night share of VIIRS hotspots rose from 48% to 62%. |
| Are the separate day and night factors stable? | No. Between the two halves of the decade the day factor fell 23% and the night factor rose 46%. The night factor is also seasonal: 0.03–0.12 outside June to August against 0.18–0.19 in July and August. |
| Is one factor biased? | Yes, in quiet periods, in opposite directions by season. In the fire season, converted values run about 15% high in a typical month, 23% high for a calendar-month median, and 27% high for a small season. It is unbiased in the three large seasons. In November to March a typical converted month is about a third low (0.66 times actual, 0.54–0.79). See [Refinements of the factor](#refinements-of-the-factor). |
| How much does uncertainty in the factor change labels? | Little. The ends of its interval changed 0 of 31 test labels. A shift of ±20% changed 2. A shift of −30% changed 7. |

**Before 2012**, the only independent record is BC area burned:

- **Order is supported.** The joined series (converted MODIS for 2003–2011, VIIRS from 2012) has a rank correlation of 0.88 with area burned. The six largest seasons by area are the six largest in the joined series. Pairs of years on either side of 2012 are ordered correctly 84% of the time, against 89% within an era.
- **Level cannot be confirmed.** The area-burned record could only detect a change of about twofold. The joined series puts converted years before 2012 about 1.6 times above VIIRS years of equal area burned (interval 1.1 to 2.6), though the step is not significant in every variant of the test. Part of it is the small-season bias above: seven of the nine seasons before 2012 were small. In 19 of the 20 wrongly ordered pairs, the year before 2012 is ranked too high.
- **MODIS itself was consistent.** The Terra-to-Aqua ratio shows no trend over 2003–2021 (+0.2% a year, −0.4 to +1.0).
- **The Terra-only years are untested.** A Terra to Terra-plus-Aqua factor of 1.90 fits well on 2003–2011, but 2001 and 2002 sit at or below the edge of the range expected from area burned.

**Intervals for a converted month.** Intervals built from held-out-year errors, grouped by the size of the predicted count, contained the true value as often as claimed (90–92%) for months of 10 or more predicted hotspots:

| Predicted hotspots | Interval, as multiples of the converted value |
|---|---|
| 1,000 or more | 0.45 to 1.3 |
| 100 to 1,000 | 0.45 to 1.5 |
| 10 to 100 | 0.39 to 4.9 |
| Under 10 | No honest interval (55% coverage) |

Model-based intervals did worse. Those from a beta-binomial model were too narrow (they contained the true value 72–79% of the time for a nominal 90%), and those from a negative binomial model were about twice as wide as needed in large months. Because one factor is applied to every converted year, its error does not average out across years, and a per-month interval leaves that part out.

## The orbit drift

Detail: [a09](harmonization-tests-research/a09-drift-curve.md), [a10](harmonization-tests-research/a10-diagnostics.md), [w03](harmonization-tests-research/w03-data-availability.md).

Level of each MODIS pass relative to its stable-orbit level, allowing for the size of the fire year. Bold marks values outside the year-to-year scatter.

| Year | Terra day (pass time) | Aqua day | Terra evening | Aqua night |
|---|---|---|---|---|
| 2022 | 0.91 (11:04) | 1.14 | 0.96 | 1.19 |
| 2023 | 0.87 (10:44) | 0.95 | 0.95 | 1.05 |
| 2024 | 0.81 (10:32) | 1.07 | 1.14 | 1.12 |
| 2025 | 0.71 (10:04) | 1.07 | 1.07 | 0.97 |
| 2026 | **0.50** (09:20) | 0.90 | 1.09 | **0.70** |

- **Only 2026 is established.** Terra's daytime count was about half of normal in 2026 (0.41–0.61 across five methods). The raw ratio to NOAA-20, without a size adjustment, shows no decline in 2022–2025 (1.07, 1.05, 0.95, 0.98 of the 2018–2021 level). The gradual decline appears only after the size adjustment, which fits small years poorly.
- **Independent confirmation.** BC's provisional 2026 records put 2026 second of 27 years for area burned in the box (about 410,000 ha). Measured against area burned, Terra's daytime yield in 2026 is 0.41–0.45 of its 2021 and 2023 levels. NOAA-20's is 0.74–0.93.
- **Aqua's night pass** is at 0.70 in 2026, as it moves toward dawn.
- **A correction for Terra by day is possible but thinly validated.** A daily fire curve fitted to the data peaks at 13.4 h (12.7–13.8), about 1.2 hours earlier than the published curve (14.57 h). Fitted on 2012–2024 only, it predicts Terra's 2025 and 2026 daytime levels to within 3–4%. Once single-year scatter is included, the interval for 2026 is 0.69 to 1.72, and the validation rests on one decisive year. The published curve over-corrects by 26% and 37%.
- **For the other three passes the data support flagging only.** Their arcs are flat or move only in 2026.
- **Detection.** A control chart on Terra's daytime ratio signalled in September 2025. A chart on the Terra-plus-Aqua all-hours total never signalled, partly because Terra's night count held up while its day count fell.

## The day and night label

Detail: [a06](harmonization-tests-research/a06-daynight-rule.md).

- **One rule reproduces every label.** "Night when the sun is more than 85 degrees from vertical" matches the delivered label for all 737,244 rows, standard and near-real-time, on all five sensors.
- **The near-real-time rule cannot be told apart yet.** The documentation says near-real-time rows are labelled by orbit direction. No near-real-time row falls in the range of sun angles where the two rules would disagree, so the data fit either.
- **Labelling by pass makes almost no difference today.** It differs for 10 hotspots in 26 years, all from one Terra evening pass in July 2026. The halving of Terra's daytime count in 2026 is the same under either label.
- **The risk is ahead.** Terra's evening pass and Aqua's dawn pass now sit a few degrees from the 85-degree line in summer. As they cross it, the sun-angle rule will move parts of those passes into the day series. A pass-based rule would keep each pass whole.

## Static and recurring sources

Detail: [a12](harmonization-tests-research/a12-static-sources.md), [w03](harmonization-tests-research/w03-data-availability.md).

| Source | Position | Record | Seen by |
|---|---|---|---|
| Kamloops site | 50.688°N, 120.408°W | 712 dates in every year 2012–2026; all at night; median 1.0 MW | All three VIIRS satellites; never MODIS |
| Second weak source | 50.815°N, 121.650°W | 42 dates, 2012–2016; none since | Suomi NPP only |
| Third weak source | 50.661°N, 120.061°W | 12 dates, 2013–2016; none since | Suomi NPP only |

- A second, independent search with a different grid found the same three sites and no others.
- The Kamloops site is seasonal: 80% of its dates fall in June to September. In a quiet summer month it makes up 87% of the Suomi NPP count within 25 km and 69% within 50 km.
- The nearest facility in Canada's national pollutant registry is a pulp mill 0.4 km away. That is proximity, not identification.
- November and spring burning is spread across valleys, not at fixed points. A persistence mask would remove real burning, which the challenge counts as burning activity.

## Follow-up tests

Three questions that the first version of this document listed as missing were tested afterwards. Each was run by an analyst and then re-run and independently recomputed by a reviewer. Every one reproduced the starting check of 48,233 MODIS and 198,916 Suomi NPP hotspots and the ratio of 0.2425.

### A baseline of the real length

Detail: [f01](harmonization-tests-research/f01-real-length-baseline.md).

**The question.** Every class test above used nine or ten stable years. The real calendar will use about 24: converted MODIS for 2003–2011, when seven of nine seasons were small, and VIIRS from 2012. Does a converted era made mostly of small seasons still give the right class, and how much do real labels change when the converted years are added?

**Terms.** The *mixed baseline* is the median for the same calendar month over converted MODIS in 2003–2011 (Terra plus Aqua divided by 0.2425) and VIIRS in 2012–2025, leaving out the month's own year. The *VIIRS-only baseline* uses 2012–2025 alone. The VIIRS value is Suomi NPP, with NOAA-20 times 1.011 for its masked months and for all of 2026. *Large seasons* are 2017, 2018 and 2021.

**On the stable years.** The main test was run over all 582 ways of choosing three, four or five of the ten years as the pretend MODIS era, and grouped by how many large seasons that era holds. Whole box, fire season:

| Pretend MODIS era | Splits | One factor, exact class | Short VIIRS-only baseline, exact class | Converted baseline median, as a multiple of the true median |
|---|---|---|---|---|
| Five years, no large season | 21 | 87.4% (80–93) | 60.7% | 1.156 (1.12–1.19) |
| Five years, one large season | 105 | 84.8% | 68.3% | 1.138 |
| Five years, two large seasons | 105 | 83.6% | 68.9% | 1.109 |
| Five years, three large seasons | 21 | 83.5% (78–90) | 60.0% | 1.043 (1.02–1.07) |
| Mostly small (at most a quarter of the years large) | 301 | 86.5% (82–90) | 71.1% (63–77) | 1.114 (1.09–1.14) |

- **Composition hardly matters.** Agreement changes by about 1 point per large season, within the spread across splits (a standard deviation of 5–6 points). The real 2003–2011 era, with two large seasons in nine (2003 and 2009), belongs to the mostly-small group.
- **The level bias barely reaches the classes.** In the mostly-small group the converted baseline median runs 11% high, but the share of months labelled above normal is 2.6 points too low (−6 to +1) and the share below normal 0.6 points too high. Kappa, which allows for agreement by chance, is 0.81 for one factor against 0.61 for the short baseline.
- **No remedy helps by more than the spread.** Change in exact agreement from one factor, mostly-small group, in points: geometric mean of yearly ratios +0.8 (−0.3 to +1.8); two factors by season size +0.2 (−1.7 to +1.8); a log-log curve by season size +0.6 (−1.9 to +2.6); two factors by monthly MODIS count −2.5 (−4.3 to −0.3); one factor per calendar month −1.1 (−3.0 to +0.9); separate fire-season and off-season factors, no change.

**On the real baseline.** Labels from the mixed baseline compared with labels from the VIIRS-only baseline, for 2012–2025 months:

| Set | Months | Labels differ | Direction |
|---|---|---|---|
| Box, fire season | 105 | 41 (39.0%, 33–45) | Mixed lower in 38, higher in 3 |
| Box, all months | 177 | 58 (32.8%, 29–37) | Mixed lower in 47, higher in 11 |
| 100 km circles, fire season | 3,255 | 36.1% (31–41) | Mixed lower in 33.2% of months, higher in 2.9% |
| 100 km circles, all months | 5,487 | 34.6% (31–38) | Mixed lower in 28.9% of months, higher in 5.7% |
| Box, fire season, mixed baseline with and without Terra-only 2001–2002 | 105 | 8 (7.6%, 4–12) | Split 3 and 5 |
| 100 km circles, fire season, with and without Terra-only years | 3,255 | 10.6% (9–13) | Split 2.8% and 7.8% of months |

- **Where the difference comes from.** Converted 2003–2011 medians in the box, as multiples of the 2012–2025 VIIRS medians: March 1.6, April 2.8, May 3.9, June 1.5, July 0.58, August 0.50, September 1.7, October 1.9, November 1.8. Each ratio's interval includes 1.
- **In 2026,** April, May and October are one class lower under the mixed baseline. June to September are the same.
- **Remedies on the real baseline.** The remedies listed above left 38 to 46 of the 105 box fire-season labels different from VIIRS-only. A factor per calendar month left 34.

**How much is the change of length alone?** Any longer baseline changes some labels. The 2012–2021 months were classed against a long and a short baseline, and this was repeated with the years reassigned at random (1,000 times in the box, 300 at 100 km), so the null shows what a change of length alone does if the years are interchangeable. Fire season:

| Comparison | Labels differ, observed | Expected from length alone, mean (95th percentile) | p |
|---|---|---|---|
| Box, MODIS counts only, no conversion | 26.5% (19–33) | 25.6% (38%) | 0.46 |
| Box, converted, 2012–2025 | 38.8% | 22.4% (34%) | 0.014 |
| Box, converted, same years | 38.6% | 24.2% (39%) | 0.05 |
| 100 km, MODIS counts only, no conversion | 33.0% | 24.3% (32%) | 0.023 |
| 100 km, converted, same years | 40.5% | 24.9% (33%) | 0.003 |

The converted comparison shows an excess over the length effect, and its downward direction is more significant still (p = 0.006 in the box, 2012–2025). In the box, MODIS counts alone show no excess.

**What the excess would cost in level.** Dividing the converted pre-2012 values by a constant moves box fire-season labels upward only:

| Converted pre-2012 values divided by | Labels differ from VIIRS-only | Labels changed against the plain mixed baseline |
|---|---|---|
| 1 | 41 (39%) | None |
| 1.15 (the typical-month bias) | 34 (32%) | 10 |
| 1.27 (the small-season bias) | 29 (28%) | 17 |
| 1.6 (the pre-2012 step from area burned) | 21 (20%) | 27 |

A pre-2012 level about 1.6 times too high would remove the excess, bringing the gap down to about the length-only null. So would real differences in burning before 2012, such as more spring and autumn burning. The data cannot tell these apart.

**How strong.**

- **Strong** for the hindcast and the label counts. The analyst's scripts re-ran byte-identically, and the reviewer reproduced every headline number with an independent script.
- **Moderate** for the excess over the length effect. The null assumes the years are interchangeable, so a real trend in fire regime would appear as excess. The p-values near 0.05 are borderline, and the circles used 300 draws.
- **Limits.** Ten stable years, reused by all 582 splits. The intervals on the real baseline resample only the evaluated years, and the factor was fitted on years that include them (shown earlier to move labels by 0.3 points or less). The unlisted Suomi NPP gaps of May to July 2024 and the partial loss of July 2025 were left in. The circles are 100 km only.

### Refinements of the factor

Detail: [f02](harmonization-tests-research/f02-factor-refinements.md).

**The question.** Does any refinement of the overlap factor give better calendar labels than one all-hours factor? The designs, each fitted on the whole box on the years a test allows:

- **Day and night factors:** as tested above.
- **Seasonal night factor:** day and night factors, with the night factor fitted separately for June to August and for the other months.
- **Day and night in the fire season only:** day and night factors fitted on and used in April to October, with an all-hours factor for November to March.
- **Season factors:** separate all-hours factors for April to October and for November to March.
- **Size-dependent factor:** a curve fitted between monthly MODIS and Suomi NPP counts on a log scale and then inverted, so the month's MODIS count sets the factor (0.21 to 0.23 between 5 and 5,000 hotspots).
- **Geometric mean:** the geometric mean of the yearly ratios.

**Labels in the main test** (202 splits), exact agreement minus one factor, in points. Bold marks intervals that exclude zero.

| Design | Box, fire season | Box, all months | Box, November to March | 100 km circles, fire season |
|---|---|---|---|---|
| One factor, exact agreement | 84.4% | 79.7% | 73.1% | 77.4% |
| Day and night factors | −1.3 (−4.8 to +2.0) | **−6.9 (−10.2 to −3.9)** | **−14.9 (−21.3 to −7.7)** | +0.7 (−0.6 to +1.8) |
| Seasonal night factor | +0.1 (−3.6 to +3.3) | **−4.7 (−7.3 to −2.6)** | **−11.4 (−16.2 to −6.2)** | −0.4 (−1.8 to +0.9) |
| Day and night in the fire season only | −2.0 (−5.3 to +1.3) | −1.3 (−2.9 to +0.4) | −0.4 (−2.0 to +1.5) | +0.6 (−0.7 to +1.8) |
| Season factors | +0.1 (−0.3 to +0.5) | −0.1 (−0.9 to +0.8) | −0.4 (−2.0 to +1.5) | +0.1 (0.0 to +0.1) |
| Size-dependent factor | −1.7 (−3.7 to +0.2) | −1.3 (−3.0 to +0.4) | −0.7 (−4.0 to +2.6) | **−2.0 (−2.6 to −1.5)** |
| Geometric mean | +0.3 (−0.7 to +1.2) | −0.5 (−1.8 to +0.6) | −1.5 (−4.2 to +1.1) | **+0.3 (+0.1 to +0.5)** |

- **No refinement wins.** In the box, the standard deviation of these differences across splits is 1 to 5 points. The only gain whose interval excludes zero is the geometric mean in the circles, at 0.3 points.
- **The day and night split is only partly repaired.** A seasonal night factor brings the fire season level, but November to March is still 11.4 points worse. Using the split only in the fire season is level over all months. When 2017–2021 is taken as the MODIS era, it loses 8.6 points in the box fire season.

**Bias in a typical month** (fit on nine years, convert the tenth; whole box). The bias is the geometric mean of converted over actual.

| Design | Fire season | November to March | Exact agreement minus one factor, fire season (points) |
|---|---|---|---|
| One factor | 1.14 (1.03–1.26) | 0.66 (0.54–0.79) | 0 (one factor: 69%) |
| Day and night factors | 0.99 (0.91–1.07) | 0.52 (0.43–0.62) | −2.9 (−8.8 to +2.9) |
| Seasonal night factor | 1.07 (1.00–1.15) | 0.60 (0.50–0.72) | −2.9 (−9.4 to +4.3) |
| Day and night in the fire season only | 0.98 (0.90–1.07) | 0.67 (0.54–0.80) | −2.9 (−8.8 to +2.9) |
| Season factors | 1.14 (1.03–1.26) | 0.67 (0.54–0.80) | 0.0 |
| Size-dependent factor | 1.27 (1.16–1.41) | 0.73 (0.60–0.85) | −1.5 (−7.8 to +4.4) |
| Geometric mean | 1.07 (0.97–1.19) | 0.62 (0.51–0.74) | **−5.9 (−10.6 to −1.4)** |

- **The plain day and night split and the fire-season split remove the fire-season bias** (0.99 and 0.98); the seasonal night factor leaves some (1.07). Of the two, only the fire-season split does so without losing points over all months in the main test. In the 100 km circles, in this test, its bias is 0.93 (0.86–1.01) against 1.05 for one factor, and its agreement is 3.4 points higher (+0.6 to +6.0). In the box its point estimates are 2 to 3 points lower than one factor in both tests, and losses of 5 to 9 points are not excluded.
- **Every design converts typical winter months too low.** A version of the bias that keeps months with zero values, the geometric mean of (converted + 1) over (actual + 1), lowers the one-factor figure for November to March further, to 0.58.

**Why the bias runs in opposite directions.** Box months split into thirds by their Suomi NPP count:

| Season and size third | MODIS / Suomi NPP | By day | At night |
|---|---|---|---|
| April to October, smallest | 0.345 | 0.58 | 0.12 |
| April to October, largest | 0.242 | 0.34 | 0.19 |
| November to March, smallest | 0.120 | 0.24 | 0.03 |
| November to March, largest | 0.251 | 0.38 | 0.09 |

Small fire-season months have a high ratio and are converted too high. Small winter months have a low ratio and are converted too low. Neither a season factor nor a single size curve can follow both slopes.

**Stability and the pre-2012 totals.**

- **Fit period.** Fitting on 2017–2021 instead of 2012–2016 changes the implied all-hours factor to 0.84 times (0.77–0.92) for one factor, 1.18 for day and night factors, 0.89 for the seasonal night factor and 0.96 for the fire-season split. Split by season, the night factors hardly move: 0.198 against 0.192 in June to August, and 0.100 against 0.101 in other months.
- **Converted 2003–2011 totals.** One factor turns 22,540 MODIS hotspots into 92,956 VIIRS-equivalent hotspots. The other designs give 0.93 to 1.09 times that total; the widest interval is the size-dependent factor's (1.09, 0.99–1.32). The choice of fit years moves each total by 8 to 26%, more than the choice of design.
- **The pre-2012 mix differs.** In 2003–2011, November to March holds 25% of MODIS hotspots, against 10% in the overlap years, and night holds 33% against 44%. The winter undershoot may therefore matter more there. Nothing can check those totals.

**How strong.**

- **Strong** that no refinement wins, and for the opposite biases by season. The analyst's scripts re-ran byte-identically, and an independent rewrite that does not use the analyst's code recomputed every design and table.
- **Moderate** for the fire-season split. Its bias gain is clear; whether it costs a few points in class is not.
- **Limits.** The main test's intervals resample the classed years but do not refit the factors, so they understate the uncertainty; the split standard deviation is the better guide. The circle intervals cover year-to-year variation only. Only two forms of the size-dependent factor were tested. The current month is Suomi NPP only.

### Availability flag and the combined VIIRS series

Detail: [f03](harmonization-tests-research/f03-availability-flag.md).

**The question.** Applied day by day, does the catalogue-based availability flag work, and what does it change? A satellite-day is counted as available when the catalogue has at least one day scene and one night scene, less the days on the outage list and days a count check marks as suspect. Dates here are local.

**The flag.** On days it marks empty, FIRMS has almost no hotspots. There are two holes where the catalogue is silent but data exist: Suomi NPP near-real-time data on 4–6 August 2026, and NOAA-20 on 1 April to 4 June 2018 (406 rows against Suomi NPP's 434, so treated as available). It also shows half-day losses that the list lacks; for example Suomi NPP on 3–4 August 2021 had 336 and 759 hotspots against NOAA-20's 1,208 and 2,011. Gaps since 2012 with no scene that the outage list lacks:

| Satellite | Days with no scene |
|---|---|
| Suomi NPP | 25 March 2012; 26 July 2023; 30 May – 3 June, 10–15 July, 24–28 July and 26 September 2024 |
| Terra | 12–15 May 2025; 4–9 March 2026 |
| NOAA-20 | 30 September 2023 |
| NOAA-21 | 27–28 February 2024; 10–14 January 2026 |

- **Listed gaps the catalogue contradicts.** Suomi NPP 11–20 August 2022 has scenes and 408 hotspots. Suomi NPP 2–6 November 2024 has scenes on 3 of the 5 days. Terra 15 April 2001 and 26–27 March 2026 have scenes, with no hotspots.
- **A new loss inside scenes.** A count check against the other VIIRS satellites found NOAA-20 with 0 hotspots on each of 19–22 July 2023, against Suomi NPP's 34, 141, 360 and 597, with normal scenes. This makes NOAA-20 alone 23% low in July 2023. The check finds a 75% loss in 87–92% of the fire-season windows it can test, but only 18–55% of June-to-September windows have enough fire to test. It finds a 50% loss in 8–34%.

**Ratios with the day mask.**

| Quantity | No day mask | Day mask |
|---|---|---|
| MODIS / Suomi NPP, 116 stable months | 0.2425 (0.237–0.266) | 0.2381 (0.231–0.267) |
| Factor bringing NOAA-20 to the Suomi NPP level, April 2018 to October 2026 | 1.001 (0.96–1.04) | 1.0245 (1.014–1.047) |
| Factor bringing NOAA-21 to the Suomi NPP level, March 2023 to October 2026 | 1.027 (1.016–1.054) | 1.0503 (1.030–1.083) |

The factors used so far, 1.011 and 1.034, came from dropping whole months. With the day mask, Suomi NPP / NOAA-20 in the fire season runs 0.93–1.07 by year: 2023 moves from 1.064 to 1.028 and 2024 from 0.881 to 0.994. NOAA-21 / NOAA-20 over all months is 1.002, 0.929, 0.914 and 0.962 for 2023–2026; four years cannot separate drift from year-to-year variation.

**The combined series.** Each day, take the mean of the available satellites, each scaled to Suomi NPP, then sum over the month. Difference of each alternative from the combined series, whole box:

| Month | Combined | Suomi NPP alone | NOAA-20 alone | Plain monthly mean |
|---|---|---|---|---|
| July 2022 | 629 | −64% | −3% | −34% |
| August 2022 | 2,266 | −55% | −1% | −28% |
| July 2023 (NOAA-20 loss) | 4,753 | −0.4% | −23% | −8% |
| July 2024 | 7,102 | −18% | +3% | −8% |
| November 2024 | 690 | −23% | −0.5% | −7% |
| August 2026 | 29,590 | −4% | +2% | −1% |

It stays level with Suomi NPP alone at each change in the number of satellites: 0.980 in April to October 2018 and 1.008 in March to October 2023, where a plain sum would be 1.93 and 2.9 times.

**Label noise from the change of satellite.** NOAA-20 alone classed against a Suomi NPP baseline (2012–2021, leaving out the tested year), compared with Suomi NPP's own label; test years 2018–2021 and 2023–2025:

| Scope | Months | Label changed | Two or more classes apart |
|---|---|---|---|
| Box, fire season | 49 | 16% (4–29) | 0% |
| Box, fire season, no flagged day for either satellite | 37 | 13.5% (3–23) | 0% |
| Box, fire season, baseline median at least 100 | 24 | 1 month | 0% |
| 100 km circles, fire season | 1,519 | 23% (18–28) | 7.4% |
| 100 km circles, fire season, baseline median at least 10 | 939 | 14% (11–18) | 1.5% |

The combined series changes 10% of fire-season box months and 16% at 100 km, which flatters it because half of it is Suomi NPP itself in 2018–2021. With these five classes, no conversion can be expected to agree with Suomi NPP's own labels in much more than about 85% of box months.

**How strong.**

- **Strong** for the gap lists, the masked ratios and factors, and the combined series. The reviewer rebuilt the flag from the catalogue and recomputed them independently.
- **Moderate** for the label noise. The intervals rest on 7–10 years (3–4 for NOAA-21), and the circle intervals are optimistic because circles overlap.
- **Limits.** The count-check simulations were re-run from the analyst's scripts, not reimplemented, and its thresholds were chosen after looking at the data. NOAA-20 on 1 April to 4 June 2018 is assumed available, though Suomi NPP saw 1.38 times NOAA-20's hotspots in July 2018. The flag for November 2026 is unverified.

## Approaches borrowed from other fields

Detail: [a03](harmonization-tests-research/a03-thinning-model.md), [a07](harmonization-tests-research/a07-box-counting.md), [a08](harmonization-tests-research/a08-completeness.md), [a09](harmonization-tests-research/a09-drift-curve.md), [a10](harmonization-tests-research/a10-diagnostics.md), [a11](harmonization-tests-research/a11-latent-models.md), [w01](harmonization-tests-research/w01-crossfield-sources-a.md), [w02](harmonization-tests-research/w02-crossfield-sources-b.md).

All of them have real, citable foundations. None has been applied to MODIS or VIIRS hotspot counts in any source found. Each fits the problem only as an analogy, and the analogy breaks in the same place: VIIRS is not a complete truth, and MODIS hotspots are not a random subset of VIIRS hotspots.

| Approach | Verdict | What the test showed |
|---|---|---|
| Thinning by expectation | Useful as an explanation | Identical to scaling up. It supplies the table of what a MODIS zero is consistent with. |
| Random thinning | Not useful | Worse than one factor, and it classes fewer months in small areas. Random loss of hotspots explains only 15–26% of the scatter, so a thinned series is not a simulation of MODIS. |
| Box counting | Useful as an explanation, not as a converter | The factor splits exactly into a pixel-size part (2.56 Suomi NPP hotspots per occupied 1 km cell) and a remaining part (0.62 MODIS hotspots per such cell). The remaining part carries about two thirds of the day-to-night difference. No cell-based conversion beat the plain ratio. |
| A detection curve for MODIS, with VIIRS as the reference | Not useful | The power at which Aqua detects half the time is not a fixed property: 12 MW measured one way, 55–70 MW another, and 8–47 MW between years. As a converter it is worse than one factor (error 0.37 against 0.30). |
| Counting only hotspots above a common power | Not useful | By day it steadies the ratio across years but discards half of the VIIRS record and does not cut single-month error. |
| The drift as a sampler of the daily fire cycle | Partly useful | Clear for Terra by day only. See [The orbit drift](#the-orbit-drift). |
| Control charts | Useful as a monitor | The only method that flagged Terra's daytime loss early. A monthly chart on NOAA-21 against NOAA-20 would catch only large shifts, because it rests on few months. |
| Double-mass curves | Useful as a picture | Straight through the stable years with slope 0.242. The only clear bend is Terra by day. |
| Bland-Altman limits of agreement | Useful for communication | Gives the plain statement in the table above. With ten seasons the limits themselves are uncertain. |
| Passing-Bablok regression, concordance correlation | Not useful | The correlation is inflated by the wide range of counts, and the regression has too few independent seasons. |
| Intervals from held-out-year errors | Useful for 10 or more predicted hotspots | Coverage as claimed. With only ten seasons to calibrate on, delivered coverage itself varies. |
| Item-response model of the sensors | Not useful | Rejected by its fit. It reproduces the simple ratios. Its one by-product is evidence that day and night behave as separate dimensions. |
| Hidden activity states | Not useful | Its 90% agreement between sensors is matched by plain ratio classes cut into the same number of groups (91%). |
| Shrinking small areas toward the region | Untested in a fair form | See [User-sized areas](#user-sized-areas). |

Two cautions from the source check:

- **Extrapolation.** The only published limit on extrapolating from a smaller sample that was found is two to three times the sample, and it is for species richness, not counts. Scaling MODIS up is a step of 4.1 times, and 18 times for Aqua at night.
- **Agreement rates are not comparable across schemes with different numbers of classes.** Coarser classes agree more often partly because there are fewer of them.

## New data found

Detail: [w03](harmonization-tests-research/w03-data-availability.md).

| Source | What it gives | Usable before the deadline |
|---|---|---|
| NASA's open granule catalogue | Every MODIS and VIIRS scene over the box, including passes that found no fire: 124,636 scenes, no login, a few minutes to fetch. It gives a per-day availability flag for each satellite. | Yes; already downloaded |
| BC Wildfire current-season layer | Provisional 2026 fires: 645 incidents in the box, about 410,000 ha | Yes; already downloaded |
| Canada's pollutant release registry | Facility locations, for labelling static sources | Yes |
| GOES-West fire product | Hourly fire data for a local daily cycle. Its pixels over the box are about 2.3 by 4.2 km, and it saw 14–30 fire pixels on a day when NOAA-20 saw 905 hotspots. | Later: days of work |
| Sentinel-3 fire radiative power | A morning observer besides Terra (passes near 09:00–11:00 local time) | Later: needs an account |
| Landsat active fire | 30 m fire pixels from June 2022 | Later, and only as a spot check |
| FIRMS swath outlines | A map layer only; no download | No |

**Limits of the availability flag.** It sees half-day losses, as a missing day or night pass, but it cannot see losses inside a scene: Aqua's 2020 failure looks normal in it. A check of daily counts against the other VIIRS satellites finds such a loss only when it is large and the fire is busy (see [Availability flag](#availability-flag-and-the-combined-viirs-series)). The near-real-time catalogue keeps only about seven days, so the current month may lack a flag; it missed Suomi NPP data on 4–6 August 2026.

**FIRMS acquisition times** are whole minutes, and appear to be the time of the pixel, not of the scene.

## What the tests say about a provisional pipeline

During this work the AI assistant was asked to rank methods and suggested a five-piece pipeline, and later an alternative. The team has not adopted either. The tests bear on each piece as follows.

| Piece | Supported by | Undercut by | Not tested |
|---|---|---|---|
| Combine VIIRS satellites as a daily mean of those with data | The earlier evidence. The availability flag it needs was built from the open catalogue and applied day by day; unlisted gaps had moved one yearly ratio by 12%. The combined series stays level through every real outage month and at each change in the number of satellites. | The flag cannot see losses inside a scene; a count check finds only large ones in busy periods. It is not verified for the current month and missed 4–6 August 2026. A NOAA-20 current month changes about one fire-season label in seven against Suomi NPP's own, before any conversion error. | The combined series as the current month inside the mixed-baseline class test. Label changes were measured only against Suomi NPP's own label. |
| Convert with one overlap factor, split by day and night | Fitting on the whole box over the stable years; labels barely move with the factor. No refinement of one all-hours factor gave better labels. | The split: 7 points worse over all months, and the two factors moved −23% and +46% within the decade. A seasonal night factor is still 4.7 points worse over all months; a split in the fire season only is level but may cost a few points. A size-dependent factor is no better. Any single factor runs 15–27% high in quiet fire-season periods and about a third low in typical November-to-March months. | Size-dependent factors other than the two forms tried. |
| Use MODIS to 2011 and VIIRS from 2012; flag drifted MODIS | VIIRS from 2012 avoids the drift. Flagging is what the data support for three of the four MODIS passes. The order of converted years holds. On the stable years, a converted era of the real composition gives the right class in 87% of fire-season months. | The level before 2012 cannot be validated and is plausibly high for small seasons. On the real 24-year baseline, 39% of box fire-season labels differ from VIIRS-only, against about 22% from the change of length alone, and the excess pushes months lower. | Whether that excess is real pre-2012 burning or conversion level. The Terra-only years against a known answer. |
| Validate on held-out years; show intervals and coarse classes | Whole years are the right unit. Size-grouped intervals hold for 10 or more predicted hotspots. | No honest interval below 10. A per-month interval omits the shared error of the factor. Coarse classes agree more partly because there are fewer. | Class probabilities; intervals for circles. |
| Show converted history only from about 100 km radius | 100 km is where it beats the VIIRS-only baseline on every measure. | At 50 km it is already slightly ahead on exact class, so the cut is cautious. Near Kamloops a small-area VIIRS record depends on removing the static site. | Regional context, a season in place of a month, and presence or absence, as displays. |
| Alternative: compare in MODIS-equivalent terms by thinning VIIRS | By expectation it gives the same class as scaling up. It is the direction that interpolates. | Random thinning is worse and does not fix zeros. | How users would read numbers about four times smaller than the counts shown for the current month. |

## Corrections to earlier documents

| Document | As written | What the tests show |
|---|---|---|
| [harmonization-evidence.md](harmonization-evidence.md) | The sensors give the same five-class label in 71% of fire-season months | 68–69% on the definitions used here. The earlier figure included a month's own year in its baseline and used UTC months. |
| [harmonization-evidence.md](harmonization-evidence.md) | Evidence for a gradual Terra daytime decline in 2023–2025 is "moderate" | Weak. It depends on the size adjustment. Only 2026 is established. |
| [harmonization-evidence.md](harmonization-evidence.md) | Near-real-time rows label day and night by orbit direction | The delivered labels match the sun-angle rule for every row. The data cannot yet tell the two rules apart. |
| [sensor-reference.md](sensor-reference.md), outage table | Suomi NPP gap of 26 July to 20 August 2022 | The catalogue shows scenes, and FIRMS has hotspots, on 11–20 August 2022. |
| [sensor-reference.md](sensor-reference.md), outage table | Terra gap of 26–27 March 2026 | Scenes exist on both days. The data were flagged questionable, not missing. |
| [sensor-reference.md](sensor-reference.md), outage table | No entry | Suomi NPP has no scenes on 30 May – 3 June, 10–15 July and 24–28 July 2024. Terra has none on 13–15 May 2025 and 5–10 March 2026. NOAA-21 has none on 10–14 January 2026. These are UTC dates; by local date the Terra gaps are 12–15 May 2025 and 4–9 March 2026. The follow-up also found no scenes for Suomi NPP on 25 March 2012, 26 July 2023 and 26 September 2024, for NOAA-20 on 30 September 2023, and for NOAA-21 on 27–28 February 2024 (local dates). |
| [sensor-reference.md](sensor-reference.md), outage table | Suomi NPP gap of 2–6 November 2024 | Scenes exist on 3 of the 5 days; the listed gap is about 3 days too wide. |
| [sensor-reference.md](sensor-reference.md), outage table | Terra gap of 15 April 2001 | Scenes exist, with no hotspots. |
| [sensor-reference.md](sensor-reference.md), outage table | No entry | NOAA-20 recorded no hotspots on 19–22 July 2023 while Suomi NPP recorded 34 to 597 a day, with normal scenes: a loss inside the scenes. |

## What is still missing

The follow-up tests answered three items listed here at first: a baseline of the real length, a repaired day and night split, and the availability flag applied throughout with the scale factors re-estimated. See [Follow-up tests](#follow-up-tests).

1. Whether the excess in label changes on the real baseline is real burning before 2012 or a conversion level about 1.6 times too high. The data in hand cannot separate them.
2. The current month taken from NOAA-20, or from the daily mean of the VIIRS satellites, inside the mixed-baseline class test. So far it has been compared only with Suomi NPP's own label.
3. The effect of the winter undershoot on converted 2003–2011, when November to March held a quarter of MODIS hotspots, against 10% in the overlap years.
4. Small-area displays scored fairly: regional context, a season in place of a month, presence or absence.
5. Class probabilities, and any honest interval for months under about 10 predicted hotspots.
6. An independent daily fire cycle for the region, to check the fitted 13.4 h peak before a Terra correction is relied on.
7. The reliability of NOAA-20 on 1 April to 4 June 2018, which the catalogue does not cover and which is assumed available.
8. Final 2026 BC area burned (April 2027).
9. NOAA-21 against MODIS directly. There is no stable-orbit overlap, only a chain through NOAA-20.
10. Whether near-real-time and standard rows differ for the current month in anything besides the label. In 2026, Suomi NPP / NOAA-20 is 0.999 in the near-real-time months of August to October against 1.046 in January to July.
11. The availability flag for the current month, which the near-real-time catalogue keeps for only about seven days.

## Changes since first compiled

Each change was made in place above, on 2026-11-14, from the three follow-up tests reported under [Follow-up tests](#follow-up-tests).

| Date | Statement | First compilation | Now | Source |
|---|---|---|---|---|
| 2026-11-14 | Direction of the bias of one factor in quiet periods ("At a glance" point 8; the table on factor stability; the pipeline table) | Runs about 15–27% high in quiet months and small seasons | High only in the fire season. In typical November-to-March months it runs low under every design (0.66 times actual, 0.54–0.79, for one factor). | [f02](harmonization-tests-research/f02-factor-refinements.md) |
| 2026-11-14 | Limits of the availability flag | Cannot see partial losses | Sees half-day losses as a missing day or night pass; cannot see losses inside a scene. A count check finds only large losses in busy periods. The flag also missed Suomi NPP data on 4–6 August 2026. | [f03](harmonization-tests-research/f03-availability-flag.md) |
| 2026-11-14 | Listed outage dates the catalogue contradicts ("At a glance" point 13; corrections table) | Two | Four: Suomi NPP 11–20 August 2022 and 2–6 November 2024, Terra 15 April 2001 and 26–27 March 2026. Further unlisted gaps and a NOAA-20 loss on 19–22 July 2023 were added to the corrections table. | [f03](harmonization-tests-research/f03-availability-flag.md) |
| 2026-11-14 | Suomi NPP against NOAA-20 by year (table on factor stability) | No step or trend; 2024 dip explained | Added: the high 2023 value (1.064) was the NOAA-20 loss of July 2023; masked it is 1.028, and the series runs 0.93–1.07. | [f03](harmonization-tests-research/f03-availability-flag.md) |
| 2026-11-14 | Day and night split ("At a glance" point 4; pipeline table) | Did not earn its place; a seasonal night factor untested | Added the repaired splits: a seasonal night factor is still 4.7 points worse over all months, and a split in the fire season only is level but may cost a few points. No refinement beat one factor. | [f02](harmonization-tests-research/f02-factor-refinements.md) |
| 2026-11-14 | "Not tested" in the pipeline table | A baseline of the real length; a seasonal night factor; a size-dependent factor; the combining rule at circle scale | Moved to "Supported by" or "Undercut by" with the follow-up results. What remains untested is listed in its place. | [f01](harmonization-tests-research/f01-real-length-baseline.md), [f02](harmonization-tests-research/f02-factor-refinements.md), [f03](harmonization-tests-research/f03-availability-flag.md) |
| 2026-11-14 | "At a glance" | Thirteen points | Two points added, on the real-length baseline and on label changes from a change of satellite | [f01](harmonization-tests-research/f01-real-length-baseline.md), [f03](harmonization-tests-research/f03-availability-flag.md) |
| 2026-11-14 | "What is still missing" | Ten items | The three answered items removed; items found missing by the follow-ups added | [f01](harmonization-tests-research/f01-real-length-baseline.md), [f02](harmonization-tests-research/f02-factor-refinements.md), [f03](harmonization-tests-research/f03-availability-flag.md) |
| 2026-11-14 | Which designs remove the fire-season bias ("Refinements of the factor") | The day and night designs (0.98–0.99) | The plain split (0.99) and the fire-season split (0.98); the seasonal night factor leaves 1.07 | [f02](harmonization-tests-research/f02-factor-refinements.md), Protocol A table |

## How this was produced

| File | Question |
|---|---|
| [a01-hindcast-box.md](harmonization-tests-research/a01-hindcast-box.md) | Does a converted record give the right class? Whole box |
| [a02-hindcast-circles.md](harmonization-tests-research/a02-hindcast-circles.md) | The same, for user-sized areas |
| [a03-thinning-model.md](harmonization-tests-research/a03-thinning-model.md) | Thinning: irreducible scatter, and what a zero means |
| [a04-factor-stability.md](harmonization-tests-research/a04-factor-stability.md) | Is the factor stable, and does it survive the end of Suomi NPP? |
| [a05-pre2012-check.md](harmonization-tests-research/a05-pre2012-check.md) | Can the factor be trusted before 2012? |
| [a06-daynight-rule.md](harmonization-tests-research/a06-daynight-rule.md) | One day-and-night rule for every row |
| [a07-box-counting.md](harmonization-tests-research/a07-box-counting.md) | Separating pixel size from sensitivity |
| [a08-completeness.md](harmonization-tests-research/a08-completeness.md) | A detection curve for MODIS; counts above a common threshold |
| [a09-drift-curve.md](harmonization-tests-research/a09-drift-curve.md) | Using the drift to trace the daily fire cycle |
| [a10-diagnostics.md](harmonization-tests-research/a10-diagnostics.md) | Double-mass curves, control charts, agreement statistics |
| [a11-latent-models.md](harmonization-tests-research/a11-latent-models.md) | Item-response model and hidden activity states (single agent, not independently reviewed) |
| [a12-static-sources.md](harmonization-tests-research/a12-static-sources.md) | Static and recurring sources |
| [w01-crossfield-sources-a.md](harmonization-tests-research/w01-crossfield-sources-a.md) | Sources: thinning, rarefaction, inverse problems, box counting, completeness |
| [w02-crossfield-sources-b.md](harmonization-tests-research/w02-crossfield-sources-b.md) | Sources: agreement statistics, control charts, intervals, latent models, drift as sampling |
| [w03-data-availability.md](harmonization-tests-research/w03-data-availability.md) | What extra data could be obtained (single agent, not independently reviewed) |
| [f01-real-length-baseline.md](harmonization-tests-research/f01-real-length-baseline.md) | Follow-up: how does a baseline of the real length behave? |
| [f02-factor-refinements.md](harmonization-tests-research/f02-factor-refinements.md) | Follow-up: does any refinement of the factor beat one all-hours factor? |
| [f03-availability-flag.md](harmonization-tests-research/f03-availability-flag.md) | Follow-up: a per-day availability flag, and the VIIRS satellites combined with it |
| [_cross-check.md](harmonization-tests-research/_cross-check.md) | Reconciled numbers and conflicting conclusions |

- **AI assistance.** The tests, source checks and this write-up were produced with AI agents (Claude) on 14 November 2026: 29 agents ran and checked the analyses, and the results were aggregated into this document. The cross-field approaches were proposed by the AI assistant from memory and then sourced and tested. The Space Apps submission guide requires that such use be acknowledged, and says AI should not be used to come up with the idea of how to solve the challenge. The choice of method is the team's.
- **AI assistance in the follow-ups.** The three follow-up tests were run later on 14 November 2026 by AI agents (Claude): for each, one agent ran the analysis and a second re-ran it and recomputed it independently. The review of the real-length baseline added two remedies to those the analyst tested. The section "Follow-up tests", the updates elsewhere in this document and the corrections listed under "Changes since first compiled" were written by an AI agent from those working files. A final review by an AI agent the same day re-checked them against the working files and the catalogue, and carried the follow-up results into the other three documents.
- **Limits of the whole exercise.** One box and ten stable-orbit years, dominated by three large fire seasons (2017, 2018, 2021). The 202 splits reuse those ten years, so the spread across splits understates the uncertainty. The answer each design is scored against is a nine-year VIIRS median, not fire itself.
- **Scripts and tables.** The working files name the scripts and result tables behind each number. Those are kept outside version control with the cached data.
