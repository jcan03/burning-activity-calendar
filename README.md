# Kamloops Burning Activity Calendar

A web app for the NASA Space Apps 2026 challenge [Harmonization of MODIS and VIIRS Hot Spots](https://www.spaceappschallenge.org/2026/challenges/modis-and-viirs-hot-spots/). Team: City of Kamloops & Co.

The app is a Streamlit page (`app.py`) that runs offline from cached FIRMS data.

## Goal

Build a monthly burning activity calendar that merges MODIS and VIIRS (S-NPP, NOAA-20, and NOAA-21) fire detections for an area of interest, with a focus on Kamloops and Interior BC. Users will pick an area and a date range, compare recent fire activity against the long-term record, and download a CSV.

## Data sources

Fire detections come from [FIRMS](https://firms.modaps.eosdis.nasa.gov/api/):

- Open yearly country CSVs at the [FIRMS country data page](https://firms.modaps.eosdis.nasa.gov/data/country/)
- Near-real-time and other recent data via the FIRMS API, which needs a MAP_KEY from the [FIRMS MAP_KEY request page](https://firms.modaps.eosdis.nasa.gov/api/map_key)

## Documentation

- [docs/challenge.md](docs/challenge.md): what the challenge asks for, the author's clarifications, FIRMS access notes and the team's proposed direction.
- [docs/sensor-reference.md](docs/sensor-reference.md): sourced facts about MODIS and VIIRS needed to harmonize the records. It covers the satellites and orbits, the instruments, coverage and overpass timing, the detection algorithms, FIRMS columns and processing streams, outages, and where sources disagree. It states facts only and recommends no method.
- [docs/sensor-research/](docs/sensor-research/): the fifteen working files behind the sensor reference, one per topic, each with its full source list.
- [docs/harmonization-research.md](docs/harmonization-research.md): research on how to combine the two sensors, with a recommended method and how well it tested.

## Setup

1. Create and activate a virtual environment:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Copy `.env.example` to `.env` and add your `FIRMS_MAP_KEY`.

4. Download the Kamloops-area hotspots into `data/kamloops/` (about 1 GB of all-Canada yearly files is streamed and clipped; about 70 MB is saved):

   ```bash
   python download_kamloops.py
   ```

   Without a key it still saves the open yearly MODIS, S-NPP and NOAA-20 files; it skips recent dates and NOAA-21. Re-running skips files already downloaded.

5. Build the SQLite database the app reads (`data/kamloops.sqlite`):

   ```bash
   python build_db.py
   ```

6. Optional: download the terrain drawn under the maps and the 3D view (`data/basemap.jpg` and `data/terrain.npz`, 5 MB together, from NASA GIBS, no key needed). Without it the maps have a plain background:

   ```bash
   python download_basemap.py
   ```

7. Run the app. It needs no internet and no `FIRMS_MAP_KEY`:

   ```bash
   streamlit run app.py
   ```

## Repo layout

- `README.md`: this file
- `.env.example`: template for the FIRMS MAP_KEY (copy to `.env`, which is gitignored)
- `requirements.txt`: Python dependencies
- `download_kamloops.py`: caches FIRMS hotspots for the Kamloops area in `data/kamloops/`
- `build_db.py`: loads the cached CSVs into `data/kamloops.sqlite`
- `download_basemap.py`: caches NASA terrain for the area: a shaded-relief picture (`data/basemap.jpg`) and elevation with a water mask (`data/terrain.npz`)
- `app.py`: the Streamlit app (calendar, season and daily views, map, method, CSV download)
- `charts.py`: the Plotly figures the app shows
- `animations.py`: the Map tab's period timeline, timelapse map and 3D columns that rise and fall through a period
- `harmonize.py`: interim MODIS and VIIRS harmonization, to be replaced by the team's final method
- `.streamlit/config.toml`: light theme and no usage statistics
- `docs/`: challenge reference, sensor reference and its research files (see [Documentation](#documentation))
- `data/`: local FIRMS downloads (gitignored except `data/.gitkeep`)
