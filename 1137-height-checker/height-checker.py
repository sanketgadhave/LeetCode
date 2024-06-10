class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        orignal_height = heights.copy()
        heights.sort()
        count = 0
        for i in range(0,len(heights)):
            if orignal_height[i] != heights[i]:
                count += 1
            
        return count