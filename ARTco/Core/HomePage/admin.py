from django.contrib import admin
from Core.HomePage.models import Visita

class filtroVisita(admin.ModelAdmin):
    # esto para mostrar sólo algunos campos en el Panel de Administración
    list_display = ("fch_visita","ip_visita","ubicacion_visita","dispositivo_visitante","navegador","sistema_operativo") 
    # y para agregar los filtros de busqueda se colocan los campos q se desan hacer búsqueda
    search_fields = ("ip_visita","sistema_operativo","fch_visita")
    # para ver ciertos campos en el Panel de Administración
    fields = ["fch_visita","ip_visita","ubicacion_visita","dispositivo_visitante","navegador","sistema_operativo"]
admin.site.register(Visita, filtroVisita)
#