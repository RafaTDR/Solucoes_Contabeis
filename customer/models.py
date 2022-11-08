from django.db import models
from django.urls import reverse
from .choices import *
# Create your models here.



class Customer(models.Model):

    cliente = models.CharField(max_length=50)
    email = models.EmailField()
    assunto = models.CharField(max_length=30)
    mensagem = models.TextField(max_length=2000)
    dia = models.CharField(max_length=2)
    responsavel = models.CharField(max_length=30)
    setor = models.PositiveSmallIntegerField(choices=SETORES_CHOICES, default=2)
    ativo = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)


    def __str__(self):
        return f"{self.cliente} {self.email}"

    # def get_full_phone_number(self):
    #     return f"({self.area_code}) {self.phone_number} "

    def get_full_name(self):
        return f"{self.cliente}"

    # def get_full_city(self):
    #     return f"{self.city} - {self.state}"

    def get_absolute_url(self):
        return reverse("customer:customer-update", kwargs={"id": self.id})

    def get_delete_url(self):
        return reverse("customer:customer-delete", kwargs={"id": self.id})

    class Meta:
        db_table = "customer"