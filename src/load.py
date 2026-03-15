import pandas as pd
from pathlib import Path

_ROOT = Path(__file__).parent.parent
_LOG = _ROOT / "training_logs" / "log.tsv"
_LOG_EXAMPLE = _ROOT / "training_logs" / "log.example.tsv"


def load_log(path: Path | None = None) -> pd.DataFrame:
    """Load training log TSV and compute effective_load."""
    if path is None:
        path = _LOG if _LOG.exists() else _LOG_EXAMPLE
    df = pd.read_csv(path, sep="\t", parse_dates=["date"])
    df["effective_load"] = df["body_weight"] + df["assist_kg"]
    return df
