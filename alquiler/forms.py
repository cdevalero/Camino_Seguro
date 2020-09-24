from django import forms
from django.forms import DateInput
from .models import *

class FormLugarDir(forms.ModelForm):
    class Meta:
        model = Lugares_Dir;
        fields = ('nombre', 'tipo', 'id_lugar')
    def __init__(self, *args, **kwargs):
        super(FormLugarDir, self).__init__(*args, **kwargs)
        self.fields['id_lugar'].queryset = Lugares_Dir.objects.filter(tipo='e')

class FormOficinas(forms.ModelForm):
    class Meta:
        model = Oficinas;
        fields = ('nombre', 'calleav', 'id_ciudad')

    def __init__(self, ciudad, *args, **kwargs):
        super(FormOficinas, self).__init__(*args, **kwargs)
        self.fields['id_ciudad'].queryset = Lugares_Dir.objects.filter(tipo=ciudad)

class FormCompanias(forms.ModelForm):
    class Meta:
        model = Companias;
        fields = ('codigo','nombre', 'calleav', 'id_ciudad')

    def __init__(self, ciudad, *args, **kwargs):
        super(FormCompanias, self).__init__(*args, **kwargs)
        self.fields['id_ciudad'].queryset = Lugares_Dir.objects.filter(tipo=ciudad)

class FormParticulares(forms.ModelForm):
    class Meta:
        model = Particulares;
        fields = ('dni','nombre', 'apellido1', 'apellido2','calleav','tip_lic','fecha_exp','riesgo','id_ciudad')
        widgets = {
            'fecha_exp': DateInput(attrs={'type': 'date'})
        }

    def __init__(self, ciudad, *args, **kwargs):
        super(FormParticulares, self).__init__(*args, **kwargs)
        self.fields['id_ciudad'].queryset = Lugares_Dir.objects.filter(tipo=ciudad)

class FormCamiones(forms.ModelForm):
    class Meta:
        model = Camiones;
        fields = ('num_registro', 'fecha_exp', 'fecha_man','tammts','km','capacidad','radio','id_oficina')
        widgets = {
            'fecha_exp': DateInput(attrs={'type': 'date'}),
            'fecha_man': DateInput(attrs={'type': 'date'})
        }

class FormRemolques(forms.ModelForm):
    class Meta:
        model = Remolques;
        fields = ('num_registro', 'fecha_exp', 'fecha_man','tammts','material','abierto','id_oficina')
        widgets = {
            'fecha_exp': DateInput(attrs={'type': 'date'}),
            'fecha_man': DateInput(attrs={'type': 'date'})
        }

class FormContratos(forms.ModelForm):
    class Meta:
        model = Contrartos;
        fields = ('fecha_alquiler', 'dura', 'deposito','tar_dia','id_ofic_origen','id_ofic_destino','id_camion','id_remolque','id_compa','id_per')
        widgets = {
            'fecha_alquiler': DateInput(attrs={'type': 'date'})
        }

class FormParticulares_cliente(forms.ModelForm):
    class Meta:
        model = Particulares;
        fields = ('dni','nombre', 'apellido1', 'apellido2','calleav','tip_lic','fecha_exp','id_ciudad')
        widgets = {
            'fecha_exp': DateInput(attrs={'type': 'date'})
        }

    def __init__(self, ciudad, *args, **kwargs):
        super(FormParticulares_cliente, self).__init__(*args, **kwargs)
        self.fields['id_ciudad'].queryset = Lugares_Dir.objects.filter(tipo=ciudad)

class FormParticulares_inicio(forms.Form):
    dni = forms.IntegerField()

class FormPedido(forms.Form):
    pass

