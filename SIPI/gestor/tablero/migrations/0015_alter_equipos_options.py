# Generated by Django 3.2.22 on 2023-10-14 02:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tablero', '0014_alter_equipos_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='equipos',
            options={'verbose_name': 'Equipos de Trabajo', 'verbose_name_plural': 'equipos'},
        ),
    ]
