class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l1p=0
        l2p=0
        nlc=0
        total=(len(nums1)+len(nums2))
        cplusone=total/2
        nl=[]
        # Easy: sort/merge
        nl=sorted(nums1+nums2)
        # Fast: Array merge to half way point - instead of using "sorted(l1+l2)"
        # while nlc <= cplusone and l1p<len(nums1) and l2p<len(nums2):
        #     if nums1[l1p]<nums2[l2p]:
        #         nl.append(nums1[l1p])
        #         l1p+=1
        #     else:
        #         nl.append(nums2[l2p])
        #         l2p+=1
        #     nlc+=1
        # while nlc <= cplusone and l1p<len(nums1):
        #     nl.append(nums1[l1p])
        #     l1p+=1
        #     nlc+=1
        # while nlc <= cplusone and l2p<len(nums2):
        #     nl.append(nums2[l2p])
        #     l2p+=1
        #     nlc+=1
        print nl
        print cplusone
        if total&1:
            return nl[cplusone]
        else:
            return 1.0*(nl[cplusone]+nl[cplusone-1])/2

x=Solution()

q=[[1,3],[2]]
e=2
a=x.findMedianSortedArrays(q[0],q[1])
print "Question",q
print "Expect",e
print "Result",a
print e==a

q=[[1,2],[3,4]]
e=2.5
a=x.findMedianSortedArrays(q[0],q[1])
print "Question",q
print "Expect",e
print "Result",a
print e==a
