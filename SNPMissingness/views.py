'''
Created on Jun 4, 2013

@author: nmsuton
'''

from django.shortcuts import render
from SNPMissingness.models import *

def index(request):
    SNPList = SNPMissingness.objects.all().order_by('-SNPsMissingProportion')[:40]
    context = {'SNPList': SNPList}
    return render(request, 'SNPMissingness/index.html', context)
