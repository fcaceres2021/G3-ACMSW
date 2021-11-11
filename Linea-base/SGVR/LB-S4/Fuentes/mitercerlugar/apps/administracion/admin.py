from django.contrib import admin
from apps.administracion.models import Imagen, Etiqueta, Pagina, Blog, Contenido
#from apps.administracion.forms import ImagenCreationForm

from django.contrib.auth.models import User

class ImagenAdmin(admin.ModelAdmin):
	exclude = ('usuario',)
	model = Imagen
	#form = ImagenCreationForm
	list_display = ('id', 'nombre', 'imagen', 'fecha_creacion','usuario')
	search_fields = ('nombre', )

	def save_model(self, request, obj, form, change):
		obj.usuario = request.user
		obj.save()

admin.site.register(Imagen, ImagenAdmin)

class EtiquetaAdmin(admin.ModelAdmin):
	exclude = ('usuario',)
	model = Etiqueta
	list_display = ('id', 'nombre', 'fecha_creacion', 'usuario')
	ordering = ('fecha_creacion', )
	search_fields = ('nombre', )
	list_per_page = 50

	def save_model(self, request, obj, form, change):
		obj.usuario = request.user
		obj.save()

admin.site.register(Etiqueta, EtiquetaAdmin)

class PaginaAdmin(admin.ModelAdmin):
	exclude = ('usuario',)
	model = Pagina
	list_display = ('id', 'titulo', 'subtitulo', 'ruta', 'orden', 'menu', 'id_pagina', 'usuario', 'fecha_creacion')
	ordering = ('fecha_creacion', )
	search_fields = ('titulo', )
	list_per_page = 10

	def save_model(self, request, obj, form, change):
		obj.usuario = request.user
		obj.save()

admin.site.register(Pagina, PaginaAdmin)

class ContenidoAdmin(admin.ModelAdmin):
	exclude = ('usuario',)
	model = Contenido
	list_display = (
		'id',
		'pagina', 
		'etiqueta', 
		'nombre', 
		'estilo', 
		'valor', 
		'requerido', 
		'imagen', 
		'link', 
		'orden', 
		'columna', 
		'html', 
		#'origen', 
		'general')
	ordering = ('fecha_creacion', )
	list_filter = ('general', 'pagina', 'origen', )
	search_fields = ('nombre', )
	list_per_page = 20

	def save_model(self, request, obj, form, change):
		obj.usuario = request.user
		obj.save()

admin.site.register(Contenido, ContenidoAdmin)