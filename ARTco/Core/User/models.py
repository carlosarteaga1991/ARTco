from email.policy import default
from secrets import choice
from unittest.util import _MAX_LENGTH
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.forms import model_to_dict

# para implementar slug
import uuid
from django.db.models.signals import pre_save
from datetime import *
import random



class Perfil_Usuario(models.Model):
    id_rol = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre',max_length=100, unique=True)
    tiene_permisos = models.CharField(max_length=2, default='No',choices=[('Si','Si'),('No','No')])
    fch_creacion = models.DateTimeField(auto_now_add=True)
    usuario_creacion = models.IntegerField(blank=True,null=True)
    fch_modificacion = models.DateTimeField(auto_now=True,blank=True,null=True)
    usuario_modificacion = models.IntegerField(blank=True,null=True)
    estado = models.CharField(max_length=1, default='1',choices=[('1','Activo'),('2','Inactivo')])
    borrado = models.CharField(max_length=1, default='0',choices=[('1','Si'),('0','No')])
    slug_perfil_usuario = models.SlugField(max_length=255, blank=True, unique=True)

    def __str__(self):
        return self.nombre
    
    #def toJSON(self): 
    #    item = model_to_dict(self, exclude=['usuario_modificacion'])
    #    return item

    class Meta:
        verbose_name_plural = "Perfil de Usuarios"
        ordering = ['id_rol']
    
    def save(self, *args, **kwargs):
        if not self.slug_perfil_usuario:
            a=str(uuid.uuid4())
            b=str(datetime.now()).replace('-','').replace(':','').replace('.','-').replace(' ','-')
            c=random.choice(["a26", "31b", "98c", "d32", "11e", "f09", "28g"]) + random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ") + str(random.randint(1, 500))
            self.slug_perfil_usuario = random.choice("!&%#|£“¡¬-+}{ñ*-())^~$,_:¿?") + a + '-' + b + '-' + c
        return super().save(*args, **kwargs)

class UsuarioManager(BaseUserManager):
    def create_user(self,email,username,nombres,apellidos,id_departamento,id_puesto,password,**other_fields):
        if not email:
            raise ValueError('El usuario debe tener un correo electrónico')
        
        user = self.model(
            username = username,
            email = self.normalize_email(email),
            nombres = nombres,
            apellidos = apellidos,
            id_departamento = int(id_departamento),
            id_puesto = int(id_puesto),
            **other_fields
        )

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,username,email,nombres,apellidos,id_departamento,id_puesto,password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('superusuario', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'El super usuario debe asignarle a la variable is_staff=True'
            )
        
        if other_fields.get('superusuario') is not True:
            raise ValueError(
                'El super usuario debe asignarle a la variable superusuario=True'
            )

        user = self.create_user(
            email,
            username = username,
            nombres = nombres,
            apellidos = apellidos,
            password = password,
            id_departamento = int(id_departamento),
            id_puesto = int(id_puesto),
            **other_fields
        )
        #user.usuario_administrador = True
        user.save()
        return user

class Pantalla(models.Model):
    id_pantalla = models.AutoField(primary_key=True)
    nombre_pantalla = models.CharField('Pantalla',max_length=100, unique=True)
    fch_creacion = models.DateTimeField(auto_now_add=True)
    usuario_creacion = models.IntegerField(blank=True,null=True)
    fch_modificacion = models.DateTimeField(auto_now=True,blank=True,null=True)
    usuario_modificacion = models.IntegerField(blank=True,null=True)
    estado = models.CharField(max_length=1, default='1',choices=[('1','Activo'),('2','Inactivo')])
    slug_pantalla = models.SlugField(max_length=255, blank=True, unique=True)

    def __str__(self):
        return self.nombre_pantalla
        
    class Meta:
        verbose_name_plural = "Pantallas"
        ordering = ['id_pantalla']

    def save(self, *args, **kwargs):
        if not self.slug_pantalla:
            a=str(uuid.uuid4())
            b=str(datetime.now()).replace('-','').replace(':','').replace('.','-').replace(' ','-')
            c=random.choice(["a26", "31b", "98c", "d32", "11e", "f09", "28g"]) + random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ") + str(random.randint(1, 500))
            self.slug_pantalla = random.choice("!&%#|£“¡¬-+}{ñ*-())^~$,_:¿?") + a + '-' + b + '-' + c
        return super().save(*args, **kwargs)

