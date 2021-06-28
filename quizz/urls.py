from django.shortcuts import render
from django.urls import path
from . import views

app_name = "quizz"

urlpatterns = [
    path('', views.quizz_view, name="quizz"),
    path('submit/', views.SubmitTentativa_view, name="submeter"),
    path('pontuacao/', views.pontuacao_view, name="pontuacao"),
]