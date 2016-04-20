from django.contrib.auth.hashers import check_password
from rSocial.models import genero, grupo, usuario, album, miembro, post

class UserBackend(object):

	def authenticate(self, username=None, password=None):
		try:
			user = usuario.objects.get(email=username)
			if password == user.password:
				return user
			else:
			    return None
		except usuario.DoesNotExist:
		    return None

	def get_user(self, user_id):
	    try:
	        return usuario.objects.get(id_usuario=user_id)
	    except usuario.DoesNotExist:
	        return None    	    	    	
			
