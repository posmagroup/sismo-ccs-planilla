# -*- coding: utf8 -*-
import os

from django.contrib.auth.models import User
from django.conf import settings


from django.contrib.gis.db import models
#region  1.Datos Generales (Modelo Inspeccion, Poligono)
class Poligono(models.Model):

    # acá viene la magia de geodjango
    poligono = models.PolygonField()
    objects = models.GeoManager()

    class  Meta:

        verbose_name ='Poligono'
        verbose_name_plural ='Poligonos'

    def __unicode__(self):

        return u'Poligono %s ' % (self.id)



class  Inspeccion(models.Model):

    """
    Purpose:
        Defines a  model for handling Inspections

    Features:
        1) Some fields are mandatory.
    """


    fecha = models.DateField(verbose_name="Fecha", help_text="Día en que se levantó la información de campo mediante la planilla de inspección",auto_now=False)
    hor_inicio = models.CharField(verbose_name="Hora de Inicio",help_text="Hora en que se inició la inspección",max_length=100,null= True, blank=True)
    hora_fin = models.CharField(verbose_name="Hora de culminación",help_text="Hora en que se terminó la inspección",max_length=100,null= True, blank=True)



    class  Meta:

        verbose_name ='Inspección'
        verbose_name_plural ='Inspecciones'

    def __unicode__(self):

        return u'Inspección %s' % self.id



#endregion



#region  2.Datos de los participantes (Modelo Participante)

class Participante(models.Model):

    """
    Purpose:
        Defines a  model for handling users
        to include in the inspection model

    Features:
        1) All fields are not mandatory.
    """


    limit_inspector  = models.Q(groups__name='Inspector')
    limit_revisor  = models.Q(groups__name='Revisor')
    limit_supervisor  = models.Q(groups__name='Supervisor')

    inspeccion = models.ForeignKey(Inspeccion,verbose_name="Inspección")
    inspector = models.ForeignKey(User, verbose_name='Inspector', help_text='Usuario que inspeccionó la planilla.', related_name='inspector_planilla', limit_choices_to=limit_inspector)
    revisor = models.ForeignKey(User, verbose_name='Revisor', help_text='Usuario que revisó la planilla.', related_name='revisor_planilla', limit_choices_to=limit_revisor,null= True, blank=True)
    supervisor = models.ForeignKey(User, verbose_name='Supervisor', help_text='Supervisor de  la planilla.', related_name='supervisor_planilla',limit_choices_to=limit_supervisor,null= True, blank=True)

    class  Meta:

        verbose_name ='Dato del participante'
        verbose_name_plural ='Datos de los participantes'

    def __unicode__(self):

        return u'Datos de los participantes, consultar para mas detalles. '

#endregion

#region  3.Datos del Entrevistado (Modelo Entrevistado)

class Entrevistado(models.Model):

    """
    Purpose:
        Defines a  model for handling Interviewee
        to include in the inspection model

    Features:
        1) Some fields are mandatory.
    """
    inspeccion = models.ForeignKey(Inspeccion,verbose_name="Inspeccion")
    cod_ocup = models.CharField(verbose_name="Relación con la Edif",help_text="Tipo de condición que tiene el entrevistado, con relación a la edificación",max_length=100,null= True, blank=True)
    nom_entrev = models.CharField(verbose_name="Nombre y Apellido",help_text="Nombre completo de la persona entrevistada",max_length=100)
    tlf_entrev = models.CharField(verbose_name="Teléfono",help_text="Teléfono  de la persona entrevistada",max_length=100,null= True, blank=True)
    email_entr = models.EmailField(verbose_name="Correo Electrónico",help_text="Correo Electrónico de la persona entrevistada",max_length=100,null= True, blank=True)

    class  Meta:

        verbose_name ='Datos del Entrevistado'
        verbose_name_plural ='Datos de los Entrevistados'

    def __unicode__(self):

        return u' Entrevistado: Nombre: %s  -Telefono: %s  -Email: %s' % (self.nom_entrev,self.tlf_entrev, self.email_entr)


