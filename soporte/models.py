from django.db import models
from django.contrib.auth.models import User

class Ticket(models.Model):
    # Definición de opciones
    CATEGORIAS = [
        ('SIHOS', 'Falla en SIHOS'),
        ('EQUIPOS', 'Computador / Periféricos'),
        ('IMPRESORA', 'Impresoras / Toner'),
        ('RED', 'Internet / Conectividad'),
        ('OTRO', 'Otro Requerimiento'),
    ]
    
    ESTADOS = [
        ('PENDIENTE', 'Pendiente de Asignar'),
        ('EN_PROCESO', 'En Revisión'),
        ('RESUELTO', 'Resuelto'),
    ]

    PRIORIDAD = [
        ('BAJA', 'Baja'),
        ('MEDIA', 'Media'),
        ('ALTA', 'Alta'),
    ]

    # Campos del solicitante (Públicos)
    nombre = models.CharField(max_length=100, verbose_name="Nombre del Solicitante")
    cargo = models.CharField(max_length=100, help_text="Ej: Médico, Enfermera Jefe")
    ubicacion = models.CharField(max_length=100, verbose_name="Sede / Área", help_text="Ej: Urgencias, Sede Admin")
    descripcion = models.TextField(verbose_name="Descripción del Problema")
    prioridad = models.CharField(max_length=10, choices=PRIORIDAD, default='MEDIA')
    categoria = models.CharField(max_length=20, choices=CATEGORIAS, default='OTRO')

    # Campos de gestión (Internos TI)
    asignado_a = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Técnico/Ing Asignado")
    estado = models.CharField(max_length=20, choices=ESTADOS, default='PENDIENTE')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_cierre = models.DateTimeField(null=True, blank=True)
    solucion = models.TextField(blank=True, verbose_name="Solución Técnica")

    def __str__(self):
        return f"Ticket #{self.id} - {self.categoria}"