import pdfquery
import pandas as pd
import time

import xml.etree.ElementTree as et

pdf = pdfquery.PDFQuery('./pdf_data/file.pdf')
pdf.load()
pdf.tree.write('./pdf_data/pdfXML.xml', pretty_print=True)
root = et.parse('./pdf_data/pdfXML.txt').getroot()
lista = []
for child in root:
    for subchild in child:
        for subsubchild in subchild:
            lista.append(subsubchild.text)

print(lista)
print(list(filter(lambda t: any(a.islower() for a in t), lista)))


