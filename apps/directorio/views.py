from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView

from apps.directorio.models import *
from apps.directorio.forms import *
# Create your views here.

def index(request):
    return HttpResponse("Index")

class RegistroArtista(CreateView):
	model = Artista
	form_class = ArtistaForm
	template_name = 'forms/rartista_form.html'

def crearEvento(request):
    return HttpResponse("Crear Evento")

def crearCapsula(request):
    return HttpResponse("Crear Capsula")
