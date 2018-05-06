from __future__ import print_function
import os 
import sys
from sklearn import svm
from numpy import median
from numpy import std
from scipy.stats import kurtosis
import random
# from statistics import mode
stops = []
from sklearn import linear_model
import matplotlib.pyplot as plt
# print(__doc__)

import numpy as np
import matplotlib.pyplot as plt
# from sklearn import svm


def myfunc(arr):
	# return reduce(lambda x, y: x + y, arr) / len(arr)  #mean
	return min(set(arr), key=arr.count)       #mode
	# return median(arr)                          ##median 
	# return std(arr,axis = 0) #deviation
	# return kurtosis(arr)

def getOffset(v1,v2,v3,id):
	# m = min(v1,v2,v3)
	# M = max(v1,v2,v3)
	# avg = v1+v2+v3-m-M

	# if m == M:
	# 	return 0
	# ans = float(avg-m)/float(M-m)

	fac = random.randint(0,1)

	ans = 0.1

	if fac == 0:
		fac -=1 

	return fac*ans



for subdir, dirs, files in os.walk(os.getcwd()):
    for file in files:
        filepath = subdir + os.sep + file
        if file.startswith( 'NNLacc' ):
        	stops.append(filepath)


# print (stops)

graph = []
graph.append((1,6,7,12,13,14,15,16,18,19,20,21)) 
        	# 1,1,1,1, 1,  1, 0, 0, 1, 1, 1, 1
d = {}

for idx in graph[0]:
	fp = open(stops[idx],'r')
	# next(fp)
	for line in fp:
		line = ' '.join(line.split())
		line = line.strip()
		line = line.replace(' ',',')
		line = line.split(',')
		if line[-1].startswith('BusStop'):
			continue

		# print (line)
		fac = 1

		if idx == 15 or idx == 16:
			fac = 0
		

		if (line[4] + stops[idx]) not in d:
			d[line[4] + stops[idx]] = []
		d[line[4] + stops[idx]].append((line[0],line[1],line[2],fac))

		# if idx == 15 or idx == 16:

		# 	for i in range(1,2):
		# 		v1 = getOffset(float(line[0]),float(line[1]),float(line[2]),0)*float(line[0])
		# 		v2 = getOffset(float(line[0]),float(line[1]),float(line[2]),0)*float(line[1])
		# 		v3 = getOffset(float(line[0]),float(line[1]),float(line[2]),0)*float(line[2])
		# 		print (line[0], v1 , line[1], v2 ,line[2], v3 )
		# 		d[line[4] + stops[idx]].append((v1+float(line[0]),v2+float(line[1]),v3+float(line[2]),fac))



X = []
Y = []
c1 = 0
c2 = 0
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
		
		# print (addtemp,val[3])
		X.append(addtemp)
		Y.append(float(val[3]))
		if float(val[3]) == 0:
			c1+=1
		else :
			c2+=1

print (c1,c2)

# fac = 4
# idd = 0
# xx = {}
# for val in X:
# 	if round(val[idd],fac) not in xx:
# 		xx[round(val[idd],fac)] = 0
# 	xx[round(val[idd],fac)] += 1

# aa = []
# bb = []


# for key,value in sorted(xx.iteritems()):
# 	aa.append(key)
# 	bb.append(value)

# # print (bb)

# f, ax = plt.subplots()
# ax.plot(aa,bb)
# ax.set_title('Window Min LaccX')

# # plt.plot(aa,bb)
# # plt.set_title('Window Mean')
# plt.show()

clf = svm.SVC()
 
clf = svm.SVC()
clf = linear_model.SGDClassifier(class_weight='balanced')
clf.fit(X, Y) 

wclf = svm.SVC(class_weight = 'balanced')
wclf.fit(X, Y)


# # # num = 0
# # # den = 0

print ( clf.score(X,Y) )
print ( wclf.score(X,Y) )

# orig_stdout = sys.stdout

# f = open('debugdata3.txt','w')
# sys.stdout = f
# # for key,value in sorted(d.iteritems()):
# #     	if len(value) is not 0:
# #     		print key,sorted(value)

# count = 0

# for key,value in sorted(d.iteritems()):
# 	if len(value) == 5:
# 		tempx = []
# 		tempy = []
# 		tempz = []
# 		for val in value:
# 			tempx.append(float(val[0]))
# 			tempy.append(float(val[1]))
# 			tempz.append(float(val[2]))

# 		res = []
# 		res.append(myfunc(tempx))
# 		res.append(myfunc(tempy))
# 		res.append(myfunc(tempz))
# 		print (clf.predict([res]))
# 		if clf.predict([res]) == float(val[3]):
# 			print (res,"yes")
# 			num+=1
# 		else:
# 			print (res,"no")

# 		if clf.predict([res]) == 1:
# 			count+=1
# 		# print:
# 		# 	gelse "no"
# 		den+=1




# sys.stdout = orig_stdout
# f.close()


# print (float(num)/float(den))



