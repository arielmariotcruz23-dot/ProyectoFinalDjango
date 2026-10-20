from django.db import models


class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    correo = models.CharField(max_length=150, null=True, blank=True)

    class Meta:
        db_table = 'clientes'

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Barbero(models.Model):
    id_barbero = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    especialidad = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = 'barberos'

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Servicio(models.Model):
    id_servicio = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(null=True, blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    duracion = models.IntegerField()

    class Meta:
        db_table = 'servicios'

    def __str__(self):
        return self.nombre


class Cita(models.Model):
    id_cita = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        db_column='id_cliente'
    )
    barbero = models.ForeignKey(
        Barbero,
        on_delete=models.CASCADE,
        db_column='id_barbero'
    )
    servicio = models.ForeignKey(
        Servicio,
        on_delete=models.CASCADE,
        db_column='id_servicio'
    )
    fecha = models.DateField()
    hora = models.TimeField()
    estado = models.CharField(max_length=20, default='Pendiente')
    observaciones = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'citas'

    def __str__(self):
        return f"Cita {self.id_cita} - {self.fecha} {self.hora}"


class Horario(models.Model):
    id_horario = models.AutoField(primary_key=True)
    barbero = models.ForeignKey(
        Barbero,
        on_delete=models.CASCADE,
        db_column='id_barbero'
    )
    dia_semana = models.CharField(max_length=20)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()

    class Meta:
        db_table = 'horarios'

    def __str__(self):
        return f"{self.barbero} - {self.dia_semana}"