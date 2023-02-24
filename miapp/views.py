from django.http import HttpResponse
from .models import Proyecto,Tarea
from django.shortcuts import render, redirect
from .formularios import CrearNuevaTarea

# Create your views here.
#def index(request):
#    return HttpResponse('Index page')
#
#def hello(request, username):
#    print(username)
#    return render("<h2>Hello %s</h2>" % username)
#
#def about(request):
#	return HttpResponse('About')
#
#def proyectos(request):
#    proyectos = list(Proyecto.objects.values())
#    return JsonResponse(proyectos, safe=False)
#
#def tareas(request, id):
#    tareas = Tarea.objects.get(id=id)
#    tareas = get_object_or_404(Tarea, id=id)
#    return HttpResponse('Tareas: %s' % tareas.titulo)


# Para poder utilizar html:
def index(request):
    nombre = 'Lucas'
    return render(request,'index.html',{
         'nombre': nombre
    })

def hello(request, username):
    print(username)
    return render("<h2>Hello %s</h2>" % username)

def about(request):
	return render(request,'about.html')

def proyectos(request):
    #proyectos = list(Proyecto.objects.values())
    proyectos = Proyecto.objects.all()
    return render(request, 'proyecto.html', {
         'proyectos' : proyectos
    })

def tareas(request):
#    tareas = Tarea.objects.get(id=id)
    tareas = Tarea.objects.all()
    return render(request, 'tarea.html', {
         'tareas' : tareas
    })

def crear_tareas(request):
    if request.method == 'GET':
        return render(request,'crear_tarea.html',{
            'formulario':CrearNuevaTarea()
        })
        # show interface
#        return render(request,'tarea.html')
    else:
        Tarea.objects.create(
            titulo=request.POST['titulo'],
            descripcion=request.POST['descripcion'],
            proyecto_id=2
        )
        return redirect('/tareas/')

def lucas(request):
    return render(request,'lucas.html')



