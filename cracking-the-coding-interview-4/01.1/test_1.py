import sys
from collections import defaultdict

string="asdf";

a=defaultdict(int)

for ii in string:
	a[ii]+=1

for vv in a.itervalues():
	if vv > 1:
		print "Duplicates present"
		sys.exit()

print "No Duplicates"
sys.exit()

