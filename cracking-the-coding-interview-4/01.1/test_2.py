import sys

string="asdaf"

sl=len(string)
for ii in range(sl):
	for jj in range(ii+1,sl):
		if string[ii] == string[jj]:
			print "Duplicates present"
			sys.exit()

print "No Duplicates present"
sys.exit()