'''
Created on Jun 3, 2013

@author: nmsuton
'''

from django.conf.urls.defaults import *

from GeneticAnalysisTools import GeneratePlot
from HardyWeinberg.models import * # database access
from HardyWeinberg import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^plot$', GeneratePlot.PlotData, {'GeneticDataRecords':HardyWeinberg.objects.all(), 'GeneticAttributeName':'ObservedHeterozygosity', 'PlotXLabel':'Observed Heterozygosity', 'PlotYLabel':'Number of SNPs', 'PlotTitle':'Total distribution of SNP Observed Heterozygosity \n(I\'m working on a OH/EH graph)'}),
)
