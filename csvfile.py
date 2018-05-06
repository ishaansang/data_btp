import os 
import csv

myData = []
with open('stop_route0.txt') as fp:
	for line in fp:
		line = ' '.join(line.split())
		line = line.strip()
		line = line.replace(' ',',')
		line = line.split(',')
		print line
		myData.append((float(line[0]),float(line[1])))

# sort(myData)
# myData = sorted(myData, key=lambda x: x[2], reverse=True)
xx = []

# for i in range(25):
	# xx.append((myData[i][0],myData[i][1],myData[i][2]))


myFile = open('example2.csv', 'w')
with myFile:
    writer = csv.writer(myFile)
    writer.writerows(myData)