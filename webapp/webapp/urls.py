from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

from apps.inspeccion.views import Periodo_Construccion_By_YearView, Year_By_Periodo_ConstruccionView, get_map, response_csv

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^periodo_given_year/(?P<year>[-\d]+)',
        Periodo_Construccion_By_YearView.as_view(),
        name="periodo_construccion_given_year"),

    url(r'^year_given_periodo/(?P<id_periodo>[-\d]+)',
        Year_By_Periodo_ConstruccionView.as_view(),
        name="year_given_periodo"),

    url('^pages/', include('django.contrib.flatpages.urls')),

    url('^mapa/', get_map),

    url('^csv/', response_csv),

    url(r'^public/(?P<path>.*)$',
        'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),








) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
