from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Pagina do artista")

def all(request):
    return HttpResponse("Todos os artistas")

def artist(request, artist_id):
    return HttpResponse("Você está vendo o artista %s." % artist_id)
