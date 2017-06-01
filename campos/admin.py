from django.contrib import admin

from .models import Campo, Potrero

class CampoAdmin(admin.ModelAdmin):
    list_display = ('nombre', )

class PotreroAdmin(admin.ModelAdmin):
    list_display = ('campo', 'nombre')


admin.site.register(Campo, CampoAdmin)
admin.site.register(Potrero, PotreroAdmin)


