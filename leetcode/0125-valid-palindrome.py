class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        cmap={}
        for ii in range(26):
            cmap[chr(ord("a")+ii)] = chr(ord("a")+ii)
            cmap[chr(ord("A")+ii)] = chr(ord("a")+ii)
        for ii in range(10):
            cmap[chr(ord("0")+ii)] = chr(ord("0")+ii)
        print cmap
        t=[cmap[c] for c in s if c in cmap]
        print t
        return t==t[::-1]

x=Solution()

q = "A man, a plan, a canal: Panama"
e = True
print "Question",q
print "Expect",e
a = x.isPalindrome(q)
print "Result",a
print e==a



q = "0P"
e = False
print "Question",q
print "Expect",e
a = x.isPalindrome(q)
print "Result",a
print e==a
