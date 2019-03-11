class Solution(object):
    def largestSumAfterKNegations(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        ss=K
        nn=0
        A.sort()
        # print A
        for ii in range(K):
            if A[ii]<0:
                A[ii]=-A[ii]
            else:
                nn=K-ii
                if ii>0 and abs(A[ii-1])<abs(A[ii]):
                    ss=ii-1
                else:
                    ss=ii
                break
        # print A,ss
        for jj in range(nn):
            A[ss]=-A[ss]
        # print A
        return sum(A)

x=Solution()

q1 = [4,2,3]
q2 = 1
e = 5
print "Question",q1,q2
print "Expect",e
a = x.largestSumAfterKNegations(q1,q2)
print "Result",a
print e==a

q1 = [3,-1,0,2]
q2 = 3
e = 6
print "Question",q1,q2
print "Expect",e
a = x.largestSumAfterKNegations(q1,q2)
print "Result",a
print e==a

q1 = [2,-3,-1,5,-4]
q2 = 2
e = 13
print "Question",q1,q2
print "Expect",e
a = x.largestSumAfterKNegations(q1,q2)
print "Result",a
print e==a

q1 = [-8,3,-5,-3,-5,-2]
q2 = 6
e = 22
print "Question",q1,q2
print "Expect",e
a = x.largestSumAfterKNegations(q1,q2)
print "Result",a
print e==a
