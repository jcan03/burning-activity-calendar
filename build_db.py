"""Load the cached Kamloops hotspots (data/kamloops/*.csv) into data/kamloops.sqlite.

Run after download_kamloops.py:  python build_db.py
Rebuilds the database from scratch each time.

One table, `hotspots`: one row per FIRMS hotspot with the FIRMS columns plus
`source`. MODIS-only columns (brightness, bright_t31) are NULL for VIIRS rows
and VIIRS-only columns (bright_ti4, bright_ti5) are NULL for MODIS rows.
`type` is NULL for near-real-time rows. `confidence` is text: 0-100 for MODIS,
l/n/h for VIIRS.
"""
import sqlite3
from pathlib import Path

import pandas as pd

DATA = Path(__file__).parent / "data"
DB = DATA / "kamloops.sqlite"
TEXT_COLS = {"acq_time": str, "version": str, "confidence": str}


def main():
    files = sorted((DATA / "kamloops").glob("*.csv"))
    df = pd.concat(pd.read_csv(f, dtype=TEXT_COLS) for f in files)
    df["type"] = df["type"].astype("Int64")

    DB.unlink(missing_ok=True)
    with sqlite3.connect(DB) as con:
        df.to_sql("hotspots", con, index=False)
        con.execute("CREATE INDEX idx_date ON hotspots (acq_date)")
        con.execute("CREATE INDEX idx_satellite_date ON hotspots (satellite, acq_date)")
        count = con.execute("SELECT COUNT(*) FROM hotspots").fetchone()[0]
    print(f"{count} hotspots from {len(files)} files in {DB}")


if __name__ == "__main__":
    main()
