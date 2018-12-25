class Solution(object):
    # Generate primes
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

    # Count generated prime array - too slow
    def countPrimesWithGeneration(self, n):
        """
        :type n: int
        :rtype: int
        """
        return len(self.sieveOfErastothenes(n))

    # Simplified erastothenes. Count hits using sets - fast enough but too memory intensive
    def countPrimesWithSets(self, n):
        """
        :type n: int
        :rtype: int
        """
        yes_primes=0
        not_primes=set()
        for ii in xrange(2,n):
            if ii in not_primes:
                continue
            for jj in xrange(2*ii,n,ii):
                not_primes.add(jj)
            yes_primes+=1
        return yes_primes

    # Simplified erastothenes saving a bit of memory by using array instead of set
    #
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<3:
            return 0
        yes_primes=[True]*n
        for ii in xrange(2,n):
            if yes_primes[ii]:
                for jj in xrange(2*ii,n,ii):
                    yes_primes[jj]=False
        # # We could recover the actual primes here
        # print [prime for prime,isprime in enumerate(yes_primes) if isprime]
        return sum(yes_primes)-2


x=Solution()

q = 10
e = 4
print "Question",q
print "Expect",e
a = x.countPrimes(q)
print "Result",a
print e==a

q = 1000000
e = 78498
print "Question",q
print "Expect",e
a = x.countPrimes(q)
print "Result",a
print e==a

q = 0
e = 0
print "Question",q
print "Expect",e
a = x.countPrimes(q)
print "Result",a
print e==a

q = 1
e = 0
print "Question",q
print "Expect",e
a = x.countPrimes(q)
print "Result",a
print e==a

q = 2
e = 0
print "Question",q
print "Expect",e
a = x.countPrimes(q)
print "Result",a
print e==a
