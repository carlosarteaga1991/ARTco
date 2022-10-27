# Generated by Django 4.1.2 on 2022-10-26 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_politica_seguridad_intentos_fallidos_login_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='fch_ingreso_labores',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de Ingreso a Laborar'),
        ),
        migrations.AddField(
            model_name='user',
            name='fch_ultimo_cambio_password',
            field=models.CharField(blank=True, max_length=70),
        ),
        migrations.AddField(
            model_name='user',
            name='token',
            field=models.UUIDField(blank=True, editable=False, null=True),
        ),
    ]