# Generated by Django 3.2.22 on 2023-10-12 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tablero', '0005_auto_20231011_2322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarea',
            name='estado',
            field=models.CharField(choices=[('P', 'Pendiente'), ('I', 'Inciada'), ('F', 'Finalizada')], default='I', max_length=1),
        ),
    ]
