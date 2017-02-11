import random

def xor_swap(a,b):
	b^=a
	a^=b
	b^=a
	return (a,b)

sa=random.randrange(0,255)
sb=random.randrange(0,255)
(ra,rb) = xor_swap(sa,sb)
print "Original: %10s - %10s" % (bin(sa),bin(sb))
print "Swapped:  %10s - %10s" % (bin(ra),bin(rb))