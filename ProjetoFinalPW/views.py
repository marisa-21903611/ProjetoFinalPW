from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Usuario, Comentario
from .forms import UsuarioFormulario, ComentarioFormulario

from django.views.generic import ListView

# Create your views here.

# Mapa
def mapa_page_view(request):
    return render(request, 'ProjetoFinalPW/mapa.html')


# Informacao
def informcao_page_view(request):
    return render(request, 'ProjetoFinalPW/informacao.html')


# Formulário
def formulario_page_view(request):
    form = ComentarioFormulario(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('formulario'))
    context = {'form': form}

    return render(request, 'ProjetoFinalPW/formulario.html',context)


# Index
def index_page_view(request):
    return render(request, 'ProjetoFinalPW/index.html')


# Mirazur
def mirazurIntroducao_page_view(request):
    return render(request, 'ProjetoFinalPW/mirazurIntroducao.html')


def mirazurCozinha_page_view(requeste):
    return render(requeste, 'ProjetoFinalPW/mirazurCozinha.html')


def mirazurPinteresse_page_view(requeste):
    return render(requeste, 'ProjetoFinalPW/mirazurPinteresse.html')


# Celler
def cellerIntroducao_page_view(request):
    return render(request, 'ProjetoFinalPW/cellerIntroducao.html')


def cellerCozinha_page_view(requeste):
    return render(requeste, 'ProjetoFinalPW/cellerCozinha.html')


def cellerPinteresse_page_view(requeste):
    return render(requeste, 'ProjetoFinalPW/cellerPinteresse.html')


# Noma
def nomaIntroducao_page_view(request):
    return render(request, 'ProjetoFinalPW/nomaIntroducao.html')


def nomaCozinha_page_view(requeste):
    return render(requeste, 'ProjetoFinalPW/nomaCozinha.html')


def nomaPinteresse_page_view(request):
    return render(request, 'ProjetoFinalPW/nomaPinteresse.html')


# Contacto
def contacto_page_view(request):
    context = {'ProjetoPW': Usuario.objects.all()}
    return render(request, 'ProjetoFinalPW/contacto.html', context)


def novo_contacto_view(request):
    form = UsuarioFormulario(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('ProjetoFinalPW:contacto'))

    context = {'form': form}

    return render(request, 'ProjetoFinalPW/listar.html', context)


def edita_contacto_view(request, usuario_id):
    usuario = Usuario.objects.get(id=usuario_id)
    form = UsuarioFormulario(request.POST or None, instance=usuario)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('ProjetoFinalPW:contacto'))

    context = {'form': form, 'usuario_id': usuario_id}
    return render(request, 'ProjetoFinalPW/edita.html', context)


def apaga_contacto_view(request, usuario_id):
    Usuario.objects.get(id=usuario_id.delete())
    return HttpResponseRedirect(reverse('ProjetoFinalPW:contacto'))