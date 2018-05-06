import os 
import sys

stops = []
gpsdata = []

TimeConstant = 30
orig_stdout = sys.stdout

def diff(time1,time2):
	A = int(time1[-2:]) + 60*int(time1[-5:-3]) + 3600*int(time1[0:-6])
	B = int(time2[-2:]) + 60*int(time2[-5:-3]) + 3600*int(time2[0:-6])

	return A - B 

'''returns the start and end times array for all the bus stops'''
def gettime(stops):
	start = []
	end = []
	fp = open(stops,'r')
	for line in fp:
		line = ' '.join(line.split())
		line = line.strip()
		line = line.replace(' ',',')
		line = line.split(',')
		start.append(line[2])
		end.append(line[1])

	return start,end

def check(start,end,time):
	for st,en in zip(start,end):
		if diff(st,time) <= 0 and diff(time,en) >= 0:
			return False

	for val in start:
		if diff(val,time) < TimeConstant and diff(val,time) > 0:
			# print time
			return True

	for val in end:
		if diff(time,val) < TimeConstant and diff(time,val) > 0:
			# print time
			return True

	return False



###################################################


for subdir, dirs, files in os.walk(os.getcwd()):
    for file in files:
        filepath = subdir + os.sep + file
        if file.startswith( 'stoptiming' ):
        	# print filepath
        	stops.append(filepath)
        if file.startswith( 'LACC' ):
        	gpsdata.append(filepath)
        	# print filepath



for a,b in zip(stops,gpsdata):
	start,end = gettime(a)
	print start,end

	fp = open(b,'r')
	f = open(b[0:-32] + 'NNLaccNearStops.txt',"w")
	sys.stdout = f
	next(fp)
	for line in fp:
		temp = line
		line = ' '.join(line.split())
		line = line.strip()
		line = line.replace(' ',',')
		line = line.split(',')
		if 'BusStop' in line[5]:
			continue
		var = check(start,end,line[4])

		if var is True:
			print temp,

	sys.stdout = orig_stdout
	f.close()
		