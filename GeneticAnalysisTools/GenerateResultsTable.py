# Copyright by Nate Sutton 2013 
"""
Html from the genetic experiment results table is returned in a stream to avoid an alternative approach of 
having to store a large string comprised of html in computer memory while the html is generated. 

References:
A reference used was http://stackoverflow.com/questions/2922874/how-to-stream-an-httpresponse-with-django
"""

from django.http import HttpResponse
from django.views.decorators.http import condition

@condition(etag_func=None)
def GenerateResultsTable(request, TableTitle, TableColumnSummaryDescriptions, TableColumnData, TableColumnNames):
    resp = HttpResponse( stream_response_generator(TableTitle, TableColumnSummaryDescriptions, TableColumnData, TableColumnNames), mimetype='text/html')
    return resp

def stream_response_generator(TableTitle, TableColumnSummaryDescriptions, TableColumnData, TableColumnNames):
    yield "<html><body>\n"
    yield "<u><b>"+TableTitle+"</b></u>\n"
    yield "<table><thead><tr>\n"
    for ColumnDescription in TableColumnSummaryDescriptions:
        yield "<th>"+ColumnDescription+"</th>"
    yield "\n</tr></thead><tbody>\n"
    if (TableColumnData):
        for ColumnDataEntry in TableColumnData:
            yield "<tr>"
            for ColumnName in TableColumnNames:
                yield "<td>"
                yield getattr(ColumnDataEntry, ColumnName)
                yield "</td>"
            yield "</tr>\n"
    else:
        yield "<p>No table data is available.</p>"
    yield "</body></html>\n"
