from django.forms.models import BaseInlineFormSet
from django.forms.models import ModelForm
from django.contrib.gis import admin

from models import Estructura
from widgets import Select_Polygon_Widget

class RequiredInlineFormSet(BaseInlineFormSet):
    """
        Clase que permite que las validaciones de los
        modelos que se colocan como inline en el
        admin de inspeccion funcionen.
    """

    def _construct_form(self, i, **kwargs):
        """
        Override the method to change the form attribute empty_permitted
        """
        form = super(RequiredInlineFormSet, self)._construct_form(i, **kwargs)
        form.empty_permitted = False
        return form


class EstructuraInlineForm(ModelForm):
    """
        Clase que permite donde se especifica
        el widget con el que se va a renderizar
        el atributo poligo del modelo Estructura.
    """

    def __init__(self, *args, **kwargs):
        super(EstructuraInlineForm, self).__init__(*args, **kwargs)
        estructura_admin = admin.site._registry[Estructura]
        model_field = self._meta.model._meta.get_field('poligono')
        self.fields['poligono'].widget = Select_Polygon_Widget()
