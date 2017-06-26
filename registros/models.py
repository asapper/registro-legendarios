from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Legado(models.Model):
    OPCIONES_LEGADO = (
        ('Osos', 'Osos'),
        ('Jaguares', 'Jaguares'),
        ('Águilas', 'Águilas'),
    )

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_de_nacimiento = models.DateField()
    tipo = models.CharField(max_length=50, choices=OPCIONES_LEGADO)

    def __str__(self):
        return "{} {}".format(self.nombre, self.apellido)


class Miembro(models.Model):
    OPCIONES_ESTATUS = (
        ('activo', 'Activo'),
        ('inactivo', 'Inactivo'),
    )

    # referencia a login credentials
    user = models.OneToOneField(User)
    # datos de miembro
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_de_nacimiento = models.DateField(null=True)  # not required upon registration
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=25, default="")
    foto = models.ImageField(upload_to="miembros/", null=True)
    tipo_de_sangre = models.CharField(max_length=25, default="")
    estado_civil = models.CharField(max_length=50, default="")
    pais = models.CharField(max_length=100, default="")
    congregacion = models.CharField(max_length=100, default="")
    numero_de_legendario = models.PositiveIntegerField(unique=True)
    testimonio = models.TextField(default="")
    estatus = models.CharField(max_length=25, choices=OPCIONES_ESTATUS, default='activo')
    # links for social networks
    facebook_link = models.URLField(default="", blank=True)
    instagram_link = models.URLField(default="", blank=True)
    twitter_link = models.URLField(default="", blank=True)

    def __str__(self):
        return "{} {}".format(self.nombre, self.apellido)


class Evento(models.Model):
    OPCIONES_TIPO = (
        ('REC', 'REC'),
        ('RAC', 'RAC'),
        ('RIO', 'RIO'),
        ('Legado', 'Legado'),
    )

    nombre = models.CharField(unique=True, max_length=254)
    descripcion = models.TextField()
    tipo = models.CharField(max_length=50, choices=OPCIONES_TIPO)
    fecha = models.DateField()
    pais = models.CharField(max_length=100)
    localidad = models.CharField(max_length=100)
    badge = models.ImageField(upload_to="eventos/")
    miembros = models.ManyToManyField(Miembro, through='Participacion')

    def __str__(self):
        return self.nombre


class Participacion(models.Model):
    OPCIONES_ROL = (
        ('Participante', 'Participante'),
        ('Coordinación', 'Coordinación'),
        ('Sub Coordinación', 'Sub Coordinación'),
        ('Administración', 'Administración'),
        ('Jefe de Tribu', 'Jefe de Tribu'),
        ('Voz', 'Voz'),
        ('Logística', 'Logística'),
        ('Evento', 'Evento'),
        ('Seguridad', 'Seguridad'),
        ('Apoyo', 'Apoyo'),
    )

    miembro = models.ForeignKey(Miembro)
    evento = models.ForeignKey(Evento)
    rol = models.CharField(max_length=50, choices=OPCIONES_ROL)
    descripcion = models.TextField()

    class Meta:
        verbose_name_plural = 'Participaciones'

    def __str__(self):
        return "{} - {}".format(self.miembro, self.evento)
