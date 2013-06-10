Sismo-Caracas: Instalación
==========================


PostgreSQL:
-----------

PostgreSQL es el servidor de base de datos que utiliza el proyecto de sismo-caracas. Se puede descargar e instalar un servidor 
postgreSQL desde la página oficial: http://www.postgresql.org/download/

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

Para crear la base de datos con acceso a tipos de datos geográficos, debe ejecutarse los siguientes comandos en una consola de postgresql:

	$ createdb  <db name>
	$ psql <db name>
	> CREATE EXTENSION postgis;
	
Esto habrá habilitado nuestra base de datos para albergar data geográfica.


Luego debemos crear un usuario con los permisos necesarios para poder accesar la bD de postgresql, en una consola colocamos:
	
	$ sudo su postgres -c psql template1
	postgres#= CREATE USER funvisis WITH PASSWORD 'funvisis' CREATEDB;  // sustituir funvisis por el nombre deseado, igual para la clave.
	postgres#=\q


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
        }
	} // Sustituir los valores por los establecidos en los pasos anteriores.

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

	// AÚN EN ETAPA DE REVISIÓN Y DEFINICIÓN
	
	from django.contrib.gis.db import models

	

	class Poligono(models.Model):


		# acá viene la magia de geodjango
		poligono = models.MultiPolygonField(null=True, blank=True)
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

		
		fecha = models.DateField(verbose_name="Fecha", help_text="Día en que se levantó la información de campo mediante la planilla de inspección",auto_now=False,null= True, blank=True)
		hor_inicio = models.CharField(verbose_name="Hora de Inicio",help_text="Hora en que se inició la inspección",max_length=100,null= True, blank=True)
		hora_fin = models.CharField(verbose_name="Hora de culminación",help_text="Hora en que se terminó la inspección",max_length=100,null= True, blank=True)
		
		poligono = models.ForeignKey(Poligono,verbose_name="Polìgono", blank=True, null=True) # <--


		class  Meta:

			verbose_name ='Inspección'
			verbose_name_plural ='Inspecciones'

		def __unicode__(self):

			return u'Inspección %s' % self.id
	
Nótese que ``Poligono`` está heredando de la clase Models, pero esta vez la clase Models viene de ``django.contrib.gis.db`` y no de ``django.db`` como es lo usual.
Esto transforma nuestra clase en una clase geográfica, pudiendo acceder a la data de postgis como si fuesen tipos de campo normales de django.

Una vez hecho esto, debe correrse ``syncdb`` y ``migrate`` para que sean actualizadas las tablas en BD

	
Importación de los datos:
-------------------------

Para hablitar el campo de tipo ``Polygon``, debemos importar la data de los shapefiles a la base de datos geográfica en formato postgis,
para esto usaremos la herramienta ``LayerMapping`` de django. Hagamos un script con las siguientes instrucciones:

	from django.contrib.gis.utils import LayerMapping
	from apps.inspeccion.models import Poligono # <--  Esta la clase que tiene el tipo de dato geoespacial.
	
	mapping = {
			'poligono' : 'POLYGON', # <--  Esta este es el atributo de la clase que es de tipo models.MultiPolygonField
	}

	lm = LayerMapping(Poligono, 'edif_candelaria.shp', mapping) # <--  Poligono es la clase que importamos, luego viene la ruta al shapefile ('edif_candelaria.shp') y mapping queda igual.
	lm.save(verbose=True)

Esto mapea el campo de tipo ``POLYGON`` al campo ``poligono`` en nuestro modelo.

Para más información, revisar la documentación de django: https://docs.djangoproject.com/en/dev/ref/contrib/gis/layermapping/#django.contrib.gis.utils.LayerMapping

Otros links de interés:
-----------------------

* http://www.postgis.org/documentation/manual-2.0/postgis_installation.html#id554707
* http://trac.osgeo.org/postgis/wiki/UsersWikiPostgreSQLPostGIS
* https://docs.djangoproject.com/en/dev/ref/contrib/gis/
