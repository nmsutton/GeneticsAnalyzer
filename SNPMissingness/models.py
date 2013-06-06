from django.db import models

class SNPMissingness(models.Model):
    ExtraSpace = models.CharField(max_length=200)
    Chromosome = models.IntegerField(max_length=5)
    SNP = models.CharField(primary_key=True,max_length=40)
    IndividualsMissingSNP = models.IntegerField(max_length=30)
    GenotypesMissing = models.IntegerField(max_length=30)
    SNPsMissingProportion = models.DecimalField(max_digits=8, decimal_places=8)

    def __unicode__(self):
        return self.SNP
