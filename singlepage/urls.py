from django.urls import path

from . import views

app_name = "singlepage"

urlpatterns = [
    path("", views.index, name="index"),
    path("sections/<int:num>", views.section, name="section")
]