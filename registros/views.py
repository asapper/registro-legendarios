import codecs, csv

from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        UserPassesTestMixin,
                                        PermissionRequiredMixin)
from django.contrib.auth.models import Group, User
from django.contrib.messages.views import SuccessMessageMixin
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import DetailView, ListView
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView, UpdateView

from .forms import MiembroForm
from .models import Evento, Miembro, Legado
from .utility import MainController

LOGIN_URL = '/login/'
MAYOR_ACCESO_GROUP = Group.objects.get(name='Mayor acceso usuario')


def home_view(request):
    """This view redirects to the logged-in user's profile page."""
    return redirect(reverse('registros:miembro_detail',
                    kwargs={'pk': request.user.miembro.pk}))


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
        return Evento.objects.all()


class EventoDetailView(LoginRequiredMixin,
                       PermissionRequiredMixin, DetailView):
    login_url = LOGIN_URL
    model = Evento
    template_name = 'registros/evento_detail.html'
    permission_required = 'registros.view_eventos'

    def post(self, *args, **kwargs):
        # archivo subido por el usuario
        miembros_file = self.request.FILES['archivo_miembros']
        # lee csv y lo guarda en Dict
        reader = csv.DictReader(codecs.iterdecode(miembros_file, "utf-8"),
                fieldnames=MainController.FIELDNAMES_CSV)
        # handle creation/assigning of miembros
        object_pk = self.kwargs['pk']
        MainController.nuevos_miembros_csv(reader, object_pk)
        # add alert for user
        messages.success(self.request, 'Miembros añadidos exitosamente')
        return redirect(reverse('registros:evento_detail',
                        kwargs={'pk': object_pk}))


class MiembrosView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    login_url = LOGIN_URL
    template_name = 'registros/miembros.html'
    context_object_name = 'latest_miembros_list'
    permission_required = 'registros.view_all_miembros'
    raise_exception = True  # 403 instead of login redirect

    def get_queryset(self):
        """Return all Miembros."""
        return Miembro.objects.all()


class NuevoMiembroView(SuccessMessageMixin, FormView):
    template_name = 'registros/registro_nuevo_miembro.html'
    form_class = MiembroForm
    success_url = '/registros/'
    success_message = 'Has sido registrado correctamente'

    def form_valid(self, form):
        """
        Create User and Miembro based on data provided.
        """
        # handle creation of new member
        user = MainController.create_new_miembro(form)
        # log user in
        login(self.request, user)
        return super(NuevoMiembroView, self).form_valid(form)


class MiembroUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Miembro
    fields = ['nombre', 'apellido', 'fecha_de_nacimiento', 'correo',
            'telefono', 'foto', 'tipo_de_sangre', 'estado_civil',
            'pais', 'testimonio', 'congregacion']
    template_name_suffix = '_update_form'
    success_message = 'Tu perfil ha sido actualizado exitosamente.'

    def get_object(self):
        """
        Allow editing only if user is this Miembro.
        """
        object = super(MiembroUpdateView, self).get_object()
        if object.pk == self.request.user.miembro.pk:
            return object
        else:
            raise PermissionDenied

    def get_success_url(self):
        """Redirect back to Profile page."""
        return reverse('registros:miembro_detail',
                    kwargs={'pk': self.request.user.miembro.pk})


class MiembroDetailView(LoginRequiredMixin,
                        PermissionRequiredMixin, DetailView):
    login_url = LOGIN_URL
    model = Miembro
    template_name = 'registros/miembro_detail.html'
    permission_required = 'registros.view_all_miembros'


class LegadosView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    login_url = LOGIN_URL
    template_name = 'registros/legados.html'
    context_object_name = 'latest_legados_list'
    permission_required = 'registros.view_legados'
    raise_exception = True  # 403 instead of login redirect

    def get_queryset(self):
        """Return all Legados."""
        return Legado.objects.all()


class LegadoDetailView(LoginRequiredMixin,
                       PermissionRequiredMixin, DetailView):
    login_url = LOGIN_URL
    model = Legado
    template_name = 'registros/legado_detail.html'
    permission_required = 'registros.view_legados'
    raise_exception = True  # 403 instead of login redirect
