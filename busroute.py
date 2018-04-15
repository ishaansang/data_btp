import os,sys



graph = []
graph.append((0,1,6,7,12,13,14,15,16,18,19,20,21)) 
graph.append((2,3)) 
graph.append((4,))
graph.append((5,11, 22, 23))
graph.append((8,9))
graph.append((10,))
graph.append((17,))

files = []
files2 = []

# with open('filepaths.txt') as fp:
# 	for line in fp:
# 		files2.append(line)
# 		print line

for subdir, dirs, files in os.walk(os.getcwd()):
    for file in files:
        filepath = subdir + os.sep + file
        if file.startswith( 'stoptiming' ):
        	files2.append(filepath)
        	print filepath

print files2

id = 0
for rows in graph:
	d = {}
	orig_stdout = sys.stdout
	for idx in rows:
		with open(files2[idx]) as fp:
			for line in fp:
				line = ' '.join(line.split())
				line = line.strip()
				line = line.replace(' ',',')
				line = line.split(',')
				if (line[3],line[4]) not in d:
					d[(line[3],line[4])] = []
				d[(line[3],line[4])].append(line[2])

	f = open('stop_route'+str(id)+'.txt','w')
	for key,value in sorted(d.iteritems()):
		f.write( "%s %s %s \n" %(key[0], key[1], value) )

	f.close()
	id += 1

	# print "tyoyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy"
	# for key,value in sorted(d.iteritems()):
	#     	if len(value) is not 0:
	#     		print key,sorted(value)

	# sys.stdout = orig_stdout
	# f.close()
	

