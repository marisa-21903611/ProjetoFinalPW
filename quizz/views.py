from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from quizz.forms import NovoQuizzFormulario, NovaPerguntaFormulario
from quizz.models import Resposta, Pergunta, Quizz, Tentativa
# Create your views here.

def quizz_view(request):
    context = {'quizzes': Quizz.objects.all(), 'perguntas': Pergunta.objects.all()}
    return render(request, 'quizz/quizz.html', context)

    form = NovoQuizzFormulario (request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse(''))
    context = {'form': form}

    return render(request, 'quizz/quizz.html', context)

def SubmitTentativa_view (request):
    user = request.user
    pontosGanhos = 0
    quizz_id = request.POST.get('quizz_id')
    quizz = Quizz.objects.get(id=quizz_id)

    r1 = int(request.POST.get('1'))
    r2 = int(request.POST.get('2'))
    r3 = int(request.POST.get('3'))
    r4 = int(request.POST.get('4'))

    if request.method == 'POST':
        pontos = r1 + r2 + r3 + r4

    t = Tentativa.objects.create(
        quizz=quizz,
        usuario=user,
        pontos=pontos
    )

    t.save()
    return redirect('ProjetoFinalPW/index.html')

def pontuacao_view(request):
    user = request.user
    quizzes = Quizz.objects.all()
    tentativas = Tentativa.objects.all()
    contagem = 0

    for tentativa in tentativas:
        if tentativa.usuario == user:
            contagem = contagem+1

    context = { 'quizz': quizzes, 'tentativas': tentativas,'contagem':contagem}
    return render (request, "quizz/pontuacao.html", context)