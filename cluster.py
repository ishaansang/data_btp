import os
from Queue import PriorityQueue
from sets import Set
from sklearn.cluster import KMeans
import numpy as np

def group(val,s1,s2,arr):
	sum1 = 100000.0
	sum2 = 100000.0

	print val
	for x in s1:
		# print x
		sum1 = min(arr[val][x],sum1)

	for y in s2:
		sum2 = min(arr[val][y],sum2)
		# print y

	print sum1,sum2
	return sum1 > sum2
		


arr = []
fp = open("dtw_data0.txt","r")
for line in fp:
	line = ' '.join(line.split())
	line = line.strip()
	line = line.replace(' ',',')
	line = line.split(',')
	line = map(float,line)
	arr.append(line)


q = PriorityQueue()

for i in range(len(arr)):
	for j in range(len(arr[0])):
		q.put((-1*arr[i][j],i,j))

s1 = set()
s2 = set()
s = set()
item = q.get()

s1.add(item[1])
s2.add(item[2])

s.add(item[1])
s.add(item[2])

while not q.empty():
	item = q.get()
	if item[1] in s and item[2] not in s:
		temp = group(item[2],s1,s2,arr)
		print temp
		s.add(item[2])
		if temp is False:
			s1.add(item[2])
		else :
			s2.add(item[2])


	if item[2] in s and item[1] not in s:
		temp = group(item[1],s1,s2,arr)
		print temp
		s.add(item[1])
		if temp is False:
			s1.add(item[1])		
		else :
			s2.add(item[1])		



X = np.array(arr)
kmeans = KMeans(n_clusters=2, random_state=None).fit(X)
print kmeans.labels_	

print 'here'
