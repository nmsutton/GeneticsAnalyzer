# Copyright by Nate Sutton 2013 
"""
This file specifies the attributes of any database tables that are used to access
genetic data for this genetic analysis module of the application. 
"""

from django.db import models

class ChiSquareAssociation(models.Model):
    ExtraSpace = models.CharField(max_length=200)
    Chromosome = models.IntegerField(max_length=5)
    SNP = models.CharField(primary_key=True,max_length=40)    
    UnadjustedPValue = models.CharField(max_length=200)
    CorrectedPValue = models.IntegerField(max_length=11)
    BonfCorrectedPValue = models.FloatField()
    HolmPValue = models.FloatField()
    SidakSSPValue = models.FloatField()
    SidakSDPValue = models.FloatField()
    FDR_BH = models.CharField(max_length=30)
    FDR_BY = models.CharField(max_length=30)
    ExtraSpace2 = models.CharField(max_length=30)

    def __unicode__(self):
        return self.SNP
