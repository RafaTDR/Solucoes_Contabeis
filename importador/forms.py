from django import forms

from .models import Empresa

class DateInput (forms.DateInput):
    input_type = "date"


class EmpresaForm(forms.ModelForm):
    code = forms.CharField(
        label="Código",
        error_messages={"max_length": "O código não pode ter mais de 50 caracteres"}
        )
    name = forms.CharField(
        label="Nome", error_messages={"max_length": "O nome não pode ter mais de 50 caracteres"}
        )

    cod_banco = forms.CharField(
        label="Código Banco",
        help_text='Código do banco 3 caracteres + conta no arquivo retorno 12 caracteres.',
        error_messages={"max_length": "O código do banco não pode ter mais de 15 caracteres"}
        )

    conta = forms.CharField(
        label="Conta Contábil",
        error_messages={"max_length": "A conta contábil do banco não pode ter mais de 50 caracteres"}
        )
    ativo = forms.CheckboxInput(


    )
    class Meta:
        model = Empresa
        fields = (
            "code",
            "name",
            "cod_banco",
            "conta",
            "ativo"

        )

