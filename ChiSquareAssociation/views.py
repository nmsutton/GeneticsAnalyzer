# Copyright by Nate Sutton 2013 
"""
This file contains redirections to the main page and supporting files for this genetic analysis module.
Html post data submitted by the user is processed to enable custom filtering of the data represented in the
plot of the analysis results.
"""

from django.shortcuts import render
from django.http import HttpResponse
from django.conf.urls.defaults import *
from ChiSquareAssociation.forms import PlotCustomizationOptions
from ChiSquareAssociation.models import *
import GeneticAnalysisTools as GeneticAnalysisTools

def index(request):
    SNPList = ChiSquareAssociation.objects.all().order_by('BonfCorrectedPValue')[:40]
    context = {'SNPList': SNPList}
    return render(request, 'ChiSquareAssociation/index.html', context)

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
                return GeneticAnalysisTools.GeneratePlot.PlotData(request, 
GeneticDataRecords=ChiSquareAssociation.objects.all().filter(BonfCorrectedPValue__gt=FilterThreshold), GeneticAttributeName='BonfCorrectedPValue', PlotXLabel='SNP P-Value', PlotYLabel='Number of SNPs', PlotTitle='Total distribution of SNP P-Values')
            elif (form.cleaned_data.get('ArithmaticOperator', 0)=='GreaterThanOrEqual'):
                return GeneticAnalysisTools.GeneratePlot.PlotData(request, 
GeneticDataRecords=ChiSquareAssociation.objects.all().filter(BonfCorrectedPValue__gte=FilterThreshold), GeneticAttributeName='BonfCorrectedPValue', PlotXLabel='SNP P-Value', PlotYLabel='Number of SNPs', PlotTitle='Total distribution of SNP P-Values')
            elif (form.cleaned_data.get('ArithmaticOperator', 0)=='LessThan'):
                return GeneticAnalysisTools.GeneratePlot.PlotData(request, 
GeneticDataRecords=ChiSquareAssociation.objects.all().filter(BonfCorrectedPValue__lt=FilterThreshold), GeneticAttributeName='BonfCorrectedPValue', PlotXLabel='SNP P-Value', PlotYLabel='Number of SNPs', PlotTitle='Total distribution of SNP P-Values')
            elif (form.cleaned_data.get('ArithmaticOperator', 0)=='LessThanOrEqual'):
                return GeneticAnalysisTools.GeneratePlot.PlotData(request, 
GeneticDataRecords=ChiSquareAssociation.objects.all().filter(BonfCorrectedPValue__lte=FilterThreshold), GeneticAttributeName='BonfCorrectedPValue', PlotXLabel='SNP P-Value', PlotYLabel='Number of SNPs', PlotTitle='Total distribution of SNP P-Values')                                                
    else: return GeneticAnalysisTools.GeneratePlot.PlotData(request, GeneticDataRecords=ChiSquareAssociation.objects.all().filter(BonfCorrectedPValue__gt=FilterThreshold), GeneticAttributeName='BonfCorrectedPValue', PlotXLabel='SNP P-Value', PlotYLabel='Number of SNPs', PlotTitle='Total distribution of SNP P-Values')


def ResultsTable(request):
    form = PlotCustomizationOptions(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            FilterThreshold = form.cleaned_data.get('FilterThreshold', 0)
            if (form.cleaned_data.get('ArithmaticOperator', 0)=='GreaterThan'):
                return GeneticAnalysisTools.GenerateResultsTable.GenerateResultsTable(request, TableTitle='____________________Top SNPs____________________', TableColumnSummaryDescriptions=('Chromosome', 'SNP ID', 'Bonferroni Corrected P-Value'), TableColumnData=ChiSquareAssociation.objects.all().filter(BonfCorrectedPValue__gt=FilterThreshold).order_by('BonfCorrectedPValue')[:40], TableColumnNames=('Chromosome', 'SNP', 'BonfCorrectedPValue'))
            elif (form.cleaned_data.get('ArithmaticOperator', 0)=='GreaterThanOrEqual'):
                return GeneticAnalysisTools.GenerateResultsTable.GenerateResultsTable(request, TableTitle='____________________Top SNPs____________________', TableColumnSummaryDescriptions=('Chromosome', 'SNP ID', 'Bonferroni Corrected P-Value'), TableColumnData=ChiSquareAssociation.objects.all().filter(BonfCorrectedPValue__gte=FilterThreshold).order_by('BonfCorrectedPValue')[:40], TableColumnNames=('Chromosome', 'SNP', 'BonfCorrectedPValue'))
            elif (form.cleaned_data.get('ArithmaticOperator', 0)=='LessThan'):
                return GeneticAnalysisTools.GenerateResultsTable.GenerateResultsTable(request, TableTitle='____________________Top SNPs____________________', TableColumnSummaryDescriptions=('Chromosome', 'SNP ID', 'Bonferroni Corrected P-Value'), TableColumnData=ChiSquareAssociation.objects.all().filter(BonfCorrectedPValue__lt=FilterThreshold).order_by('BonfCorrectedPValue')[:40], TableColumnNames=('Chromosome', 'SNP', 'BonfCorrectedPValue'))
            elif (form.cleaned_data.get('ArithmaticOperator', 0)=='LessThanOrEqual'):
                return GeneticAnalysisTools.GenerateResultsTable.GenerateResultsTable(request, TableTitle='____________________Top SNPs____________________', TableColumnSummaryDescriptions=('Chromosome', 'SNP ID', 'Bonferroni Corrected P-Value'), TableColumnData=ChiSquareAssociation.objects.all().filter(BonfCorrectedPValue__lte=FilterThreshold).order_by('BonfCorrectedPValue')[:40], TableColumnNames=('Chromosome', 'SNP', 'BonfCorrectedPValue'))
    else: return GeneticAnalysisTools.GenerateResultsTable.GenerateResultsTable(request, TableTitle='____________________Top SNPs____________________', TableColumnSummaryDescriptions=('Chromosome', 'SNP ID', 'Bonferroni Corrected P-Value'), TableColumnData=ChiSquareAssociation.objects.all().order_by('BonfCorrectedPValue')[:40], TableColumnNames=('Chromosome', 'SNP', 'BonfCorrectedPValue'))    
