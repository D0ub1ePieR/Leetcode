class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        l=len(nums)
        end=l-1
        for i in range(l-2,-1,-1):
            if end-i<=nums[i]:
                end=i
        return end==0