#endregion

#region  4.Identificación y ubicación de la edificación (Modelo Estructura)

class Estructura(models.Model):

    """
    Purpose:
        Defines a  model for handling Estrcutures
        to include in the inspection model

    Features:
        1) Some fields are not mandatory.
    """
    inspeccion = models.ForeignKey(Inspeccion,verbose_name="Inspección")
    nombre_n = models.CharField(verbose_name="Nombre o Nº",help_text="Nombre o número de la casa o edificio",max_length=100)
    n_pisos = models.IntegerField(verbose_name="Nº de Pisos",help_text="Número de pisos que posee la estructura")
    n_semi_sot = models.IntegerField(verbose_name="Nº de Semi-Sótanos",help_text="Número de semi-sotanos que posee la estructura",default=0)
    n_sotanos = models.IntegerField(verbose_name="Nº de Sótanos",help_text="Número de sótanos que posee la estructura",default=0)
    ciudad = models.CharField(verbose_name="Ciudad",help_text="Ciudad donde se realizó la inspección",max_length=100,null= True, blank=True)
    urb_barrio = models.CharField(verbose_name="Urb.,Barrio",help_text="Urb/Barrio donde se realizó la inspección",max_length=100,null= True, blank=True)
    sector = models.CharField(verbose_name="Sector",help_text="Sector donde se realizó la inspección",max_length=100,null= True, blank=True)
    calle = models.CharField(verbose_name="Calle, Vereda",help_text="Calle o vereda donde se realizó la inspección",max_length=100,null= True, blank=True)
    manzana = models.CharField(verbose_name="Manzana Nº",help_text="Nº Manzana donde se realizó la inspección",max_length=100,null= True, blank=True)
    parcela = models.CharField(verbose_name="Nº Parcela",help_text="Nº Parcela donde se realizó la inspección",max_length=100,null= True, blank=True)
    pto_referencia = models.CharField(verbose_name="Punto de referencia",help_text="Punto de referencia",max_length=100,null= True, blank=True)
    poligono = models.MultiPolygonField(verbose_name="Edificación")
    objects = models.GeoManager()

    class  Meta:

        verbose_name =' Estructura'
        verbose_name_plural =' Estructuras'



    def __unicode__(self):

        return u'  Estructura, consultar para mas detalles. '


#endregion

#region  5.uso de la Edificación (Modelo Uso)

class  Uso(models.Model):

    """
    Purpose:
        Defines a  model for handling uses
         to include in the inspection model

    Features:
        1) All fields are not mandatory.
    """
    inspeccion = models.ForeignKey(Inspeccion,verbose_name="Inspeccion")
    u_gubernam = models.BooleanField(verbose_name="Gubernamental",help_text=" ",default= False)
    u_bomberos = models.BooleanField(verbose_name="Bomberos",help_text=" ",default= False)
    u_pr_civil = models.BooleanField(verbose_name="Protección Civil",help_text=" ",default= False)
    u_policial = models.BooleanField(verbose_name="Policial",help_text=" ",default= False)
    u_militar = models.BooleanField(verbose_name="Militar",help_text=" ",default= False)
    u_med_asis = models.BooleanField(verbose_name="Médico Asistencial",help_text=" ",default= False)
    u_educativ = models.BooleanField(verbose_name="Educativo",help_text=" ",default= False)
    u_viv_pop = models.BooleanField(verbose_name="Vivienda Popular",help_text=" ",default= False)
    u_viv_unif = models.BooleanField(verbose_name="Vivienda Unifamiliar",help_text=" ",default= False)
    u_viv_mult = models.BooleanField(verbose_name="Vivienda Multifamiliar",help_text=" ",default= False)
    u_dep_recr = models.BooleanField(verbose_name="Deportivo-Recreativo",help_text=" ",default= False)
    u_cultural = models.BooleanField(verbose_name="Cultural",help_text=" ",default= False)
    u_industri = models.BooleanField(verbose_name="Industrial",help_text=" ",default= False)
    u_comercia = models.BooleanField(verbose_name="Comercial",help_text=" ",default= False)
    u_oficina = models.BooleanField(verbose_name="Oficina",help_text=" ",default= False)
    u_religios = models.BooleanField(verbose_name="Religioso",help_text=" ",default= False)
    u_otros = models.BooleanField(verbose_name="Otros",help_text=" ",default= False)
    otro_uso = models.CharField(verbose_name="(Especifique)" , help_text="",max_length=50,null= True, blank=True)


    class  Meta:

        verbose_name ='Uso'
        verbose_name_plural ='Usos'

    def __unicode__(self):

        return u' Usos, consultar para mas detalles. '



