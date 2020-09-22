from django.shortcuts import render, redirect
from alquiler.models import *

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

