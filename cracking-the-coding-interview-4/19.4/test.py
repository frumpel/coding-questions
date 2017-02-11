"""
This question is ugly because it's somewhat language dependent - you'd solve
this different in primitive languages like C than in languages with generic
data types like Python.

Additionally I think all python solutions fundamentally cheat because the only
way to get the sign or abs(x) implies a comparison
"""

import random

def sign_plus_minus_zero(x):
	""" 
	Taken from here: 
	
	https://finnaarupnielsen.wordpress.com/2011/05/18/where-is-the-sign-function-in-python/
	
	I like that this persists non-numbers as-is
	"""
	if x > 0:
		return 1.
	elif x < 0:
		return -1.
	elif x == 0:
		return 0.
	else:
		return x

def sign_bit_zero_one(x):
	"""
	In C/Java this would be (((int)x)>>31)&0x1
	"""
	if sign_plus_minus_zero(x) < 0:
		return 1
	else:
		return 0

def max_pythonic_abs(a,b):
	return ((a+b)/2.0 + abs((a-b))/2.0)

def max_pythonic_sign(a,b):
	return (a+b)/2.0 + sign_plus_minus_zero(a-b)*(a-b)/2.0

def max_java_sign(a,b):
	return a - sign_bit_zero_one(a-b)*(a-b)

for ii in range(10):
	a=random.randrange(-100,100)
	b=random.randrange(-100,100)
	print "max(%3d, %3d) => %3d / %3d / %3d" % (
		a,b,
		max_pythonic_abs(a,b),
		max_pythonic_sign(a,b),
		max_java_sign(a,b))

	
