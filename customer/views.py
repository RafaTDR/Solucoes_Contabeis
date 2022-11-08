from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Customer
from .forms import CustomerForm
from .tables import CustomerTable
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django_tables2.views import SingleTableView
from django_tables2.export.views import ExportMixin

# Create your views here.

class CustomerListView(ListView):
    template_name = "customer/customer_list.html"
    paginate_by = 10
    model = Customer

    def get_queryset(self):
        name = self.request.GET.get("name")
        if name:
            object_list = self.model.objects.filter(
                Q(cliente__icontains=name) | Q(responsavel__icontains=name) | Q(setor__icontains=name)
            ).order_by("cliente")
        else:
            object_list = self.model.objects.all().order_by("cliente")
        return object_list


class CustomerCreateView(CreateView):
    template_name = "customer/customer.html"
    form_class = CustomerForm

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("customer:customer-list")

class CustomerUpdateView(UpdateView):
    template_name = "customer/customer.html"
    form_class = CustomerForm

    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(Customer, id=id)


    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("customer:customer-list")

class CustomerDeleteView(DeleteView):


    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(Customer, id=id)




    def get_success_url(self):
        return reverse("customer:customer-list")

class CustomerList(ExportMixin, SingleTableView):
    model = Customer
    table_class = CustomerTable
    export_name = 'clientes'
    template_name = 'customer/customer_table.html'