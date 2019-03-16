class Solution(object):
    def circleWorks(self,gas,cost,startat):
        tank=0
        for ii in range(len(gas)):
            tank+=gas[(ii+startat)%len(gas)]-cost[(ii+startat)%len(gas)]
            if tank < 0:
                return False
        return True

    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        for ii in range(len(gas)):
            if self.circleWorks(gas,cost,ii):
                return ii
        return -1


x=Solution()


q1 = [1,2,3,4,5]
q2 = [3,4,5,1,2]
e = 3
print "Question",q1,q2
print "Expect",e
a = x.canCompleteCircuit(q1,q2)
print "Result",a
print e==a

q1 = [2,3,4]
q2 = [3,4,3]
e = -1
print "Question",q1,q2
print "Expect",e
a = x.canCompleteCircuit(q1,q2)
print "Result",a
print e==a
