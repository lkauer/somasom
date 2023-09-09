from django.http import HttpResponse
from django.template import loader
from django.http import Http404


def index(request):
    template = loader.get_template("artist/index.html")
    context = {
        
    }
    return HttpResponse(template.render(context, request))

def all(request):
    template = loader.get_template("artist/all.html")
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