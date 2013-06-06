from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'views.home'),
    url(r'^welcome.html$', 'views.Welcome'),    
    url(r'^SNPMissingness/', include('SNPMissingness.urls')),
    url(r'^MinorAllele/', include('MinorAllele.urls')),
    url(r'^HardyWeinberg/', include('HardyWeinberg.urls')),
    url(r'^ChiSquareAssociation/', include('ChiSquareAssociation.urls')), 
)
