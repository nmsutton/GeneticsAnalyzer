'''
Created on Jun 4, 2013

@author: nmsuton
'''

from django.shortcuts import render
from HardyWeinberg.models import *

def index(request):
    SNPList = HardyWeinberg.objects.all().order_by('ObservedHeterozygosity')[:40]
    context = {'SNPList': SNPList}
    return render(request, 'HardyWeinberg/index.html', context)
