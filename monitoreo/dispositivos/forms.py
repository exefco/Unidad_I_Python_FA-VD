from django import forms
from .models import Dispositivo

class DispositivoForm(forms.ModelForm):
    class Meta:
        model = Dispositivo
        fields = '__all__'
        widgets = {
            'nombre' : forms.TextInput(attrs={'class':'form-control'}),
            'consumo_maximo' : forms.TextInput(attrs={'class': 'form-control'}),
            'categoria' : forms.Select(attrs={'class' : 'form-select'}),
            'zona' : forms.Select(attrs={'class' : 'form-select'}),
            'estado' : forms.TextInput(attrs={'class' : 'form-select'}),
        }
    
    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre') #Valor ingresado por el usuario cleaned_data es un diccionario para acceder a los datos limpios.

        if len(nombre) < 3: #Validación de Caracteres por nombre
            raise forms.ValidationError('El nombre debe tener al menos 3 caracteres')
        
        return nombre
