from dataclasses import dataclass
import xlrd


@dataclass
class Settings:
    font_style: str = 'Calibri'
    template_src: str = 'template.doc'
    output_folder: str = 'output'
    people_page: str = 'people'
    res_filename: str = 'res'

    text_box_x: int = 10
    text_box_y: int = 10
    text_box_height: int = 100
    text_box_width: int = 100

    def __setitem__(self, key, value):
        match key:
            case 'font_style':
                self.font_style = value
            case 'template_src':
                self.template_src = value
            case 'output_folder':
                self.output_folder = value
            case 'people_page':
                self.people_page = value
            case 'text_box_x':
                self.text_box_x = value
            case 'text_box_y':
                self.text_box_y = value
            case 'text_box_width':
                self.text_box_width = value
            case 'text_box_height':
                self.text_box_height = value
            case 'res_filename':
                self.res_filename = value
            case _:
                raise Exception(f'Field {key} not found')


def load_settings(sheet: xlrd.sheet.Sheet):
    settings = Settings()
    for i in range(0, sheet.nrows):
        setting_name = sheet.cell(rowx=i, colx=0).value
        if setting_name != '':
            setting_val = sheet.cell(rowx=i, colx=1).value
            settings[setting_name] = setting_val
    return settings


def load_sheets(filename):
    rb = xlrd.open_workbook(filename, formatting_info=True)

    sheets = dict()
    for sheet in rb.sheets():
        sheets[sheet.name] = sheet

    return sheets


def load_sheet_data(sheet):
    for i in range(sheet.nrows):
        for j in range(sheet.ncols):
            congratulation = sheet.cell(rowx=i, colx=j).value
            if congratulation != '':
                yield congratulation


def load_congratulations(congratulations_sheets):
    congratulation_groups = {}
    for sheet in congratulations_sheets:
        congratulation_groups[sheet.name] = list(load_sheet_data(sheet))

    return congratulation_groups
