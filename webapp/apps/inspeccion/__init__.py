#from django.contrib.gis.gdal.datasource import DataSource
#from django.contrib.gis.utils import LayerMapping
#from models import Poligono
#from webapp.settings import VAR_ROOT
##
#from django.db import connection
#
#
#
#mapping = {
#    'poligono' : 'POLYGON',
#    }
##
#ds = DataSource(VAR_ROOT + '/Edif_Candelaria.shp')
#
###print open(VAR_ROOT + '/candelaria.shp')
##
##
##
#layer = ds[0]
#print(layer.geom_type)
#print(layer.fields)
#print(layer.srs)
#lm = LayerMapping(Poligono, ds, mapping)
#print connection.queries
#lm.save(verbose=True)
#print connection.queries
