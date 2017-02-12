"""
(a) Prove the following theorem by Nicomachus by induction: 1^3 = 1, 2^3 = 3+5, 3^3=7+9+11, ...
(b) Use that so prove sum(n^3)=sum(n)^2
"""

# This has nothing to do with the induction itself and merely creates 
# the numbers and verifies that the statement is right.
for ii in range(1,10):
	i2 = ii**2
	i3 = ii**3
	icomp = [i2+ii-1-x for x in range(0,2*ii,2)]
	isum = 0
	for jj in icomp:
		isum += jj
	print "%d: %4d = %4d %s" % (ii, i3, isum, icomp)