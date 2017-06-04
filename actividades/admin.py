from django.contrib import admin

from .models import ActivityM, ActivityMovement, ActivitySanitario

class ActivityMAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'rodeo', 'animal')

    def rodeo(self, obj):
        return obj.animal.rodeo.nombre
    rodeo.short_description = 'Rodeo'
    rodeo.admin_order_field = 'animal__rodeo__nombre'

class ActivityMovementAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'animal', 'rodeo_destino')


class ActivitySanitarioAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'animal', 'comentario')


admin.site.register(ActivityM, ActivityMAdmin)
admin.site.register(ActivityMovement, ActivityMovementAdmin)
admin.site.register(ActivitySanitario, ActivitySanitarioAdmin)