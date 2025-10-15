import os
import sys
from fpdf import FPDF


def get_file_path_from_arg():
    if len(sys.argv) != 2:
        print(f'usage: {sys.argv[0]} "path_to_anamnese"', file=sys.stderr)
        sys.exit(1)

    file = sys.argv[1]

    if not os.path.isfile(file):
        print(f'error: file not found: "{file}"', file=sys.stderr)
        sys.exit(1)
    return file


def save_pdf(text, file):

    dir_path = os.path.dirname(file)
    pdf_path = os.path.join(dir_path, "relatorio.pdf")

    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)

    for line in text.split("\n"):
        pdf.multi_cell(0, 10, line)

    pdf.output(pdf_path)

    return pdf_path
