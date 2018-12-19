import heapq
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last=None
        count=2
        heapq.heapify(nums)
        while len(nums):
            x=heapq.heappop(nums)
            print nums,x,last,count
            if x != last:
                if count!=2:
                    return last
                count=0
                last=x
            else:
                count+=1
        return x

x=Solution()

q = [2,2,3,2]
e = 3
print "Question",q
print "Expect",e
a = x.singleNumber(q)
print "Result",a
print e==a

q = [0,1,0,1,0,1,99]
e = 99
print "Question",q
print "Expect",e
a = x.singleNumber(q)
print "Result",a
print e==a

q = [1,2,2,2,3,3,3]
e = 1
print "Question",q
print "Expect",e
a = x.singleNumber(q)
print "Result",a
print e==a
