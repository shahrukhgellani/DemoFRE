from invoice2data import extract_data
from invoice2data.extract.loader import read_templates

def extract(name):
    templates = read_templates(r'C:\Users\Shahrukh\Desktop\djangofilesupload\MlEngine\invoiceX\templates')
    result = extract_data(name, templates=templates)
    return result