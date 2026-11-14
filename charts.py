"""Plotly figures for the burning calendar. Each function takes tables from harmonize.py."""
import base64
import io
from functools import lru_cache
from pathlib import Path

import numpy as np
import pandas as pd
import plotly.graph_objects as go
from PIL import Image
from plotly.subplots import make_subplots

from harmonize import BASE_YEARS, BOX, MODIS, OVERLAP, SPLICE, daily_index

# Both cover the data box, north row first, and come from download_basemap.py.
BASEMAP = Path(__file__).parent / "data" / "basemap.jpg"   # shaded-relief picture for the flat maps
TERRAIN = Path(__file__).parent / "data" / "terrain.npz"   # elevation in metres and a water mask for the 3D view

MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
CLASSES = ["Much below normal", "Below normal", "Near normal", "Above normal", "Much above normal"]
# Blue to red around a neutral grey; adjacent steps stay distinct with colour-blind vision.
CLASS_COLORS = ["#1c5cab", "#86b6ef", "#d9d8d4", "#ee8a82", "#c5302c"]
UNRANKED = "#a3a29d"
BLUES = ["#cde2fb", "#9ec5f4", "#6da7ec", "#3987e5", "#256abf", "#184f95", "#0d366b"]
VIIRS_COLOR, MODIS_COLOR, MUTED, INK = "#2a78d6", "#eb6834", "#8a8984", "#3b3b38"
CITIES = {"Kamloops": (50.6745, -120.3273), "Kelowna": (49.888, -119.496), "Vernon": (50.267, -119.272),
          "Penticton": (49.499, -119.594), "Merritt": (50.111, -120.786), "Salmon Arm": (50.700, -119.284),
          "Lillooet": (50.686, -121.936), "Williams Lake": (52.141, -122.141), "100 Mile House": (51.644, -121.295),
          "Revelstoke": (50.998, -118.196), "Clearwater": (51.650, -120.038), "Princeton": (49.458, -120.510),
          "Chase": (50.819, -119.686), "Logan Lake": (50.494, -120.813), "Savona": (50.753, -120.844),
          "Sun Peaks": (50.884, -119.886), "Barriere": (51.183, -120.124), "Ashcroft": (50.724, -121.281),
          "Lytton": (50.231, -121.581)}


@lru_cache(maxsize=1)
def _basemap():
    """The terrain picture as a grey array, lightened so the data stands out. None if it is not downloaded."""
    if not BASEMAP.exists():
        return None
    grey = np.asarray(Image.open(BASEMAP).convert("L"), dtype=float)
    return (255 - (255 - grey) * 0.5).astype(np.uint8)


def _crop(grid, bbox):
    """The part of a grid of the whole data box that lies inside bbox."""
    south, west, north, east = bbox
    rows, cols = grid.shape
    left, right = np.round((np.array([west, east]) - BOX[1]) / (BOX[3] - BOX[1]) * cols).astype(int)
    top, bottom = np.round((BOX[2] - np.array([north, south])) / (BOX[2] - BOX[0]) * rows).astype(int)
    return grid[top:bottom, left:right]


def terrain(bbox, max_pixels):
    """The part of the terrain picture inside bbox, at most max_pixels on its longer side. None if not downloaded."""
    full = _basemap()
    if full is None:
        return None
    picture = Image.fromarray(_crop(full, bbox))
    picture.thumbnail((max_pixels, max_pixels))
    return picture


@lru_cache(maxsize=1)
def _terrain():
    if not TERRAIN.exists():
        return None
    grids = np.load(TERRAIN)
    return grids["elevation"], grids["water"]


def relief(bbox, max_pixels):
    """Elevation (metres) and a water mask for bbox, south row first, at most max_pixels on the longer side.

    None if the terrain has not been downloaded.
    """
    grids = _terrain()
    if grids is None:
        return None
    elevation, water = (_crop(grid, bbox) for grid in grids)
    scale = min(1, max_pixels / max(elevation.shape))
    size = (max(round(elevation.shape[1] * scale), 2), max(round(elevation.shape[0] * scale), 2))
    elevation = np.asarray(Image.fromarray(elevation.astype(np.float32)).resize(size, Image.BILINEAR))
    water = np.asarray(Image.fromarray(water.astype(np.uint8) * 255).resize(size, Image.BILINEAR)) > 127
    return elevation[::-1], water[::-1]


