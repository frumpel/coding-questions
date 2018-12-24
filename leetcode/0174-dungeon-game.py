class Solution(object):
    def walkPath(self,dungeon,x,y):
        """
        :type dungeon: List[List[int]]
        :type x: int
        :type y: int
        :rtype: int
        """

        if y==len(dungeon)-1 and x==len(dungeon[0])-1:
            s = min(0,dungeon[y][x])
            return s,"S("+str(s)+")["+str(x)+","+str(y)+"]"
        if y==len(dungeon)-1:
            l,t = self.walkPath(dungeon,x+1,y)
            l   = min(0,l + dungeon[y][x])
            return l,t+"-L("+str(l)+")["+str(x)+","+str(y)+"]"
        if x==len(dungeon[0])-1:
            u,t = self.walkPath(dungeon,x,y+1)
            u   = min(0,u + dungeon[y][x])
            return u,t+"-U("+str(u)+")["+str(x)+","+str(y)+"]"

        l,t1 = self.walkPath(dungeon,x+1,y)
        l    = min(0,l + dungeon[y][x])
        u,t2 = self.walkPath(dungeon,x,y+1)
        u    = min(0,u + dungeon[y][x])
        if u>l:
            return u,t2+"-cU("+str(u)+")["+str(x)+","+str(y)+"]"
        else:
            return l,t1+"-cL("+str(l)+")["+str(x)+","+str(y)+"]"

    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        v,t = self.walkPath(dungeon,0,0)
        print t
        return abs(v)+1

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

q = [
[-2,0,-3,3],
[-5,-99,-10,1],
[10,-99,30,-5]
]
e = 7
print "Question",q
print "Expect",e
a = x.calculateMinimumHP(q)
print "Result",a
print e==a

q = [
[-2,-3,3],
[-99,-99,0],
[-5,-10,1],
[10,30,-5]
]
e = 7
print "Question",q
print "Expect",e
a = x.calculateMinimumHP(q)
print "Result",a
print e==a
