#! /bin/python

import glob
import os

os.chdir("repo")
for files in glob.glob("*.html"):
    print "<a herf='repo/%s' />" %files
