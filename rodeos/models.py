from django.db import models

from campos.models import Potrero

class Rodeo(models.Model):

    nombre = models.CharField(max_length=25)
    fecha = models.DateTimeField(auto_now_add=True)
    cantidad = models.IntegerField()
    potrero = models.ForeignKey(Potrero, on_delete=models.CASCADE)

    def __str__(self):
        """Return a string representation of this Rodeo."""
        return '{}'.format(self.nombre)

class Stock(models.Model):
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

    animal = models.CharField(max_length=2, choices=ANIMAL_CHOICES)
    cantidad = models.IntegerField()
    rodeo = models.ForeignKey(Rodeo, on_delete=models.CASCADE)

    def _get_animal_name(self):
        for item in self.ANIMAL_CHOICES:
            if item[0] == self.animal:
                return item[1]
        return ''

    def save(self, *args, **kwargs):
        if not self.pk:
            #This code only happens if the objects is
            #not in the database yet. Otherwise it would
            #have pk
            self.rodeo.cantidad += self.cantidad
            self.rodeo.save()
        super(Stock, self).save(*args, **kwargs)

    def __str__(self):
        """Return a string representation of this Stock."""
        return '{}'.format( self.rodeo.nombre + self._get_animal_name() + " " + str(self.cantidad))
