# -*- coding: utf8 -*-

from django.contrib.gis import admin
from django.contrib.admin import SimpleListFilter

from forms import RequiredInlineFormSet

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

from widgets import Select_Polygon_Widget


#region  1.Poligono (Modelo Poligono)
class PoligonoAdmin(admin.GeoModelAdmin):

    options = {
        'default_lat':  10.50882052,
        'default_lon': -66.89968507,
    }


#region  7.Año de Construccion (Modelo Periodo_Construccion y Anio_Construccion)
class Periodo_ConstruccionAdmin(admin.ModelAdmin):

    class  Media:
        js = ("js/periodo_construccion.js",)

    fieldsets = (
        (None, {
            'fields': (
                ('periodo', 'anio_inici', 'anio_fin'),
            )
        }),
    )


class ParticipanteInline(admin.StackedInline):
    model = Participante
    can_delete = False
    can_add = False
    verbose_name_plural = 'Datos de los participantes'
    max_num = 1

    class  Media:
        js = ("js/sismo_caracas_validaciones.js",)


class EntrevistadoInline(admin.StackedInline):
    model = Entrevistado
    verbose_name_plural = 'Datos del Entrevistado'
    max_num = 1
    formset = RequiredInlineFormSet

    fieldsets = (
        (None, {
            'fields': (
                ('cod_ocup', 'nom_entrev'),
                ('tlf_entrev', 'email_entr'),
            )
        }),
    )


class EstructuraInline(admin.StackedInline):
    model = Estructura
    can_delete = False
    verbose_name_plural = 'Identificación y ubicación de la edificación'
    max_num = 1
#    formfield_overrides = {
#        model.poligono : {'widget': Select_Polygon_Widget()},
#
#    }
    fieldsets = (
        (None, {
            'fields': (
                ('nombre_n', 'n_pisos'),
                ('n_semi_sot', 'n_sotanos'),
                ('ciudad', 'urb_barrio'),
                ('sector', 'calle'),
                ('pto_referencia', 'poligono'),
            )
        }),
    )

#    class Media:
#        css = {
#            "all": ("OpenLayers/theme/default/style.css","OpenLayers/style.css",)
#        }
#        js = ("OpenLayers/lib/OpenLayers.js",)


class UsoInline(admin.StackedInline):
    model = Uso
    can_delete = False
    verbose_name_plural = 'Uso de la edificación. (Debe seleccionar al menos uno).'
    max_num = 1
    formset = RequiredInlineFormSet
    fieldsets = (
        (None, {
            'fields': (
                ('u_gubernam', 'u_educativ'),
                ('u_bomberos', 'u_dep_recr'),
                ('u_pr_civil',  'u_cultural'),
                ('u_policial', 'u_industri'),
                ('u_militar', 'u_comercia'),
                ('u_viv_pop', 'u_oficina'),
                ('u_viv_unif', 'u_religios'),
                ('u_viv_mult', 'u_otros'),
                ('u_med_asis'),
                ('otro_uso')
            ),
        }),
    )

    class Media:
        css = {
            'all': ("stylesheets/tipo_estructural.css",)
        }


class Capacidad_OcupacionInline(admin.StackedInline):
    model = Capacidad_Ocupacion
    can_delete = False
    verbose_name_plural = 'Capacidad de Ocupación. (Debe seleccionar al menos uno).'
    max_num = 1
    formset = RequiredInlineFormSet
    fieldsets = (
        (None, {
            'fields': (
                ('habitantes', 't_o_manana', 't_o_tarde', 't_o_noche'),
            ),
        }),
    )

    class Media:
        css = {
            'all': ("stylesheets/tipo_estructural.css",)
        }


