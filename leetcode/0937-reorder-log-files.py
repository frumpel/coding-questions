class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        ll=[]
        nl=[]
        for line in logs:
            larr=line.split(" ")
            if larr[1].isdigit():
                nl.append(line)
            else:
                ll.append(larr[1:]+[larr[0]])
        ll.sort()
        ls=[]
        for line in ll:
            ls.append(" ".join([line[-1]] + line[0:-1]))
        return ls + nl

x=Solution()

q = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
e = ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]
print "Question",q
print "Expect",e
a = x.reorderLogFiles(q)
print "Result",a
print e==a
