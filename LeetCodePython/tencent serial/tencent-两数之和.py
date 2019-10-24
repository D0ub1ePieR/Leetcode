class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic={}
        for index,num in enumerate(nums):
            if target-num in dic:
                return [index,dic[target-num]]
            dic[num]=index

t=Solution()
print(t.twoSum([2,7,11,15],9))
# 98.35
