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

    path('lugar_dir/add/', add_lugar_dir, name="add_lugar_dir"),
    path('oficinas/add/', add_oficinas, name="add_oficinas"),
    path('companias/add/', add_companias, name="add_companias"),
    path('particulares/add/', add_particulares, name="add_particulares"),
    path('camiones/add/', add_camiones, name="add_camiones"),
    path('remolques/add/', add_remolques, name="add_remolques"),
    path('contratos/add/', add_contratos, name="add_contratos"),

    path('lugar_dir/delete/<int:id>', delete_lugar_dir, name="delete_lugar_dir"),
    path('oficinas/delete/<int:id>', delete_oficinas, name="delete_oficinas"),
    path('companias/delete/<int:id>', delete_companias, name="delete_companias"),
    path('particulares/delete/<int:id>', delete_particulares, name="delete_particulares"),
    path('camiones/delete/<int:id>', delete_camiones, name="delete_camiones"),
    path('remolques/delete/<int:id>', delete_remolques, name="delete_remolques"),
    path('contratos/delete/<int:id>', delete_contratos, name="delete_contratos"),

    path('lugar_dir/edit/<int:id>', edit_lugar_dir, name="edit_lugar_dir"),
    path('oficinas/edit/<int:id>', edit_oficinas, name="edit_oficinas"),
    path('companias/edit/<int:id>', edit_companias, name="edit_companias"),
    path('particulares/edit/<int:id>', edit_particulares, name="edit_particulares"),
    path('camiones/edit/<int:id>', edit_camiones, name="edit_camiones"),
    path('remolques/edit/<int:id>', edit_remolques, name="edit_remolques"),
    path('contratos/edit/<int:id>', edit_contratos, name="edit_contratos"),

    path('lugar_dir/ciudades/', lugar_dir_ciudades, name="lugar_dir_ciudades"),
    path('lugar_dir/estados/', lugar_dir_estados, name="lugar_dir_estados"),
    
]
