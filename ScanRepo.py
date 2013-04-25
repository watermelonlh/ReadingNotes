#! /bin/python

import glob
import os

f1 = open("template", "r")
f = f1.read()
f1.close()

os.chdir("repo")
section = ""
for files in glob.glob("*.html"):
    text = "<h3><a class='note' href='repo/%s' >%s</a></h3>\n" % (files, files[:files.find('.')])
    section = section + text
os.chdir("..")

nf = f.replace("$section$", section)

try:
    f2 = open("index.html", "w")
    f2.write(nf)
    f2.flush()
    f2.close()
except IOError as (e, stre):
    print e, stre

#print nf
