# -*- coding: utf8 -*-
from django.contrib.gis import admin

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
from forms import RequiredInlineFormSet

#region  Admin Poligono

class PoligonoAdmin(admin.GeoModelAdmin):
    """
        Admin de la clase Poligono.
        Hereda de GeoModelAdmin permitiendo
        que django se encarge de la visualizacion
        de los poligonos.
    """

    options = {
        'default_lat':  10.50882052,
        'default_lon': -66.89968507,
        }

#endregion
#region Admin Participante
class ParticipanteAdmin(admin.ModelAdmin):
    """
        Admin de la clase Participante.
    """
    def get_model_perms(self, request):
        """
            Sobreescritura del metodo de los permisos.
            Se devuelve una lista vacia para que este
            modelo no se muestre en el admin pero aun
            permita incluirlo como inline dentro de
            inspeccion

        """
        return {}
#endregion
#region Inline Participante
class ParticipanteInline(admin.StackedInline):
    """
        Clase que permite inlcuir el modelo
        como un inline en el admin de inspeccion.
        Usa el form 'RequiredInlineFormSet(forms.py)'
        para mantener las validaciones propias del admin
        de este modelo
    """
    model = Participante
    formset = RequiredInlineFormSet
    can_delete = False
    can_add = False
    verbose_name_plural = 'Datos de los participantes'
    max_num = 1
#endregion
#region Admin Entrevistado

class EntrevistadoAdmin(admin.ModelAdmin):
    """
        Admin de la clase Entrevistado.
    """

    def get_model_perms(self, request):
        """
            Sobreescritura del metodo de los permisos.
            Se devuelve una lista vacia para que este
            modelo no se muestre en el admin pero aun
            permita incluirlo como inline dentro de
            inspeccion

        """
        return {}
#endregion
#region Inline Entrevistado
class EntrevistadoInline(admin.StackedInline):
    """
        Clase que permite inlcuir el modelo
        como un inline en el admin de inspeccion.
        Usa el form 'RequiredInlineFormSet(forms.py)'
        para mantener las validaciones propias del admin
        de este modelo
    """
    model = Entrevistado
    verbose_name_plural = 'Datos del Entrevistado'
    max_num = 1
    formset = RequiredInlineFormSet

    fieldsets = ( #Redefine que campos se muestran y como se agrupan
        (None, {
            'fields': (
                ('cod_ocup','nom_entrev'),
                ('tlf_entrev','email_entr'),

                )
        }),
        )

#endregion
#region Admin Estructura
class EstructuraAdmin(admin.ModelAdmin):
    """
        Admin de la clase Estructura.
    """
    def get_model_perms(self, request):
        """
            Sobreescritura del metodo de los permisos.
            Se devuelve una lista vacia para que este
            modelo no se muestre en el admin pero aun
            permita incluirlo como inline dentro de
            inspeccion

        """
        return {}
