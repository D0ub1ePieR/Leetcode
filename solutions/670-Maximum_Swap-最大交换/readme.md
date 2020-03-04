# 670、最大交换
> tag: python3 、 数组 、 数学

***
### 题目描述

&emsp;&emsp;给定一个非负整数，你**至多**可以交换一次数字中的任意两位。返回你能得到的最大值。

### 示例1

```
  输入: 2736
  输出: 7236
  解释: 交换数字2和数字7。
```

### 示例2

```
  输入: 9973
  输出: 9973
  解释: 不需要交换。
```

**注意**:

1. 给定数字的范围是 `[0, 10^8]`

***
### 题目链接
[670. 最大交换](https://leetcode-cn.com/problems/maximum-swap/)

***
### 题解

* **暴力法**

&emsp;&emsp;题目描述数字范围 `[0, 10^8]`，也就是说最多只有8位数字，最多只有 `8*7/2=28` 种交换的情况。那么就可以穷举这些可能，保留最大的结果并返回。

* **贪心**

&emsp;&emsp;主要思想便是从最高位开始比较需要保证由高到低的位数需要按照组成这个数的数字的降序排列，直到第一个不同的值出现，将其与这个数最后一次出现的位置交换(*如果这个第 `n` 大的值出现多次则需要降低这个交换过去的较小的值的影响，就是让它与更低位的交换*)。

```python
  class Solution:
      def maximumSwap(self, num: int) -> int:
          numbers = list(str(num))
          sort_num = sorted(numbers[:])
          sort_num.reverse()  # 降序排列的原数数字序列
          reverse_num = numbers[:]
          reverse_num.reverse() # 用于寻找最后一次出现不合降序的值的位置
          for i in range(len(numbers)):
              if numbers[i] != sort_num[i]:
                  # 出现不是当前可能的最大值的情况
                  index = reverse_num.index(sort_num[i])
                  t = numbers[-(index+1)]   # 交换
                  numbers[-(index+1)] = numbers[i]
                  numbers[i] = t
                  break
          return int(''.join(numbers))
```

&emsp;&emsp;最终结果，*运行时间32ms*，超过75.33%；*占用内存13.4MB*，超过28.13%。我这样写有一点就是复制的数组过多导致占用内存更多。
