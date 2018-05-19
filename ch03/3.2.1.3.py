# _*_ coding: utf-8 _*_

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random

pages=set()
random.seed(datetime.datetime.now())

# get page internal links list
def getInternalLinks(bsObj,includeUrl):
	internalLinks=[]
	for link in bsObj.findAll("a",href=re.compile("^(/|.*"+includeUrl+")")):
		if link.attrs['href'] is not None:
			if link.attrs['href'] not in internalLinks:
				internalLinks.append(link.attrs['href'])
	return internalLinks
	
# get page external links list

def getExternalLinks(bsObj,excludeUrl):
	externalLinks=[]
	for link in bsObj.findAll("a",href=re.compile("^(http|www)((?!"+excludeUrl+").)*$")):
		if link.attrs['href'] is not None:
			if link.attrs['href'] not in externalLinks:
				externalLinks.append(link.attrs['href'])
	return externalLinks
	
def splitAddress(address):
	addressParts=address.replace("http://","").split("/")
	return addressParts
	
def getRandomExternalLink(startingPage):
	html=urlopen(startingPage)
	bsObj=BeautifulSoup(html)
	externalLinks=getExternalLinks(bsObj,splitAddress(startingPage)[0])
	if len(externalLinks)==0:
		internalLinks=getInternalLinks(startingPage)
		return getNextExternalLink(internalLinks[random.randint(0,len(internalLinks)-1)])
	else:
		return externalLinks[random.randint(0,len(externalLinks)-1)]
		
def followExternalOnly(startingSite):
	externalLink=getRandomExternalLink("http://oreilly.com")
	print("The random link:"+externalLink)
	followExternalOnly(externalLink)
	
# Add new function

allExtLinks=set()
allIntLinks=set()

def getAllExternalLinks(siteUrl):
	html=urlopen(siteUrl)
	bsObj=BeautifulSoup(html)
	internalLinks=getInternalLinks(bsObj,splitAddress(siteUrl)[0])
	externalLinks=getExternalLinks(bsObj,splitAddress(siteUrl)[0])
	for link in externalLinks:
		if link not in allExtLinks:
			allExtLinks.add(link)
			print(link)
	for link in internalLinks:
		if link not in allIntLinks:
			print('Coming url:'+link)
			allIntLinks.add(link)
			getAllExternalLinks(link)
	
#followExternalOnly("http://oreilly.com")
getAllExternalLinks("http://oreilly.com")

