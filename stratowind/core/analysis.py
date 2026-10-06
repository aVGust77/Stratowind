from __future__ import annotations

import pandas as pd


def find_calm_layers(df: pd.DataFrame, threshold: float = 2.0, altitude_col: str = "altitude_m", wind_speed_col: str = "wind_speed_mps"):
    """Return altitude layers below a wind-speed threshold."""
    if df.empty:
        return []

    subset = df[[altitude_col, wind_speed_col]].copy()
    subset = subset.dropna().copy()
    if "u_mps" in df.columns:
        subset["u_mps"] = df["u_mps"].reindex(subset.index).fillna(0.0)
    if "v_mps" in df.columns:
        subset["v_mps"] = df["v_mps"].reindex(subset.index).fillna(0.0)

    calm = subset[subset[wind_speed_col] <= threshold].sort_values(by=[wind_speed_col, altitude_col], ascending=[True, True])
    return [
        {
            "altitude_m": float(row[altitude_col]),
            "wind_speed_mps": float(row[wind_speed_col]),
            "u_mps": float(row.get("u_mps", 0.0)),
            "v_mps": float(row.get("v_mps", 0.0)),
        }
        for _, row in calm.iterrows()
    ]


def recommend_altitude(df: pd.DataFrame, max_wind_speed: float = 10.0, altitude_col: str = "altitude_m", wind_speed_col: str = "wind_speed_mps"):
    """Pick the highest altitude that remains under the maximum allowed wind speed."""
    if df.empty:
        return {"altitude_m": None, "wind_speed_mps": None, "status": "empty"}

    safe = df[df[wind_speed_col] <= max_wind_speed].copy()
    if safe.empty:
        worst = df.sort_values(by=wind_speed_col, ascending=False).iloc[0]
        return {
            "altitude_m": float(worst[altitude_col]),
            "wind_speed_mps": float(worst[wind_speed_col]),
            "status": "no_safe_layer",
        }

    selected = safe.sort_values(by=altitude_col, ascending=False).iloc[0]
    return {
        "altitude_m": float(selected[altitude_col]),
        "wind_speed_mps": float(selected[wind_speed_col]),
        "status": "safe",
    }
