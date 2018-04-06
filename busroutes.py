import os
import sys
orig_stdout = sys.stdout
d = {}

fp = open("stopdata.txt","r")
for line in fp:
	line = ' '.join(line.split())
	line = line.strip()
	line = line.replace(' ',',')
	line = line.split(',')
	# print line 
	if (line[0],line[1]) not in d:
		d[(line[0],line[1])] = []
	

for subdir, dirs, files in os.walk(os.getcwd()):
    for file in files:
        filepath = subdir + os.sep + file
        if file.startswith( 'stoptiming' ):
        	# str = filepath[0:-14] + "busroute.txt"
        	b = {}
        	# b = d
        	# print str
        	fp2 = open(filepath,'r')
        	# f = open(str, 'w')
        	
        	for line in fp2:
        		line = ' '.join(line.split())
        		line = line.strip()
        		line = line.replace(' ',',')
        		line = line.split(',')
        		# print line
        		if (line[0],line[1]) not in b:
        			b[(line[3],line[4])] = []
        		# if (line[3],line[4]) in d:
        		b[(line[3],line[4])].append(line[2])
        		d[(line[3],line[4])].append(line[2])
    		


f = open('busroutes.txt','w')
sys.stdout = f
for key,value in sorted(d.iteritems()):
    	if len(value) is not 0:
    		print key,sorted(value)

sys.stdout = orig_stdout
f.close()
