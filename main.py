import xlrd, xlwt
from dataclasses import dataclass
from settings import load_settings
import win32com.client


def load_sheets(filename):
    rb = xlrd.open_workbook(filename, formatting_info=True)

    sheets = dict()
    for sheet in rb.sheets():
        sheets[sheet.name] = sheet

    return sheets


if __name__ == '__main__':
    sheets = load_sheets('x.xls')
    settings = sheets['settings']
    rb = xlrd.open_workbook('x.xls')
    settings = load_settings(settings)
    print(settings)



