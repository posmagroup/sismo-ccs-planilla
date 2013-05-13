from django.contrib import admin

from models import Entrevistado
from models import Direccion
from models import Condicion_Terreno

class Condicion_TerrenoAdmin(admin.ModelAdmin):

    class  Media:
        js = ("js/sismo_caracas_validaciones.js",)




admin.site.register(Entrevistado)
admin.site.register(Direccion)
admin.site.register(Condicion_Terreno,Condicion_TerrenoAdmin)
