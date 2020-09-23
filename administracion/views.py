from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from alquiler.models import *
from alquiler.forms import *
from django.contrib import messages

#index
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

# add
def add_lugar_dir(request):
    if request.method == 'POST':
        form = FormLugarDir(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lugar_dir_admin')
        else:
            messages.error(request, 'Form invalido')
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
            messages.error(request, 'Form invalido')
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
            messages.error(request, 'Form invalido')
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
            messages.error(request, 'Form invalido')
            return redirect('particulares_admin')
    form = FormParticulares('c')
    return render(request, 'tablas/add/add_particulares.html',{'form':form})

def add_camiones(request):
    if request.method == 'POST':
        form = FormCamiones(request.POST)
        if form.is_valid():
            num_camion = form.cleaned_data.get('num_registro')
            try:
                Remolques.objects.get(num_registro=num_camion)
            except:                             
                form.save()
                return redirect('camiones_admin')
            messages.error(request, 'Ese numero de registro ya esta en uso por un Remolque')
            return render(request, 'tablas/add/add_camiones.html',{'form':form}) 
        else:
            messages.error(request, 'Form invalido')
            return redirect('camiones_admin')
    form = FormCamiones()
    return render(request, 'tablas/add/add_camiones.html',{'form':form})

def add_remolques(request):
    if request.method == 'POST':
        form = FormRemolques(request.POST)
        if form.is_valid():
            num_remolque = form.cleaned_data.get('num_registro')
            try:
                Camiones.objects.get(num_registro=num_remolque)
            except:
                form.save()
                return redirect('remolques_admin')
            messages.error(request, 'Ese numero de registro ya esta en uso por un Camion')
            return render(request, 'tablas/add/add_remolques.html',{'form':form}) 
        else:
            messages.error(request, 'Form invalido')
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
            messages.error(request, 'Form invalido')
            return redirect('add_contratos')
    form = FormContratos()
    return render(request, 'tablas/add/add_contratos.html',{'form':form})


# delete
def delete_lugar_dir(request, id):
    try:
        obj = Lugares_Dir.objects.get(pk=id)
    except Lugares_Dir.DoesNotExist:        
        messages.error(request, 'No existe la entrada')
        return redirect('lugar_dir_admin')
    obj.delete()
    return redirect('lugar_dir_admin')

def delete_oficinas(request, id):
    try:
        obj = Oficinas.objects.get(pk=id)
    except Oficinas.DoesNotExist:        
        messages.error(request, 'No existe la entrada')
        return redirect('oficinas_admin')
    obj.delete()
    return redirect('oficinas_admin')

def delete_companias(request, id):
    try:
        obj = Companias.objects.get(pk=id)
    except Companias.DoesNotExist:        
        messages.error(request, 'No existe la entrada')
        return redirect('companias_admin')
    obj.delete()
    return redirect('companias_admin')

def delete_particulares(request, id):
    try:
        obj = Particulares.objects.get(pk=id)
    except Particulares.DoesNotExist:        
        messages.error(request, 'No existe la entrada')
        return redirect('particulares_admin')
    obj.delete()
    return redirect('particulares_admin')

def delete_camiones(request, id):
    try:
        obj = Camiones.objects.get(pk=id)
    except Camiones.DoesNotExist:        
        messages.error(request, 'No existe la entrada')
        return redirect('camiones_admin')
    obj.delete()
    return redirect('camiones_admin')

def delete_remolques(request, id):
    try:
        obj = Remolques.objects.get(pk=id)
    except Remolques.DoesNotExist:        
        messages.error(request, 'No existe la entrada')
        return redirect('remolques_admin')
    obj.delete()
    return redirect('remolques_admin')

def delete_contratos(request, id):
    try:
        obj = Contrartos.objects.get(pk=id)
    except Contrartos.DoesNotExist:        
        messages.error(request, 'No existe la entrada')
        return redirect('contratos_admin')
    obj.delete()
    return redirect('contratos_admin')

#edit
def edit_lugar_dir(request, id):
    try:
        obj = Lugares_Dir.objects.get(pk=id)
    except Lugares_Dir.DoesNotExist:
        messages.error(request, 'No existe la entrada')
        return redirect('lugar_dir_admin')

    if request.method == 'POST':
        form = FormLugarDir(request.POST, instance= obj)
        if form.is_valid():
            form.save()
            return redirect('lugar_dir_admin')
        else:
            messages.error(request, 'Form invalido')
            return redirect('lugar_dir_admin')

    form = FormLugarDir(instance= obj)
    return render(request, 'tablas/add/add_lugar_dir.html',{'form':form})

def edit_oficinas(request, id):
    try:
        obj = Oficinas.objects.get(pk=id)
    except Oficinas.DoesNotExist:
        messages.error(request, 'No existe la entrada')
        return redirect('oficinas_admin')

    if request.method == 'POST':
        form = FormOficinas('c',request.POST, instance= obj)
        if form.is_valid():
            form.save()
            return redirect('oficinas_admin')
        else:
            messages.error(request, 'Form invalido')
            return redirect('oficinas_admin')
    form = FormOficinas('c', instance= obj)
    return render(request, 'tablas/add/add_oficinas.html',{'form':form})

def edit_companias(request, id):
    try:
        obj = Companias.objects.get(pk=id)
    except Companias.DoesNotExist:
        messages.error(request, 'No existe la entrada')
        return redirect('companias_admin')

    if request.method == 'POST':
        form = FormCompanias('c',request.POST, instance= obj)
        if form.is_valid():
            form.save()
            return redirect('companias_admin')
        else:
            messages.error(request, 'Form invalido')
            return redirect('companias_admin')
    form = FormCompanias('c', instance= obj)
    return render(request, 'tablas/add/add_companias.html',{'form':form})

def edit_particulares(request, id):
    try:
        obj = Particulares.objects.get(pk=id)
    except Particulares.DoesNotExist:
        messages.error(request, 'No existe la entrada')
        return redirect('particulares_admin')

    if request.method == 'POST':
        form = FormParticulares('c',request.POST, instance= obj)
        if form.is_valid():
            form.save()
            return redirect('particulares_admin')
        else:
            messages.error(request, 'Form invalido')
            return redirect('particulares_admin')
    form = FormParticulares('c', instance= obj)
    return render(request, 'tablas/add/add_particulares.html',{'form':form})

def edit_camiones(request, id):
    try:
        obj = Camiones.objects.get(pk=id)
    except Camiones.DoesNotExist:
        messages.error(request, 'No existe la entrada')
        return redirect('camiones_admin')

    if request.method == 'POST':
        form = FormCamiones(request.POST, instance= obj)
        if form.is_valid():
            num_camion = form.cleaned_data.get('num_registro')
            try:
                Remolques.objects.get(num_registro=num_camion)
            except:                             
                form.save()
                return redirect('camiones_admin')
            messages.error(request, 'Ese numero de registro ya esta en uso por un Remolque')
            return render(request, 'tablas/add/add_camiones.html',{'form':form}) 
        else:
            messages.error(request, 'Form invalido')
            return redirect('camiones_admin')
    form = FormCamiones(instance= obj)
    return render(request, 'tablas/add/add_camiones.html',{'form':form})

def edit_remolques(request, id):
    try:
        obj = Remolques.objects.get(pk=id)
    except Remolques.DoesNotExist:
        messages.error(request, 'No existe la entrada')
        return redirect('remolques_admin')
       
    if request.method == 'POST':
        form = FormRemolques(request.POST, instance= obj)
        if form.is_valid():
            num_remolque = form.cleaned_data.get('num_registro')
            try:
                Camiones.objects.get(num_registro=num_remolque)
            except:
                form.save()
                return redirect('remolques_admin')
            messages.error(request, 'Ese numero de registro ya esta en uso por un Camion')
            return render(request, 'tablas/add/add_remolques.html',{'form':form}) 
        else:
            messages.error(request, 'Form invalido')
            return redirect('remolques_admin')
    form = FormRemolques(instance= obj)
    return render(request, 'tablas/add/add_remolques.html',{'form':form})

def edit_contratos(request, id):
    try:
        obj = Contrartos.objects.get(pk=id)
    except Contrartos.DoesNotExist:
        messages.error(request, 'No existe la entrada')
        return redirect('contratos_admin')
  
    if request.method == 'POST':
        form = FormContratos(request.POST, instance= obj)
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
            messages.error(request, 'Form invalido')
            return redirect('add_contratos')
    form = FormContratos(instance= obj)
    return render(request, 'tablas/add/add_contratos.html',{'form':form})