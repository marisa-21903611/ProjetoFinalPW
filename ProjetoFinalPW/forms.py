from django import forms
from .models import Usuario, Comentario

class UsuarioFormulario(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ["nome", "apelido", "telefone", "email", "dataNascimento"]

        help_texts = {
            'telefone' : '+351 XXX XXX XXX'
        }

class ComentarioFormulario(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = '__all__'

        labels = {
           'clareza' : 'Classifique quanto à Clareza',
            'rigor' : 'Classifique quanto ao Rigor',
            'profundidade' : 'Classifique quanto à Profundida',
            'layout' : 'Classifique quanto ao Layout',
            'logica' : 'Classifique quanto à Lógica',
            'estrutura' : 'Classifique quanto à Estrutura',
            'originalidade' : 'Classifique quanto à Originalidade',
            'cores' : 'Classifique quanto às Cores',
            'animacoes': 'Classifique as Animações usadas',
        }