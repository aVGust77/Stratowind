from __future__ import annotations

import pandas as pd
import streamlit as st

from stratowind.core.analysis import find_calm_layers, recommend_altitude
from stratowind.core.dataset import build_demo_profile, load_profile

st.set_page_config(page_title="StratoWind", page_icon="🌬️", layout="wide")

st.title("StratoWind")
st.caption("Open-source stratospheric wind analysis for HAPS and high-altitude platforms.")

uploaded_file = st.file_uploader("Upload a profile CSV or JSON file", type=["csv", "json"])

if uploaded_file is not None:
    with st.spinner("Loading profile..."):
        profile = load_profile(uploaded_file)
else:
    profile = build_demo_profile()

st.subheader("Wind profile")
st.dataframe(profile, use_container_width=True)

threshold = st.slider("Calm layer threshold (m/s)", min_value=0.5, max_value=20.0, value=2.0, step=0.5)
max_wind_speed = st.slider("Maximum wind speed for altitude recommendation (m/s)", min_value=2.0, max_value=40.0, value=10.0, step=1.0)

calm_layers = find_calm_layers(profile, threshold=threshold)
recommendation = recommend_altitude(profile, max_wind_speed=max_wind_speed)

st.subheader("Recommended altitude")
st.json(recommendation)

st.subheader("Calm layers")
if calm_layers:
    st.json(calm_layers)
else:
    st.info("No calm layers found at the selected threshold.")

line_chart = profile[["altitude_m", "wind_speed_mps"]].copy()
line_chart["altitude_km"] = line_chart["altitude_m"] / 1000
st.line_chart(line_chart.set_index("altitude_km")["wind_speed_mps"])
