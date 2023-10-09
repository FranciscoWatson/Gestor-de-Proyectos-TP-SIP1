from django.contrib import admin
from django.http import HttpResponseRedirect
from .models import Proyecto, Tarea


def ver_tablero(modeladmin, request, queryset):
    for proyecto in queryset:
        # Recuperar todas las tareas relacionadas con el proyecto seleccionado
       ids_seleccionados = queryset.values_list('id', flat=True)
       tareas_del_proyecto = Tarea.objects.filter(proyecto=proyecto)

        # Redirige a otra página pasando los IDs como parámetros
       tablero = f'/tablero/?ids={",".join(map(str, ids_seleccionados))}'

    return HttpResponseRedirect(tablero)

   
@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha_creacion')
    list_filter = ('fecha_creacion',)
    search_fields = ('nombre', 'descripcion')
    actions = [ver_tablero]  # Agregar la acción personalizada


@admin.register(Tarea)
class TareaAdmin(admin.ModelAdmin):
    list_display = ('nombre','estado','proyecto', 'fecha_creacion', 'completada')
    list_filter = ('proyecto', 'completada')
    search_fields = ('nombre', 'descripcion')
# Register your models here.


