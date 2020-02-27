# 367、有效的完全平方数
> tag: python3 、 数学

***
### 题目描述

&emsp;&emsp;给定一个正整数 `num`，编写一个函数，如果 `num` 是一个完全平方数，则返回 `True`，否则返回 `False`。

&emsp;&emsp;**说明**：不要使用任何内置的库函数，如 `sqrt`。

### 示例1

```
  输入：16
  输出：True
```

### 示例2

```
  输入：14
  输出：False
```

***
### 题目链接
[367. 有效的完全平方数](https://leetcode-cn.com/problems/valid-perfect-square/)

***
### 题解

* **二分法**

&emsp;&emsp;很显然当 `n > 2` 时， `n` 的平方根一定是小于 `n / 2` 的，于是我们便可以将上界定位 `n / 2` 使用二分法进行寻找最接近 `n` 的平方根的整数，最后判断该整数是否为其平方根。为了加快区间缩小，我们可以将区间定位 `(mid, n // mid)` 或 `(n // mid, mid)` 同时收缩上下界。

```python
  class Solution:
      def isPerfectSquare(self, num: int) -> bool:
          mid = num // 2
          while mid * mid > num:
              mid = (mid + num // mid) // 2
          return num == 1 or mid * mid == num
```

&emsp;&emsp;最终结果，*运行时间40ms*，超过39.32%；*占用内存13.6MB*，超过30.20%。

* **累加求平方数**

&emsp;&emsp;我们可以发现 `1 + 3 + 5 + ...` 这个式子产生的结果都为完全平方数 `1, 4, 9, 16` ，那么我们就可以不断得将奇数累加，直到和大于 `n` 了则返回 `False` ，如果正好等于 `n` ，那么则返回 `True`。

```python
  class Solution:
      def isPerfectSquare(self, num: int) -> bool:
          s = 1
          res = 0
          while res < num:
              res += s
              s += 2
          if res == num:
              return True
          else:
              return False
```

&emsp;&emsp;最终结果，*运行时间40ms*，超过39.32%；*占用内存13.6MB*，超过30.20%。

* <del>**奇怪的方法**</del>

&emsp;&emsp;题目规定不适用 `sqrt`，但是我们还是可以使用 `n ** 0.5` 的方式计算 `1 / 2` 次方。不过我觉得还是不符合题意的。

```python
  class Solution:
      def isPerfectSquare(self, num: int) -> bool:
          return num ** 0.5 == int(num ** 0.5)
```

&emsp;&emsp;最终结果，*运行时间32ms*，超过75.78%；*占用内存13.2MB*，超过30.39%。这么一看，在基础功能面前一切花里胡哨都是比不过内置的。
