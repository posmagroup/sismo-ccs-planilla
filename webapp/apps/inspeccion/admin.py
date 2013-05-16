# -*- coding: utf8 -*-
from django.contrib import admin

from models import Entrevistado
from models import Direccion
from models import Condicion_Terreno
from models import Tipo_Estructural
from models import Uso
from models import Irregularidad
from models import Grado_Deterioro
from models import Periodo_Construccion
from models import Estructura
from models import Inspeccion

class Condicion_TerrenoAdmin(admin.ModelAdmin):

    class  Media:
        js = ("js/sismo_caracas_validaciones.js",)

class Tipo_EstructuralAdmin(admin.ModelAdmin):

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



class IrregularidadAdmin(admin.ModelAdmin):

    fieldsets = (
        (None, {
            'fields': (
                ('a_viga_alt','p_entrep_b'),
                ('p_column_c','disc_eje_c'),
                ('abert_losa', 'f_asim_mas'),
                ('aus_mur_1d','ados_los_l'),
                ('ados_los_c'),
                ('sep_edif'),

            )
        }),
        )

    class Media:
        css = {
            'all':("stylesheets/tipo_estructural.css",)
        }


class Grado_DeterioroAdmin(admin.ModelAdmin):

    fieldsets = (
        (None, {
            'fields': (
                ('ec_agri_es','ea_corr_ac'),
                ('agrietamie','e_mantenim'),


            )
        }),
    )

    class Media:
        css = {
            'all':("stylesheets/tipo_estructural.css",)
        }


class Periodo_ConstruccionAdmin(admin.ModelAdmin):

    class  Media:
        js = ("js/sismo_caracas_validaciones.js",)


# Adding UserProfile fields to the admin
# Define an inline admin descriptor for User model
# which acts a bit like a singleton
class EntrevistadoInline(admin.StackedInline):
    model = Entrevistado
    can_delete = False
    verbose_name_plural = 'Datos del Entrevistado'
    max_num = 1



# Adding UserProfile fields to the admin
# Define an inline admin descriptor for User model
# which acts a bit like a singleton
class EstructuraInline(admin.StackedInline):
    model = Estructura
    can_delete = False
    verbose_name_plural = 'Identificacion y ubicacion de la edificacion'
    max_num = 1



# Adding UserProfile fields to the admin
# Define an inline admin descriptor for User model
# which acts a bit like a singleton
class DireccionInline(admin.StackedInline):
    model = Direccion
    can_delete = False
    verbose_name_plural = 'Identificacion y ubicacion de la edificacion'
    max_num = 1


# Adding UserProfile fields to the admin
# Define an inline admin descriptor for User model
# which acts a bit like a singleton
class UsoInline(admin.StackedInline):
    model = Uso
    can_delete = False
    verbose_name_plural = 'Uso de la edificacion'
    max_num = 1
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


# Adding UserProfile fields to the admin
# Define an inline admin descriptor for User model
# which acts a bit like a singleton
class Periodo_ConstruccionInline(admin.StackedInline):
    model = Periodo_Construccion
    can_delete = False
    verbose_name_plural = 'Año de construccion'
    max_num = 1

    class  Media:
        js = ("js/sismo_caracas_validaciones.js",)

# Adding UserProfile fields to the admin
# Define an inline admin descriptor for User model
# which acts a bit like a singleton
class Condicion_TerrenoInline(admin.StackedInline):
    model = Condicion_Terreno
    can_delete = False
    verbose_name_plural = 'Condición del terreno'
    max_num = 1

    class  Media:
        js = ("js/sismo_caracas_validaciones.js",)



# Adding UserProfile fields to the admin
# Define an inline admin descriptor for User model
# which acts a bit like a singleton
class Tipo_EstructuralInline(admin.StackedInline):
    model = Tipo_Estructural
    can_delete = False
    verbose_name_plural = 'Tipo estructural'
    max_num = 1

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




# Adding UserProfile fields to the admin
# Define an inline admin descriptor for User model
# which acts a bit like a singleton
class IrregularidadInline(admin.StackedInline):
    model = Irregularidad
    can_delete = False
    verbose_name_plural = 'Irregularidades'
    max_num = 1

    fieldsets = (
        (None, {
            'fields': (
                ('a_viga_alt','p_entrep_b'),
                ('p_column_c','disc_eje_c'),
                ('abert_losa', 'f_asim_mas'),
                ('aus_mur_1d','ados_los_l'),
                ('ados_los_c'),
                ('sep_edif'),

                )
        }),
        )

    class Media:
        css = {
            'all':("stylesheets/tipo_estructural.css",)
        }



# Adding UserProfile fields to the admin
# Define an inline admin descriptor for User model
# which acts a bit like a singleton
class Grado_DeterioroInline(admin.StackedInline):
    model = Grado_Deterioro
    can_delete = False
    verbose_name_plural = 'Grado de deterioro'
    max_num = 1

    fieldsets = (
        (None, {
            'fields': (
                ('ec_agri_es','ea_corr_ac'),
                ('agrietamie','e_mantenim'),


                )
        }),
        )

    class Media:
        css = {
            'all':("stylesheets/tipo_estructural.css",)
        }



# Define a new User admin
class InspeccionAdmin(admin.ModelAdmin):
    inlines = ( EntrevistadoInline,EstructuraInline,DireccionInline, UsoInline,Periodo_ConstruccionInline,Condicion_TerrenoInline,Tipo_EstructuralInline, IrregularidadInline, Grado_DeterioroInline )
    verbose_name = 'Datos Generales'




admin.site.register(Entrevistado)
admin.site.register(Direccion)
admin.site.register(Estructura)
admin.site.register(Inspeccion,InspeccionAdmin)
admin.site.register(Grado_Deterioro,Grado_DeterioroAdmin)
admin.site.register(Uso,UsoAdmin)
admin.site.register(Irregularidad,IrregularidadAdmin)
admin.site.register(Tipo_Estructural,Tipo_EstructuralAdmin)
admin.site.register(Condicion_Terreno,Condicion_TerrenoAdmin)
admin.site.register(Periodo_Construccion,Periodo_ConstruccionAdmin)

