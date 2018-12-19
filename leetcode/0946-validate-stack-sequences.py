class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        if len(pushed) == 1:
            return pushed == popped



x=Solution()

q1=[1]
q2=[1]
e=True
a=x.validateStackSequences(q1,q2)
print "Question",q1,q2
print "Expect",e
print "Result",a
print e==a

q1=[1]
q2=[2]
e=False
a=x.validateStackSequences(q1,q2)
print "Question",q1,q2
print "Expect",e
print "Result",a
print e==a

q1=[1,2,3,4,5]
q2=[4,5,3,2,1]
e=True
a=x.validateStackSequences(q1,q2)
print "Question",q1,q2
print "Expect",e
print "Result",a
print e==a
