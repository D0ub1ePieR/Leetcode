# python3
# simple
# 数组 双指针
# 44ms 43.32%
# 13.7MB 5.36%

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        from bisect import insort
        for i in range(len(nums1)-m):
            del nums1[m]
        for i in nums2:
            insort(nums1, i)
