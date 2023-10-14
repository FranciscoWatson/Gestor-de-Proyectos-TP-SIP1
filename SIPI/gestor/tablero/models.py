
from django.db import models
from django.contrib.auth.models import User  
from datetime import datetime
from django.contrib.auth.models import User

# models.py


class Proyecto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_creacion = models.DateField(auto_now_add=True)
    activo = models.BooleanField(default=True)
    fecha_finalizacion = models.DateField(null=True,blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "proyecto"  
        verbose_name_plural = "proyectos"  # Nombre plural en el administrador



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
        if self.usuario and not self.fecha_asignacion: # fecha_asignacion queda determinada por la primera asignacion, sin importar las asignaciones posteriores.
            self.fecha_asignacion = datetime.now()
            self.estado = 'I'  
        super(Tarea, self).save(*args, **kwargs)


class equipos(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    integrantes = models.ManyToManyField(User,null=True,blank=True)
    fecha_creacion = models.DateField(auto_now_add=True)
    activo = models.BooleanField(default=True)
    fecha_finalizacion = models.DateField(null=True,blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Equipo" 
        verbose_name_plural = "equipos de trabajo"  


