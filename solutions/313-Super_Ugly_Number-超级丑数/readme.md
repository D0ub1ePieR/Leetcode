# 313、超级丑数
>tag: python 、 堆 、 数学

***
### 题目描述

&emsp;&emsp;编写一段程序来查找第 `n` 个超级丑数。

&emsp;&emsp;超级丑数是指其所有质因数都是长度为 `k` 的质数列表 `primes` 中的正整数。

### 示例

```
  输入: n = 12, primes = [2,7,13,19]
  输出: 32
  解释: 给定长度为 4 的质数列表 primes = [2,7,13,19]，前 12 个超级丑数序列为：[1,2,4,7,8,13,14,16,19,26,28,32] 。
```

### 说明

* `1` 是任何给定 `primes` 的超级丑数

* 给定 `primes` 中的数字以升序排列

* `0 < k ≤ 100`, `0 < n ≤ 106`, `0 < primes[i] < 1000 `

* 第 `n` 个超级丑数确保在 `32` 位有符整数范围内

***
### 题目链接
[313. 超级丑数](https://leetcode-cn.com/problems/super-ugly-number/)

***
### 题解

* **堆**

&emsp;&emsp;与[丑数II](../264-Ugly_Number_II-丑数II)类似的使用堆处理，只是将其中的 `2,3,5` 变为 `primes` 数组，每次将堆顶元素乘上 `primes` 中的每个值后插入堆中。但是使用 `bisect` 模块会超时，变为使用 `heapq` 模块即可通过。

```python
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        import heapq
        l = [1]
        c = 0
        while c < n - 1:
            t = heapq.heappop(l)
            while l and t == l[0]:
                t = heapq.heappop(l)
            for num in primes:
                heapq.heappush(l, t*num)
            c += 1
        return heapq.heappop(l)
```

&emsp;&emsp;最终结果，*运行时间1764ms*，超过5.22%；*占用内存116.9MB*，超过5.26%。

* **动态规划**

&emsp;&emsp;我们记录 `primes` 中每一个数已经乘到了第几个丑数，令这个数组为 `loc`。显然丑数从小到大的顺序，那么每一个因子也是按照丑数从小到大的顺序与之相乘的。我们每次取 `primes[k] * loc[k]` 中最小的一个，即当前下一个数中所有可能最小的一个，将其加入丑数序列，并进行判断，`ugly_list[i] > primes[j] * loc[j]` 用于排除不同的乘法可能得到的相同的数值，满足条件即将 `loc[j]` 加一。

```python
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        l = [1]
        loc = [0] * len(primes)
        for i in range(1, n):
            l.append(min(x * l[y] for x, y in zip(primes, loc)))
            for j in range(len(primes)):
                if l[i] >= primes[j] * l[loc[j]]:
                    loc[j] += 1
        return l[-1]
```

&emsp;&emsp;最终结果，*运行时间1028ms*，超过52.75%；*占用内存17.3MB*，超过44.21%。

* **两者结合**

&emsp;&emsp;将动态规划的 `loc` 数组与堆的存储方式相结合，可以得到。

```python
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        import heapq
        l = [1]
        loc = [0] * len(primes)
        heap = []
        visited = set()
        for index, num in enumerate(primes):
            heapq.heappush(heap, [num, index])
            visited.add(num)
        for i in range(1, n):
            t, k = heapq.heappop(heap)
            l.append(t)
            while primes[k] * l[loc[k]] in visited:
                loc[k] += 1
            heapq.heappush(heap, [primes[k]*l[loc[k]], k])
            visited.add(primes[k]*l[loc[k]])
        return l[-1]
```

&emsp;&emsp;最终结果，*运行时间328ms*，超过91.21%；*占用内存25.1MBMB*，超过41.05%。达到了比两种方法更好的结果。
