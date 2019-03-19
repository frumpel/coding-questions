

class Solution(object):
    def isPalindrome(self,s):
        for ii in range(len(s)/2):
            if s[ii]!=s[len(s)-ii-1]:
                return False
        return True

    def createNumericPalindromes(self,min_str,max_str):
        min_dig = len(min_str)
        max_dig = len(max_str)
        val_min = int(min_str)
        val_max = int(max_str)
        # print min_dig,max_dig,val_min,val_max
        for ii in xrange(min_dig,max_dig+1):
            cnt_dig = (ii+1)/2
            rng_min = int("1"+"0"*(cnt_dig-1))
            rng_max = int("9"*cnt_dig)
            for jj in xrange(rng_min,rng_max+1):
                res_str = str(jj) + str(jj)[0:ii-cnt_dig][::-1]

                if int(res_str)>val_max:
                    return
                if int(res_str)>=val_min:
                    yield res_str

    def superpalindromesInRange(self, L, R):
        """
        :type L: str
        :type R: str
        :rtype: int
        """
        count=0
        pcount=0
        min_root=int(int(L)**0.5)
        max_root=int(int(R)**0.5)+1
        # print "Calling palindrome creation with",min_root,max_root
        for ii in self.createNumericPalindromes(str(min_root),str(max_root)):
            # print "...",ii
            pcount+=1
            square=int(ii)**2
            # print "Palindrome",ii,square
            if self.isPalindrome(str(square)) and square>=int(L) and square<=int(R):
                # print "Superpalindrome",ii,square
                count+=1
        # print "Summary numbers",count,pcount,max_root-min_root
        return count

    # def superpalindromesInRangeOld(self, L, R):
    #     """
    #     :type L: str
    #     :type R: str
    #     :rtype: int
    #     """
    #     count=0
    #     pcount=0
    #     min_root=int(int(L)**0.5)
    #     max_root=int(int(R)**0.5)+1
    #     for ii in xrange(min_root,max_root+1):
    #         if self.isPalindrome(str(ii)):
    #             square=ii**2
    #             # print "Palindrome",ii,square
    #             if self.isPalindrome(str(square)) and square>=int(L) and square<=int(R):
    #                 print "Superpalindrome",ii,square
    #                 count+=1
    #     print "Summary numbers",count,pcount,max_root-min_root
    #     return count

x=Solution()

# # Validate palindrome creation
# for ii in x.createNumericPalindromes("7","321"):
#     print ii

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
e = 30
print "Question",q1,q2
print "Expect",e
a = x.superpalindromesInRange(q1,q2)
print "Result",a
print e==a
