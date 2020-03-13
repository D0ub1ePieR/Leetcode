# 264、丑数II
> tag: python3 、 堆 、 数学 、 动态规划

***
### 题目描述

&emsp;&emsp;编写一个程序，找出第 `n` 个丑数。

&emsp;&emsp;丑数就是只包含质因数 `2, 3, 5` 的 **正整数**。

### 示例

```
  输入: n = 10
  输出: 12
  解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
```

### 说明

1. `1` 是丑数。

2. `n` 不超过1690。

***
### 题目链接
[264. 丑数II](https://leetcode-cn.com/problems/ugly-number-ii/)

***
### 题解

* **堆**

&emsp;&emsp;可以发现根据定义所有的丑数都是 `2,3,5` 的倍数，而规定了 `1` 又是丑数，则可以建立一个**堆**，初始只有一个元素 `1`，每次向堆中添加第 `i` 个元素的 `2,3,5` 倍中没有出现过的数。随后 `i = i + 1`，由于堆的性质，可以得到 `i` 对应的便是第 `i` 小的元素，当 `i` 到 `n - 1` 时，就可以得到第 `n` 个丑数(次数堆中元素的个数大于等于 `n`)。

```python
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        l = [1]
        c = 0
        while c < n-1:
            if l[c] * 2 not in l:
                bisect.insort(l, l[c]*2)
            if l[c] * 3 not in l:
                bisect.insort(l, l[c]*3)
            if l[c] * 5 not in l:
                bisect.insort(l, l[c]*5)
            c += 1
        return l[c]
```

&emsp;&emsp;最终结果，*运行时间3052ms*，超过5.03%；*占用内存13.6MB*，超过5.35%。

* **奇特优化**

&emsp;&emsp;可以发现使用以上的方法十分得慢，观察了*官方题解*发现。由于题目给定了 `n` 不会超过1690，那么我们就可以提前计算出前1690个丑数，以备每一个样例使用。这里虽然一下子计算1690个数一定需要较长时间，但是如果测试用例较多，能够保证计算一次所有样例使用的话就能比每一个样例计算一次的别的算法的时间来的更短。

&emsp;&emsp;这里在 `Solution` 类外又定义了一个丑数类 `Ugly` 类，在 `Solution` 类构造时调用 `Ugly` 类，计算出前 1690 个丑数。随后在所有测试用例执行时，调用 `Solution` 类的 `nthUglyNumber` 函数，就可以调用到其私有变量直接查询第 `n` 个丑数是多少。

```python
class Ugly:
    def __init__(self):
        self.nums = [1]
        for i in range(1691):
            if self.nums[i] * 2 not in self.nums:
                bisect.insort(self.nums, self.nums[i]*2)
            if self.nums[i] * 3 not in self.nums:
                bisect.insort(self.nums, self.nums[i]*3)
            if self.nums[i] * 5 not in self.nums:
                bisect.insort(self.nums, self.nums[i]*5)

class Solution:
    u = Ugly()
    def nthUglyNumber(self, n: int) -> int:
        return self.u.nums[n-1]
```

&emsp;&emsp;最终结果，*运行时间108ms*，超过96.62%；*占用内存13.7MB*，超过5.02%。可以发现一下子效率得到了很大幅度的提升，虽然单个用例使用页面上 *执行代码* 测试时(尤其是 `n` 较小时)花的时间会更多，但是当用例增多时，优势便能体现出来。
