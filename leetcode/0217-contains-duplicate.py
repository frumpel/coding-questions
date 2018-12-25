class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        history=set()
        for ii in nums:
            if ii in history:
                return True
            history.add(ii)
        return False

x=Solution()

q = [1,2,3,1]
e = True
print "Question",q
print "Expect",e
a = x.containsDuplicate(q)
print "Result",a
print e==a
