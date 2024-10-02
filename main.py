"""Module providing a function generating JSON data for Calendar."""

import os
import json
from utils.pascha import calculate_pascha
from utils.moon_phase import get_moon_phase
from utils.check_date import is_valid_date

# Define the constants
BUILD_PATH = './build/'
PASCHALION = "paschalion"
SUNDAY_LECTIONARY = "sunday-lectionary"
YEAR_START = 1924
YEAR_END = 2100
LANGUAGES = ["en", "el", "ro"]
CALENDAR_STYLES = ["old", "new"]
CALENDAR = "calendar"


def main():
    """Function generating JSON data for Calendar."""

    # Create a folder for each language
    for language in LANGUAGES:
        # Create a folder for each calendar_style
        for calendar_style in CALENDAR_STYLES:
            calendar_style_path = os.path.join(
                BUILD_PATH, language, calendar_style)
            os.makedirs(calendar_style_path, exist_ok=True)

            # Create a folder for the paschalion
            paschalion_path = os.path.join(
                BUILD_PATH, language, calendar_style, PASCHALION)
            os.makedirs(paschalion_path, exist_ok=True)

            # Create a JSON file for the paschalion
            paschalion_filename = f'{YEAR_START}-{YEAR_END - 1}.json'
            paschalion_filepath = os.path.join(
                paschalion_path, paschalion_filename)
            paschalion_data = {
                "language": language,
            }

            for paschalion_year in range(YEAR_START, YEAR_END):
                pascha_date = calculate_pascha(paschalion_year, calendar_style)
                paschalion_data[paschalion_year] = {
                    "pascha": pascha_date,
                }

            with open(paschalion_filepath, 'w', encoding="utf-8") as json_file:
                json.dump(paschalion_data, json_file, indent=4)

            # Create a folder for the sunday_lectionary
            sunday_lectionary_path = os.path.join(
                BUILD_PATH, language, calendar_style, SUNDAY_LECTIONARY)
            os.makedirs(sunday_lectionary_path, exist_ok=True)

            for sunday_lectionary_year in range(YEAR_START, YEAR_END):
                # Create a folder for each year for sunday_lectionary
                sunday_lectionary_year_path = os.path.join(
                    sunday_lectionary_path, str(sunday_lectionary_year))
                os.makedirs(sunday_lectionary_year_path, exist_ok=True)

                for sunday_lectionary_month in range(1, 13):
                    # Create a JSON file for each month for the sunday_lectionary
                    sunday_lectionary_filename = f'{
                        sunday_lectionary_month:02d}.json'
                    sunday_lectionary_filepath = os.path.join(
                        sunday_lectionary_year_path, sunday_lectionary_filename)
                    sunday_lectionary_data = {"language": language}

                    with open(sunday_lectionary_filepath, 'w', encoding="utf-8") as json_file:
                        json.dump(sunday_lectionary_data, json_file, indent=4)

            # Create a folder for the calendar
            calendar_path = os.path.join(
                BUILD_PATH, language, calendar_style, CALENDAR)
            os.makedirs(calendar_path, exist_ok=True)
            for calendar_year in range(YEAR_START, YEAR_END):
                # Create a folder for each year for calendar
                calendar_year_path = os.path.join(
                    calendar_path, str(calendar_year))
                os.makedirs(calendar_year_path, exist_ok=True)

                for calendar_month in range(1, 13):
                    # Create a JSON file for each month for the calendar
                    calendar_filename = f'{calendar_month:02d}.json'
                    calendar_filepath = os.path.join(
                        calendar_year_path, calendar_filename)
                    calendar_data = {
                        "language": language,
                    }

                    for calendar_day in range(1, 32):
                        if is_valid_date(calendar_year, calendar_month, calendar_day):
                            calendar_data[f'{calendar_day:02d}'] = {
                                "moon_phase": get_moon_phase(
                                    calendar_year, calendar_month, calendar_day, calendar_style
                                ),
                            }

                    with open(calendar_filepath, 'w', encoding="utf-8") as json_file:
                        json.dump(calendar_data, json_file, indent=4)


if __name__ == "__main__":
    main()
