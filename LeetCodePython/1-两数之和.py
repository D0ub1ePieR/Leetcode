class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in nums:
            j=target-i
            if j in nums[nums.index(i)+1:]:
                return [nums.index(i),nums[nums.index(i)+1:].index(j)+nums.index(i)+1]
s=Solution()
nums=[3,2,2,5,3]
target=6
print(s.twoSum(nums,target))
