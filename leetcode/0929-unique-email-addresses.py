import re

class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        unique_emails=set()
        for email in emails:
            x = re.search("^([^+@]+)(\+[^@]+)?@(.+)$",email)
            if x:
                name=re.sub("\.","",x.group(1))
                domain=x.group(3)
                unique_emails.add(name+"@"+domain)
        return len(unique_emails)

x=Solution()

q = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
e = 2
print "Question",q
print "Expect",e
a = x.numUniqueEmails(q)
print "Result",a
print e==a
