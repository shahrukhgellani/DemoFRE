from invoice2data import extract_data
from invoice2data.extract.loader import read_templates
import glob
from PyPDF2 import PdfFileReader, PdfFileWriter
import os
import shutil


def extract(name):
    templates = read_templates(r'C:\Users\Shahrukh\Desktop\djangofilesupload\MlEngine\invoiceX\templates')
    result = extract_data(name, templates=templates)
    return result


def pdf_splitter(file_refrence, catagory):
    """

    """
    fname = os.path.splitext(os.path.basename(file_refrence))[0]
    pdf = PdfFileReader(
        r"C:\Users\Shahrukh\Desktop\djangofilesupload\ML Data\{catagory}\{file}".format(file=file_refrence,
                                                                                        catagory=catagory))
    print("Check")
    for page in range(pdf.getNumPages()):
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(pdf.getPage(page))
        output_filename = r'C:\Users\Shahrukh\Desktop\djangofilesupload\filesupload\pdf_processing/{}_page_{}.pdf'.format(
            fname, page + 1)
        with open(output_filename, 'wb+') as out:
            pdf_writer.write(out)


def extract_multi(file_refrence, catagory):
    pdf_splitter(file_refrence, catagory)

    pages = glob.glob(r"C:\Users\Shahrukh\Desktop\djangofilesupload\filesupload\pdf_processing\{}".format("*.pdf"))
    print(pages)
    result = ''
    templates = read_templates(r'C:\Users\Shahrukh\Desktop\djangofilesupload\MlEngine\invoiceX\templates')
    for page in pages:
        # path = r"C:\Users\Shahrukh\Desktop\djangofilesupload\filesupload\pdf_processing\{pdf}".format(pdf=page)
        result += to_table(extract_data(page, templates=templates), page)
    remove_file()
    return result


def remove_file():
    folder = r'C:\Users\Shahrukh\Desktop\djangofilesupload\filesupload\pdf_processing'
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))


def to_table(extracted, file):
    table = '<tr><th>File Name</th><th>{f}</th></tr>'.format(f=file.split('\\')[-1])
    item = ''
    i = 1
    for key in extracted.keys():
        if key.endswith('net'):
            table += '<tr><td>Item {i}</td><td>{info}</td></tr>'.format(info=item, i=i)
            i += 1
            item = ''
        elif key.startswith('item'):
            item += '{Lable}: {data}<br/>'.format(Lable=key.split('_')[-1],
                                             data=extracted.get(key) if extracted.get(key) != "" else 0)
        else:
            table += '<tr><td>{lable}</td><td>{info}</td></tr>'.format(lable=key, info=extracted.get(key))
    return '<table>{table}</table><br/><hr/>'.format(table=table)
