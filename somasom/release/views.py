from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from .models import Release
from artist.models import Artist

def index(request):
    release_list = Release.objects.all()
    template = loader.get_template("release/index.html")
    context = {
        "release_list" : release_list
    }
    return HttpResponse(template.render(context, request))

def song(request, id_release):
    release = Release.objects.get(pk=id_release)
    artist = Artist.get_artist_by_id(release.artist)

    template = loader.get_template("release/song_id.html")
    context = {
        "release" : release,
        "artist" : artist
    }
    return HttpResponse(template.render(context, request))

def album(request, id_release):
    
    release = Release.objects.get(pk=id_release)
    artist = Artist.get_artist_by_id(release.artist)
    template = loader.get_template("release/album_id.html")
    context = {
        "release" : release,
        "artist" : artist
    }
    return HttpResponse(template.render(context, request))