def month_name(t):
    return t.strftime("%B %Y")


def flags(r):
    """Plain-language data-quality notes for one month."""
    notes = []
    if r.nrt:
        notes.append("provisional near-real-time data")
    if r.partial:
        notes.append("month not finished")
    if r.terra_only:
        notes.append("only one satellite (Terra) was flying")
    elif r.modis_scaled:
        notes.append("scaled from MODIS, good to about a factor of 2")
    if r.outage:
        notes.append("a satellite outage this month")
    if r.modis_ranked:
        notes.append("ranked against MODIS years only")
    return notes


def _hover(t, r):
    lines = [f"<b>{month_name(t)}</b>"]
    if np.isnan(r["index"]):
        lines.append("Not enough data")
    else:
        lines.append(f"Index: {r['index']:,.0f} hotspots per satellite per 30 days")
        if r.uncertain:
            lines.append("Cannot be ranked: too many years tie")
        elif not np.isnan(r.cls):
            record = " (record)" if r.record else ""
            lines.append(f"{CLASSES[int(r.cls)]}{record}: rank {r['rank']:.0f} of {r.n_years:.0f}")
    lines.append(f"Raw hotspots: MODIS {r.count_modis:,.0f}, VIIRS {r.count_viirs:,.0f}")
    return "<br>".join(lines + [f"<i>{n}</i>" for n in flags(r)])


def calendar(c, view, selected, years):
    """Year by month heatmap. view is 'class' or 'index'. Cells can be clicked (customdata = month)."""
    c = c[(c.index.year >= years[0]) & (c.index.year <= years[1])]
    yrs = list(range(years[0], years[1] + 1))
    x, y = c.index.month, c.index.year

    def grid(values):
        return pd.Series(np.asarray(values, dtype=float), index=[y, x]).unstack().reindex(index=yrs, columns=range(1, 13))

    fig = go.Figure()
    if view == "class":
        z = grid(np.where(c.uncertain, 5, c.cls))
        colors = CLASS_COLORS + [UNRANKED]
        scale = [[b, col] for i, col in enumerate(colors) for b in (i / 6, (i + 1) / 6)]
        fig.add_heatmap(z=z, x=list(range(1, 13)), y=yrs, colorscale=scale, zmin=-0.5, zmax=5.5,
                        showscale=False, xgap=2, ygap=2, hoverinfo="skip")
        for name, col in zip(CLASSES + ["Cannot be ranked"], colors):
            fig.add_scatter(x=[None], y=[None], mode="markers", name=name, marker=dict(symbol="square", size=12, color=col))
        s = c[c.record]
        fig.add_scatter(x=s.index.month, y=s.index.year, mode="markers", name="Record for that month", hoverinfo="skip",
                        marker=dict(symbol="star", size=11, color="white", line=dict(color=INK, width=1)))
    else:
        ticks = [0, 10, 100, 1000, 10000]
        fig.add_heatmap(z=np.log10(grid(c["index"]) + 1), x=list(range(1, 13)), y=yrs, zmin=0, zmax=np.log10(60001),
                        colorscale=[[i / 6, col] for i, col in enumerate(BLUES)], xgap=2, ygap=2, hoverinfo="skip",
                        colorbar=dict(title="Index", tickvals=np.log10(np.array(ticks) + 1),
                                      ticktext=[f"{t:,}" for t in ticks], len=0.5, thickness=12))
    s = c[c.nrt]
    fig.add_scatter(x=s.index.month - 0.3, y=s.index.year - 0.28, mode="markers", name="Provisional data", hoverinfo="skip",
                    marker=dict(symbol="circle", size=6, color="white", line=dict(color=INK, width=1)))
    if years[0] <= SPLICE.year <= years[1]:
        fig.add_scatter(x=[0.5, 1.5, 1.5, 12.5], y=[SPLICE.year + 0.5, SPLICE.year + 0.5, SPLICE.year - 0.5, SPLICE.year - 0.5],
                        mode="lines", name="Above this line: scaled from MODIS", hoverinfo="skip",
                        line=dict(color=INK, width=1.5, dash="dot"))
    # Invisible markers on every cell carry the hover text and make the cell clickable.
    fig.add_scatter(x=x, y=y, mode="markers", customdata=c.index.astype(str), showlegend=False,
                    hovertext=[_hover(t, r) for t, r in c.iterrows()], hoverinfo="text",
                    marker=dict(size=20, opacity=0), selected=dict(marker=dict(opacity=0)),
                    unselected=dict(marker=dict(opacity=0)))
    if selected in c.index:
        fig.add_shape(type="rect", x0=selected.month - 0.5, x1=selected.month + 0.5, y0=selected.year - 0.5,
                      y1=selected.year + 0.5, line=dict(color=INK, width=3))
    fig.update_xaxes(tickvals=list(range(1, 13)), ticktext=MONTHS, side="top", range=[0.5, 12.5], showgrid=False,
                     fixedrange=True)
    fig.update_yaxes(dtick=1, range=[years[1] + 0.5, years[0] - 0.5], showgrid=False, fixedrange=True)
    fig.update_layout(height=24 * len(yrs) + 150, margin=dict(l=10, r=10, t=30, b=10), dragmode=False,
                      clickmode="event+select", legend=dict(orientation="h", y=-0.02, yanchor="top"))
    return fig


