# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-03 18:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0002_auto_20170601_1723'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='badge',
            field=models.ImageField(default='miembros/GOPR0046.JPG', upload_to='eventos/'),
            preserve_default=False,
        ),
    ]