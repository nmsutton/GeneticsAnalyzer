# Copyright by Nate Sutton 2013 
"""
The urls for each sub area of this web application are here.
"""

from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'views.home'),
    url(r'^welcome.html$', 'views.Welcome'),    
    url(r'^StaticResources/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    url(r'^SNPMissingness/', include('SNPMissingness.urls')),
    url(r'^MinorAllele/', include('MinorAllele.urls')),
    url(r'^HardyWeinberg/', include('HardyWeinberg.urls')),
    url(r'^ChiSquareAssociation/', include('ChiSquareAssociation.urls')),
    url(r'^PopulationStratification/', include('PopulationStratification.urls')),  
)
