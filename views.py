# Copyright by Nate Sutton 2013 
"""
This file contains redirections to the main and welcome pages in this application.
"""

import os
from django.shortcuts import render

def home(request):
    return render(request, 'home/home.html')

def Welcome(request):
    return render(request, 'home/welcome.html')

