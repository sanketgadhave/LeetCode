import itertools
import numpy as np

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [1] * n  # Product of elements to the left of nums[i]
        right = [1] * n  # Product of elements to the right of nums[i]
        output_list = [1] * n
        
        # Fill the left array
        for i in range(1, n):
            left[i] = nums[i - 1] * left[i - 1]
        
        # Fill the right array
        for i in range(n - 2, -1, -1):
            right[i] = nums[i + 1] * right[i + 1]
        
        # Construct the output array
        for i in range(n):
            output_list[i] = left[i] * right[i]
        
        return output_list