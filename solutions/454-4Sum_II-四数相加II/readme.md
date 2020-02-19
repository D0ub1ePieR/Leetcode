# 454、四数相加 II
> tag: python3 、 哈希表 、 二分查找

***
### 题目描述

&emsp;&emsp;给定四个包含整数的数组列表 A , B , C , D ,计算有多少个元组 `(i, j, k, l)` ，使得 `A[i] + B[j] + C[k] + D[l] = 0`。

&emsp;&emsp;为了使问题简单化，所有的 A, B, C, D 具有相同的长度 `N`，且 `0 ≤ N ≤ 500` 。所有整数的范围在 `-2^28` 到 `2^28 - 1` 之间，最终结果不会超过 `2^31 - 1` 。

### 例如
```
  输入:
  A = [ 1, 2]
  B = [-2,-1]
  C = [-1, 2]
  D = [ 0, 2]

  输出:
  2

  解释:
  两个元组如下:
  1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
  2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0
```

***
### 题目链接
[454.四数之和II](https://leetcode-cn.com/problems/4sum-ii/)
***
### 题解
> 各方法完整代码可见 py 文件

* **基于暴力求解的优化**

  &emsp;&emsp;第一时间就联想到是否又可以使用多指针来进行求解，但是进行到一半发现由于数据是四个独立的数组，没有办法固定住保持恒定大小相关的指针，于是干脆就在暴力循环的基础上进行一定的优化看能不能通过。

  + 可以通过 `-(A[i] + B[j] + C[k]) in D` 来忽略掉最后一层循环。

  + 通过记录当前循环下的下层循环的总可能数，当下一个数与上一个数相同时可以跳过下一轮循环，直接在结果上添加记录值

  + 与类似题相同的，通过判断当前轮可能达到的最大值和最小值与 `0` 相比较，跳出或跳过当前循环

  + 通过 `bisect` 库，判断每层循环可以缩小的左右边界，减少每层循环量

  > 最终还是在倒数第三组 (46) 个样例时超时了，暂时还没有相处再如何优化可以使其勉强过线

  ```python
  A.sort()
  B.sort()
  C.sort()
  D.sort()
  res = 0
  tmp_a = tmp_b = tmp_c = 0
  end_a = bisect.bisect_right(A, (-B[0]-C[0]-D[0])//2)
  start_b = bisect.bisect_left(A, (-B[-1]-C[-1]-D[-1])//2)
  for i in range(len(A)):
      if i > 0 and A[i] == A[i-1]:
          res += tmp_a
          continue
      else:
          tmp_a = 0
      if A[i] + B[0] + C[0] + D[0] > 0:
          break
      if A[i] + B[-1] + C[-1] + D[-1] < 0:
          continue
      # 限制循环边界
      end_b = bisect.bisect_right(B, (-A[i]-C[0]-D[0])//2)
      start_b = bisect.bisect_left(B, (-A[i]-C[-1]-D[-1])//2)
      for j in range(start_b, min(len(B), end_b)):
          # 记录相同值达到条件的可能个数，跳过相同值的循环
          if j > 0 and B[j] == B[j-1]:
              res += tmp_b
              tmp_a += tmp_b
              continue
          else:
              tmp_b = 0
          # 判断当前循环可能达到的最大值和最小值
          if A[i] + B[j] + C[0] + D[0] > 0:
              break
          if A[i] + B[j] + C[-1] + D[-1] < 0:
              continue
          end_c = bisect.bisect_right(C, (-A[i]-B[j]-D[0])//2)
          start_c = bisect.bisect_left(C, (-A[i]-B[j]-D[-1])//2)
          for k in range(start_c, min(len(C), end_c)):
              if k > 0 and C[k] == C[k-1]:
                  res += tmp_c
                  tmp_b += tmp_c
                  tmp_a += tmp_c
                  continue
              else:
                  tmp_c = 0
              if A[i] + B[j] + C[k] + D[0] > 0:
                  break
              if A[i] + B[j] + C[k] + D[-1] < 0:
                  continue
              if -(A[i] + B[j] + C[k]) in D:
                  s = D.count(-(A[i] + B[j] + C[k]))
                  res += s
                  tmp_a += s
                  tmp_b += s
                  tmp_c += s     
  return res
  ```

* **两个哈希表的配对**

  &emsp;&emsp;上面的方法其实是将四个数组独立的对待，而双指针其实也是将两个数建立关联减少自由的量。那么我们也可以将这四组数分为两组，很显然就是 `group1` 的值和 `group2` 的值和要为 `0`。那么我们又要如何统计每一组的和的可能性呢？

  &emsp;&emsp;最简单的方法便是各自对 `A, B` 和 `C, D` 建立一个字典，存储 **和 - 达到这个和的可能的个数** 的键值对，时间复杂度只有 `O(n^2)`。最后只要在这两个字典中寻找互为相反数的键，在最终结果中加上两者值的乘积(*相当于target=0的两数之和*)

  ```python
  class Solution:
      def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
          l = len(A)
          dict1 = {}
          dict2 = {}
          for i in range(l):
              for j in range(l):
                  sum1 = A[i] + B[j]
                  sum2 = C[i] + D[j]
                  dict1[sum1] = dict1.get(sum1, 0) + 1
                  dict2[sum2] = dict2.get(sum2, 0) + 1
          res = 0
          for num in dict1:
              res += dict1[num] * dict2.get(-num, 0)
          return res
  ```
  &emsp;&emsp;最终结果，*运行时间704ms*，超过5.12%；*占用内存65.6MB*，超过5.28%。

* **两个哈希表的配对优化**

  &emsp;&emsp;可见上面的方法虽然通过了，但是结果依旧不尽如人意。于是我们考虑到，在建立两个哈希表的时候，可能存在很多情况是重复的值，我们没有进行处理。于是我们可以首先对 `A, B, C ,D` 进行预处理，统计各自 **出现的值以及出现的个数**，随后在建立哈希表。这里依旧使用了 `collections` 模块。

  ```python
    a = collections.Counter(A)
    b = collections.Counter(B)
    c = collections.Counter(C)
    d = collections.Counter(D)
  ```

  随后通过其出现值个数乘积建立哈希表

  ```python
    for i in a:
        for j in b:
            dict1[i+j] = dict1.get(i+j, 0) + a[i]*b[j]
  ```

  最后的查找最终结果方式保持不变

  最终结果，*运行时间432ms*，超过24.34%；*占用内存75.3MB*，超过5.28%

* **单哈希表**

  &emsp;&emsp;可见经过了优化有了一些提升，但是还不够明显。那么能不能从内存占用的角度再次对代码进行优化呢。于是想到，我们可以不建立第二个哈希表，在原来第二个哈希表建立的过程中直接进行判断，不仅可以省去最后一个整个循环的步骤，又可以减少一个字典的空间占用。即将第二个循环改成

  ```python
    for i in c:
        for j in d:
            if -i-j in dict1:
                res += c[i] * d[j] * dict1[-i-j]
  ```
  > 这里发现直接使用 if 语句进行判断比使用 dict1.get(-i-j, 0)的不存在返回0 的效率高很多

  &emsp;&emsp;最终结果，*运行时间284ms*，超过83.26%；*占用内存50MB*，超过19.72%。达到了可以接受的结果。
