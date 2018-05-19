# _*_ coding:utf-8 _*_

from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re

# time was the seed of the random generator. 
random.seed(datetime.datetime.now())

def getLinks(articleUrl):
	html=urlopen("http://en.wikipedia.org"+articleUrl)
	bsObj=BeautifulSoup(html)
	return bsObj.find("div",{"id":"bodyContent"}).findAll("a",\
	href=re.compile("^(/wiki/)((?!:).)*$"))
	
links=getLinks("/wiki/kevin_Bacon")
while len(links)>0:
	newArticle=links[random.randint(0,len(links)-1)].attrs["href"]
	print(newArticle)
	links=getLinks(newArticle)
