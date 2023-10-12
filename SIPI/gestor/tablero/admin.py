from django.contrib import admin
from django.http import HttpResponseRedirect
from .models import Proyecto, Tarea
from django.contrib import messages
from datetime import datetime
from datetime import date
from django.utils.html import format_html

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
    list_display = ('nombre','usuario','estado','proyecto', 'fecha_creacion', 'completada','dias_trascurridos','tiempo_transcurrido')
    list_filter = ('proyecto', 'completada','usuario')
    search_fields = ('nombre', 'descripcion')
    readonly_fields = ["fecha_asignacion"]

# Register your models here.

        
    def dias_trascurridos(self, obj):

        if obj.fecha_asignacion:
            today = date.today()
            delta = today - obj.fecha_asignacion
            return int(delta.days)
        return None


    def tiempo_transcurrido(self, obj):
       if obj.fecha_asignacion:
           today = date.today()
           delta = today - obj.fecha_asignacion
           delta = int(delta.days)
           porcen = float(delta/obj.duracion_en_dias_habiles)*100
           if porcen < 35:
               return format_html('<a style="color: green;">{}</a>', str(porcen) + " %")
           elif (porcen >=35 and porcen < 75):
               return format_html('<a style="color: orage;">{}</a>', str(porcen) + " %")
           else:
          #      return format_html('<b style="background:{};">{}</b>',color,obj.status)
               return format_html('<a style="color: red;">{}</a>',str(porcen) + " %")



