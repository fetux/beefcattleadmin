from django.db import models

from rodeos.models import Rodeo, Animal

class Activity(models.Model):

    fecha = models.DateField()
    animal = models.ForeignKey(Animal)
    comentario = models.CharField(max_length=255)


class ActivityM(Activity):
    class Meta:
        verbose_name = 'Muerte de Animal'
        verbose_name_plural = 'Muerte de Animales'

    def save(self, *args, **kwargs):
        self.animal.fecha_muerte = self.fecha
        self.animal.save()
        super(ActivityM, self).save(*args, **kwargs)

    def __str__(self):
        """Return a string representation of this ActivityM."""
        return '{}'.format(self.animal)


class ActivityMovement(Activity):
    class Meta:
        verbose_name = 'Transferencia de Animal'
        verbose_name_plural = 'Transferencia de Animales'

    rodeo_destino = models.ForeignKey(Rodeo, related_name='rodeo_destino')

    def save(self, *args, **kwargs):
        self.animal.rodeo = self.rodeo_destino
        self.animal.save()
        super(ActivityMovement, self).save(*args, **kwargs)

    def __str__(self):
        """Return a string representation of this ActivityMovement."""
        return '{}'.format(self.animal)


class ActivitySanitario(Activity):
    class Meta:
        verbose_name = 'Registro Sanitario'
        verbose_name_plural = 'Registros Sanitarios'

    def __str__(self):
        """Return a string representation of this ActivitySanitario."""
        return '{}'.format(self.animal)