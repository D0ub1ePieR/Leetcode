# 167、两数之和II-输入有序数组
> tag: python3 、 数组 、 双指针 、 二分查找

***
### 题目描述
&emsp;&emsp;给定一个已按照 **升序排列** 的有序数组，找到两个数使得它们相加之和等于目标数。  

&emsp;&emsp;函数应该返回这两个下标值 `index1` 和 `index2`，其中 `index1` 必须小于 `index2`。
### 说明
&emsp;&emsp;返回的下标值`(index1 和 index2)`不是从零开始的。  

&emsp;&emsp;你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。
### 示例
```
  输入: numbers = [2, 7, 11, 15], target = 9
  输出: [1,2]
  解释: 2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。
```

***
### 题目链接
[167. 两数之和 II - 输入有序数组](https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted/)
***
### 题解

* 类似[两数之和](../1-Two_Sum-两数之和)，再其基础上添加了数组已经为升序的条件，依旧可以使用*哈希表*的方法，但是这相当于没有用到新增加的条件

* **暴力方法**

* **双指针**

  由于数组已经按照升序排列，所以我们可以将两个指针分别放在数组的两端。每一次比较两个指针(`start和end`)所对应的值的和与` target` 之间的大小。
  + 如果和比 `target` 小，则说明有一个值需要增大，而靠末端的 `end` 指针由于是从数组末尾向起始移动的，不能让它退回去，则要将 `start` 指针加一
  + 如果和比 `target` 大，则说明需要将 `end` 指针减一，以缩小两数之和

  ```python
  class Solution:
      def twoSum(self, numbers: List[int], target: int) -> List[int]:
          start, end = 0, len(numbers) - 1
          while numbers[start] + numbers[end] != target:
              if numbers[start] + numbers[end] > target:
                  end -= 1
              else:
                  start += 1
          return [start + 1, end + 1]
  ```

  &emsp;&emsp;最终结果，*运行时间72ms*，超过73.28%；*占用内存13.5MB*，超过45.12%。
  > 注意一点，题目中说明了下标不是从0开始，则在返回的时候需要将两个指针的数值加一返回
