import django_tables2 as tables
from .models import Customer

class CustomerTable(tables.Table):
    export_formats = ['xlsx']  # a list of formats you'll like to export to
    class Meta:
        model = Customer
        fields = ('cliente', 'email', 'assunto', 'mensagem', 'dia', 'responsavel','setor', 'ativo', 'created_date',
                  'updated_date', 'active')