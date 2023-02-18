import random

from data_load import load_sheets, load_settings, load_congratulations
from congratulations_creator import CongratulationsCreator

FILENAME = 'x.xls'
SETTINGS_SHEET_NAME = 'settings'
PEOPLE_SHEET_NAME = 'people'


if __name__ == '__main__':
    sheets = load_sheets(FILENAME)
    settings = sheets[SETTINGS_SHEET_NAME]
    settings = load_settings(settings)
    print(settings)
    print(sheets)

    congratulations = load_congratulations(filter(lambda sheet: sheet.name != SETTINGS_SHEET_NAME, sheets.values()))
    print(congratulations)

    print('Generated traids:')
    cong_creator = CongratulationsCreator(congratulations)
    for i in range(10):
        print(cong_creator.get_triad())




