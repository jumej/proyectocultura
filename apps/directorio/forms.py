#Archivo que llevara todos los formularios
from django import forms
from apps.directorio.models import *

class ArtistaForm(forms.ModelForm):
	class Meta:
		model = Artista