class Permiso(models.Model):
    id_permiso = models.AutoField(primary_key=True)
    nombre_permiso = models.CharField('Permiso',max_length=100, unique=True)
    id_rol = models.ForeignKey(Perfil_Usuario,on_delete=models.PROTECT,verbose_name="Perfil de Usuario")
    id_pantalla = models.ForeignKey(Pantalla,on_delete=models.PROTECT,verbose_name="Pantalla")
    ver = models.CharField(max_length=1, default='1',choices=[('1','Si'),('0','No')])
    actualizar = models.CharField(max_length=1, default='0',choices=[('1','Si'),('0','No')])
    crear = models.CharField(max_length=1, default='0',choices=[('1','Si'),('0','No')])
    borrar = models.CharField(max_length=1, default='0',choices=[('1','Si'),('0','No')])
    fch_creacion = models.DateTimeField(auto_now_add=True)
    usuario_creacion = models.IntegerField(blank=True,null=True)
    fch_modificacion = models.DateTimeField(auto_now=True,blank=True,null=True)
    usuario_modificacion = models.IntegerField(blank=True,null=True)
    estado = models.CharField(max_length=1, default='1',choices=[('1','Activo'),('2','Inactivo')])
    borrado = models.CharField(max_length=1, default='0',choices=[('1','Si'),('0','No')])
    slug_permiso = models.SlugField(max_length=255, blank=True, unique=True)

    def __str__(self):
        return self.nombre_permiso
    
    #def toJSON(self): 
    #    item = model_to_dict(self, exclude=['usuario_modificacion'])
    #    return item

    class Meta:
        verbose_name_plural = "Permisos"
        ordering = ['id_permiso']
    
    def save(self, *args, **kwargs):
        if not self.slug_permiso:
            a=str(uuid.uuid4())
            b=str(datetime.now()).replace('-','').replace(':','').replace('.','-').replace(' ','-')
            c=random.choice(["a26", "31b", "98c", "d32", "11e", "f09", "28g"]) + random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ") + str(random.randint(1, 500))
            self.slug_permiso = random.choice("!&%#|£“¡¬-+}{ñ*-())^~$,_:¿?") + a + '-' + b + '-' + c
        return super().save(*args, **kwargs)

class Departamento(models.Model):
    id_departamento = models.AutoField(primary_key=True)
    nombre_departamento = models.CharField('Nombre Departamento',max_length=100, unique=True)
    fch_creacion = models.DateTimeField(auto_now_add=True)
    usuario_creacion = models.IntegerField(blank=True,null=True)
    fch_modificacion = models.DateTimeField(auto_now=True,blank=True,null=True)
    usuario_modificacion = models.IntegerField(blank=True,null=True)
    estado = models.CharField(max_length=1, default='1',choices=[('1','Activo'),('2','Inactivo')])
    borrado = models.CharField(max_length=1, default='0',choices=[('1','Si'),('0','No')])
    slug_departamento = models.SlugField(max_length=255, blank=True, unique=True)

    def __str__(self):
        return self.nombre_departamento
    
    def toJSON(self): #función para crear diccionarios que se envían en la vista
        item = model_to_dict(self, exclude=['usuario_modificacion','slug_departamento']) # si deseamos excluir ciertos parámetros usamos  como atributo ,exclude['']
        return item

    class Meta:
        verbose_name_plural = "Departamentos"
        ordering = ['id_departamento']
    
    def save(self, *args, **kwargs):
        if not self.slug_departamento:
            a=str(uuid.uuid4())
            b=str(datetime.now()).replace('-','').replace(':','').replace('.','-').replace(' ','-')
            c=random.choice(["a26", "31b", "98c", "d32", "11e", "f09", "28g"]) + random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ") + str(random.randint(1, 500))
            self.slug_departamento = random.choice("!&%#|£“¡¬-+}{ñ*$-())^~,_:¿?") + a + '-' + b + '-' + c
        return super().save(*args, **kwargs)


