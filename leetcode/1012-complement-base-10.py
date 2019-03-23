class Solution(object):
    def bitwiseComplement(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N==0:
            return 1
        r=0
        p=0
        while N > 0:
            r+=((~N)&1)<<p
            p+=1
            N>>=1
        return r




x=Solution()

q = 5
e = 2
print "Question",q
print "Expect",e
a = x.bitwiseComplement(q)
print "Result",a
print e==a

q = 7
e = 0
print "Question",q
print "Expect",e
a = x.bitwiseComplement(q)
print "Result",a
print e==a

q = 10
e = 5
print "Question",q
print "Expect",e
a = x.bitwiseComplement(q)
print "Result",a
print e==a

q = 0
e = 1
print "Question",q
print "Expect",e
a = x.bitwiseComplement(q)
print "Result",a
print e==a
