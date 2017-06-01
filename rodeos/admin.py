from django.contrib import admin

from nested_inline.admin import NestedStackedInline, NestedModelAdmin

from .models import Rodeo, Stock


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


admin.site.register(Rodeo, RodeoAdmin)
admin.site.register(Stock, StockAdmin)