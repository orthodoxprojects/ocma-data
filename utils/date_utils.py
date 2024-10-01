"""
Module providing a function that modify a given date by adding or subtracting a number of days.
"""

from datetime import datetime, timedelta


def modify_date(date_str: str, days: int):
    """Function that modify a given date by adding or subtracting a number of days."""

    date_format = "%Y-%m-%d"
    date = datetime.strptime(date_str, date_format)
    modified_date = date + timedelta(days=days)
    return modified_date.strftime(date_format)
