# python3
# simple
# 哈希表 数组
# 60ms 73.87%
# 15MB 18.46%

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
