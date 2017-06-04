from django.db import models

from campos.models import Potrero

class Producto(models.Model):

    nombre = models.CharField(max_length=25)

    def __str__(self):
        """Return a string representation of this Cultivo."""
        return '{}'.format(self.nombre)


class Cultivo(models.Model):

    potrero = models.ForeignKey(Potrero)
    superficie = models.IntegerField()
    producto = models.ForeignKey(Producto)

    def __str__(self):
        """Return a string representation of this Cultivo."""
        return '{} {} {} {}'.format(self.potrero.campo, self.potrero, str(self.superficie), self.producto)