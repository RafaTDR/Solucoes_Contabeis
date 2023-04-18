from django.shortcuts import render, redirect
from django.http import HttpResponse
from random import randrange
from .forms import EmpresaForm
from .models import Empresa
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import json
from .models import File
import datetime
from django.core.files.storage import FileSystemStorage
from .recebimentos import ret_recbto_febraban240
# Create your views here.

context = {
    'page_title' : 'File Management System',
}

def index_cobra240(request):

    empresas = set(Empresa.objects.values_list('code', 'name'))

    context = {'empresas': empresas}

    if request.method == 'POST' and request.FILES['file']:
        files = request.FILES.getlist('file')

        empresa = request.POST["codigo_empresa"]

        aleatorio = str(randrange(100, 999)) + str(datetime.datetime.now().strftime("%Y_%m_%d-%H_%M_%S"))

        nome = \
            str(empresa).replace("[", "").replace("(", "").replace("]", "").replace(")", "").replace("'", "").split(',')[1]
        pathtxt = aleatorio

        for file1 in files:

            upload_file = file1

            file = File(file=upload_file, pasta=aleatorio)

            file.save()

        ret_recbto_febraban240(empresa, pathtxt=FileSystemStorage().path(pathtxt))
        texto = str(FileSystemStorage().path(pathtxt) + ".txt")

        with open(texto, 'rb') as f:
            testname = str(nome + "_Recebimentos")
            extension = ".txt"
            response = HttpResponse(f.read(), content_type='text/plain')
            response['Content-Disposition'] = 'attachment; filename={}_Report{}'.format(testname, extension)
            return response
    else:
        return render(request, 'importador/importador_cob_febraban240.html', context)

def error_500(request):
    return render(request, 'importador/500_error.html')

def error_404(request, exception=None):
    return render(request, exception, 'importador/404_error.html')

class EmpresaListView(ListView):
    template_name = "importador/empresa_banco_list.html"
    paginate_by = 15
    model = Empresa

    def get_queryset(self):
        name = self.request.GET.get("name")
        if name:
            object_list = self.model.objects.filter(
                Q(code__icontains=name) | Q(name__icontains=name) | Q(cod_banco__icontains=name)
            ).order_by("code")
        else:
            object_list = self.model.objects.all().order_by("code")
        return object_list

class EmpresaCreateView(CreateView):
    template_name = "importador/empresa_banco.html"
    form_class = EmpresaForm

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("importador:empresa-list")



class EmpresaUpdateView(UpdateView):
    template_name = "importador/empresa_banco.html"
    form_class = EmpresaForm

    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(Empresa, id=id)


    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("importador:empresa-list")

class EmpresaDeleteView(DeleteView):


    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(Empresa, id=id)




    def get_success_url(self):
        return reverse("importador:empresa-list")

# Create your views here.

