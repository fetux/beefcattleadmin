from django.contrib import admin

from django.contrib import admin

from nested_inline.admin import NestedStackedInline, NestedModelAdmin

from .models import Producto, Cultivo


class CultivoAdminInline(NestedStackedInline):
        model = Cultivo
        fields = ['producto', 'superficie']
        extra = 0
        min_num = 0

class CultivoAdmin(admin.ModelAdmin):
    list_display = ('producto', 'superficie')


class ProductoAdmin(NestedModelAdmin):
    list_display = ('nombre',)
    inlines = [
        CultivoAdminInline,
    ]

    def get_ordering(self, request):
        return ['-nombre']

    def potrero(self, obj):
        return obj.potrero.nombre
        potrero.short_description = 'Potrero'
        potrero.admin_order_field = 'potrero__nombre'


admin.site.register(Producto, ProductoAdmin)
admin.site.register(Cultivo, CultivoAdmin)
