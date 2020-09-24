from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('registro/persona', registro_user_persona, name="registro_user_persona"),
    path('registro/compania', registro_user_compania, name="registro_user_compania"),
    path('registro/opcion', registro_user_opcion, name="registro_user_opcion"),
    path('', inicio_user, name="inicio_user"),
]
