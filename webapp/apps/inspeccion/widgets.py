from django.template.loader import render_to_string
from django.forms import widgets


class Select_Polygon_Widget(widgets.Widget):
    """
       Widget para el renderizado del mapa
       de poligonos.
    """
    def __init__(self, attrs=None):
        super( Select_Polygon_Widget, self).__init__(attrs)

    def render(self, name, value, attrs=None):

         return render_to_string("map_widget.html")


