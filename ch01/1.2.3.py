from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def getTitle(url):
	try:
		html=urlopen(url)
	except HTTPError as e:
		return none
	try:
		bsObj=BeautifulSoup(html.read())
		title=bsObj.body.h1
	except AttributeError as e:
		return none
	return title
	
title=getTitle("http://bbs.keinsci.com/thread-9969-1-1.html")
if title == None:
	print("Title could not be found")
else:
	print(title)
