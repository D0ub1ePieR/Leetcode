class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num=0
        if nums==[]:
            return 0
        last=nums[0]
        for i in nums:
            if num==0:
                nums[num]=i
                num+=1
            if i==last:
                continue
            else:
                nums[num]=i
                num+=1
                last=i
        return num
# 96.79
