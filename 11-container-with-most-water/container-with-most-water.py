class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0 
        right = len(height) - 1
        cur_max = 0
        while left < right:
            minimum_height = min(height[left], height[right])
            max_water = minimum_height * (right-left)
            cur_max = max(cur_max, max_water)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return cur_max
