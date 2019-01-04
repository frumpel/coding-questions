from itertools import permutations

class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        n=len(S)+1
        for ii in permutations(range(n)):
            ns=""
            for jj in range(n-1):
                if ii[jj]<ii[jj+1]:
                    ns+="I"
                else:
                    ns+="D"
            if ns == S:
                return list(ii)


x=Solution()

q = "III"
e = [0,1,2,3]
print "Question",q
print "Expect",e
a = x.diStringMatch(q)
print "Result",a
print e==a

q = "IDID"
e = [0,2,1,4,3]
print "Question",q
print "Expect",e
a = x.diStringMatch(q)
print "Result",a
print e==a

q="DDIIDIDIID"
e = [2, 1, 0, 3, 5, 4, 7, 6, 8, 10, 9]
print "Question",q
print "Expect",e
a = x.diStringMatch(q)
print "Result",a
print e==a
