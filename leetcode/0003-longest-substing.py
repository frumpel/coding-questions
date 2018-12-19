import time

class Solution(object):
    # Accepted solution O(n)
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        sp=0
        ep=0
        tp=0
        ml=0
        history={}
        while ep<len(s):
            # print "ML:",ml,"SP:",sp,"EP:",ep,history
            if s[ep] in history:
                tp=history[s[ep]]
                # print "backtracking:",ep,s[ep],tp
                while sp <= tp:
                    del(history[s[sp]])
                    sp+=1
                sp=tp+1
            history[s[ep]] = ep
            ml=max(ml,len(history))
            ep+=1
        return ml

    # # This works but is too slow O(n^2)
    # def lengthOfLongestSubstring(self, s):
    #     """
    #     :type s: str
    #     :rtype: int
    #     """
    #     sp=0
    #     ml=0
    #     history=set()
    #     while sp<len(s):
    #         history=set()
    #         for ii in range(sp,len(s)):
    #             if s[ii] in history:
    #                 ml=max(ml,len(history))
    #                 break
    #             history.add(s[ii])
    #         if ii==len(s)-1:
    #             ml=max(ml,len(history))
    #             return ml
    #         sp+=1
    #     return ml


    # # This seemed tempting but it probably still is O(n^2)
    # def lengthOfLongestSubstring(self, s):
    #     """
    #     :type s: str
    #     :rtype: int
    #     """
    #     history=set()
    #     sp=0
    #     ep=0
    #     rp=0
    #     ml=0
    #     while ep<len(s):
    #         print "ML:",ml,"SP:",sp,"EP:",ep,history
    #         if s[ep] in history:
    #             print "backtrack",ep
    #             cl=ep-sp
    #             ml=max(ml,cl)
    #             rp=ep-1
    #             while rp > 0:
    #                 print "ML:",ml,"SP:",sp,"EP:",ep,"RP:",rp,history
    #                 if s[rp] == s[ep]:
    #                     history.remove(s[rp])
    #                     sp=rp+1
    #                     break
    #                 rp-=1
    #                 time.sleep(1)
    #         history.add(s[ep])
    #         ep+=1
    #         time.sleep(1)
    #     return ml




x = Solution()

q = "abcabcbb"
e = 3
a = x.lengthOfLongestSubstring(q)
print "Question",q
print "Expect",e
print "Result",a
print e==a

q = "abcadbcdbb"
e = 4
a = x.lengthOfLongestSubstring(q)
print "Question",q
print "Expect",e
print "Result",a
print e==a

q = "pwwkew"
e = 3
a = x.lengthOfLongestSubstring(q)
print "Question",q
print "Expect",e
print "Result",a
print e==a

q = "a"
e = 1
a = x.lengthOfLongestSubstring(q)
print "Question",q
print "Expect",e
print "Result",a
print e==a

q = "au"
e = 2
a = x.lengthOfLongestSubstring(q)
print "Question",q
print "Expect",e
print "Result",a
print e==a

q = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ "
e = 95
a = x.lengthOfLongestSubstring(q)
print "Question",q
print "Expect",e
print "Result",a
print e==a
