class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs==[]:
            return ""
        flex=strs[0]
        for st in strs:
            for i in range(len(flex)):
                if i>=len(st):
                    flex=flex[:i]
                    break
                if st[i]!=flex[i]:
                    flex=flex[:i]
                    break
        return flex
# 79.27
