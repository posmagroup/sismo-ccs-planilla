# -*- coding: utf8 -*-
from django.db import models


class Entrevistado(models.Model):

    """
    Purpose:
        Defines a  model for handling Interviewee
        to include in the inspection model

    Features:
        1) All fields are mandatory.
    """

    cod_ocup = models.CharField(verbose_name="Condición del Ocupante",help_text="Tipo de condición que tiene el entrevistado, con relación a la edificación",max_length=100)
    nom_entrev = models.CharField(verbose_name="Nombre completo del Ocupante",help_text="Nombre completo de la persona entrevistada",max_length=100)
    tlf_entrev = models.CharField(verbose_name="Teléfono del Ocupante",help_text="Teléfono de de la persona entrevistada",max_length=100)
    email_entr = models.EmailField(verbose_name="E-Mail del Ocupante",help_text="Correo Electrónico de la persona entrevistada",max_length=100)

    class  Meta:

        verbose_name ='Datos del Entrevistado'
        verbose_name_plural ='Datos de los Entrevistados'

    def __unicode__(self):

        return u' Entrevistado: Nombre: %s  -Telefono: %s  -Email: %s' % (self.nom_entrev,self.tlf_entrev, self.email_entr)


class Direccion(models.Model):

    """
    Purpose:
        Defines a  model for handling Interviewee s
        address to include in the inspection model

    Features:
        1) All fields are mandatory.
    """

    calle = models.CharField(verbose_name="Calle, Vereda",help_text="Calle o vereda donde se realizó la inspección",max_length=100)
    avenida = models.CharField(verbose_name="Avenida",help_text="Avenida donde se realizó la inspección",max_length=100)
    pto_referencia = models.CharField(verbose_name="Punto de referencia",help_text="Punto de referencia",max_length=100)

    class  Meta:

        verbose_name ='Direccion'
        verbose_name_plural ='Direcciones'

    def __unicode__(self):

        return u' Direccion: calle: %s  -Avenida: %s  -Punto de Referencia: %s' % (self.calle,self.avenida, self.pto_referencia)


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

    forma_terr = models.CharField(verbose_name="Forma del terreno",max_length=1,help_text="Forma del terreno donde está emplazada la edificación",choices=FORMA_TERRENO_CHOICES)
    pend_terr =  models.CharField(verbose_name="Pendiente del terreno",max_length=1, help_text="Grado de Inclinación del terreno cada 100 metros",choices=PENDIENTE_TERRENO_CHOICES, blank=True, null=True)
    l_m_ladera = models.BooleanField(verbose_name="Localizada sobre la mitad superior de la ladera",help_text="Ubicación de la edificacion en una ladera con respecto a la altura total del terreno. Responde la pregunta ¿La edificación esta construida en la mitad superior de la ladera?",default= False, blank=True)
    pend_talud = models.CharField(verbose_name="Pendiente del talud",help_text="Grado de inclinación del terreno en el talud",max_length=1,choices=PENDIENTE_TALUD_CHOICES, blank=True, null=True)
    sep_talud = models.CharField(verbose_name="Separacion del talud",help_text="separación que existe entre la edificación y el talud en metros",max_length=1,choices=SEPARACION_TALUD_CHOICES, blank=True, null=True)
    drenaje = models.BooleanField(verbose_name="Drenajes",help_text="Si la edificaicón esta ubicada sobre el curso de una quebrada, o un cauce intermitente",default= False, blank=False)


    class  Meta:

        verbose_name ='Condicion del Terreno'
        verbose_name_plural ='Condiciones de los Terrenos'

    def __unicode__(self):

        return u' Condicion: Forma del Terreno %s ' % (self.forma_terr)




