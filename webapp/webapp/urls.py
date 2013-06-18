from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from apps.inspeccion.views import Periodo_Construccion_By_YearView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sismo_caracas.views.home', name='home'),
    # url(r'^sismo_caracas/', include('sismo_caracas.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
     url(r'^periodo_given_year/(?P<year>[-\d]+)',Periodo_Construccion_By_YearView.as_view(),name="periodo_construccion_given_year"),
)
