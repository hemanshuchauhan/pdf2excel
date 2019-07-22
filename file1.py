from PyPDF2 import PdfFileReader
f = open('samplepdf1.pdf', 'rb')
reader = PdfFileReader(f)
contents = reader.getPage(0).extractText().split('\n')
f.close()