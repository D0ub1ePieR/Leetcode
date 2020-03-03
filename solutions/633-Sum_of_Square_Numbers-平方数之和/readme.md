# 633、平方数之和
> tag: python3 、 数学

***
### 题目描述

&emsp;&emsp;给定一个非负整数 `c` ，你要判断是否存在两个整数 `a` 和 `b`，使得 `a2 + b2 = c`。

### 示例1

```
  输入: 5
  输出: True
  解释: 1 * 1 + 2 * 2 = 5
```

### 示例2

```
  输入: 3
  输出: False
```

***
### 题目链接
[633. 平方数之和](https://leetcode-cn.com/problems/sum-of-square-numbers/)

***
### 题解

* **循环判断**

  &emsp;&emsp;直接得从 `1` 开始循环至 `sqrt(c)` 逐个判断 `c` 减去其平方后的值是否依旧为完全平方数。

  ```python
    class Solution:
        def judgeSquareSum(self, c: int) -> bool:
            for i in range(int(c ** 0.5)+1):
                t = int((c-i*i) ** 0.5)
                if t*t + i*i == c:
                    return True
                if t < i:
                    break
            return False
  ```

  &emsp;&emsp;最终结果，*运行时间212ms*，超过70.38%；*占用内存13.3MB*，超过30.00%。

* **费马平方和定理**

  &emsp;&emsp;根据费马平方和定理可知，**自然数 `n` 可以表示为两个平方数之和等价于 `n` 的每个形如 `p=4m+3` 的素因子的次数为偶数**。

  ```python
    class Solution:
        def judgeSquareSum(self, c: int) -> bool:
            for i in range(2, int(c ** 0.5)+1):
                if c % i == 0:
                    count = 0
                    while c % i == 0:
                        count += 1
                        c /= i
                    if i % 4 == 3 and count % 2 == 1:
                        return False
            return c % 4 != 3
  ```

  &emsp;&emsp;最终结果，*运行时间68ms*，超过98.43%；*占用内存13.4MB*，超过25.59%。
