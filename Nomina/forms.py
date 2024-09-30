from django import forms
from .models import Afiliado

class AfiliadoForm(forms.ModelForm):
    class Meta:
        model = Afiliado
        # fields = "__all__"
        fields = ['nombre', 'apellido', 'cuil', 'dni', 'sexo', 
                  'nro_afiliado', 'email', 'telefono', 'nacimiento', 
                  'calle', 'nro', 'piso', 'localidad']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'cuil': forms.NumberInput(attrs={'class': 'form-control form-control-sm'}),
            'dni': forms.NumberInput(attrs={'class': 'form-control form-control-sm'}),
            'sexo': forms.Select(choices=[('M', 'M'), ('F', 'F'), ('X', 'X'), ], attrs={'class': 'form-control form-control-sm'}),
            'nro_afiliado': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'disabled': 'disabled'}),
            'email': forms.EmailInput(attrs={'class': 'form-control form-control-sm'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'nacimiento': forms.DateInput(attrs={'class': 'form-control form-control-sm', 'type': 'date'}),
            'calle': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'nro': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'piso': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'localidad': forms.Select(attrs={'class': 'form-control form-control-sm'}),
        }