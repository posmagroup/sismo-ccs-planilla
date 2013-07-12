# -*- coding: utf8 -*-
from django.contrib.gis import admin
from floppyforms.gis.widgets import BaseOsmWidget
from forms import RequiredInlineFormSet
from django.forms.models import ModelForm
from django.contrib.gis.geos import MultiPolygon, Polygon
from django.contrib.gis.db import models
from olwidget.admin import GeoModelAdmin

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
from models import Anexo
from models import Poligono

#region  1.Poligono (Modelo Poligono)

#
#class PoligonoAdmin(admin.ModelAdmin):
#
#    class  Media:
#        js = ("js/sismo_caracas_validaciones.js",)
#        css = {
#            'all':("stylesheets/tipo_estructural.css",)
#        }


#    def get_model_perms(self, request):
#        """
#        Return empty perms dict thus hiding the model from admin index.
#        """
#        return {}

class PoligonoInline(admin.StackedInline):
    model = Poligono
    can_delete = False
    can_add = False
    verbose_name_plural = 'Poligono'
    max_num = 1


    class  Media:
        js = ("js/sismo_caracas_validaciones.js",)
        css = {
            'all':("stylesheets/tipo_estructural.css",)
        }

class PoligonoAdmin(GeoModelAdmin):


    options = {
        'default_lat': 44,
        'default_lon': -72,
        }



#endregion

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

    class Media:
        css = {
            'all':("stylesheets/tipo_estructural.css",)
        }

    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}

class EntrevistadoInline(admin.StackedInline):
    model = Entrevistado
    verbose_name_plural = 'Datos del Entrevistado'
    max_num = 1
    formset = RequiredInlineFormSet


    fieldsets = (
        (None, {
            'fields': (
                ('cod_ocup','nom_entrev'),
                ('tlf_entrev','email_entr'),

                )
        }),
        )

#endregion

#region  4.Identificación y ubicación de la edificación (Modelo Estructura)

class EstructuraAdmin(admin.OSMGeoAdmin):

    class Media:
        css = {
            'all':("stylesheets/tipo_estructural.css",)
        }
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}
#
class EstructuraInlineForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(EstructuraInlineForm, self).__init__(*args, **kwargs)
        estructura_admin = admin.site._registry[Estructura]
        model_field = self._meta.model._meta.get_field('poligono')
       # self.fields['poligono'].widget = estructura_admin.get_map_widget(model_field)()




class EstructuraInline(admin.StackedInline):
    model = Estructura
    form = EstructuraInlineForm
    can_delete = False
    verbose_name_plural = 'Identificación y ubicación de la edificación'
    max_num = 1

    fieldsets = (
        (None, {
            'fields': (
                ('nombre_n','n_pisos'),
                ('n_semi_sot','n_sotanos'),
                ('ciudad','urb_barrio'),
                ('sector','calle'),
                ('pto_referencia','poligono'),


                )
        }),
    )




#endregion

#region  5.Uso de la Edificación (Modelo Uso)

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
    verbose_name_plural = 'Uso de la edificación. (Debe seleccionar al menos uno).'
    max_num = 1
    formset = RequiredInlineFormSet
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
    verbose_name_plural = 'Capacidad de Ocupación. (Debe seleccionar al menos uno).'
    max_num = 1
    formset = RequiredInlineFormSet
    fieldsets = (
        (None, {
            'fields': (



                ('habitantes','t_o_manana','t_o_tarde','t_o_noche'),


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

    #exclude = ('fecha_inf',)

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
    #exclude = ('fecha_inf',)
    formset = RequiredInlineFormSet


    fieldsets = (
        (None, {
            'fields': (
                ('anio','periodo'),
                ('fecha_inf',),



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
    formset = RequiredInlineFormSet

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
    verbose_name_plural = 'Tipo estructural. (Debe seleccionar al menos uno).'
    max_num = 1
    formset = RequiredInlineFormSet

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
                ('tipo_predomi'),

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
    formset = RequiredInlineFormSet

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
    formset = RequiredInlineFormSet

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
    formset = RequiredInlineFormSet
    fieldsets = (
        (None, {
            'fields': (
                ('a_viga_alt','f_asim_mas'),
                ('aus_mur_1d','ados_los_l'),
                ('p_entrep_b', 'ados_los_c'),
                ('p_column_c','sep_edif'),
                ('disc_eje_c','estr_frag'),
                ('abert_losa'),

                )
        }),
    )

    class Media:
        css = {
            'all':("stylesheets/tipo_estructural.css",)
        }



#endregion

#region  13.Grados de deterioro (Modelo  Grado_Deterioro)



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
    formset = RequiredInlineFormSet
    fieldsets = (
        (None, {
            'fields': (
                ('ec_agri_es','agrietamie'),
                ('ea_corr_ac','e_mantenim'),


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
    verbose_name_plural = 'Observaciones (máximo 140 caracteres)'
    max_num = 1
    formset = RequiredInlineFormSet
    class  Media:
        js = ("js/sismo_caracas_validaciones.js",)




#endregion

#region  15.Anexos (Modelo Anexo)

class AnexoAdmin(admin.ModelAdmin):

    list_display = ('foto_facha', 'pla_esca', 'show_image')
    class  Media:
        js = ("js/sismo_caracas_validaciones.js",)

    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


class AnexoInline(admin.StackedInline):
    model = Anexo
    can_delete = False
    verbose_name_plural = 'Anexos'
    max_num = 1
    formset = RequiredInlineFormSet
    list_display = ('foto_facha', 'pla_esca', 'show_image')

    class  Media:
        js = ("js/sismo_caracas_validaciones.js",)










#endregion

#region  Admin (inlines )de  Inspeccion

class InspeccionAdmin(admin.GeoModelAdmin):
    inlines = ( EntrevistadoInline,EstructuraInline, UsoInline,Capacidad_OcupacionInline,Anio_ConstruccionInline,Condicion_TerrenoInline,Tipo_EstructuralInline,Esquema_PlantaInline,Esquema_ElevacionInline,IrregularidadInline, Grado_DeterioroInline,ObservacionInline,AnexoInline )

    verbose_name = 'Datos Generales'
    verbose_name_plural = 'Datos Generales'
    exclude = ('cod_pla',)

    class  Media:
        js = ("js/periodo_construccion.js","js/jquery.js","js/charCount.js","js/sismo_caracas_validaciones.js","js/widget_poligono.js")

       


#endregion

#region  Registro de modelos  en el admin
admin.site.register(Poligono, PoligonoAdmin)
admin.site.register(Participante,ParticipanteAdmin)
admin.site.register(Esquema_Planta,Esquema_PlantaAdmin)
admin.site.register(Esquema_Elevacion,Esquema_ElevacionAdmin)
admin.site.register(Entrevistado,EntrevistadoAdmin)
admin.site.register(Estructura, EstructuraAdmin)
admin.site.register(Capacidad_Ocupacion,Capacidad_OcupacionAdmin)
admin.site.register(Grado_Deterioro,Grado_DeterioroAdmin)
admin.site.register(Uso,UsoAdmin)
admin.site.register(Anexo,AnexoAdmin)
admin.site.register(Irregularidad,IrregularidadAdmin)
admin.site.register(Tipo_Estructural,Tipo_EstructuralAdmin)
admin.site.register(Condicion_Terreno,Condicion_TerrenoAdmin)
admin.site.register(Periodo_Construccion,Periodo_ConstruccionAdmin)
admin.site.register(Anio_Construccion,Anio_ConstruccionAdmin)
admin.site.register(Inspeccion,InspeccionAdmin)

#endregion