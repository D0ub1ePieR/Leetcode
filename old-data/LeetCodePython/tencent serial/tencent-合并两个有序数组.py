class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        for i in nums2:
            for j in range(m):
                if nums1[j]>i:
                    nums1.insert(j,i)
                    m+=1
                    break
            if j==m-1:
                nums1.insert(nums1.index(0),i)
                m+=1
        return nums1[:m]

t=Solution()
print(t.merge([1,2,3,0,0,0],3,[2,5,6],3))
# 50.25
