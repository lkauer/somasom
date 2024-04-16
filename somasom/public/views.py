from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from artist.models import Artist
from release.models import Release
from .forms import SearchForm
from django.shortcuts import get_object_or_404


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
    if request.method == "GET":
        form = SearchForm(request.GET)
        if form.is_valid():
            try:
                artist_list = Artist.objects.get(nm_artist__contains=form.cleaned_data["search"])
                status = "ok"
                artist_iter = hasattr(artist_list, '__iter__')
            except Artist.DoesNotExist:
                artist_list = None
                status = "Ninguem colou aqui"
                artist_iter = False

            try:
                release_list = Release.objects.get(nm_release__contains=form.cleaned_data["search"])
                status = "ok"
                release_iter = hasattr(release_list, '__iter__')
            except Release.DoesNotExist:
                release_list = None
                status = "Ninguem colou aqui"
                release_iter = False

            context = {
                "artist_list" : artist_list,
                "artist_iter" : artist_iter,
                "release_list": release_list,
                "release_iter" : release_iter,
                "status" : status,
                "search" : form.cleaned_data["search"]
            }
        else:
            context = {}   
    return HttpResponse(template.render(context, request))

def manifest(request):
    template = loader.get_template("public/manifest.html")
    context = {
        
    }
    return HttpResponse(template.render(context, request))

