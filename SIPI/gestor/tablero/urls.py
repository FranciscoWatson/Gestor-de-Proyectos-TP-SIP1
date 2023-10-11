from django.urls import path
from .views import ProyectoLista,TareaLista
urlpatterns = [
    path('proyectos/', ProyectoLista.as_view(), name='proyecto-lista'),
    path('tareas/', TareaLista.as_view(), name='tarea-lista'),
]
