from django.http import HttpResponse
from .models import Proyecto,Tarea
from django.shortcuts import render, redirect, get_object_or_404
from .formularios import CrearNuevaTarea, CrearNuevoProyecto


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
    return render(request, 'proyectos/proyecto.html', {
         'proyectos' : proyectos
    })

def tareas(request):
#    tareas = Tarea.objects.get(id=id)
    tareas = Tarea.objects.all()
    return render(request, 'tareas/tarea.html', {
         'tareas' : tareas
    })

def crear_tareas(request):
    if request.method == 'GET':
        return render(request,'tareas/crear_tarea.html',{
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

def crear_proyectos(request):
    if request.method == 'GET':
        return render(request, 'proyectos/crear_proyecto.html', {
        'formulario':CrearNuevoProyecto() })
    else:
        Proyecto.objects.create(nombre=request.POST['nombre'])
        return redirect('proyectos')

def detalle_proyectos(request, id):
    proyecto = get_object_or_404(Proyecto, id=id)
    tareas = Tarea.objects.filter(proyecto_id=id)
    return render(request,'proyectos/detalle.html',{
        'proyecto':proyecto,
        'tareas':tareas
    })

def lucas(request):
    return render(request,'lucas.html')



