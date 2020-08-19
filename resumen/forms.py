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


class RegistroNomina(forms.Form):
    
    nombre  = forms.CharField(max_length=20, label='Nomina',
                            required=True, help_text='ORDINARIA',
                            widget=forms.TextInput())
    anno  = forms.CharField(label="Año", 
                            required=True,max_length=4, 
                            help_text='2020',widget=forms.TextInput())
    periodo  = forms.CharField(label="Periodo",
                                required=True, max_length=2,
                                help_text='01', widget=forms.TextInput())
    id_ejecucion  = forms.CharField(max_length=20, label="ID Ejecucion",
                                    required=True, help_text='ZN',
                                    widget=forms.TextInput())
    fecha_pago = forms.CharField(max_length=10, label="Fecha de Pago",
                                    required=True, help_text='14/01/2020',
                                    widget=forms.TextInput()) 
    num_xml = forms.IntegerField(label="No. XML´S",
                                required=True, help_text='1589'
                                )
    importe_isr  = forms.FloatField(label="Importe ISR",
                                    widget=forms.NumberInput(),
                                    required=True,help_text='31566689.01'
                                )
    isr_retim  = forms.FloatField(label="Importe Retimbre",
                                    widget=forms.NumberInput(),
                                required=True, help_text='2476.24'
                                )    
    comentario  = forms.CharField(label="Comentarios",
                                required=True, help_text='TEXTO....',
                                widget=forms.Textarea(attrs={'class' : 'in-comentario'}),
                                max_length=300)
    modificado_por = forms.CharField(max_length=8,label="Modificado Por",
                                    widget=forms.TextInput(attrs={'id' : 'usuario'}), 
                                    disabled=True, required=False)
    fecha_mod  = forms.DateTimeField(label="Ultima Modificación", 
                                    disabled=True, required=False,
                                    widget=forms.DateTimeInput(attrs={'id' : 'fecha-mod'}),
                                    input_formats='%Y-%m-%d %H:%M')

    def __init__(self, *args, **kwargs):
        super(RegistroNomina, self).__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['placeholder'] = 'HONORARIOS'
        self.fields['anno'].widget.attrs['placeholder'] = '2020'
        self.fields['periodo'].widget.attrs['placeholder'] = '01'
        self.fields['id_ejecucion'].widget.attrs['placeholder'] = 'ZH_ZHON_A414012020'
        self.fields['fecha_pago'].widget.attrs['placeholder'] = '14012020'
        

