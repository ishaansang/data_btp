import sys
import os
import re
import datetime

orig_stdout = sys.stdout
d = {}

def getTimediff(str,str1):
	start_dt = datetime.datetime.strptime(str, '%H:%M:%S')
	end_dt = datetime.datetime.strptime(str1, '%H:%M:%S')
	diff = (end_dt - start_dt)
	return diff

for subdir, dirs, files in os.walk(os.getcwd()):
    for file in files:
        filepath = subdir + os.sep + file
        if file.startswith( 'busstop' ):
            d.clear()
            str = (filepath[0:-11]) + "stoptiming.txt"
            print str,filepath
            f = open(str, 'w')
            sys.stdout = f

            fp = open(filepath,'r')
            for line in fp:
                line = ' '.join(line.split())
                line = line.strip()
                line = line.replace(' ',',')
                line = line.split(',')
                # print line
                if line[-1] not in d:
                    d[line[-1]] = []
                d[line[-1]].append((line[-2],line[0],line[1]))
            for key,value in sorted(d.iteritems()):
            	print key,value[-1][0],value[0][0],value[0][1],value[0][2],getTimediff(value[0][0],value[-1][0])
            sys.stdout = orig_stdout
            f.close()