#endregion

#region  6.Capacidad de Ocupación (Modelo Capacidad_Ocupación)

class Capacidad_Ocupacion(models.Model):

    """
    Purpose:


    Features:
        1) .
    """
    inspeccion = models.ForeignKey(Inspeccion,verbose_name="Inspeccion")
    habitantes = models.IntegerField(verbose_name="Número de personas que ocupan el inmueble")
    t_o_manana = models.BooleanField(default=False,verbose_name="Ocupación durante la mañana")
    t_o_tarde = models.BooleanField(default=False,verbose_name="Ocupación  durante la tarde")
    t_o_noche = models.BooleanField(default=False,verbose_name="Ocupación durante la noche")


    class  Meta:

        verbose_name ='Capacidad de Ubicación'
        verbose_name_plural ='Capacidad de Ubicación'


    def __unicode__(self):

        return u'Capacidad de Ubicación,consultar para mas detalles. '



#endregion

#region  7.Año de Construccion (Modelo Periodo_Construccion y Anio_Construccion)

class Periodo_Construccion(models.Model):

    """
    Purpose:
        Defines a  model for handling the
        time frames.

    Features:
        1) fecha_infer is calculated according to
        user choice.
    """

    # Defining possible choices
    # for the periodo field in the model.
    PERIODO_CHOICES = (
        ('1', 'Antes de'),
        ('2', 'Entre'),
        ('3', 'Despues de')
        )
    periodo = models.CharField(verbose_name="Período" , help_text="Describe el período de construcción, en caso de que no se conozca la fecha exacta.",max_length=1,choices=PERIODO_CHOICES,null= True, blank=True)
    anio_inici = models.CharField(verbose_name="Año Inicio" , help_text="Año en el que empieza el período",max_length=5, null= True, blank=True)
    anio_fin = models.CharField(verbose_name="Año Fin" , help_text="Año en el que finaliza el período",max_length=5, null= True, blank=True)



    class  Meta:

        verbose_name ='Período de Construcción'
        verbose_name_plural ='Período de Construcción'

    def __unicode__(self):


        if (self.periodo == '1'):

            return u'  Antes de %s' % self.anio_inici

        if (self.periodo == '2'):

            return u'  Entre  %s y %s' % (self.anio_inici,self.anio_fin)

        if (self.periodo == '3'):

            return u'  Despues de  %s ' % self.anio_fin

        return u'  consultar para mas detalles. '






class Anio_Construccion(models.Model):

    """
    Purpose:
        Defines a  model for handling Estrcutures
        to include in the inspection model

    Features:
        1) All fields are not mandatory.
    """
    inspeccion = models.ForeignKey(Inspeccion,verbose_name="Inspección")
    periodo = models.ForeignKey(Periodo_Construccion,verbose_name="Periodo de Construccion",help_text="Describe el período de construcción, en caso de que no se conozca la fecha exacta.")
    anio = models.CharField(verbose_name="Año" , help_text="",max_length=5)
    fecha_inf = models.BooleanField(verbose_name="Fecha Inferida",help_text="",default= False)

    class  Meta:

        verbose_name ='Año de Construcción'
        verbose_name_plural ='Años de Construcción'



    def __unicode__(self):

        return u'Año de Construcción, consultar para mas detalles. '


