"""Module providing a function generating JSON data for Calendar."""


import os
import json

# Define the constants
BUILD_PATH = './build/'
PASCHALION = "paschalion"
SUNDAY_LECTIONARY = "sunday-lectionary"
YEAR_START = 1924
YEAR_END = 2100
LANGUAGES = ["en", "el", "ro"]
CALENDARS = ["old-calendar", "new-calendar"]


def main():
    """Function generating JSON data for Calendar."""

    for language in LANGUAGES:
        # Create a folder for the paschalion
        paschalion_path = os.path.join(BUILD_PATH, language, PASCHALION)
        os.makedirs(paschalion_path, exist_ok=True)

        # Create a JSON file for the paschalion
        paschalion_filename = f'{YEAR_START}-{YEAR_END - 1}.json'
        paschalion_filepath = os.path.join(
            paschalion_path, paschalion_filename)
        paschalion_data = {"language": language}

        with open(paschalion_filepath, 'w', encoding="utf-8") as json_file:
            json.dump(paschalion_data, json_file, indent=4)

        # Create a folder for the sunday_lectionary
        sunday_lectionary_path = os.path.join(
            BUILD_PATH, language, SUNDAY_LECTIONARY)
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

        for calendar in CALENDARS:
            calendar_path = os.path.join(BUILD_PATH, language, calendar)
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
                    calendar_data = {"language": language}

                    with open(calendar_filepath, 'w', encoding="utf-8") as json_file:
                        json.dump(calendar_data, json_file, indent=4)


if __name__ == "__main__":
    main()
