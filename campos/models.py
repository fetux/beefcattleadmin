from django.db import models


class Campo(models.Model):

    nombre = models.CharField(max_length=25)

class Potrero(models.Model):

    nombre = models.CharField(max_length=25)
    campo = models.ForeignKey(Campo, on_delete=models.CASCADE)


