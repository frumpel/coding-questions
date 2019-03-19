class Solution(object):
    def isPalindrome(self,s):
        for ii in range(len(s)/2):
            if s[ii]!=s[len(s)-ii-1]:
                return False
        return True

    def superpalindromesInRange(self, L, R):
        """
        :type L: str
        :type R: str
        :rtype: int
        """
        count=0
        min_root=int(int(L)**0.5)
        max_root=int(int(R)**0.5)+1
        for ii in xrange(min_root,max_root+1):
            if self.isPalindrome(str(ii)):
                square=ii**2
                # print "Palindrome",ii,square
                if self.isPalindrome(str(square)) and square>=int(L) and square<=int(R):
                    print "Superpalindrome",ii,square
                    count+=1
        return count


x=Solution()

# q = "4"
# e = True
# print "Question",q
# print "Expect",e
# a = x.isPalindrome(q)
# print "Result",a
# print e==a
#
# q = "12"
# e = False
# print "Question",q
# print "Expect",e
# a = x.isPalindrome(q)
# print "Result",a
# print e==a
#
# q = "121"
# e = True
# print "Question",q
# print "Expect",e
# a = x.isPalindrome(q)
# print "Result",a
# print e==a
#
# q = "122"
# e = False
# print "Question",q
# print "Expect",e
# a = x.isPalindrome(q)
# print "Result",a
# print e==a
#
# q = "1221"
# e = True
# print "Question",q
# print "Expect",e
# a = x.isPalindrome(q)
# print "Result",a
# print e==a

q1 = "4"
q2 = "1000"
e = 4
print "Question",q1,q2
print "Expect",e
a = x.superpalindromesInRange(q1,q2)
print "Result",a
print e==a

q1 = "92904622"
q2 = "232747148"
e = 6
print "Question",q1,q2
print "Expect",e
a = x.superpalindromesInRange(q1,q2)
print "Result",a
print e==a

q1 = "43143"
q2 = "7072263972576"
e = 6
print "Question",q1,q2
print "Expect",e
a = x.superpalindromesInRange(q1,q2)
print "Result",a
print e==a
