from django import forms
from .models import *
from django.forms import ModelForm

class formulario(forms.ModelForm):
	class Meta:
		model = co
		fields =('Nombre', 'Apellido', 'Telefono')