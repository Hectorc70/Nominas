from django import forms
from django.forms import Textarea

from usuarios.models import Usuario
from resumen.models import Nomina


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
        

class NominaForm(forms.ModelForm):

    class Meta:
        model = Nomina
        fields = '__all__'
        widgets = {
            'comentario': Textarea(attrs={'cols': 80, 'rows': 20}),
        }
    
    def __init__(self, *args, **kwargs):
        super(NominaForm, self).__init__(*args, **kwargs)
        self.fields['fecha_mod'].widget.attrs.update({
                                            'class':'fecha-mod',
                                            'readonly': 'True',
        })
        self.fields['fecha_mod'].required = False
        self.fields['mod_usuario'].widget.attrs.update({
                                            'class':'usuario',
                                            'readonly': 'True',
        }) 
        self.fields['mod_usuario'].required = False 
        self.fields['nombre'].widget.attrs['placeholder'] = 'HONORARIOS'
        self.fields['anno'].widget.attrs['placeholder'] = '2020'
        self.fields['periodo'].widget.attrs['placeholder'] = '01'
        self.fields['id_ejecucion'].widget.attrs['placeholder'] = 'ZH_ZHON_A414012020'
        self.fields['fecha_pago'].widget.attrs['placeholder'] = '14012020'
        self.fields['comentario'].required = False
        self.fields['comentario'].widget.attrs.update({
                                            'class':'in-comentario',
        }) 