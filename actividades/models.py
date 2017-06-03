from django.db import models

from rodeos.models import Stock

class Activity(models.Model):

    stock = models.ForeignKey(Stock)
    fecha = models.DateField()
    comentario = models.CharField(max_length=255)


class ActivityM(Activity):
    class Meta:
        verbose_name = 'Muerte de Animal'
        verbose_name_plural = 'Muerte de Animales'

    cantidad = models.IntegerField()

    def save(self, *args, **kwargs):
        if not self.pk:
            #This code only happens if the objects is
            #not in the database yet. Otherwise it would
            #have pk
            self.stock.cantidad -= self.cantidad
            self.stock.rodeo.cantidad -= self.cantidad
            self.stock.save()
            self.stock.rodeo.save()
        super(ActivityM, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.stock.cantidad += self.cantidad
        self.stock.rodeo.cantidad += self.cantidad
        self.stock.save()
        self.stock.rodeo.save()
        super(ActivityMovement, self).delete(*args, **kwargs)

class ActivityMovement(Activity):
    class Meta:
        verbose_name = 'Transferencia de Animal'
        verbose_name_plural = 'Transferencia de Animales'

    cantidad = models.IntegerField()
    stock_destino = models.ForeignKey(Stock, related_name='stock_destino')

    def save(self, *args, **kwargs):
        if not self.pk:
            #This code only happens if the objects is
            #not in the database yet. Otherwise it would
            #have pk
            self.stock.cantidad -= self.cantidad
            self.stock_destino.cantidad += self.cantidad
            self.stock.save()
            self.stock_destino.save()
        super(ActivityMovement, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.stock.cantidad += self.cantidad
        self.stock_destino.cantidad -= self.cantidad
        self.stock.save()
        self.stock_destino.save()
        super(ActivityMovement, self).delete(*args, **kwargs)


class ActivitySanitario(Activity):
    class Meta:
        verbose_name = 'Registro Sanitario'
        verbose_name_plural = 'Registros Sanitarios'

    cantidad = models.IntegerField()

