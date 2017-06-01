from django.contrib import admin

from nested_inline.admin import NestedStackedInline, NestedModelAdmin

from .models import Campo, Potrero, Rodeo, Stock, ActivityM, ActivityMovement

class ActivityMAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'rodeo', 'stock', 'cantidad')

    def rodeo(self, obj):
        return obj.stock.rodeo.nombre
    rodeo.short_description = 'Rodeo'
    rodeo.admin_order_field = 'stock__rodeo__nombre'

class ActivityMovementAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'stock', 'stock_destino', 'cantidad')

    def rodeo(self, obj):
        return obj.stock.rodeo.nombre
    rodeo.short_description = 'Rodeo'
    rodeo.admin_order_field = 'stock__rodeo__nombre'


class CampoAdmin(admin.ModelAdmin):
    list_display = ('nombre', )

class PotreroAdmin(admin.ModelAdmin):
    list_display = ('campo', 'nombre')


class StockAdminInline(NestedStackedInline):
        model = Stock
        fields = ['rodeo', 'animal', 'cantidad']
        extra = 0
        min_num = 0

class StockAdmin(admin.ModelAdmin):
    list_display = ('rodeo', 'animal', 'cantidad')


class RodeoAdmin(NestedModelAdmin):
    list_display = ('fecha', 'nombre', 'cantidad')
    inlines = [
        StockAdminInline,
    ]

    def get_ordering(self, request):
        return ['-fecha']



admin.site.register(Campo, CampoAdmin)
admin.site.register(Potrero, PotreroAdmin)
admin.site.register(Rodeo, RodeoAdmin)
admin.site.register(Stock, StockAdmin)
admin.site.register(ActivityM, ActivityMAdmin)
admin.site.register(ActivityMovement, ActivityMovementAdmin)