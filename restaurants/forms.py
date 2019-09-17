# Customized fields for models
from django import forms

from .models import Usuario, ImagenesEstablecimiento

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        widgets = {
        'contrasena': forms.PasswordInput(),
    }

class ImageMultipleForm(forms.ModelForm):
    image = forms.ImageField(label='Imagen')    
    class Meta:
        model = ImagenesEstablecimiento
        fields = ('imagen', )