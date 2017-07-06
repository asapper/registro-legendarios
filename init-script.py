from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

from registros.models import Miembro, Evento, Participacion, Legado

# get or create groups
mayor_group, mayor_created = Group.objects.get_or_create(name='Mayor acceso usuario')
lgnd_group, lgnd_created = Group.objects.get_or_create(name='Legendario')
lider_group, lider_created = Group.objects.get_or_create(name='Lider')

if mayor_created is True or lgnd_created is True or lider_created is True:
    # get content types
    evento_ct = ContentType.objects.get_for_model(Evento)
    miembro_ct = ContentType.objects.get_for_model(Miembro)
    participacion_ct = ContentType.objects.get_for_model(Participacion)
    legado_ct = ContentType.objects.get_for_model(Legado)

    # create permissions and assign to groups
    ## Legado
    legado_perm_view = Permission.objects.create(codename='view_legados', name='Can view legados', content_type=legado_ct)
    legado_perm_add = Permission.objects.get(name='Can add legado')
    legado_perm_change = Permission.objects.get(name='Can change legado')
    ## Evento
    evento_perm_view = Permission.objects.create(codename='view_eventos', name='Can view eventos', content_type=evento_ct)
    evento_perm_add_miembros = Permission.objects.create(codename='add_miembros', name='Can add miembros to Evento', content_type=evento_ct)
    evento_perm_add = Permission.objects.get(name='Can add evento')
    evento_perm_change = Permission.objects.get(name='Can change evento')
    ## Miembro
    miembro_perm_view_all = Permission.objects.create(codename='view_all_miembros', name='Can view all miembros', content_type=miembro_ct)
    miembro_perm_view_detail = Permission.objects.create(codename='view_miembro_detail', name='Can view miembro detail', content_type=miembro_ct)
    miembro_perm_add = Permission.objects.get(name='Can add miembro')
    miembro_perm_change = Permission.objects.get(name='Can change miembro')
    ## Group
    group_perm_add = Permission.objects.get(name='Can add group')
    group_perm_change = Permission.objects.get(name='Can change group')
    ## User
    user_perm_change = Permission.objects.get(name='Can change user')
    ## Participacion
    participacion_perm_add = Permission.objects.get(name='Can add participacion')
    participacion_perm_change = Permission.objects.get(name='Can change participacion')

    # assign permissions per group
    ## Mayor acceso usuario
    mayor_group.permissions.add(group_perm_add)
    mayor_group.permissions.add(group_perm_change)
    mayor_group.permissions.add(user_perm_change)
    mayor_group.permissions.add(evento_perm_add)
    mayor_group.permissions.add(evento_perm_change)
    mayor_group.permissions.add(evento_perm_add_miembros)
    mayor_group.permissions.add(evento_perm_view)
    mayor_group.permissions.add(legado_perm_add)
    mayor_group.permissions.add(legado_perm_change)
    mayor_group.permissions.add(legado_perm_view)
    mayor_group.permissions.add(miembro_perm_add)
    mayor_group.permissions.add(miembro_perm_change)
    mayor_group.permissions.add(miembro_perm_view_all)
    mayor_group.permissions.add(miembro_perm_view_detail)
    mayor_group.permissions.add(participacion_perm_add)
    mayor_group.permissions.add(participacion_perm_change)
    ## Lider
    lider_group.permissions.add(evento_perm_view)
    lider_group.permissions.add(miembro_perm_view_all)
    lider_group.permissions.add(miembro_perm_view_detail)
    ## Legendario
    lgnd_group.permissions.add(evento_perm_view)
    lgnd_group.permissions.add(miembro_perm_view_all)
