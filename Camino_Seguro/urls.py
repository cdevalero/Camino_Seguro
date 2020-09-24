from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('py_admin/', admin.site.urls),
    path('', include('alquiler.urls')),
    path('admin/', include('administracion.urls')),
]
