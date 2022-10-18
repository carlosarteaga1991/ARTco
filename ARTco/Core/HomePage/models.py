from django.db import models

class visitas(models.Model):
    id = models.AutoField(primary_key=True)
    fch_visita = models.DateTimeField(auto_now=True)
    ip_visita = models.CharField(max_length=255, blank=True, null=True)
    ubicación_visita = models.CharField(max_length=255, blank=True, null=True)
    navegador = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        #verbose_name = 'VisitasHomepage'
        verbose_name_plural = 'HomepageVisitas'
        ordering = ['id']

        def __str__(self):
            return self.ip_visita


