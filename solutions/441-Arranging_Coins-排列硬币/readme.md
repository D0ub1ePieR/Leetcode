# 441、排列硬币
>tag: python 、 数学 、 二分查找

***
### 题目描述

&emsp;&emsp;你总共有 `n` 枚硬币，你需要将它们摆成一个阶梯形状，第 `k` 行就必须正好有 `k` 枚硬币。

&emsp;&emsp;给定一个数字 `n`，找出可形成完整阶梯行的总行数。

&emsp;&emsp;`n` 是一个非负整数，并且在32位有符号整型的范围内。

### 示例1

```
  n = 5

  硬币可排列成以下几行:
  ¤
  ¤ ¤
  ¤ ¤

  因为第三行不完整，所以返回2.
```

### 示例2

```
  n = 8

  硬币可排列成以下几行:
  ¤
  ¤ ¤
  ¤ ¤ ¤
  ¤ ¤

  因为第四行不完整，所以返回3.
```

***
### 题目链接
[441. 排列硬币](https://leetcode-cn.com/problems/arranging-coins/)

***
### 题解

* **循环**

&emsp;&emsp;由 `1` 开始逐渐与 `n` 相减，直到小于 `0`。

```python
class Solution:
    def arrangeCoins(self, n: int) -> int:
        i = 1
        while n - i >= 0:
            n -= i
            i += 1
        return i - 1
```

&emsp;&emsp;最终结果，*运行时间1064ms*，超过26.14%；*占用内存13.6MB*，超过5.73%。

* **公式**

&emsp;&emsp;我们可以发现最终结果 `k` 一定满足 `k(k+1)/2 <= n`，实际上就是求满足 `k^2 + k - 2n <= 0` 的最大正整数。那就可以转换为 `k^2 + k - 2n = 0` 的较大解向下取整。

```python
class Solution:
    def arrangeCoins(self, n: int) -> int:
        return int((math.sqrt(1+8*n)-1)//2)
```

&emsp;&emsp;最终结果，*运行时间48ms*，超过63.31%；*占用内存13.5MB*，超过5.73%。

&emsp;&emsp;还可以做一些细小的优化，即简化一下运算

```python
    return math.floor((math.sqrt(0.25+2*n)-0.5))
```

&emsp;&emsp;最终结果，*运行时间40ms*，超过76.50%；*占用内存13.5MB*，超过5.73%。
