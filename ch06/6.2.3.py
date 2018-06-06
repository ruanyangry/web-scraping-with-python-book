from urllib.request import urlopen
from io import StringIO
import csv

data=urlopen("http://pythonscraping.com/files/MontyPythonAlbums.csv").read().\
decode('ascii','ignore')

dataFile=StringIO(data)
#csvReader=csv.reader(dataFile)
dictReader=csv.DictReader(dataFile)
print(dictReader.fieldnames)

#i=0
#for row in csvReader:
#	i +=1
#	if i< 20:
#		print(row)
#		#print("The ablum \""+row[0]+"\ was released in"+str(row[1])) 

print("\n")

i=0
for row in dictReader:
	i += 1
	if i < 20:
		print(row)