#endregion

#region  8.Condicion del terreno (Modelo Condicion_Terreno)


class Condicion_Terreno(models.Model):

    """
    Purpose:
        Defines a  model for handling terrain conditions
         to include in the inspection model

    Features:
        1) Drenaje and  forma_terr fields are mandatory.
    """

    # Defining possible choices
    # for the forma_terr field in the model.
    FORMA_TERRENO_CHOICES = (
        ('1', 'Planice'),
        ('2', 'Ladera'),
        ('3', 'Base'),
        ('4', 'Cima')
        )

    # Defining possible choices
    # for the pend_terr field in the model.
    PENDIENTE_TERRENO_CHOICES = (
        ('1', '20º-45º'),
        ('2', 'Mayor a 45º')
        )

    # Defining possible choices
    # for the pend_talud field in the model.
    PENDIENTE_TALUD_CHOICES = (
        ('1', '20º-45º'),
        ('2',  'Mayor a 45º')
        )

    # Defining possible choices
    # for the sep_talud field in the model.
    SEPARACION_TALUD_CHOICES = (
        ('1', 'Menor a H del talud'),
        ('2',  'Mayor a H del talud')
        )

    # Defining possible choices
    # for the sep_talud field in the model.
    DRENAJE_TALUD_CHOICES = (
        ('1', 'Si'),
        ('2',  'No')
        )
    inspeccion = models.ForeignKey(Inspeccion,verbose_name="Inspeccion")
    forma_terr = models.CharField(verbose_name="Edificación en",max_length=1,help_text="Forma del terreno donde está emplazada la edificación",choices=FORMA_TERRENO_CHOICES)
    pend_terr =  models.CharField(verbose_name="Pendiente del terreno",max_length=1, help_text="Grado de Inclinación del terreno cada 100 metros",choices=PENDIENTE_TERRENO_CHOICES, blank=True, null=True)
    l_m_ladera = models.CharField(verbose_name="Localizada sobre la mitad superior de la ladera",help_text="Ubicación de la edificacion en una ladera con respecto a la altura total del terreno. Responde la pregunta ¿La edificación esta construida en la mitad superior de la ladera?",choices=DRENAJE_TALUD_CHOICES,max_length=1,blank=True, null=True)
    pend_talud = models.CharField(verbose_name="Pendiente del talud",help_text="Grado de inclinación del terreno en el talud",max_length=1,choices=PENDIENTE_TALUD_CHOICES, blank=True, null=True)
    sep_talud = models.CharField(verbose_name="Separación del talud",help_text="separación que existe entre la edificación y el talud en metros",max_length=1,choices=SEPARACION_TALUD_CHOICES, blank=True, null=True)
    drenaje = models.CharField(verbose_name="Drenajes",help_text="Si la edificaicón esta ubicada sobre el curso de una quebrada, o un cauce intermitente",max_length=1,choices=DRENAJE_TALUD_CHOICES)


    class  Meta:

        verbose_name ='Condición del Terreno'
        verbose_name_plural ='Condiciones de los Terrenos'

    def __unicode__(self):

        return u' Condición: Forma del Terreno %s ' % (self.forma_terr)



#endregion

#region  9.Tipo Estructural (Modelo Tipo_Estructural)

