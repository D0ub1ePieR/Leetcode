## 1、两数之和
> tag: python3 、 数组 、 哈希表

***
### 题目描述
&emsp;&emsp;给定一个整数数组 `nums` 和一个目标值 `target`，请你在该数组中找出和为目标值的那 **两个** 整数，并返回他们的数组下标。  
&emsp;&emsp;你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
### 示例
```
给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
```
***
### 题目链接
[1.两数之和](#https://leetcode-cn.com/problems/two-sum/)
***
### 题解

* **暴力求解**

  首先想到的便是使用两层循环，判断两层循环中的值相加是否为target的值。但是此方法的时间复杂度就会达到 $O(n^2)$

* **哈希表**

  这种方法只需要 $O(n)$ 的空间和时间复杂度。建立一个哈希表，每一次循环当前对应的 $nums[i]$ 的值是否在表中
  + 如果在，则返回 $i$ 及 哈希表对应的值。
  + 如果不在，则向哈希表中添加键为 $target-nums[i]$ ，值为 $i$ 的键值对

  ```python
  class Solution:
      def twoSum(self, nums: List[int], target: int) -> List[int]:
          l = len(nums)
          d = {}
          for i in range(l):
              try:
                  index = d[str(nums[i])]
              except:
                  d[str(target - nums[i])] = i
              else:
                  return [index, i]
  ```

    &emsp;最终*运行时间60ms*，超过73.87%。*占用内存15MB*，超过18.46%。  

    &emsp;一开始突然想不起来如何快速得判断某个值是否在字典的所有键中，便使用了`try catch`来判断，可能导致速度降低一些并且占用更多的内存。**实际上**，只需要使用 if 语句即可。
    ```python
      if str(nums[i]) in d:
        return [d[str(nums[i])], i]
      else:
        d[str(target - nums[i])] = i
    ```
    &emsp;同时多了一步字符串的转换也会导致速度降低空间占用过多。也可以将字符串的转换省去。
