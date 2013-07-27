# Copyright by Nate Sutton 2013 
"""
This file specifies the attributes of any database tables that are used to access
genetic data for this genetic analysis module of the application. 
"""

from django.db import models

class MinorAllele(models.Model):
    ExtraSpace = models.CharField(max_length=200)
    Chromosome = models.IntegerField(max_length=5)
    SNP = models.CharField(primary_key=True,max_length=40)
    Cluster = models.IntegerField(max_length=30)
    Allele1 = models.IntegerField(max_length=2)
    Allele2 = models.IntegerField(max_length=2)
    MinorAlleleFrequency = models.FloatField()
    MinorAlleleCount = models.IntegerField(max_length=11)
    ExtraSpace2 = models.CharField(max_length=30)

    def __unicode__(self):
        return self.SNP
