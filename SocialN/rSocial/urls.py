from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^registro/$', views.registro, name='registro'),
    url(r'^Inicio/$', views.Inicio, name='Inicio'),
    url(r'^Perfil/(.+)$', views.Perfil, name='Perfil'),
    url(r'^grupo/(.+)$', views.grupo, name='grupo'),

]
