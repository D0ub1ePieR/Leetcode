from math import pow
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag=''
        if x<0:
            x=abs(x)
            flag='-'
        x=list(str(x))
        x.reverse()
        x.insert(0,flag)
        if -pow(2,31)<=int(''.join(x))<pow(2,31):
            return int(''.join(x))
        else:
            return 0

t=Solution()
print(t.reverse(123))

# 93.78
