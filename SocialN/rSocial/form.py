from django import forms

class RegistroUsuario(forms.Form):
	nombre = forms.CharField(label="nombre")
	email = forms.EmailField(label="email")
	password = forms.CharField(label="contrasena", max_length=32, widget=forms.PasswordInput)

class InicioSesion(forms.Form):
	email = forms.EmailField(label="email")
	password = forms.CharField(label="contrasena",max_length=32, widget=forms.PasswordInput)

class RegistroPost(forms.Form):
	cuerpo = forms.CharField(label = "comentario", max_length=150)