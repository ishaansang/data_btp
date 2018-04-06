import os
import re

for subdir, dirs, files in os.walk(os.getcwd()):
    for file in files:
        #print os.path.join(subdir, file)
        filepath = subdir + os.sep + file

       	if file.startswith( 'GPS' ):
        	print (filepath)