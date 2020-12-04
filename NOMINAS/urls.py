"""NOMINAS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

import resumen.views
import concentrado.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', resumen.views.ingresar, name='login'),
    path('salir/', resumen.views.salir, name='salir'),
    path('inicio/', resumen.views.mostrar_inicio, name='index'),
    path('registro/', resumen.views.registro_usuario, name='registro'),
    path('nomina/', resumen.views.registro_nomina, name='nomina'),
    path('editar/<int:id_nom>', resumen.views.editar_nom, name='edit_nom'),     
    path('borrar/<int:id_nom>', resumen.views.eliminar_registro_nom),

    path('concentrado/', concentrado.views.mostrar_concentrado, name='concentrado'),
    path('agregar_datos/', concentrado.views.cargar_archivo, name='agregar_datos'),
]
