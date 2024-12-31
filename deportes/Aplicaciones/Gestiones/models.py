from django.db import models

#-----------------------------------------PARTICIPANTES----------------------------------------------------------------
class Participante(models.Model):
    id = models.AutoField(primary_key=True) 
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

#-----------------------------------------EVENTOS----------------------------------------------------------------
class Evento(models.Model):
    id = models.AutoField(primary_key=True) 
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    ubicacion = models.CharField(max_length=200)
    organizador = models.CharField(max_length=100)
    cupo_maximo = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nombre

#-----------------------------------------ACTIVIDADES----------------------------------------------------------------
class Actividad(models.Model):
    id = models.AutoField(primary_key=True) 
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    duracion = models.DurationField()
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name="actividades")
    nivel_dificultad = models.CharField(max_length=50, choices=[('Facil', 'Fácil'), ('Intermedio', 'Intermedio'), ('Avanzado', 'Avanzado')])
    equipo_necesario = models.TextField()

    def __str__(self):
        return self.nombre

#-----------------------------------------INSCRIPCIONES----------------------------------------------------------------
class Inscripcion(models.Model):
    id = models.AutoField(primary_key=True)  
    participante = models.ForeignKey(Participante, on_delete=models.CASCADE, related_name="inscripciones")
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name="inscripciones")
    fecha_inscripcion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=50, choices=[('Confirmada', 'Confirmada'), ('Pendiente', 'Pendiente'), ('Cancelada', 'Cancelada')])
    comentarios = models.TextField(blank=True, null=True)

    class Meta:
        unique_together = ('participante', 'evento')

    def __str__(self):
        return f"{self.participante} inscrito en {self.evento}"

#-----------------------------------------REGISTRO DE ACTIVIDAD----------------------------------------------------------------
class RegistroActividad(models.Model):
    id = models.AutoField(primary_key=True) 
    participante = models.ForeignKey(Participante, on_delete=models.CASCADE, related_name="registros_actividades")
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE, related_name="registros_actividades")
    resultado = models.TextField(blank=True, null=True)
    puntuacion = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)
    fecha_realizacion = models.DateTimeField()

    class Meta:
        unique_together = ('participante', 'actividad')

    def __str__(self):
        return f"{self.participante} en {self.actividad}"
    

