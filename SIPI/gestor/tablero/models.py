from django.db import models
from django.contrib.auth.models import User  
from datetime import datetime
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
    fecha_asignacion = models.DateField(null=True, blank=True)
    fecha_finalizacion = models.DateField(null=True, blank=True)
    estado = models.CharField(max_length=1,choices=ESTADOS,default='I',null=True, blank=True)
    completada = models.BooleanField(default=False)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    duracion_en_dias_habiles = models.PositiveIntegerField(null=True, blank=True)


    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        if self.usuario and not self.fecha_asignacion:
            self.fecha_asignacion = datetime.now()
            self.estado = 'I'  
        super(Tarea, self).save(*args, **kwargs)

# Create your models here.
