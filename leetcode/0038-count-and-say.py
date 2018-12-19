class Solution(object):
    def nextSay(self,v):
        """
        :type v: str
        :rtype: str
        """
        if len(v)<1:
            return ""

        r=""
        p=v[0]
        n=0
        for ii in range(len(v)):
            c=v[ii]
            if c!=p:
                r+=str(n)+p
                n=0
                p=c
            n+=1
        if n>0:
            r+=str(n)+p
        return r

    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        r="1"
        for ii in range(n-1):
            r=self.nextSay(r)
        return r


x=Solution()

qa = {
 1:"1",
 2:"11",
 3:"21",
 4:"1211",
 5:"111221",
 6:"312211"
}

# for ii in qa:
#     if ii+1 in qa:
#         q = qa[ii]
#         e = qa[ii+1]
#         a = x.nextSay(q)
#         print "Question",q
#         print "Expect",e
#         print "Result",a
#         print e==a

for ii in qa:
    q = ii
    e = qa[ii]
    a = x.countAndSay(q)
    print "Question",q
    print "Expect",e
    print "Result",a
    print e==a
