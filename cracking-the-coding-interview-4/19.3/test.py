"""
Print the number of trailing zeros in a factorial. I think the logic goes
like this:

* this is a factoring problem
* every time you have a multiple of 5   you already have a matching 2  -> 0
* every time you have a multiple of 5^n you already have n matching 2s -> 0xn
* implementation as a loop over powers seems fastest

"""

import re

def factorial(fbase):
	ff=1
	for ii in range (1,fbase+1):
		ff *= ii
	return ff

def trailing_zeroes_of_factorial(fbase):
	power=1
	zs=0
	while fbase >= 5**power:
		zs += fbase/(5**power)
		power+=1
	return zs

def trailing_zeroes_of_number(number):
	ns=str(number)
	sl=len(re.search(r'(0*)$',ns).group(0))
	return sl

# lr=range(0,101,10)+range(5,101,10)
lr=range(1001)
lr.sort()
ll=0
for ii in lr:
	fn=factorial(ii)
	fs=str(fn)
	# fz=re.search(r'(0*)$',fs).group(0)
	# fl=len(fz)
	fl = trailing_zeroes_of_number(fn)
	fq = trailing_zeroes_of_factorial(ii)
	if fl>ll:
		print "%3d, %3d, %3d, %3d" % (ii,fl,fl-ll,fq) #,fs
		ll=fl