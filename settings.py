from dataclasses import dataclass
import xlrd, xlwt


@dataclass
class Settings:
    font_style: str = 'Calibri'
    template_src: str = 'template.doc'
    output_folder: str = 'output'

    def __setitem__(self, key, value):
        match key:
            case 'font_style':
                self.font_style = value
            case 'template_src':
                self.template_src = value
            case 'output_folder':
                self.output_folder = value
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


