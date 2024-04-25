from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from .models import Artist
from release.models import Release


def index(request):
    artist_list = Artist.objects.all()
    template = loader.get_template("artist/index.html")
    context = {
        "artist_list": artist_list
    }
    return HttpResponse(template.render(context, request))

def artist(request, id_artist):
    try:
        template = loader.get_template("artist/id_artist.html")
        artist = Artist.objects.get(pk=id_artist)
        try:

            artist_release = Release.objects.get(artist=id_artist)
            context = {
                "artist" : artist,
                "artist_release" : artist_release
            }
        except:
            context = {
                "artist" : artist,
                "artist_release" : {}
            }
    except Artist.DoesNotExist:
        raise Http404("Artist does not exist")
    return HttpResponse(template.render(context, request))