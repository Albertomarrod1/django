from django.shortcuts import render
from .forms import RegForm
from .models import Registrado
# Create your views here.
"""
def inicio(request):
	form = RegForm(request.POST or None)
	if form.is_valid:
		form_data = form.data
		obj= Registrado.objects.create(email=form_data.get('email'))
	context = {
		'el_form': form,
	}
	return render(request, 'inicio.html',context)
"""

def inicio(request):
	form = RegForm(request.POST or None)
	if form.is_valid():
		form_Data = form.data
		abc = form_Data.get('email')
		abc2= form_Data.get('nombre')
		obj = Registrado.objects.create(email=abc, nombre=abc2)
	context = {
		'el_form': form,
	}
	return render(request, 'inicio.html', context)