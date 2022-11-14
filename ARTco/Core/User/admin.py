from django.contrib import admin
from Core.User.models import *

class filtroPerfilUsuario(admin.ModelAdmin):
    # esto para mostrar sólo algunos campos en el Panel de Administración
    list_display = ("nombre","tiene_permisos","fch_creacion","estado","borrado") 
    # y para agregar los filtros de busqueda se colocan los campos q se desan hacer búsqueda
    search_fields = ("nombre","tiene_permisos","estado","borrado")
    # para ver ciertos campos en el Panel de Administración antes de guardar
    fields = ['nombre', 'estado', 'borrado']
admin.site.register(Perfil_Usuario,filtroPerfilUsuario)

class filtroPantalla(admin.ModelAdmin):
    # esto para mostrar sólo algunos campos en el Panel de Administración
    list_display = ("nombre_pantalla","usuario_creacion","estado") 
    # y para agregar los filtros de busqueda se colocan los campos q se desan hacer búsqueda
    search_fields = ("nombre_pantalla","usuario_creacion","estado")
    # para ver ciertos campos en el Panel de Administración
    fields = ['nombre_pantalla', 'estado']
admin.site.register(Pantalla, filtroPantalla)

class filtroPermiso(admin.ModelAdmin):
    # esto para mostrar sólo algunos campos en el Panel de Administración
    list_display = ("nombre_permiso","usuario_creacion","estado") 
    # y para agregar los filtros de busqueda se colocan los campos q se desan hacer búsqueda
    search_fields = ("nombre_permiso","usuario_creacion","estado")
    # para ver ciertos campos en el Panel de Administración
    fields = ['id_rol','id_pantalla','nombre_permiso', 'ver','actualizar','crear','borrar','estado','borrado']
admin.site.register(Permiso, filtroPermiso)

class filtroDepartamentos(admin.ModelAdmin):
    # esto para mostrar sólo algunos campos en el Panel de Administración
    list_display = ("nombre_departamento","usuario_creacion","estado") 
    # y para agregar los filtros de busqueda se colocan los campos q se desan hacer búsqueda
    search_fields = ("nombre_departamento","usuario_creacion","estado")
    # para ver ciertos campos en el Panel de Administración
    fields = ['nombre_departamento', 'estado', 'borrado']
admin.site.register(Departamento,filtroDepartamentos)

class filtroPuesto(admin.ModelAdmin):
    # esto para mostrar sólo algunos campos en el Panel de Administración
    list_display = ("nombre_puesto","usuario_creacion","estado") 
    # y para agregar los filtros de busqueda se colocan los campos q se desan hacer búsqueda
    search_fields = ("nombre_puesto","usuario_creacion","estado")
    # para ver ciertos campos en el Panel de Administración
    fields = ['id_departamento', 'nombre_puesto', 'estado', 'borrado']
admin.site.register(Puesto, filtroPuesto)

# Esta clase se crea para que pueda guardar encriptada la contraseña desde el Pnael de Administración de Django
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'password',
        'email',
        'nombres',
        'apellidos',
        'id_departamento',
        'id_puesto'
    )
    # para ver ciertos campos en el Panel de Administración
    fields = ['nombres', 'apellidos', 'email','fch_ingreso_labores', 'username', 'password', 'id_departamento', 'id_puesto','id_rol','primer_ingreso','cambiar_contrasenia','bloqueado','is_active','is_staff','superusuario','estado','borrado','intentos_fallidos_login']

    def save_model(self, request, obj, form, change):
        if obj.password.startswith('pbkdf2'):
            obj.password=obj.password
        else:
            obj.set_password(obj.password) 
        super().save_model(request, obj, form, change)

admin.site.register(User, UserAdmin)

class filtroPoliticaSeguridad(admin.ModelAdmin):
    # esto para mostrar sólo algunos campos en el Panel de Administración
    list_display = ("nombre_politica","usuario_creacion","estado") 
    # y para agregar los filtros de busqueda se colocan los campos q se desan hacer búsqueda
    search_fields = ("nombre_politica","usuario_creacion","estado")
    # para ver ciertos campos en el Panel de Administración
    fields = ['nombre_politica', 'tiempo_cambio_password','tiempo_inactividad_sesion','tipo_contrasenia', 'estado', 'intentos_fallidos_login']
admin.site.register(Politica_Seguridad, filtroPoliticaSeguridad)


