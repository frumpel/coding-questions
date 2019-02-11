# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        lll = 0
        lln=head
        while lln.next!=None:
            lll+=1
            lln=lln.next
        llc = (lll+1)/2
        lli=0
        ret=head
        while lli < llc:
            ret=ret.next
            lli+=1
        return ret

        
