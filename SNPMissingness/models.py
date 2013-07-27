# Copyright by Nate Sutton 2013 
"""
This file specifies the attributes of any database tables that are used to access
genetic data for this genetic analysis module of the application. 
"""

from django.db import models

class SNPMissingness(models.Model):
    ExtraSpace = models.CharField(max_length=200)
    Chromosome = models.IntegerField(max_length=5)
    SNP = models.CharField(primary_key=True,max_length=40)
    IndividualsMissingSNP = models.IntegerField(max_length=30)
    GenotypesMissing = models.IntegerField(max_length=30)
    SNPsMissingProportion = models.FloatField()

    def __unicode__(self):
        return self.SNP
