from django.db import models

# Create your models here.


class Categoria(models.Model):
	nombre = models.CharField(max_length=25)

	def __unicode__(self):
		return '{}'.format(self.nombre)

class Tamanio(models.Model):
	descripcion = models.CharField(max_length=10)

class Artista(models.Model):
	BOOL_CHOICES = ((True,'Masculino'),(False,'Femenino'))
	nombre = models.CharField(max_length=30)
	apellido = models.CharField(max_length=30)
	genero = models.BooleanField(choices = BOOL_CHOICES,default=True)
	fecha_nacimiento = models.DateField()
	telefono = models.CharField(max_length=10)
	email = models.EmailField()
	categoria = models.ForeignKey(Categoria, null=True, blank=True, on_delete=models.CASCADE)
	descripcion = models.TextField(max_length=150)

class Evento(models.Model):
	titulo = models.CharField(max_length=45)
	categoria = models.ForeignKey(Categoria, null=True, blank=True, on_delete=models.CASCADE)
	direccion = models.CharField(max_length=70)
	fecha = models.DateField()
	horario = models.DateTimeField()
	tamanio = models.ForeignKey(Tamanio, null=True, blank=True, on_delete=models.CASCADE)
	descripcion = models.TextField(max_length=200)

class Capsula(models.Model):
	contenido = models.TextField(max_length=200)
	fecha = models.DateField()