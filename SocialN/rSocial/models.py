from __future__ import unicode_literals

from django.db import models

class genero(models.Model):
	id_genero = models.AutoField(primary_key = True)
	nombre = models.CharField(max_length=50)

class grupo(models.Model):
	nombre = models.CharField(max_length=50, default="")
	id_grupo = models.AutoField(primary_key = True)
	fecha_inicio = models.DateTimeField()
	fk_grupo_genero = models.ForeignKey(genero)

class usuario(models.Model):
	id_usuario = models.AutoField(primary_key = True)
	nombre = models.CharField(max_length=50, default="")
	email = models.EmailField(max_length=50)
	password = models.CharField(max_length=50)
	isAdmin = models.BooleanField(default=False)

class album(models.Model):
	id_album = models.AutoField(primary_key = True)
	nombre = models.CharField(max_length=50)
	fk_album_grupo = models.ForeignKey(grupo)



class miembro(models.Model):
	id_miembro = models.AutoField(primary_key = True)
	nombre = models.CharField(max_length=100)
	fk_miembro_grupo = models.ForeignKey(grupo)

class post(models.Model):
	id_post = models.AutoField(primary_key = True)
	titulo = models.CharField(max_length=50)
	body = models.CharField(max_length=500)
	id_grupo_post = models.ForeignKey(grupo)




# Create your models here.
