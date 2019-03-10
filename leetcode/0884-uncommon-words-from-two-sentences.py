from collections import defaultdict

class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        Aa=A.split(" ")
        Aa.sort()
        Ac=defaultdict(int)
        for ii in Aa:
            Ac[ii]+=1
        Ba=B.split(" ")
        Ba.sort()
        Bc=defaultdict(int)
        for ii in Ba:
            Bc[ii]+=1
        uu=[]
        kk=set(Ac.keys()+Bc.keys())
        for ii in kk:
            if (Ac[ii]==1 and Bc[ii]==0) or (Ac[ii]==0 and Bc[ii]==1):
                uu.append(ii)
        return uu

x=Solution()

q1 = "this apple is sweet"
q2 = "this apple is sour"
e = ["sweet","sour"]
print "Question",q1,q2
print "Expect",e
a = x.uncommonFromSentences(q1,q2)
print "Result",a
print e==a

q1 = "apple apple"
q2 = "banana"
e = ["banana"]
print "Question",q1,q2
print "Expect",e
a = x.uncommonFromSentences(q1,q2)
print "Result",a
print e==a

q1 = "s z z z s"
q2 = "s z ejt"
e = ["ejt"]
print "Question",q1,q2
print "Expect",e
a = x.uncommonFromSentences(q1,q2)
print "Result",a
print e==a
