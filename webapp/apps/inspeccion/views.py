from django.http.response import HttpResponse

from braces.views import AjaxResponseMixin, JSONResponseMixin
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView

from models import Periodo_Construccion



class Periodo_Construccion_By_YearView(JSONResponseMixin, AjaxResponseMixin, DetailView):
    model = Periodo_Construccion
    template_name = '404.html'

    def get_object(self,request, *args, **kwargs):

        periodos = Periodo_Construccion.objects.all().order_by('anio_inici')[:1]
        choices = []





        return periodos[0]

    def get_ajax(self, request, *args, **kwargs):
        print kwargs
        obj = self.get_object(request, *args, **kwargs)
        json_dict = {
            'name': obj.id,
            'location': "New York, NY"
        }

        return self.render_json_response(json_dict)


