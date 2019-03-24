class Solution(object):

    MOUSE_INDEX=0
    CAT_INDEX=1

    RES_CAT_WINS=2
    RES_MOUSE_WINS=1
    RES_DRAW=0

    graph=[]

    def playerIndex(self,index):
        return index

    def enemyIndex(self,index):
        return (index+1)%2

    def traverseGraph(self,trail,pos,active):
        print "TG:",active,pos,trail
        if pos in trail:
            print "Double back, draw"
            return self.RES_DRAW
        if pos[self.MOUSE_INDEX]==pos[self.CAT_INDEX]:
            print "Caught mouse, cat wins"
            return self.RES_CAT_WINS
        if pos[self.MOUSE_INDEX]==0:
            print "Mouse escaped to 0, mouse wins"
            return self.RES_MOUSE_WINS

        ra=[]
        for ii in self.graph[pos[active]]:
            np=list(pos)
            np[self.playerIndex(active)]=ii
            if np[self.CAT_INDEX]!=0:
                rv=self.traverseGraph(
                    list(trail)+[pos],
                    np,
                    self.enemyIndex(active))
                ra.append(rv)
        if active == self.CAT_INDEX:
            if self.RES_CAT_WINS in ra:
                res = self.RES_CAT_WINS
            elif self.RES_DRAW in ra:
                res = self.RES_DRAW
            else:
                res = self.RES_MOUSE_WINS
        else:
            if self.RES_MOUSE_WINS in ra:
                res = self.RES_MOUSE_WINS
            elif self.RES_DRAW in ra:
                res = self.RES_DRAW
            else:
                res = self.RES_CAT_WINS
        print "Results:",active,ra,res
        return res

    def catMouseGame(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        self.graph=graph
        # Mouse start at 1, cat at 2
        return self.traverseGraph([],(1,2),self.MOUSE_INDEX)

x=Solution()

q = [[2,5],[3],[0,4,5],[1,4,5],[2,3],[0,2,3]]
e = 0
print "Question",q
print "Expect",e
a = x.catMouseGame(q)
print "Result",a
print e==a

q = [[3,4],[3,4],[3,4],[1,2],[1,2]]
e = 2
print "Question",q
print "Expect",e
a = x.catMouseGame(q)
print "Result",a
print e==a

q = [[],[3],[4],[1],[2]]
e = 0
print "Question",q
print "Expect",e
a = x.catMouseGame(q)
print "Result",a
print e==a

q = [[4,5],[4,5],[3],[2,4,5],[0,1,3],[0,1,3]]
e = 1
print "Question",q
print "Expect",e
a = x.catMouseGame(q)
print "Result",a
print e==a
