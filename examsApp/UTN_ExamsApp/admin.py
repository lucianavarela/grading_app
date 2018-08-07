from django.contrib import admin
from .models import TipoPregunta, Tema, Pregunta, Habilidad, Clasificacion, Respuesta, Revision

admin.site.register(TipoPregunta)
admin.site.register(Tema)
admin.site.register(Pregunta)
admin.site.register(Habilidad)
admin.site.register(Clasificacion)
admin.site.register(Respuesta)
admin.site.register(Revision)