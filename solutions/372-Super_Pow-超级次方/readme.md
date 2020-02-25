# 372、超级次方
> tag: python3 、 数学

***
### 题目描述

&emsp;&emsp;你的任务是计算 `a^b` 对 1337 取模，`a` 是一个正整数，`b` 是一个非常大的正整数且会以数组形式给出。

### 示例1

```
  输入: a = 2, b = [3]
  输出: 8
```

### 示例2

```
  输入: a = 2, b = [1,0]
  输出: 1024
```

***
### 题目链接
[372.超级次方](https://leetcode-cn.com/problems/super-pow/)

***
### 题解

* **内置函数**

&emsp;&emsp;<del>很显然 `python` 的特性很好</del>，首先我们使用字符串操作将 `b` 转换为一个完整的数(甚至不需要循环)，随后使用 `pow` 函数并将可选项填写为 `1337` ，最后就**完成了**~

```python
  pow(x,y) => x^y

  pow(x,y,z) => x^y%z
```

可以得到

```python
  class Solution:
      def superPow(self, a: int, b: List[int]) -> int:
          b = int(''.join([str(x) for x in b]))
          return pow(a, b, 1337)
```

&emsp;&emsp;最终结果，*运行时间104ms*，超过87.19%；*占用内存13.4MB*，超过37.10%。可以发现竟然格外地迅速。

* **快速幂**

&emsp;&emsp;与[50.Pow(x, n)](../50-Pow(x,n)-Pow(x,n))类似的，即每次处理一位并累乘。我们可以从高位向低位计算

```python
  class Solution:
      def superPow(self, a: int, b: List[int]) -> int:
          a %= 1337
          res = 1
          for i in b[:-1]:
              res *= pow(a, i) % 1337
              res = pow(res, 10) % 1337
          res *= pow(a, b[-1]) % 1337
          return res % 1337
```

&emsp;&emsp;最终结果，*运行时间128ms*，超过70.12%；*占用内存13.3MB*，超过38.71%。

也可以由高位向低位计算

```python
  class Solution:
      def superPow(self, a: int, b: List[int]) -> int:
          res = 1
          a %= 1337
          tmp = a
          if a == 0 or a == 1:
              return a
          for i in b[::-1]:
              if tmp == 0 or tmp == 1:
                  break
              if i > 0:
                  res *= pow(tmp, i) % 1337
              tmp = pow(tmp, 10) % 1337
          return res % 1337
```

&emsp;&emsp;最终结果，*运行时间144ms*，超过53.66%；*占用内存13.3MB*，超过38.71%。
