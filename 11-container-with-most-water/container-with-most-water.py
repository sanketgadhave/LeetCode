class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_level = 0
        min1 = 0
        max1 = len(height)-1
        while min1 < max1:
            current_level = min(height[min1], height[max1]) * (max1-min1)
            max_level = max(max_level, current_level)

            if height[min1] < height[max1]:
                min1+=1
            else:
                max1-=1
        return max_level
            
