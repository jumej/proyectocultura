from django.conf.urls import patterns, url
from apps.directorio.views import *

urlpatterns = patterns('',

     url(r'^$', index, name="index"),
     url(r'^rartista/', RegistroArtista.as_view(), name='crear_artista'),
     url(r'^cevento/', crearEvento),
     url(r'^capsula/', crearCapsula),

)
