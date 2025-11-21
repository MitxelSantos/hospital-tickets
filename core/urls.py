# core/urls.py
from django.contrib import admin
from django.urls import path
from soporte.views import crear_ticket # Importamos la vista

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', crear_ticket, name='crear_ticket'), # Ruta raíz
]
