from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, RequestContext
from django.template.loader import get_template
from rSocial.models import genero, grupo, usuario, album, miembro, post, opinion
from form import RegistroUsuario, InicioSesion, RegistroPost
from django.contrib.auth import authenticate, get_backends,login
from django.core.urlresolvers import reverse



def index2(request, id2):
	b = usuario.objects.get(id_usuario=id2)
	if b.inSesion == True:
	    t = get_template("index.html")
	    group_list = grupo.objects.order_by("id_grupo")
	    post_list = post.objects.order_by("id_post")
	    bandera1 = False
	    bandera2 = False
	    if not (post_list.count()==0):
		    bandera1 = True
	    if not (group_list.count() == 0):
	        bandera2 = True	
	    html = t.render(RequestContext(request, {"nombre":b.nombre, "Logeado":True,"hay_posts":bandera1,"hay_grupos":bandera2,"post_list":post_list,"group_list":group_list, "usuario":id2}))
	    return HttpResponse(html)



def index(request):
	t = get_template("index.html")
	group_list = grupo.objects.order_by("id_grupo")
	post_list = post.objects.order_by("id_post")
	bandera1 = False
	bandera2 = False
	if not (post_list.count()==0):
		bandera1 = True
	if not (group_list.count() == 0):
	    bandera2 = True	
	html = t.render(RequestContext(request, {"hay_posts":bandera1,"hay_grupos":bandera2,"post_list":post_list,"group_list":group_list}))
	return HttpResponse(html)


def registro(request):
	if request.method == 'POST':
		form = RegistroUsuario(request.POST)
		if form.is_valid():
			em = form.cleaned_data['email']
			if (usuario.objects.filter(email=em).count()==0):
			    r=usuario(nombre= form.cleaned_data['nombre'],email=form.cleaned_data['email'], password=form.cleaned_data['password'], isAdmin=False)
			    r.inSesion = True
			    r.save()
			    t = get_template("registro.html")
			    html=t.render(RequestContext(request, {"formulario":"Registro_exitoso"}))
			    return HttpResponseRedirect(reverse('Perfil', args=(r.id_usuario,)))
			else:
			    t=get_template("registro.html")
			    form = RegistroUsuario()
			    html=t.render(RequestContext(request, {"formulario":form, "mensaje":"correo ya registrado, ingresa otro"}))
			    return HttpResponse(html)
			    #email ya registrado mandar mensaje email ya registrado    
	else:	
	    form = RegistroUsuario()
	    t = get_template("registro.html")
	    html = t.render(RequestContext(request, {"formulario":form}))
	    return HttpResponse(html)


def Inicio(request):	    
	if request.method == 'POST':
		form = InicioSesion(request.POST)
		if form.is_valid():
			em = form.cleaned_data['email']
			pp = form.cleaned_data['password']
			if not(usuario.objects.filter(email=em).count()==0):
				user = usuario.objects.get(email=em)
				if user.password == pp:
				    user.inSesion = True
				    user.save()
				    return HttpResponseRedirect(reverse('Perfil', args=(user.id_usuario,)))
				else:
				    form = InicioSesion()
				    t = get_template("InicioSesion.html")
				    html = t.render(RequestContext(request,{"formulario":form, "mal_p":True}))
				    return HttpResponse(html)
			else:
			    form = InicioSesion()
			    t = get_template("InicioSesion.html")
			    html = t.render(RequestContext(request, {"formulario":form, "mal_u":True}))
			    return HttpResponse(html) 

				#pasar user kawart
	else:
		form = InicioSesion()
		t = get_template("InicioSesion.html")
		html = t.render(RequestContext(request, {"formulario":form}))
		return HttpResponse(html)

def Perfil(request, id2):
	b = usuario.objects.get(id_usuario=id2)
	if b.inSesion == True:
	    return HttpResponseRedirect(reverse('index2', args=(b.id_usuario,)))
	else:
		form = InicioSesion()
		t=get_template("perfil.html")
		html = t.render(RequestContext(request,{"Logeado":False, "formulario":form}))
		return HttpResponse(html)    

	# Create your views here.

def salir(request, id2):
	print id2
	usr = None
	usr = usuario.objects.get(id_usuario=id2)
	if not (usr == None):
		usr.inSesion = False
		usr.save()
	return index(request)


