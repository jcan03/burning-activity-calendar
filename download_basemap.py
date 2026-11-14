"""Download terrain for the data area: a relief picture for the maps and elevation for the 3D view.

Run once while online:  python download_basemap.py
The app still runs without these files; the maps then have a plain background.

Everything comes from NASA GIBS in plain latitude/longitude, so it lines up with
the hotspot coordinates. No key needed. Three layers:
- ASTER_GDEM_Greyscale_Shaded_Relief -> data/basemap.jpg, drawn under the flat maps.
- ASTER_GDEM_Color_Index -> elevation in metres. GIBS serves it as colours, and its
  colour map says which elevation each colour stands for (10 to 25 m steps here).
- MODIS_Terra_L3_Land_Water_Mask -> lakes and wide rivers (250 m).
Elevation and water are saved together in data/terrain.npz.
"""
import io
import re
from pathlib import Path

import numpy as np
import requests
from PIL import Image

from harmonize import BOX

GIBS = "https://gibs.earthdata.nasa.gov"
DATA = Path(__file__).parent / "data"


def picture(layer, pixels_per_degree, kind):
    """One GIBS layer over the data box, as image bytes."""
    south, west, north, east = BOX
    r = requests.get(f"{GIBS}/wms/epsg4326/best/wms.cgi", timeout=300, params={
        "SERVICE": "WMS", "REQUEST": "GetMap", "VERSION": "1.1.1", "SRS": "EPSG:4326", "STYLES": "",
        "LAYERS": layer, "FORMAT": f"image/{kind}", "BBOX": f"{west},{south},{east},{north}",
        "WIDTH": round((east - west) * pixels_per_degree), "HEIGHT": round((north - south) * pixels_per_degree)})
    r.raise_for_status()
    if not r.headers.get("content-type", "").startswith("image"):
        raise SystemExit(f"GIBS did not return a picture for {layer}: {r.text[:300]}")
    return r.content


def main():
    relief = picture("ASTER_GDEM_Greyscale_Shaded_Relief", 800, "jpeg")
    (DATA / "basemap.jpg").write_bytes(relief)
    print(f"basemap.jpg: {len(relief) / 1e6:.1f} MB")

    # Each colour of the elevation layer stands for a range of metres; keep the bottom of the range.
    colours = requests.get(f"{GIBS}/colormaps/v1.3/ASTER_GDEM_Color_Index.xml", timeout=60)
    colours.raise_for_status()
    entries = re.findall(r'<ColorMapEntry rgb="(\d+),(\d+),(\d+)"[^>]*? value="\[(-?\d+)', colours.text)
    metres = {(int(r) << 16) | (int(g) << 8) | int(b): max(int(low), 0) for r, g, b, low in entries}
    rgb = np.asarray(Image.open(io.BytesIO(picture("ASTER_GDEM_Color_Index", 400, "png"))).convert("RGB")).astype(np.int32)
    packed = (rgb[..., 0] << 16) | (rgb[..., 1] << 8) | rgb[..., 2]
    known, where = np.unique(packed, return_inverse=True)
    elevation = np.array([metres.get(int(c), -1) for c in known], dtype=np.int16)[where].reshape(packed.shape)
    elevation = np.where(elevation < 0, np.roll(elevation, 1, axis=1), elevation)   # a stray empty pixel takes its neighbour

    water = np.asarray(Image.open(io.BytesIO(picture("MODIS_Terra_L3_Land_Water_Mask", 400, "png"))).convert("RGBA"))[..., 3] > 0
    np.savez_compressed(DATA / "terrain.npz", elevation=elevation, water=water)
    print(f"terrain.npz: {(DATA / 'terrain.npz').stat().st_size / 1e6:.1f} MB, {elevation.shape[1]} x {elevation.shape[0]} cells, "
          f"{elevation.min()} to {elevation.max()} m, {water.mean():.1%} water")


if __name__ == "__main__":
    main()
