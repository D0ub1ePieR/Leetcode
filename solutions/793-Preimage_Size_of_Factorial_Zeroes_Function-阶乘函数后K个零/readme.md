# 793、阶乘函数后K个零
>tag: python3 、 二分查找

***
### 题目描述

&emsp;&emsp;`f(x)` 是 `x!` 末尾是0的数量。（回想一下 `x! = 1 * 2 * 3 * ... * x`，且 `0! = 1`）

&emsp;&emsp;例如， `f(3) = 0` ，因为 `3! = 6` 的末尾没有0；而 `f(11) = 2` ，因为 `11!= 39916800` 末端有2个0。给定 `K`，找出多少个非负整数 `x` ，有 `f(x) = K` 的性质。

### 示例

```
  示例 1:
  输入:K = 0
  输出:5
  解释: 0!, 1!, 2!, 3!, and 4! 均符合 K = 0 的条件。

  示例 2:
  输入:K = 5
  输出:0
  解释:没有匹配到这样的 x!，符合K = 5 的条件。
```

**注意**：

* `K` 是范围在 `[0, 10^9]` 的整数。

***
### 题目链接
[793. 阶乘函数后K个零](https://leetcode-cn.com/problems/preimage-size-of-factorial-zeroes-function/)

***
### 题解

&emsp;&emsp;首先我们可以明确，返回的结果只可能为 `5` 或者 `0`。因为 `f(x)` 末尾零的数量受 `[0,x]` 中五的因子个数的影响，而每增加五个数则必回增加一个。

* **二分查找**

&emsp;&emsp;考虑到返回值只有两种情况，那么我们就可以想到如果能够找到一个 `x` 使得 `f(x)=K` 那么显然返回 `5`，而如果找不到则返回 `0`。那么这个寻找的范围怎么约束呢，上界可以定为 `K*5+1`，因为假设 `[0,K]` 中都没有因子5，那么 `[0,5*K]` 中则必由 `K` 个因子5则末尾零的个数至少为 `K`；而下界可以定为 `K`，因为假设 `[0,K]` 中每一个数都有因子5，那么末尾零的个数也至多为 `K`。

&emsp;&emsp;随后在这个范围中使用二分查找，寻找 `f(x)=K` 可能的 `x` 的值。其中 `f(x)` 的计算使用 [172. 阶乘后的零](../172-Factorial_Trailing_Zeroes-阶乘后的零) 中的方法。

```python
  class Solution:
      def preimageSizeFZF(self, K: int) -> int:
          start, end = K, K * 5 + 1
          if K == 0:
              return 5
          while start < end:
              mid = (start + end) // 2
              tmp = 5
              s = 0
              while mid >= tmp:
                  s += mid // tmp
                  tmp *= 5
              if s == K:
                  return 5
              elif s < K:
                  start = mid + 1
              else:
                  end = mid - 1
          return 0
```

&emsp;&emsp;最终结果，*运行时间36ms*，超过64.91%；*占用内存13.2MB*，超过52.00%。

* **数学推导**
> 由于github显示的readme中markdown格式好像不支持latex公式，所以可读性有所降低

&emsp;&emsp;对于 `f(x)` 如果我们将 `x` 写做五进制则可以得到 `x = an*5^n + an-1*5^(n-1) + ... + a0*5^0`，设 `ci` 为 `[1, 5^i]` 中因子5的个数。那么 `f(x)= a0c0 + a1c1 + ... + ancn`。不难发现 `ci` 有这样的递推公式 `ci = 5 * ci-1 + 1, c0 = 0`。那么把 `K` 转化为以 `ci` 为底的 `ci` 可变进制数，如果每一位都不超过5，那么这个 `K` 就是可能达到的。

```python
class Solution:
    def preimageSizeFZF(self, K: int) -> int:
        ci = 0
        while ci < K:
            ci = ci * 5 + 1
        while K > 0:
            ci = (ci - 1) / 5
            if K / ci >= 5:
                return 0
            K %= ci
        return 5
```

&emsp;&emsp;最终结果，*运行时间40ms*，超过49.12%；*占用内存13.4MB*，超过52.00%。
