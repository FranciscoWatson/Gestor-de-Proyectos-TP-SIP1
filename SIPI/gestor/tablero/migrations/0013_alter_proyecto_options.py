# Generated by Django 3.2.22 on 2023-10-14 02:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tablero', '0012_alter_proyecto_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='proyecto',
            options={'verbose_name': 'proyecto', 'verbose_name_plural': 'proyectos'},
        ),
    ]