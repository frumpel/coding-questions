class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        while num//2.0 == num/2.0:
            num//=2.0
        while num//3.0 == num/3.0:
            num//=3.0
        while num//5.0 == num/5.0:
            num//=5.0
        if num==1:
            return True
        return False

x=Solution()

q = 0
e = False
print "Question",q
print "Expect",e
a = x.isUgly(q)
print "Result",a
print e==a

q = 1
e = True
print "Question",q
print "Expect",e
a = x.isUgly(q)
print "Result",a
print e==a

q = 2
e = True
print "Question",q
print "Expect",e
a = x.isUgly(q)
print "Result",a
print e==a

q = 3
e = True
print "Question",q
print "Expect",e
a = x.isUgly(q)
print "Result",a
print e==a

q = 4
e = True
print "Question",q
print "Expect",e
a = x.isUgly(q)
print "Result",a
print e==a

q = 5
e = True
print "Question",q
print "Expect",e
a = x.isUgly(q)
print "Result",a
print e==a

q = 6
e = True
print "Question",q
print "Expect",e
a = x.isUgly(q)
print "Result",a
print e==a

q = 7
e = False
print "Question",q
print "Expect",e
a = x.isUgly(q)
print "Result",a
print e==a

q = 15
e = True
print "Question",q
print "Expect",e
a = x.isUgly(q)
print "Result",a
print e==a

q = 60
e = True
print "Question",q
print "Expect",e
a = x.isUgly(q)
print "Result",a
print e==a

q = 61
e = False
print "Question",q
print "Expect",e
a = x.isUgly(q)
print "Result",a
print e==a
