from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^registro/$', views.registro, name='registro'),
    url(r'^post/(.+)$', views.paginas, name='paginas'),
    url(r'^Inicio/$', views.Inicio, name='Inicio'),
    url(r'^salir/(.+)$', views.salir, name='salir'),
    url(r'^Perfil/(.+)$', views.Perfil, name='Perfil'),
    url(r'^banda/(.+)$', views.Controller, name='Controller'),
    url(r'^ind/(.+)$', views.index2, name='index2'),

]
