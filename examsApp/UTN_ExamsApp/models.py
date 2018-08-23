from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class TipoPregunta(models.Model):
    descripcion = models.CharField(max_length=200)


class Habilidad(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=300)
    #bugfixing, correccion de codigo, etc


class Tema(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=300)


class Clasificacion(models.Model):
    tema = models.ForeignKey(Tema)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=300)


class Pregunta(models.Model):
    creador = models.ForeignKey(User)
    fecha_creacion = models.DateTimeField(default=timezone.now)
    tipo = models.ForeignKey(TipoPregunta)
    habilidad = models.ForeignKey(Habilidad, null=True, blank=True)
    titulo = models.CharField(max_length=150)
    contenido = models.CharField(max_length=1000, null=True, blank=True)
    #imagen = models.ImageField(null=True, blank=True)
    dificultad = models.IntegerField(null=True, blank=True)
    #notas y mantenimiento, alertar errores


class Respuesta(models.Model):
    pregunta = models.ForeignKey(Pregunta)
    contenido = models.CharField(max_length=500)
    es_correcta = models.BooleanField(default=False)


class Revision(models.Model):
    ESTADOS = (
        ('pendiente', 'Pendiente'), ('aprobada', 'Aprobada'), ('desaprobada', 'Desaprobada'), ('cancelada', 'Cancelada'),
    )
    pregunta = models.ForeignKey(Pregunta)
    revisor = models.ForeignKey(User)
    fecha_revision = models.DateTimeField(null=True, blank=True)
    estado = models.CharField(max_length=60, choices=ESTADOS, default='pendiente')
    observaciones = models.CharField(max_length=1000, null=True, blank=True)
    dificultad_propuesta = models.IntegerField(null=True, blank=True)


class Examen(models.Model):
    codigo = models.CharField(max_length=10, null=True, blank=True, default=None) #acortar, otro formato?
    activo = models.BooleanField(default=False)

    preguntas = models.ManyToManyField(Pregunta, related_name='preguntas_examen', null=True, blank=True)
    fecha_creacion = models.DateTimeField(default=timezone.now)
    creador = models.ForeignKey(User)


class Evaluacion(models.Model):
    nombre_alumno = models.CharField(max_length=500)
    apellido_alumno = models.CharField(max_length=500)
    dni_alumno = models.IntegerField()
    examen = models.ForeignKey(Examen)
    fecha_creacion = models.DateTimeField(default=timezone.now)
    corregido = models.BooleanField(default=False)
    resultado = models.CharField(max_length=30, null=True, blank=True, default=None)
    nota = models.FloatField()

#tabla respuestas: related user, related examen, pregunta, respuestas
#alumno:

#rol para los usuarios. permisos

#SE VENCE PYTHON