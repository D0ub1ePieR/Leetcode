class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur=0
        maxnum=nums[0]
        for i in nums:
            cur+=i
            maxnum=max(cur,maxnum);
            if cur<0:
                cur=0
        return maxnum
# 93.56
