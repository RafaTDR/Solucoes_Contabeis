from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .models import File
import datetime
from .xmltoexcel import xmlnfe, xmlcte, xmlnfs
from django.http import HttpResponse
from random import randrange

# Create your views here.


def index(request):

    if request.method == 'POST' and request.FILES['file']:
        files = request.FILES.getlist('file')

        aleatorio = ""
        pathxml = aleatorio

        for file1 in files:

            upload_file = file1

            file = File(file=upload_file)

            file.save()

        xmlnfe(pathxml=FileSystemStorage().path(pathxml))
        excel = str(FileSystemStorage().path(pathxml) + ".xlsx")

        with open(excel, 'rb') as f:
            testname = "teste"
            extension = ".xlsx"
            response = HttpResponse(f.read(), content_type="application/ms-excel")
            response['Content-Disposition'] = 'attachment; filename={}_Report{}'.format(testname, extension)

        return render(request, 'xmltoexcel/conversor.html', {
            'upload_file_path': 'Sucesso', 'excel': excel
        })
    else:
        return render(request, 'xmltoexcel/conversor.html')


def nfe(request):

    if request.method == 'POST' and request.FILES['file']:
        files = request.FILES.getlist('file')

        aleatorio = str(randrange(1000, 9999)) + str(datetime.datetime.now().strftime("%Y_%m_%d-%H_%M_%S"))

        pathxml = aleatorio

        for file1 in files:

            upload_file = file1

            file = File(file=upload_file, pasta=aleatorio)

            file.save()

        xmlnfe(pathxml=FileSystemStorage().path(pathxml))
        excel = str(FileSystemStorage().path(pathxml) + ".xlsx")

        with open(excel, 'rb') as f:
            testname = "NFEXML"
            extension = ".xlsx"
            response = HttpResponse(f.read(), content_type="application/ms-excel")
            response['Content-Disposition'] = 'attachment; filename={}_Report{}'.format(testname, extension)
            return response

    else:
        return render(request, 'xmltoexcel/conversornfe.html')


def cte(request):

    if request.method == 'POST' and request.FILES['file']:
        files = request.FILES.getlist('file')

        aleatorio = str(randrange(1000, 9999)) + str(datetime.datetime.now().strftime("%Y_%m_%d-%H_%M_%S"))
        pathxml = aleatorio

        for file1 in files:

            upload_file = file1

            file = File(file=upload_file, pasta=aleatorio)

            file.save()

        xmlcte(pathxml=FileSystemStorage().path(pathxml))
        excel = str(FileSystemStorage().path(pathxml) + ".xlsx")

        with open(excel, 'rb') as f:
            testname = "CTEXML"
            extension = ".xlsx"
            response = HttpResponse(f.read(), content_type="application/ms-excel")
            response['Content-Disposition'] = 'attachment; filename={}_Report{}'.format(testname, extension)
            return response

    else:
        return render(request, 'xmltoexcel/conversorcte.html')


def nfscxs(request):

    if request.method == 'POST' and request.FILES['file']:
        files = request.FILES.getlist('file')

        aleatorio = str(randrange(1000, 9999)) + str(datetime.datetime.now().strftime("%Y_%m_%d-%H_%M_%S"))
        pathxml = aleatorio

        for file1 in files:

            upload_file = file1

            file = File(file=upload_file, pasta=aleatorio)

            file.save()

        xmlnfs(pathxml=FileSystemStorage().path(pathxml))
        excel = str(FileSystemStorage().path(pathxml) + ".xlsx")

        with open(excel, 'rb') as f:
            testname = "NFSXML"
            extension = ".xlsx"
            response = HttpResponse(f.read(), content_type="application/ms-excel")
            response['Content-Disposition'] = 'attachment; filename={}_Report{}'.format(testname, extension)
            return response

    else:
        return render(request, 'xmltoexcel/conversornfscxs.html')
