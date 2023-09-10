from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import Http404


def index(request):
    template = loader.get_template("public/index.html")
    context = {
        
    }
    return HttpResponse(template.render(context, request))


def search(request):
    template = loader.get_template("public/search.html")
    context = {
        
    }
    return HttpResponse(template.render(context, request))
