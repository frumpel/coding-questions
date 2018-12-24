class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        m=n
        c=0
        while not m&1:
            m>>=1
            c+=1
        return n == 2**c

x=Solution()

q = 3
e = False
print "Question",q
print "Expect",e
a = x.isPowerOfTwo(q)
print "Result",a
print e==a

q = 2
e = True
print "Question",q
print "Expect",e
a = x.isPowerOfTwo(q)
print "Result",a
print e==a

q = 16
e = True
print "Question",q
print "Expect",e
a = x.isPowerOfTwo(q)
print "Result",a
print e==a

q = 218
e = False
print "Question",q
print "Expect",e
a = x.isPowerOfTwo(q)
print "Result",a
print e==a
