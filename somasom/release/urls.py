from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("song/<slug:id_release>", views.song, name="song"),
    path("album/<slug:id_release>", views.album, name="album"),
]