from django import forms

from .models import Customer
from .choices import *
class DateInput (forms.DateInput):
    input_type = "date"


class CustomerForm(forms.ModelForm):
    cliente = forms.CharField(
        label="Nome",
        error_messages={"max_length": "O nome não pode ter mais de 50 caracteres"}
        )
    # last_name = forms.CharField(
    #     label="Sobrenome",
    #     error_messages={"max_length": "O sobrenome não pode ter mais de 30 caracteres"}
    # )
    email = forms.EmailField(label="E-mail")
    assunto = forms.CharField(
        label="Assunto",
        error_messages={"max_length": "O nome não pode ter mais de 30 caracteres"}
        )
    mensagem = forms.Textarea(
        #label="Mensagem",
        #error_messages={"max_length": "O nome não pode ter mais de 300 caracteres"}
        )
    dia = forms.CharField(
        label="Dia",
        error_messages={"max_length": "O nome não pode ter mais de 2 caracteres"}
        )
    responsavel = forms.CharField(
        label="Responsavel",
        error_messages={"max_length": "O nome não pode ter mais de 30 caracteres"}
        )
    setor = forms.ChoiceField(
        choices=SETORES_CHOICES,
        widget=forms.Select(), required=True

    )
    ativo = forms.CheckboxInput(


    )
    # birth_date = forms.DateField(label="Data de Nascimento", widget=DateInput())
    # area_code = forms.RegexField(
    #     label="DDD",
    #     regex=r"^\+?1?[0-9]{2}$",
    #     error_messages={"invalid" : "Número de DDD inválido"}
    #
    # )
    # phone_number = forms.RegexField(
    #     label="Telefone",
    #     regex=r"^\+?1?[0-9]{8,15}$",
    #     error_messages={"invalid": "Número de Telefone inválido"}
    # )
    # country = forms.CharField(label="País")
    # state = forms.CharField(label="Estado")
    # city = forms.CharField(label="Cidade")


    class Meta:
        model = Customer
        fields = (
            "cliente",
            "email",
            "assunto",
            "mensagem",
            "dia",
            "responsavel",
            "setor",
            "ativo"

        )