class Anio_ConstruccionInline(admin.StackedInline):
    model = Anio_Construccion
    can_delete = False
    verbose_name_plural = 'Año de construcción'
    max_num = 1
    #exclude = ('fecha_inf',)
    formset = RequiredInlineFormSet

    def periodo(self, instance):
        return sorted([(p.id, "%s" % p) for p in Periodo_Construccion.objects.all()])

    fieldsets = (
        (None, {
            'fields': (
                ('anio', 'periodo'),
                ('fecha_inf',),
            )
        }),
    )

    class  Media:
        js = ("js/sismo_caracas_validaciones.js",)



class Condicion_TerrenoInline(admin.StackedInline):
    model = Condicion_Terreno
    can_delete = False
    verbose_name_plural = 'Condición del terreno'
    max_num = 1
    formset = RequiredInlineFormSet

    class  Media:
        js = ("js/sismo_caracas_validaciones.js",)


class Tipo_EstructuralInline(admin.StackedInline):
    model = Tipo_Estructural
    can_delete = False
    verbose_name_plural = 'Tipo estructural. (Debe seleccionar al menos uno).'
    max_num = 1
    formset = RequiredInlineFormSet

    fieldsets = (
        (None, {
            'fields': (
                ('pca', 'pac'),
                ('pcap', 'pre'),
                ('mca2d', 'mmc'),
                ('mca1d', 'mmnc'),
                ('pa', 'pmbc'),
                ('papt', 'vb'),
                ('pad', 'vcp'),
                ('tipo_predomi'),
            )
        }),
    )

    class Media:
        css = {
            'all': ("stylesheets/tipo_estructural.css",)
        }


class Esquema_PlantaInline(admin.StackedInline):
    model = Esquema_Planta
    can_delete = False
    verbose_name_plural = 'Esquema de planta'
    max_num = 1
    formset = RequiredInlineFormSet

    class Media:
        css = {
            'all': ("stylesheets/tipo_estructural.css",)
        }


class Esquema_ElevacionInline(admin.StackedInline):
    model = Esquema_Elevacion
    can_delete = False
    verbose_name_plural = 'Esquema de Elevación'
    max_num = 1
    formset = RequiredInlineFormSet

    class Media:
        css = {
            'all': ("stylesheets/tipo_estructural.css",)
        }


class IrregularidadInline(admin.StackedInline):
    model = Irregularidad
    can_delete = False
    verbose_name_plural = 'Irregularidades'
    max_num = 1
    formset = RequiredInlineFormSet
    fieldsets = (
        (None, {
            'fields': (
                ('a_viga_alt', 'f_asim_mas'),
                ('aus_mur_1d', 'ados_los_l'),
                ('p_entrep_b', 'ados_los_c'),
                ('p_column_c', 'sep_edif'),
                ('disc_eje_c', 'estr_frag'),
                ('abert_losa'),
            )
        }),
    )

    class Media:
        css = {
            'all': ("stylesheets/tipo_estructural.css",)
        }


class Esquema_ElevacionInline(admin.StackedInline):
    model = Esquema_Elevacion
    can_delete = False
    verbose_name_plural = 'Esquema de Elevación'
    max_num = 1
    formset = RequiredInlineFormSet

    class Media:
        css = {
            'all': ("stylesheets/tipo_estructural.css",)
        }


class Esquema_ElevacionInline(admin.StackedInline):
    model = Esquema_Elevacion
    can_delete = False
    verbose_name_plural = 'Esquema de Elevación'
    max_num = 1
    formset = RequiredInlineFormSet

    class Media:
        css = {
            'all': ("stylesheets/tipo_estructural.css",)
        }


class Grado_DeterioroInline(admin.StackedInline):
    model = Grado_Deterioro
    can_delete = False
    verbose_name_plural = 'Grado de deterioro'
    max_num = 1
    formset = RequiredInlineFormSet
    fieldsets = (
        (None, {
            'fields': (
                ('ec_agri_es', 'agrietamie'),
                ('ea_corr_ac', 'e_mantenim'),
            )
        }),
    )

    class Media:
        css = {
            'all': ("stylesheets/tipo_estructural.css",)
        }


