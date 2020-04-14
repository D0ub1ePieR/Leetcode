# python3
# simple
# 数组
# 408ms 86.94%
# 23.1MB 8.33%

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # import collections
        # return [i for i in range(1, len(nums)+1) if collections.Counter(nums)[i]==0]
        # return [i for i in range(1, len(nums)+1) if i not in nums]
        t = set(nums)
        return [i for i in range(1, len(nums)+1) if i not in t]
