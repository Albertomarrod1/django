from django.shortcuts import render
from .forms import ContactForm, RegModelForm
from .models import Registrado
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def inicio(request):
	titulo= 'Bienvenidos'
	if request.user.is_authenticated():
		titulo = 'Bienvenido %s' %(request.user)
	form = RegModelForm(request.POST or None)

	context = {
		'titulo': titulo,
		'el_form': form,
	}

	if form.is_valid():
		instance=form.save(commit=False)
		nombre = form.data.get('nombre')
		email = form.data.get('email')
		if not instance.nombre:
			instance.nombre = 'Persona'
		instance.save()
		context = {
			'titulo': 'Gracias %s!' %(nombre),
		}
		if not nombre:
			context = {
				'titulo': 'Gracias %s!' %(email),
			}
		print (instance)
		print(instance.timestamp)
		# form_Data = form.data
		# abc = form_Data.get('email')
		# abc2= form_Data.get('nombre')
		# obj = Registrado.objects.create(email=abc, nombre=abc2)



	return render(request, 'inicio.html', context)

def contact(request):
	titulo='Contacto'
	form = ContactForm(request.POST or None)
	if form.is_valid():
		# for key,value in form.data.items():
		# 	print(key,value)
		# for key in form.data:
		# 	print(key)
		# 	print(form.data.get(key))
		form_email=form.data.get('email')
		form_mensaje=form.data.get('mensaje')
		form_nombre=form.data.get('nombre')
		asunto = 'Form de Contacto'
		email_from = settings.EMAIL_HOST_USER
		email_to = [email_from]
		email_mensaje= '%s: %s enviado por %s' %(form_nombre, form_mensaje, form_email)
		send_mail(asunto,
			email_mensaje,
			email_from,
			email_to,
			fail_silently=False
			)
		# print(email,mensaje,nombre)
	context={
		"form":form,
		'titulo':titulo,
	}
	return render(request, "forms.html",context)