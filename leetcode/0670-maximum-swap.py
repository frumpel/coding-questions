class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        ns=list(str(num))

        # Find the first number we can replace
        for ii in range(len(ns)):
            maxnum = ns[ii]
            maxidx = ii
            for jj in reversed(range(ii,len(ns))):
                if ns[jj]>maxnum:
                    maxidx=jj
                    maxnum=ns[jj]
            if maxnum > ns[ii]:
                tmp = ns[maxidx]
                ns[maxidx] = ns[ii]
                ns[ii] = tmp
                break
        return int("".join(ns))

x = Solution()

q = 1234567
e = 7234561
a = x.maximumSwap(q)
print "Question",q
print "Expect",e
print "Result",a
print e==a

q = 9234567
e = 9734562
a = x.maximumSwap(q)
print "Question",q
print "Expect",e
print "Result",a
print e==a

q = 9834567
e = 9874563
a = x.maximumSwap(q)
print "Question",q
print "Expect",e
print "Result",a
print e==a
