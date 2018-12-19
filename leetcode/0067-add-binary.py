
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str

        a b c - c n
        0 0 0   0 0
        0 1 0   0 1
        1 0 0   0 1
        1 1 0   1 0

        0 0 1   0 1
        0 1 1   1 0
        1 0 1   1 0
        1 1 1   1 1

        a&b&c | a&b&!c | a&!b&c | !a&b&c
        o1 a&b | c&(a&!b | !a&b)
           a&b | c&(a^b)
        o2 (a&b) | (a&c) | (b&c)
        """
        l=max(len(a),len(b))
        a=("0"*(l-len(a)) + a)[::-1]
        b=("0"*(l-len(b)) + b)[::-1]
        bc=0
        r=""
        for ii in range(l):
            print "ii",ii
            ba=int(a[ii])
            bb=int(b[ii])
            print "...",ba,bb,bc

            bn=ba^bb^bc
            bc=(ba&bb)|(ba&bc)|(bb&bc)
            print "...","...",bn,bc

            r+=str(bn)
        if bc != 0:
            print "bc",bc
            r+=str(bc)
        return r[::-1]

x=Solution()

q1 = "0"
q2 = "0"
e = "0"
print "Question",q1,q2
print "Expect",e
a = x.addBinary(q1,q2)
print "Result",a
print e==a

q1 = "1"
q2 = "0"
e = "1"
print "Question",q1,q2
print "Expect",e
a = x.addBinary(q1,q2)
print "Result",a
print e==a

q1 = "0"
q2 = "1"
e = "1"
print "Question",q1,q2
print "Expect",e
a = x.addBinary(q1,q2)
print "Result",a
print e==a

q1 = "1"
q2 = "1"
e = "10"
print "Question",q1,q2
print "Expect",e
a = x.addBinary(q1,q2)
print "Result",a
print e==a

q1 = "11"
q2 = "11"
e = "110"
print "Question",q1,q2
print "Expect",e
a = x.addBinary(q1,q2)
print "Result",a
print e==a

q1 = "1010"
q2 = "1011"
e = "10101"
print "Question",q1,q2
print "Expect",e
a = x.addBinary(q1,q2)
print "Result",a
print e==a
