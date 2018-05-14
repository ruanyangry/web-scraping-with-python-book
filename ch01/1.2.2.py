from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
html=urlopen("http://msce.njtech.edu.cn/chinese/index.html")
bsObj=bs(html.read())
print(bsObj.h1)
