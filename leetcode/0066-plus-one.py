class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        c=1
        for ii in range(len(digits)):
            s=digits[len(digits)-1-ii]+c
            digits[len(digits)-1-ii]=s%10
            c=(s-digits[len(digits)-1-ii])//10
        if c:
            digits.insert(0,c)
        return digits

x=Solution()

q = [1,2,3,4]
e = [1,2,3,5]
print "Question",q
print "Expect",e
a = x.plusOne(q)
print "Result",a
print e==a

q = [1,2,3,9]
e = [1,2,4,0]
print "Question",q
print "Expect",e
a = x.plusOne(q)
print "Result",a
print e==a

q = [9,9,9,9]
e = [1,0,0,0,0]
print "Question",q
print "Expect",e
a = x.plusOne(q)
print "Result",a
print e==a
