'''
Created on Jun 4, 2013

@author: nmsuton
'''

from django.shortcuts import render
from MinorAllele.models import *

def index(request):
    SNPList = MinorAllele.objects.all().order_by('MinorAlleleFrequency')[:40]
    context = {'SNPList': SNPList}
    return render(request, 'MinorAllele/index.html', context)
