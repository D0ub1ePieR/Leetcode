# pyhon3
# medium
# 数组
# 432ms 83.74%
# 21.2MB 100.0%

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # import collections
        # t = collections.Counter(nums)
        # return [i for i in t.keys() if t[i]>1]
        res = []
        for i in nums:
            if nums[abs(i)-1] < 0:
                res.append(abs(i))
            else:
                nums[abs(i)-1] *= -1
        return res
