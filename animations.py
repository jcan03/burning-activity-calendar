"""Views of the hotspots through time: a period timeline, a timelapse map and 3D columns that rise and fall.

All of it plays in the browser with no web requests, so it works offline.
"""
import json

import numpy as np
import pandas as pd
import plotly.graph_objects as go

from charts import CITIES, INK, MODIS_COLOR, MUTED, VIIRS_COLOR, map_frame, relief
from harmonize import MODIS, in_box

FIRE = ["#ffd84d", "#ffa63d", "#f26a2e", "#cf2f1f", "#8c1014"]  # low to high activity
# Ground colours by elevation: water, then dry valley floors, forested plateaus and bare summits.
LAND = [[0.0, "#4f86c6"], [0.08, "#4f86c6"], [0.10, "#d9cfa0"], [0.20, "#c8c890"], [0.33, "#9db87a"],
        [0.50, "#6f9b68"], [0.66, "#5a8160"], [0.78, "#8d8b76"], [0.90, "#c9c5b8"], [1.0, "#f5f4f0"]]
LOW, HIGH = 200, 2800  # metres at the first and last land colour
GROUND_PIXELS = 180    # cells along the longer side of the 3D ground; more is sharper but slower to play
RELIEF = 0.04          # the ground's highest point stands this share of the area's width above its lowest
# Corner offsets of a column (four at the base, four at the top) and the 12 triangles that close it.
CORNER_X, CORNER_Y = np.array([-1, 1, 1, -1, -1, 1, 1, -1]), np.array([-1, -1, 1, 1, -1, -1, 1, 1])
FACES = np.array([[0, 2, 1], [0, 3, 2], [4, 5, 6], [4, 6, 7], [0, 1, 5], [0, 5, 4],
                  [1, 2, 6], [1, 6, 5], [2, 3, 7], [2, 7, 6], [3, 0, 4], [3, 4, 7]])


def timeline(index, start, stop):
    """Weekly activity across the whole record, with the chosen period shaded."""
    s = index.fillna(0).resample("W").mean()
    fig = go.Figure(go.Bar(x=s.index, y=s.values, marker=dict(color=MUTED),
                           hovertemplate="Week to %{x|%d %b %Y}: %{y:,.0f} hotspots per satellite a day<extra></extra>"))
    fig.add_vrect(x0=start, x1=stop + pd.Timedelta(days=1), fillcolor=VIIRS_COLOR, opacity=0.25, line_width=0)
    fig.update_xaxes(range=[index.index[0], index.index[-1] + pd.Timedelta(days=1)], fixedrange=True)
    fig.update_yaxes(visible=False, fixedrange=True)
    fig.update_layout(height=110, margin=dict(l=10, r=10, t=5, b=5), bargap=0, dragmode=False)
    return fig


def smooth(grid):
    """Average each cell with its eight neighbours, so stepped elevations become slopes."""
    rows, cols = grid.shape
    padded = np.pad(grid, 1, mode="edge")
    return sum(padded[i:i + rows, j:j + cols] for i in range(3) for j in range(3)) / 9


