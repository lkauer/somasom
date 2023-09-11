from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import Http404

# Create your views here.
def index(request):
    template = loader.get_template("manager/index.html")
    context = {
        
    }
    return HttpResponse(template.render(context, request))

def artist(request):
    template = loader.get_template("manager/artist.html")
    context = {
        
    }
    return HttpResponse(template.render(context, request))

def release(request):
    template = loader.get_template("manager/release.html")
    context = {
        
    }
    return HttpResponse(template.render(context, request))
