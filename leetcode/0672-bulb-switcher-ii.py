class Solution(object):
    def flipLights(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """

        # Set up operators
        data=0L
        op1=0L
        op2=0L
        op3=0L
        op4=0L
        res=set()
        for ii in range(n):
            data|= (1L<<ii)
            op1 |= (1L<<ii)
            if ii%2 == 0:
                op2 |= (1L<<ii)
            if ii%2 == 1:
                op3 |= (1L<<ii)
            if ii%3==0:
                op4 |= (1L<<ii)
        # print "data:",data
        # print "op1:",op1
        # print "op2:",op2
        # print "op3:",op3
        # print "op4:",op4

        # Optimize iteration count - m doesn't need to be larger than 2^(ops)
        if m>2**4:
            m=2**4

        d1=data
        for ii in range(m+1):
            for jj in range(m+1-ii):
                for kk in range(m+1-(ii+jj)):
                    ll = m - (ii+jj+kk)
                    d4 = data
                    if ii%2 == 1:
                        d4 ^= op1
                    if jj%2 == 1:
                        d4 ^= op2
                    if kk%2 == 1:
                        d4 ^= op3
                    if ll%2 == 1:
                        d4 ^= op4
                    # print "d4:",ii,jj,kk,ll,d4
                    res.add(d4)
        print m,n,res
        return len(res)

    # def flipLights(self, n, m):
    #     """
    #     :type n: int
    #     :type m: int
    #     :rtype: int
    #     """
    #     data=0L
    #     op1=0L
    #     op2=0L
    #     op3=0L
    #     op4=0L
    #     res=set()
    #     for ii in range(n):
    #         data|= (1L<<ii)
    #         op1 |= (1L<<ii)
    #         if ii%2 == 0:
    #             op2 |= (1L<<ii)
    #         if ii%2 == 1:
    #             op3 |= (1L<<ii)
    #         if ii%3==0:
    #             op4 |= (1L<<ii)
    #
    #     print "data:",data
    #     print "op1:",op1
    #     print "op2:",op2
    #     print "op3:",op3
    #     print "op4:",op4
    #     d1=data
    #     for ii in range(m):
    #         d2=d1
    #         for jj in range(m-ii):
    #             d3=d2
    #             for kk in range(m-(ii+jj)):
    #                 d4=d3
    #                 for ll in range(m-(ii+jj+kk)):
    #                     d4^=op4
    #                 print "d4:",ii,jj,kk,ll,d4
    #                 res.add(d4)
    #                 d3^=op3
    #             print "d3:",ii,jj,kk,ll,d3
    #             res.add(d3)
    #             d2^=op2
    #         print "d2:",ii,jj,kk,ll,d2
    #         res.add(d2)
    #         d1^=op1
    #     print "d1:",ii,jj,kk,ll,d1
    #     res.add(d1)
    #     print m,n,res
    #     return len(res)

x = Solution()

q1 = 1
q2 = 1
e = 2
a = x.flipLights(q1,q2)
print "Question",q1,q2
print "Expect",e
print "Result",a
print e==a

q1 = 2
q2 = 1
e = 3
a = x.flipLights(q1,q2)
print "Question",q1,q2
print "Expect",e
print "Result",a
print e==a

q1 = 3
q2 = 1
e = 4
a = x.flipLights(q1,q2)
print "Question",q1,q2
print "Expect",e
print "Result",a
print e==a

q1 = 3
q2 = 3
e = 8 # [0L, 2L, 5L, 6L, 4L, 3L, 7L, 1L]
a = x.flipLights(q1,q2)
print "Question",q1,q2
print "Expect",e
print "Result",a
print e==a

q1 = 5
q2 = 8
e = 8 # [0L, 2L, 5L, 6L, 4L, 3L, 7L, 1L]
a = x.flipLights(q1,q2)
print "Question",q1,q2
print "Expect",e
print "Result",a
print e==a
