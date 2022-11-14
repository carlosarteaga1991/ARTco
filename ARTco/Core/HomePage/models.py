from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save
from datetime import *
import uuid
import random

class Visita(models.Model):
    id = models.AutoField(primary_key=True)
    fch_visita = models.DateTimeField(auto_now_add=True)
    ip_visita = models.CharField(max_length=255, blank=True, null=True)
    ubicacion_visita = models.CharField(max_length=255, blank=True, null=True)
    dispositivo_visitante = models.CharField(max_length=255, blank=True, null=True)
    navegador = models.CharField(max_length=255, blank=True, null=True)
    sistema_operativo = models.CharField(max_length=255, blank=True, null=True)
    slug_visita = models.SlugField(max_length=255, blank=True, unique=True)

    def __str__(self):
        return str(self.ubicacion_visita) + ' / ' + str(self.ip_visita) + ' / ' + str(self.sistema_operativo) + ' / ' + str(self.navegador)

    class Meta:
        #verbose_name = 'VisitasHomepage'
        verbose_name_plural = 'HomepageVisitas'
        ordering = ['id']

        

    # función para generar el slog antes de guardar el registro
    def save(self, *args, **kwargs):
        if not self.slog_visita:
            a=str(uuid.uuid4())
            b=str(datetime.now()).replace('-','').replace(':','').replace('.','-').replace(' ','-')
            c=random.choice(["a26", "31b", "98c", "d32", "11e", "f09", "28g"]) + random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ") + str(random.randint(1, 500))
            self.slug_visita = random.choice("!&%#|/£“¡¬-+}{ñ*-())^~`,_:¿'?") + a + '-' + b + '-' + c
        return super().save(*args, **kwargs)




