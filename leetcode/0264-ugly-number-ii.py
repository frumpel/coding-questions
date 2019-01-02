class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 3/2 = 1.5 log(3)/log(2) = 1.58
        # 5/2 = 2.5 log(5)/log(2) = 2.32
        nums=[]
        nmax=int((n/3.75)**(1/3.0))+6
        imax=int(nmax*2.5)
        jmax=int(nmax*1.7)
        kmax=int(nmax*1.0)
        print nmax
        for ii in range(imax):
            for jj in range(jmax):
                for kk in range(kmax):
                    nums.append((2**ii)*(3**jj)*(5**kk))
        nums.sort()
        print nmax,3.75*(nmax**3),len(nums)
        print imax,jmax,kmax,imax*jmax*kmax
        return nums[n-1]

# n=1690
# x=(n/3.75)**(1/3.0)
# print x,n,x*(x*1.5)*(x*2.5)
# exit(0)

x=Solution()

q = 10
e = 12
print "Question",q
print "Expect",e
a = x.nthUglyNumber(q)
print "Result",a
print e==a

q = 16
e = 25
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
