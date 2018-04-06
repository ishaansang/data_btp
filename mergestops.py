import os
import sys
from math import radians, cos, sin, asin, sqrt



def dist2(p1, p2):
    return (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2

def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
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


def fuse(points, d):
    ret = []
    d2 = d * d
    n = len(points)
    taken = [False] * n
    for i in range(n):
        if not taken[i]:
            count = 1
            time = 0
            point = [points[i][0], points[i][1],points[i][2]]
            taken[i] = True
            for j in range(i+1, n):
                if haversine(points[i][1],points[i][0], points[j][1],points[j][0]) < d2:
                    point[0] += points[j][0]
                    point[1] += points[j][1]
                    point[2] += points[j][2]
                    count+=1
                    taken[j] = True
            point[0] /= count
            point[1] /= count
            ret.append((point[0], point[1],point[2]))
    return ret


fp = open("stopdata.txt","r")
arr = []
for line in fp:
	line = ' '.join(line.split())
	line = line.strip()
	line = line.replace(' ',',')
	line = line.split(',')
	# print line
	arr.append( (float(line[0]),(float(line[1])),(int(line[2])  )))

print len(arr)
arr = fuse(arr,0.020)
print len(arr)