class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        s=m+n-2
        t=min(m-1,n-1)
        s1=1
        s2=1
        for i in range(t):
            s1=s1*s
            s=s-1
            s2=s2*t
            t=t-1
        return s1//s2
# 13.10
