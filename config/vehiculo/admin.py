from django.contrib import admin
from .models import VehiculoModel

admin.site.register(VehiculoModel)

class VehiculoAdmin(admin.ModelAdmin):
    list_display = ('marca', 'modelo', 'categoria', 'precio', 'fecha_creacion')
    search_fields = ('marca', 'modelo', 'serial_carroceria', 'serial_motor')