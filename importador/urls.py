from django.urls import path, re_path
from importador import views
from .views import EmpresaCreateView, EmpresaListView, EmpresaUpdateView, EmpresaDeleteView
from django.views.generic import TemplateView


app_name = 'importador'
urlpatterns =[
    path('cobrancacnab240/', views.index_cobra240, name='cobrancacnab240'),
    path('cobrancacnab240/cadastro', EmpresaCreateView.as_view(), name='cadastrar'),
    path("list/", EmpresaListView.as_view(), name="empresa-list"),
    path("<int:id>/", EmpresaUpdateView.as_view(), name="empresa-update"),
    path("<int:id>/delete/", EmpresaDeleteView.as_view(), name="empresa-delete"),

]