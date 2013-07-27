# Copyright by Nate Sutton 2013 
"""
This file contains redirections to the main page and supporting files for this genetic analysis module.
Html post data submitted by the user is processed to enable custom filtering of the data represented in the
plot of the analysis results.
"""

from django.shortcuts import render
from django.http import HttpResponse
from django.conf.urls.defaults import *
from MinorAllele.forms import PlotCustomizationOptions
from MinorAllele.models import *
import GeneticAnalysisTools as GeneticAnalysisTools

def index(request):
    SNPList = MinorAllele.objects.all().order_by('MinorAlleleFrequency')[:40]
    context = {'SNPList': SNPList}
    return render(request, 'MinorAllele/index.html', context)

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
                return GeneticAnalysisTools.GeneratePlot.PlotData(request, GeneticDataRecords=MinorAllele.objects.all().filter(MinorAlleleFrequency__gt=FilterThreshold), GeneticAttributeName='MinorAlleleFrequency', PlotXLabel='Minor Allele Frequency', PlotYLabel='Number of SNPs', PlotTitle='Distribution of SNP Minor Allele Frequencies')
            elif (form.cleaned_data.get('ArithmaticOperator', 0)=='GreaterThanOrEqual'):
                return GeneticAnalysisTools.GeneratePlot.PlotData(request, GeneticDataRecords=MinorAllele.objects.all().filter(MinorAlleleFrequency__gte=FilterThreshold), GeneticAttributeName='MinorAlleleFrequency', PlotXLabel='Minor Allele Frequency', PlotYLabel='Number of SNPs', PlotTitle='Distribution of SNP Minor Allele Frequencies')
            elif (form.cleaned_data.get('ArithmaticOperator', 0)=='LessThan'):
                return GeneticAnalysisTools.GeneratePlot.PlotData(request, GeneticDataRecords=MinorAllele.objects.all().filter(MinorAlleleFrequency__lt=FilterThreshold), GeneticAttributeName='MinorAlleleFrequency', PlotXLabel='Minor Allele Frequency', PlotYLabel='Number of SNPs', PlotTitle='Distribution of SNP Minor Allele Frequencies')
            elif (form.cleaned_data.get('ArithmaticOperator', 0)=='LessThanOrEqual'):
                return GeneticAnalysisTools.GeneratePlot.PlotData(request, GeneticDataRecords=MinorAllele.objects.all().filter(MinorAlleleFrequency__lte=FilterThreshold), GeneticAttributeName='MinorAlleleFrequency', PlotXLabel='Minor Allele Frequency', PlotYLabel='Number of SNPs', PlotTitle='Distribution of SNP Minor Allele Frequencies')                                              
    else: return GeneticAnalysisTools.GeneratePlot.PlotData(request, GeneticDataRecords=MinorAllele.objects.all(), GeneticAttributeName='MinorAlleleFrequency', PlotXLabel='Minor Allele Frequency', PlotYLabel='Number of SNPs', PlotTitle='Distribution of SNP Minor Allele Frequencies')


def ResultsTable(request):
    """
    This method enables the code that generates the table of genetic experiment results to be accessed and filtered through user submitted form data. 
    """
    form = PlotCustomizationOptions(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            FilterThreshold = form.cleaned_data.get('FilterThreshold', 0)
            if (form.cleaned_data.get('ArithmaticOperator', 0)=='GreaterThan'):
                return GeneticAnalysisTools.GenerateResultsTable.GenerateResultsTable(request, TableTitle='___________Top SNPs___________', TableColumnSummaryDescriptions=('SNP ID', 'Minor Allele Frequency'), TableColumnData=MinorAllele.objects.all().filter(MinorAlleleFrequency__gt=FilterThreshold).order_by('-MinorAlleleFrequency')[:40], TableColumnNames=('SNP', 'MinorAlleleFrequency'))
            elif (form.cleaned_data.get('ArithmaticOperator', 0)=='GreaterThanOrEqual'):
                return GeneticAnalysisTools.GenerateResultsTable.GenerateResultsTable(request, TableTitle='___________Top SNPs___________', TableColumnSummaryDescriptions=('SNP ID', 'Minor Allele Frequency'), TableColumnData=MinorAllele.objects.all().filter(MinorAlleleFrequency__gte=FilterThreshold).order_by('-MinorAlleleFrequency')[:40], TableColumnNames=('SNP', 'MinorAlleleFrequency'))
            elif (form.cleaned_data.get('ArithmaticOperator', 0)=='LessThan'):
                return GeneticAnalysisTools.GenerateResultsTable.GenerateResultsTable(request, TableTitle='___________Top SNPs___________', TableColumnSummaryDescriptions=('SNP ID', 'Minor Allele Frequency'), TableColumnData=MinorAllele.objects.all().filter(MinorAlleleFrequency__lt=FilterThreshold).order_by('-MinorAlleleFrequency')[:40], TableColumnNames=('SNP', 'MinorAlleleFrequency'))
            elif (form.cleaned_data.get('ArithmaticOperator', 0)=='LessThanOrEqual'):
                return GeneticAnalysisTools.GenerateResultsTable.GenerateResultsTable(request, TableTitle='___________Top SNPs___________', TableColumnSummaryDescriptions=('SNP ID', 'Minor Allele Frequency'), TableColumnData=MinorAllele.objects.all().filter(MinorAlleleFrequency__lte=FilterThreshold).order_by('-MinorAlleleFrequency')[:40], TableColumnNames=('SNP', 'MinorAlleleFrequency'))                                                
    else: return GeneticAnalysisTools.GenerateResultsTable.GenerateResultsTable(request, TableTitle='___________Top SNPs___________', TableColumnSummaryDescriptions=('SNP ID', 'Minor Allele Frequency'), TableColumnData=MinorAllele.objects.all().order_by('-MinorAlleleFrequency')[:40], TableColumnNames=('SNP', 'MinorAlleleFrequency'))