class Tipo_Estructural(models.Model):

    """
    Purpose:
        Defines a  model for handling structures types
         to include in the inspection model

    Features:
        1) All fields are not mandatory.
    """




    inspeccion = models.ForeignKey(Inspeccion,verbose_name="Inspeccion")
    pca = models.BooleanField(verbose_name="Pórticos de concreto armado (PCA)",help_text="Sistema estructural formado por columnas y vigas de concreto armado. En esta estructura las paredes no interfieren con el desplazamiento lateral del pórtico y tienen estabilidad propia para movimientos en y fuera de su plano.",default= False)
    pcap = models.BooleanField(verbose_name="Pórticos de concreto armado rellenos con paredes de bloques de arcilla o de concreto (PCAP)",help_text="Sistema estructural formado por columnas y vigas de concreto armado. En esta estructura las paredes  interfieren con el desplazamiento lateral del pórtico, por estar embutidas en todo el marco del pórtico. Las paredes pueden ser de bloques de arcilla o concreto",default= False)
    mca2d = models.BooleanField(verbose_name="Muros de concreto armado en dos direcciones horizontales (MCA2D)",help_text="Sistema estructural resistente a cargas verticales y horizontales formado por muros de concreto armado, dispuestos en dos direcciones ortogonales, en proporciones de área transversal similar o mayor al 25%.",default= False)
    mca1d = models.BooleanField(verbose_name="Sistemas con muros de concreto armado en una sola dirección, como algunos sistemas del tipo túnel (MCAMD)",help_text="Sistema estructural resistente a cargas verticales y horizontales formado por muros de concreto armado, dispuestos en una dirección o poca área transversal de muro en la dirección ortogonal (menor al 25%).",default= False)
    pa = models.BooleanField(verbose_name="Pórticos de acero (PA)",help_text="Sistema estructural resistente a cargas verticales y horizontales formado por perfiles metálicos de sección abierta tanto en columnas como vigas.",default= False)
    papt = models.BooleanField(verbose_name="Pórticos de acero con perfiles tubulares (PAPT)",help_text="Sistema estructural resistente a cargas verticales y horizontales formado por perfiles metálicos de sección cerrada tanto en columnas como vigas.",default= False)
    pad = models.BooleanField(verbose_name="Pórticos de acero diagonalizados (PAD)",help_text="Sistema estructural resistente a cargas verticales y horizontales formado por perfiles metálicos de sección abierta o cerrada tanto en columnas como vigas, con arriostramientos concentricos o excentricos.",default= False)
    pac = models.BooleanField(verbose_name="Pórticos de acero con cerchas (PAC)",help_text="Sistema estructural resistente a cargas verticales y horizontales formado por perfiles metálicos de sección abierta tanto en columnas como vigas y sistema de losa de entrepiso o techo compuesto por cerchas metálicas.",default= False)
    pre = models.BooleanField(verbose_name="Sistemas pre-fabricados a base de grandes paneles o de pórticos (PRE)",help_text="Sistema estructural resistente a cargas verticales y horizontales formado por paneles o pórticos de concreto armado prefabricados en taller.",default= False)
    mmc = models.BooleanField(verbose_name="Sistemas cuyos elementos portantes sean muros de mampostería confinada (MMC)",help_text="Sistema resistente a cargas verticales y horizontales donde  los estructurales son los muros de mamposteria confinados por machones y viga en la totalidad de su perímetro.",default= False)
    mmnc = models.BooleanField(verbose_name="Sistemas cuyos elementos portantes sean muros de mampostería no confinada (MMNC)",help_text="Sistema resistente a cargas verticales y horizontales donde los estructurales son los muros de mamposteria no confinados por machones o viga en la totalidad de su perímetro.",default= False)
    vb = models.BooleanField(verbose_name="Viviendas de bahareque de un piso (VB)",help_text="Sistema estructural rural de un piso formado por troncos de caña o similar y barro como material aglomerante, con techo liviano.",default= False)
    vcp = models.BooleanField(verbose_name="Viviendas de construcción precaria (tiera, madera, zinc, etc.) (VCP)",help_text="Sistema estructural de contrucción precaria donde se utilizan  materiales reciclados o livianos, como zinc, madera, tierra.",default= False)
    pmbc = models.BooleanField(verbose_name="Sistemas mixtos de pórticos y de mamposteria de baja calidad de construcción (PMBC)",help_text="Sistemas mixtos de pórticos y de mamposteria de baja calidad de construcción",default= False)

    #en el excel pero no en la planilla
