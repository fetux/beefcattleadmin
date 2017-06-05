from django.contrib import admin

from nested_inline.admin import NestedStackedInline, NestedModelAdmin

from .models import Rodeo, Animal


class AnimalAdminInline(NestedStackedInline):
        model = Animal
        fields = ['nombre']
        extra = 0
        min_num = 0

class AnimalAdmin(admin.ModelAdmin):
    list_display = ('rodeo', 'nombre', 'unidad_nutricional', 'fecha_muerte')


class RodeoAdmin(NestedModelAdmin):
    list_display = ('nombre', 'cantidad', 'demanda_nutricional', 'get_fecha',)
    inlines = [
        AnimalAdminInline,
    ]

    def cantidad(self, obj):
        return obj.cantidad()
    cantidad.short_description = "Cantidad de Animales"

    def get_fecha(self, obj):
        return obj.fecha
    get_fecha.short_description = "Fecha de creación"

    def get_ordering(self, request):
        return ['-fecha']


admin.site.register(Rodeo, RodeoAdmin)
admin.site.register(Animal, AnimalAdmin)