import os

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
