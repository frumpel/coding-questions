class Solution(object):
    def walkPath(self,dungeon,x,y):
        """
        :type dungeon: List[List[int]]
        :type x: int
        :type y: int
        :rtype: int
        """
        if y==len(dungeon)-1 and x==len(dungeon[0])-1:
            return dungeon[y][x]
        if y==len(dungeon)-1:
            return self.walkPath(dungeon,x+1,y) + dungeon[y][x]
        if x==len(dungeon[0])-1:
            return self.walkPath(dungeon,x,y+1) + dungeon[y][x]

        r = self.walkPath(dungeon,x+1,y)
        d = self.walkPath(dungeon,x,y+1)
        return min(r,d) + dungeon[y][x]

    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        return self.walkPath(dungeon,0,0)

x=Solution()

q = [
[-2,-3,3],
[-5,-10,1],
[10,30,-5]
]
e = 7
print "Question",q
print "Expect",e
a = x.calculateMinimumHP(q)
print "Result",a
print e==a
