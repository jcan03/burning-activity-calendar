# What the challenge and judging material say about the open decisions

## Answer

The challenge text and the author leave all five decisions open, with three firm points. The author accepts either a MODIS-equivalent or a VIIRS-equivalent record "if properly justified". She wants continuity through NOAA-20 and NOAA-21. She calls monthly data "a solid approach", and weekly only "provided it is feasible". The challenge page names the quantity to show as "the number of hotspots", compared with "the historical median", over a calendar "from the early 2000s to the present". It never mentions fire radiative power, day versus night, or a minimum area. Nothing newer than 13 November 2026 changes this. Thread #1879 still has 2 comments, the last from the author at 18:26 UTC on 13 November, checked at 18:42 UTC on 14 November. The challenge page was last published at 03:46 UTC on 13 November. Of the five official judging criteria, Validity ("grounded in scientific principles") and Relevance (NASA data as "a core component") bear most directly on the harmonization.

## Evidence

### The five decisions

"Page" means the official challenge page and "Author" means the challenge author's reply in discussion #1879. "Team notes" means `docs/challenge.md`, `AGENTS.md`, `README.md`, `challenge-assessment.md` and `space-apps-2026-briefings.md`.

| Decision | What the official material says (exact quote, source) | What it leaves open | What the team notes already assume |
|---|---|---|---|
| 1. Counts or a class/index | Page: "A calendar of burning activity showing the number of hotspots detected"; "compare the burning activity of the current month against the historical median for a selected area"; "how color ramps might represent similarities and differences in the number of detected hotspots across months"; optional indices: "Historical comparisons, including anomalies against multi-year averages" and "Number of fires detected and reported". | Whether the colour shows absolute numbers or a category relative to the median. Whether an anomaly uses the median or the mean (the page uses both words). Whether "number of hotspots" may be a derived count such as cell-days. | A "current month vs median" card, an accessible colour ramp, and "fire cell-days" (grid cells with any detection) next to raw counts (assessment). Pre-2012 values are to be "labelled as modelled, with an uncertainty band" (assessment). |
| 2. Baseline start | Page: "from the early 2000s to the present"; "combining the extensive historical series of MODIS with the continuity and greater detail of VIIRS". Video (as summarised in `challenge.md`): without harmonization "almost 10 years of historical information will be lost". | Whether a baseline that starts in 2012 meets the request. The page asks for a calendar back to the early 2000s, not for a baseline of a particular length. | "a monthly step from the early 2000s to the present" (`challenge.md` proposal). The record starts 1 Nov 2000 (Terra only) and 4 Jul 2002 (Terra and Aqua). |
| 3. Target record | Author: "Either alternative is fine if properly justified." Page: "so that by the end of that phase the sensor of origin no longer matters". | Which one to pick, and what counts as "properly justified". | `challenge.md` leaves it open. The assessment says "Anchor to NOAA-20" and "Calibrate in the overlap years: Aqua against afternoon VIIRS". |
| 4. Day and night | Nothing in the page, the video summary or the author's replies. | Everything. | "day and night calendars" is listed only as a stretch goal (assessment). The notes record that near-real-time rows set `daynight` by a different rule. |
| 5. Area size and time step | Page: "a map where users can draw the area of interest, or an option to enter latitude and longitude"; "select a region and a specific date range". Author: daily data "generally exhibit high variability that could blur underlying patterns. Monthly data seems like a solid approach, and weekly data could be interesting, provided it is feasible… is it possible to create a calendar that contains so much data and remains easy to visualize?" | Any minimum area. Whether a week is calendar or ISO. | Kamloops and Interior BC, a monthly step, a drawn box or lat/lon entry, and a 0.1° grid per day (`challenge.md`, assessment). |

A related fact from `docs/sensor-reference.md`: the MODIS fire user's guide warns of "severe temporal and spatial biases" in time series with intervals "shorter than about eight days". A calendar week is 7 days.

### What constrains the harmonization itself

| Constraint | Exact wording and source |
|---|---|
| The method must be justified | Author: "Either alternative is fine if properly justified." |
| FIRMS is acceptable data | Author: "Yes, it is acceptable since FIRMS is the suggested NASA resource for the challenge." The Resources tab lists FIRMS as its only NASA resource. |
| Other routes are allowed, but NASA resources come first | Author on Earth Engine: "Yes it is acceptable, but keep in mind to use NASA suggested resources during the challenge solving process." |
| The record must continue past MODIS | Author: "it makes sense to look for solutions that extend into the future—therefore, NOAA-20 and NOAA-21 satellites that are still active." |
| The sensor must stop mattering | Page: "the sensor of origin no longer matters and the patterns, trends, and anomalies become the focus." |
| Outputs | Page: download "analytics and visualizations"; "A downloadable CSV File of hot spots detected during a search would be another useful output." |
| NASA data is required for global awards | Submission guide: "To be eligible for a Global Award, you must use at least one NASA data or resource." |
| Demo limits | Submission guide: "Video (30 seconds or less) or slide deck (up to seven slides including title and intro slides)". Projects over these limits "will not be eligible for Global Judging". |
| Use of AI tools must be declared | Submission guide: "Code and data: Must acknowledge SI generation in descriptive text and metadata." It also says SI "should not be used to (come up with your idea of how to solve the challenge)." "SI" is the organisers' word for AI. |
| Team rule | `AGENTS.md`: "Every decision favors a working demo and a complete submission. Cut scope." "The demo must run offline from cached data." |

