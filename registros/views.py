from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView, ListView
from django.views.generic.base import TemplateView

from .models import Evento, Miembro, Legado


class IndexView(TemplateView):
    template_name = 'registros/index.html'


class EventosView(ListView):
    template_name = 'registros/eventos.html'
    context_object_name = 'latest_eventos_list'

    def get_queryset(self):
        """Return all Eventos."""
        return Evento.objects.all()


class EventoDetailView(DetailView):
    model = Evento
    template_name = 'registros/evento_detail.html'


class MiembrosView(ListView):
    template_name = 'registros/miembros.html'
    context_object_name = 'latest_miembros_list'

    def get_queryset(self):
        """Return all Miembros."""
        return Miembro.objects.all()


class MiembroDetailView(DetailView):
    model = Miembro
    template_name = 'registros/miembro_detail.html'


class LegadosView(ListView):
    template_name = 'registros/legados.html'
    context_object_name = 'latest_legados_list'

    def get_queryset(self):
        """Return all Legados."""
        return Legado.objects.all()


class LegadoDetailView(DetailView):
    model = Legado
    template_name = 'registros/legado_detail.html'
