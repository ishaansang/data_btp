import os, re
from os import path
from math import radians, cos, sin, asin, sqrt
import math
import numpy as np
# from scipy.spatial.distance import euclidean
# from fastdtw import fastdtw
# from scipy.spatial.distance import euclidean
# from fastdtw import fastdtw

def getfile(str):
	"""This code formats the raw input file into suitable data."""             
	arr = []
	file_path = os.path.relpath(str)
	# print filepath
	var = True
	with open(file_path) as fp:
		for line in fp:
			line = line.strip()
			line = line.replace(' ',',')
			if var is False:
				arr.append(line.split(','))
			var = False

	return arr

def haversine(lon1, lat1, lon2, lat2):
    """Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)."""
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    # Radius of earth in kilometers is 6371
    km = 6371* c
    return km

def samepath(paths,ii,jj):
	"""Given the paths directory and two indices this code checks whether 
	the data belongs to the same path or not using gps coordinates."""
	i=0
	j=0
	ctr = 0
	arr = getfile(paths[ii])
	brr = getfile(paths[jj])
	print (ii,jj)
	while i < len(arr):
	    j = 0
	    id = -1
	    m = 1000000000
	    while(j < len(brr)):
	        if(haversine(float(arr[i][1]),float(arr[i][0]),float(brr[j][1]),float(brr[j][0])) < m):
	            m = haversine(float(arr[i][1]),float(arr[i][0]),float(brr[j][1]),float(brr[j][0]))
	            id = j
	        j += 1
	    i += 1
	    if(m < 0.005):
	        ctr += 1

	match = float(ctr)/len(brr)
	
	if match > 0.5:
		return 1

	return 0

def getdtw(paths,graphs):
	# print os.getcwd()
	i = 0
	dtw = []
	while i < len(paths):
		file_path = os.path.relpath(os.getcwd() + "/"+paths[i] +  
									"/Experiment_" + paths[i][-19:] + "/LACC.txt")
		# print paths[0][-19:]
		# print paths
		file_path = "/" + file_path
		arr = []
		with open(file_path) as fp:
			for line in fp:
				line = line.strip()
				line = line.replace(' ',',')
				line = line.split(',')
				line = map(float,line[0:2])
				arr.append(line)

		j = 0
		cur= []
		print (i)
		while j < len(graphs[i]):
			# print graphs[i][j]
			file_path = os.path.relpath(os.getcwd() + "/"+paths[graphs[i][j]] +  
										"/Experiment_" + paths[graphs[i][j]][-19:] + "/LACC.txt")
			file_path = "/" + file_path
			brr = []
			with open(file_path) as fp:
				for line in fp:
					line = line.strip()
					line = line.split(',')
					line = map(float,line[0:2])
					brr.append(line)	

			x = np.array(arr)
			y = np.array(brr)
			# print x,y
			# print (len(x) , len(y) ,type(x[0][0]))
			distance, path = fastdtw(x, y, dist=euclidean)
			# print(distance)
			cur.append(distance)
			j += 1
		dtw.append(cur)
		i+=1
	# print dtw

"""Start of the main"""
arr = []
""" Storing all the file directory."""
for subdir, dirs, files in os.walk(os.getcwd()):
    for file in files:
        #print os.path.join(subdir, file)
        filepath = subdir + os.sep + file
        if 'GPS' in filepath:
            # print (subdir[-19:-1])
            arr.append(filepath)

# print len(arr)

i = 0
j = 0
"""storing path directory of the files that have more than 100 gps coordinates in them."""
final_dir = []
while i < len(arr):
	file1 = getfile(arr[i])
	if len(file1) < 100:
		i = i + 1
		pass
	final_dir.append(arr[i])
	i = i + 1
	pass

print (len(final_dir))
i = 0
j = 0

# print arr
"""Checks for all pairs to see if they are the same paths or not
Can be optimised to linear time but FTW."""
f1=open('final_pathdir.txt', 'w+')
graph = []
while i < len(final_dir):
	j = i +1
	cur = []
	while j < len(final_dir):
		if samepath(final_dir,i,j):
			print (final_dir[i][-19:-1],final_dir[j][-19:-1],file = f1)
			cur.append(j)
		j = j + 1
	graph.append(cur)
	i = i + 1

f1.close()

print (graph)
# 			# getdtw(final_dir,graph)

