from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("song/<int:release_id>", views.song, name="song"),
    path("album/<int:release_id>", views.album, name="album"),
]