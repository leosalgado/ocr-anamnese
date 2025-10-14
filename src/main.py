import sys
import os
import numpy as np
from pdf2image import convert_from_path as pdf_to_image
from ocr import process_anamnese


def get_file_path_from_arg():
    if len(sys.argv) != 2:
        print(f'usage: {sys.argv[0]} "path_to_anamnese"', file=sys.stderr)
        sys.exit(1)

    file = sys.argv[1]

    if not os.path.isfile(file):
        print(f'error: file not found: "{file}"', file=sys.stderr)
        sys.exit(1)
    return file


def main():

    anamnese = get_file_path_from_arg()

    ext = os.path.splitext(anamnese)[1].lower()

    if ext == ".pdf":
        pages = pdf_to_image(anamnese)
        for i, page in enumerate(pages):
            print(f"\n--- Página {i+1} ---")
            process_anamnese(np.array(page))
    else:
        process_anamnese(anamnese)


if __name__ == "__main__":
    main()
