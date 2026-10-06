from __future__ import annotations

import argparse
import json
from pathlib import Path

from .core.analysis import find_calm_layers, recommend_altitude
from .core.dataset import load_profile
from .io.exporters import export_csv, export_json


def main():
    parser = argparse.ArgumentParser(description="Analyze a stratospheric wind profile.")
    parser.add_argument("--input", required=True, help="CSV or JSON profile file.")
    parser.add_argument("--max-wind-speed", type=float, default=10.0, help="Maximum allowed wind speed in m/s.")
    parser.add_argument("--calm-threshold", type=float, default=2.0, help="Threshold used to detect calm layers.")
    parser.add_argument("--output", default=None, help="Optional output prefix for CSV/JSON exports.")
    args = parser.parse_args()

    profile = load_profile(args.input)
    recommendation = recommend_altitude(profile, max_wind_speed=args.max_wind_speed)
    calm_layers = find_calm_layers(profile, threshold=args.calm_threshold)

    summary = {
        "rows": len(profile),
        "recommended_altitude_m": recommendation["altitude_m"],
        "recommended_wind_speed_mps": recommendation["wind_speed_mps"],
        "calm_layers": calm_layers,
    }

    print(json.dumps(summary, ensure_ascii=False, indent=2))

    if args.output:
        prefix = Path(args.output)
        export_csv(profile, prefix.with_suffix(".csv"))
        export_json(summary, prefix.with_suffix(".json"))


if __name__ == "__main__":
    main()
