class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        i=0
        while i<len(nums)-1:
            if nums[i]!=nums[i+1]:
                return nums[i]
            else:
                i+=2
        return nums[-1]

t=Solution()
print(t.singleNumber([4,1,2,1,2]))
print(t.singleNumber([2,2,1]))
print(t.singleNumber([17,12,5,-6,12,4,17,-5,2,-3,2,4,5,16,-3,-4,15,15,-4,-5,-6]))
# 41.07
# 求和
# 异或
