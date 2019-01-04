class Solution(object):
    def largestTimeFromDigits(self, A):
        """
        :type A: List[int]
        :rtype: str
        """
        A.sort()
        for ii in range(1439,-1,-1):
            a=ii//600
            b=(ii-a*600)//60
            c=(ii-a*600-b*60)//10
            d=(ii-a*600-b*60-c*10)
            B=[a,b,c,d]
            if sorted(B)==A:
                return str(a)+str(b)+":"+str(c)+str(d)

x=Solution()

q = [1,2,3,4]
e = "23:41"
print "Question",q
print "Expect",e
a = x.largestTimeFromDigits(q)
print "Result",a
print e==a
