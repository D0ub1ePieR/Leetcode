# python3
# simple
# 数学 二分查找
# 40ms 76.50%
# 13.3MB 5.73%

class Solution:
    def arrangeCoins(self, n: int) -> int:
        return math.floor((math.sqrt(0.25+2*n)-0.5))

# 48ms 63.31%
# 13.5MB 5.73%

class Solution:
    def arrangeCoins(self, n: int) -> int:
        return int((math.sqrt(1+8*n)-1)//2)

# 1064ms 26.14%
# 13.6MB 5.73%

class Solution:
    def arrangeCoins(self, n: int) -> int:
        i = 1
        while n - i >= 0:
            n -= i
            i += 1
        return i - 1
