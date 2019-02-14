# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        rh = rp = ListNode(None)
        while l1!=None and l2!=None:
            # print "rh:",list_to_array(rh)," rp:",list_to_array(rp)," l1:",list_to_array(l1)," l2:",list_to_array(l2)
            if l1.val < l2.val:
                rp.next=l1
                l1=l1.next
                rp=rp.next
            else:
                rp.next=l2
                l2=l2.next
                rp=rp.next

        if l1!=None:
            rp.next=l1
        if l2!=None:
            rp.next=l2
        return rh.next

def array_to_list(a):
    rp = rh = ListNode(None)
    for v in a:
        rp.next = ListNode(v)
        rp = rp.next
    return rh.next

def list_to_array(l):
    r=[]
    while l != None:
        r.append(l.val)
        l=l.next
    return r


x=Solution()

q1 = [1,2,4]
q2 = [1,3,4]
e = [1,1,2,3,4,4]
print "Question",q1,q2
print "Expect",e
a = list_to_array(x.mergeTwoLists(array_to_list(q1),array_to_list(q2)))
print "Result",a
