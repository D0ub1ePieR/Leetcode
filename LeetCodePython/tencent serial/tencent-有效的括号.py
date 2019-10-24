class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left=['(','{','[']
        right={')':'(',']':'[','}':'{'}
        stack=[]
        for i in s:
            if i in left:
                stack.append(i)
            elif stack==[]:
                return False
            elif stack[-1]==right[i]:
                del stack[-1]
            else:
                return False
        if stack==[]:
            return True
        else:
            return False
# 95.55
