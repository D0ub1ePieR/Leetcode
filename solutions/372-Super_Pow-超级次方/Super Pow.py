# python3
# medium
# 数学
# 104ms 87.19%
# 13.4MB 37.10%

class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        b = int(''.join([str(x) for x in b]))
        return pow(a, b, 1337)

# 128ms 70.12%
# 13.3MB 38.71%

class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        a %= 1337
        res = 1
        for i in b[:-1]:
            res *= pow(a, i) % 1337
            res = pow(res, 10) % 1337
        res *= pow(a, b[-1]) % 1337
        return res % 1337

# 144ms 53.66%
# 13.3MB 38.71%

class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        res = 1
        a %= 1337
        tmp = a
        if a == 0 or a == 1:
            return a
        for i in b[::-1]:
            if tmp == 0 or tmp == 1:
                break
            if i > 0:
                res *= pow(tmp, i) % 1337
            tmp = pow(tmp, 10) % 1337
        return res % 1337
