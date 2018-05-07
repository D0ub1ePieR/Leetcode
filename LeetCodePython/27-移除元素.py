class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        res=0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[res]=nums[i]
                res+=1
        del(nums[res:])
        return len(nums)
