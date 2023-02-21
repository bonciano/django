from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Proyecto,Tarea
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    return HttpResponse('Index page')

def hello(request, username):
    print(username)
    return HttpResponse("<h2>Hello %s</h2>" % username)

def about(request):
	return HttpResponse('About')

def proyectos(request):
    proyectos = list(Proyecto.objects.values())
    return JsonResponse(proyectos, safe=False)

def tareas(request, id):
#    tareas = Tarea.objects.get(id=id)
    tareas = get_object_or_404(Tarea, id=id)
    return HttpResponse('Tareas: %s' % tareas.titulo)



