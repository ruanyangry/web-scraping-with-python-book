import smtplib
from email.mime.text import MIMEText
from bs4 import BeautifulSoup
from urllib.request import urlopen
import time

def sendMail(subject,body):
	msg=MIMEText(body)
	msg['Subject']=subject
	msg['From']='1532014681@qq.com'
	msg['to']='ruanyang_njut@163.com'
	
s=smtplib.SMTP('localhost')
s.send_message(msg)
s.quit()

bsObj=BeautifulSoup(urlopen("https://isitchristmas.com/"))
while (bsObj.find("a",{"id":"answer"}).attrs['title']=="No"):
	print("It is not Christmas yet.")
	time.sleep(3600)
bsObj=BeautifulSoup(urlopen("https://isitchristmas.com/"))
sendMail("It's Christmas!","According to http://itischristmas.com, it is Christmas!")

