from django.shortcuts import render
from .forms import ContactForm, RegModelForm
from .models import Registrado
# Create your views here.

def inicio(request):
	titulo= 'HOLA'
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
	form = ContactForm(request.POST or None)
	if form.is_valid():
		for key,value in form.data.items():
			print(key,value)
		# for key in form.data:
		# 	print(key)
		# 	print(form.data.get(key))
		# email=form.data.get('email')
		# mensaje=form.data.get('mensaje')
		# nombre=form.data.get('nombre')
		# print(email,mensaje,nombre)
	context={
		"form":form,
	}
	return render(request, "forms.html",context)