'''
Created on Jun 4, 2013

@author: nmsuton
'''

from django.shortcuts import render
from ChiSquareAssociation.models import *

def index(request):
    SNPList = ChiSquareAssociation.objects.all().order_by('BonfCorrectedPValue')[:40]
    context = {'SNPList': SNPList}
    return render(request, 'ChiSquareAssociation/index.html', context)
