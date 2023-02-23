from django.db import models

# Create your models here.

class Proyecto(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class Tarea(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    hecho = models.BooleanField(default=False) # De esta manera coloco un booleano para saber si la tarea fue hecha o no.

    def __str__(self):
        return self.titulo
