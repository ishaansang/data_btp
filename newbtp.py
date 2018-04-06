import sys
import os
import re

brr = []

for subdir, dirs, files in os.walk(os.getcwd()):
    for file in files:
        #print os.path.join(subdir, file)
        filepath = subdir + os.sep + file

       	if file.startswith( 'GPS' ):
        	print (filepath)
        	brr.append(filepath)


for location in brr:
	str = location
	orig_stdout = sys.stdout
	path = str
	id = path.rfind('GPS')
	path = path[0:id] + "busstop.txt"
	print path

	f = open(path, 'w')
	sys.stdout = f

	fp = open(str,'r')
	arr = []
	old = []
	for line in fp:
		line = line.strip()
		line = line.replace(' ',',')
		line = line.split(',')
		if line[-1].startswith( 'BusStop' ):
			for j in line:
				print j, 
				print "",
			print 


	sys.stdout = orig_stdout
	f.close()