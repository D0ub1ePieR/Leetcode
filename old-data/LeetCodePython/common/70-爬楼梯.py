import operator
from functools import reduce
class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dt=[n//2,n%2]
        s=0
        while dt[0]>=0:
           if dt[0]>0:
               s+=reduce(operator.mul, range(dt[1] + 1, dt[0] + dt[1] + 1)) /reduce(operator.mul, range(1, dt[0] +1)) 
           else:
               s+=1
           dt[0]-=1
           dt[1]+=2
        return s

t=Solution()
print(t.climbStairs(2))
