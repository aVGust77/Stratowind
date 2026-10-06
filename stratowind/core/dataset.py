from __future__ import annotations

import json
from pathlib import Path

import pandas as pd

from .wind import wind_components


def _ensure_vector_columns(df: pd.DataFrame) -> pd.DataFrame:
    result = df.copy()
    if "u_mps" not in result.columns or "v_mps" not in result.columns:
        if "wind_speed_mps" in result.columns and "wind_direction_deg" in result.columns:
            u_values, v_values = zip(
                *(wind_components(row["wind_speed_mps"], row["wind_direction_deg"]) for _, row in result.iterrows())
            )
            result["u_mps"] = u_values
            result["v_mps"] = v_values
        else:
            result["u_mps"] = 0.0
            result["v_mps"] = 0.0
    return result


def load_profile(path):
    """Load a vertical profile from CSV or JSON."""
    file_path = Path(path)
    if not file_path.exists():
        raise FileNotFoundError(f"Profile file not found: {file_path}")

    if file_path.suffix.lower() == ".csv":
        df = pd.read_csv(file_path)
    elif file_path.suffix.lower() == ".json":
        with file_path.open("r", encoding="utf-8") as handle:
            payload = json.load(handle)
        if isinstance(payload, dict) and "data" in payload:
            df = pd.DataFrame(payload["data"])
        else:
            df = pd.DataFrame(payload)
    else:
        raise ValueError(f"Unsupported input format: {file_path.suffix}")

    required = {"altitude_m", "wind_speed_mps"}
    missing = sorted(required - set(df.columns))
    if missing:
        raise ValueError(f"Profile file is missing required columns: {missing}")

    df = _ensure_vector_columns(df)
    return df.sort_values("altitude_m").reset_index(drop=True)


def build_demo_profile():
    """Build a small sample profile for demos and tests."""
    data = {
        "altitude_m": [12000, 15000, 18000, 21000, 24000, 27000],
        "wind_speed_mps": [15.0, 9.0, 7.0, 8.0, 12.0, 18.0],
        "u_mps": [-10.0, -4.0, 2.0, 3.0, 7.0, 11.0],
        "v_mps": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    }
    return pd.DataFrame(data)
