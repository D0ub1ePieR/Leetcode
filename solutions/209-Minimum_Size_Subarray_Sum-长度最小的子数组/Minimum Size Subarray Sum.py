# python3
# medium
# 数组 双指针 二分查找
# 56ms 86.32%
# 15.2MB 90.95%

class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        start = 0
        end = 0
        res = len(nums)
        if sum(nums) < s:
            return 0
        temp_sum = 0
        while end < len(nums):
            while temp_sum < s and end < len(nums):
                temp_sum += nums[end]
                end += 1
            while end - start > 1 and temp_sum - nums[start] >= s:
                temp_sum -= nums[start]
                start += 1
            res = min(res, end-start)
            temp_sum -= nums[start]
            start += 1
        return res

# 2812ms 5.02%
# 15.2MB 82.76%

class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        start = 0
        end = 0
        res = len(nums)
        if sum(nums) < s:
            return 0
        while end < len(nums):
            while sum(nums[start:end]) < s and end < len(nums):
                end += 1
            while end - start > 1 and sum(nums[start+1:end]) >= s:
                start += 1
            res = min(res, end-start)
            start += 1
        return res
