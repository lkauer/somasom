from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import Http404


def index(request):
    template = loader.get_template("release/index.html")
    context = {
        
    }
    return HttpResponse(template.render(context, request))

def song(request, release_id):
    
    template = loader.get_template("release/song_id.html")
    context = {
        "releasea" : release_id
    }

    # try:
        # something
    # except Question.DoesNotExist:
        # raise Http404("Question does not exist")
    return HttpResponse(template.render(context, request))

def album(request, release_id):
    
    template = loader.get_template("release/album_id.html")
    context = {
        "releasea" : release_id
    }

    # try:
        # something
    # except Question.DoesNotExist:
        # raise Http404("Question does not exist")
    return HttpResponse(template.render(context, request))