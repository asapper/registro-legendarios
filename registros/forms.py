# -*- coding: utf-8 -*-
from django import forms

from .models import Miembro


class MiembroForm(forms.ModelForm):
    contrasena1 = forms.CharField(min_length=8, max_length=25,
                                  widget=forms.PasswordInput,
                                  label='Contraseña')
    contrasena2 = forms.CharField(min_length=8, max_length=25,
                                  widget=forms.PasswordInput,
                                  label='Confirma tu contraseña')

    class Meta:
        model = Miembro
        fields = ['nombre', 'apellido', 'correo', 'numero_de_legendario']

    def clean(self):
        MIN_LENGTH = 8
        # get cleaned data
        cleaned_data = super(MiembroForm, self).clean()
        contrasena1 = cleaned_data.get('contrasena1')
        contrasena2 = cleaned_data.get('contrasena2')
        # check passwords match
        if contrasena1 and contrasena2:
            if contrasena1 != contrasena2:
                raise forms.ValidationError('Las contraseñas no coinciden.')
        # check password strength
        if len(contrasena1) < MIN_LENGTH:
            raise forms.ValidationError(
                    'La contraseña debe tener 8 caracteres o más.')
        if all(char.isalpha() for char in contrasena1):
            raise forms.ValidationError(
                    ('La contraseña debe contener una combinación de \
                     letras y al menos un número (a-z, A-Z, 0-9).'))
