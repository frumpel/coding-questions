class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 3/2 = 1.5
        # 5/2 = 2.5
        nums=[]
        nmax=int(2.7*(n**(1.0/3)))
        for ii in range(nmax):
            for jj in range(nmax):
                for kk in range(nmax):
                    nums.append((2**ii)*(3**jj)*(5**kk))
        nums.sort()
        return nums[n-1]




x=Solution()

q = 10
e = 12
print "Question",q
print "Expect",e
a = x.nthUglyNumber(q)
print "Result",a
print e==a

q = 110
e = 2048
print "Question",q
print "Expect",e
a = x.nthUglyNumber(q)
print "Result",a
print e==a

q = 1690
e = 2123366400
print "Question",q
print "Expect",e
a = x.nthUglyNumber(q)
print "Result",a
print e==a
