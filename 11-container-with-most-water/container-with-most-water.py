class Solution:
    def maxArea(self, height: List[int]) -> int:
        total_water = 0
        left_pt, right_pt = 0, len(height) - 1

        while left_pt < right_pt:
            min_ele = min(height[left_pt],height[right_pt])
            temp_water = min_ele * (right_pt-left_pt)
            total_water = max(temp_water, total_water)
            if height[left_pt] < height[right_pt]:
                left_pt += 1
            else:
                right_pt -= 1
        return total_water
        