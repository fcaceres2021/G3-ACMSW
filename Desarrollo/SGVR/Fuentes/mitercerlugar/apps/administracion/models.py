from django.db import models
from apps.usuarios.models import Usuario

from django.db.models.signals import post_delete, post_save, pre_save
from django.dispatch.dispatcher import receiver
import os

class Imagen(models.Model):
	usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
	nombre = models.CharField(max_length=150, unique=True)
	imagen = models.ImageField(upload_to='administracion/imagenes/')
	fecha_creacion = models.DateTimeField(auto_now_add=True, blank=True)

	def __str__(self):
		return self.nombre

def _delete_file(path):
	if os.path.isfile(path):
		os.remove(path)

@receiver(post_delete)
def delete_img_post_delete(sender, instance, *args, **kwargs):
	if hasattr(instance, 'imagen'):
		if hasattr(instance.imagen, 'path'):
			_delete_file(instance.imagen.path)

class Etiqueta(models.Model):
	usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
	nombre = models.CharField(max_length=100, unique=True)
	fecha_creacion = models.DateTimeField(auto_now_add=True, blank=True)

	def __str__(self):
		return self.nombre

class Pagina(models.Model):
	usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
	contenidos = models.ManyToManyField(Etiqueta, through='Contenido')
	titulo = models.CharField(max_length=100)
	subtitulo = models.CharField(max_length=100, null=True, blank=True)
	ruta = models.CharField(max_length=100, null=True, blank=True)
	menu = models.BooleanField(default=False)
	orden = models.IntegerField(null=True, blank=True)
	id_pagina = models.IntegerField(null=True, blank=True)
	fecha_creacion = models.DateTimeField(auto_now_add=True, blank=True)

	def __str__(self):
		return self.titulo

class Blog(models.Model):
	usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
	titulo = models.CharField(max_length=100)
	subtitulo = models.CharField(max_length=100, null=True, blank=True)
	descripcion = models.TextField(null=True, blank=True)
	ruta = models.CharField(max_length=100, null=True, blank=True)
	orden = models.IntegerField(null=True, blank=True)
	imagen = models.ForeignKey(Imagen, null=True, blank=True, on_delete=models.CASCADE, related_name='blog_imagen')
	imagen_alterna = models.ForeignKey(Imagen, null=True, blank=True, on_delete=models.CASCADE, related_name='blog_imagen_alterna')
	fecha_creacion = models.DateTimeField(auto_now_add=True, blank=True)

	def __str__(self):
		return self.titulo

class Contenido(models.Model):
	usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
	pagina = models.ForeignKey(Pagina, null=True, blank=True, on_delete=models.CASCADE)
	blog = models.ForeignKey(Blog, null=True, blank=True, on_delete=models.CASCADE)
	etiqueta = models.ForeignKey(Etiqueta, null=True, blank=True, on_delete=models.CASCADE)
	nombre = models.CharField(max_length=100, null=True, blank=True)
	estilo = models.CharField(max_length=100, null=True, blank=True)
	valor = models.TextField(null=True, blank=True)
	requerido = models.BooleanField(default=False)
	imagen = models.ForeignKey(Imagen, null=True, blank=True, on_delete=models.CASCADE)
	link = models.CharField(max_length=500,null=True, blank=True)
	orden = models.IntegerField(null=True, blank=True)
	columna = models.IntegerField(null=True, blank=True)
	html = models.TextField(null=True, blank=True)
	origen = models.ManyToManyField("self")
	general = models.BooleanField(default=False)
	estado = models.BooleanField(default=True)
	fecha_creacion = models.DateTimeField(auto_now_add=True, blank=True)