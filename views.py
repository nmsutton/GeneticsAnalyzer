import os
from django.shortcuts import render

def home(request):
    return render(request, 'home/home.html')

def Welcome(request):
    return render(request, 'home/welcome.html')

