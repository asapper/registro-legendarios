from django.contrib import admin
from django.contrib.auth.models import Permission

from .models import Legado, Miembro, Evento, Participacion

admin.site.register(Legado)
admin.site.register(Miembro)
admin.site.register(Evento)
admin.site.register(Participacion)

admin.site.register(Permission)
