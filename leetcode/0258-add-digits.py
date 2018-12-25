class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        n=num
        s=0
        while n:
            s+=n%10
            n//=10
        if s > 9:
            return self.addDigits(s)
        return s


x=Solution()

q = 38
e = 2
print "Question",q
print "Expect",e
a = x.addDigits(q)
print "Result",a
print e==a

for ii in range(120):
    print ii,x.addDigits(ii)
