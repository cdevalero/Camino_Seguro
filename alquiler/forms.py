from django import forms
from .models import *

class FormLugarDir(forms.ModelForm):
    class Meta:
        model = Lugares_Dir;
        fields = ('nombre', 'tipo', 'id_lugar')

class FromOficinas(forms.ModelForm):
    class Meta:
        model = Oficinas;
        fields = ('nombre', 'calleav', 'id_ciudad')

    def __init__(self, ciudad, *args, **kwargs):
        super(FromOficinas, self).__init__(*args, **kwargs)
        self.fields['id_ciudad'].queryset = Lugares_Dir.objects.filter(tipo=ciudad)
