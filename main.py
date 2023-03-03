import random
import sys
import os
import win32com.client as win32
import datetime
from docxcompose.composer import Composer
from docx import Document as Document

import functions
from functions import concatenate_words, delete_files
from data_load import load_sheets, load_settings, load_congratulations, load_sheet_data
from congratulations_creator import CongratulationsCreator

FILENAME = 'x.xls'
SETTINGS_SHEET_NAME = 'settings'
PEOPLE_SHEET_NAME = 'people'


def load_data(filename):
    sheets = load_sheets(filename)
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

    return settings, people, congratulations


def gen_triads(n, congratulations):
    c = CongratulationsCreator(congratulations)
    for i in range(n):
        yield c.get_triad()


def write_to_word(output_folder, people, triads, res_filename):
    if not os.path.exists(output_folder):
        os.mkdir(output_folder)

    word = win32.gencache.EnsureDispatch('Word.Application')
    time_words_folder = f'{os.getcwd()}\\{output_folder}'
    i = 0
    for name, triad in zip(people, triads):
        congratulation = f'{name}, поздравляю тебя с новым годом, желаю тебе {triad[0].val}, {triad[1].val} и {triad[2].val}'
        doc = word.Documents.Open(f'{os.getcwd()}\\{settings.template_src}')

        try:
            tb = doc.Shapes.AddTextbox(1, settings.text_box_x, settings.text_box_y, settings.text_box_width,
                                       settings.text_box_height)
            tb.TextFrame.TextRange.Text = congratulation
            tb.TextFrame.MarginTop = 0
            tb.TextFrame.MarginLeft = 0
            tb.Fill.Visible = 0
            tb.Line.Visible = 0


            doc.SaveAs2(f'{time_words_folder}\\{i}.docx')
            doc.Close()
        except BaseException as e:
            doc.Close()
            raise Exception(e)
        i += 1
    word.Application.Quit()

    temporary_files = [f'{time_words_folder}\\{i}.docx' for i in range(len(people))]
    ind = functions.get_file_ind(time_words_folder, res_filename)
    concatenate_words(temporary_files, f'{time_words_folder}\\{res_filename}{ind}.docx')
    delete_files(temporary_files)



if __name__ == '__main__':
    settings, people, congratulations = load_data(FILENAME)

    triads = list(gen_triads(len(people), congratulations))

    write_to_word(settings.output_folder, people, triads, 'res')
