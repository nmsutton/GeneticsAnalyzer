'''
Created on Jun 3, 2013

@author: nmsuton
'''

from django.conf.urls.defaults import *

from GeneticAnalysisTools import GeneratePlot
from ChiSquareAssociation.models import * # database access
from ChiSquareAssociation import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^plot$', GeneratePlot.PlotData, {'GeneticDataRecords':ChiSquareAssociation.objects.all(), 'GeneticAttributeName':'BonfCorrectedPValue', 'PlotXLabel':'SNP P-Value', 'PlotYLabel':'Number of SNPs', 'PlotTitle':'Total distribution of SNP P-Values'}),
)
