import pandas as pd

from stratowind.core.analysis import find_calm_layers, recommend_altitude
from stratowind.core.wind import wind_components, wind_speed_and_direction


def test_wind_components_and_direction():
    u, v = wind_components(10.0, 90.0)
    assert round(u, 6) == -10.0
    assert round(v, 6) == 0.0

    speed, direction = wind_speed_and_direction(u, v)
    assert round(speed, 6) == 10.0
    assert round(direction, 6) == 90.0


def test_find_calm_layers():
    df = pd.DataFrame(
        {
            "altitude_m": [15000, 18000, 21000],
            "wind_speed_mps": [2.0, 1.5, 3.0],
            "u_mps": [1.0, -0.4, 2.0],
            "v_mps": [0.5, 0.2, -1.5],
        }
    )
    calm = find_calm_layers(df, threshold=2.0)
    assert calm[0]["altitude_m"] == 18000


def test_recommend_altitude_prefers_lowest_safe_layer():
    df = pd.DataFrame(
        {
            "altitude_m": [15000, 18000, 21000, 24000],
            "wind_speed_mps": [15.0, 7.0, 8.0, 12.0],
            "u_mps": [10.0, 3.0, 2.0, 8.0],
            "v_mps": [0.0, 0.0, 0.0, 0.0],
        }
    )
    rec = recommend_altitude(df, max_wind_speed=10.0)
    assert rec["altitude_m"] == 21000
