class Solution(object):

    # Works - still only 67%?!? Well, but removing the list copy makes it slower so don't rely on that
    def minIncrementForUnique(self, B):
        """
        :type A: List[int]
        :rtype: int
        """
        A=list(B)
        A.sort()
        count=0
        for ii in range(1,len(A)):
            print A,ii,count
            if A[ii]<=A[ii-1]:
                count+=A[ii-1]+1-A[ii]
                A[ii]=A[ii-1]+1
        return count

    # # Probably works but still throws timeout
    # def minIncrementForUnique(self, B):
    #     """
    #     :type A: List[int]
    #     :rtype: int
    #     """
    #     A=list(B)
    #     A.sort()
    #     A.append(40002)
    #     count=0
    #     while len(A)>2:
    #         print A,count
    #         if A[0]==A[1]:
    #             for ii in range(1,len(A)-1):
    #                 if A[ii+1]>A[ii]+1:
    #                     count+=A[ii]+1-A[0]
    #                     A[ii]+=1
    #                     break
    #                 else:
    #                     A[ii]=A[ii+1]
    #         else:
    #             del(A[0])
    #     return count

    # # Probably works but throws timeout
    # def minIncrementForUnique(self, B):
    #     """
    #     :type A: List[int]
    #     :rtype: int
    #     """
    #     A=list(B)
    #     A.sort()
    #     A.append(40002)
    #     count=0
    #     while len(A)>2:
    #         print A,count
    #         if A[0]==A[1]:
    #             for ii in range(len(A)-1):
    #                 if A[ii+1]>A[ii]+1:
    #                     count+=A[ii]+1-A[0]
    #                     A.append(A[ii]+1)
    #                     A.sort()
    #                     break
    #         del(A[0])
    #     return count


x=Solution()

q=[3,2,1,2,1,7]
e=6
a=x.minIncrementForUnique(q)
print "Question",q
print "Expect",e
print "Result",a
print e==a

q=[9,8,7,6,5,4,3,2,1,1]
e=9
a=x.minIncrementForUnique(q)
print "Question",q
print "Expect",e
print "Result",a
print e==a

q=[9,8,7,6,5,4,3,2,1,1,1]
e=19
a=x.minIncrementForUnique(q)
print "Question",q
print "Expect",e
print "Result",a
print e==a

q=[0,2,0]
e=1
a=x.minIncrementForUnique(q)
print "Question",q
print "Expect",e
print "Result",a
print e==a

q=[1,1]
e=1
a=x.minIncrementForUnique(q)
print "Question",q
print "Expect",e
print "Result",a
print e==a

q=[1,1,1]
e=3
a=x.minIncrementForUnique(q)
print "Question",q
print "Expect",e
print "Result",a
print e==a

q=[1,3,1]
e=1
a=x.minIncrementForUnique(q)
print "Question",q
print "Expect",e
print "Result",a
print e==a
