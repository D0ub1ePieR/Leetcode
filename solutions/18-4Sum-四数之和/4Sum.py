# python3
# medium
# 数组 双指针 哈希表
# 104ms 87.45%
# 13.2MB 42.64%

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        l = len(nums)
        res = set()
        for i in range(l - 3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            mid = target - nums[i]
            big_value = nums[i] + nums[l-1] + nums[l-2] + nums[l-3]
            small_value = nums[i] + nums[i+1] + nums[i+2] + nums[i+3]
            if big_value < target:
                continue
            if small_value > target:
                break
            for j in range(i + 1, l - 2):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                k = j + 1
                n = l - 1
                big_value = nums[j] + nums[n] + nums[n - 1]
                small_value = nums[j] + nums[j + 1] + nums[j + 2]
                if big_value < mid:
                    continue
                if small_value > mid:
                    break
                while k < n:
                    s = nums[j] + nums[k] + nums[n]
                    if s == mid:
                        res.add((nums[i], nums[j], nums[k], nums[n]))
                        n -= 1
                        while k < n and nums[n + 1] == nums[n]:
                            n -= 1
                        k += 1
                        while k < n and nums[k - 1] == nums[k]:
                            k += 1
                    elif s > mid:
                        n -= 1
                        while k < n and nums[n + 1] == nums[n]:
                            n -= 1
                    else:
                        k += 1
                        while k < n and nums[k - 1] == nums[k]:
                            k += 1
        return res