class ObservacionInline(admin.StackedInline):
    model = Observacion
    can_delete = False
    verbose_name_plural = 'Observaciones (máximo 140 caracteres)'
    max_num = 1
    formset = RequiredInlineFormSet

    class  Media:
        js = ("js/sismo_caracas_validaciones.js",)


class AnexoInline(admin.StackedInline):
    model = Anexo
    can_delete = False
    verbose_name_plural = 'Anexos'
    max_num = 1
    formset = RequiredInlineFormSet
    list_display = ('foto_facha', 'pla_esca', 'show_image')

    class  Media:
        js = ("js/sismo_caracas_validaciones.js",)


class YearOfInspectionFilter(SimpleListFilter):
    """ Adds a filter by 'periodo de construccion' to the admin list."""

    title = u"año de inspección"
    parameter_name = "year"

    def lookups(self, request, model_admin):
        return sorted([(p.id, "%s" % p) for p in Periodo_Construccion.objects.all()])

    def queryset(self, request, queryset):
        if self.value() is not None:
            return Inspeccion.objects.filter(anio_construccion__periodo=self.value)
        return Inspeccion.objects.all()


class TipoEstructuralFilter(SimpleListFilter):
    """ Adds a filter by 'tipo estructural' to the admin list."""

    title = u"tipología"
    parameter_name = "tipo"

    def lookups(self, request, model_admin):
        return Tipo_Estructural.TIPO_ESTRUCTURAL_PREDOMINANTE_CHOICES

    def queryset(self, request, queryset):
        if self.value() is not None:
            return Inspeccion.objects.filter(tipo_estructural__tipo_predomi=self.value)
        return Inspeccion.objects.all()


class InspeccionAdmin(admin.ModelAdmin):
    """ The main admin class"""

    inlines = (EntrevistadoInline, EstructuraInline, UsoInline, Capacidad_OcupacionInline,
               Anio_ConstruccionInline, Condicion_TerrenoInline, Tipo_EstructuralInline,
               Esquema_PlantaInline, Esquema_ElevacionInline, IrregularidadInline,
               Grado_DeterioroInline, ObservacionInline, AnexoInline)

    verbose_name = 'Datos Generales'
    verbose_name_plural = 'Datos Generales'
    exclude = ('cod_pla',)

    list_filter = (YearOfInspectionFilter, TipoEstructuralFilter)

    class  Media:
        js = ("js/jquery-1.8.2.min.js",
              "js/charCount.js",
              "js/periodo_construccion.js",
              "js/sismo_caracas_validaciones.js"
              )

        css = {
            'all': ("stylesheets/tipo_estructural.css",)
        }

admin.site.register(Poligono, PoligonoAdmin)
#admin.site.register(Participante, ParticipanteAdmin)
#admin.site.register(Esquema_Planta, Esquema_PlantaAdmin)
#admin.site.register(Esquema_Elevacion, Esquema_ElevacionAdmin)
#admin.site.register(Entrevistado, EntrevistadoAdmin)
#admin.site.register(Estructura, EstructuraAdmin)
#admin.site.register(Capacidad_Ocupacion, Capacidad_OcupacionAdmin)
#admin.site.register(Grado_Deterioro, Grado_DeterioroAdmin)
#admin.site.register(Uso, UsoAdmin)
#admin.site.register(Anexo, AnexoAdmin)
#admin.site.register(Irregularidad, IrregularidadAdmin)
#admin.site.register(Tipo_Estructural, Tipo_EstructuralAdmin)
#admin.site.register(Condicion_Terreno, Condicion_TerrenoAdmin)
admin.site.register(Periodo_Construccion, Periodo_ConstruccionAdmin)
#admin.site.register(Anio_Construccion, Anio_ConstruccionAdmin)
admin.site.register(Inspeccion, InspeccionAdmin)
