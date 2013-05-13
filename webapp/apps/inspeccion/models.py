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


