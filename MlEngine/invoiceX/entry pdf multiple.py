from invoice2data import extract_data
from invoice2data.extract.loader import read_templates
import re
from PyPDF2 import PdfFileReader, PdfFileWriter
import os
import glob

'''
filename = './pdf_input/sample_pg_6.pdf'
templates = read_templates('./templates/')
print(templates)

result = extract_data(filename, templates=templates)
print("\n")
print(result)
'''


# Preprocessing: re-arrange and re-formating the extracted output
'''
date = result['date'].strftime('%d, %b %Y')
total = result['total']
invoice_number = result['invoice_number']
addr_from = result['From_Address']
addr_to = result['To_Address']
'''


# split the pages
def pdf_splitter(path):
    """

    """
    fname = os.path.splitext(os.path.basename(path))[0]
    pdf = PdfFileReader(path)
    for page in range(pdf.getNumPages()):
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(pdf.getPage(page))
        output_filename = './pdf_processing/{}_page_{}.pdf'.format(
            fname, page+1)
        with open(output_filename, 'wb') as out:
            pdf_writer.write(out)
        print('Created: {}'.format(output_filename))
if __name__ == '__main__':
    path = './pdf_input/Popular_PO_in_PDF.pdf'
    pdf_splitter(path)



# extract the info
pages = glob.glob("./pdf_processing/*.pdf")
for page in pages:
    filename = page
    templates = read_templates('./templates/')
    print(page)
    print(templates)

    result = extract_data(filename, templates=templates)
    print("\n")
    print(result)