'''
Created on Jun 3, 2013

@author: nmsuton
'''

from django.conf.urls.defaults import *

from GeneticAnalysisTools import GeneratePlot
from SNPMissingness.models import * # database access
from SNPMissingness import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^plot$', GeneratePlot.PlotData, {'GeneticDataRecords':SNPMissingness.objects.all(), 'GeneticAttributeName':'SNPsMissingProportion', 'PlotXLabel':'SNP Missingness Proportion', 'PlotYLabel':'Number of SNPs', 'PlotTitle':'Total distribution of SNP Missingness Proportions'}),
)