def month_history(c, t):
    """The selected calendar month in every year, against its usual range. Log scale, so +1."""
    s = c[(c.index.month == t.month) & c["index"].notna()]
    r = c.loc[t]
    fig = go.Figure()
    if not np.isnan(r.typical):
        fig.add_hrect(y0=r.low + 1, y1=r.high + 1, fillcolor=MUTED, opacity=0.18, line_width=0)
        fig.add_hline(y=r.typical + 1, line=dict(color=MUTED, width=2, dash="dash"))
        fig.add_scatter(x=[None], y=[None], mode="lines", name="Typical (median)", line=dict(color=MUTED, width=2, dash="dash"))
        fig.add_scatter(x=[None], y=[None], mode="markers", name="Middle 80% of other years",
                        marker=dict(symbol="square", size=12, color=MUTED, opacity=0.3))
    for name, part, symbol in [("Scaled from MODIS", s[s.modis_scaled], "circle-open"), ("From VIIRS", s[~s.modis_scaled], "circle")]:
        fig.add_scatter(x=part.index.year, y=part["index"] + 1, mode="markers", name=name,
                        marker=dict(symbol=symbol, size=9, color=MUTED, line=dict(width=2, color=MUTED)),
                        customdata=part["index"], hovertemplate="%{x}: %{customdata:,.0f}<extra></extra>")
    fig.add_scatter(x=[t.year], y=[r["index"] + 1], mode="markers+text", name=str(t.year), text=[str(t.year)],
                    textposition="top center", showlegend=False,
                    marker=dict(size=13, color=VIIRS_COLOR, line=dict(width=2, color="white")),
                    hovertemplate=f"{t.year}: {r['index']:,.0f}<extra></extra>")
    top = np.log10(max(s["index"].max(), r.high if not np.isnan(r.high) else 0) + 1)
    fig.update_yaxes(type="log", title="Index + 1 (log scale)", dtick=1, tickformat=",", range=[-0.1, top + 0.45])
    fig.update_xaxes(dtick=2)
    fig.update_layout(height=340, margin=dict(l=10, r=10, t=40, b=10), title=f"Every {t.strftime('%B')} on record",
                      legend=dict(orientation="h", y=-0.12, yanchor="top"))
    return fig


