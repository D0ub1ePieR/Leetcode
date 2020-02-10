class Solution:
    def maxArea(self, height: List[int]) -> int:
        front = 0
        end = len(height) - 1
        s = 0
        while front < end:
            s = max(s, min(height[front], height[end])*(end-front))
            if height[front] < height[end]:
                front += 1
            else:
                end -= 1
        return s
