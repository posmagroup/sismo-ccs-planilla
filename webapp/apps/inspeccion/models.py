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

    cod_ocup = models.CharField("Relacion con la Edif",max_length=100)
    nom_entrev = models.CharField("Nombre y apellido",max_length=100)
    tlf_entrev = models.CharField("Telefono",max_length=100)
    email_entr = models.EmailField("Correo Electronico",max_length=100)

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

    calle = models.CharField("Calle",max_length=100)
    avenida = models.CharField("Avenida",max_length=100)
    pto_referencia = models.CharField("Punto de referencia",max_length=100)

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

    forma_terr = models.CharField("Forma del terreno",max_length=1,choices=FORMA_TERRENO_CHOICES)
    pend_terr =  models.CharField("Pendiente del terreno",max_length=1, choices=PENDIENTE_TERRENO_CHOICES, blank=True, null=True)
    l_m_ladera = models.BooleanField("Localizada sobre la mitad superior de la ladera",default= False, blank=True)
    pend_talud = models.CharField("Pendiente del talud",max_length=1,choices=PENDIENTE_TALUD_CHOICES, blank=True, null=True)
    sep_talud = models.CharField("Separacion del talud",max_length=1,choices=SEPARACION_TALUD_CHOICES, blank=True, null=True)
    drenaje = models.BooleanField("Drenajes",default= False, blank=False)


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
    pca = models.BooleanField("Pórticos de concreto armado",default= False)
    pcap = models.BooleanField("Pórticos de concreto armado rellenos con paredes de bloques de arcilla o de concreto",default= False)
    mca2d = models.BooleanField("Muros de concreto armado en dos direcciones horizontales",default= False)
    mca1d = models.BooleanField("Sistemas con muros de concreto armado en una sola dirección, como algunos sistemas del tipo túnel",default= False)
    pa = models.BooleanField("Pórticos de acero",default= False)
    papt = models.BooleanField("Pórticos de acero con perfiles tubulares",default= False)
    pad = models.BooleanField("Pórticos de acero diagonalizados",default= False)
    pac = models.BooleanField("Pórticos de acero con cerchas",default= False)
    pre = models.BooleanField("Sistemas pre-fabricados a base de grandes paneles o de pórticos",default= False)
    mmc = models.BooleanField("Sistemas cuyos elementos portantes sean muros de mampostería confinada",default= False)
    mmnc = models.BooleanField("Sistemas cuyos elementos portantes sean muros de mampostería no confinada",default= False)
    vb = models.BooleanField("Viviendas de bahareque de un piso",default= False)
    vcp = models.BooleanField("Viviendas de construcción precaria (tiera, madera, zinc, etc.)",default= False)
    n_pisos_cf = models.BooleanField("N° de pisos confinados",default= False)
    n_pisos_nc = models.BooleanField("N° de pisos NO confinados",default= False)
    n_pisos_bc = models.BooleanField("N° pisos sistema mixto de baja calidad",default= False)
    esq_planta = models.BooleanField("Esquema en  Planta",default= False)
    esq_elevac = models.BooleanField("Esquema en Elevacion",default= False)

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
    u_gubernam = models.BooleanField("Uso Gubernamental",default= False)
    u_bomberos = models.BooleanField("Uso Bomberos",default= False)
    u_pr_civil = models.BooleanField("Uso Protección Civil",default= False)
    u_policial = models.BooleanField("Uso Policial",default= False)
    u_militar = models.BooleanField("Uso Militar",default= False)
    u_med_asis = models.BooleanField("Uso Médico Asistencial",default= False)
    u_educativ = models.BooleanField("Uso Educativo",default= False)
    u_viv_pop = models.BooleanField("Uso Vivienda Popular",default= False)
    u_viv_unif = models.BooleanField("Uso Vivienda Unifamiliar",default= False)
    u_viv_mult = models.BooleanField("Uso Vivienda Multifamiliar",default= False)
    u_dep_recr = models.BooleanField("Uso Deportivo-Recreativo",default= False)
    u_cultural = models.BooleanField("Uso Cultural",default= False)
    u_industri = models.BooleanField("Uso Industrial",default= False)
    u_comercia = models.BooleanField("Uso Comercial",default= False)
    u_oficina = models.BooleanField("Uso Oficina",default= False)
    u_religios = models.BooleanField("Uso Religioso",default= False)
    u_otros = models.BooleanField("Otros Usos",default= False)


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

    a_viga_alt = models.BooleanField("Ausencia de vigas altas en una o dos direcciones",default= False)
    p_entrep_b = models.BooleanField("Presencia de al menos  un entrepiso debil ó blando",default= False)
    p_column_c = models.BooleanField("Presencia de columnas cortas",default= False)
    disc_eje_c = models.BooleanField("Discontinuidad de ejes de columnas",default= False)
    abert_losa = models.BooleanField("Aberturas significativas en losas",default= False)
    f_asim_mas = models.BooleanField("Fuerte asimetría de masas o rigideces en planta",default= False)
    aus_mur_1d = models.BooleanField("Ausencia de muros en una dirección",default= False)
    ados_los_l = models.BooleanField("Adosamiento: losa contra losa",default= False)
    ados_los_c = models.BooleanField("Adosamiento:losa contra columna",default= False)
    sep_edif = models.IntegerField("Separacion entre edifcio (cm)",default=0)


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

    ec_agri_es = models.CharField("Estructura de Concreto:  Agrietamiento en elementos estructurales de concreto armado y/o corrosión en acero de refuerzo:",max_length=1,choices=GRADO_DETERIORO_CHOICES)
    ea_corr_ac = models.CharField("Estructura de Acero: Corrosión en elementos de acero y/o deterioro de conexiones y/o pandeo de elementos:",max_length=1,choices=GRADO_DETERIORO_CHOICES)
    agrietamie = models.CharField("Agrietamiento en paredes de relleno",max_length=1,choices=GRADO_DETERIORO_CHOICES)
    e_mantenim = models.CharField("Estado general de mantenimiento",max_length=1,choices=GRADO_DETERIORO_MANTENIMIENTO_CHOICES)


    class  Meta:

        verbose_name ='Grado de Deterioro'
        verbose_name_plural ='Grados de Deterioro'

    def __unicode__(self):

        return u' Grados de Deterioro, consultar para mas detalles. '



















