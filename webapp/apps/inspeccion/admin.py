# -*- coding: utf8 -*-
from django.contrib import admin

from models import Entrevistado
from models import Condicion_Terreno
from models import Tipo_Estructural
from models import Uso
from models import Irregularidad
from models import Grado_Deterioro
from models import Periodo_Construccion
from models import Estructura
from models import Inspeccion
from models import Anio_Construccion
from models import Participante
from models import Capacidad_Ocupacion
from models import Observacion
from models import Esquema_Planta
from models import Esquema_Elevacion

#region  2.Datos de los participantes (Modelo Participante)

class ParticipanteAdmin(admin.ModelAdmin):

    class  Media:
        js = ("js/sismo_caracas_validaciones.js",)
        css = {
            'all':("stylesheets/tipo_estructural.css",)
        }


    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}

class ParticipanteInline(admin.StackedInline):
    model = Participante
    can_delete = False
    can_add = False
    verbose_name_plural = 'Datos de los participantes'
    max_num = 1

    class  Media:
        js = ("js/sismo_caracas_validaciones.js",)

#endregion

#region  3.Datos del entrevistado (Modelo Entrevistado)

class EntrevistadoAdmin(admin.ModelAdmin):

    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}

class EntrevistadoInline(admin.StackedInline):
    model = Entrevistado
    can_delete = False
    verbose_name_plural = 'Datos del Entrevistado'
    max_num = 1


    fieldsets = (
        (None, {
            'fields': (
                ('cod_ocup','nom_entrev'),
                ('tlf_entrev','email_entr'),

                )
        }),
        )

#endregion

#region  4.Identificación y ubicaicón de la edificación (Modelo Estructura)

class EstructuraAdmin(admin.ModelAdmin):

    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}

class EstructuraInline(admin.StackedInline):
    model = Estructura
    can_delete = False
    verbose_name_plural = 'Identificación y ubicación de la edificación'
    max_num = 1

    fieldsets = (
        (None, {
            'fields': (
                ('nombre_n','n_pisos'),
                ('n_semi_sot','n_sotanos'),
                ('ciudad','municipio'),
                ('parroquia','urb_barrio'),
                ('sector','calle'),
                ('manzana','parcela','pto_referencia'),


                )
        }),
        )

#endregion

#region  5.uso de la Edificación (Modelo Uso)

class UsoAdmin(admin.ModelAdmin):

    fieldsets = (
        (None, {
            'fields': (


                ('u_gubernam','u_educativ'),
                ('u_bomberos','u_dep_recr'),
                ('u_pr_civil', 'u_cultural'),
                ('u_policial','u_industri'),
                ('u_militar','u_comercia'),
                ('u_viv_pop','u_oficina'),
                ('u_viv_unif','u_religios'),
                ('u_viv_mult','u_otros'),
                ('u_med_asis'),
                ),
            }),
        )

    class Media:
        css = {
            'all':("stylesheets/tipo_estructural.css",)
        }

    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}

class UsoInline(admin.StackedInline):
    model = Uso
    can_delete = False
    verbose_name_plural = 'Uso de la edificación'
    max_num = 1
    fieldsets = (
        (None, {
            'fields': (


                ('u_gubernam','u_educativ'),
                ('u_bomberos','u_dep_recr'),
                ('u_pr_civil', 'u_cultural'),
                ('u_policial','u_industri'),
                ('u_militar','u_comercia'),
                ('u_viv_pop','u_oficina'),
                ('u_viv_unif','u_religios'),
                ('u_viv_mult','u_otros'),
                ('u_med_asis'),
                ('otro_uso')
                ),
            }),
        )

    class Media:
        css = {
            'all':("stylesheets/tipo_estructural.css",)
        }


#endregion

#region  6.Capacidad de Ocupación (Modelo Capacidad_Ocupación)


class Capacidad_OcupacionAdmin(admin.ModelAdmin):

    fieldsets = (
        (None, {
            'fields': (


                ('habitantes','t_o_manana'),
                ('t_o_tarde','t_o_noche'),


                ),
            }),
        )

    class Media:
        css = {
            'all':("stylesheets/tipo_estructural.css",)
        }

    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}

class Capacidad_OcupacionInline(admin.StackedInline):
    model = Capacidad_Ocupacion
    can_delete = False
    verbose_name_plural = 'Capacidad de Ubicación'
    max_num = 1
    fieldsets = (
        (None, {
            'fields': (


                ('habitantes','t_o_manana'),
                ('t_o_tarde','t_o_noche'),


                ),
            }),
        )


    class Media:
        css = {
            'all':("stylesheets/tipo_estructural.css",)
        }
#endregion

#region  7.Año de Construccion (Modelo Periodo_Construccion y Anio_Construccion)


class Periodo_ConstruccionAdmin(admin.ModelAdmin):

    class  Media:
        js = ("js/periodo_construccion.js",)

    fieldsets = (
        (None, {
            'fields': (
                ('periodo','anio_inici', 'anio_fin'),



                )
        }),
        )


class Anio_ConstruccionAdmin(admin.ModelAdmin):

    exclude = ('fecha_inf',)

    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


class Anio_ConstruccionInline(admin.StackedInline):
    model = Anio_Construccion
    can_delete = False
    verbose_name_plural = 'Año de construcción'
    max_num = 1
    exclude = ('fecha_inf',)


    fieldsets = (
        (None, {
            'fields': (
                ('anio','periodo'),



                )
        }),
        )


    class  Media:
        js = ("js/sismo_caracas_validaciones.js",)


