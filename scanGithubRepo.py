from BeautifulSoup import BeautifulSoup
import time
import urllib2

types = ['article', 'books', 'slice']
for reading_type in types:
  try :
		type_url = "https://github.com/watermelonlh/ReadingNotes/tree/gh-pages/repo/" + reading_type
		print type_url
		response = urllib2.urlopen(type_url)
		page = response.read()
		soup = BeautifulSoup(page)

		trs = soup.tbody.findAll(attrs = { 'class' : "content" })
		files = [tr.a['href'].split('/')[-1] for tr in trs]
		print files
		for file in files:
			url = "http://watermelonlh.github.io/ReadingNotes/repo/" + reading_type + "/" + file
			print url
			response = urllib2.urlopen(url)
			doc = response.read()
			soup = BeautifulSoup(doc)

			title, = soup.body.h2.contents
			author = ""
			if (soup.body.h5 != None):
				author, = soup.body.h5.contents
			divs = soup.body.div.findAll('div')
			divs_len = len(divs)
			print "title: %s" % str(title)
			print "author: %s" % str(author)
			
			i = 0
			while i + 3 < divs_len:
				note_date = time.strptime(divs[i + 1].contents[0], "%Y-%m-%d %H:%M:%S")
				note_contents = divs[i + 2].contents[0]
				print "'%s'" % str(note_contents)
				i += 3
	except:
		None
