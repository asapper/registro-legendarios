from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        UserPassesTestMixin,
                                        PermissionRequiredMixin)
from django.contrib.auth.models import Group
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import DetailView, ListView
from django.views.generic.base import TemplateView

from .models import Evento, Miembro, Legado

LOGIN_URL = '/login/'
MAYOR_ACCESO_GROUP = Group.objects.get(name='Mayor acceso usuario')


def home_view(request):
    """This view redirects to the logged-in user's profile page."""
    return redirect(reverse('registros:miembro_detail', kwargs={'pk': request.user.miembro.pk}))


class IndexView(LoginRequiredMixin, TemplateView):
    login_url = LOGIN_URL
    template_name = 'registros/index.html'


class EventosView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    login_url = LOGIN_URL
    template_name = 'registros/eventos.html'
    context_object_name = 'latest_eventos_list'
    permission_required = 'registros.view_eventos'
    raise_exception = True  # 403 instead of login redirect

    def get_queryset(self):
        """Return all Eventos."""
        if MAYOR_ACCESO_GROUP in self.request.user.groups.all():
            return Evento.objects.all()
        else:
            return Evento.objects.filter(pk__in=self.request.user.miembro.evento_set.all())


class EventoDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    login_url = LOGIN_URL
    model = Evento
    template_name = 'registros/evento_detail.html'
    permission_required = 'registros.view_eventos'

    def get_object(self):
        object = super(EventoDetailView, self).get_object()
        if (object in self.request.user.miembro.evento_set.all() or 
                MAYOR_ACCESO_GROUP in self.request.user.groups.all()):
            return object
        else:
            raise PermissionDenied


class MiembrosView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    login_url = LOGIN_URL
    template_name = 'registros/miembros.html'
    context_object_name = 'latest_miembros_list'
    permission_required = 'registros.view_all_miembros'
    raise_exception = True  # 403 instead of login redirect

    def get_queryset(self):
        """Return all Miembros."""
        return Miembro.objects.all()


class MiembroDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    login_url = LOGIN_URL
    model = Miembro
    template_name = 'registros/miembro_detail.html'
    permission_required = 'registros.view_miembro'

    def get_object(self):
        """
        Return Miembro object only if user is that Miembro.
        """
        object = super(MiembroDetailView, self).get_object()
        if (object.pk == self.request.user.miembro.pk or 
                MAYOR_ACCESO_GROUP in self.request.user.groups.all()):
            return object
        else:
            raise PermissionDenied


class LegadosView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    login_url = LOGIN_URL
    template_name = 'registros/legados.html'
    context_object_name = 'latest_legados_list'
    permission_required = 'registros.view_legados'
    raise_exception = True  # 403 instead of login redirect

    def get_queryset(self):
        """Return all Legados."""
        return Legado.objects.all()


class LegadoDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    login_url = LOGIN_URL
    model = Legado
    template_name = 'registros/legado_detail.html'
    permission_required = 'registros.view_legados'
    raise_exception = True  # 403 instead of login redirect
