class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle)==0:
            return 0
        if len(haystack)==0:
            return -1
        if len(needle) > len(haystack):
            return -1
        hptr = nptr = 0
        for hptr in range(len(haystack)-len(needle)+1):
            match=True
            for nptr in range(len(needle)):
                if haystack[hptr+nptr]!=needle[nptr]:
                    match=False
                    break
            if match == True:
                return hptr
        return -1


x=Solution()

q1 = "hello"
q2 = "ll"
e = 2
a = x.strStr(q1,q2)
print "Question",q1,"-",q2
print "Expect",e
print "Result",a
print e==a

q1 = "a"
q2 = "a"
e = 0
a = x.strStr(q1,q2)
print "Question",q1,"-",q2
print "Expect",e
print "Result",a
print e==a

q1 = "a"
q2 = ""
e = 0
a = x.strStr(q1,q2)
print "Question",q1,"-",q2
print "Expect",e
print "Result",a
print e==a

q1 = ""
q2 = "a"
e = -1
a = x.strStr(q1,q2)
print "Question",q1,"-",q2
print "Expect",e
print "Result",a
print e==a

q1 = "missisippi"
q2 = "a"
e = -1
a = x.strStr(q1,q2)
print "Question",q1,"-",q2
print "Expect",e
print "Result",a
print e==a
