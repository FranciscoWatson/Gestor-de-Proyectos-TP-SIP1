# Generated by Django 3.2.22 on 2023-10-11 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tablero', '0004_auto_20231011_1407'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarea',
            name='duracion_en_dias_habiles',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tarea',
            name='fecha_asignacion',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tarea',
            name='fecha_finalizacion',
            field=models.DateField(blank=True, null=True),
        ),
    ]
