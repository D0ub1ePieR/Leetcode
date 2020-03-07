# python3
# simple
# 数学
# 36ms 68.98%
# 13.2MB 15.63%

class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            num = sum([int(x) for x in str(num)])
        return num

# 36ms 68.98%
# 13.2MB 15.63%

class Solution:
    def addDigits(self, num: int) -> int:
        return (1 + (num - 1) % 9) * int(num != 0)
