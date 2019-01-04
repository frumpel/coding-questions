class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A)<3:
            return False
        up=A[1]>A[0]
        if not up:
            return False
        last=A[0]
        for ii in range(1,len(A)):
            if up:
                if A[ii]<last:
                    up=False
                elif A[ii]==last:
                    return False
            else:
                if A[ii]>=last:
                    return False
            last=A[ii]
        return  up==False



x=Solution()

q = [2,1]
e = False
print "Question",q
print "Expect",e
a = x.validMountainArray(q)
print "Result",a
print e==a

q = [1,2,1]
e = True
print "Question",q
print "Expect",e
a = x.validMountainArray(q)
print "Result",a
print e==a

q = [3,5,5]
e = False
print "Question",q
print "Expect",e
a = x.validMountainArray(q)
print "Result",a
print e==a

q = [0,1,2,3,4,5,6,7,8,9]
e = False
print "Question",q
print "Expect",e
a = x.validMountainArray(q)
print "Result",a
print e==a
