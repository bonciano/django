from django.urls import path
from . import views

urlpatterns = [
	path('', views.index),
	path('about/', views.about),
    path('hello/<str:username>', views.hello),
    path('proyectos/',views.proyectos),
    path('tareas/',views.tareas),
    path('crear_tarea/',views.crear_tareas),
    path('lucas/',views.lucas)
]
