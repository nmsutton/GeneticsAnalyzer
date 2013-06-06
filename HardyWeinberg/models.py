from django.db import models

class HardyWeinberg(models.Model):
    ExtraSpace = models.CharField(max_length=200)
    Chromosome = models.IntegerField(max_length=5)
    SNP = models.CharField(primary_key=True,max_length=40)
    Test = models.CharField(max_length=30)
    Allele1 = models.IntegerField(max_length=2) 
    Allele2 = models.IntegerField(max_length=2)
    GenotypeCounts = models.CharField(max_length=40)
    ObservedHeterozygosity = models.DecimalField(max_digits=8, decimal_places=8)
    ExpectedHeterozygosity = models.DecimalField(max_digits=8, decimal_places=8)
    HWPValue = models.DecimalField(max_digits=10, decimal_places=5)

    def __unicode__(self):
        return self.SNP
