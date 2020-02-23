# python3
# simple
# 数学 二分查找
# 44ms 54.50%
# 13.4MB 37.51%

class Solution:
    def mySqrt(self, x: int) -> int:
        start, end = 0, x
        while start <= end:
            mid = (start + end) // 2
            if mid * mid > x:
                end = mid - 1
            elif mid * mid < x:
                start = mid + 1
            else:
                return mid
        return end

# 52ms 32.71%
# 13.5MB 37.46%

class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        xn = 1
        while abs(xn - 0.5*(xn+x/xn)) >= 1:
            xn = 0.5 * (xn + x/xn)
        return int(xn)

# 60ms 19.30%
# 13.5MB 37.46%

class Solution:
    def mySqrt(self, x: int) -> int:
        return int(math.sqrt(x))
