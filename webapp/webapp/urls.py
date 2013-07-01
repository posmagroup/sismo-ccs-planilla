from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

from apps.inspeccion.views import Periodo_Construccion_By_YearView,Year_By_Periodo_ConstruccionView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sismo_caracas.views.home', name='home'),
    # url(r'^sismo_caracas/', include('sismo_caracas.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
     url(r'^periodo_given_year/(?P<year>[-\d]+)',Periodo_Construccion_By_YearView.as_view(),name="periodo_construccion_given_year"),
    url(r'^year_given_periodo/(?P<id_periodo>[-\d]+)',Year_By_Periodo_ConstruccionView.as_view(),name="year_given_periodo"),
    url(r'^public/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
