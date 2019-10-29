class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = 0
        flag = 0
        l = len(nums)
        for i in range(l):
            if i == 0 or nums[i-1]!=nums[i]:
                j = i + 1
                k = l - 1
                while j < k:
                    s = nums[i] + nums[j] + nums[k]
                    if flag == 0:
                        res = s
                        flag = 1
                    if s == target:
                        return target
                    elif s > target:
                        if abs(s-target) < abs(res-target):
                            res = s
                        k -= 1
                    else:
                        if abs(s-target) < abs(res-target):
                            res = s
                        j += 1
        return res

# 94.12%
# 5.04%
