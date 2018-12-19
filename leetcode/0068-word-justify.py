from itertools import chain, izip
class Solution(object):
    def bothJustifyLine(self,words,maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        # Assumption is that if we can't justify both sides we will justify left
        if len(words)==1:
            return words[0]+" "*(maxWidth-len(words[0]))

        clen=len("".join(words))
        nspc=maxWidth-clen
        cspc=len(words)-1
        step=1.0*nspc/cspc

        # # "even" distribution of space
        # spaces=[]
        # for ii in range(cspc):
        #     addcnt=int((ii+1)*step+0.5)-int((ii)*step+0.5)
        #     spaces.append(" "*addcnt)
        # spaces.append("")

        # Left weighted space
        spaces=[""]*cspc
        for ii in range(nspc):
            spaces[ii%cspc]+=" "
        spaces.append("")

        return "".join(list(chain.from_iterable(izip(words,spaces))))

    def leftJustifyLine(self,words,maxWidth):
        if len(words)==1:
            return words[0]+" "*(maxWidth-len(words[0]))

        clen=len("".join(words))
        cspc=len(words)-1
        spaces=[" "]*cspc
        spaces.append("")
        line = "".join(list(chain.from_iterable(izip(words,spaces))))
        return line+" "*(maxWidth-len(line))

    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        # Fit words into lines
        lines=[]
        line=[]
        clen=0
        for word in words:
            # print word,line,lines
            if clen+len(word)+len(line)-1 < maxWidth:
                line.append(word)
                clen+=len(word)
            else:
                lines.append(line)
                line=[word]
                clen=len(word)
        lastline=line

        # Pad lines with spaces
        r=[]
        for line in lines:
            r.append(self.bothJustifyLine(line,maxWidth))
        r.append(self.leftJustifyLine(lastline,maxWidth))
        return r




x=Solution()

q1 = ["This", "is", "an", "example", "of", "text", "justification."]
q2 = 16
e = [
   "This    is    an",
   "example  of text",
   "justification.  "
]
print "Question",q1,q2
print "Expect",e
a = x.fullJustify(q1,q2)
print "Result",a
print e==a


q1 = ["What","must","be","acknowledgment","shall","be"]
q2 = 16
e = [
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
print "Question",q1,q2
print "Expect",e
a = x.fullJustify(q1,q2)
print "Result",a
print e==a

q1 = ["Science","is","what","we","understand","well","enough","to","explain",
         "to","a","computer.","Art","is","everything","else","we","do"]
q2 = 20
e = [
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]
print "Question",q1,q2
print "Expect",e
a = x.fullJustify(q1,q2)
print "Result",a
print e==a
