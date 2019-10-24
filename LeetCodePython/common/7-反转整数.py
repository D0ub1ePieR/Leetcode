class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x>0:
            flag=1
        else:
            flag=-1
        x=str(abs(x))
        l=list(x)
        l.reverse()
        res="".join(l)
        res=int(res)*flag
        if res in range(-pow(2,31),pow(2,31)):
            return res
        else:
            return 0