#endregion
#region Inline Estructura
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

    fieldsets = ( #Redefine que campos se muestran y como se agrupan
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
#region Admin Uso
class UsoAdmin(admin.ModelAdmin):
    """
        Admin de la clase Uso.
    """
    fieldsets = (#Redefine que campos se muestran y como se agrupan
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

    def get_model_perms(self, request):
        """
            Sobreescritura del metodo de los permisos.
            Se devuelve una lista vacia para que este
            modelo no se muestre en el admin pero aun
            permita incluirlo como inline dentro de
            inspeccion

        """
        return {}
#endregion
#region Inline Uso
class UsoInline(admin.StackedInline):
    """
        Clase que permite inlcuir el modelo
        como un inline en el admin de inspeccion.
        Usa el form 'RequiredInlineFormSet(forms.py)'
        para mantener las validaciones propias del admin
        de este modelo.
    """
    model = Uso
    can_delete = False
    verbose_name_plural = 'Uso de la edificación. (Debe seleccionar al menos uno).'
    max_num = 1
    formset = RequiredInlineFormSet
    fieldsets = ( #Redefine que campos se muestran y como se agrupan
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

#endregion
#region Admin Capacidad_Ocupación
class Capacidad_OcupacionAdmin(admin.ModelAdmin):
    """
        Admin de la clase Capacidad_Ocupacion.
    """
    fieldsets = ( #Redefine que campos se muestran y como se agrupan
        (None, {
            'fields': (

                ('habitantes','t_o_manana'),
                ('t_o_tarde','t_o_noche'),

                ),
            }),
        )

    def get_model_perms(self, request):
        """
            Sobreescritura del metodo de los permisos.
            Se devuelve una lista vacia para que este
            modelo no se muestre en el admin pero aun
            permita incluirlo como inline dentro de
            inspeccion

        """
        return {}
#endregion
#region Inline Capacidad_Ocupacion
class Capacidad_OcupacionInline(admin.StackedInline):
    """
        Clase que permite inlcuir el modelo
        como un inline en el admin de inspeccion.
        Usa el form 'RequiredInlineFormSet(forms.py)'
        para mantener las validaciones propias del admin
        de este modelo
    """
    model = Capacidad_Ocupacion
    can_delete = False
    verbose_name_plural = 'Capacidad de Ocupación. (Debe seleccionar al menos uno).'
    max_num = 1
    formset = RequiredInlineFormSet
    fieldsets = ( #Redefine que campos se muestran y como se agrupan
        (None, {
            'fields': (



                ('habitantes','t_o_manana','t_o_tarde','t_o_noche'),


                ),
            }),
        )
#endregion
#region Admin Periodo_Construccion
class Periodo_ConstruccionAdmin(admin.ModelAdmin):
    """
        Admin de la clase  Periodo_Construccion.
    """
    fieldsets = ( #Redefine que campos se muestran y como se agrupan
        (None, {
            'fields': (
                ('periodo','anio_inici', 'anio_fin'),

                )
        }),
        )
    class  Media:
        js = ("js/periodo_construccion.js",)


#endregion
#region Admin Anio_Construccion
class Anio_ConstruccionAdmin(admin.ModelAdmin):
    """
        Admin de la clase  Anio_Construccion..
    """
    def get_model_perms(self, request):
        """
            Sobreescritura del metodo de los permisos.
            Se devuelve una lista vacia para que este
            modelo no se muestre en el admin pero aun
            permita incluirlo como inline dentro de
            inspeccion

        """
        return {}
#endregion
#region Inline Anio_Construccion
class Anio_ConstruccionInline(admin.StackedInline):
    """
        Clase que permite inlcuir el modelo
        como un inline en el admin de inspeccion.
        Usa el form 'RequiredInlineFormSet(forms.py)'
        para mantener las validaciones propias del admin
        de este modelo
    """
    model = Anio_Construccion
    can_delete = False
    verbose_name_plural = 'Año de construcción'
    max_num = 1
    formset = RequiredInlineFormSet

    fieldsets = ( #Redefine que campos se muestran y como se agrupan
        (None, {
            'fields': (
                ('anio','periodo'),
                ('fecha_inf',),



                )
        }),
        )
#endregion
#region  Admin  Condicion_Terreno
class Condicion_TerrenoAdmin(admin.ModelAdmin):
    """
        Admin de la clase  Condicion_Terreno..
    """
    def get_model_perms(self, request):
        """
            Sobreescritura del metodo de los permisos.
            Se devuelve una lista vacia para que este
            modelo no se muestre en el admin pero aun
            permita incluirlo como inline dentro de
            inspeccion

        """
        return {}
#endregion
#region Inline Condicion_Terreno
class Condicion_TerrenoInline(admin.StackedInline):
    """
        Clase que permite inlcuir el modelo
        como un inline en el admin de inspeccion.
        Usa el form 'RequiredInlineFormSet(forms.py)'
        para mantener las validaciones propias del admin
        de este modelo
    """
    model = Condicion_Terreno
    can_delete = False
    verbose_name_plural = 'Condición del terreno'
    max_num = 1
    formset = RequiredInlineFormSet

#endregion
#region Admin Tipo_Estructural
class Tipo_EstructuralAdmin(admin.ModelAdmin):
    """
        Admin de la clase  Tipo_Estructural.
    """
    fieldsets = ( #Redefine que campos se muestran y como se agrupan
        (None, {
            'fields': (
                ('pca','pcap'),
                ('mca2d','mca1d'),
                ('pa', 'papt'),
                ('pad','pac'),
                ('pre','mmc'),
                ('mmnc','vb'),
                ('vcp'),
                )
        }),
        )

    def get_model_perms(self, request):
        """
            Sobreescritura del metodo de los permisos.
            Se devuelve una lista vacia para que este
            modelo no se muestre en el admin pero aun
            permita incluirlo como inline dentro de
            inspeccion

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
#region  Admin Esquema_Planta
class Esquema_PlantaAdmin(admin.ModelAdmin):
    """
        Admin de la clase  Esquema_Planta.
    """
    def get_model_perms(self, request):
        """
            Sobreescritura del metodo de los permisos.
            Se devuelve una lista vacia para que este
            modelo no se muestre en el admin pero aun
            permita incluirlo como inline dentro de
            inspeccion

        """
        return {}
#endregion
#region Inline Esquema_Planta
class Esquema_PlantaInline(admin.StackedInline):
    """
        Clase que permite inlcuir el modelo
        como un inline en el admin de inspeccion.
        Usa el form 'RequiredInlineFormSet(forms.py)'
        para mantener las validaciones propias del admin
        de este modelo
    """
    model = Esquema_Planta
    can_delete = False
    verbose_name_plural = 'Esquema de planta'
    max_num = 1
    formset = RequiredInlineFormSet
#endregion
#region  Admin Esquema_Elevacion
class Esquema_ElevacionAdmin(admin.ModelAdmin):
    """
        Admin de la clase  Esquema_Planta.
    """
    def get_model_perms(self, request):
        """
            Sobreescritura del metodo de los permisos.
            Se devuelve una lista vacia para que este
            modelo no se muestre en el admin pero aun
            permita incluirlo como inline dentro de
            inspeccion

        """
        return {}
#endregion
#region Inline Esquema_Elevacion
class Esquema_ElevacionInline(admin.StackedInline):
    """
        Clase que permite inlcuir el modelo
        como un inline en el admin de inspeccion.
        Usa el form 'RequiredInlineFormSet(forms.py)'
        para mantener las validaciones propias del admin
        de este modelo
    """
    model = Esquema_Elevacion
    can_delete = False
    verbose_name_plural = 'Esquema de Elevación'
    max_num = 1
    formset = RequiredInlineFormSet
#endregion
#region  Admin  Irregularidad
class IrregularidadAdmin(admin.ModelAdmin):
    """
        Admin de la clase Irregularidad.
    """
    def get_model_perms(self, request):
        """
            Sobreescritura del metodo de los permisos.
            Se devuelve una lista vacia para que este
            modelo no se muestre en el admin pero aun
            permita incluirlo como inline dentro de
            inspeccion

        """
        return {}
#endregion
#region Inline Irregularidad
class IrregularidadInline(admin.StackedInline):
    """
        Clase que permite inlcuir el modelo
        como un inline en el admin de inspeccion.
        Usa el form 'RequiredInlineFormSet(forms.py)'
        para mantener las validaciones propias del admin
        de este modelo
    """
    model = Irregularidad
    can_delete = False
    verbose_name_plural = 'Irregularidades'
    max_num = 1
    formset = RequiredInlineFormSet
    fieldsets = ( #Redefine que campos se muestran y como se agrupan
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
#endregion
#region  Admin Grado_Deterioro
class Grado_DeterioroAdmin(admin.ModelAdmin):
    """
        Admin de la clase Irregularidad.
    """
    fieldsets = ( #Redefine que campos se muestran y como se agrupan
        (None, {
            'fields': (
                ('ec_agri_es','ea_corr_ac'),
                ('agrietamie','e_mantenim'),


                )
        }),
        )

    def get_model_perms(self, request):
        """
            Sobreescritura del metodo de los permisos.
            Se devuelve una lista vacia para que este
            modelo no se muestre en el admin pero aun
            permita incluirlo como inline dentro de
            inspeccion

        """
        return {}
#endregion
#region Inline Grado_Deterioro
class Grado_DeterioroInline(admin.StackedInline):
    """
        Clase que permite inlcuir el modelo
        como un inline en el admin de inspeccion.
        Usa el form 'RequiredInlineFormSet(forms.py)'
        para mantener las validaciones propias del admin
        de este modelo
    """
    model = Grado_Deterioro
    can_delete = False
    verbose_name_plural = 'Grado de deterioro'
    max_num = 1
    formset = RequiredInlineFormSet
    fieldsets = ( #Redefine que campos se muestran y como se agrupan
        (None, {
            'fields': (
                ('ec_agri_es','agrietamie'),
                ('ea_corr_ac','e_mantenim'),


                )
        }),
    )

#endregion
#region Admin  Observacion
class ObservacionAdmin(admin.ModelAdmin):
    """
        Admin de la clase Observacion.
    """
    def get_model_perms(self, request):
        """
            Sobreescritura del metodo de los permisos.
            Se devuelve una lista vacia para que este
            modelo no se muestre en el admin pero aun
            permita incluirlo como inline dentro de
            inspeccion

        """
        return {}
#endregion
#region Inline Observacion
class ObservacionInline(admin.StackedInline):
    """
        Clase que permite inlcuir el modelo
        como un inline en el admin de inspeccion.
        Usa el form 'RequiredInlineFormSet(forms.py)'
        para mantener las validaciones propias del admin
        de este modelo
    """
    model = Observacion
    can_delete = False
    verbose_name_plural = 'Observaciones (máximo 500 caracteres)'
    max_num = 1
    formset = RequiredInlineFormSet

#endregion
#region  Admin Anexo
class AnexoAdmin(admin.ModelAdmin):
    """
        Admin de la clase Anexo.
    """
    def get_model_perms(self, request):
        """
            Sobreescritura del metodo de los permisos.
            Se devuelve una lista vacia para que este
            modelo no se muestre en el admin pero aun
            permita incluirlo como inline dentro de
            inspeccion

        """
        return {}
#endregion
#region Inline Anexo
class AnexoInline(admin.StackedInline):
    """
        Clase que permite inlcuir el modelo
        como un inline en el admin de inspeccion.
        Usa el form 'RequiredInlineFormSet(forms.py)'
        para mantener las validaciones propias del admin
        de este modelo
    """
    model = Anexo
    can_delete = False
    verbose_name_plural = 'Anexos'
    max_num = 1
    formset = RequiredInlineFormSet
#endregion
#region  Admin Inspeccion
class InspeccionAdmin(admin.ModelAdmin):
    """
        Admin de la clase Inspeccion.
        Usa como inlines los demas modelos
        con el fin de que se agregue toda la
        data desde una misma estructura y
        la visualizacion sea lo mas exacta
        posible con relacion a la planilla fisica.
    """
    inlines = ( EntrevistadoInline,EstructuraInline, UsoInline,Capacidad_OcupacionInline,Anio_ConstruccionInline,Condicion_TerrenoInline,Tipo_EstructuralInline,Esquema_PlantaInline,Esquema_ElevacionInline,IrregularidadInline, Grado_DeterioroInline,ObservacionInline,AnexoInline )

    verbose_name = 'Datos Generales'
    verbose_name_plural = 'Datos Generales'
    exclude = ('cod_pla',)

    class  Media:
        js = ("js/jquery-1.8.2.min.js","js/charCount.js","js/periodo_construccion.js","js/sismo_caracas_validaciones.js")

        css = {
            'all':("stylesheets/tipo_estructural.css",)
        }

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