from collections import defaultdict

class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        ll=defaultdict(int)
        rr=[]
        for ii in A[0]:
            for jj in ii:
                ll[jj]+=1
        for ii in A[1:]:
            tt=defaultdict(int)
            for jj in ii:
                tt[jj]+=1
            for jj in tt.keys()+ll.keys():
                ll[jj]=min(ll[jj],tt[jj])
        for ii in ll:
            if ll[ii]>0:
                for jj in range(ll[ii]):
                    rr.append(ii)
        return rr

x=Solution()

q = ["bella","label","roller"]
e = ["e","l","l"]
print "Question",q
print "Expect",e
a = x.commonChars(q)
print "Result",a
print e==a

q = ["cool","lock","cook"]
e = ["c","o"]
print "Question",q
print "Expect",e
a = x.commonChars(q)
print "Result",a
print e==a

q = ["acabcddd","bcbdbcbd","baddbadb","cbdddcac","aacbcccd","ccccddda","cababaab","addcaccd"]
e = []
print "Question",q
print "Expect",e
a = x.commonChars(q)
print "Result",a
print e==a
