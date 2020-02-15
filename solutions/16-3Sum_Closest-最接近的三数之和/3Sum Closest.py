# python3
# medium
# 数组 双指针
# 88ms 95.13%
# 13MB 47.01%

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = nums[0] + nums[1] + nums[2]
        for i in range(len(nums)-2):
            j = i + 1
            k = len(nums) - 1

            min_sum = nums[i] + nums[j] + nums[j+1]
            max_sum = nums[i] + nums[k-1] + nums[k]
            if min_sum > target:
                if abs(min_sum - target) < abs(res - target):
                    res = min_sum
                    break
            if max_sum < target:
                if abs(max_sum - target) < abs(res - target):
                    res = max_sum
                    continue

            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s == target:
                    return s
                elif abs(s - target) < abs(res - target):
                    res = s
                elif s > target:
                    k -= 1
                    while j < k and nums[k + 1] == nums[k]:
                        k -= 1
                else:
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
        return res

# 144ms 51.14%
# 13.1MB 48.75%

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = nums[0] + nums[1] + nums[2]
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s == target:
                    return s
                elif abs(s - target) < abs(res - target):
                    res = s
                    if s > target:
                        k -= 1
                        while j < k and nums[k + 1] == nums[k]:
                            k -= 1
                    else:
                        j += 1
                        while j < k and nums[j] == nums[j - 1]:
                            j += 1
                elif s > target:
                    k -= 1
                    while j < k and nums[k + 1] == nums[k]:
                        k -= 1
                else:
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
        return res
