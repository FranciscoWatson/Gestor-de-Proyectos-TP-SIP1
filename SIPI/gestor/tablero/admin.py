from django.contrib import admin
from django.http import HttpResponseRedirect
from .models import Proyecto, Tarea
from django.contrib import messages


def ver_tablero(modeladmin, request, queryset):
    if queryset.count() != 1:
        messages.error(request,'Se debe seleccionar un solo proyecto')
        return

    proyecto = queryset.first()
    id_proyecto = str(proyecto.id)
    dir_tablero = 'http://173.230.135.41/?id=' + id_proyecto
    return HttpResponseRedirect(dir_tablero)

   
@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ('nombre','descripcion','fecha_creacion','activo')
    list_filter = ('fecha_creacion','activo')
    search_fields = ('nombre', 'descripcion')
    actions = [ver_tablero]  # Agregar la acción personalizada


@admin.register(Tarea)
class TareaAdmin(admin.ModelAdmin):
    list_display = ('nombre','usuario','estado','proyecto', 'fecha_creacion', 'completada')
    list_filter = ('proyecto', 'completada','usuario')
    search_fields = ('nombre', 'descripcion')
# Register your models here.


