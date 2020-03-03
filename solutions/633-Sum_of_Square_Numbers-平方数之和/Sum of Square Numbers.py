# python3
# simple
# 数学
# 68ms 98.43%
# 13.4MB 25.59%

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for i in range(2, int(c ** 0.5)+1):
            if c % i == 0:
                count = 0
                while c % i == 0:
                    count += 1
                    c /= i
                if i % 4 == 3 and count % 2 == 1:
                    return False
        return c % 4 != 3

# 212ms 70.38%
# 13.3MB 30.00%

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for i in range(int(c ** 0.5)+1):
            t = int((c-i*i) ** 0.5)
            if t*t + i*i == c:
                return True
            if t < i:
                break
        return False
