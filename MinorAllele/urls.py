'''
Created on Jun 3, 2013

@author: nmsuton
'''

from django.conf.urls.defaults import *

from GeneticAnalysisTools import GeneratePlot
from MinorAllele.models import * # database access
from MinorAllele import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^plot$', GeneratePlot.PlotData, {'GeneticDataRecords':MinorAllele.objects.all(), 'GeneticAttributeName':'MinorAlleleFrequency', 'PlotXLabel':'Minor Allele Frequency', 'PlotYLabel':'Number of SNPs', 'PlotTitle':'Total distribution of SNP Minor Allele Frequencies'}),
)
