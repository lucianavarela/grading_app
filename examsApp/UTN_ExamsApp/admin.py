from django.contrib import admin
from .models import TipoPregunta, Tema, Pregunta, Habilidad, Clasificacion, Respuesta, Revision, Examen, Evaluacion

admin.site.register(TipoPregunta)
admin.site.register(Tema)
admin.site.register(Pregunta)
admin.site.register(Habilidad)
admin.site.register(Clasificacion)
admin.site.register(Respuesta)
admin.site.register(Revision)
admin.site.register(Examen)
admin.site.register(Evaluacion)