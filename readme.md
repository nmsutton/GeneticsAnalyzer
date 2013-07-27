Copyright by Nate Sutton 2013 

Thank you for using this sample genetic analysis application!

This application is meant to show an examples of ways to view and interact with 
analyses from a genetic experiment.  Some included data is from the hapmap project
and used in the site for the Plink tool at 
http://pngu.mgh.harvard.edu/~purcell/plink/tutorial.shtml .  Analyses performed in
this application were done with that tool. 

This application provides a front end for users based on html, javascript, and css.
In the back end, the Django python web framework is utilized to integrate python 
functionality into the site.  This application is built through python and includes
features based on the matplotlib graphics library.  The genetic data used in this
site is stored in a MySQL database and accessed through the use of the mysqldb 
python library and django's database interaction capabilities.

This application is designed provide examples of genetic analyses capabilities that
can be used in a wide variety of disease/other phenotype association studies.  The 
programming used for this application's underlying genetic experiment analyses 
system is able to be built upon to scale and extend to other genetic experiments 
and analyses features. 

The url.py file enables users to reach the welcome page to start using the site and
specifies the links to get to each sub area of this application.  The 
/home/home.html file is the page the site uses for all actions and individual
application modules are included in subdirectories of this base directory. 
