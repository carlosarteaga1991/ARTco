from django.contrib import admin
from Core.Auditoria.models import log

class filtroLog(admin.ModelAdmin):
    # esto para mostrar sólo algunos campos en el Panel de Administración
    list_display = ('ip','fch','ubicacion','dispositivo','navegador','sistemaoperativo','pantalla_afectada','DB_afectada','tabla_afectada','campo_afectado','id_registro_afectado','id_usuario','accion','estado','dato_viejo','dato_nuevo','otra_accion') 
    # y para agregar los filtros de busqueda se colocan los campos q se desan hacer búsqueda
    search_fields = ("ip","fch","accion","tabla_afectada")
    # para ver ciertos campos en el Panel de Administración
    fields = ['ip','fch','ubicacion','dispositivo','navegador','sistemaoperativo','pantalla_afectada','DB_afectada','tabla_afectada','campo_afectado','id_registro_afectado','id_usuario','accion','estado','dato_viejo','dato_nuevo','otra_accion']
admin.site.register(log, filtroLog)




