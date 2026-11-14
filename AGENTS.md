# Agents

Guidance for AI coding agents and humans in this repository. This is Lee Bergstrand's team (City of Kamloops & Co.) for NASA Space Apps 2026.

## Purpose

Build a web app that harmonizes MODIS and VIIRS active-fire hotspots into a burning-activity calendar, so a user can compare current burning in a selected area with its history. Challenge facts, data limits, and the current proposal are in [docs/challenge.md](docs/challenge.md). Read that before changing data handling or the calendar.

## Sensor reference

Facts about the sensors, satellites, orbits, fire products and FIRMS files are in [docs/sensor-reference.md](docs/sensor-reference.md). Read the relevant section before changing how hotspots from different sensors are loaded, filtered, counted or combined.

- It states facts only. It does not choose a harmonization method.
- Start with its "At a glance" list and the "Which sensors were flying when" table.
- Per-topic detail and full source lists are in [docs/sensor-research/](docs/sensor-research/). Those fifteen files are large (about 650 KB together). Open one only when the report's section is not enough.
- It was compiled on 2026-11-13, after `docs/challenge.md`, and is the newer source where the two differ. For example, open yearly country files do exist for NOAA-20, under the prefix `viirs-jpss1`.

## Harmonization evidence

The team's research handoff and recommended method are in [docs/harmonization-research.md](docs/harmonization-research.md), and `harmonize.py` implements an interim version of it. Read both before changing how the calendar is computed.

Three further documents report what the team's own FIRMS data and the literature show about combining the sensors. All three were corrected on 2026-11-14; each lists its corrections under "Changes since first compiled".

- [docs/harmonization-evidence.md](docs/harmonization-evidence.md): the first measurements on the team's data, arranged by the choices the team has to make. Read it before deciding how counts are converted, combined or compared.
- [docs/harmonization-methods.md](docs/harmonization-methods.md): a catalogue of candidate methods with published precedent and effort. Read it when looking for a method or for precedent to cite.
- [docs/harmonization-tests.md](docs/harmonization-tests.md): the latest tests, including three follow-ups, with how strong each result is. It is the newest of the three and wins where they differ. Read it before relying on any number.

Findings that any code touching the hotspot record has to respect. Each is from those documents.

- **Months are keyed by local date.** Keying by UTC date moved 455 MODIS hotspots from 30 June 2021 into July, because Terra's evening pass falls after midnight UTC.
- **The fixed heat source near 50.688°N, 120.408°W is removed before any scaling.** It is seen on 712 dates in 2012–2026, only by the VIIRS satellites and only at night, and no scale factor can remove an added constant.
- **Counts from several VIIRS satellites are not summed or pooled against a single-satellite baseline.** Summing gives 1.99 times one satellite's count from April 2018 and 2.95 times from March 2023.
- **Conversion factors are fitted on the whole box over the stable-orbit years, not on a user's area.** The tested factor is 0.2425 (Terra plus Aqua over Suomi NPP) on the 116 stable-orbit months of 2012–2021. In a 25 km circle MODIS records nothing in 40% of the months in which Suomi NPP saw fire.
- **Near-real-time rows have no `type` column.** The newest months of any download are near-real-time; in the team's data on 14 November 2026, standard rows ended on 29 August 2026 for MODIS and 31 July 2026 for VIIRS.
- **Converted history is unsupported below about 50 km radius.** At 25 km a VIIRS-only baseline gives the right class more often, and only 22% of fire-season months can be classed at all; at 50 km the converted baseline is borderline, and from about 100 km it is supported without qualification.
- **The published outage list is incomplete.** NASA's open granule catalogue showed unlisted gaps and listed gaps that are wrong; the dates are in the outage table of the sensor reference.
- **Suomi NPP data ended at 15:40 UTC on 2 November 2026,** and Terra's daytime count in 2026 is about half of normal (0.41–0.61 across five methods).

The Space Apps submission guide requires that AI assistance be acknowledged. The choice of harmonization method is the team's; these documents report evidence and do not choose it.

## Deadline

Hackathon: Saturday 14 November through Sunday 15 November 2026. Submissions close Sunday 15 November 2026 at 11:59 PM Kamloops time (UTC-7).

Every decision favors a working demo and a complete submission. Cut scope. Do not gold-plate.

## Stack

- Python 3, Streamlit, and pandas. Dependencies are listed in `requirements.txt`.
- Cache FIRMS downloads under `data/`. That directory is git-ignored except `data/.gitkeep`. Do not commit cached files.

## Secrets

`FIRMS_MAP_KEY` comes only from a git-ignored `.env`. Never put the key in code, commits, logs, or pull requests.

## Workflow

- One change per branch. Open a pull request against `main`.
- The pull request says what the change does and how it was tested.
- Never push to `main`, merge, force-push, delete branches, or change repository settings. Lee merges.

## Code

- Simple code. Make the smallest change that works.
- Run it before calling it done. Test behavior, not implementation.
- No speculative abstractions.

## Demo

The demo must run offline from cached data. Do not require a live FIRMS call or a MAP_KEY at demo time.
