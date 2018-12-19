
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        map = {
            "(":1, ")":-1,
            "[":2, "]":-2,
            "{":3, "}":-3,
        }
        h=[]
        for ii in s:
            if ii in map:
                if map[ii]>0:
                    h.append(map[ii])
                else:
                    if len(h)<1:
                        return False
                    if h.pop() != -map[ii]:
                        return False
        if len(h):
            return False
        return True

x=Solution()

q = "()[]{}"
e = True
a = x.isValid(q)
print "Question",q
print "Expect",e
print "Result",a
print e==a

q = "(]"
e = False
a = x.isValid(q)
print "Question",q
print "Expect",e
print "Result",a
print e==a

q = "([)]"
e = False
a = x.isValid(q)
print "Question",q
print "Expect",e
print "Result",a
print e==a

q = "{[]}"
e = True
a = x.isValid(q)
print "Question",q
print "Expect",e
print "Result",a
print e==a

q = "]"
e = False
a = x.isValid(q)
print "Question",q
print "Expect",e
print "Result",a
print e==a
