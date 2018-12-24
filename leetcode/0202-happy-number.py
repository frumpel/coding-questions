class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen=set()
        # while True:
        while True:
            seen.add(n)
            o=0
            for ii in str(n):
                o+=int(ii)**2
            print n,o
            if o == 1:
                return True
            if o in seen:
                return False
            n=o

x=Solution()

q = 19
e = True
print "Question",q
print "Expect",e
a = x.isHappy(q)
print "Result",a
print e==a

q = 2
e = False
print "Question",q
print "Expect",e
a = x.isHappy(q)
print "Result",a
print e==a
