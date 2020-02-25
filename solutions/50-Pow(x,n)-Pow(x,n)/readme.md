# 50、Pow(x, n)
> tag: python3 、 数学 、 二分查找

***
### 题目描述

&emsp;&emsp;实现 `pow(x, n)` ，即计算 `x` 的 `n` 次幂函数

### 示例1

```
  输入: 2.00000, 10
  输出: 1024.00000
```

### 示例2

```
  输入: 2.10000, 3
  输出: 9.26100
```

### 示例3

```
  输入: 2.00000, -2
  输出: 0.25000
  解释: 2-2 = 1/22 = 1/4 = 0.25
```

###说明

* -100.0 < x < 100.0
* `n` 是32位有符号整数，其数值范围是 `[-2^31, 2^31-1]`

***
### 题目链接
[50.Pow(x, n)](https://leetcode-cn.com/problems/powx-n/)

***
### 题解
* **递归方法**

&emsp;&emsp;计算 `x` 的 `n` 次幂显然不能将 `n` 个 `x`相乘，那么我们发现可以将 `x^n` 变为 `(x^(n//2))^2` 或 `(x^(n//2))^2 * x` 分别对应 `n` 为偶数和奇数的情况。那么我们就可以将计算一直进行拆分产生递归操作，知道幂指数为 **1** 时直接返回 `x`。在这之前首先将 `n = 0` 的情况直接返回结果 `1`，`n < 0` 的情况将 `x = 1 / x`，`n` 变为正。

```python
  class Solution:
      def myPow(self, x: float, n: int) -> float:
              def mypow(x, n):
                  if n == 1:
                      return x
                  t = mypow(x, n//2)
                  if n % 2 == 1:
                      return t*t*x
                  else:
                      return t*t
              if n == 0:
                  return 1
              if n < 0:
                  x = 1 / x
                  n = abs(n)
              return mypow(x, n)
```

&emsp;&emsp;最终结果，*运行时间32ms*，超过76.74%；*占用内存13.4MB*，超过32.14%。

* **循环方法**

&emsp;&emsp;上述方法也可以改为非递归的形式。(*这里经过处理已经使 `n` 为正*)。这里我使用的是将 `n` 转换为 **二进制**，很容易可以看出将每一位单独计算相乘则是最终结果，且每一位所要乘得的数为后一位所要乘的数的平方。

```
  例如： n = 10 时， n = 0b 1010
        x ^ n = (x ^ 8) * 1 * (x ^ 2) * 1 而其中 1 可以忽略
        同时 从右往左 循环时，可以依次计算 x^1 x^2 x^4 ... 不会产生额外操作
```

那么就可以得到

```python
  class Solution:
      def myPow(self, x: float, n: int) -> float:
              if n == 0:
                  return 1
              res = 1
              if n < 0:
                  n = abs(n)
                  x = 1 / x
              b = reversed(str(bin(n))[2:])
              tmp = x
              for i in b:
                  if i == '1':
                      res *= tmp
                  tmp = tmp * tmp
              return res
```

&emsp;&emsp;最终结果，*运行时间32ms*，超过76.74%；*占用内存13.4MB*，超过32.14%。可以发现与递归效率一样。
