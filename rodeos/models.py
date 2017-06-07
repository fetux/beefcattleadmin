from functools import reduce

from django.db import models

from campos.models import Potrero

class Rodeo(models.Model):

    nombre = models.CharField(max_length=25)
    fecha = models.DateTimeField(auto_now_add=True)
    potrero = models.ForeignKey(Potrero)

    def cantidad(self):
        return self.animal_set.filter(fecha_muerte=None).count()

    def demanda_nutricional(self):
        return reduce(lambda demanda, animal: demanda + animal.unidad_nutricional,
                      self.animal_set.filter(fecha_muerte=None),
                      0)

    def __str__(self):
        """Return a string representation of this Rodeo."""
        return '{}'.format(self.nombre)


class AnimalCategoria(models.Model):
    class Meta:
        verbose_name = 'Categoría de Animal'
        verbose_name_plural = 'Categorías de Animales'

    nombre = models.CharField(max_length=30)
    unidad_nutricional = models.FloatField()

    def __str__(self):
        """Return a string representation of this AnimalCategoria."""
        return '{}'.format(self.nombre)


class Animal(models.Model):
    class Meta:
        verbose_name = 'Animal'
        verbose_name_plural = 'Animales'

    categoria = models.ForeignKey(AnimalCategoria, on_delete=models.CASCADE)
    unidad_nutricional = models.FloatField()
    rodeo = models.ForeignKey(Rodeo)
    fecha_muerte = models.DateField(null=True, blank=True, default=None)


    def __str__(self):
        """Return a string representation of this Animal."""
        return '{}'.format( self.rodeo.nombre +"#"+ str(self.id) + " " + self.categoria.nombre)
