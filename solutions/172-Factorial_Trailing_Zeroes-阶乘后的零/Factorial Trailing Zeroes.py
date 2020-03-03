# python3
# simple
# 数学
# 32ms 77.80%
# 13.4 30.69%

class Solution:
    def trailingZeroes(self, n: int) -> int:
        c_2, c_5 =0, 0
        t = 2
        while t <= n:
            c_2 += n // t
            t *= 2
        t = 5
        while t <= n:
            c_5 += n // t
            t *= 5
        return min(c_2, c_5)
