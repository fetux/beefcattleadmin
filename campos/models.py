from django.db import models


class Campo(models.Model):

    nombre = models.CharField(max_length=25)

    def __str__(self):
        """Return a string representation of this Campo."""
        return '{}'.format(self.nombre)


class Potrero(models.Model):

    nombre = models.CharField(max_length=25)
    campo = models.ForeignKey(Campo, on_delete=models.CASCADE)

    def __str__(self):
        """Return a string representation of this Potrero."""
        return '{}'.format(self.nombre)


