"""
Module providing a function that calculate the moon phase for a given date 
using John Conway's algorithm.
"""

from datetime import date, datetime
from utils.date_utils import modify_date


def get_moon_phase(year_str: str, month_str: str, day_str: str, calendar_style: str):
    """Function that calculate the moon phase for a given date using John Conway's algorithm."""

    # date_moon = datetime.strptime(date_str, "%Y-%m-%d")

    year = year_str
    month = month_str
    day = day_str

    if calendar_style == "old":
        date_str = date(year_str, month_str, day_str).isoformat()
        date_old = datetime.strptime(
            modify_date(date_str, 13), "%Y-%m-%d").date()
        year = date_old.year
        month = date_old.month
        day = date_old.day

    # Adjust year and month for dates in January and February
    if month < 3:
        year -= 1
        month += 12

    # Known starting point for moon phase calculation (Jan 1, 2000)
    days_since_known_new_moon = (year % 100) + \
        (month + 1) * 30.6001 + day - 694039.09

    # The length of a lunar cycle is about 29.53 days
    lunar_cycle_length = 29.53058867

    # Calculate the position in the current lunar cycle (a value between 0 and 1)
    moon_cycle_position = (days_since_known_new_moon / lunar_cycle_length) % 1

    # Convert the cycle position to a number of days into the lunar cycle
    days_into_cycle = abs(moon_cycle_position) * lunar_cycle_length

    # Define the moon phases and their index
    moon_phases = [
        (0, "New Moon"),
        (1, "Waxing Crescent"),
        (2, "First Quarter"),
        (3, "Waxing Gibbous"),
        (4, "Full Moon"),
        (5, "Waning Gibbous"),
        (6, "Last Quarter"),
        (7, "Waning Crescent")
    ]

    # Determine the moon phase based on how many days into the cycle we are
    if days_into_cycle < 1.8457:
        return moon_phases[0]
    if days_into_cycle < 5.53699:
        return moon_phases[1]
    if days_into_cycle < 9.22831:
        return moon_phases[2]
    if days_into_cycle < 12.91963:
        return moon_phases[3]
    if days_into_cycle < 16.61096:
        return moon_phases[4]
    if days_into_cycle < 20.30228:
        return moon_phases[5]
    if days_into_cycle < 23.99361:
        return moon_phases[6]
    return moon_phases[7]
