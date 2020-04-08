# 526、优美的排列
> tag: python3 、 回溯算法

***
### 题目描述

&emsp;&emsp;假设有从 `1` 到 `N` 的 `N` 个整数，如果从这 `N` 个数字中成功构造出一个数组，使得数组的第 `i` 位 `(1 <= i <= N)` 满足如下两个条件中的一个，我们就称这个数组为一个优美的排列。条件：

1. 第 `i` 位的数字能被 `i` 整除
2. `i` 能被第 `i` 位上的数字整除

&emsp;&emsp;现在给定一个整数 `N`，请问可以构造多少个优美的排列？

### 示例1

```
  输入: 2
  输出: 2
  解释:

  第 1 个优美的排列是 [1, 2]:
    第 1 个位置（i=1）上的数字是1，1能被 i（i=1）整除
    第 2 个位置（i=2）上的数字是2，2能被 i（i=2）整除

  第 2 个优美的排列是 [2, 1]:
    第 1 个位置（i=1）上的数字是2，2能被 i（i=1）整除
    第 2 个位置（i=2）上的数字是1，i（i=2）能被 1 整除
```

**说明**：

&emsp;&emsp;`N` 是一个正整数，并且不会超过15。

***
### 题目链接
[526.优美的排列](https://leetcode-cn.com/problems/beautiful-arrangement/)

***
### 题解

* **回溯算法**

  &emsp;&emsp;每次获得 **(当前数组,剩余数字)** 两个数组，初始即为 `[]` 和 `list(range(1,N+1))`。随后每次取一个一个数字，在剩余数字的数组中寻找当前要添加至当前数组中的第 `i` 位数，如果满足能被 `i` 整除或能整除 `i`，便将其加入至当前数组中，从剩余数字中去除。当剩余数字为空时说明已经达到了优美数组的要求，则统计变量加一。

  ```python
  class Solution:
      def __init__(self):
          self.res = 0

      def countArrangement(self, N: int) -> int:
          def count(l, res_l):
              lenth = len(l) + 1
              if res_l == []:
                  self.res += 1
                  return
              for i in res_l:
                  if i % lenth == 0 or lenth % i == 0:
                      tmp, tmp_res = l[:], res_l[:]
                      tmp.append(i)
                      tmp_res.remove(i)
                      count(tmp, tmp_res)
          count([], list(range(1, N+1)))
          return self.res
  ```

  &emsp;&emsp;最终结果，*运行时间1080ms*，超过70.52%；*占用内存13.7MB*，超过25.00%。

  > 要注意其中创建临时变量的时候不能直接 tmp = l，这样只是创建了一个新的指向 l 地址的指针，当其改变时原数组也会改变，我们需要的是 l 数组的一个复制
