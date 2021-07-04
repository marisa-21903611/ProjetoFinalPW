from django import forms
from .models import Usuario, Comentario

class UsuarioFormulario(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ["nome", "apelido", "telefone", "email", "dataNascimento"]

class ComentarioFormulario(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = '__all__'