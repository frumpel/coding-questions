class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        map_f={}
        map_r={}
        if len(s) != len(t):
            return False
        for ii in range(len(s)):
            if not s[ii] in map_f:
                if t[ii] in map_r:
                    return False
                map_f[s[ii]]=t[ii]
                map_r[t[ii]]=s[ii]
            elif map_f[s[ii]]!=t[ii]:
                return False
        return True

x=Solution()

q1 = "egg"
q2 = "add"
e = True
print "Question",q1,q2
print "Expect",e
a = x.isIsomorphic(q1,q2)
print "Result",a
print e==a

q1 = "foo"
q2 = "bar"
e = False
print "Question",q1,q2
print "Expect",e
a = x.isIsomorphic(q1,q2)
print "Result",a
print e==a

q1 = "paper"
q2 = "title"
e = True
print "Question",q1,q2
print "Expect",e
a = x.isIsomorphic(q1,q2)
print "Result",a
print e==a

q1 = "aa"
q2 = "ab"
e = False
print "Question",q1,q2
print "Expect",e
a = x.isIsomorphic(q1,q2)
print "Result",a
print e==a

q1 = "ab"
q2 = "aa"
e = False
print "Question",q1,q2
print "Expect",e
a = x.isIsomorphic(q1,q2)
print "Result",a
print e==a
