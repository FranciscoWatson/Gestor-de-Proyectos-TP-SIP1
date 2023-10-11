# -*- coding: utf-8 -*-
from django.shortcuts import render
from .models import Proyecto, Tarea
from rest_framework import generics
from .serializers import ProyectoSerializer,TareaSerializer




def ver_tablero(request):
  
    ids = request.GET.get('ids', '')
    ids_lista = ids.split(',')

    tareas_del_proyecto = Tarea.objects.filter(proyecto=ids_lista[0])


    return render(request, 'index.html', {'tareas': tareas_del_proyecto})

class ProyectoLista(generics.ListCreateAPIView):
    queryset = Proyecto.objects.all()
    serializer_class = ProyectoSerializer


class TareaLista(generics.ListCreateAPIView):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer

    def get_queryset(self):
        # Obtiene el valor del parámetro 'id' de la URL
        id = self.request.query_params.get('id')
        # Filtra las tareas por el valor de 'id' (puedes personalizar esto según tus necesidades)
        queryset = Tarea.objects.filter(proyecto=id)
        return queryset
