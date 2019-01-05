class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        def isLetter(c):
            if (ord(c)>=65 and ord(c)<=90) or (ord(c)>=97 and ord(c)<=122):
                return True
            return False

        r=list(S)
        sp=len(S)-1
        rp=0
        while True:
            # print sp,rp,S,r
            while sp>=0 and not isLetter(S[sp]):
                sp-=1
            while rp<len(S)-1 and not isLetter(r[rp]):
                rp+=1
            # print sp,rp
            if sp<0 or rp>len(S)-1:
                break
            r[rp]=S[sp]
            sp-=1
            rp+=1
        return "".join(r)

x=Solution()

q = "ab-cd"
e = "dc-ba"
print "Question",q
print "Expect",e
a = x.reverseOnlyLetters(q)
print "Result",a
print e==a

q = "a-bC-dEf-ghIj"
e = "j-Ih-gfE-dCba"
print "Question",q
print "Expect",e
a = x.reverseOnlyLetters(q)
print "Result",a
print e==a

q = "-"
e = "-"
print "Question",q
print "Expect",e
a = x.reverseOnlyLetters(q)
print "Result",a
print e==a

q = ";1yDV"
e = ";1VDy"
print "Question",q
print "Expect",e
a = x.reverseOnlyLetters(q)
print "Result",a
print e==a
