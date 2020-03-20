# python3
# medium
# 动态规划 广度优先搜索 数学
# 556ms 73.84%
# 14.3MB 11.18%

class Solution:
    def numSquares(self, n: int) -> int:
        from collections import deque
        if n == 0:
            return 0
        queue = deque([n])
        step = 0
        visited = set()
        while queue:
            step += 1
            l = len(queue)
            for i in range(l):
                tmp = queue.pop()
                for j in range(1,math.floor(tmp**0.5)+1):
                    x = tmp - j**2
                    if x == 0:
                        return step
                    if x not in visited:
                        queue.appendleft(x)
                        visited.add(x)
        return step

# 5916ms 26.23%
# 13.8MB 20.76%

class Solution:
    def numSquares(self, n: int) -> int:
        dp = [i for i in range(n+1)]
        for i in range(n+1):
            for j in range(math.floor(i**0.5)+1):
                dp[i] = min(dp[i], dp[i-j*j]+1)
        return dp[-1]
