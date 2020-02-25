# python3
# medium
# 数字 二分查找
# 32ms 76.74%
# 13.4MB 32.14%

class Solution:
    def myPow(self, x: float, n: int) -> float:
            if n == 0:
                return 1
            res = 1
            if n < 0:
                n = abs(n)
                x = 1 / x
            b = reversed(str(bin(n))[2:])
            tmp = x
            for i in b:
                if i == '1':
                    res *= tmp
                tmp = tmp * tmp
            return res

# 32ms 76.74%
# 13.4MB 32.14%

class Solution:
    def myPow(self, x: float, n: int) -> float:
            def mypow(x, n):
                if n == 1:
                    return x
                t = mypow(x, n//2)
                if n % 2 == 1:
                    return t*t*x
                else:
                    return t*t
            if n == 0:
                return 1
            if n < 0:
                x = 1 / x
                n = abs(n)
            return mypow(x, n)
