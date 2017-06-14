from django import forms

from .models import Miembro


class MiembroForm(forms.ModelForm):
    contraseña1 = forms.CharField(min_length=8, max_length=25,
                                  widget=forms.PasswordInput,
                                  label='Contraseña')
    contraseña2 = forms.CharField(min_length=8, max_length=25,
                                  widget=forms.PasswordInput,
                                  label='Confirma tu contraseña')

    class Meta:
        model = Miembro
        fields = ['nombre', 'apellido', 'correo', 'numero_de_legendario']

    def clean(self):
        cleaned_data = super(MiembroForm, self).clean()
        contraseña1 = cleaned_data.get('contraseña1')
        contraseña2 = cleaned_data.get('contraseña2')
        # check passwords match
        if contraseña1 and contraseña2:
            if contraseña1 != contraseña2:
                raise forms.ValidationError('Las contraseñas no coinciden.')
