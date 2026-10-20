from django.contrib import admin
from .models import Cliente, Barbero, Servicio, Cita, Horario


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['id_cliente', 'nombre', 'apellido', 'telefono', 'correo']
    search_fields = ['nombre', 'apellido', 'telefono', 'correo']


@admin.register(Barbero)
class BarberoAdmin(admin.ModelAdmin):
    list_display = ['id_barbero', 'nombre', 'apellido', 'telefono', 'especialidad']
    search_fields = ['nombre', 'apellido', 'especialidad']


@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ['id_servicio', 'nombre', 'precio', 'duracion']
    search_fields = ['nombre']


@admin.register(Cita)
class CitaAdmin(admin.ModelAdmin):
    list_display = ['id_cita', 'cliente', 'barbero', 'servicio', 'fecha', 'hora', 'estado']
    list_filter = ['estado', 'fecha', 'barbero']
    search_fields = ['cliente__nombre', 'cliente__apellido']


@admin.register(Horario)
class HorarioAdmin(admin.ModelAdmin):
    list_display = ['id_horario', 'barbero', 'dia_semana', 'hora_inicio', 'hora_fin']
    list_filter = ['dia_semana', 'barbero']