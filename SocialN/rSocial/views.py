from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, RequestContext
from django.template.loader import get_template
from rSocial.models import genero, grupo, usuario, album, miembro, post
from form import RegistroUsuario, InicioSesion
from django.contrib.auth import authenticate, get_backends,login
from django.core.urlresolvers import reverse

def index(request):
	t = get_template("index.html")
	post_list = post.objects.order_by("id_post")
	group_list = grupo.objects.order_by("id_grupo")
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
			    r.save()
			    t = get_template("registro.html")
			    html=t.render(RequestContext(request, {"formulario":"Registro_exitoso"}))
			    return HttpResponse(html)
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
			if not(usuario.objects.filter(email=em).count()==0):
				user = usuario.objects.get(email=em)
				return HttpResponseRedirect(reverse('Perfil', args=(user.id_usuario,)))
				#pasar user kawart
	else:
		form = InicioSesion()
		t = get_template("InicioSesion.html")
		html = t.render(RequestContext(request, {"formulario":form}))
		return HttpResponse(html)

def Perfil(request, id2):
	b = usuario.objects.get(id_usuario=id2)
	t = get_template("perfil.html")
	html = t.render(RequestContext(request,{"nombre":b.nombre, "esAdmin":b.isAdmin}))
	return HttpResponse(html)

	# Create your views here.
def grupo(request, id2):
	b = grupo.objects.get(id_grupo=id2)
	t = get_template("grupo.html")
	html = t.render(RequestContext(request, {"nombre":b.nombre, "integrantes":miembro.objects.filter(fk_miembro_grupo=b.id_grupo)	, "genero":b.fk_grupo_genero, "album":, "post":, "fecha"}))
	return HttpResponse(html)
