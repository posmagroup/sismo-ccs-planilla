from django.contrib.gis.gdal.datasource import DataSource
from django.contrib.gis.utils import LayerMapping
from models import Inspeccion
from webapp.settings import VAR_ROOT

mapping = {
    'poligono' : 'MULTIPOLYGON',
    }

ds = DataSource(VAR_ROOT + '/Edif_Candelaria.shp')

##print open(VAR_ROOT + '/candelaria.shp')
#
#
#
#layer = ds[0]
#print(layer.geom_type)
#print(layer.fields)
#print(layer.srs)
#lm = LayerMapping(Inspeccion, ds, mapping)
#lm.save(verbose=True)