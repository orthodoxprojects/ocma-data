"""Module providing a function that checks if the provided date string is a valid date."""

from datetime import date


def is_valid_date(year_str: str, month_str: str, day_str: str):
    """Function that checks if the provided date string is a valid date."""

    try:
        date(year_str, month_str, day_str)
        return True
    except ValueError:
        return False
