# Kamloops Burning Activity Calendar

A web app for the NASA Space Apps 2026 challenge [Harmonization of MODIS and VIIRS Hot Spots](https://www.spaceappschallenge.org/2026/challenges/modis-and-viirs-hot-spots/). Team: City of Kamloops & Co.

The app is coming soon. This repo currently holds setup files only.

## Goal

Build a monthly burning activity calendar that merges MODIS and VIIRS (S-NPP, NOAA-20, and NOAA-21) fire detections for an area of interest, with a focus on Kamloops and Interior BC. Users will pick an area and a date range, compare recent fire activity against the long-term record, and download a CSV.

## Data sources

Fire detections come from [FIRMS](https://firms.modaps.eosdis.nasa.gov/api/):

- Open yearly country CSVs at the [FIRMS country data page](https://firms.modaps.eosdis.nasa.gov/data/country/)
- Near-real-time and other recent data via the FIRMS API, which needs a MAP_KEY from the [FIRMS MAP_KEY request page](https://firms.modaps.eosdis.nasa.gov/api/map_key)

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

## Repo layout

- `README.md`: this file
- `.env.example`: template for the FIRMS MAP_KEY (copy to `.env`, which is gitignored)
- `requirements.txt`: Python dependencies
- `data/`: local FIRMS downloads (gitignored except `data/.gitkeep`)
