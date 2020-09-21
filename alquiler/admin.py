from django.contrib import admin

from alquiler.models import *

# admin se encarga de agragarlo
admin.site.register([Camiones, Companias, Lugares_Dir, Oficinas, Remolques, Particulares, Contrartos])