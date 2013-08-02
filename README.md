Sismo-Caracas: Instalación
==========================


PostgreSQL:
-----------

PostgreSQL es el servidor de base de datos que utiliza el proyecto de sismo-caracas. Se puede descargar e instalar un servidor 
postgreSQL desde la página oficial: http://www.postgresql.org/download/

Para este proyecto se está usando la versión *PostgreSQL 9.1*.

PostGIS:
--------

PostGIS es una extensión de postgresql para albergar data geográfica. Antes de descargar deben revisarse los requisitos de postgis en la documentación oficial: 
http://www.postgis.org/documentation/manual-2.0/postgis_installation.html#id554707

Para descargar la fuente de PostGIS y extraer:

	$ wget http://download.osgeo.org/postgis/source/postgis-2.0.3.tar.gz
	$ tar xzf postgis-2.0.3.tar.gz
	$ cd postgis-2.0.3

Luego, para instalar:

	$ ./configure
	$ make
	$ sudo make install
	$ cd ..

En Debian, la instalación puede hacerse de la siguiente manera:

    $ sudo apt-get -u install postgresql-9.1 postgis postgresql-9.1-postgis-2.0 postgresql-9.1-postgis-2.0-scripts


Para crear la base de datos con acceso a tipos de datos geográficos debe ejecutase los siguientes comandos:

	$ psql                                          # Inicia una consola de postgresql usando postgres como base de datos por defecto.
    > CREATE USER <usuario> PASSWORD '<passwd>';    # Crea el usuario que usará la base de datos.
    > CREATE DATABASE <db name>                     # Crea una base de datos con nombre <db name>.
    > \c <db name>                                  # Se conecta a <db name>
	> CREATE EXTENSION postgis;                     # Agrega soporte para información geográfica a <db name>.
    > \q                                            # Salir.


Esto habrá habilitado nuestra base de datos para albergar data geográfica.


Para más información, revisar la documentación oficial: https://docs.djangoproject.com/en/dev/ref/contrib/gis/install/postgis/   y  http://www.postgresql.org/docs/8.0/static/sql-createuser.html

GeoDjango:
----------

GeoDjango es una extensión que nos permitirá usar tipos de datos geográficos en los modelos estándar de Django.

El backend de Geodjango viene incluido en la instalación de django, sin embargo se requiere la instalación de varias dependencias:

* GEOS
* PROJ.4
* GDAL
	
Para más información, revisar la siguiente referencia: 

https://docs.djangoproject.com/en/dev/ref/contrib/gis/install/geolibs/#geospatial-libs

Una vez que estén todas las dependencias instaladas, debe configurarse en el archivo ``settings.py`` para que use postgis como base de datos:

	DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'sismocaracas',
        'USER':'funvisis',
        'PASSWORD':'funvisis',
        'HOST':'localhost',
        'PORT':'5432'
        }
	} # Sustituir los valores por los establecidos en los pasos anteriores.

Y debe agregarse geodjango como aplicación instalada:

	INSTALLED_APPS = (
		'django.contrib.admin',
		'django.contrib.auth',
		'django.contrib.contenttypes',
		'django.contrib.sessions',
		'django.contrib.messages',
		'django.contrib.staticfiles',
		
		'django.contrib.gis',	# <--
		
		'apps.usuario',
		'apps.inspeccion',
	)

