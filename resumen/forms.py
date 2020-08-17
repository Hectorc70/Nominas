from django import forms

from usuarios.models import Usuario


class RegistroForm(forms.Form):

    control     = forms.CharField(label='Numero de Control', required=True, 
                                  max_length=8, widget=forms.TextInput())

    name        = forms.CharField(label='Nombre', required=True, max_length=50,
                                  widget=forms.TextInput())

    last_name   = forms.CharField(label='Apellido Paterno', required=True, 
                                 max_length=50, widget=forms.TextInput())

    last_second_name = forms.CharField(label='Apellido Materno', required=False, 
                                       max_length=50, widget=forms.TextInput())

    email       = forms.EmailField(label='Correo Electronico', required=True, 
                                    widget=forms.EmailInput())

    password    = forms.CharField(label='Contraseña', required=True, 
                                min_length=5, widget=forms.PasswordInput())

    password_2  = forms.CharField(label='Repetir Contraseña', required=True, 
                                min_length=5, widget=forms.PasswordInput())


    def clean_control(self):
        control = self.cleaned_data.get('control')

        if Usuario.objects.filter(control=control).exists():
            raise forms.ValidationError('Ya existe el Usuario')
        
        return control                            