#endregion

#region  8.Condicion del terreno (Modelo Condicion_Terreno)


class Condicion_TerrenoAdmin(admin.ModelAdmin):

    class  Media:
        js = ("js/sismo_caracas_validaciones.js",)

    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


class Condicion_TerrenoInline(admin.StackedInline):
    model = Condicion_Terreno
    can_delete = False
    verbose_name_plural = 'Condición del terreno'
    max_num = 1

    class  Media:
        js = ("js/sismo_caracas_validaciones.js",)

#endregion

#region  9.Tipo Estructural (Modelo Tipo_Estructural)


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
                ('vcp'),
#                ('n_pisos_nc','n_pisos_bc'),
#                ('esq_planta','esq_elevac'),
                )
        }),
        )

    class Media:
        css = {
            'all':("stylesheets/tipo_estructural.css",)
        }

    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}



class Tipo_EstructuralInline(admin.StackedInline):
    model = Tipo_Estructural
    can_delete = False
    verbose_name_plural = 'Tipo estructural'
    max_num = 1


    fieldsets = (
        (None, {
            'fields': (
                ('pca','pac'),
                ('pcap','pre'),
                ('mca2d', 'mmc'),
                ('mca1d','mmnc'),
                ('pa','pmbc'),
                ('papt','vb'),
                ('pad','vcp'),
                #('n_pisos_nc','n_pisos_bc'),
                #                ('esq_planta','esq_elevac'),
                )
        }),
        )




class Media:
        css = {
            'all':("stylesheets/tipo_estructural.css",)
        }


#endregion

#region  10.Esquema Planta (Modelo Esquema_Planta)



class Esquema_PlantaAdmin(admin.ModelAdmin):


    class Media:
        css = {
            'all':("stylesheets/tipo_estructural.css",)
        }

    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}





class Esquema_PlantaInline(admin.StackedInline):
    model = Esquema_Planta
    can_delete = False
    verbose_name_plural = 'Esquema de planta'
    max_num = 1


    class Media:
        css = {
            'all':("stylesheets/tipo_estructural.css",)
        }
#endregion

#region  11.Esquema de Elevaciòn (Modelo Esquema_Elevacion)



class Esquema_ElevacionAdmin(admin.ModelAdmin):


    class Media:
        css = {
            'all':("stylesheets/tipo_estructural.css",)
        }

    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}





class Esquema_ElevacionInline(admin.StackedInline):
    model = Esquema_Elevacion
    can_delete = False
    verbose_name_plural = 'Esquema de Elevación'
    max_num = 1


    class Media:
        css = {
            'all':("stylesheets/tipo_estructural.css",)
        }
#endregion

#region  12.Irregularidades (Modelo Irregularidad)

class IrregularidadAdmin(admin.ModelAdmin):


    class Media:
        css = {
            'all':("stylesheets/tipo_estructural.css",)
        }

    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}




class IrregularidadInline(admin.StackedInline):
    model = Irregularidad
    can_delete = False
    verbose_name_plural = 'Irregularidades'
    max_num = 1

    fieldsets = (
        (None, {
            'fields': (
                ('a_viga_alt','f_asim_mas'),
                ('p_entrep_b','aus_mur_1d'),
                ('p_column_c', 'ados_los_l'),
                ('disc_eje_c','ados_los_c'),
                ('abert_losa','sep_edif'),

                )
        }),
    )

    class Media:
        css = {
            'all':("stylesheets/tipo_estructural.css",)
        }



#endregion

#region  14.Observaciones (Modelo Observacion)


class ObservacionAdmin(admin.ModelAdmin):

    class  Media:
        js = ("js/sismo_caracas_validaciones.js",)

    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}

class ObservacionInline(admin.StackedInline):
    model = Observacion
    can_delete = False
    verbose_name_plural = 'Observaciones'
    max_num = 1

    class  Media:
        js = ("js/sismo_caracas_validaciones.js",)




#endregion





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

    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}










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




class InspeccionAdmin(admin.ModelAdmin):
    inlines = ( ParticipanteInline,EntrevistadoInline,EstructuraInline, UsoInline,Capacidad_OcupacionInline,Anio_ConstruccionInline,Condicion_TerrenoInline,Tipo_EstructuralInline,Esquema_PlantaInline,Esquema_ElevacionInline,IrregularidadInline, Grado_DeterioroInline,ObservacionInline )
    verbose_name = 'Datos Generales'
    verbose_name_plural = 'Datos Generales'




#region  Registro de modelos  en el admin

admin.site.register(Participante,ParticipanteAdmin)
admin.site.register(Esquema_Planta,Esquema_PlantaAdmin)
admin.site.register(Esquema_Elevacion,Esquema_ElevacionAdmin)
admin.site.register(Entrevistado,EntrevistadoAdmin)
admin.site.register(Estructura, EstructuraAdmin)
admin.site.register(Inspeccion,InspeccionAdmin)
admin.site.register(Capacidad_Ocupacion,Capacidad_OcupacionAdmin)
admin.site.register(Grado_Deterioro,Grado_DeterioroAdmin)
admin.site.register(Uso,UsoAdmin)
admin.site.register(Irregularidad,IrregularidadAdmin)
admin.site.register(Tipo_Estructural,Tipo_EstructuralAdmin)
admin.site.register(Condicion_Terreno,Condicion_TerrenoAdmin)
admin.site.register(Periodo_Construccion,Periodo_ConstruccionAdmin)
admin.site.register(Anio_Construccion,Anio_ConstruccionAdmin)


#endregion