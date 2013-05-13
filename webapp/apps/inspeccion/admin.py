from django.contrib import admin

from models import Entrevistado
from models import Direccion
from models import Condicion_Terreno
from models import Tipo_Estructural
from models import Uso

class Condicion_TerrenoAdmin(admin.ModelAdmin):

    class  Media:
        js = ("js/sismo_caracas_validaciones.js",)

class Tipo_EstrcuturalAdmin(admin.ModelAdmin):

    fieldsets = (
        (None, {
            'fields': (
                ('pca','pcap'),
                ('mca2d','mca1d'),
                ('pa', 'papt'),
                ('pad','pac'),
                ('pre','mmc'),
                ('mmnc','vb'),
                ('vcp','n_pisos_cf'),
                ('n_pisos_nc','n_pisos_bc'),
                ('esq_planta','esq_elevac'),
            )
        }),
    )

    class Media:
        css = {
                'all':("stylesheets/tipo_estructural.css",)
        }


class UsoAdmin(admin.ModelAdmin):

    fieldsets = (
        (None, {
            'fields': (
                ('u_gubernam','u_bomberos'),
                ('u_pr_civil','u_policial'),
                ('u_militar', 'u_med_asis'),
                ('u_educativ','u_viv_pop'),
                ('u_viv_unif','u_viv_mult'),
                ('u_dep_recr','u_cultural'),
                ('u_industri','u_comercia'),
                ('u_oficina','u_religios'),
                ('u_otros'),
                )
        }),
        )

    class Media:
        css = {
            'all':("stylesheets/tipo_estructural.css",)
        }


admin.site.register(Entrevistado)
admin.site.register(Direccion)
admin.site.register(Uso,UsoAdmin)
admin.site.register(Tipo_Estructural,Tipo_EstrcuturalAdmin)
admin.site.register(Condicion_Terreno,Condicion_TerrenoAdmin)


