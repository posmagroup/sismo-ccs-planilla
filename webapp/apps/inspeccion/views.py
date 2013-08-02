from datetime import date
import json
from django.http.response import HttpResponse

from braces.views import AjaxResponseMixin, JSONResponseMixin
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.utils import simplejson
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView

from models import Periodo_Construccion, Poligono

class Periodo_Construccion_By_YearView(JSONResponseMixin, AjaxResponseMixin, DetailView):
    model = Periodo_Construccion
    template_name = '404.html'

    def get_object(self,request, *args, **kwargs):

        periodos = Periodo_Construccion.objects.all().order_by('anio_inici')
        choices = []
        year = int(kwargs['year'])

        for periodo in periodos:

            init_year = periodo.anio_inici
            finish_year =  periodo.anio_fin

            #para periodos con fecha inicio y fecha fin definidos ( del tipo entre)
            if (year >= init_year) and (year <=finish_year) and (init_year!=None) and (finish_year!= None):
                choices.append(periodo.id)

            #para periodos con fecha inicio  ( del tipo antes de)
            if (year <= init_year)  and (init_year!=None) and (finish_year== None):
                choices.append(periodo.id)

                #para periodos con fecha fin  ( del tipo despues de)
            if (year >= finish_year)  and (init_year==None) and (finish_year!= None):
                choices.append(periodo.id)
        return choices

    def get_ajax(self, request, *args, **kwargs):

        obj = self.get_object(request, *args, **kwargs)
        json_dict = {
            'id': obj[0]

        }

        return self.render_json_response(json_dict)

class Year_By_Periodo_ConstruccionView(JSONResponseMixin, AjaxResponseMixin, DetailView):
    model = Periodo_Construccion
    template_name = '404.html'

    def get_object(self,request, *args, **kwargs):

        id_periodo = int(kwargs['id_periodo'])
        periodo = Periodo_Construccion.objects.get(pk=id_periodo)
        init_year = periodo.anio_inici
        finish_year =  periodo.anio_fin

        #para periodos con fecha inicio y fecha fin definidos ( del tipo entre)
        if (init_year!=None) and (finish_year!= None):

            return int((init_year + finish_year)/2)

        #para periodos con fecha inicio  ( del tipo antes de)
        if  (init_year!=None) and (finish_year== None):

            return init_year -1

            #para periodos con fecha fin  ( del tipo despues de)
        if (init_year==None) and (finish_year!= None):

            return int((finish_year +int(date.today().year))/2 )

        return -1

    def get_ajax(self, request, *args, **kwargs):

        obj = self.get_object(request, *args, **kwargs)
        print obj
        json_dict = {
            'year': obj

        }

        return self.render_json_response(json_dict)



def get_map(request, *args, **kwargs):

    template_name ='map_widget.html'

    return render_to_response(template_name,context_instance=RequestContext(request))
