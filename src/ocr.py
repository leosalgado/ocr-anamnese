import easyocr


def process_anamnese(anamnese):

    reader = easyocr.Reader(["pt"])
    output = reader.readtext(anamnese, detail=0)

    print(output)
