import pandas as pd
import plotly.graph_objects as go


def build_figures(df: pd.DataFrame) -> list[go.Figure]:
    return [
        _max_reps_by_load(df),
        _daily_volume(df),
        _weekly_volume_trend(df),
    ]


def _max_reps_by_load(df: pd.DataFrame) -> go.Figure:
    """Graph 1: Max reps per day by exercise × load — tracks strength progress."""
    fig = go.Figure()
    for (exercise, load), group in df.groupby(["exercise", "effective_load"]):
        daily_max = group.groupby("date")["reps"].max().reset_index()
        fig.add_trace(go.Scatter(
            x=daily_max["date"],
            y=daily_max["reps"],
            mode="lines+markers",
            name=f"{exercise} @ {load}kg",
        ))
    fig.update_layout(
        title="Max Reps per Day by Exercise × Load",
        xaxis_title="Date",
        yaxis_title="Max Reps",
    )
    return fig


def _daily_volume(df: pd.DataFrame) -> go.Figure:
    """Graph 2: Daily total volume (Σ effective_load × reps), color-coded by exercise."""
    df = df.copy()
    df["volume"] = df["effective_load"] * df["reps"]
    fig = go.Figure()
    for exercise, group in df.groupby("exercise"):
        daily = group.groupby("date")["volume"].sum().reset_index()
        fig.add_trace(go.Bar(
            x=daily["date"],
            y=daily["volume"],
            name=exercise,
        ))
    fig.update_layout(
        title="Daily Total Volume by Exercise",
        xaxis_title="Date",
        yaxis_title="Volume (kg × reps)",
        barmode="stack",
    )
    return fig


def _weekly_volume_trend(df: pd.DataFrame) -> go.Figure:
    """Graph 3: Volume trend by exercise (weekly aggregation)."""
    df = df.copy()
    df["volume"] = df["effective_load"] * df["reps"]
    df["week"] = df["date"].dt.to_period("W").apply(lambda p: p.start_time)
    fig = go.Figure()
    for exercise, group in df.groupby("exercise"):
        weekly = group.groupby("week")["volume"].sum().reset_index()
        fig.add_trace(go.Scatter(
            x=weekly["week"],
            y=weekly["volume"],
            mode="lines+markers",
            name=exercise,
        ))
    fig.update_layout(
        title="Weekly Volume Trend by Exercise",
        xaxis_title="Week",
        yaxis_title="Volume (kg × reps)",
    )
    return fig
