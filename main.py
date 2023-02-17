import xlrd, xlwt
from dataclasses import dataclass
from settings import load_settings


def load_sheets(filename):
    rb = xlrd.open_workbook(filename, formatting_info=True)

    sheets = dict()
    for sheet in rb.sheets():
        sheets[sheet.name] = sheet

    return sheets


def load_congratulations(congratulations_sheets):
    congratulation_groups = {}
    for sheet in congratulations_sheets:
        congratulation_groups[sheet.name] = []
        for i in range(sheet.nrows):
            for j in range(sheet.ncols):
                congratulation = sheet.cell(rowx=i, colx=j).value
                if congratulation != '':
                    congratulation_groups[sheet.name].append(congratulation)
    return congratulation_groups


if __name__ == '__main__':
    sheets = load_sheets('x.xls')
    settings = sheets['settings']
    rb = xlrd.open_workbook('x.xls')
    settings = load_settings(settings)
    print(settings)
    print(sheets)

    congratulations = load_congratulations(filter(lambda sheet: sheet.name != 'settings', sheets.values()))
    print(congratulations)



