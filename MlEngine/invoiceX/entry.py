from invoice2data import extract_data
from invoice2data.extract.loader import read_templates
import sys




filename = 'C://Users//Shahrukh//Desktop//document_ai//invoiceX//pdf_input//sample_pg_6.pdf'
#filename = sys.argv[1]
templates = read_templates('C://Users//Shahrukh//Desktop//document_ai//invoiceX//templates')
print(templates)

result = extract_data(filename, templates=templates)
#print("\n")
print(result)
#print("Working inside the jojo code")


# Preprocessing: re-arrange and re-formating the extracted output
'''
date = result['date'].strftime('%d, %b %Y')
total = result['total']
invoice_number = result['invoice_number']
addr_from = result['From_Address']
addr_to = result['To_Address']
'''

