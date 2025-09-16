import easyocr

reader = easyocr.Reader(["pt"])
output = reader.readtext("./data/receita.jpg", detail=0)

print(output)
