# Generated by Django 3.2.22 on 2023-10-14 02:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tablero', '0010_auto_20231012_1416'),
    ]

    operations = [
        migrations.CreateModel(
            name='equipos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('activo', models.BooleanField(default=True)),
                ('fecha_finalizacion', models.DateField(blank=True, null=True)),
                ('integrantes', models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL)),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tablero.proyecto')),
            ],
        ),
    ]