#    n_pisos_cf = models.BooleanField(verbose_name="N° de pisos confinados",help_text="Números de pisos confinados que posee la estrutura. Se cumple la condición de confinado cuando las paredes presentan machones y viga de corona en su perímetro.",default= False)
#    n_pisos_nc = models.BooleanField(verbose_name="N° de pisos NO confinados",help_text="Números de pisos no confinados que posee la estrutura. Se cumple la condición de no confinado cuando las paredes no presentan machones o vigas de corona en su perímetro.",default= False)
#    n_pisos_bc = models.BooleanField(verbose_name="N° pisos sistema mixto de baja calidad",help_text="Números de pisos de sistemas conformados por pórticos de concreto o acero sin diseño según la normas vigente para la época construcción.",default= False)
    #en el excel pero no en la planilla


    class  Meta:

        verbose_name ='Tipo Estructural'
        verbose_name_plural ='Tipos Estructurales'

    def __unicode__(self):

        return u' Tipo Estructural, consultar para mas detalles. '




#endregion

#region  10.Esquema Planta (Modelo Esquema_Planta)


class Esquema_Planta(models.Model):

    """
    Purpose:


    Features:
        1) .
    """

    # Defining possible choices
    # for the esq_planta field in the model.
    ESQUEMA_PLANTA_CHOICES = (
        ('1', 'H'),
        ('2', 'T'),
        ('3', 'U ó C'),
        ('4', 'L'),
        ('5', 'Cajón'),
        ('6', 'Regular'),
        ('7', 'Esbeltez Horizontal'),
        ('8', ' Ninguno')

        )

    inspeccion = models.ForeignKey(Inspeccion,verbose_name="Inspección")
    esq_planta = models.CharField(verbose_name="Esquema de  Planta",max_length=1,choices=ESQUEMA_PLANTA_CHOICES,help_text="Describe la forma de la planta del edificio, es decir, vista desde arriba. Si se coloca 'Ninguno' corresponde a una forma irregular. En caso de 'Esbeltez Horizontal' se cumpla cuando el cociente entre el largo y ancho del menor rectangula que inscriba al edificio en planta sea mayor a 5.")

    class  Meta:

        verbose_name ='Esquema Planta'
        verbose_name_plural ='Esquema Planta'



    def __unicode__(self):

        return u'Esquema Planta, consultar para mas detalles. '





#endregion

#region  11.Esquema de Elevaciòn (Modelo Esquema_Elevacion)


class Esquema_Elevacion(models.Model):

    """
    Purpose:


    Features:
        1) .
    """

    # Defining possible choices
    # for the esq_elevac field in the model.
    ESQUEMA_ELEVACION_CHOICES = (
        ('1', 'T'),
        ('2', 'Piramide Invertida'),
        ('3', 'Piramidal'),
        ('4', 'U'),
        ('5', 'L'),
        ('6', 'Rectangular'),
        ('8', 'Esbeltez Vertical'),
        ('9', 'Ninguno'),

        )

    inspeccion = models.ForeignKey(Inspeccion,verbose_name="Inspección")
    esq_elevac = models.CharField(verbose_name="Esquema de Elevación",max_length=1,choices=ESQUEMA_ELEVACION_CHOICES,help_text="Describe la forma de elevación del edificio, es decir, vista desde un lateral. Si se coloca 'Ninguno' corresponde a una forma irregular. En caso de 'Esbeltez Vertical' se cumpla cuando el cociente entre la altura del edificio y la menor dimensión en planta exceda a 4.")

    class  Meta:

        verbose_name ='Esquema Elevación'
        verbose_name_plural ='Esquema Elevación'



    def __unicode__(self):

        return u'Esquema Elevación, consultar para mas detalles. '





#endregion

