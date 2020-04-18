# 389、找不同
> tag: python3 、 位运算 、 哈希表

***
### 题目描述

&emsp;&emsp;给定两个字符串 **s** 和 **t**，它们只包含小写字母。

&emsp;&emsp;字符串 **t** 由字符串 **s** 随机重排，然后在随机位置添加一个字母。

&emsp;&emsp;请找出在 **t** 中被添加的字母。

### 示例

```
  输入：
  s = "abcd"
  t = "abcde"

  输出：
  e

  解释：
  'e' 是那个被添加的字母。
```

***
### 题目链接
[389.找不同](https://leetcode-cn.com/problems/find-the-difference/)

***
### 题解

* **一行 - 位运算**

  如果我们将 `s` 和 `t` 放在一起考虑，那么就和 [只出现一次的数字](../136-Single_Number-只出现一次的数字) 类似，进行异或操作最终得到的结果即是添加的字母，但是字符并不能直接进行异或，那么我们就可以首先将其转换为 **ASCII** 码，最终再转回字符。

  ```python
  class Solution:
      def findTheDifference(self, s: str, t: str) -> str:
          return chr(reduce(lambda x,y: x^y, [ord(i) for i in s+t]))
  ```

  &emsp;&emsp;最终结果，*运行时间40ms*，超过69.86%；*占用内存13.7MB*，超过20.00%。

* **数组**

  我们可以将 `s` 和 `t` 转换为数组，随后将 `s` 中出现的元素都在 `t` 中移除，最终 `t` 剩下来的元素即为添加的字母。

  ```python
  class Solution:
      def findTheDifference(self, s: str, t: str) -> str:
          s, t = list(s), list(t)
          for x in s:
              t.remove(x)
          return t[0]
  ```

  &emsp;&emsp;最终结果，*运行时间52ms*，超过32.66%；*占用内存13.5MB*，超过--.--%。
