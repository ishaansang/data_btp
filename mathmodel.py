from __future__ import print_function
import os 
import sys
from sklearn import svm
from numpy import median
from numpy import std
from scipy.stats import kurtosis
# from statistics import mode
stops = []


def myfunc(arr):
	# return reduce(lambda x, y: x + y, arr) / len(arr)  #mean
	# return max(set(arr), key=arr.count)       #mode
	# return median(arr)                          ##median 
	# return std(arr,axis = 0) #deviation
	return kurtosis(arr)


for subdir, dirs, files in os.walk(os.getcwd()):
    for file in files:
        filepath = subdir + os.sep + file
        if file.startswith( 'LaccNearStops' ):
        	stops.append(filepath)



graph = []
graph.append((1,6,7,12,13,14,15,16,18,19,20,21)) 
        	# 1,1,1,1, 1,  1, 0, 0, 1, 1, 1, 1
d = {}

for idx in graph[0]:
	fp = open(stops[idx],'r')
	for line in fp:
		line = ' '.join(line.split())
		line = line.strip()
		line = line.replace(' ',',')
		line = line.split(',')
		
		fac = 1

		if idx == 15 or idx == 16:
			fac = 0
		if (line[4] + stops[idx]) not in d:
			d[line[4] + stops[idx]] = []
		d[line[4] + stops[idx]].append((line[0],line[1],line[2],fac))



X = []
Y = []
for key,value in sorted(d.iteritems()):
	if len(value) == 5:
		addtemp = []
		temp = []
		for val in value:
			temp.append(float(val[0]))
		addtemp.append(myfunc(temp))
		
		temp = []
		for val in value:
			temp.append(float(val[1]))
		addtemp.append(myfunc(temp))
		
		temp = []
		for val in value:
			temp.append(float(val[2]))
		addtemp.append(myfunc(temp))
		
		print (addtemp,val[3])
		X.append(addtemp)
		Y.append(float(val[3]))


clf = svm.SVC()
clf.fit(X, Y)  

num = 0
den = 0

orig_stdout = sys.stdout

f = open('debugdata3.txt','w')
sys.stdout = f
# for key,value in sorted(d.iteritems()):
#     	if len(value) is not 0:
#     		print key,sorted(value)



for key,value in sorted(d.iteritems()):
	if len(value) == 5:
		tempx = []
		tempy = []
		tempz = []
		for val in value:
			tempx.append(float(val[0]))
			tempy.append(float(val[1]))
			tempz.append(float(val[2]))

		res = []
		res.append(myfunc(tempx))
		res.append(myfunc(tempy))
		res.append(myfunc(tempz))
		print (clf.predict([res]))
		if clf.predict([res]) == float(val[3]):
			print (res,"yes")
			num+=1
		else:
			print (res,"no")
		# print:
		# 	gelse "no"
		den+=1




sys.stdout = orig_stdout
f.close()


print (float(num)/float(den))



