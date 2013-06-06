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

Para más información, revisar la documentación oficial: https://docs.djangoproject.com/en/dev/ref/contrib/gis/install/postgis/


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
			'NAME': 'geodjango',
			'USER': 'geo',
		}
	}

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

	class  Inspeccion(models.Model):

		fecha = models.DateField()
		hor_inicio = models.CharField(max_length=100)
		hora_fin = models.CharField(max_length=100)
		
		# acá viene la magia de geodjango
		estructura = models.PolygonField()
		objects = models.GeoManager()
	
Nótese que ``Inspeccion`` está heredando de la clase Models, pero esta vez la clase Models viene de ``django.contrib.gis.db`` y no de ``django.db`` como es lo usual.
Esto transforma nuestra clase en una clase geográfica, pudiendo acceder a la data de postgis como si fuesen tipos de campo normales de django.

Una vez hecho esto, debe correrse ``syncdb`` y ``migrate`` para que sean actualizadas las tablas en BD

	
Importación de los datos:
-------------------------

Para hablitar el campo de tipo ``Polygon``, debemos importar la data de los shapefiles a la base de datos geográfica en formato postgis,
para esto usaremos la herramienta ``LayerMapping`` de django. Hagamos un script con las siguientes instrucciones:

	from django.contrib.gis.utils import LayerMapping
	from apps.inspeccion.models import Inspeccion
	
	mapping = {
			'estructura' : 'POLYGON',
	}

	lm = LayerMapping(Inspeccion, 'edif_candelaria.shp', mapping)
	lm.save(verbose=True)

Esto mapea el campo de tipo ``POLYGON`` al campo ``estructura`` en nuestro modelo.

Para más información, revisar la documentación de django: https://docs.djangoproject.com/en/dev/ref/contrib/gis/layermapping/#django.contrib.gis.utils.LayerMapping

Otros links de interés:
-----------------------

	* http://www.postgis.org/documentation/manual-2.0/postgis_installation.html#id554707
	* http://trac.osgeo.org/postgis/wiki/UsersWikiPostgreSQLPostGIS
	* https://docs.djangoproject.com/en/dev/ref/contrib/gis/
