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
    hostname_visitante = models.CharField(max_length=255, blank=True, null=True)
    navegador = models.CharField(max_length=255, blank=True, null=True)
    sistema_operativo = models.CharField(max_length=255, blank=True, null=True)
    slog_visita = models.SlugField(max_length=255, blank=True, unique=True)

    class Meta:
        #verbose_name = 'VisitasHomepage'
        verbose_name_plural = 'HomepageVisitas'
        ordering = ['id']

        def __str__(self):
            return self.ip_visita

    # función para generar el slog antes de guardar el registro
    def save(self, *args, **kwargs):
        if not self.slog_visita:
            a=str(uuid.uuid4())
            b=str(datetime.now()).replace('-','').replace(':','').replace('.','-').replace(' ','-')
            c=random.choice(["a26", "31b", "98c", "d32", "11e", "f09", "28g"]) + random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ") + str(random.randint(1, 500))
            self.slog_visita = random.choice("!&%#|/£“¡¬-+}{ñ*-())^~`,_:¿'?") + a + '-' + b + '-' + c
        return super().save(*args, **kwargs)

#modelo para registrar cada visita a la página


