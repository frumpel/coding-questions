import string

class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        def unimaketrans(src, dst):
            uniarr=range(256)
            for ii in range(len(src)):
                uniarr[ord(src[ii])]=ord(dst[ii])
            return "".join([unichr(x) for x in uniarr])

        alpha="abcdefghijklmnopqrstuvwxyz"
        # trmap=string.maketrans(order,alpha)
        trmap=unimaketrans(order,alpha)
        # print trmap[0:127]
        # print "abc".translate(trmap)
        sword = sorted(words,key = lambda s : s.translate(trmap))
        print words,"->",sword
        return words == sword


x=Solution()

q1 = []
q2 = "hlabcdefgijkmnopqrstuvwxyz"
e = True
print "Question",q1
print "Expect",e
a = x.isAlienSorted(q1,q2)
print "Result",a
print e==a

q1 = ["hello","leetcode"]
q2 = "hlabcdefgijkmnopqrstuvwxyz"
e = True
print "Question",q1
print "Expect",e
a = x.isAlienSorted(q1,q2)
print "Result",a
print e==a

q1 = ["word","world","row"]
q2 = "worldabcefghijkmnpqstuvxyz"
e = False
print "Question",q1
print "Expect",e
a = x.isAlienSorted(q1,q2)
print "Result",a
print e==a

q1 = ["apple","app"]
q2 = "abcdefghijklmnopqrstuvwxyz"
e = False
print "Question",q1
print "Expect",e
a = x.isAlienSorted(q1,q2)
print "Result",a
print e==a

q1 = ["kuvp","q"]
q2 = "ngxlkthsjuoqcpavbfdermiywz"
e = True
print "Question",q1
print "Expect",e
a = x.isAlienSorted(q1,q2)
print "Result",a
print e==a
