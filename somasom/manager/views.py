from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from .forms import NewArtistForm
from .forms import NewReleaseForm
from artist.models import Artist
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    template = loader.get_template("manager/index.html")
    try:

        artist = Artist.objects.get(user_id=request.user.user_id)
        context = {
            "artist" : artist,
        }
    except:
        context = {
            "artist" : {}        
        }

    return HttpResponse(template.render(context, request))

def artist(request):

    user_id = request.user.user_id
    template = loader.get_template("manager/artist.html")
    context = {
        'user_id': user_id
    }
    return HttpResponse(template.render(context, request))

def release(request):
    template = loader.get_template("manager/release.html")
    context = {
        
    }
    return HttpResponse(template.render(context, request))

def create_artist(request):
    template = loader.get_template("manager/index.html")
    context = {}
    
    if request.method == "POST":
        form = NewArtistForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            context['form'] = form

    return HttpResponse(template.render(context, request))

def create_release(request):
    template = loader.get_template("manager/index.html")
    context = {}
    
    if request.method == "POST":
        form = NewReleaseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            context['form'] = form

    return HttpResponse(template.render(context, request))