def steps(day, start, stop, most=125):
    """Cut start..stop into animation frames: runs of days for a short period, calendar months for a long one.

    Returns each day's frame number and the label of every frame.
    """
    days = (stop - start).days + 1
    for n in (1, 2, 3, 7, 14):
        if days <= most * n:
            spans = [(a, min(a + pd.Timedelta(days=n - 1), stop)) for a in (start + pd.Timedelta(days=i * n) for i in range(-(-days // n)))]
            labels = [f"{a:%d %b %Y}" if a == b else f"{a:%d %b} to {b:%d %b %Y}" for a, b in spans]
            return (day - start).dt.days // n, labels
    months = pd.period_range(start, stop, freq="M")
    return (day.dt.year - start.year) * 12 + day.dt.month - start.month, [m.strftime("%B %Y") for m in months]


def timelapse(points, bbox, start, stop, max_dots=1000):
    """Animated map of the area: each step's hotspots in colour over a grey trail of the three steps before.

    Dots are a sample of at most `max_dots` per step; the title counts every hotspot.
    """
    p = in_box(points, bbox)
    p = p[(p.day >= start) & (p.day <= stop)]
    frame_of, labels = steps(p.day, start, stop)
    frame_of, n = frame_of.to_numpy(), len(labels)
    counts = np.bincount(frame_of, minlength=n)
    sample = {}                             # frame -> longitudes, latitudes, is MODIS
    for f, g in p.groupby(frame_of):
        g = g.sample(max_dots, random_state=0) if len(g) > max_dots else g
        sample[f] = g.lon.to_numpy(np.float32).round(3), g.lat.to_numpy(np.float32).round(3), g.sat.isin(MODIS).to_numpy()

    def dots(frames, modis=None):
        """The sampled dots of these frames: every sensor, or only MODIS (True) or VIIRS (False)."""
        parts = [sample[f] for f in frames if f in sample]
        if not parts:
            return dict(x=[], y=[])
        lon, lat, is_modis = (np.concatenate(part) for part in zip(*parts))
        keep = slice(None) if modis is None else is_modis == modis
        return dict(x=lon[keep], y=lat[keep])

    def frame(f):
        title = f"<b>{labels[f]}</b>: {counts[f]:,} hotspot{'' if counts[f] == 1 else 's'}, {counts[:f + 1].sum():,} so far"
        return go.Frame(name=labels[f], traces=[0, 1, 2], layout=dict(title=dict(text=title)),
                        data=[dots(range(max(f - 3, 0), f)), dots([f], False), dots([f], True)])

    fig = go.Figure()
    layers = [("Three steps before", MUTED, 4, 0.4), ("VIIRS", VIIRS_COLOR, 6, 0.85), ("MODIS", MODIS_COLOR, 6, 0.85)]
    for name, color, size, opacity in layers:   # the three traces that every frame redraws
        fig.add_scattergl(mode="markers", showlegend=False, hoverinfo="skip", marker=dict(size=size, color=color, opacity=opacity))
    for name, color, size, opacity in layers:   # legend entries that stay put when a frame has no dots
        fig.add_scatter(x=[None], y=[None], mode="markers", name=name, marker=dict(size=8, color=color))
    fig.frames = [frame(f) for f in range(n)]
    for trace, first in zip(fig.data, fig.frames[0].data):
        trace.x, trace.y = first.x, first.y
    map_frame(fig, bbox)
    # Scattergl only repaints when the whole frame is redrawn. Long runs of frames play faster.
    go_to = dict(frame=dict(duration=150 if n <= 80 else 80, redraw=True), transition=dict(duration=0), mode="immediate")
    fig.update_layout(
        title=fig.frames[0].layout.title, height=700, margin=dict(l=10, r=10, t=50, b=70), dragmode=False,
        legend=dict(orientation="h", y=1.02, x=1, xanchor="right"),
        updatemenus=[dict(type="buttons", direction="left", x=0, y=-0.1, xanchor="left", yanchor="top", showactive=False,
                          buttons=[dict(label="Play", method="animate", args=[None, go_to]),
                                   dict(label="Pause", method="animate", args=[[None], go_to]),
                                   dict(label="Resume", method="animate", args=[None, dict(go_to, fromcurrent=True)])])],
        sliders=[dict(x=0.22, len=0.78, y=-0.1, yanchor="top", currentvalue=dict(visible=False),
                      steps=[dict(label=name.split(" to ")[0] if i % -(-n // 8) == 0 else "", method="animate", args=[[name], go_to])
                             for i, name in enumerate(labels)])])
    return fig


PLAYER = """
<style>body { margin: 0; overflow: hidden; }</style>
<div style="font:14px sans-serif;color:#3b3b38;display:flex;gap:10px;align-items:center;padding:4px 8px">
  <button id="play" style="width:72px;padding:5px;cursor:pointer">Play</button>
  <input id="step" type="range" min="0" max="__LAST__" value="0" style="flex:1">
  <b id="date" style="width:190px;text-align:right"></b>
</div>
__PLOT__
<script>
const D = __DATA__, plot = document.getElementById('plot'), slider = document.getElementById('step');
const date = document.getElementById('date'), button = document.getElementById('play');
const SX = [-1, 1, 1, -1, -1, 1, 1, -1], SY = [-1, -1, 1, 1, -1, -1, 1, 1], LAST = D.dates.length - 1;
let timer = null, next = 0;   // Play starts from the first step
function show(f) {
  slider.value = f; date.textContent = D.dates[f];
  const x = [], y = [], z = [], colour = [], height = new Float32Array(D.x0.length), pairs = D.heights[f];
  for (let i = 0; i < pairs.length; i += 2) height[pairs[i]] = pairs[i + 1];   // only burning squares are listed
  D.x0.forEach((x0, c) => {
    const h = height[c], on = h > 0;   // a square with nothing in it shrinks to a point inside the ground
    const x1 = D.x1[c], y0 = D.y0[c], y1 = D.y1[c];
    for (let v = 0; v < 8; v++) {
      x.push(on ? (SX[v] < 0 ? x0 : x1) : (x0 + x1) / 2); y.push(on ? (SY[v] < 0 ? y0 : y1) : (y0 + y1) / 2);
      z.push(on ? (v > 3 ? D.base[c] + h : D.foot[c]) : 0);   // from the ground at its lowest corner to its top
    }
    for (let t = 0; t < 12; t++) colour.push(h / D.top);
  });
  Plotly.restyle(plot, {x: [x], y: [y], z: [z], intensity: [colour]}, [0]);   // restyle keeps the camera
  if (D.orbit && timer) {
    const a = D.orbit * Math.PI / 180 * (f / LAST - 0.5), r = Math.hypot(D.eye.x, D.eye.y);
    const a0 = Math.atan2(D.eye.x, -D.eye.y);
    Plotly.relayout(plot, {'scene.camera.eye': {x: r * Math.sin(a0 + a), y: -r * Math.cos(a0 + a), z: D.eye.z}});
  }
}
function stop() { clearInterval(timer); timer = null; button.textContent = 'Play'; }
button.onclick = () => {
  if (timer) return stop();
  button.textContent = 'Pause';
  timer = setInterval(() => { show(next); next = next < LAST ? next + 1 : 0; if (next === 0) stop(); }, 90);
};
slider.oninput = () => { stop(); show(+slider.value); next = +slider.value < LAST ? +slider.value + 1 : 0; };
slider.value = D.shown; date.textContent = D.dates[D.shown];
</script>"""


def columns_3d(points, bbox, start, stop, cell_km, add_up=False, orbit=0, max_cells=6000, height=640):
    """3D columns of activity that play through the period: a web page for st.iframe.

    Each frame is one step of the period (see `steps`). A column's height is the square root of its
    square's activity in that step (or of everything so far, with `add_up`), relative to the busiest
    square in any frame. `points` needs the weight column `w` (harmonize.weights), so activity is
    hotspots per satellite in VIIRS units. Squares widen until there are at most `max_cells`.
    Returns (html, busiest square's activity, cell_km, how many times taller than true the ground
    is drawn or None without terrain), or None if there are no hotspots.
    """
    south, west, north, east = bbox
    p = in_box(points, bbox)
    p = p[(p.day >= start) & (p.day <= stop) & (p.w > 0)]
    if p.empty:
        return None
    km_east = 111.2 * np.cos(np.radians((south + north) / 2))
    wide, tall = (east - west) * km_east, (north - south) * 111.2
    frame_of, labels = steps(p.day, start, stop)
    frame_of, n = frame_of.rename("frame"), len(labels)
    while True:
        col = ((p.lon - west) * km_east // cell_km).astype(int).rename("col")
        row = ((p.lat - south) * 111.2 // cell_km).astype(int).rename("row")
        grid = p.w.groupby([row, col, frame_of]).sum().unstack("frame", fill_value=0)
        if len(grid) <= max_cells:
            break
        cell_km *= 2
    grid = grid.reindex(columns=range(n), fill_value=0)
    if add_up:
        grid = grid.cumsum(axis=1)
    top = grid.to_numpy().max()
    tallest = 0.25 * max(wide, tall)                         # km on screen for the busiest square
    heights = (np.sqrt(grid / top) * tallest).round(2).to_numpy()
    # Each column's footprint: its square, cut off at the area's edge, less a sliver so neighbours stay apart.
    def edges(name, size):
        """Where the columns start and stop along one side of the area."""
        low = grid.index.get_level_values(name).to_numpy() * cell_km
        high = np.minimum(low + cell_km, size)
        low = np.minimum(low, np.maximum(high - 0.2 * cell_km, 0))   # a square cut off by the edge keeps some width
        return low + 0.04 * (high - low), high - 0.04 * (high - low)

    (x0, x1), (y0, y1) = edges("col", wide), edges("row", tall)
    cx, cy = (x0 + x1) / 2, (y0 + y1) / 2

    # The ground: real elevation, stretched so the area's relief is RELIEF of its width. Flat if it is not downloaded.
    land = relief(bbox, GROUND_PIXELS)
    ground, stretch = np.zeros((2, 2)), None
    if land is not None:
        elevation, water = land
        elevation = smooth(smooth(elevation))
        stretch = RELIEF * max(wide, tall) * 1000 / max(np.ptp(elevation), 1)    # times taller than true
        ground = (elevation - elevation.min()) / 1000 * stretch                  # km on screen
    per_km_y, per_km_x = (ground.shape[0] - 1) / tall, (ground.shape[1] - 1) / wide   # ground cells per km

    def ground_at(x, y):
        """Height of the ground (km on screen) at points given in km from the south-west corner."""
        return ground[np.round(np.asarray(y) * per_km_y).astype(int), np.round(np.asarray(x) * per_km_x).astype(int)]

    # A column runs from the lowest ground under it, so it never hangs in the air, to its height above its centre.
    foot = np.array([ground[int(a * per_km_y):int(np.ceil(b * per_km_y)) + 1, int(c * per_km_x):int(np.ceil(d * per_km_x)) + 1].min()
                     for a, b, c, d in zip(y0, y1, x0, x1)])
    base = ground_at(cx, cy)
    # Before Play is pressed, show the busiest step (or the end, when adding up).
    shown = n - 1 if add_up else int(grid.sum(axis=0).to_numpy().argmax())
    first = heights[:, shown]
    on = (first > 0)[:, None]                                # a square with nothing in it shrinks to a point

    def corners(low, high, side):
        return np.where(on, np.where(side < 0, low[:, None], high[:, None]), ((low + high) / 2)[:, None]).ravel()

    faces = (FACES[None] + 8 * np.arange(len(cx))[:, None, None]).reshape(-1, 3)
    fig = go.Figure(go.Mesh3d(
        x=corners(x0, x1, CORNER_X), y=corners(y0, y1, CORNER_Y),
        z=np.where(on, np.where(np.arange(8) > 3, (base + first)[:, None], foot[:, None]), 0).ravel(),
        i=faces[:, 0], j=faces[:, 1], k=faces[:, 2],
        intensity=np.repeat(first / tallest, 12), intensitymode="cell", cmin=0, cmax=1, showscale=False,
        colorscale=[[i / 4, c] for i, c in enumerate(FIRE)], flatshading=True, hoverinfo="skip",
        lighting=dict(ambient=0.6, diffuse=0.8, specular=0.05, roughness=0.9), lightposition=dict(x=-2000, y=-3000, z=6000)))
    bottom = 0
    if land is None:
        fig.add_scatter3d(x=[0, wide, wide, 0, 0], y=[0, 0, tall, tall, 0], z=[0] * 5, mode="lines",
                          line=dict(color=MUTED, width=3), hoverinfo="skip")
    else:
        # The ground is a solid block: an extra ring of cells drops straight down from its edges to a flat bottom.
        bottom = -0.03 * max(wide, tall)
        water[[0, -1]], water[:, [0, -1]] = False, False     # no water on the rim, or it would run down the sides
        tint = np.where(water, 0, 0.1 + 0.9 * np.clip((elevation - LOW) / (HIGH - LOW), 0, 1))
        no_lines = dict(highlight=False)
        fig.add_surface(x=np.r_[0, np.linspace(0, wide, ground.shape[1]), wide], y=np.r_[0, np.linspace(0, tall, ground.shape[0]), tall],
                        z=np.pad(ground, 1, constant_values=bottom).round(2), surfacecolor=np.pad(tint, 1, mode="edge").round(3),
                        cmin=0, cmax=1, colorscale=LAND, showscale=False, hoverinfo="skip",
                        contours=dict(x=no_lines, y=no_lines, z=no_lines), lightposition=dict(x=-3000, y=3000, z=4000),
                        lighting=dict(ambient=0.55, diffuse=0.75, specular=0.03, roughness=0.9, fresnel=0))
    cities = {name: (lat, lon) for name, (lat, lon) in CITIES.items() if south < lat < north and west < lon < east}
    city_x = np.array([(lon - west) * km_east for lat, lon in cities.values()])
    city_y = np.array([(lat - south) * 111.2 for lat, lon in cities.values()])
    fig.add_scatter3d(x=city_x, y=city_y, z=ground_at(city_x, city_y) + 0.02 * tallest,
                      mode="markers+text", text=list(cities), textposition="top center", hoverinfo="skip",
                      marker=dict(size=3, color=INK), textfont=dict(size=12, color=INK))
    eye = dict(x=0.1, y=-1.25, z=0.7)
    ceiling = ground.max() + tallest * 1.05
    fig.update_layout(
        height=height - 46, margin=dict(l=0, r=0, t=0, b=0), showlegend=False,
        scene=dict(aspectmode="manual", aspectratio=dict(x=1, y=tall / wide, z=0.4 * (ceiling - bottom) / (tallest * 1.05)),
                   camera=dict(eye=eye, center=dict(x=0, y=0, z=-0.25)),   # look below the middle: columns sit on the ground
                   xaxis=dict(visible=False, range=[0, wide]), yaxis=dict(visible=False, range=[0, tall]),
                   zaxis=dict(visible=False, range=[bottom, ceiling])))
    # For each frame, only the squares that are burning: [square, height, square, height, ...].
    burning = [[v for c in np.flatnonzero(frame) for v in (int(c), float(frame[c]))] for frame in heights.T]
    data = dict(heights=burning, dates=labels, top=tallest, orbit=orbit, eye=eye, shown=shown,
                **{name: values.round(2).tolist() for name, values in dict(x0=x0, x1=x1, y0=y0, y1=y1, foot=foot, base=base).items()})
    plot = fig.to_html(full_html=False, include_plotlyjs=True, div_id="plot", config={"displayModeBar": False})
    # The plot goes in last: it carries all of plotly.js, which must not be searched for the other markers.
    html = PLAYER.replace("__LAST__", str(n - 1)).replace("__DATA__", json.dumps(data, separators=(",", ":")))
    return html.replace("__PLOT__", plot), top, cell_km, stretch
