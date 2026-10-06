from __future__ import annotations

import numpy as np


def wind_components(speed_mps: float, direction_deg: float):
    """Convert meteorological wind speed and direction to U/V components.

    Speed and direction follow the usual meteorological convention, where the
    direction is from where the wind is blowing. The result is a vector aligned
    with the east and north axes.
    """
    direction_rad = np.deg2rad(direction_deg)
    u = -float(speed_mps) * np.sin(direction_rad)
    v = -float(speed_mps) * np.cos(direction_rad)
    return u, v


def wind_speed_and_direction(u_mps: float, v_mps: float):
    """Convert U/V wind components back to speed and meteorological direction."""
    speed = float(np.hypot(u_mps, v_mps))
    direction = float(np.mod(np.degrees(np.arctan2(-u_mps, -v_mps)), 360.0))
    return speed, direction
