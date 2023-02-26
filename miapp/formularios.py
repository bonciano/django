from django import forms

class CrearNuevaTarea(forms.Form):
    titulo = forms.CharField(label='Titulo de tarea', max_length=200,widget=forms.TextInput(attrs={'class': 'input'}))
    # si bien esto se parece a lo mismo que hicimos con la creacion de modelos, en realidad
    # lo que estamos haciendo es que que django nos cree el formulario en el html.
    descripcion = forms.CharField(label='Descripcion de la tarea',widget = forms.Textarea(attrs={'class':'input'}))

class CrearNuevoProyecto(forms.Form):
    nombre = forms.CharField(label='Nombre del proyecto',max_length=200, widget=forms.TextInput(attrs={'class' : 'input'}))
