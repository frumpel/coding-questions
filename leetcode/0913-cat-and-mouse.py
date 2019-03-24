from collections import deque

class Solution(object):

    MOUSE_INDEX=0
    CAT_INDEX=1

    RES_CAT_WINS=2
    RES_MOUSE_WINS=1
    RES_DRAW=0

    queue = None
    trail = None

    def catMouseGame(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        pos_mouse=1
        pos_cat=2

        self.queue=deque()
        self.queue.append([pos_mouse,pos_cat,self.MOUSE_INDEX])
        self.trail=[]

        while len(self.queue) > 0:
            print "--- \nqueue",len(self.queue),self.queue
            pos_mouse, pos_cat, active = self.queue.popleft()

            if [pos_mouse,pos_cat] in self.trail:
                return self.RES_DRAW

            self.trail.append([pos_mouse,pos_cat])

            if active == self.CAT_INDEX:
                for ii in graph[pos_cat]:
                    if pos_mouse == ii:
                        print "Cat catches mouse at",ii
                        return self.RES_CAT_WINS
                    elif ii != 0:
                        print "Adding cat pos to queue",pos_mouse,ii,self.MOUSE_INDEX
                        self.queue.append([pos_mouse,ii,self.MOUSE_INDEX])
                    else:
                        print "Skipping cat option",pos_mouse,ii
            else:
                for ii in graph[pos_mouse]:
                    if 0 == ii:
                        print "Mouse escapes to",ii
                        return self.RES_MOUSE_WINS
                    elif ii != pos_cat:
                        print "Adding mouse pos to queue",ii,pos_cat,self.CAT_INDEX
                        self.queue.append([ii,pos_cat,self.CAT_INDEX])
                    else:
                        print "Skipping mouse option",ii,pos_cat
        print "Empty queue, draw"
        return self.RES_DRAW

x=Solution()

# q = [[2,5],[3],[0,4,5],[1,4,5],[2,3],[0,2,3]]
# e = 0
# print "Question",q
# print "Expect",e
# a = x.catMouseGame(q)
# print "Result",a
# print e==a
#
# q = [[3,4],[3,4],[3,4],[1,2],[1,2]]
# e = 2
# print "Question",q
# print "Expect",e
# a = x.catMouseGame(q)
# print "Result",a
# print e==a
#
# q = [[],[3],[4],[1],[2]]
# e = 0
# print "Question",q
# print "Expect",e
# a = x.catMouseGame(q)
# print "Result",a
# print e==a
#
# q = [[4,5],[4,5],[3],[2,4,5],[0,1,3],[0,1,3]]
# e = 1
# print "Question",q
# print "Expect",e
# a = x.catMouseGame(q)
# print "Result",a
# print e==a
#
# q = [[1,4],[0,2,5,6],[1,7],[5,7,8],[0,7,9],[1,3,9],[1],[2,3,4,9],[3],[4,5,7]]
# e = 1
# print "Question",q
# print "Expect",e
# a = x.catMouseGame(q)
# print "Result",a
# print e==a

q = [[2,3],[3,4],[0,4],[0,1],[1,2]]
e = 1
print "Question",q
print "Expect",e
a = x.catMouseGame(q)
print "Result",a
print e==a