Si todo ha salido bien hasta ahora, podemos usar las clases y tipos definidos por geodjango. 
Definimos entonces un modelo geográfico (modificar el mismo modelo de inspección):

	from django.contrib.gis.db import models

    class Poligono(models.Model):
        fid_edific = models.IntegerField()
        layer = models.CharField(max_length=12)
        gm_type = models.CharField(max_length=17)
        elevation = models.FloatField()
        xdata0 = models.IntegerField()
        shape_leng = models.FloatField()
        shape_area = models.FloatField()
        otro_conta = models.CharField(max_length=250)
        # acá viene la magia de geodjango
        poligono = models.MultiPolygonField(null=True, blank=True)
        objects = models.GeoManager()

	class Estructura(models.Model):

        inspeccion = models.ForeignKey(Inspeccion,verbose_name="Inspección")
        nombre_n = models.CharField(verbose_name="Nombre o Nº",help_text="Nombre o número de la casa o edificio",
                                    max_length=100)
        n_pisos = models.IntegerField(verbose_name="Nº de Pisos",help_text="Número de pisos que posee la estructura")
        n_semi_sot = models.IntegerField(verbose_name="Nº de Semi-Sótanos",
                                        help_text="Número de semi-sotanos que posee la estructura",default=0)
        n_sotanos = models.IntegerField(verbose_name="Nº de Sótanos",help_text="Número de sótanos que posee la estructura",
                                        default=0)
        ciudad = models.CharField(verbose_name="Ciudad",help_text="Ciudad donde se realizó la inspección",max_length=100,
                                  null= True, blank=True)
        urb_barrio = models.CharField(verbose_name="Urb.,Barrio",help_text="Urb/Barrio donde se realizó la inspección",
                                  max_length=100,null= True, blank=True)
        sector = models.CharField(verbose_name="Sector",help_text="Sector donde se realizó la inspección",max_length=100,
                                  null= True, blank=True)
        calle = models.CharField(verbose_name="Calle, Vereda",help_text="Calle o vereda donde se realizó la inspección",
                                 max_length=100,null= True, blank=True)
        pto_referencia = models.CharField(verbose_name="Punto de referencia",help_text="Punto de referencia",max_length=100,
                                          null= True, blank=True)
        poligono = models.ForeignKey(Poligono, null=True,blank=True,default=None) # <--
	
Nótese que ``Poligono`` está heredando de la clase Models, pero esta vez la clase Models viene de ``django.contrib.gis.db`` y no de ``django.db`` como es lo usual.
Esto transforma nuestra clase en una clase geográfica, pudiendo acceder a la data de postgis como si fuesen tipos de campo normales de django.

Una vez hecho esto, debe ejecutarse ``syncdb`` y ``migrate`` para que sean actualizadas las tablas en BD

	
Importación de los datos:
-------------------------

Para hablitar el campo de tipo ``Polygon``, debemos importar la data de los shapefiles a la base de datos geográfica en formato postgis,
para esto usaremos la herramienta ``LayerMapping`` de django. Hagamos un script con las siguientes instrucciones:

	from django.contrib.gis.utils import LayerMapping
	from apps.inspeccion.models import Poligono # <--  Esta la clase que tiene el tipo de dato geoespacial.


    mapping = {
        'fid_edific' : 'FID_Edific',
        'layer' : 'LAYER',
        'gm_type' : 'GM_TYPE',
        'elevation' : 'ELEVATION',
        'xdata0' : 'xdata0',
        'shape_leng' : 'Shape_Leng',
        'shape_area' : 'Shape_Area',
        'otro_conta' : 'otro_conta',
        'geom' : 'POLYGON',

       }

    ds = DataSource(VAR_ROOT + '/Edif_Candelaria.shp')

    lm = LayerMapping(Poligono, ds, mapping)

    lm.save(verbose=True)

Esto mapea el campo de tipo ``POLYGON`` al campo ``poligono`` en nuestro modelo.

Para más información, revisar la documentación de django: https://docs.djangoproject.com/en/dev/ref/contrib/gis/layermapping/#django.contrib.gis.utils.LayerMapping


*NOTA*: En caso de recibir el error: 

    LayerMapError: Could not translate between the data source and model geometry: permiso denegado a la relación spatial_ref_sys

Deben darse permisos al usuario:

    ALTER TABLE spatial_ref_sys OWNER TO <usuario>;



Otros links de interés:
-----------------------

* http://www.postgis.org/documentation/manual-2.0/postgis_installation.html#id554707
* http://trac.osgeo.org/postgis/wiki/UsersWikiPostgreSQLPostGIS
* https://docs.djangoproject.com/en/dev/ref/contrib/gis/
