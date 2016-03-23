from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *
# Create your views here.
def co_list(request, template_name = 'lista_contactos.html'):
	cos = co.objects.all()
	#u = {}
	#u['object_list'] = cos
	return render(request, template_name, {'cos': cos})

def co_add(request, template_name = 'add_contactos.html'):
	form = formulario(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('co_list')
	return render(request, template_name,{'form': form})

def co_edit(request, pk, template_name = 'add_contactos.html'):
	Co = get_object_or_404(co, pk = pk)
	form = formulario(request.POST or None, instance = Co)
	if form.is_valid():
		form.save()
		return redirect('co_list')
	return render(request, template_name,{'form': form})

def co_view(request, pk, template_name = 'view_contactos.html'):
	cos = get_object_or_404(co, pk=pk)
	form = formulario(request.POST or None, instance=cos)
	if form.is_valid():
		form.save()
		return redirect('co_list')
	return render(request, template_name, {'form':form,'cos': cos})

def co_ini(request, template_name = 'inicial.html'):
	return render(request, template_name)
