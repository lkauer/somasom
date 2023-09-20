from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from .models import Artist


def index(request):
    artist_list = Artist.objects.all()
    template = loader.get_template("artist/index.html")
    context = {
        "artist_list": artist_list
    }
    return HttpResponse(template.render(context, request))

def create(request):
    template = loader.get_template("artist/create.html")
    context = {
        
    }
    return HttpResponse(template.render(context, request))

def artist(request, artist_id):
    
    template = loader.get_template("artist/artist_id.html")
    context = {
        "artista" : artist_id
    }

    # try:
        # something
    # except Question.DoesNotExist:
        # raise Http404("Question does not exist")
    return HttpResponse(template.render(context, request))