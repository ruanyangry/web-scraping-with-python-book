from urllib.request import urlopen
html=urlopen("http://msce.njtech.edu.cn/chinese/index.html")
print(html.read())

