from django.contrib import admin

from .models import Legado, Miembro, Evento, Participacion

admin.site.register(Legado)
admin.site.register(Miembro)
admin.site.register(Evento)
admin.site.register(Participacion)