#region  12.Irregularidades (Modelo Irregularidad)

class Irregularidad(models.Model):


    """
    Purpose:
        Defines a  model for handling irregularity
         to include in the inspection model

    Features:
        1) sep_edif field is mandatory.
    """
    inspeccion = models.ForeignKey(Inspeccion,verbose_name="Inspeccion")
    a_viga_alt = models.BooleanField(verbose_name="Ausencia de vigas altas en una o dos direcciones",help_text="Irregularidad que describe la ausencia de vigas altas en una o dos direcciones ortogonales de la estructura. Una viga alta es considerada cuando su altura es mayor que el espesor o altura de la losa.",default= False)
    p_entrep_b = models.BooleanField(verbose_name="Presencia de al menos  un entrepiso débil ó blando",help_text="Irregularidad que describe la presencia de una planta baja o entrepiso libre o blando. Esta condición se cumple cuando:i) la diferencia de la sección transversal de paredes de un piso con respecto a las siguientes es más del 50%, ii) más del 50% de los pórticos de un piso no presentan paredes o iii) cuando existe una discontinuidad en vertical de elementos resistentes como la presencia de muros y luego cambia a columnas.",default= False)
    p_column_c = models.BooleanField(verbose_name="Presencia de columnas cortas",help_text="Irregularidad caracterizada cuando una o varias columnas de concreto armado presenta una porción de su altura sin restricciones laterales como paredes. Esta condición no se cumple cuando la totalidad de la altura presenta o carece de restricciones laterales.",default= False)
    disc_eje_c = models.BooleanField(verbose_name="Discontinuidad de ejes de columnas",help_text="Irregularidad que describe la interrupción o variación en planta de los ejes de elementos verticales, muro o columna en dos pisos consecutivos. La variación debe ser mayor a 1/3 de la dimensión horizontal del miembro inferior en la dirección del deslizamiento.",default= False)
    abert_losa = models.BooleanField(verbose_name="Aberturas significativas en losas",help_text="Irregularidad que describe cuando el área total de aberturas de un piso sea mayor a un 20% del area total de la planta.",default= False)
    f_asim_mas = models.BooleanField(verbose_name="Fuerte asimetría de masas o rigideces en planta",help_text="Irregularidad que describe la presencia  de muros estructurales, paredes, núcleo de ascensores, núcleo de escaleras u otro, excéntricas en la estructura, que generen asimetría de masas y/o rigideces.",default= False)
    aus_mur_1d = models.BooleanField(verbose_name="Ausencia de muros en una dirección",help_text="Irregularidad que describe la ausencia de muros en una dirección, esta condicion se cumple en los sistemas estructurales con muros en una dirección.",default= False)
    ados_los_l = models.BooleanField(verbose_name="Adosamiento: Losa contra losa",help_text="Irregularidad que describe cuando dos edificios adyacentes no poseen una distancia suficiente entre ellos para evitar el choque y a la vez las alturas de losas de entre piso se encuentran a la misma cota o elevación.",default= False)
    ados_los_c = models.BooleanField(verbose_name="Adosamiento:Losa contra columna",help_text="Irregularidad que describe cuando dos edificios adyacentes no poseen una distancia suficiente entre ellos para evitar el choque y a la vez las alturas de losas de entre piso no se encuentran a la misma cota o elevación.",default= False)
    sep_edif = models.IntegerField(verbose_name="Separación entre edifcio (cm)",help_text="Valor de la menor separación entre los edificios adyacentes. Se debe activar en caso de que halla adosamiento de lo contrario no.",default=0)


    class  Meta:

        verbose_name ='Irregularidad'
        verbose_name_plural ='Irregularidades'

    def __unicode__(self):

        return u' Irregularidades, consultar para mas detalles. '


#endregion

#region  13.Grados de deterioro (Modelo  Grado_Deterioro)


