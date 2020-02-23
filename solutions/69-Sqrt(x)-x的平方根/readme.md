# 69. x的平方根
> tag: python 、 数学 、 二分查找
***
### 题目描述

&emsp;&emsp;实现 `int sqrt(int x)` 函数。

&emsp;&emsp;计算并返回 `x` 的平方根，其中 `x` 是非负整数。

&emsp;&emsp;由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

### 示例1
```
  输入: 4
  输出: 2
```

### 示例2
```
  输入: 8
  输出: 2
  说明: 8 的平方根是 2.82842...,
       由于返回类型是整数，小数部分将被舍去。
```

***
### 题目链接
[69. x的平方根](https://leetcode-cn.com/problems/sqrtx/)
***
### 题解
* **库函数**

&emsp;&emsp;可以<del>很不要脸得</del>使用 `math.sqrt` 函数，后台并没有禁用这个功能。

&emsp;&emsp;最终结果，*运行时间60ms*，超过19.30%；*占用内存13.5MB*，超过37.46%。

* **牛顿法迭代**

&emsp;&emsp;可以利用公式 `Xn+1 = (Xn + x / Xn) / 2` 进行推导，最终该式会收敛于 `x的平方根`。当 `Xn+1` 与 `Xn` 都属于 `[n, n+1)`时，则可以得到结果返回 `n`。( `X1 = 1 或 x` 都可)

```python
  class Solution:
      def mySqrt(self, x: int) -> int:
          if x < 2:
              return x
          xn = 1
          while abs(xn - 0.5*(xn+x/xn)) >= 1:
              xn = 0.5 * (xn + x/xn)
          return int(xn)
```

&emsp;&emsp;最终结果，*运行时间52ms*，超过32.71%；*占用内存13.5MB*，超过37.46%。

* **二分法**

&emsp;&emsp;在区间 `[0, x]` 中寻找 `x` 的平方根，使用二分法进行查找。

```python
  class Solution:
      def mySqrt(self, x: int) -> int:
          start, end = 0, x
          while start <= end:
              mid = (start + end) // 2
              if mid * mid > x:
                  end = mid - 1
              elif mid * mid < x:
                  start = mid + 1
              else:
                  return mid
          return end
```

&emsp;&emsp;最终结果，*运行时间44ms*，超过54.50%；*占用内存13.4MB*，超过37.51%。
