# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views


app_name = 'registros'
urlpatterns = [
    # ex: /registros/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # ex: /nuevo-miembro/
    url(r'^nuevo-miembro/$', views.NuevoMiembroView.as_view(), name='nuevo-miembro'),
    # ex: /registros/home
    url(r'^home/$', views.home_view, name='home'),
    # ex: /registros/eventos/
    url(r'^eventos/$', views.EventosView.as_view(), name='eventos'),
    # ex: /registros/eventos/1/
    url(r'^eventos/(?P<pk>[0-9]+)/$', views.EventoDetailView.as_view(), name='evento_detail'),
    # ex: /registros/miembros/
    url(r'^miembros/$', views.MiembrosView.as_view(), name='miembros'),
    # ex: /registros/miembros/1/
    url(r'^miembros/(?P<pk>[0-9]+)/$', views.MiembroDetailView.as_view(), name='miembro_detail'),
    # ex: /registros/miembros/1/editar
    url(r'^miembros/(?P<pk>[0-9]+)/editar/$', views.MiembroUpdateView.as_view(), name='miembro_update'),
    # ex: /registros/legados/
    url(r'^legados/$', views.LegadosView.as_view(), name='legados'),
    # ex: /registros/legados/1/
    url(r'^legados/(?P<pk>[0-9]+)/$', views.LegadoDetailView.as_view(), name='legado_detail'),
]

if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
