# Copyright by Nate Sutton 2013 
"""
This file specifies the attributes of any database tables that are used to access
genetic data for this genetic analysis module of the application. 
"""

from django.db import models

class PopulationStratification(models.Model):
    ID = models.CharField(primary_key=True,max_length=40)
    MDS1 = models.FloatField()
    MDS2 = models.FloatField()

    def __unicode__(self):
        return self.SNP
