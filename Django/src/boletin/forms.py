from django import forms
from .models import Registrado

class RegModelForm(forms.ModelForm):
	class Meta:
		model = Registrado
		fields = ['nombre','email']

	def clean_email(self):
		email=self.data.get('email')
		email_base, proveedor = email.split('@')
		dominio, extension = proveedor.split('.')
		if not extension =='edu':
			raise forms.ValidationError('Utiliza un email con la extensión .EDU')
		return email

	def clean_nombre(self):
		nombre = self.data.get('nombre')

		return nombre

class ContactForm(forms.Form):
	nombre = forms.CharField(required=False)
	email = forms.EmailField()
	mensaje=forms.CharField(widget=forms.Textarea)
	#def clean_email(self):
	#	email=self.data.get('email')
	#	email_base, proveedor = email.split('@')
	#	dominio, extension = proveedor.split('.')
	#	if not extension =='edu':
	#		raise forms.ValidationError('Utiliza un email con la extensión .EDU')
	#	return email