from django.db import models
import datetime
from random import randrange

# Create your models here.


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
