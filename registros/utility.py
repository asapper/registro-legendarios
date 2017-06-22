from django.contrib.auth.models import Group, User

from .models import Evento, Miembro, Participacion

class MainController():
    # columns for CSV file
    NOMBRES_CSV = 'nombres'
    APELLIDOS_CSV = 'apellidos'
    CORREO_CSV = 'correo'
    NUM_LGND_CSV = 'numero_lgnd'
    ROL_CSV = 'rol'
    DESC_CSV = 'descripcion'
    # field names in CSV file
    FIELDNAMES_CSV = [
            NOMBRES_CSV, APELLIDOS_CSV, CORREO_CSV, NUM_LGND_CSV,
            ROL_CSV, DESC_CSV]

    @classmethod
    def create_new_miembro(cls, form):
        user = User.objects.create_user(
                username=form.cleaned_data['correo'],
                password=form.cleaned_data['contraseña1'])
        miembro = Miembro.objects.create(
                nombre=form.cleaned_data['nombre'],
                apellido=form.cleaned_data['apellido'],
                correo=form.cleaned_data['correo'],
                numero_de_legendario=form.cleaned_data['numero_de_legendario'],
                user=user)
        miembro.save()
        # assign basic group to new User
        cls._assign_user_basic_group(user)
        return user

    @classmethod
    def _assign_user_basic_group(cls, user):
        # get Legendario group
        legendario_group = Group.objects.get(name='Legendario')
        # add user to group
        user.groups.add(legendario_group)

    @classmethod
    def nuevos_miembros_csv(cls, dict_miembros, evento_id):
        """
        Asigna miembros al evento indicado.
        Si el miembro no exise, uno nuevo es creado.
        De lo contrario, el miembro existente es usado.
        """
        for row in dict_miembros:
            # create User or retrieve it if it already exists
            user, created_user = User.objects.get_or_create(
                username=row[cls.CORREO_CSV])
            # assign password if new User
            if created_user is True:
                user.set_password(User.objects.make_random_password())
                user.save()
            # create Miembro or retrieve it if it already exists
            miembro, created_miembro = Miembro.objects.get_or_create(
                nombre=row[cls.NOMBRES_CSV],
                apellido=row[cls.APELLIDOS_CSV],
                correo=row[cls.CORREO_CSV],
                numero_de_legendario=row[cls.NUM_LGND_CSV],
                user=user)
            # assign basic group if new User
            if created_user is True:
                cls._assign_user_basic_group(user)
            # retrieve evento instance
            evento = Evento.objects.get(pk=evento_id)
            # create Participacion instance
            Participacion.objects.get_or_create(
                miembro=miembro,
                evento=evento,
                rol=row[cls.ROL_CSV],
                descripcion=row[cls.DESC_CSV])
