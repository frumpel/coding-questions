class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A)<2:
            return True
        for ii in range(len(A)-1):
            if A[ii]>A[ii+1]:
                for jj in range(ii+1,len(A)-1):
                    if A[jj]<A[jj+1]:
                        return False
                return True
            elif A[ii]<A[ii+1]:
                for jj in range(ii+1,len(A)-1):
                    if A[jj]>A[jj+1]:
                        return False
                return True
        return True

x=Solution()

q = [1,2,2,3]
e = True
print "Question",q
print "Expect",e
a = x.isMonotonic(q)
print "Result",a
print e==a

q = [1,1,1]
e = True
print "Question",q
print "Expect",e
a = x.isMonotonic(q)
print "Result",a
print e==a

q = [1,4,2]
e = False
print "Question",q
print "Expect",e
a = x.isMonotonic(q)
print "Result",a
print e==a

q = [1,4,1]
e = False
print "Question",q
print "Expect",e
a = x.isMonotonic(q)
print "Result",a
print e==a

q = [1,4,0]
e = False
print "Question",q
print "Expect",e
a = x.isMonotonic(q)
print "Result",a
print e==a

q = [1,4,-1]
e = False
print "Question",q
print "Expect",e
a = x.isMonotonic(q)
print "Result",a
print e==a

q = [0,1,0]
e = False
print "Question",q
print "Expect",e
a = x.isMonotonic(q)
print "Result",a
print e==a
