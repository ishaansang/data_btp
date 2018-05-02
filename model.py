import os 
import sys
from sklearn import svm

stops = []

for subdir, dirs, files in os.walk(os.getcwd()):
    for file in files:
        filepath = subdir + os.sep + file
        if file.startswith( 'LaccNearStops' ):
        	# print filepath
        	stops.append(filepath)



graph = []
graph.append((1,6,7,12,13,14,15,16,18,19,20,21)) 
        	# 1,1,1,1, 1,  1, 0, 0, 1, 1, 1, 1
d = {}

for idx in graph[0]:
	# print stops[idx]
	fp = open(stops[idx],'r')
	for line in fp:
		line = ' '.join(line.split())
		line = line.strip()
		line = line.replace(' ',',')
		line = line.split(',')
		# print line
		
		fac = 1

		if idx == 15 or idx == 16:
			fac = 0
		if (line[4] + stops[idx]) not in d:
			d[line[4] + stops[idx]] = []
			# print line[4] + stops[idx]
		d[line[4] + stops[idx]].append((line[0],line[1],line[2],fac))



X = []
Y = []
for key,value in sorted(d.iteritems()):
	# print len(value)
	if len(value) == 5:
		temp = []
		for val in value:
			# print val[0:3]
			# print val[0],val[1],val[2],val[3]
			temp.append(float(val[0]))
			temp.append(float(val[1]))
			temp.append(float(val[2]))
		X.append(temp)
		Y.append(float(val[3]))


clf = svm.SVC()
clf.fit(X, Y)  

num = 0
den = 0



for key,value in sorted(d.iteritems()):
	if len(value) == 5:
		temp = [[]]
		for val in value:
			temp[0].append(float(val[0]))
			temp[0].append(float(val[1]))
			temp[0].append(float(val[2]))
		if clf.predict(temp) == float(val[3]):
			# print "yes"
			num+=1
		# print:
		# 	gelse "no"
		den+=1


print float(num)/float(den)



