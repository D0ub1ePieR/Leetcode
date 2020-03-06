# python3
# simple
# 数学
# 40ms 43.39%
# 13.4MB 14.96%

class Solution:
    def isUgly(self, num: int) -> bool:
        if num == 0:
            return False
        while num % 2 == 0:
            num /= 2
        while num % 3 == 0:
            num /= 3
        while num % 5 == 0:
            num /= 5
        return num == 1