class Puesto(models.Model):
    id_puesto = models.AutoField(primary_key=True)
    id_departamento = models.ForeignKey(Departamento, on_delete=models.PROTECT) #protege en caso de querer borrar
    nombre_puesto = models.CharField(max_length=100)
    fch_creacion = models.DateTimeField(auto_now_add=True)
    usuario_creacion = models.IntegerField(blank=True,null=True)
    fch_modificacion = models.DateTimeField(auto_now=True,blank=True,null=True)
    usuario_modificacion = models.IntegerField(blank=True,null=True)
    estado = models.CharField(max_length=1, default='1',choices=[('1','Activo'),('2','Inactivo')])
    borrado = models.CharField(max_length=1, default='0',choices=[('1','Si'),('0','No')])
    slug_puesto = models.SlugField(max_length=255, blank=True, unique=True)

    def __str__(self):
        return self.nombre_puesto
    
    #def toJSON(self): #función para crear diccionarios que se envían en la vista
    #    item = model_to_dict(self, exclude=['usuario_modificacion']) # si deseamos excluir ciertos parámetros usamos  como atributo ,exclude['']
    #   return item

    class Meta:
        verbose_name_plural = "Puestos" #para que no le agrega una ese en el admin panel de django
        ordering = ['id_puesto']

    def save(self, *args, **kwargs):
        if not self.slug_puesto:
            a=str(uuid.uuid4())
            b=str(datetime.now()).replace('-','').replace(':','').replace('.','-').replace(' ','-')
            c=random.choice(["a26", "31b", "98c", "d32", "11e", "f09", "28g"]) + random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ") + str(random.randint(1, 500))
            self.slug_puesto = random.choice("!&%#|£“¡¬-+}{ñ*-())^~$,_:¿?") + a + '-' + b + '-' + c
        return super().save(*args, **kwargs)

