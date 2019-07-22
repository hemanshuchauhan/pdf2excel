from PyPDF2 import PdfFileWriter, PdfFileReader
output = PdfFileWriter()

ipdf = PdfFileReader(open('samplepdf1.pdf', 'rb'))
watermark = ipdf.getPage(0)
print(watermark)