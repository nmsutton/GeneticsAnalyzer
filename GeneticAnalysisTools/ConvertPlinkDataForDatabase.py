#!/usr/bin/python

# Copyright by Nate Sutton 2013 
"""
This file is used for converting analyses results generated with the plink tool into a format that works with importing it into
this application's MySQL database.  It is used as a stand alone tool but is needed for creating this application.  The results
file is parsed and reformatted using regular expressions.

References:
Used some code from http://www.tutorialspoint.com/python/python_files_io.htm
"""

import re
import sys

def FilterInput(InputFile, OutputFile, RegEx):
    for line in InputFile.readlines():
        RegExMatch = RegEx.match(line)
        if (sys.argv[1]=='SNPMissingness'):
            FilterReplacementPattern = " "+RegExMatch.group(2)+" "+RegExMatch.group(4)+" "+RegExMatch.group(6)+" "+RegExMatch.group(8)+" "+RegExMatch.group(10)+"\n";  #" $2 $4 $6 $8 $10"
        elif (sys.argv[1]=='MinorAllele'):
            FilterReplacementPattern = " "+RegExMatch.group(2)+" "+RegExMatch.group(4)+" "+RegExMatch.group(6)+" "+RegExMatch.group(8)+" "+RegExMatch.group(10)+" "+RegExMatch.group(12)+" "+RegExMatch.group(14)+" "+RegExMatch.group(16)+"\n";  #$2 $4 $6 $8 $10 $12 $14 $16
        elif (sys.argv[1]=='HardyWeinburg'):
            FilterReplacementPattern = " "+RegExMatch.group(2)+" "+RegExMatch.group(4)+" "+RegExMatch.group(6)+" "+RegExMatch.group(8)+" "+RegExMatch.group(10)+" "+RegExMatch.group(12)+" "+RegExMatch.group(14)+" "+RegExMatch.group(16)+"\n";  #$2 $4 $6 $8 $10 $12 $14 $16
        elif (sys.argv[1]=='ChiSquare'):
            FilterReplacementPattern = " "+RegExMatch.group(2)+" "+RegExMatch.group(4)+" "+RegExMatch.group(6)+" "+RegExMatch.group(8)+" "+RegExMatch.group(10)+" "+RegExMatch.group(12)+" "+RegExMatch.group(14)+" "+RegExMatch.group(16)+" "+RegExMatch.group(18)+" "+RegExMatch.group(20)+"\n";  #$2 $4 $6 $8 $10 $12 $14 $16            

        OutputFile.write(FilterReplacementPattern);

if (sys.argv[1]=='SNPMissingness'):
    InputFile = open('/var/lib/mysql/hapmapdata/hapmap1_missing.lmiss')
    OutputFile = open('/var/lib/mysql/hapmapdata/hapmap1_missing_converted.lmiss', 'w+')
    RegEx = re.compile("(\s+)(\S+)(\s+)(\S+)(\s+)(\S+)(\s+)(\S+)(\s+)(\S+)", re.IGNORECASE)    
    FilterInput(InputFile, OutputFile, RegEx)
    
elif (sys.argv[1]=='MinorAllele'):
    InputFile = open('/var/lib/mysql/hapmapdata/hapmap_minorallele.frq.strat')
    OutputFile = open('/var/lib/mysql/hapmapdata/hapmap_minorallele_converted', 'w+')
    RegEx = re.compile("(\s+)(\S+)(\s+)(\S+)(\s+)(\S+)(\s+)(\S+)(\s+)(\S+)(\s+)(\S+)(\s+)(\S+)(\s+)(\S+)(\s+)", re.IGNORECASE)
    FilterInput(InputFile, OutputFile, RegEx)   

elif (sys.argv[1]=='HardyWeinburg'):
    InputFile = open('/var/lib/mysql/hapmapdata/hapmap1_hardyw.hwe')
    OutputFile = open('/var/lib/mysql/hapmapdata/hapmap1_hardyw_converted.hwe', 'w+')
    RegEx = re.compile("(\s+)(\S+)(\s+)(\S+)(\s+)(\S+)(\s+)(\S+)(\s+)(\S+)(\s+)(\S+)(\s+)(\S+)(\s+)(\S+)(\s+)", re.IGNORECASE)
    FilterInput(InputFile, OutputFile, RegEx)   

elif (sys.argv[1]=='ChiSquare'):
    InputFile = open('/var/lib/mysql/hapmapdata/hapmap1_assoc.assoc')
    OutputFile = open('/var/lib/mysql/hapmapdata/hapmap1_assoc_converted.assoc', 'w+')
    RegEx = re.compile("(\s+)(\S+)(\s+)(\S+)(\s+)(\S+)(\s+)(\S+)(\s+)(\S+)(\s+)(\S+)(\s+)(\S+)(\s+)(\S+)(\s+)(\S+)(\s+)(\S+)(\s+)", re.IGNORECASE)
    FilterInput(InputFile, OutputFile, RegEx) 