import os
import sys
import pypandoc


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

    pypandoc.convert_text(
        text,
        "pdf",
        format="md",
        outputfile=pdf_path,
        extra_args=["--standalone", "--pdf-engine=weasyprint"],
    )
