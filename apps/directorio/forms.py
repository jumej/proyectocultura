#Archivo que llevara todos los formularios
from django import forms
from apps.directorio.models import *
class ArtistaForm(forms.ModelForm):
	class Meta:
		model = Artista

		fields = [
			'nombre',
			'apellido',
			'genero',
			'fecha_nacimiento',
			'telefono',
			'email',
			'categoria',
			'descripcion',
		]

		labels = {
			'nombre': 'Nombre',
			'apellido': 'Apellido',
			'genero': 'Genero',
			'fecha_nacimiento': 'Fecha nacimiento',
			'telefono': 'Telefono',
			'email': 'Correo',
			'categoria': 'Categoria',
			'descripcion': 'Descripcion',

		}

		widgets = {

			'nombre': forms.TextInput(attrs={'class':'form-control'}),
			'apellido': forms.TextInput(attrs={'class':'form-control'}),
			'genero': forms.RadioSelect,
			'fecha_nacimiento': forms.TextInput(attrs={'class':'form-control'}),
			'telefono': forms.TextInput(attrs={'class':'form-control'}),
			'email': forms.TextInput(attrs={'class':'form-control'}),
			'categoria': forms.Select(attrs={'class':'form-control'}),
			'descripcion': forms.TextInput(attrs={'class':'form-control'}),



		}
