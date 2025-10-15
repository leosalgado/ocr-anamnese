import os
import numpy as np
from pdf2image import convert_from_path as pdf_to_image

from ocr import process_anamnese
from anamnese_ai import anamnese_ai_analysis
from utils import get_file_path_from_arg, save_pdf


def main():

    anamnese = get_file_path_from_arg()

    ext = os.path.splitext(anamnese)[1].lower()
    ocr_output = []

    if ext == ".pdf":
        pages = pdf_to_image(anamnese)
        for i, page in enumerate(pages):
            print(f"\n--- Página {i+1} ---")
            ocr_output.append(process_anamnese(np.array(page)))
    else:
        ocr_output.append(process_anamnese(anamnese))

    result = anamnese_ai_analysis(ocr_output)

    save_pdf(result, anamnese)


if __name__ == "__main__":
    main()
