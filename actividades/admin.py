from django.contrib import admin

from .models import ActivityM, ActivityMovement, ActivitySanitario

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


class ActivitySanitarioAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'stock', 'cantidad', 'comentario')

    def rodeo(self, obj):
        return obj.stock.rodeo.nombre
    rodeo.short_description = 'Rodeo'
    rodeo.admin_order_field = 'stock__rodeo__nombre'


admin.site.register(ActivityM, ActivityMAdmin)
admin.site.register(ActivityMovement, ActivityMovementAdmin)
admin.site.register(ActivitySanitario, ActivitySanitarioAdmin)