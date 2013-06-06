'''
Created on Jun 3, 2013

@author: nmsuton
'''

# Some code used from http://stackoverflow.com/questions/5515278/plot-matplotlib-on-the-web
# http://stackoverflow.com/questions/5515278/plot-matplotlib-on-the-web
# http://stackoverflow.com/questions/8328198/pil-valueerror-not-enough-image-data

from django.http import HttpResponse
import StringIO, cStringIO
import Image, ImageDraw # image libraries
import os, tempfile
os.environ['MPLCONFIGDIR'] = tempfile.mkdtemp() # Added to ccomidate websever matplotlib access 
import matplotlib # added first to avoid dep error. https://groups.google.com/forum/?fromgroups#!topic/modwsgi/97bnQk9ojtY
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.figure import Figure                      
from matplotlib.backends.backend_agg import FigureCanvasAgg
import matplotlib.mlab as mlab

'''
Created on Jun 3, 2013

@author: nmsuton
'''

# Some code used from http://stackoverflow.com/questions/5515278/plot-matplotlib-on-the-web
# http://stackoverflow.com/questions/5515278/plot-matplotlib-on-the-web
# http://stackoverflow.com/questions/8328198/pil-valueerror-not-enough-image-data

from django.http import HttpResponse
import StringIO, cStringIO
import Image, ImageDraw # image libraries
import os, tempfile
os.environ['MPLCONFIGDIR'] = tempfile.mkdtemp() # Added to ccomidate websever matplotlib access 
import matplotlib # added first to avoid dep error. https://groups.google.com/forum/?fromgroups#!topic/modwsgi/97bnQk9ojtY
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.figure import Figure                      
from matplotlib.backends.backend_agg import FigureCanvasAgg
import matplotlib.mlab as mlab

def PlotData(request, GeneticDataRecords, GeneticAttributeName, PlotXLabel, PlotYLabel, PlotTitle):
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