def paginas(request, id2):
	usr = None
	doe = "Visitante"
	if request.method == 'POST':
		form = RegistroPost(request.POST)
		body = "hola :)"
		if form.is_valid():
			body = form.cleaned_data['cuerpo']
		if len(id2)>=3:
		    usr = usuario.objects.get(id_usuario=id2.split('/')[1])
		if not(usr==None):
		    doe = usr.nombre    
		p = post.objects.get(id_post=id2.split('/')[0])    	
		op = opinion(autor=doe, body=body, id_post_opinion=p)
		op.save()
	usr = None
	bandera1 = False
	listilla = []
	if not(opinion.objects.filter(id_post_opinion=id2.split('/')[0]).count()==0):
		listilla = opinion.objects.filter(id_post_opinion=id2.split('/')[0])
		bandera1 = True
	if len(id2)>=3:
		usr = usuario.objects.get(id_usuario=id2.split('/')[1])
	p = post.objects.get(id_post=id2.split('/')[0])
	if not(usr == None):
		if usr.inSesion:
		    t=get_template("posts.html")
		    form = RegistroPost()
		    html = t.render(RequestContext(request, {"comentario":listilla, "post_id":p.id_post,"hay_comentarios":bandera1, "formulario":form, "Logeado":True, "nombre":usr.nombre, "usuario":id2.split('/')[1], "titulo":p.titulo, "cuerpo":p.body}))
		    return HttpResponse(html)
		else:
		    form = InicioSesion()
		    t = get_template("perfil.html")
		    html = t.render(RequestContext(request, {"Logeado":False, "formulario":form}))
		    return HttpResponse(html)	
	else:
		form = RegistroPost()
		t = get_template("posts.html")
		html = t.render(RequestContext(request, {"comentario":listilla, "post_id":p.id_post, "hay_comentarios":bandera1, "formulario":form,"Logeado":False, "titulo":p.titulo, "cuerpo":p.body}))
		return HttpResponse(html)


def Controller(request, id2):
	if len(id2)>=3:
		usr = usuario.objects.get(id_usuario=id2.split('/')[1])
		if usr.inSesion:
			b = grupo.objects.get(id_grupo=id2.split('/')[0])
			t = get_template("grupos.html")
			a = False
			z = False
			c = False
			if not (miembro.objects.filter(fk_miembro_grupo=b.id_grupo).count()==0):
				a = True
			if not (album.objects.filter(fk_album_grupo=b.id_grupo).count()==0):
				z = True
			if not (post.objects.filter(id_grupo_post=b.id_grupo).count()==0):
				c = True
			ggg = b.fk_grupo_genero.nombre
			html = t.render(RequestContext(request, {"Logeado":True, "usuario": usr.nombre, "usuariod":id2.split('/')[1],"nombre":b.nombre, "integrantes":miembro.objects.filter(fk_miembro_grupo=b.id_grupo), "g":ggg, "album":album.objects.filter(fk_album_grupo=b.id_grupo), "post":post.objects.filter(id_grupo_post=b.id_grupo), "fecha":b.fecha_inicio, "hay_integrante":a, "hay_album":z, "hay_post":c}))
			return HttpResponse(html)
		else:
			form = InicioSesion()
			t=get_template("perfil.html")
			html = t.render(RequestContext(request,{"Logeado":False, "formulario":form}))
			return HttpResponse(html)
	b = grupo.objects.get(id_grupo=id2[0])
	t = get_template("grupos.html")
	a = False
	z = False
	c = False
	if not (miembro.objects.filter(fk_miembro_grupo=b.id_grupo).count()==0):
		a = True
	if not (album.objects.filter(fk_album_grupo=b.id_grupo).count()==0):
		z = True
	if not (post.objects.filter(id_grupo_post=b.id_grupo).count()==0):
		c = True
	ggg = b.fk_grupo_genero.nombre
	html = t.render(RequestContext(request, {"nombre":b.nombre, "integrantes":miembro.objects.filter(fk_miembro_grupo=b.id_grupo), "g":ggg, "album":album.objects.filter(fk_album_grupo=b.id_grupo), "post":post.objects.filter(id_grupo_post=b.id_grupo), "fecha":b.fecha_inicio, "hay_integrante":a, "hay_album":z, "hay_post":c}))
	return HttpResponse(html)