class Tipo_Estructural(models.Model):

    """
    Purpose:
        Defines a  model for handling structures types
         to include in the inspection model

    Features:
        1) All fields are not mandatory.
    """
    pca = models.BooleanField(verbose_name="Pórticos de concreto armado",help_text="descripcion",default= False)
    pcap = models.BooleanField(verbose_name="Pórticos de concreto armado rellenos con paredes de bloques de arcilla o de concreto",help_text="descripcion",default= False)
    mca2d = models.BooleanField(verbose_name="Muros de concreto armado en dos direcciones horizontales",help_text="descripcion",default= False)
    mca1d = models.BooleanField(verbose_name="Sistemas con muros de concreto armado en una sola dirección, como algunos sistemas del tipo túnel",help_text="descripcion",default= False)
    pa = models.BooleanField(verbose_name="Pórticos de acero",help_text="descripcion",default= False)
    papt = models.BooleanField(verbose_name="Pórticos de acero con perfiles tubulares",help_text="descripcion",default= False)
    pad = models.BooleanField(verbose_name="Pórticos de acero diagonalizados",help_text="descripcion",default= False)
    pac = models.BooleanField(verbose_name="Pórticos de acero con cerchas",help_text="descripcion",default= False)
    pre = models.BooleanField(verbose_name="Sistemas pre-fabricados a base de grandes paneles o de pórticos",help_text="descripcion",default= False)
    mmc = models.BooleanField(verbose_name="Sistemas cuyos elementos portantes sean muros de mampostería confinada",help_text="descripcion",default= False)
    mmnc = models.BooleanField(verbose_name="Sistemas cuyos elementos portantes sean muros de mampostería no confinada",help_text="descripcion",default= False)
    vb = models.BooleanField(verbose_name="Viviendas de bahareque de un piso",help_text="descripcion",default= False)
    vcp = models.BooleanField(verbose_name="Viviendas de construcción precaria (tiera, madera, zinc, etc.)",help_text="descripcion",default= False)
    n_pisos_cf = models.BooleanField(verbose_name="N° de pisos confinados",help_text="descripcion",default= False)
    n_pisos_nc = models.BooleanField(verbose_name="N° de pisos NO confinados",help_text="descripcion",default= False)
    n_pisos_bc = models.BooleanField(verbose_name="N° pisos sistema mixto de baja calidad",help_text="descripcion",default= False)
    esq_planta = models.BooleanField(verbose_name="Esquema en  Planta",help_text="descripcion",default= False)
    esq_elevac = models.BooleanField(verbose_name="Esquema en Elevacion",help_text="descripcion",default= False)

    class  Meta:

        verbose_name ='Tipo Estructural'
        verbose_name_plural ='Tipos Estructurales'

    def __unicode__(self):

        return u' Tipo Estructural, consultar para mas detalles. '





class  Uso(models.Model):

    """
    Purpose:
        Defines a  model for handling uses
         to include in the inspection model

    Features:
        1) All fields are not mandatory.
    """
    u_gubernam = models.BooleanField(verbose_name="Uso Gubernamental",help_text="Uso de la estructura",default= False)
    u_bomberos = models.BooleanField(verbose_name="Uso Bomberos",help_text="Uso de la estructura",default= False)
    u_pr_civil = models.BooleanField(verbose_name="Uso Protección Civil",help_text="Uso de la estructura",default= False)
    u_policial = models.BooleanField(verbose_name="Uso Policial",help_text="Uso de la estructura",default= False)
    u_militar = models.BooleanField(verbose_name="Uso Militar",help_text="Uso de la estructura",default= False)
    u_med_asis = models.BooleanField(verbose_name="Uso Médico Asistencial",help_text="Uso de la estructura",default= False)
    u_educativ = models.BooleanField(verbose_name="Uso Educativo",help_text="Uso de la estructura",default= False)
    u_viv_pop = models.BooleanField(verbose_name="Uso Vivienda Popular",help_text="Uso de la estructura",default= False)
    u_viv_unif = models.BooleanField(verbose_name="Uso Vivienda Unifamiliar",help_text="Uso de la estructura",default= False)
    u_viv_mult = models.BooleanField(verbose_name="Uso Vivienda Multifamiliar",help_text="Uso de la estructura",default= False)
    u_dep_recr = models.BooleanField(verbose_name="Uso Deportivo-Recreativo",help_text="Uso de la estructura",default= False)
    u_cultural = models.BooleanField(verbose_name="Uso Cultural",help_text="Uso de la estructura",default= False)
    u_industri = models.BooleanField(verbose_name="Uso Industrial",help_text="Uso de la estructura",default= False)
    u_comercia = models.BooleanField(verbose_name="Uso Comercial",help_text="Uso de la estructura",default= False)
    u_oficina = models.BooleanField(verbose_name="Uso Oficina",help_text="Uso de la estructura",default= False)
    u_religios = models.BooleanField(verbose_name="Uso Religioso",help_text="Uso de la estructura",default= False)
    u_otros = models.BooleanField(verbose_name="Otros Usos",help_text="Uso de la estructura",default= False)


    class  Meta:

        verbose_name ='Uso'
        verbose_name_plural ='Usos'

    def __unicode__(self):

        return u' Usos, consultar para mas detalles. '


