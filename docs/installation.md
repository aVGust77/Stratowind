# Installation

## Python setup

```bash
python -m pip install --upgrade pip
python -m pip install -e .[dev]
```

## Run the CLI

```bash
stratowind --input data/sample_profile.csv --max-wind-speed 10
```

## Run the Streamlit app

```bash
streamlit run apps/streamlit_app.py
```
