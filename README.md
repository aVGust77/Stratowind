# StratoWind

StratoWind is an open-source toolkit for analyzing stratospheric wind profiles for HAPS, high-altitude balloons, atmospheric research, and related applications.

## Project status

This project is actively maintained and released as a reusable Python toolkit. It began as practical wind-analysis work for stratospheric flight planning and was packaged into a clean, open-source foundation for broader research and engineering use.

The repository is maintained by aVGust77 and is intended as a practical, extensible starting point for atmospheric profile analysis, mission planning, and scientific workflows.

The project is designed to help engineers and researchers:

- load wind data from NetCDF, GRIB, or similar atmospheric datasets;
- select coordinates and time windows;
- analyze vertical wind structure from roughly 10 km to 30 km altitude;
- compute wind speed, direction, calm layers, and recommended flight altitudes;
- export results to CSV or JSON;
- visualize wind profiles and heatmaps from a lightweight Streamlit interface;
- use the same logic as a Python library in scripts and notebooks.

## Why this project exists

High-altitude platforms and atmospheric missions need reliable understanding of wind conditions across altitude. StratoWind provides a clean open-source foundation for that work, turning raw meteorological data into operational summaries that can be reused in research and engineering workflows.

## Features

- ERA5 / GFS / NetCDF / GRIB-ready input abstraction
- coordinate and date selection
- vertical profile analysis from 10–30 km
- wind vector decomposition into U/V components
- calm layer finder
- altitude recommendation
- heatmap generation
- CSV and JSON export
- simple Streamlit UI
- reusable Python API

## Installation

```bash
python -m pip install --upgrade pip
python -m pip install -e .
```

## Quick start

```bash
stratowind --input data/sample_profile.csv --max-wind-speed 10
```

Or launch the UI:

```bash
streamlit run apps/streamlit_app.py
```

## Example usage

```python
import pandas as pd
from stratowind.core.analysis import find_calm_layers, recommend_altitude
from stratowind.core.dataset import load_profile

profile = load_profile("data/sample_profile.csv")
calm_layers = find_calm_layers(profile, threshold=2.0)
recommendation = recommend_altitude(profile, max_wind_speed=10.0)
print(calm_layers)
print(recommendation)
```

## Project structure

```text
stratowind/
├── stratowind/
│   ├── __init__.py
│   ├── cli.py
│   ├── core/
│   │   ├── analysis.py
│   │   ├── dataset.py
│   │   └── wind.py
│   └── io/
│       └── exporters.py
├── apps/
│   └── streamlit_app.py
├── data/
│   └── sample_profile.csv
├── tests/
│   └── test_core.py
├── pyproject.toml
├── README.md
├── CONTRIBUTING.md
├── CHANGELOG.md
├── LICENSE
└── .github/workflows/ci.yml
```

## Roadmap

- v0.1.0: dataset loading, wind profile analysis, calm layer detection, export functions, Streamlit UI
- v0.2.0: NetCDF/GRIB ingestion, richer plotting, improved recommendation logic
- v0.3.0: climate summaries, altitudinal windows, notebook examples, documentation expansion

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for development setup and contribution rules.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
