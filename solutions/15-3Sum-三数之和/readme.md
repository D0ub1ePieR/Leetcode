# 15、三数之和
> tag: python3 、 数组 、 双指针

***
### 题目描述

&emsp;&emsp;给定一个包含 `n` 个整数的数组 `nums`，判断 `nums` 中是否存在三个元素 `a`，`b`，`c` ，使得 `a + b + c = 0` ？找出所有满足条件且不重复的三元组。

**注意**：答案中不可以包含重复的三元组。

### 示例
```
  给定数组 nums = [-1, 0, 1, 2, -1, -4]，

  满足要求的三元组集合为：
  [
    [-1, 0, 1],
    [-1, -1, 2]
  ]
```
***
### 题目链接
[15、三数之和](https://leetcode-cn.com/problems/3sum/)
***
### 题解

* **双指针**

  &emsp;&emsp;[两数之和Ⅱ_输入有序数组](../167-Two_SumII_Input_array_is_sorted-两数之和Ⅱ_输入有序数组)中使用双指针来寻找和为目标 `target` 的两数，那么这里就很容易想到只要先对数组进行**排序**，随后在最外层进行对数组的遍历，再在剩余部分寻找和为其相反数的两个数即可。但是这样很容易便会超时。

  &emsp;&emsp;那么就需要进行一些改进，首先在双指针向中间靠拢时进行判断，如果下一个数和当前数相同，那么就再进行一次移动的操作，即**每一次移动时都会跳过所有相同的数字**。这样还是不能够过滤掉所有可能的相同的结果，最外层循环所取到的数字依旧可能重复。这里有两种选择，在加入结果时进行一次判断，但是依旧会导致超时。另一种便是在第一层循环时添加一条判断，同样得过滤掉所有相同的数，对于**一个相同的值只进行一次统计**。
  ```python
    class Solution:
        def threeSum(self, nums: List[int]) -> List[List[int]]:
            nums.sort()
            l = len(nums)
            res = []
            for i in range(l):
                # 排除外层循环相同的值
                if i == 0 or nums[i] != nums[i - 1]:
                    j = i + 1
                    k = l - 1
                    while j < k:
                        s = nums[i] + nums[j] + nums[k]
                        if s == 0:
                            res.append([nums[i], nums[j], nums[k]])
                            j += 1
                            k -= 1
                            # 排除双指针指向相同的值
                            while j < k and nums[j - 1] == nums[j]:
                                j += 1
                            while j < k and nums[k] == nums[k + 1]:
                                k -= 1
                        elif s < 0:
                            j += 1
                        else:
                            k -= 1
            return res
  ```
  > 缺少排除一些相同的值，会导致在倒数第三个(311)个测试用例时超时。

  &emsp;&emsp;最终结果，*运行时间1092ms*，超过48.38%；*占用内存16.6MB*，超过48.54%。结果还是不太令人满意。

* **分情况讨论，缩小寻找范围**

  &emsp;&emsp;为了使效率进一步提升，我们考虑到对于**重复的数字**
  + 重复出现**三次**，那么只有零符合条件

  + 重复出现**两次**，设这个数为 `n` ，那么只有当 `-2n` 也在数组中才符合条件

  + 接下来便可以统计出所有出现过的数字，假设他们只出现了**一次**进行讨论。同时题目要求相加需要和为0，所以必定存在一个正数和一个负数(*在不全为零的时候*)。则考虑只遍历负数部分，后面部分依旧使用双指针的思想，但是可以根据一定的规则缩小寻找的范围

    1. 查找的**左边界**一定比 `0 - n - nums[-1]` 大，那么就可以找到处于起始的指针的位置

    2. 查找的**右边界**一定比 `(0 - n) // 2` 小，那么就可以找到处于末尾的指针的位置

  ```python
    class Solution:
        def threeSum(self, nums: List[int]) -> List[List[int]]:
            res = []
            counts = collections.Counter(nums)
            sort_nums = sorted(counts)
            for i, num in enumerate(sort_nums):
                if counts[num] > 1:
                    if num == 0:
                        if counts[num] > 2:
                            res.append([0, 0, 0])
                    elif -2 * num in sort_nums:
                        res.append([num, num, -2 * num])
                if num < 0:
                    left = bisect.bisect_left(sort_nums, -num - sort_nums[-1], i + 1)
                    right = bisect.bisect_right(sort_nums, (-num) // 2, left)
                    for n in sort_nums[left:right]:
                        if -num - n in counts and -num-n != n:
                            res.append([num, n, -num-n])  
            return res
  ```

  > 统计每个出现的数字及其个数，可以使用collections模块中的Counter函数直接得到结果，也可以通过构建一个字典进行统计。在寻找左右边界时，可以使用bisect模块，通过确定想有序数组中插入某一个值的位置来确定边界。

  &emsp;&emsp;最终结果，*运行时间304ms*，超过99.51%；*占用内存17MB*，超过20.33%。
