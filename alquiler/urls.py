from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', registro_user, name="registro_user"),
]
