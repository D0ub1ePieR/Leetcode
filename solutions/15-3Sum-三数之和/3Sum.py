# python3
# medium
# 数组 双指针
# 304ms 99.15%
# 17MB 20.33%

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

# 1092ms 48.38%
# 16.6MB 48.54%

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        l = len(nums)
        res = []
        for i in range(l):
            if i == 0 or nums[i] != nums[i - 1]:
                j = i + 1
                k = l - 1
                while j < k:
                    s = nums[i] + nums[j] + nums[k]
                    if s == 0:
                        res.append([nums[i], nums[j], nums[k]])
                        j += 1
                        k -= 1
                        while j < k and nums[j - 1] == nums[j]:
                            j += 1
                        while j < k and nums[k] == nums[k + 1]:
                            k -= 1
                    elif s < 0:
                        j += 1
                    else:
                        k -= 1
        return res
