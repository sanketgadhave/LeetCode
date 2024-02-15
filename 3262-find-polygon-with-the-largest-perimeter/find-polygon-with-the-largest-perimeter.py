class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        perimeter = -1
        dummy_list = nums.copy()
        for i in range(len(nums) - 1, 1, -1):
            if sum(dummy_list) - nums[i] > nums[i]:
                perimeter = sum(dummy_list)
                break
            dummy_list.pop()

        return perimeter
            