class User(AbstractBaseUser):
    username = models.CharField('Usuario',max_length=20, unique=True)
    email = models.EmailField('Correo Electrónico', max_length=70,unique=True)
    nombres = models.CharField('Nombres',max_length=45,blank= True, null = True)
    apellidos = models.CharField('Apellidos',max_length=45,blank= True, null = True)
    #id_departamento = models.ForeignKey(Departamento,on_delete=models.PROTECT,blank=True,verbose_name="Departamento")
    #id_puesto = models.ForeignKey(Puesto,on_delete=models.PROTECT,blank=True,verbose_name="Puesto")
    id_departamento = models.IntegerField(blank=True,verbose_name="Departamento")
    id_puesto = models.IntegerField(blank=True,verbose_name="Puesto")
    ip_ultimo_acceso = models.CharField(max_length=50, blank=True)
    usuario_creacion = models.IntegerField(blank=True,null=True)
    fch_creacion = models.DateTimeField(auto_now_add=True)
    fch_ingreso_labores = models.DateField('Fecha de Ingreso a Laborar',blank= True, null = True)
    fch_modificacion = models.DateTimeField(auto_now=True,blank=True,null=True)
    fch_cambio_password = models.DateTimeField(blank=True,null=True)
    fch_ultimo_cambio_password = models.CharField(max_length=70, blank=True)
    usuario_modificacion = models.IntegerField(blank=True,null=True)
    estado = models.CharField('Estado',max_length=1,blank=True, default='1',choices=[('1','Activo'),('2','Inactivo')])
    borrado = models.CharField(max_length=1, default='0',blank=True,choices=[('1','Si'),('0','No')])
    primer_ingreso = models.IntegerField(default=1,blank=True,null=True)
    cambiar_contrasenia = models.CharField(max_length=1, default='1',blank=True,choices=[('1','Si'),('0','No')])
    bloqueado = models.CharField(max_length=1, default='0',blank=True,choices=[('1','Bloqueado'),('0','Desbloqueado')])
    intentos_fallidos_login = models.IntegerField(default=0,blank=True,null=True)
    autenticacion_doble_factor = models.BooleanField(default=False, null=True, choices=[(False,"No"),(True,"Si")])
    #img_user = models.ImageField('Imagen de Perfil', height_field=None,width_field=None,blank=True, max_length=200)
    #id_rol = models.ForeignKey(Perfil_Usuario,on_delete=models.PROTECT,blank=True,verbose_name="Perfil de Usuario",null=True)
    id_rol = models.IntegerField(blank=True,null=True,verbose_name="Perfil de Usuario")
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    superusuario = models.BooleanField(default = False)
    objects = UsuarioManager()
    token = models.UUIDField(primary_key=False, editable=False, null=True, blank=True)
    slug_usuario = models.SlugField(max_length=255, blank=True, unique=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','nombres','apellidos','id_departamento','id_puesto']

    def __str__(self):
        return self.username
    
    def has_perm(self,perm,obj = None):
        return True
    
    def has_module_perms(self,app_label):
        return True

    class Meta:
        verbose_name_plural = "Usuarios" #para que no le agrega una ese en el admin panel de django
        ordering = ['username']
    
    @property
    def is_superuser(self):
        #return self.usuario_administrador
        return self.is_superuser

    def save(self, *args, **kwargs):
        if not self.slug_usuario:
            a=str(uuid.uuid4())
            b=str(datetime.now()).replace('-','').replace(':','').replace('.','-').replace(' ','-')
            c=random.choice(["a26", "31b", "98c", "d32", "11e", "f09", "28g"]) + random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ") + str(random.randint(1, 500))
            self.slug_usuario = random.choice("!&%#|/£“¡¬-+}{ñ*-())^~`,_:¿'?") + a + '-' + b + '-' + c
        return super().save(*args, **kwargs)

    

class Politica_Seguridad(models.Model):
    id_politica = models.AutoField(primary_key=True)
    nombre_politica = models.CharField(max_length=50, blank=True)
    tiempo_cambio_password = models.IntegerField(default=90,blank=True,null=True, verbose_name="Frecuencia en Días de Cambio de Contraseña")
    tiempo_inactividad_sesion = models.CharField(max_length=1, default='5',
    choices=[('1','5 Minutos'),
            ('2','10 Minutos'),
            ('3','30 Minutos'),
            ('4','1 Hora'),
            ('5','Nunca')])
    tipo_contrasenia = models.CharField(max_length=1, default='5',
    choices=[('1','Mínimo 10 carácteres / contener números, mayúsculas, carácter especial'),
             ('2','Mínimo 8 carácteres / contener números, mayúsculas'),
             ('3','Mínimo 8 carácteres / contener sólo letras'),
             ('4','Mínimo 6 carácteres / contener sólo letras'),
             ('5','Mínimo 4 carácteres ')])
    fch_creacion = models.DateTimeField(auto_now_add=True)
    intentos_fallidos_login = models.IntegerField(default=3,blank=True,null=True)
    permitir_sesion_duplicada = models.BooleanField(default=False,
    choices=[(False,'Si'),
             (True,'No')])
    usuario_creacion = models.IntegerField(blank=True,null=True)
    fch_modificacion = models.DateTimeField(auto_now=True,blank=True,null=True)
    usuario_modificacion = models.IntegerField(blank=True,null=True)
    estado = models.CharField('Estado',max_length=1,blank=True, default='1',choices=[('1','Activo'),('2','Inactivo')])
    slug_politica_seguridad = models.SlugField(max_length=255, blank=True, unique=True)
    
    def __str__(self):
        return self.nombre_politica

    class Meta:
        verbose_name_plural = "Políticas de Seguridad" #para que no le agrega una ese en el admin panel de django
        ordering = ['id_politica']
    
    def save(self, *args, **kwargs):
        if not self.slug_politica_seguridad:
            a=str(uuid.uuid4())
            b=str(datetime.now()).replace('-','').replace(':','').replace('.','-').replace(' ','-')
            c=random.choice(["a26", "31b", "98c", "d32", "11e", "f09", "28g"]) + random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ") + str(random.randint(1, 500))
            self.slug_politica_seguridad = random.choice("!&%#|/£“¡¬-+}{ñ*-())^~`,_:¿'?") + a + '-' + b + '-' + c
        return super().save(*args, **kwargs)
    
    
