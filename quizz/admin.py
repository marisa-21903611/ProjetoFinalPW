from django.contrib import admin
from .models import Pergunta, Resposta, Quizz, Tentativa

# Register your models here.
admin.site.register(Pergunta)
admin.site.register(Resposta)
admin.site.register(Quizz)
admin.site.register(Tentativa)
