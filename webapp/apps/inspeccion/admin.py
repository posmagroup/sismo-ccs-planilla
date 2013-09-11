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

from forms import EstructuraInlineForm


class PoligonoAdmin(admin.GeoModelAdmin):
    options = {
        'default_lat':  10.50882052,
        'default_lon': -66.89968507,
    }


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
    """
    """

    model = Participante
    formset = RequiredInlineFormSet
    can_delete = False
    can_add = False
    verbose_name_plural = 'Datos de los participantes'
    max_num = 1


class EntrevistadoInline(admin.StackedInline):
    """
    """

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
    """
        Clase que permite inlcuir el modelo
        como un inline en el admin de inspeccion.
        Usa el form 'RequiredInlineFormSet(forms.py)'
        para mantener las validaciones propias del admin
        de este modelo.

        En esta clase es que se debe sobreescribir el form
        para estructura para que use EstructuraInlineForm (forms.py)
        que es el form que llama al widget de los mapas
        Ejemplo : form=EstructuraInlineForm

    """
    model = Estructura
    can_delete = False
    verbose_name_plural = 'Identificación y ubicación de la edificación'
    max_num = 1

    fieldsets = (  # Redefine que campos se muestran y como se agrupan
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


class UsoInline(admin.StackedInline):
    """
    """

    model = Uso
    can_delete = False
    verbose_name_plural = 'Uso de la edificación. (Debe seleccionar al menos uno).'
    max_num = 1
    formset = RequiredInlineFormSet
    fieldsets = (  # Redefine que campos se muestran y como se agrupan
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
    """
    """

    model = Capacidad_Ocupacion
    can_delete = False
    verbose_name_plural = 'Capacidad de Ocupación. (Debe seleccionar al menos uno).'
    max_num = 1
    formset = RequiredInlineFormSet
    fieldsets = (  # Redefine que campos se muestran y como se agrupan
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
    """
    """

    model = Anio_Construccion
    can_delete = False
    verbose_name_plural = 'Año de construcción'
    max_num = 1
    formset = RequiredInlineFormSet

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
    """
    """

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
    """
    """
    
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
    """
    """
    
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
    """
    """

    model = Irregularidad
    can_delete = False
    verbose_name_plural = 'Irregularidades'
    max_num = 1
    formset = RequiredInlineFormSet
    fieldsets = (  # Redefine que campos se muestran y como se agrupan
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
    """
    """

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
    """
    """

    model = Grado_Deterioro
    can_delete = False
    verbose_name_plural = 'Grado de deterioro'
    max_num = 1
    formset = RequiredInlineFormSet
    fieldsets = (  # Redefine que campos se muestran y como se agrupan
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
    """
    """

    model = Observacion
    can_delete = False
    verbose_name_plural = 'Observaciones (máximo 500 caracteres)'
    max_num = 1
    formset = RequiredInlineFormSet

    class  Media:
        js = ("js/sismo_caracas_validaciones.js",)


class AnexoInline(admin.StackedInline):
    """
    """

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

    title = u"año de inspección."
    parameter_name = "year"

    def lookups(self, request, model_admin):
        return sorted([(p.id, "%s" % p) for p in Periodo_Construccion.objects.all()])

    def queryset(self, request, queryset):
        if self.value() is not None:
            return Inspeccion.objects.filter(anio_construccion__periodo=self.value)


class TipoEstructuralFilter(SimpleListFilter):
    """ Adds a filter by 'tipo estructural' to the admin list."""

    title = u"tipología estructural predominante."
    parameter_name = "tipo"

    def lookups(self, request, model_admin):
        return Tipo_Estructural.TIPO_ESTRUCTURAL_PREDOMINANTE_CHOICES

    def queryset(self, request, queryset):
        if self.value() is not None:
            return Inspeccion.objects.filter(tipo_estructural__tipo_predomi=self.value)


# Actions
def return_csv(self, request, queryset):
        import csv
        from django.http import HttpResponse
        """ Acción para el admin que retorna las inspecciones seleccionadas como un CSV """
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="listado_inspecciones_sismocaracas.csv"'
        writer = csv.writer(response)
        for obj in queryset:
            writer.writerow(['Identificador', 'Fecha de Inspección', 'Hora de Inicio', 'Hora de Finalización'])
            writer.writerow([
                            "%s," % obj.id,
                            "%s," % obj.fecha,
                            "%s," % obj.hor_inicio,
                            "%s," % obj.hora_fin,
                            ])

        return response

return_csv.short_description = "Generar archivo separado por comas (CSV)"


class InspeccionAdmin(admin.ModelAdmin):
    """ The main admin class"""

    inlines = (EntrevistadoInline, EstructuraInline, UsoInline, Capacidad_OcupacionInline,
               Anio_ConstruccionInline, Condicion_TerrenoInline, Tipo_EstructuralInline,
               Esquema_PlantaInline, Esquema_ElevacionInline, IrregularidadInline,
               Grado_DeterioroInline, ObservacionInline, AnexoInline)

    verbose_name = 'Datos Generales'
    verbose_name_plural = 'Datos Generales'
    exclude = ('cod_pla',)

    list_filter = [YearOfInspectionFilter, TipoEstructuralFilter]
    list_display = ('cod_insp', 'tipo_str_predom', 'anio_const',)
    actions = [return_csv]

    def anio_const(self, obj):
        """ Retorna el año de inspección """
        return "%s" % obj.anio_construccion_set.all()[0].anio

    def cod_insp(self, obj):
        """ Retorna el código de la inspección """
        return "Inspección %s" % obj.id

    def tipo_str_predom(self, obj):
        """ Retorna el tipo de estructura predominante """
        tipo = obj.tipo_estructural_set.all()[0]
        valor = tipo.TIPO_ESTRUCTURAL_PREDOMINANTE_CHOICES[int(tipo.tipo_predomi)]
        return "%s" % valor[1]

    class  Media:
        js = ("js/jquery-1.8.2.min.js",
              "js/charCount.js",
              "js/periodo_construccion.js",
              "js/sismo_caracas_validaciones.js"
              )

        css = {
            'all': ("stylesheets/tipo_estructural.css",)
        }

    # Short descriptions for listing
    anio_const.short_description = "Año de Construcción"
    cod_insp.short_description = "Código de la Inspección"
    tipo_str_predom.short_description = "Tipo Estructural Predominante"


admin.site.register(Poligono, PoligonoAdmin)
admin.site.register(Periodo_Construccion, Periodo_ConstruccionAdmin)
admin.site.register(Inspeccion, InspeccionAdmin)
