import os
import re

from docx import Document
from docxcompose.composer import Composer


def concatenate_words(files, composed_filename):
    result = Document(files[0])
    result.add_page_break()
    composer = Composer(result)

    for i in range(1, len(files)):
        doc = Document(files[i])

        if i != len(files) - 1:
            doc.add_page_break()

        composer.append(doc)

    composer.save(composed_filename)


def delete_files(files):
    for filename in files:
        if os.path.exists(filename):
            print('0')
            os.remove(filename)


def get_file_ind(path, res_filename):
    max_ind = 0
    for filename in os.listdir(path):
        if re.match(f'{res_filename}\d.docx', filename):
            ind_str = filename.replace(res_filename, '').replace('.docx', '')
            if ind_str.isdigit():
                max_ind = max(max_ind, int(ind_str))
    return max_ind + 1
