from django.contrib.gis.gdal.datasource import DataSource
from django.contrib.gis.geos import MultiPolygon, Polygon
from django.contrib.gis.utils import LayerMapping
from models import Poligono, Inspeccion
from webapp.settings import VAR_ROOT

from django.db import connection


#
#mapping = {
#    'fid_edific' : 'FID_Edific',
#    'layer' : 'LAYER',
#    'gm_type' : 'GM_TYPE',
#    'elevation' : 'ELEVATION',
#    'xdata0' : 'xdata0',
#    'shape_leng' : 'Shape_Leng',
#    'shape_area' : 'Shape_Area',
#    'otro_conta' : 'otro_conta',
#    'geom' : 'MULTIPOLYGON',
#
#    }
#
#ds = DataSource(VAR_ROOT + '/Edif_Candelaria.shp')
#
#lm = LayerMapping(Poligono, ds, mapping)

#lm.save(verbose=True)
##
#p = [x for x in Poligono.objects.all()[:10]]
###
#union = p[8].geom
#
###
#for poligono in Poligono.objects.all()[:1000]:
###
#   try:
#       union.append(poligono.geom.cascaded_union)
#
#
#   except :
#
#       print 'erro en el poligono %d'% poligono.id
#
###
#poli =  Poligono.objects.get(pk =3)
#poli.geom = union
#poli.save()

