from django.contrib import admin
from .models import genero, grupo, usuario, album, miembro, post, comentario



#class Genero_Admin(admin.ModelAdmin):
	#list_display = ('nombre',)
	#list_filter = ('nombre',)
	#ordering = ('nombre',)
	#serch_fields = ('nombre',)

admin.site.register(genero)

#class Grupo_Admin(admin.ModelAdmin):
	#list_display =('nombre',)
	#list_filter = ('nombre',)
	#ordering = ('nombre',)
	#serch_fields = ('nombre',)

admin.site.register(grupo)

#class Usuario_Admin(admin.ModelAdmin):
	#list_display('nombre', 'email')
	#list_filter('nombre', 'email')
	#ordering('nombre',)
	#serch_fields('nombre',)

admin.site.register(usuario)

#class Album_Admin(admin.ModelAdmin):
	#list_display('nombre',)
	#list_filter('nombre',)
	#ordering('nombre',)
	#serch_fields('nombre',)

admin.site.register(album)
admin.site.register(miembro)
admin.site.register(post)
admin.site.register(comentario)

# Register your models here.
