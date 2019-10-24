class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res=[1]
        for i in nums:
            res.append(res[-1]*i)
        tmp=1
        for i in range(len(nums),0,-1):
            res[i]=res[i-1]*tmp
            tmp=tmp*nums[i-1]
        return res[1:]

t=Solution()
print(t.productExceptSelf([1,2,3,4]))
# 45.24
