class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l=[]
        maxnum=0
        for ch in s:
            if ch in l:
                l=l[l.index(ch)+1:]
            l.append(ch)
            maxnum=max(maxnum,len(l))
        return maxnum
                
