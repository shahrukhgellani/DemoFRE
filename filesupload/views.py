from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm
from django.views.decorators.csrf import ensure_csrf_cookie
from subprocess import run, PIPE
from . import filedata


@ensure_csrf_cookie
def upload_file(request):
    """

    """
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        msg = '<span style="color: green;">' + request.POST.get('catagory') + ' successfully uploaded</span>'

        handle_uploaded_file(request.FILES['file'], request.POST.get('catagory').lower())
        out = filedata.extract_multi(request.FILES['file'].name, request.POST.get('catagory').lower())
        print(out)
        context = {'msg': msg, 'time': 'Extracted Data : ',
                   'outpt': '<span>' + str(out) + '</span>'}

        return render(request, "single.html", context)
    else:
        form = UploadFileForm()
        return render(request, 'single.html', {'form': form})


@ensure_csrf_cookie
def upload_multiple_files(request):
    """

    """
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        files = request.FILES.getlist('files')
        msg = '<span style="color: green;">' + request.POST.get('catagory') + ' successfully uploaded</span>'
        out = ''
        catagory = request.POST.get('catagory')
        for f in files:
            handle_uploaded_file(f, catagory)
            out += filedata.extract_multi(f.name, catagory)
            #Testing

        context = {'msg': msg, 'time': 'Extracted Data : ',
                   'outpt': '<span>' + str(out) + '</span>'}

        return render(request, "multiple.html", context)

    else:
        form = UploadFileForm()
    return render(request, 'multiple.html', {'form': form})


def handle_uploaded_file(f, catagory):
    name = r"C:\Users\Shahrukh\Desktop\djangofilesupload\ML Data\{catagory}\{fname}".format(fname=f.name,
                                                                                            catagory=catagory)
    with open(name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
