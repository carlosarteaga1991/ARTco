# Generated by Django 4.1.2 on 2022-10-31 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0004_politica_seguridad_permitir_sesion_duplicada'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='autenticacion_doble_factor',
            field=models.BooleanField(choices=[(False, 'No'), (True, 'Si')], default=False, null=True),
        ),
    ]
