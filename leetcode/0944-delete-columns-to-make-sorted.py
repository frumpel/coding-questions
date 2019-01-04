class Solution(object):
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        ww=len(A[0])
        hh=len(A)
        di=[]
        for xx in range(ww):
            for yy in range(1,hh):
                if A[yy][xx]<A[yy-1][xx]:
                    di.append(xx)
                    break
        return len(di)



x=Solution()

q = ["cba","daf","ghi"]
e = 1
print "Question",q
print "Expect",e
a = x.minDeletionSize(q)
print "Result",a
print e==a


q = ["a","b"]
e = 0
print "Question",q
print "Expect",e
a = x.minDeletionSize(q)
print "Result",a
print e==a


q = ["zyx","wvu","tsr"]
e = 3
print "Question",q
print "Expect",e
a = x.minDeletionSize(q)
print "Result",a
print e==a
