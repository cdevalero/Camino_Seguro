from django.shortcuts import render, redirect
from .forms import *
from django.http import HttpResponse
from django.contrib import messages

def registro_user_persona(request):
    if request.method == 'POST':
        form = FormParticulares_cliente('c',request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio_user')
        else:
            messages.error(request, 'Error')
            return render(request, 'register.html', {'form':form})
    form = FormParticulares_cliente('c')
    return render(request, 'register.html', {'form':form})

def registro_user_opcion(request):
    return render(request, 'opcion.html')

def registro_user_compania(request):
    if request.method == 'POST':
        form = FormCompanias('c',request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio_user')
        else:
            messages.error(request, 'Error')
            return render(request, 'register.html', {'form':form})
    form = FormCompanias('c')
    return render(request, 'register.html', {'form':form})

def inicio_user(request):
    if request.method == 'POST':
        form = FormParticulares_inicio(request.POST)
        if form.is_valid():
            dni = form.cleaned_data['dni']
            try:
                obj = Particulares.objects.get(dni=dni)
            except Particulares.DoesNotExist:
                try:
                    comp = Companias.objects.get(codigo=dni)
                except Companias.DoesNotExist:
                    messages.error(request, 'No existe el usuario, por favor registrarse (comp)')
                    return redirect('inicio_user')
                finally:
                    return redirect('particulares_admin')
                messages.error(request, 'No existe el usuario, por favor registrarse')
                return redirect('inicio_user')
            return redirect('particulares_admin')
        messages.error(request, 'No existe el usuario, por favor registrarse (invalido)')
        return redirect('inicio_user')
    form = FormParticulares_inicio()
    return render(request, 'inicio.html', {'form':form})