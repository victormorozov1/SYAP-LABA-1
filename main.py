import random
import sys
import os
import win32com.client as win32
import datetime

from data_load import load_sheets, load_settings, load_congratulations, load_sheet_data
from congratulations_creator import CongratulationsCreator

FILENAME = 'x.xls'
SETTINGS_SHEET_NAME = 'settings'
PEOPLE_SHEET_NAME = 'people'


if __name__ == '__main__':
    sheets = load_sheets(FILENAME)
    print(sheets)

    settings_page = sheets[SETTINGS_SHEET_NAME]
    settings = load_settings(settings_page)
    print(settings)

    people = list(load_sheet_data(sheets[settings.people_page]))
    print(people)

    congratulations = load_congratulations(filter(
        lambda sheet: sheet.name not in [SETTINGS_SHEET_NAME, settings.people_page],
        sheets.values()))
    print(congratulations)

    if not os.path.exists(settings.output_folder):
        os.mkdir(settings.output_folder)

    word = win32.gencache.EnsureDispatch('Word.Application')
    c = CongratulationsCreator(congratulations)
    for name in load_sheet_data(sheets[settings.people_page]):
        triad = c.get_triad()
        congratulation = f'{name}, поздравляю тебя с новым годом, желаю тебе {triad[0].val}, {triad[1].val} и {triad[2].val}'
        doc = word.Documents.Open(f'{os.getcwd()}\\{settings.template_src}')

        try:
            tb = doc.Shapes.AddTextbox(1, settings.text_box_x, settings.text_box_y, settings.text_box_width, settings.text_box_height)
            tb.TextFrame.TextRange.Text = congratulation
            tb.TextFrame.MarginTop = 0
            tb.TextFrame.MarginLeft = 0
            tb.Fill.Visible = 0
            tb.Line.Visible = 0


            doc.SaveAs2(f'{os.getcwd()}\\{settings.output_folder}\\{name}_congratulation ({str(datetime.datetime.now()).replace(".", ",").replace(":", ",")}).docx')
            doc.Close()
        except BaseException as e:
            doc.Close()
            raise Exception(e)
    word.Application.Quit()



    # import docx
    #
    # doc = docx.Document('main.docx')
    # doc.
    # text = []
    # for paragraph in doc.paragraphs:
    #     text.append(paragraph)
    # print('\n'.join(text))






