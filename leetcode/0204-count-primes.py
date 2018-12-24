class Solution(object):
    def sieveOfErastothenes(self,n):
        """
        :type n: int
        :rtype: List[int]
        """
        r=range(2,n)
        for ii in range(2,n):
            for jj in range(2*ii,n,ii):
                if jj in r:
                    r.remove(jj)
        return r

    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        return len(self.sieveOfErastothenes(n))

x=Solution()

q = 10
e = 4
print "Question",q
print "Expect",e
a = x.countPrimes(q)
print "Result",a
print e==a
