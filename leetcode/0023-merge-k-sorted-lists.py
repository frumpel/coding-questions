# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def ArrayOfNodelists_from_ArrayOfArrays(self, arrayOfArrays):
        ret=[]
        for ii in arrayOfArrays:
            start=previous=current=ListNode(0)
            for jj in ii:
                current.val=jj
                current.next=ListNode(0)
                previous = current
                current = current.next
            previous.next=None
            ret.append(start)
        return ret

    def ArrayOfArrays_from_ArrayOfNodeLists(self,arrayOfNodes):
        ret=[]
        for listnode in arrayOfNodes:
            ret.append(self.Array_from_NodeList(listnode))
        return ret

    def Array_from_NodeList(self,listNode):
        ret=[]
        while listNode != None:
            ret.append(listNode.val)
            listNode=listNode.next
        return ret

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        from Queue import PriorityQueue
        head = point = ListNode(0)
        q = PriorityQueue()
        for l in lists:
            if l:
                q.put((l.val, l))
        while not q.empty():
            val, node = q.get()
            point.next = ListNode(val)
            point = point.next
            node = node.next
            if node:
                q.put((node.val, node))
        return head.next
    # def mergeKLists(self, lists):
    #     """
    #     :type lists: List[ListNode]
    #     :rtype: ListNode
    #     """
    #     if len(lists) < 1:
    #         return None
    #
    #     ret=previous=current=ListNode(0)
    #
    #     # Find minval instead of assuming
    #     while len(lists) > 0:
    #         print "Lists",lists
    #         minval=lists[0].val
    #         listindex = 0
    #         for ii in range(len(lists)):
    #             if lists[ii].val < minval:
    #                 minval = lists[ii].val
    #                 listindex = ii
    #         current.val = minval
    #         current.next = ListNode(0)
    #         previous = current
    #         current = current.next
    #         if lists[listindex].next != None:
    #             lists[listindex]=lists[ii].next
    #         else:
    #             del(lists[listindex])
    #     previous.next = None
    #     return ret


x=Solution()

q=[[1,4,5],[1,3,4],[2,6]]
qll=x.ArrayOfNodelists_from_ArrayOfArrays(q)
# print "qll",qll
# qla=x.ArrayOfArrays_from_ArrayOfNodeLists(qll)
# print "qla",qla
qla=x.mergeKLists(qll)
print "qla",qla
# qla=[ListNode(1),ListNode(2),ListNode(3)]
a=x.Array_from_NodeList(qla)
e=[1,1,2,3,4,4,5,6]
print "Question",q
print "Expect",e
print "Result",a
print e==a
