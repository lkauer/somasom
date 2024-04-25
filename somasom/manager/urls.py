from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("artist", views.artist, name="artist"),
    path("release", views.release, name="release"),
    path("create_artist", views.create_artist, name="create_artist"),
    path("create_release", views.create_release, name="create_release"),
    path("edit_artist", views.edit_artist, name="edit_artist"),
]