def season(d, k, year):
    """Cumulative index through the year: the chosen year against the other years."""
    v = daily_index(d, k).fillna(0)
    leap_shift = (v.index.is_leap_year & (v.index.dayofyear > 59)).astype(int)  # fold 29 Feb into 28 Feb
    cum = pd.DataFrame({"year": v.index.year, "doy": v.index.dayofyear - leap_shift, "v": v.values}) \
        .groupby(["doy", "year"]).v.sum().unstack().cumsum()
    base = cum[[y for y in range(BASE_YEARS[0], BASE_YEARS[1] + 1) if y != year]]
    days = pd.date_range("2025-01-01", "2025-12-31")  # any non-leap year, for month ticks
    fig = go.Figure()
    fig.add_scatter(x=days, y=base.quantile(0.9, axis=1), mode="lines", line=dict(width=0), showlegend=False, hoverinfo="skip")
    fig.add_scatter(x=days, y=base.quantile(0.1, axis=1), mode="lines", line=dict(width=0), fill="tonexty",
                    fillcolor="rgba(138,137,132,0.25)", name="Middle 80% of other years", hoverinfo="skip")
    fig.add_scatter(x=days, y=base.median(axis=1), mode="lines", name="Typical year (median)",
                    line=dict(color=MUTED, width=2, dash="dash"), hovertemplate="%{x|%d %b}: %{y:,.0f}<extra>typical</extra>")
    top = base.iloc[-1].idxmax()
    fig.add_scatter(x=days, y=base[top], mode="lines", name=f"{top} (highest other year)", line=dict(color=INK, width=1),
                    hovertemplate="%{x|%d %b}: %{y:,.0f}<extra>" + str(top) + "</extra>")
    if year in cum:
        last = d.index.max()
        line = cum[year].where(days.dayofyear <= last.dayofyear) if year == last.year else cum[year]
        fig.add_scatter(x=days, y=line, mode="lines", name=str(year), line=dict(color=VIIRS_COLOR, width=3),
                        hovertemplate="%{x|%d %b}: %{y:,.0f}<extra>" + str(year) + "</extra>")
    fig.update_xaxes(tickformat="%b", dtick="M1")
    fig.update_yaxes(title="Hotspots per satellite, added up since 1 January", rangemode="tozero")
    fig.update_layout(height=420, margin=dict(l=10, r=10, t=40, b=10), title=f"How {year} built up, day by day",
                      hovermode="x unified", legend=dict(orientation="h", y=-0.1, yanchor="top"))
    return fig


def daily_bars(d, k, t):
    """Hotspots per satellite on each day of the month. Indicative only: days are not ranked."""
    v = daily_index(d, k).loc[str(t)]
    fig = go.Figure(go.Bar(x=v.index, y=v.values, marker=dict(color=VIIRS_COLOR, cornerradius=3),
                           hovertemplate="%{x|%d %b %Y}: %{y:,.0f}<extra></extra>"))
    fig.update_yaxes(title="Hotspots per satellite", rangemode="tozero")
    fig.update_xaxes(tickformat="%d", dtick=86400000 * 2)
    fig.update_layout(height=300, margin=dict(l=10, r=10, t=40, b=10), title=f"Each day of {month_name(t)}", bargap=0.2)
    return fig


def map_frame(fig, bbox):
    """Lat/lon axes over the area with the cached terrain picture, cities and the area outline. Works offline."""
    fig.add_scatter(x=[v[1] for v in CITIES.values()], y=[v[0] for v in CITIES.values()], mode="markers+text",
                    text=list(CITIES), textposition="top center", showlegend=False, hoverinfo="skip",
                    marker=dict(symbol="diamond", size=7, color=INK), textfont=dict(color=INK, size=11))
    south, west, north, east = bbox
    fig.add_shape(type="rect", x0=west, x1=east, y0=south, y1=north, line=dict(color=INK, width=2, dash="dash"))
    picture = terrain(bbox, 1000)
    if picture is not None:
        jpeg = io.BytesIO()
        picture.save(jpeg, "JPEG", quality=80)
        fig.add_layout_image(source="data:image/jpeg;base64," + base64.b64encode(jpeg.getvalue()).decode(), layer="below",
                             xref="x", yref="y", x=west, y=north, sizex=east - west, sizey=north - south, sizing="stretch")
    fig.update_xaxes(range=[west - 0.1, east + 0.1], title="Longitude", showgrid=False, zeroline=False,
                     constrain="domain")
    fig.update_yaxes(range=[south - 0.1, north + 0.1], title="Latitude", showgrid=False, zeroline=False,
                     constrain="domain", scaleanchor="x", scaleratio=1 / np.cos(np.radians((south + north) / 2)))


