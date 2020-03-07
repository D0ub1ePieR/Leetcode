# 202、 快乐数
> tag: python3 、 哈希表 、 数学

***
### 题目描述

&emsp;&emsp;编写一个算法来判断一个数是不是“快乐数”。

&emsp;&emsp;一个“快乐数”定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，然后重复这个过程直到这个数变为 `1`，也可能是无限循环但始终变不到 `1`。如果可以变为 `1`，那么这个数就是快乐数。

### 示例

```
  输入: 19
  输出: true
  解释:
  12 + 92 = 82
  82 + 22 = 68
  62 + 82 = 100
  12 + 02 + 02 = 1
```

***
### 题目链接
[202. 快乐数](https://leetcode-cn.com/problems/happy-number/)

***
### 题解

* **循环加集合**

&emsp;&emsp;每次计算当前数的各位数平方和，并更新当前数，将每个结果加入集合中，如果当前数为 `1`，则返回 `True`，如果集合中已有相同数，则返回 `False`。

```python
  class Solution:
      def isHappy(self, n: int) -> bool:
          record = []
          while 1:
              s = sum([int(x)**2 for x in str(n)])
              if s == 1:
                  return True
              if s in record:
                  return False
              record.append(s)
              n = s
```

&emsp;&emsp;最终结果，*运行时间48ms*，超过31.73%；*占用内存13.4MB*，超过15.50%。

* **快慢指针**

&emsp;&emsp;可以发现无论是否 `n` 为快乐数，最终都会产生一个循环，只是循环是否为 `1` 的区别。那么我们就可以通过两个指针使用不同的步长向前进来判断循环周期。我们设置一个慢指针每次前进一步，快指针每次前进两步，那么就相当于不断增加周期的长度进行判断是否产生了循环，产生了循环后判断是否由 `1` 产生并返回结果。

```python
  class Solution:
      def isHappy(self, n: int) -> bool:
          def cal_sum(num):
              s = sum([int(x)**2 for x in str(num)])
              # s = 0
              # while num != 0:
              #    s += (num % 10) ** 2
              #    num //= 10
              # return s
          slow = fast = n
          while 1:
              slow = cal_sum(slow)
              fast = cal_sum(cal_sum(fast))
              if slow == fast:
                  break
          return slow == 1
```

&emsp;&emsp;最终结果，*运行时间56ms*，超过18.34%；*占用内存13.4MB*，超过15.50%。方法很妙，但是效果不及的原因我觉得是因为当循环产生由于 `1` 时，需要慢指针也到达 `1`。同时尝试了两种求各位数和的方法，发现还是转换为字符串的拆分求和更为迅速，相比使用循环每次拆除一位计算。
