# Copyright by Nate Sutton 2013 
"""
This file contains redirections to the main page and supporting files for this genetic analysis module.
Html post data submitted by the user is processed to enable custom filtering of the data represented in the
plot of the analysis results.
"""

from django.shortcuts import render
from django.http import HttpResponse
from django.conf.urls.defaults import *
from PopulationStratification.forms import PlotCustomizationOptions
from PopulationStratification.models import *
import GeneticAnalysisTools as GeneticAnalysisTools

def index(request):
    SNPList = PopulationStratification.objects.all()
    context = {'SNPList': SNPList}
    return render(request, 'PopulationStratification/index.html', context)


def GeneratePlot(request):
    """
    Input options from the analysis filtering html form is processed here and custom django database filtering procedures are automatically 
    specified.  Labels for the plot are dynamically created based on the parameters included when the plotting method.  The column name in the
    relevant database table is specified through a django parameter to access the data relevant to this genetic analysis module.    
    """
    form = PlotCustomizationOptions(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            FilterThreshold = form.cleaned_data.get('FilterThreshold', 0)
            return GeneticAnalysisTools.GeneratePlot.ScatterPlotData(request, GeneticDataRecords=PopulationStratification.objects.all(), GeneticAttributeNameA='MDS1', GeneticAttributeNameB='MDS2', ClusterCutOff=FilterThreshold, PlotXLabel='Multidimentional Scaling Factor 1', PlotYLabel='Multidimentional Scaling Factor 2', PlotTitle='Population stratification amongst individuals')
    else: return GeneticAnalysisTools.GeneratePlot.ScatterPlotData(request, GeneticDataRecords=PopulationStratification.objects.all(), GeneticAttributeNameA='MDS1', GeneticAttributeNameB='MDS2', ClusterCutOff='-0.01', PlotXLabel='Multidimentional Scaling Factor 1', PlotYLabel='Multidimentional Scaling Factor 2', PlotTitle='Population stratification amongst individuals')
