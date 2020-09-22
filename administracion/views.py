from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from alquiler.models import *
from alquiler.forms import *
from django.contrib import messages

def index_admin(request):
    return render(request, 'base_admin.html')

def lugar_dir_admin(request):
    obj = Lugares_Dir.objects.all()
    return render(request, 'tablas/lugar_dir.html', {'lugares': obj})

def companias_admin(request):
    obj = Companias.objects.all()
    return render(request, 'tablas/companias.html', {'companias': obj})

def particulares_admin(request):
    obj = Particulares.objects.all()
    return render(request, 'tablas/particulares.html', {'particulares': obj})

def oficinas_admin(request):
    obj = Oficinas.objects.all()
    return render(request, 'tablas/oficinas.html', {'oficinas': obj})

def camiones_admin(request):
    obj = Camiones.objects.all()
    return render(request, 'tablas/camiones.html', {'camiones': obj})

def remolques_admin(request):
    obj = Remolques.objects.all()
    return render(request, 'tablas/remolques.html', {'remolques': obj})

def contratos_admin(request):
    obj = Contrartos.objects.all()
    return render(request, 'tablas/contratos.html', {'contratos': obj})

def add_lugar_dir(request):
    if request.method == 'POST':
        form = FormLugarDir(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lugar_dir_admin')
        else:
            for msg in form.errors_messages:
                messages.error(request, form.error_messages[msg])
                return redirect('lugar_dir_admin')
    form = FormLugarDir()
    return render(request, 'tablas/add/add_lugar_dir.html',{'form':form})

def add_oficinas(request):
    if request.method == 'POST':
        form = FormOficinas('c',request.POST)
        if form.is_valid():
            form.save()
            return redirect('oficinas_admin')
        else:
            for msg in form.errors_messages:
                messages.error(request, form.error_messages[msg])
                return redirect('oficinas_admin')
    form = FormOficinas('c')
    return render(request, 'tablas/add/add_oficinas.html',{'form':form})

def add_companias(request):
    if request.method == 'POST':
        form = FormCompanias('c',request.POST)
        if form.is_valid():
            form.save()
            return redirect('companias_admin')
        else:
            for msg in form.errors_messages:
                messages.error(request, form.error_messages[msg])
                return redirect('companias_admin')
    form = FormCompanias('c')
    return render(request, 'tablas/add/add_companias.html',{'form':form})

def add_particulares(request):
    if request.method == 'POST':
        form = FormParticulares('c',request.POST)
        if form.is_valid():
            form.save()
            return redirect('particulares_admin')
        else:
            for msg in form.errors_messages:
                messages.error(request, form.error_messages[msg])
                return redirect('particulares_admin')
    form = FormParticulares('c')
    return render(request, 'tablas/add/add_particulares.html',{'form':form})

def add_camiones(request):
    if request.method == 'POST':
        form = FormCamiones(request.POST)
        if form.is_valid():
            form.save()
            return redirect('camiones_admin')
        else:
            for msg in form.errors_messages:
                messages.error(request, form.error_messages[msg])
                return redirect('camiones_admin')
    form = FormCamiones()
    return render(request, 'tablas/add/add_camiones.html',{'form':form})

def add_remolques(request):
    if request.method == 'POST':
        form = FormRemolques(request.POST)
        if form.is_valid():
            form.save()
            return redirect('remolques_admin')
        else:
            for msg in form.errors_messages:
                messages.error(request, form.error_messages[msg])
                return redirect('remolques_admin')
    form = FormRemolques()
    return render(request, 'tablas/add/add_remolques.html',{'form':form})

def add_contratos(request):
    if request.method == 'POST':
        form = FormContratos(request.POST)
        if form.is_valid():
            if form.cleaned_data.get('id_camion') and form.cleaned_data.get('id_remolque'):
                messages.error(request, 'No se puede conectar un contrato con un Camion y un Remolque a la vez')
                return render(request, 'tablas/add/add_contratos.html',{'form':form})
            if form.cleaned_data.get('id_per') and form.cleaned_data.get('id_compa'):
                messages.error(request, 'No se puede conectar un contrato con una Persona y una Compañia a la vez')
                return render(request, 'tablas/add/add_contratos.html',{'form':form})
            form.save()
            return redirect('contratos_admin')
        else:
            for msg in form.errors_messages:
                messages.error(request, form.error_messages[msg])
                return redirect('add_contratos')
    form = FormContratos()
    return render(request, 'tablas/add/add_contratos.html',{'form':form})
