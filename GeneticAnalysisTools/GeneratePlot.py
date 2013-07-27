# Copyright by Nate Sutton 2013 
"""
The code here is for the generation of plots used to display results from the genetic analyses.
Database columns are passed into this file and the plots are dynamically created with the use
of the column data.  The scale of the plot is automatically adjusted by the matplotlib library.  

References:
Some code used from http://stackoverflow.com/questions/5515278/plot-matplotlib-on-the-web
http://stackoverflow.com/questions/5515278/plot-matplotlib-on-the-web
http://stackoverflow.com/questions/8328198/pil-valueerror-not-enough-image-data
https://groups.google.com/forum/?fromgroups#!topic/modwsgi/97bnQk9ojtY
"""

from django.http import HttpResponse
import StringIO, cStringIO
import Image, ImageDraw # image libraries
import os, tempfile
os.environ['MPLCONFIGDIR'] = tempfile.mkdtemp() # Added to accomidate websever matplotlib access 
import matplotlib # added first to avoid dep error.
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.figure import Figure                      
from matplotlib.backends.backend_agg import FigureCanvasAgg
import matplotlib.mlab as mlab

def PlotData(request, GeneticDataRecords, GeneticAttributeName, PlotXLabel, PlotYLabel, PlotTitle):
    """
    This is the standard genetic module plotting option and a histogram is created.  The plot is written to
    a string buffer and later rendered as a png image which is returned in a html response.  The image is not
    needed to be saved as a file in the hard disk each time it is created.
    """
    AttributeGroupGeneticDataRecords = []
    for RecordEntry in GeneticDataRecords:
        AttributeGroupGeneticDataRecords.append(float(getattr(RecordEntry, GeneticAttributeName)))

    plt.xlabel(PlotXLabel)
    plt.ylabel(PlotYLabel)
    plt.title(PlotTitle)
    fig = Figure(figsize=[8,8])                               
    ax = fig.add_subplot(1,1,1)
    ax.hist(AttributeGroupGeneticDataRecords, 23, normed=1, facecolor='green', alpha=0.75)
    canvas = FigureCanvasAgg(fig)
    ax.set_xlabel(PlotXLabel)
    ax.set_ylabel(PlotYLabel)
    ax.set_title(PlotTitle)

    # write image data to a string buffer and get the PNG image bytes
    buf = cStringIO.StringIO()
    canvas.print_png(buf)
    data = buf.getvalue()
    
    img = Image.open(StringIO.StringIO(data))
    response = HttpResponse(mimetype="image/png")
    img.save(response, 'PNG')

    return (response)

def ScatterPlotData(request, GeneticDataRecords, GeneticAttributeNameA, GeneticAttributeNameB, ClusterCutOff, PlotXLabel, PlotYLabel, PlotTitle):
    """ 
    This plotting option is for creating a scatter plot.  
    """
    plt.xlabel(PlotXLabel)
    plt.ylabel(PlotYLabel)
    plt.title(PlotTitle)
    fig = Figure(figsize=[8,8])                               
    ax = fig.add_subplot(1,1,1)
    # A color swtich is added below for any data past the threshold inputted into this method.
    for GeneticAttributeEntry in GeneticDataRecords:
        if (float(getattr(GeneticAttributeEntry, GeneticAttributeNameA)) < float(ClusterCutOff)):
            ax.scatter(float(getattr(GeneticAttributeEntry, GeneticAttributeNameA)),float(getattr(GeneticAttributeEntry, GeneticAttributeNameB)),c="blue")
        else:
            ax.scatter(float(getattr(GeneticAttributeEntry, GeneticAttributeNameA)),float(getattr(GeneticAttributeEntry, GeneticAttributeNameB)),c="red")
    canvas = FigureCanvasAgg(fig)
    ax.set_xlabel(PlotXLabel)
    ax.set_ylabel(PlotYLabel)
    ax.set_title(PlotTitle)

    # write image data to a string buffer and get the PNG image bytes
    buf = cStringIO.StringIO()
    canvas.print_png(buf)
    data = buf.getvalue()
    
    img = Image.open(StringIO.StringIO(data))
    response = HttpResponse(mimetype="image/png")
    img.save(response, 'PNG')

    return (response)