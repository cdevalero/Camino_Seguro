from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index_admin, name="index_admin"),
    path('lugar_dir/', lugar_dir_admin, name="lugar_dir_admin"),
    path('companias/', companias_admin, name="companias_admin"),
    path('particulares/', particulares_admin, name="particulares_admin"),
    path('oficinas/', oficinas_admin, name="oficinas_admin"),
    path('camiones/', camiones_admin, name="camiones_admin"),
    path('remolques/', remolques_admin, name="remolques_admin"),
    path('contratos/', contratos_admin, name="contratos_admin"),
]
