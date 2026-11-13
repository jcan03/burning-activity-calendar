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
