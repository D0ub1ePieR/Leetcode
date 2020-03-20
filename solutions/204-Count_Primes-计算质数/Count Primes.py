# python3
# simple
# 哈希表 数学
# 108ms 92.78%
# 36.5MB 6.58%

class Solution:
    def countPrimes(self, n: int) -> int:
        if n in [0, 1]:
            return 0
        flag = [0] * n
        flag[0] = flag[1] = 1
        for i in range(int(math.sqrt(n))+1):
            if flag[i] == 0:
                flag[i*i:n:i] = [1] * ((n-1-i*i) // i + 1)
        return flag.count(0)

# 852ms 30.93%
# 24.9MB 68.61%

class Solution:
    def countPrimes(self, n: int) -> int:
        if n in [0, 1]:
            return 0
        flag = [0] * n
        flag[0] = 1
        flag[1] = 1
        for i in range(int(math.sqrt(n))+1):
            if flag[i] == 0:
                k = i
                while k * i < n:
                    flag[k * i] = 1
                    k += 1
        return flag.count(0)

# 928ms 28.13%
# 25.1MB 68.35%

class Solution:
    def countPrimes(self, n: int) -> int:
        if n in [0, 1]:
            return 0
        flag = [0] * n
        flag[0] = 1
        flag[1] = 1
        for i in range(int(math.sqrt(n))+1):
            if flag[i] == 0:
                k = 2
                while k * i < n:
                    flag[k * i] = 1
                    k += 1
        return flag.count(0)

# 1860ms 10.98%
# 25.2MB 68.35%

class Solution:
    def countPrimes(self, n: int) -> int:
        if n in [0, 1]:
            return 0
        flag = [0] * n
        flag[0] = 1
        flag[1] = 1
        for i in range(n):
            if flag[i] == 0:
                k = 2
                while k * i < n:
                    flag[k * i] = 1
                    k += 1
        return flag.count(0)
