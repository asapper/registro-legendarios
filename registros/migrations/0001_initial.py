# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-01 22:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=254, unique=True)),
                ('descripcion', models.TextField()),
                ('tipo', models.CharField(choices=[('REC', 'REC'), ('RAC', 'RAC'), ('RIO', 'RIO'), ('Legado', 'Legado')], max_length=50)),
                ('fecha', models.DateField()),
                ('pais', models.CharField(max_length=100)),
                ('localidad', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Legado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('fecha_de_nacimiento', models.DateField()),
                ('tipo', models.CharField(choices=[('Osos', 'Osos'), ('Jaguares', 'Jaguares'), ('Águilas', 'Águilas')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Miembro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('fecha_de_nacimiento', models.DateField()),
                ('correo', models.EmailField(max_length=254)),
                ('telefono', models.CharField(max_length=25)),
                ('foto', models.ImageField(upload_to='')),
                ('tipo_de_sangre', models.CharField(max_length=25)),
                ('estado_civil', models.CharField(max_length=50)),
                ('pais', models.CharField(max_length=100)),
                ('numero_de_legendario', models.PositiveIntegerField()),
                ('testimonio', models.TextField()),
                ('estatus', models.CharField(choices=[('activo', 'Activo'), ('inactivo', 'Inactivo')], max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Participacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rol', models.CharField(choices=[('Participante', 'Participante'), ('Coordinación', 'Coordinación'), ('Sub Coordinación', 'Sub Coordinación'), ('Administración', 'Administración'), ('Jefe de Tribu', 'Jefe de Tribu'), ('Voz', 'Voz'), ('Logística', 'Logística'), ('Evento', 'Evento'), ('Seguridad', 'Seguridad'), ('Apoyo', 'Apoyo')], max_length=50)),
                ('descripcion', models.TextField()),
                ('evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registros.Evento')),
                ('miembro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registros.Miembro')),
            ],
        ),
        migrations.AddField(
            model_name='evento',
            name='miembros',
            field=models.ManyToManyField(through='registros.Participacion', to='registros.Miembro'),
        ),
    ]
