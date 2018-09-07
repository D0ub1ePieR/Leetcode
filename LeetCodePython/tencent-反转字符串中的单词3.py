class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        a=s.split(' ')
        for i in range(len(a)):
            a[i]=a[i][::-1]
        return ' '.join(a)
# 31.75
