# Copyright by Nate Sutton 2013 
"""
This file contains redirections to the main page and supporting files for this genetic analysis module.
Html post data submitted by the user is processed to enable custom filtering of the data represented in the
plot of the analysis results.
"""

from django.shortcuts import render
from django.http import HttpResponse
from django.conf.urls.defaults import *
from HardyWeinberg.models import *
from HardyWeinberg.forms import PlotCustomizationOptions
import GeneticAnalysisTools as GeneticAnalysisTools

def index(request):
    SNPList = HardyWeinberg.objects.all().filter(ObservedHeterozygosity__gt=0).order_by('oh_divided_by_eh')[:40]
    context = {'SNPList': SNPList}
    return render(request, 'HardyWeinberg/index.html', context)

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
            if (form.cleaned_data.get('ArithmaticOperator', 0)=='GreaterThan'):
                return GeneticAnalysisTools.GeneratePlot.PlotData(request, GeneticDataRecords=HardyWeinberg.objects.all().filter(oh_divided_by_eh__gt=FilterThreshold), GeneticAttributeName='oh_divided_by_eh', PlotXLabel='Observed Heterozygosity / Expected Heterozygosity', PlotYLabel='Number of SNPs', PlotTitle='Total distribution of SNP Observed Heterozygosity / Expected Heterozygosity')
            elif (form.cleaned_data.get('ArithmaticOperator', 0)=='GreaterThanOrEqual'):
                return GeneticAnalysisTools.GeneratePlot.PlotData(request, GeneticDataRecords=HardyWeinberg.objects.all().filter(oh_divided_by_eh__gte=FilterThreshold), GeneticAttributeName='oh_divided_by_eh', PlotXLabel='Observed Heterozygosity / Expected Heterozygosity', PlotYLabel='Number of SNPs', PlotTitle='Total distribution of SNP Observed Heterozygosity / Expected Heterozygosity')
            elif (form.cleaned_data.get('ArithmaticOperator', 0)=='LessThan'):
                return GeneticAnalysisTools.GeneratePlot.PlotData(request, GeneticDataRecords=HardyWeinberg.objects.all().filter(oh_divided_by_eh__lt=FilterThreshold), GeneticAttributeName='oh_divided_by_eh', PlotXLabel='Observed Heterozygosity / Expected Heterozygosity', PlotYLabel='Number of SNPs', PlotTitle='Total distribution of SNP Observed Heterozygosity / Expected Heterozygosity')
            elif (form.cleaned_data.get('ArithmaticOperator', 0)=='LessThanOrEqual'):
                return GeneticAnalysisTools.GeneratePlot.PlotData(request, GeneticDataRecords=HardyWeinberg.objects.all().filter(oh_divided_by_eh__lte=FilterThreshold), GeneticAttributeName='oh_divided_by_eh', PlotXLabel='Observed Heterozygosity / Expected Heterozygosity', PlotYLabel='Number of SNPs', PlotTitle='Total distribution of SNP Observed Heterozygosity / Expected Heterozygosity')                                                
    else: return GeneticAnalysisTools.GeneratePlot.PlotData(request, GeneticDataRecords=HardyWeinberg.objects.all(), GeneticAttributeName='oh_divided_by_eh', PlotXLabel='Observed Heterozygosity / Expected Heterozygosity', PlotYLabel='Number of SNPs', PlotTitle='Total distribution of SNP Observed Heterozygosity / Expected Heterozygosity')

def ResultsTable(request):
    form = PlotCustomizationOptions(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            FilterThreshold = form.cleaned_data.get('FilterThreshold', 0)
            if (form.cleaned_data.get('ArithmaticOperator', 0)=='GreaterThan'):
                return GeneticAnalysisTools.GenerateResultsTable.GenerateResultsTable(request, TableTitle='____________________Top SNPs____________________', TableColumnSummaryDescriptions=('SNP ID', 'Observed Heterozygosity', 'Expected Heterozygosity', 'Observed/Expected Heterozygosity'), TableColumnData=HardyWeinberg.objects.all().filter(oh_divided_by_eh__gt=FilterThreshold).order_by('-oh_divided_by_eh')[:40], TableColumnNames=('SNP', 'ObservedHeterozygosity', 'ExpectedHeterozygosity', 'oh_divided_by_eh'))
            elif (form.cleaned_data.get('ArithmaticOperator', 0)=='GreaterThanOrEqual'):
                return GeneticAnalysisTools.GenerateResultsTable.GenerateResultsTable(request, TableTitle='____________________Top SNPs____________________', TableColumnSummaryDescriptions=('SNP ID', 'Observed Heterozygosity', 'Expected Heterozygosity', 'Observed/Expected Heterozygosity'), TableColumnData=HardyWeinberg.objects.all().filter(oh_divided_by_eh__gte=FilterThreshold).order_by('-oh_divided_by_eh')[:40], TableColumnNames=('SNP', 'ObservedHeterozygosity', 'ExpectedHeterozygosity', 'oh_divided_by_eh'))
            elif (form.cleaned_data.get('ArithmaticOperator', 0)=='LessThan'):
                return GeneticAnalysisTools.GenerateResultsTable.GenerateResultsTable(request, TableTitle='____________________Top SNPs____________________', TableColumnSummaryDescriptions=('SNP ID', 'Observed Heterozygosity', 'Expected Heterozygosity', 'Observed/Expected Heterozygosity'), TableColumnData=HardyWeinberg.objects.all().filter(oh_divided_by_eh__lt=FilterThreshold).order_by('-oh_divided_by_eh')[:40], TableColumnNames=('SNP', 'ObservedHeterozygosity', 'ExpectedHeterozygosity', 'oh_divided_by_eh'))
            elif (form.cleaned_data.get('ArithmaticOperator', 0)=='LessThanOrEqual'):
                return GeneticAnalysisTools.GenerateResultsTable.GenerateResultsTable(request, TableTitle='____________________Top SNPs____________________', TableColumnSummaryDescriptions=('SNP ID', 'Observed Heterozygosity', 'Expected Heterozygosity', 'Observed/Expected Heterozygosity'), TableColumnData=HardyWeinberg.objects.all().filter(oh_divided_by_eh__lte=FilterThreshold).order_by('-oh_divided_by_eh')[:40], TableColumnNames=('SNP', 'ObservedHeterozygosity', 'ExpectedHeterozygosity', 'oh_divided_by_eh'))                                                
    else: return GeneticAnalysisTools.GenerateResultsTable.GenerateResultsTable(request, TableTitle='____________________Top SNPs____________________', TableColumnSummaryDescriptions=('SNP ID', 'Observed Heterozygosity', 'Expected Heterozygosity', 'Observed/Expected Heterozygosity'), TableColumnData=HardyWeinberg.objects.all().order_by('-oh_divided_by_eh')[:40], TableColumnNames=('SNP', 'ObservedHeterozygosity', 'ExpectedHeterozygosity', 'oh_divided_by_eh'))