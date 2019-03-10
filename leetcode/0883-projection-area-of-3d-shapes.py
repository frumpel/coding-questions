class Solution(object):
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        nn=len(grid)
        ll=[0]*nn
        ff=[0]*nn
        tt=0
        for ii in range(nn):
            for jj in range(nn):
                if grid[ii][jj]>0:
                    tt+=1
                ll[ii]=max(ll[ii],grid[ii][jj])
                ff[jj]=max(ff[jj],grid[ii][jj])
        return tt+sum(ll)+sum(ff)

x=Solution()

q = [[2]]
e = 5
print "Question",q
print "Expect",e
a = x.projectionArea(q)
print "Result",a
print e==a

q = [[1,2],[3,4]]
e = 17
print "Question",q
print "Expect",e
a = x.projectionArea(q)
print "Result",a
print e==a

q = [[1,0],[0,2]]
e = 8
print "Question",q
print "Expect",e
a = x.projectionArea(q)
print "Result",a
print e==a

q = [[1,1,1],[1,0,1],[1,1,1]]
e=14
print "Question",q
print "Expect",e
a = x.projectionArea(q)
print "Result",a
print e==a
