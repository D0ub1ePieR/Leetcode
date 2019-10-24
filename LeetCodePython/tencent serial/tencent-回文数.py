class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x=str(x)
        i=0
        j=len(x)-1
        while i<j:
            if x[i]!=x[j]:
                return False
            i+=1
            j-=1
        return True
# 96.42
