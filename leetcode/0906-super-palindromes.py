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
        for ii in range(int(L),int(R)+1):
            if self.isPalindrome(str(ii)):
                root=ii**0.5
                # print "Palindrome",ii,root
                if root==int(root) and self.isPalindrome(str(int(root))):
                    print "Superpalindrome",ii,root
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
