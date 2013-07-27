# Copyright by Nate Sutton 2013 
"""
This file contains redirections to the main page and supporting files for this genetic analysis module.
Html post data submitted by the user is processed to enable custom filtering of the data represented in the
plot of the analysis results.
"""

from django.shortcuts import render
from django.http import HttpResponse
from django.conf.urls.defaults import *
from SNPMissingness.forms import PlotCustomizationOptions
from SNPMissingness.models import *
import GeneticAnalysisTools as GeneticAnalysisTools

def index(request):
    SNPList = SNPMissingness.objects.all().order_by('-SNPsMissingProportion')[:40]
    context = {'SNPList': SNPList}
    return render(request, 'SNPMissingness/index.html', context)


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
                return GeneticAnalysisTools.GeneratePlot.PlotData(request, GeneticDataRecords=SNPMissingness.objects.all().filter(SNPsMissingProportion__gt=FilterThreshold), GeneticAttributeName='SNPsMissingProportion', PlotXLabel='SNP Missingness Proportion', PlotYLabel='Number of SNPs', PlotTitle='Distribution of SNP Missingness Proportions')
            elif (form.cleaned_data.get('ArithmaticOperator', 0)=='GreaterThanOrEqual'):
                return GeneticAnalysisTools.GeneratePlot.PlotData(request, GeneticDataRecords=SNPMissingness.objects.all().filter(SNPsMissingProportion__gte=FilterThreshold), GeneticAttributeName='SNPsMissingProportion', PlotXLabel='SNP Missingness Proportion', PlotYLabel='Number of SNPs', PlotTitle='Distribution of SNP Missingness Proportions')
            elif (form.cleaned_data.get('ArithmaticOperator', 0)=='LessThan'):
                return GeneticAnalysisTools.GeneratePlot.PlotData(request, GeneticDataRecords=SNPMissingness.objects.all().filter(SNPsMissingProportion__lt=FilterThreshold), GeneticAttributeName='SNPsMissingProportion', PlotXLabel='SNP Missingness Proportion', PlotYLabel='Number of SNPs', PlotTitle='Distribution of SNP Missingness Proportions')
            elif (form.cleaned_data.get('ArithmaticOperator', 0)=='LessThanOrEqual'):
                return GeneticAnalysisTools.GeneratePlot.PlotData(request, GeneticDataRecords=SNPMissingness.objects.all().filter(SNPsMissingProportion__lte=FilterThreshold), GeneticAttributeName='SNPsMissingProportion', PlotXLabel='SNP Missingness Proportion', PlotYLabel='Number of SNPs', PlotTitle='Distribution of SNP Missingness Proportions')                                       
    else: return GeneticAnalysisTools.GeneratePlot.PlotData(request, GeneticDataRecords=SNPMissingness.objects.all(), GeneticAttributeName='SNPsMissingProportion', PlotXLabel='SNP Missingness Proportion', PlotYLabel='Number of SNPs', PlotTitle='Distribution of SNP Missingness Proportions')

def ResultsTable(request):
    """
    This method enables the code that generates the table of genetic experiment results to be accessed and filtered through user submitted form data. 
    """
    form = PlotCustomizationOptions(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            FilterThreshold = form.cleaned_data.get('FilterThreshold', 0)
            if (form.cleaned_data.get('ArithmaticOperator', 0)=='GreaterThan'):
                return GeneticAnalysisTools.GenerateResultsTable.GenerateResultsTable(request, TableTitle='_____________Top SNPs_____________', TableColumnSummaryDescriptions=('SNP ID', 'SNP Missingness Proportion'), TableColumnData=SNPMissingness.objects.all().filter(SNPsMissingProportion__gt=FilterThreshold).order_by('-SNPsMissingProportion')[:40], TableColumnNames=('SNP', 'SNPsMissingProportion'))
            elif (form.cleaned_data.get('ArithmaticOperator', 0)=='GreaterThanOrEqual'):
                return GeneticAnalysisTools.GenerateResultsTable.GenerateResultsTable(request, TableTitle='_____________Top SNPs_____________', TableColumnSummaryDescriptions=('SNP ID', 'SNP Missingness Proportion'), TableColumnData=SNPMissingness.objects.all().filter(SNPsMissingProportion__gte=FilterThreshold).order_by('-SNPsMissingProportion')[:40], TableColumnNames=('SNP', 'SNPsMissingProportion'))
            elif (form.cleaned_data.get('ArithmaticOperator', 0)=='LessThan'):
                return GeneticAnalysisTools.GenerateResultsTable.GenerateResultsTable(request, TableTitle='_____________Top SNPs_____________', TableColumnSummaryDescriptions=('SNP ID', 'SNP Missingness Proportion'), TableColumnData=SNPMissingness.objects.all().filter(SNPsMissingProportion__lt=FilterThreshold).order_by('-SNPsMissingProportion')[:40], TableColumnNames=('SNP', 'SNPsMissingProportion'))
            elif (form.cleaned_data.get('ArithmaticOperator', 0)=='LessThanOrEqual'):
                return GeneticAnalysisTools.GenerateResultsTable.GenerateResultsTable(request, TableTitle='_____________Top SNPs_____________', TableColumnSummaryDescriptions=('SNP ID', 'SNP Missingness Proportion'), TableColumnData=SNPMissingness.objects.all().filter(SNPsMissingProportion__lte=FilterThreshold).order_by('-SNPsMissingProportion')[:40], TableColumnNames=('SNP', 'SNPsMissingProportion'))                                                
    else: return GeneticAnalysisTools.GenerateResultsTable.GenerateResultsTable(request, TableTitle='_____________Top SNPs_____________', TableColumnSummaryDescriptions=('SNP ID', 'SNP Missingness Proportion'), TableColumnData=SNPMissingness.objects.all().order_by('-SNPsMissingProportion')[:40], TableColumnNames=('SNP', 'SNPsMissingProportion'))
