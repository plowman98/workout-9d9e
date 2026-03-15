# workout

Personal bodyweight training log viewer.
Reads a TSV log file and renders 3 interactive graphs in the browser.

## Setup

```bash
uv sync
```

## Usage

1. Copy `training_logs/log.example.tsv` to `training_logs/log.tsv` and edit it with your data
2. Run:

```bash
uv run python main.py
```

A browser tab opens with all 3 graphs stacked vertically. Scroll down to see each one.

## Data format

`training_logs/log.tsv`:

| date | exercise | body_weight | assist_kg | reps |
|------|----------|-------------|-----------|------|
| 2026-03-01 | dips | 80 | -25 | 5 |

- `effective_load = body_weight + assist_kg`
- Negative `assist_kg` = resistance band assist (reduces load)
- `log.tsv` is gitignored; only `log.example.tsv` is tracked

## Graphs

### 1. Max Reps per Day by Exercise × Load

Tracks how many reps you can do at each load over time.
One line per exercise × load combination (e.g. "dips @ 55kg").

### 2. Daily Total Volume

Stacked bar chart of `effective_load × reps` summed per day, color-coded by exercise.

### 3. Weekly Volume Trend

Line chart of total weekly volume per exercise. Useful for spotting overtraining or progress plateaus.

### Plotly controls

| Action | How |
|--------|-----|
| Scroll to graph 2 / 3 | Scroll down in the browser |
| Zoom in | Click and drag on the graph area |
| Zoom out / reset view | Double-click the graph area |
| Pan | Hold Shift + drag |
| Show/hide a series | Click its name in the legend |
| Isolate one series | Double-click its name in the legend |
| Hover for exact values | Move mouse over data points |
| Save as PNG | Click the camera icon in the top-right toolbar |
