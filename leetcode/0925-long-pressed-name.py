class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        def splitToLettersArray(s):
            if len(s)<1:
                return []
            ret=[]
            ll=ts=s[0]
            na=[]
            for ii in s[1:]:
                if ii == ll:
                    ts+=ii
                else:
                    na.append(ts)
                    ll=ts=ii
            na.append(ts)
            return na

        a1=splitToLettersArray(name)
        a2=splitToLettersArray(typed)

        if len(a1)>len(a2):
            return False
            
        for ii in range(len(a1)):
            if a1[ii][0]!=a2[ii][0] or len(a1[ii])>len(a2[ii]):
                return False
        return True

x=Solution()

q1 = "alex"
q2 = "aaleex"
e = True
print "Question",q1,q2
print "Expect",e
a = x.isLongPressedName(q1,q2)
print "Result",a
print e==a

q1 = "saeed"
q2 = "ssaaedd"
e = False
print "Question",q1,q2
print "Expect",e
a = x.isLongPressedName(q1,q2)
print "Result",a
print e==a

q1 = "pyplrz"
q2 = "ppyypllr"
e = False
print "Question",q1,q2
print "Expect",e
a = x.isLongPressedName(q1,q2)
print "Result",a
print e==a
