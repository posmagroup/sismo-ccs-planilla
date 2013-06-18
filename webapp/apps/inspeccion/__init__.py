from django.contrib.gis.gdal.datasource import DataSource
from django.contrib.gis.geos import MultiPolygon, Polygon
from django.contrib.gis.utils import LayerMapping
from models import Poligono, Inspeccion
from webapp.settings import VAR_ROOT

from django.db import connection



mapping = {
    'poligono' : 'POLYGON',
    }
#
ds = DataSource(VAR_ROOT + '/Edif_Candelaria.shp')

##print open(VAR_ROOT + '/candelaria.shp')


#print(layer.geom_type)
#print(layer.fields)
#print(layer.srs)
lm = LayerMapping(Poligono, ds, mapping)


#lm.save(verbose=True)

#print connection.queries
#
#poli = Poligono.objects.all()
#
#
#
#try:
#
#    inspeccion = Inspeccion.objects.all()[:1]
#    insp = inspeccion[0]
#    multi = MultiPolygon(poli[0].poligono)
#   # for poligono in poli:
#    #    multi.append(poligono.poligono)
#    #insp.poligono = multi
#    #insp.save()
#
#except :
#    raise

#
#poligono = poli[0]
#print poligono
#
#print poligono.poligono
#inspeccion = Inspeccion.objects.all()[:1]
#
#insp = Inspeccion()
#
#insp = inspeccion[0]
#print insp
#
#print insp.poligono
#
#try:
#
#    multi = MultiPolygon(poligono.poligono)
#    multi.append(poli[1].poligono)
#    insp.poligono = multi
#    insp.save()
#
#except :
#    raise


