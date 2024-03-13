"""
URL configuration for proyecto project.

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
from django.contrib             import admin
from django.urls                import path
from django.conf                import settings
from django.conf.urls           import handler404
from django.conf.urls.static    import static
from tienda.views               import *

handler404= error_404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='inicio'),
    path("contacto/",contacto, name="contacto"),    
    path("tienda/",tienda, name="tienda"),
    path('buscar/', busqueda, name="buscar"),
    path('registro/',usuario_nuevo, name='registro'),
    path('ingresar/', ingresar, name='ingresar'),
    path('privado/',privado, name='privado'),
    path('salir/',salir, name='salir'),
    path("tienda_SW/", tienda_SM, name='tienda_SM'),
    path("tienda_HW/", tienda_NS, name='tienda_NS'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
