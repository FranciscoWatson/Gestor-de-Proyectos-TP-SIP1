# -*- coding: utf-8 -*-
from django.shortcuts import render
from .models import Proyecto, Tarea




def ver_tablero(request):
  
    ids = request.GET.get('ids', '')
    ids_lista = ids.split(',')

    tareas_del_proyecto = Tarea.objects.filter(proyecto=ids_lista[0])


    return render(request, 'index.html', {'tareas': tareas_del_proyecto})
