# 279、完全平方数
> tag: python3 、 数学 、 动态规划 、 广度优先搜索

***
### 题目描述

&emsp;&emsp;给定正整数 `n`，找到若干个完全平方数（比如 `1, 4, 9, 16, ...`）使得它们的和等于 `n`。你需要让组成和的完全平方数的个数最少。

### 示例1

```
  输入: n = 12
  输出: 3
  解释: 12 = 4 + 4 + 4.
```

### 示例2

```
  输入: n = 13
  输出: 2
  解释: 13 = 4 + 9.
```

***
### 题目链接
[279. 完全平方数](https://leetcode-cn.com/problems/perfect-squares/)

***
### 题解

* **动态规划**

  &emsp;&emsp;首先初始化长度为 `n+1` 的数组，其中 `dp[i] = i`，即每一个数都由 `1` 相加得来。随后逐个遍历，对于 `j*j <= i`，令 `dp[i] = min(dp[i], dp[i-j*j]+1)`，保证 `i` 之前所有的值都是最小的，那么其后由前面的值组成的新的值也是最小的。最后返回 `dp[-1]`。

  ```python
    class Solution:
        def numSquares(self, n: int) -> int:
            dp = [i for i in range(n+1)]
            for i in range(n+1):
                for j in range(math.floor(i**0.5)+1):
                    dp[i] = min(dp[i], dp[i-j*j]+1)
            return dp[-1]
  ```

  &emsp;&emsp;最终结果，*运行时间5916ms*，超过26.23%；*占用内存13.8MB*，超过20.76%。可以发现用时十分的长，主要原因我觉得是这种方法实际上计算了所有 `[0, n]` 的结果，远大于目标期望。

* **BFS**

  &emsp;&emsp;对于 `n` 来说和构成它的值的可能是有限的，只有 `[1, 4, ..., int(n**0,5)]` ，那么就可以每一步穷举当前值减去这所有可能的结果(即广度优先)，并将结果去重放入队列，最终出现 `0` 则停止并返回步数。例如

  - n = 10

  - step = 0, queue = [11], visited = [11]

  - step = 1, queue = [10, 7, 2], visited = [11, 10, 7, 2]

  - step = 2, queue = [9, 6, 1, <del>6</del>, 3, <del>1</del>], visited = [11, 10, 7, 2, 9, 6, 1, 3]

  - step = 3, queue = [..., 0, ...]

  - return step=3

  ```python
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
  ```

  &emsp;&emsp;最终结果，*运行时间556ms*，超过73.84%；*占用内存14.3MB*，超过11.18%。
