class Solution(object):
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        A=0
        for yy in range(len(grid)):
            for xx in range(len(grid[0])):
                # Add top/bottom
                if grid[yy][xx]>0:
                    A+=2
                # Add left/right boundaries
                if xx == 0:
                    A+=grid[yy][xx]
                if xx==len(grid[0])-1:
                    A+=grid[yy][xx]
                if xx<len(grid[0])-1:
                    A+=abs(grid[yy][xx+1]-grid[yy][xx])
                # Add top/bottom boundaries
                if yy == 0:
                    A+=grid[yy][xx]
                if yy==len(grid)-1:
                    A+=grid[yy][xx]
                if yy<len(grid)-1:
                    A+=abs(grid[yy+1][xx]-grid[yy][xx])
        return A

x=Solution()

q = [[2]]
e = 10
print "Question",q
print "Expect",e
a = x.surfaceArea(q)
print "Result",a
print e==a

q = [[2,2,2],[2,1,2],[2,2,2]]
e = 46
print "Question",q
print "Expect",e
a = x.surfaceArea(q)
print "Result",a
print e==a

q = [[1,2],[3,4]]
e = 34
print "Question",q
print "Expect",e
a = x.surfaceArea(q)
print "Result",a
print e==a

q = [[1,0],[0,2]]
e = 16
print "Question",q
print "Expect",e
a = x.surfaceArea(q)
print "Result",a
print e==a

q = [[1,1,1],[1,0,1],[1,1,1]]
e = 32
print "Question",q
print "Expect",e
a = x.surfaceArea(q)
print "Result",a
print e==a
