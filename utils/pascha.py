"""
Module providing a function that calculate the date of Pascha
for the given year using the Jacques Oudin Algorithm.
"""

from datetime import date


def calculate_pascha(year: int):
    """
    Function that calculate the date of Pascha
    for the given year using the Jacques Oudin Algorithm.
    """

    golden_number = year % 19
    epact = (19 * golden_number + 15) % 30
    century_offset = (year + year // 4 + epact) % 7
    paschal_full_moon = epact - century_offset
    easter_month = 3 + (paschal_full_moon + 40) // 44
    easter_day = paschal_full_moon + 28 - 31 * (easter_month // 4)

    julian_pascha_date = date(year, easter_month, easter_day)
    return julian_pascha_date.isoformat()
