# python3
# simple
# 数学 二分查找
# 32ms 75.78%
# 13.2MB 30.39%

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return num ** 0.5 == int(num ** 0.5)

# 40ms 39.32%
# 13.6MB 27.84%

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        s = 1
        res = 0
        while res < num:
            res += s
            s += 2
        if res == num:
            return True
        else:
            return False

# 40ms 39.32%
# 13.6MB 30.20%

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        mid = num // 2
        while mid * mid > num:
            mid = (mid + num // mid) // 2
        return num == 1 or mid * mid == num
