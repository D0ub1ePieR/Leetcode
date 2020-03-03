# 172、阶乘后的零
>tag: python 、 数学

***
### 题目描述

&emsp;&emsp;给定一个整数 `n`，返回 `n!` 结果尾数中零的数量。

### 示例1

```
  输入: 3
  输出: 0
  解释: 3! = 6, 尾数中没有零。
```

### 示例2

```
  输入: 5
  输出: 1
  解释: 5! = 120, 尾数中有 1 个零.
```

**说明**: 你算法的时间复杂度应为 `O(log n)`。
***
### 题目链接
[172. 阶乘后的零](https://leetcode-cn.com/problems/factorial-trailing-zeroes/)

***
### 题解

&emsp;&emsp;很简单的一道题，感觉在奥数中也很常见。只需要找到小于 `n` 的所有是 2 和 5 的各幂次的倍数的数个数，并根据指数累加便可，最后取较小的那个值便是末尾零的个数。

```python
  class Solution:
      def trailingZeroes(self, n: int) -> int:
          c_2, c_5 =0, 0
          t = 2
          while t <= n:
              c_2 += n // t
              t *= 2
          t = 5
          while t <= n:
              c_5 += n // t
              t *= 5
          return min(c_2, c_5)
```

&emsp;&emsp;最终结果，*运行时间32ms*，超过77.80%；*占用内存13.4MB*，超过30.69%。
