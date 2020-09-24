from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages

def registro_user(request):
    if request.method == 'POST':
        form = FormParticulares_cliente('c',request.POST)
        if form.is_valid():
            form.save()
            return redirect('particulares_admin')
        else:
            messages.error(request, 'Form invalido')
            return redirect('particulares_admin')
    form = FormParticulares_cliente('c')
    return render(request, 'register.html', {'form':form})