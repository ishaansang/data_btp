import os
import sys
d= {}

def convert(s):
	return int(s[-2:]) + 60*int(s[-5:-3]) + 3600*int(s[0:-6])

for subdir, dirs, files in os.walk(os.getcwd()):
    for file in files:
        filepath = subdir + os.sep + file
        if file.startswith( 'stoptiming' ):
            # print filepath
            fp = open(filepath,'r')
            for line in fp:
                line = ' '.join(line.split())
                line = line.strip()
                line = line.replace(' ',',')
                line = line.split(',')
                # print line
                if (line[-3],line[-2]) not in d:
                    d[(line[-3],line[-2])] = 0
                d[(line[-3],line[-2])] = int(convert(line[-1])) + d[(line[-3],line[-2])]

f = open("stopdata.txt","w+")
for key,value in sorted(d.iteritems()):
	f.write( "%s %s %s \n" %(key[0], key[1], value) )

f.close()

