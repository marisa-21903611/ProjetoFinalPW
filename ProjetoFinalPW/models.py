from django.db import models

# Create your models here.
class Usuario(models.Model):
    nome = models.CharField(max_length=30, null=False)
    apelido = models.CharField(max_length=30, null=False)
    telefone = models.CharField(max_length=9, null=False)
    email = models.EmailField(null=False)
    dataNascimento = models.DateTimeField(null=False)

    def __str__(self):
        return f"{self.nome} {self.apelido} {self.telefone} {self.email} {self.dataNascimento}"

COMENTARIO_CHOICES = [
    (1, 'O site está horrível'),
    (2, 'O site está mau '),
    (3, 'O site está aceitável'),
    (4, 'O site está bom'),
    (5, 'O site está excelente'),
]
class Comentario(models.Model):
    clareza = models.IntegerField(choices=COMENTARIO_CHOICES,default=3)
    rigor = models.IntegerField(choices=COMENTARIO_CHOICES,default=3)
    profundidade = models.IntegerField(choices=COMENTARIO_CHOICES,default=3)
    layout = models.IntegerField(choices=COMENTARIO_CHOICES,default=3)
    logica = models.IntegerField(choices=COMENTARIO_CHOICES,default=3)
    estrutura = models.IntegerField(choices=COMENTARIO_CHOICES,default=3)
    originalidade = models.IntegerField(choices=COMENTARIO_CHOICES,default=3)
    cores = models.IntegerField(choices=COMENTARIO_CHOICES,default=3)
    animacoes = models.IntegerField(choices=COMENTARIO_CHOICES,default=3)