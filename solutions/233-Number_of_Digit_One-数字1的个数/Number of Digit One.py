# python3
# hard
# 数学
# 32ms 76.90%
# 13.5MB 6.94%

class Solution:
    def countDigitOne(self, n: int) -> int:
        i = 1
        s = 0
        while i <= n:
            s += n // (i*10) * i + min(i, max(n % (i*10) - i + 1, 0))
            i *= 10
        return s
