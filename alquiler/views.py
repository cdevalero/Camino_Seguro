from django.shortcuts import render, redirect
from .forms import *
from django.http import HttpResponse
from django.contrib import messages
from datetime import timedelta

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
                    obj = Companias.objects.get(codigo=dni)
                except Companias.DoesNotExist:
                    messages.error(request, 'No existe el usuario, por favor registrarse')
                    return redirect('inicio_user')            
            return redirect('pedido')
        messages.error(request, 'No existe el usuario, por favor registrarse (invalido)')
        return redirect('inicio_user')
    form = FormParticulares_inicio()
    return render(request, 'inicio.html', {'form':form})

def pedido(request):
    if request.method == 'POST':
        form = FormContratos(request.POST)
        if form.is_valid():
            if form.cleaned_data.get('id_camion') and form.cleaned_data.get('id_remolque'):
                messages.error(request, 'No se puede conectar un contrato con un Camion y un Remolque a la vez')
                return render(request, 'pedido.html',{'form':form})
            if form.cleaned_data.get('id_per') and form.cleaned_data.get('id_compa'):
                messages.error(request, 'No se puede conectar un contrato con una Persona y una Compañia a la vez')
                return render(request, 'pedido.html',{'form':form})
            if form.cleaned_data.get('id_per'):
                persona = form.cleaned_data.get('id_per')
                if persona.riesgo:
                    dni = persona.dni
                    messages.error(request, f'El cliente DNI:{dni} es una persona con estado de riesgo')
                    return redirect('pedido')
            if form.cleaned_data.get('id_camion'):
                camion = form.cleaned_data.get('id_camion')
                camion = Contrartos.objects.filter(id_camion=camion.id)
                fecha = form.cleaned_data.get('fecha_alquiler')
                if camion:
                    for cam in camion:
                        fecha_cam = cam.fecha_alquiler
                        fecha_cam = fecha_cam + timedelta(days=cam.dura)
                        if fecha_cam > fecha and fecha > cam.fecha_alquiler:
                            messages.error(request, 'El Camion esta en uso para esa fecha de alquiler')
                            return redirect('pedido')
            if form.cleaned_data.get('id_remolque'):
                remolque = form.cleaned_data.get('id_remolque')
                remolque = Contrartos.objects.filter(id_remolque=remolque.id)
                fecha = form.cleaned_data.get('fecha_alquiler')
                if remolque:
                    for remo in remolque:
                        fecha_remo = remo.fecha_alquiler
                        fecha_remo = fecha_remo + timedelta(days=remo.dura)
                        if fecha_remo > fecha and fecha > remo.fecha_alquiler:
                            messages.error(request, 'El Remolque esta en uso para esa fecha de alquiler')
                            return redirect('pedido')
            form.save()
            return redirect('pedido')
        else:
            messages.error(request, 'Form invalido')
            return redirect('pedido')
    form = FormContratos()
    return render(request, 'pedido.html',{'form':form})
