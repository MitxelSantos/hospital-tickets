from django.contrib import admin
from .models import Ticket

class TicketAdmin(admin.ModelAdmin):
    # Columnas que verás en la tabla
    list_display = ('id', 'nombre', 'categoria', 'prioridad', 'estado', 'asignado_a', 'fecha_creacion')
    # Filtros laterales
    list_filter = ('estado', 'categoria', 'asignado_a', 'prioridad')
    # Buscador
    search_fields = ('nombre', 'descripcion')
    # Campos que solo se pueden leer (para que no modifiquen el reporte original por error)
    readonly_fields = ('fecha_creacion',)

admin.site.register(Ticket, TicketAdmin)