### Judging criteria in the organisers' words

The submission guide says: "Your project will be evaluated using five criteria: Impact, Creativity, Validity, Relevance, and Presentation." The judging guide's text for a score of 5 is:

| Criterion | Score-of-5 text (judging and awards guide) |
|---|---|
| Impact | "addressing a significant problem with proposed solutions. Its reach is extensive, inspiring, benefits a large audience, or could change the world." |
| Creativity | "introducing a groundbreaking approach that has never been attempted before. It challenges conventional methods" |
| Validity | "scientifically sound and technically feasible, demonstrating strong alignment with established principles. It is fully developed and ready for real-world implementation… highly usable and user-friendly" |
| Relevance | "NASA data is integral to the project's success, providing meaningful insights… The use of data is well-executed, enhancing both the credibility and impact of the solution." |
| Presentation | "clearly articulating the challenge, proposed solution, and importance of the project." The general description adds: "Judges evaluate the demo and full project to compute this score." |

The general (not score-5) Validity description says a project should be "grounded in scientific principles". The guide also says to "pay equal attention to the final criterion: presentation". One of the ten global awards is "Best Use of Science: The project that makes the best and most valid use of the scientific method."

### Newer material checked on 14 November 2026

- Discussion #1879 has no replies after 13 November. Five other threads about this challenge were read: #1786, #1959, #2016, #2080 and #2125. They contain replies only from participants and Space Apps navigators, none from the author. One navigator (#2016) wrote that "the most important part of this challenge is to demonstrate how MODIS and VIIRS observations can be harmonized". That is not an official ruling.
- The question in #1879 dates the end of Suomi NPP data to 2 November 2022. The team's sensor reference gives 2 November 2026. The author did not correct the date.

## What this implies for the approach

- **Target record.** The material does not favour either target. Whichever target the team picks, the write-up must justify it. A MODIS-equivalent target still has to be produced from VIIRS alone after Terra and Aqua retire, because the author wants NOAA-20 and NOAA-21 continuity.
- **Unit.** The page names "number of hotspots" and "historical median". Raw counts, or a median-relative class built on counts, match the wording most directly. Cell-days or anomalies are allowed, but each would need a sentence explaining how it relates to "number of hotspots". Fire radiative power appears nowhere in the challenge material.
- **Scaling.** Nothing prescribes the form of the scaling. Validity ("grounded in scientific principles", "scientifically sound") is the test it will be judged against. The view that "a single scaling factor will not survive a remote-sensing judge" comes from the team's own assessment, not from the organisers.
- **Combining VIIRS satellites.** NOAA-20 and NOAA-21 are expected. The method has to cope with the number of VIIRS satellites changing (1, 2, 3, then 2 after Suomi NPP ended on 2 November 2026). November 2026, the current month, is split by that change.
- **MODIS since 2022.** The challenge material says only that MODIS is "approaching the end of its operational life". How to treat the orbit drift is entirely the team's choice and must be explained.
- **Time step and day/night.** A monthly step has the author's explicit support. A weekly step is below the MODIS guide's roughly 8-day threshold, and the author asks whether it would stay readable. Showing day and night separately is neither asked for nor ruled out.

## Limits

- The author video was not re-watched. Its content comes from `challenge.md`, which relies on an auto-generated transcript.
- The judging guide page shows no publication date. It is taken to be the 2026 guide because the submission guide links to the "2026 Judging and Awards Guide" and the page names the 2026 partners. The 1-to-5 scale was not found in the extracted text and is unconfirmed for 2026.
- Kamloops local judges may weigh the criteria differently. No local rubric was found.
- The author may still reply after 18:42 UTC on 14 November 2026.
- WebFetch failed with a TLS certificate error. Pages were read with curl from the JSON embedded in the HTML, and the GitHub threads through the GitHub API. Wording could differ slightly from the rendered page.

## Sources

- Challenge page (details and Resources tab, `lastPublishedAt` 2026-11-13T03:46Z): https://www.spaceappschallenge.org/2026/challenges/modis-and-viirs-hot-spots/
- Author Q&A: https://github.com/nasa/spaceapps/discussions/1879
- Other threads about this challenge: https://github.com/nasa/spaceapps/discussions/1786, /1959, /2016, /2080, /2125
- Judging and awards guide: https://www.spaceappschallenge.org/resources/judging-awards-guide/
- Project submission guide: https://www.spaceappschallenge.org/resources/project-submission-guide/
- Local team files: `docs/challenge.md`, `docs/sensor-reference.md` ("At a glance"; "Observations per day"; "What NASA says about combining the sensors"), `AGENTS.md`, `README.md`, `../challenge-assessment.md` (sections 1 and 09), `../space-apps-2026-briefings.md` (preamble and section 09)
- Helper used to read the pages: `scripts/decode_next.py`
