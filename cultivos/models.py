from django.db import models

from campos.models import Potrero

class Producto(models.Model):

    nombre = models.CharField(max_length=25)


class Cultivo(models.Model):

    potrero = models.ForeignKey(Potrero)
    superficie = models.IntegerField()
    producto = models.ForeignKey(Producto)
