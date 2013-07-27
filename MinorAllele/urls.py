# Copyright by Nate Sutton 2013 
"""
The urls for this genetic analysis module of the application are included here.
"""

from django.conf.urls.defaults import *

from GeneticAnalysisTools import GeneratePlot, GenerateResultsTable
from MinorAllele.models import * # database access
from MinorAllele import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^plot$', views.GeneratePlot),
    url(r'^table$', views.ResultsTable),    
)