def hotspot_map(points, bbox, title):
    """Hotspot locations in the chosen area. Drag a box to zoom in to a smaller one."""
    if len(points) > 20000:
        points = points.sample(20000, random_state=0)
    fig = go.Figure()
    for name, sats, color in [("VIIRS", ~points.sat.isin(MODIS), VIIRS_COLOR), ("MODIS", points.sat.isin(MODIS), MODIS_COLOR)]:
        p = points[sats]
        fig.add_scattergl(x=p.lon, y=p.lat, mode="markers", name=name, marker=dict(size=4, color=color, opacity=0.55),
                          hovertemplate="%{y:.3f}, %{x:.3f}<extra>" + name + "</extra>")
    map_frame(fig, bbox)
    fig.update_layout(height=620, margin=dict(l=10, r=10, t=40, b=10), title=title, dragmode="select",
                      legend=dict(orientation="h", y=-0.08, yanchor="top"))
    return fig


def sensor_check(c, k):
    """Overlap months: the index built from MODIS alone against the one built from VIIRS alone."""
    o = c.loc[OVERLAP[0]:OVERLAP[1]].dropna(subset=["rate_modis", "rate_viirs"])
    x, y = k * o.rate_modis + 1, o.rate_viirs + 1
    lim = [1, max(x.max(), y.max()) * 1.5]
    fig = go.Figure()
    for factor, dash, name in [(1, "solid", "Perfect agreement"), (2, "dot", "Factor of 2"), (0.5, "dot", None)]:
        fig.add_scatter(x=lim, y=[lim[0] * factor, lim[1] * factor], mode="lines", name=name, showlegend=name is not None,
                        line=dict(color=MUTED, width=1.5, dash=dash), hoverinfo="skip")
    fig.add_scatter(x=x, y=y, mode="markers", name="One month", text=o.index.strftime("%b %Y"),
                    marker=dict(size=8, color=VIIRS_COLOR, opacity=0.7, line=dict(width=1, color="white")),
                    hovertemplate="%{text}<br>from MODIS %{x:,.0f}, from VIIRS %{y:,.0f}<extra></extra>")
    fig.update_xaxes(type="log", title="Index from MODIS alone, + 1", range=np.log10(lim), dtick=1, tickformat=",")
    fig.update_yaxes(type="log", title="Index from VIIRS alone, + 1", range=np.log10(lim), dtick=1, tickformat=",")
    fig.update_layout(height=420, margin=dict(l=10, r=10, t=40, b=10), title="Do the two sensors tell the same story?",
                      legend=dict(orientation="h", y=-0.18, yanchor="top"))
    return fig


def adding_satellites(c):
    """Yearly totals: all hotspots added together, against the harmonized index."""
    c = c.loc[str(BASE_YEARS[0]):]
    raw = (c.count_modis + c.count_viirs).groupby(c.index.year).sum()
    index = c["index"].groupby(c.index.year).sum()
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.12,
                        subplot_titles=["Every hotspot from every satellite, added up", "Harmonized index (per satellite)"])
    fig.add_bar(x=raw.index, y=raw.values, marker=dict(color=MUTED, cornerradius=3), row=1, col=1,
                hovertemplate="%{x}: %{y:,.0f} hotspots<extra></extra>")
    fig.add_bar(x=index.index, y=index.values, marker=dict(color=VIIRS_COLOR, cornerradius=3), row=2, col=1,
                hovertemplate="%{x}: %{y:,.0f}<extra></extra>")
    for year, label in [(2012, "1st VIIRS"), (2018, "2nd VIIRS"), (2023, "3rd VIIRS")]:
        fig.add_vline(x=year - 0.5, line=dict(color=INK, width=1, dash="dot"))
        fig.add_annotation(x=year - 0.4, y=1, yref="y domain", text=label, showarrow=False, xanchor="left", yanchor="top")
    fig.update_xaxes(dtick=2)
    fig.update_layout(height=460, margin=dict(l=10, r=10, t=40, b=10), showlegend=False, bargap=0.2)
    return fig
