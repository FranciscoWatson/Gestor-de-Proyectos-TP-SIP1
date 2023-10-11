from django.db import models
from django.contrib.auth.models import User  

# models.py

from django.db import models

class Proyecto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_creacion = models.DateField(auto_now_add=True)
    activo = models.BooleanField(default=True)
    fecha_finalizacion = models.DateField(null=True,blank=True)

    def __str__(self):
        return self.nombre



class Tarea(models.Model):
    ESTADOS = (
        ('P', 'Pendiente'),
        ('I', 'Inciada'),
        ('F', 'Finalizada'),
    )
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_creacion = models.DateField(auto_now_add=True)
    estado = models.CharField(max_length=1,choices=ESTADOS)
    completada = models.BooleanField(default=False)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)


    def __str__(self):
        return self.nombre


# Create your models here.
