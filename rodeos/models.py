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

class Animal(models.Model):
    class Meta:
        verbose_name = 'Animal'
        verbose_name_plural = 'Animales'

    VV = 'VV'
    VE = 'VE'
    VQ = 'Q'
    TR = 'TR'
    TA = 'TA'
    NT = 'NT'
    NO = 'NO'
    TO = 'TO'

    ANIMAL_CHOICES = (
        (VV, 'VACA VIENTRE'),
        (VE, 'VACA ENGORDE'),
        (VQ, 'VAQUILLONA'),
        (TR, 'TERNERO'),
        (TA, 'TERNERA'),
        (NT, 'NOVILLITO'),
        (NO, 'NOVILLO'),
        (TO, 'TORO'),
    )

    nombre = models.CharField(max_length=2, choices=ANIMAL_CHOICES)
    unidad_nutricional = models.IntegerField()
    rodeo = models.ForeignKey(Rodeo)
    fecha_muerte = models.DateField(null=True, blank=True, default=None)

    def _get_animal_name(self):
        for item in self.ANIMAL_CHOICES:
            if item[0] == self.nombre:
                return item[1]
        return ''

    def __str__(self):
        """Return a string representation of this Animal."""
        return '{}'.format( self.rodeo.nombre +"#"+ str(self.id) + " " + self._get_animal_name())