class Grado_Deterioro(models.Model):

    """
    Purpose:
        Defines a  model for handling damage
         to include in the inspection model

    Features:
        1) sep_edif field is mandatory.
    """

    # Defining possible choices
    # for the ec_agri_es,ea_corr_ac,agrietamie fields in the model.
    GRADO_DETERIORO_CHOICES = (
        ('1', 'Ninguno'),
        ('2', 'Moderado'),
        ('3', 'Severo')
        )

    # Defining possible choices
    # for the e_mantenim field in the model.
    GRADO_DETERIORO_MANTENIMIENTO_CHOICES = (
        ('1', 'Bueno'),
        ('2', 'Regular'),
        ('3', 'Bajo')
        )
    inspeccion = models.ForeignKey(Inspeccion,verbose_name="Inspeccion")
    ec_agri_es = models.CharField(verbose_name="Estructura de Concreto:  Agrietamiento en elementos estructurales de concreto armado y/o corrosión en acero de refuerzo" , help_text="Describe el grado de mantenimiento que poseen los elementos estructurales de concreto como: columnas, vigas, muros o losas, en términos de agrietamiento en éstos, presencia de corrosión del acero de refuezo, pérdida del recubrimiento entre otros.",max_length=1,choices=GRADO_DETERIORO_CHOICES)
    ea_corr_ac = models.CharField(verbose_name="Estructura de Acero: Corrosión en elementos de acero y/o deterioro de conexiones y/o pandeo de elementos" , help_text="Describe el grado de mantenimiento que poseen los elementos estructurales de acero como: sistema de piso, columnas, vigas o arriostramientos de perfiles de sección abierta o cerrada, en términos de pandeo, fractura en conexiones, corrosión entre otros.",max_length=1,choices=GRADO_DETERIORO_CHOICES)
    agrietamie = models.CharField(verbose_name="Agrietamiento en paredes de relleno",help_text="Describe la presencia de grietas en las paredes de bloques de concreto o arcilla, si estas presentan una abertura mayor a los 2mm.",max_length=1,choices=GRADO_DETERIORO_CHOICES)
    e_mantenim = models.CharField(verbose_name="Estado general de mantenimiento", help_text="Describe el estado de mantenimiento en general de la estructura en terminos de humedad o filtración, deterioro y abandono.", max_length=1,choices=GRADO_DETERIORO_MANTENIMIENTO_CHOICES)


    class  Meta:

        verbose_name ='Grado de Deterioro'
        verbose_name_plural ='Grados de Deterioro'

    def __unicode__(self):

        return u' Grados de Deterioro, consultar para mas detalles. '




#endregion

#region  14.Observaciones (Modelo Observacion)

class Observacion(models.Model):

    """
    Purpose:
        Defines a  model for handling the
        time frames.

    Features:
        1) fecha_infer is calculated according to
        user choice.
    """
    inspeccion = models.ForeignKey(Inspeccion,verbose_name="Inspección")
    observacion = models.TextField(max_length=140)

    class  Meta:

        verbose_name ='Observación'
        verbose_name_plural ='Observaciones'



    def __unicode__(self):

        return u'Observaciones, consultar para mas detalles. '




#endregion

#region  15.Anexos (Modelo Anexo)

class Anexo(models.Model):

    """
    Purpose:


    Features:

    """

    def upload_to_path(self, filename):

        """
        Purpose:

        Features:

        """
        return  os.path.join(settings.MEDIA_ROOT, filename)


    inspeccion = models.ForeignKey(Inspeccion,verbose_name="Inspección")
    foto_facha = models.FileField(verbose_name='Foto de fachada',upload_to=upload_to_path, blank=True, default='', null=True)
    pla_esca = models.FileField(verbose_name='Planilla Escaneada',upload_to=upload_to_path, blank=True, default='', null=True)

    class  Meta:

        verbose_name ='Anexo'
        verbose_name_plural ='Anexos'



    def __unicode__(self):

        return u'Anexos, consultar para mas detalles. '




#endregion






