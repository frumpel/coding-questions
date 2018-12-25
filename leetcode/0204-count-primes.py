class Solution(object):
    def sieveOfErastothenes(self,n):
        """
        :type n: int
        :rtype: List[int]
        """
        yes_primes=[]
        not_primes=set()

        for ii in xrange(2,n):
            if ii in not_primes:
                continue
            for jj in xrange(2*ii,n,ii):
                not_primes.add(jj)
            yes_primes.append(ii)
        return yes_primes

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

q = 1000000
e = 4
print "Question",q
print "Expect",e
a = x.countPrimes(q)
print "Result",a
print e==a
