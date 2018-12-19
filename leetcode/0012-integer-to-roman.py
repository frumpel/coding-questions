class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        map={
            "M":1000,
            "D":500,
            "C":100,
            "L":50,
            "X":10,
            "V":5,
            "I":1,
            " ":0
        }
        s+=" "
        num=0
        ptr=0
        while ptr < len(s)-1:
            if map[s[ptr+1]] > map[s[ptr]]:
                num+=map[s[ptr+1]]-map[s[ptr]]
                ptr+=1
            else:
                num+=map[s[ptr]]
            ptr+=1
        return num

    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str

        I can be placed before V (5) and X (10) to make 4 and 9.
        X can be placed before L (50) and C (100) to make 40 and 90.
        C can be placed before D (500) and M (1000) to make 400 and 900.
        """
        if num < 1:
            return ""
        s=""
        # Thousands
        t=num//1000
        s+="M"*t;
        num-=(t*1000)

        # hundreds
        t=num//100
        if t==9:
            s+="CM"
        elif t>=5 and t<9:
            s+="D"+"C"*(t-5)
        elif t==4:
            s+="CD"
        else:
            s+="C"*(t)
        num-=(t*100)

        # tens
        t=num//10
        if t==9:
            s+="XC"
        elif t>=5 and t<9:
            s+="L"+"X"*(t-5)
        elif t==4:
            s+="XL"
        else:
            s+="X"*(t)
        num-=(t*10)

        # ones
        t=num
        if t==9:
            s+="IX"
        elif t>=5 and t<9:
            s+="V"+"I"*(t-5)
        elif t==4:
            s+="IV"
        else:
            s+="I"*(t)
        num-=(t*10)

        return s

x=Solution()

qa={
1:"I",
2:"II",
3:"III",
4:"IV",
5:"V",
6:"VI",
7:"VII",
8:"VIII",
9:"IX",
10:"X",
49:"XLIX",
1499:"MCDXCIX"
}

# for q in qa:
#     e = qa[q]
#     a = x.intToRoman(q)
#     print "Question",q
#     print "Expect",e
#     print "Result",a
#     print e==a

for e in qa:
    q = qa[e]
    a = x.romanToInt(q)
    print "Question",q
    print "Expect",e
    print "Result",a
    print e==a