class Irregularidad(models.Model):


    """
    Purpose:
        Defines a  model for handling irregularity
         to include in the inspection model

    Features:
        1) sep_edif field is mandatory.
    """

    a_viga_alt = models.BooleanField(verbose_name="Ausencia de vigas altas en una o dos direcciones",help_text="Irregularidad que describe la ausencia de vigas altas en una o dos direcciones ortogonales de la estructural. Una viga alta es considerada cuando su altura es mayor que el espesor o altura de la losa.",default= False)
    p_entrep_b = models.BooleanField(verbose_name="Presencia de al menos  un entrepiso debil ó blando",help_text="Irregularidad que describe la presencia de una planta baja o entrepiso libre o blando. Esta condición se cumple cuando:i) la diferencia de la sección transversal de paredes de un piso con respecto a las siguientes es más del 50%, ii) más del 50% de los pórticos de un piso no presentan paredes o iii) cuando existe una discontinuidad en vertical de elementos resistentes como la presencia de muros y luego cambia a columnas.",default= False)
    p_column_c = models.BooleanField(verbose_name="Presencia de columnas cortas",help_text="Irregularidad caracterizada cuando una o varias columnas de concreto armado presenta una porción de su altura sin restricciones laterales como paredes. Esta condición no se cumple cuando la totalidad de la altura presenta o carece de restricciones laterales.",default= False)
    disc_eje_c = models.BooleanField(verbose_name="Discontinuidad de ejes de columnas",help_text="Irregularidad que describe la interrupción o variación en planta de los ejes de elementos verticales, muro o columna en dos pisos consecutivos. La variación debe ser mayor a 1/3 de la dimensión horizontal del miembro inferior en la dirección del deslizamiento.",default= False)
    abert_losa = models.BooleanField(verbose_name="Aberturas significativas en losas",help_text="Irregularidad que describe cuando el área total de aberturas de un piso sea mayor a un 20% del area total de la planta.",default= False)
    f_asim_mas = models.BooleanField(verbose_name="Fuerte asimetría de masas o rigideces en planta",help_text="Irregularidad que describe la presencia  de muros estructurales, paredes, núcleo de ascensores, núcleo de escaleras u otro, excéntricas en la estructura, que generen asimetría de masas y/o rigideces.",default= False)
    aus_mur_1d = models.BooleanField(verbose_name="Ausencia de muros en una dirección",help_text="Irregularidad que describe la ausencia de muros en una dirección, esta condicion se cumple en los sistemas estructurales con muros en una dirección.",default= False)
    ados_los_l = models.BooleanField(verbose_name="Adosamiento: losa contra losa",help_text="Irregularidad que describe cuando dos edificios adyacentes no poseen una distancia suficiente entre ellos para evitar el choque y a la vez las alturas de losas de entre piso se encuentran a la misma cota o elevación.",default= False)
    ados_los_c = models.BooleanField(verbose_name="Adosamiento:losa contra columna",help_text="Irregularidad que describe cuando dos edificios adyacentes no poseen una distancia suficiente entre ellos para evitar el choque y a la vez las alturas de losas de entre piso no se encuentran a la misma cota o elevación.",default= False)
    sep_edif = models.IntegerField(verbose_name="Separacion entre edifcio (cm)",help_text="Valor de la menor separación entre los edificios adyacentes. Se debe activar en caso de que halla adosamiento de lo contrario no.",default=0)


    class  Meta:

        verbose_name ='Irregularidad'
        verbose_name_plural ='Irregularidades'

    def __unicode__(self):

        return u' Irregularidades, consultar para mas detalles. '





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

    ec_agri_es = models.CharField(verbose_name="Estructura de Concreto:  Agrietamiento en elementos estructurales de concreto armado y/o corrosión en acero de refuerzo" , help_text="Describe el grado de mantenimiento que poseen los elementos estructurales de concreto como: columnas, vigas, muros o losas, en términos de agrietamiento en éstos, presencia de corrosión del acero de refuezo, pérdida del recubrimiento entre otros.",max_length=1,choices=GRADO_DETERIORO_CHOICES)
    ea_corr_ac = models.CharField(verbose_name="Estructura de Acero: Corrosión en elementos de acero y/o deterioro de conexiones y/o pandeo de elementos" , help_text="Describe el grado de mantenimiento que poseen los elementos estructurales de acero como: sistema de piso, columnas, vigas o arriostramientos de perfiles de sección abierta o cerrada, en términos de pandeo, fractura en conexiones, corrosión entre otros.",max_length=1,choices=GRADO_DETERIORO_CHOICES)
    agrietamie = models.CharField(verbose_name="Agrietamiento en paredes de relleno",help_text="Describe la presencia de grietas en las paredes de bolques de concreto o arcilla, si estas presentan una abertura mayor a los 2mm.",max_length=1,choices=GRADO_DETERIORO_CHOICES)
    e_mantenim = models.CharField(verbose_name="Estado general de mantenimiento", help_text="Describe el estado de mantenimiento en general de la estructura en terminos de humedad o filtración, deterioro y abandono.", max_length=1,choices=GRADO_DETERIORO_MANTENIMIENTO_CHOICES)


    class  Meta:

        verbose_name ='Grado de Deterioro'
        verbose_name_plural ='Grados de Deterioro'

    def __unicode__(self):

        return u' Grados de Deterioro, consultar para mas detalles. '





#class Estructura(models.Model):














