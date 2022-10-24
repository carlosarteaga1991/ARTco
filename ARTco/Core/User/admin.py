from django.contrib import admin
from Core.User.models import *

admin.site.register(Perfil_Usuario)
#admin.site.register(UsuarioManager)
admin.site.register(Pantalla)
admin.site.register(Permiso)
admin.site.register(Departamento)
admin.site.register(Puesto)

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

    def save_model(self, request, obj, form, change):
        if obj.password.startswith('pbkdf2'):
            obj.password=obj.password
        else:
            obj.set_password(obj.password) 
        super().save_model(request, obj, form, change)

admin.site.register(User, UserAdmin)
admin.site.register(Politica_Seguridad)


