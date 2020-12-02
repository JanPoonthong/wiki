from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("CSS", views.CSS, name="CSS"),
    path("Django", views.Django, name="Django"),
    path("HTML", views.HTML, name="HTML"),
    path("Git", views.Git, name="Git"),
    path("Python", views.Python, name="Python")
]
