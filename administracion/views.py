from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from alquiler.models import *
from alquiler.forms import *

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
    form = FormLugarDir()
    return render(request, 'tablas/add/add_lugar_dir.html',{'form':form})

def add_oficinas(request):
    if request.method == 'POST':
        form = FromOficinas(request.POST)
        if form.is_valid():
            form.save()
            return redirect('oficinas_admin')
    form = FromOficinas('c')
    return render(request, 'tablas/add/add_oficinas.html',{'form':form})