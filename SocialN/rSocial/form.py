from django import forms

class RegistroUsuario(forms.Form):
	nombre = forms.CharField(label="nombre")
	email = forms.EmailField(label="email")
	password = forms.CharField(label="contrasena", max_length=32)

class InicioSesion(forms.Form):
	email = forms.EmailField(label="email")
	password = forms.CharField(label="contrasena",max_length=32, widget=forms.PasswordInput)
