# Generated by Django 4.1.2 on 2022-10-18 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HomePage', '0002_rename_visitas_homepage_visitas'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='visitas',
            options={'ordering': ['id'], 'verbose_name_plural': 'HomepageVisitas'},
        ),
        migrations.AddField(
            model_name='visitas',
            name='navegador',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='visitas',
            name='ubicación_visita',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]