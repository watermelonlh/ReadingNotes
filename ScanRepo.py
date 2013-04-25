#! /bin/python

import glob
import os

os.chdir("repo")
for files in glob.glob("*.html"):
    print "<h3><a href='repo/%s' >%s</a></h3>" % (files, files[:files.find('.')])
