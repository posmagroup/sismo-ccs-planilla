from django.forms.models import BaseInlineFormSet
from django.forms.models import ModelForm
from django.contrib.gis import admin

from models import Estructura
from widgets import Select_Polygon_Widget

class RequiredInlineFormSet(BaseInlineFormSet):
    """
    Generates an inline formset that is required
    """

    def _construct_form(self, i, **kwargs):
        """
        Override the method to change the form attribute empty_permitted
        """

        form = super(RequiredInlineFormSet, self)._construct_form(i, **kwargs)
        form.empty_permitted = False
        return form


class EstructuraInlineForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(EstructuraInlineForm, self).__init__(*args, **kwargs)
        estructura_admin = admin.site._registry[Estructura]
        model_field = self._meta.model._meta.get_field('poligono')
        self.fields['poligono'].widget = Select_Polygon_Widget()
