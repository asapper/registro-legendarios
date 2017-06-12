from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.views.generic.base import TemplateView

from .models import Evento, Miembro, Legado

LOGIN_URL = '/login/'


class IndexView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    login_url = LOGIN_URL
    template_name = 'registros/index.html'

    def test_func(self):
        return (self.request.user.has_perm('registros.view_evento') and
                self.request.user.has_perm('registros.view_legado') and
                self.request.user.has_perm('registros.view_miembro'))


class EventosView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    login_url = LOGIN_URL
    template_name = 'registros/eventos.html'
    context_object_name = 'latest_eventos_list'

    def get_queryset(self):
        """Return all Eventos."""
        return Evento.objects.all()

    def test_func(self):
        return self.request.user.has_perm('registros.view_evento')


class EventoDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    login_url = LOGIN_URL
    model = Evento
    template_name = 'registros/evento_detail.html'

    def test_func(self):
        return self.request.user.has_perm('registros.view_evento')


class MiembrosView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    login_url = LOGIN_URL
    template_name = 'registros/miembros.html'
    context_object_name = 'latest_miembros_list'

    def get_queryset(self):
        """Return all Miembros."""
        return Miembro.objects.all()

    def test_func(self):
        return self.request.user.has_perm('registros.view_miembro')


class MiembroDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    login_url = LOGIN_URL
    model = Miembro
    template_name = 'registros/miembro_detail.html'

    def test_func(self):
        return self.request.user.has_perm('registros.view_miembro')


class LegadosView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    login_url = LOGIN_URL
    template_name = 'registros/legados.html'
    context_object_name = 'latest_legados_list'

    def get_queryset(self):
        """Return all Legados."""
        return Legado.objects.all()

    def test_func(self):
        return self.request.user.has_perm('registros.view_legado')


class LegadoDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    login_url = LOGIN_URL
    model = Legado
    template_name = 'registros/legado_detail.html'

    def test_func(self):
        return self.request.user.has_perm('registros.view_legado')
