from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save
from datetime import *
import uuid
import random

class log(models.Model):
    id = models.AutoField(primary_key=True)
    fch = models.DateTimeField(auto_now_add=True)
    ip = models.CharField(max_length=255, blank=True, null=True)
    ubicacion = models.CharField(max_length=255, blank=True, null=True)
    dispositivo = models.CharField(max_length=255, blank=True, null=True)
    navegador = models.CharField(max_length=255, blank=True, null=True)
    sistemaoperativo = models.CharField(max_length=255, blank=True, null=True)
    pantalla_afectada = models.CharField(max_length=255, blank=True, null=True)
    DB_afectada = models.CharField(max_length=255, blank=True, null=True)
    tabla_afectada = models.CharField(max_length=255, blank=True, null=True)
    campo_afectado = models.CharField(max_length=255, blank=True, null=True)
    id_registro_afectado = models.IntegerField(blank=True,null=True)
    id_usuario = models.IntegerField(blank=True,null=True)
    accion = models.CharField('Tipo de Acción', max_length=255, blank=True, null=True)
    # Insertar, Modificar, Ver, Borrar, Envío de Correo, Inicio de Sesión, Restablecer Contraseña
    estado = models.CharField(max_length=255, blank=True, null=True) 
    # Exitodo, Fallido, Usuario Bloqueado
    dato_viejo = models.CharField(max_length=255, blank=True, null=True)
    dato_nuevo = models.CharField(max_length=255, blank=True, null=True)
    otra_accion = models.CharField(max_length=255, blank=True, null=True)
    slug_log = models.SlugField(max_length=255, blank=True, unique=True)

    class Meta:
        #verbose_name = 'VisitasHomepage'
        verbose_name_plural = 'Bitácora'
        ordering = ['id']

    def __str__(self):
        return self.DB_afectada

    # función para generar el slog antes de guardar el registro 
    def save(self, *args, **kwargs):
        if not self.slug_log:
            a=str(uuid.uuid4())
            b=str(datetime.now()).replace('-','').replace(':','').replace('.','-').replace(' ','-')
            c=random.choice(["a26", "31b", "98c", "d32", "11e", "f09", "28g"]) + random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ") + str(random.randint(1, 500))
            self.slug_log = random.choice("!&%#|/£“¡¬-+}{ñ*-())^~`,_:¿'?") + a + '-' + b + '-' + c
        return super().save(*args, **kwargs)




