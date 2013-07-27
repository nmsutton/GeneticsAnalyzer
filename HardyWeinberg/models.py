# Copyright by Nate Sutton 2013 
"""
This file specifies the attributes of any database tables that are used to access
genetic data for this genetic analysis module of the application. 
"""

from django.db import models

class HardyWeinberg(models.Model):
    ExtraSpace = models.CharField(max_length=200)
    Chromosome = models.IntegerField(max_length=5)
    SNP = models.CharField(primary_key=True,max_length=40)
    Test = models.CharField(max_length=30)
    Allele1 = models.IntegerField(max_length=2) 
    Allele2 = models.IntegerField(max_length=2)
    GenotypeCounts = models.CharField(max_length=40)
    ObservedHeterozygosity = models.FloatField()
    ExpectedHeterozygosity = models.FloatField()
    HWPValue = models.FloatField()
    oh_divided_by_eh = models.FloatField()

    def __unicode__(self):
        return self.SNP
