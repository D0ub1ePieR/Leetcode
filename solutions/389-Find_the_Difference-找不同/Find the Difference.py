# python3
# simple
# 位运算 哈希表
# 40ms 69.86%
# 13.7MB 20.00%

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return chr(reduce(lambda x,y: x^y, [ord(i) for i in s+t]))

# 52ms 32.66%
# 13.5MB --.--%

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s, t = list(s), list(t)
        for x in s:
            t.remove(x)
        return t[0]
