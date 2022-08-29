"""proyectoRentame URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from contenido import views

from cabañas import views as views_cabañas
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views_cabañas.promociones,name="Promociones"),
    path('principal/', views.principal, name='Principal'),
    path('catalogo/', views_cabañas.catalogo, name="Catalogo"),
    path('opiniones/',views_cabañas.opiniones, name="Opiniones"),
    path('registrarOpinion/', views_cabañas.registrarOpinion, name='RegistrarOpinion'), 
    path('editarDuda/<int:id>', views_cabañas.editarDuda, name='EditarDuda'),
    path('consultarDuda/<int:id>', views_cabañas.consultarDuda, name='ConsultarDuda'),
    path('eliminarDuda/<int:id>', views_cabañas.eliminarDuda, name='EliminarDuda'),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
