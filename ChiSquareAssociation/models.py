from django.db import models

class ChiSquareAssociation(models.Model):
    ExtraSpace = models.CharField(max_length=200)
    Chromosome = models.IntegerField(max_length=5)
    SNP = models.CharField(primary_key=True,max_length=40)    
    UnadjustedPValue = models.CharField(max_length=200)
    CorrectedPValue = models.IntegerField(max_length=11)
    BonfCorrectedPValue = models.DecimalField(max_digits=10, decimal_places=6) 
    HolmPValue = models.DecimalField(max_digits=10, decimal_places=6) 
    SidakSSPValue = models.DecimalField(max_digits=10, decimal_places=6) 
    SidakSDPValue = models.DecimalField(max_digits=10, decimal_places=6) 
    FDR_BH = models.CharField(max_length=30)
    FDR_BY = models.CharField(max_length=30)
    ExtraSpace2 = models.CharField(max_length=30)

    def __unicode__(self):
        return self.SNP
