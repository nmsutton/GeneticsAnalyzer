# Copyright by Nate Sutton 2013 
"""
This file specifies the attributes that are passed through html forms into python files for
this genetic analysis module of the application.   

References:
Some code used from http://stackoverflow.com/questions/8433510/html-forms-to-django
"""

from django import forms

class PlotCustomizationOptions(forms.Form):
    FilterThreshold = forms.FloatField()
