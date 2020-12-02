from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.search, name="search"),
    path("edit/<str:edit_title>", views.edit_page, name="edit_page")
]
