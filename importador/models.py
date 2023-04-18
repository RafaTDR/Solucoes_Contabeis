from django.db import models
from django.urls import reverse
from django.utils import timezone
import datetime
from random import randrange

class Empresa(models.Model):
    code = models.CharField(max_length=100,blank=True, null=True)
    name = models.CharField(max_length=250,blank=True, null=True)
    cod_banco = models.CharField(max_length=15)
    conta = models.CharField(max_length=60)

    ativo = models.BooleanField(default=True)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.code + ' - ' + self.name

    def get_full_name(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse("importador:empresa-update", kwargs={"id": self.id})

    def get_delete_url(self):
        return reverse("importador:empresa-delete", kwargs={"id": self.id})

    class Meta:
        db_table = "empresa"

def createdir():
    pasta = str(randrange(1000, 9999)) + str(datetime.datetime.now().strftime("%Y_%m_%d-%H_%M_%S"))
    return pasta


def localsalvar(instance, filename):

    pasta = instance.pasta

    return "{}/{}".format(str(pasta), instance)


class File(models.Model):

    pasta = models.CharField(max_length=30)
    file = models.FileField(upload_to=localsalvar)

    def __str__(self):
        return self.file.name

# Create your models here.
