import sys
import os
import re

arr = []

for subdir, dirs, files in os.walk(os.getcwd()):
    for file in files:
        #print os.path.join(subdir, file)
        filepath = subdir + os.sep + file

       	if file.startswith( 'GPS' ):
        	print (filepath)
        	arr.append(filepath)




orig_stdout = sys.stdout
f = open('busstop.txt', 'w')
sys.stdout = f

fp = open("GPS_2015_05_16_10_43_20_924.txt",'r')
arr = []
old = []
for line in fp:
	line = line.strip()
	line = line.replace(' ',',')
	line = line.split(',')
	if line[-1].startswith( 'BusStop' ):
		for j in line:
			print j, 
			print " ",
		print 


sys.stdout = orig_stdout
f.close()