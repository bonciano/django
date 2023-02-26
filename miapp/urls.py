from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('about/', views.about, name='about'),
    path('hello/<str:username>', views.hello, name='hello'),
    path('proyectos/',views.proyectos, name='proyectos'),
    path('proyectos/<int:id>',views.detalle_proyectos, name='detalle_proyectos'),
    path('tareas/',views.tareas, name='tareas'),
    path('crear_tarea/',views.crear_tareas, name='crear_tarea'),
    path('crear_proyecto/',views.crear_proyectos, name='crear_proyecto'),
    path('lucas/',views.lucas, name='lucas')
]
