"""
URL configuration for EventosApi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from eventosApiapp.views import get_eventos, post_evento, put_evento, delete_evento, get_boletas, post_boleta, put_boleta, delete_boletas 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('eventos/', get_eventos, name='eventos'),
    path('eventos/crear/', post_evento, name='crear_evento'),
    path('eventos/modificar/<int:evento_id>/', put_evento, name='modificar_evento'),
    path('eventos/eliminar/<int:evento_id>/', delete_evento, name='elimimar_evento'),

    path('boletas/', get_boletas, name='boletas'),
    path('boletas/crear/', post_boleta, name='crear_boleta'),
    path('boletas/modificar/<int:boleta_id>/', put_boleta, name='modificar_boleta'),
    path('boletas/eliminar/<int:boleta_id>/', delete_boletas, name='elimimar_boleta'),
    
]
