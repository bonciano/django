"""miproyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
# include sirve para incluir un bloque de urls que viene por parte de una aplicacion.

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', include('miapp.urls')) # en el primer parametro (que esta vacio) si lo dejo asi es como si la app estuviera en la raiz, si le coloco por ejemplo "home/", en la url del server, luego del puerto y como antecesor de todas las secciones de mi app, debo colocar 'home/'.
]
