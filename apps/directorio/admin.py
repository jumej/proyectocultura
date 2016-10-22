from django.contrib import admin

# Register your models here.

from apps.directorio.models import Artista,Categoria,Evento,Capsula,Tamanio, Departamento

admin.site.register(Categoria)
admin.site.register(Artista)
admin.site.register(Evento)
admin.site.register(Capsula)
admin.site.register(Tamanio)
admin.site.register(Departamento)