from django import forms
from .models import VehiculoModel

class VehiculoForm(forms.ModelForm):
 # specify the name of model to use
    class Meta:
        model = VehiculoModel
        fields = ['marca', 'modelo', 'serial_carroceria', 'serial_motor', 'categoria', 'precio']
