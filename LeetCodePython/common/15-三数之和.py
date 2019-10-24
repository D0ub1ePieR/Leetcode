class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        nums.sort()
        for i in range(len(nums)):
            if i==0 or nums[i-1]!=nums[i]:
                j=i+1
                k=len(nums)-1
                while j<k:
                    s=nums[i]+nums[j]+nums[k]
                    if s==0:
                        res.append([nums[i],nums[j],nums[k]])
                        j+=1
                        k-=1
                        while j<k and nums[j]==nums[j-1]:
                            j+=1
                        while j<k and nums[k+1]==nums[k]:
                            k-=1
                    elif s>0:
                        k-=1
                    else:
                        j+=1
        return res
            
# 73.99
