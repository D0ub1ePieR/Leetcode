from math import floor
class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #dic={}
        #flag=floor(len(nums)/2)
        #for i in nums:
        #    if i in dic:
        #        dic[i]+=1
        #        if dic[i]>=flag:
        #            return i
        #    else:
        #        dic[i]=0
        #        if dic[i]>=flag:
        #            return i
        nums.sort()
        return nums[len(nums)//2]
# 90.49
