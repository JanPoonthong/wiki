from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:entry_title>", views.entry, name="entry"),
    path("wiki/<str:edit_entry>/edit", views.edit, name="edit"),
    path("newentry", views.newentry, name="newentry")
]
