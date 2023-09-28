from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from artist.models import Artist
from release.models import Release

def index(request):
    artist_list = Artist.objects.all()
    release_list = Release.objects.all()
    template = loader.get_template("public/index.html")
    context = {
        "artist_list": artist_list,
        "release_list": release_list,
    }
    return HttpResponse(template.render(context, request))

def search(request):
    template = loader.get_template("public/search.html")
    context = {
        
    }
    return HttpResponse(template.render(context, request))

def manifest(request):
    template = loader.get_template("public/manifest.html")
    context = {
        
    }
    return HttpResponse(template.render(context, request))
