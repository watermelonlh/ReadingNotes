#! /bin/python

import glob
import os

os.chdir("repo")
for files in glob.glob("*.html"):
    print "<a href='repo/%s' >%s</a>" % (files, files)
