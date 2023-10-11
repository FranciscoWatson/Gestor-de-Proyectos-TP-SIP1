# Generated by Django 3.1.7 on 2023-10-10 19:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tarea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('estado', models.CharField(choices=[('P', 'Pendiente'), ('I', 'Inciada'), ('F', 'Finalizada')], max_length=1)),
                ('completada', models.BooleanField(default=False)),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tablero.proyecto')),
            ],
        ),
    ]
