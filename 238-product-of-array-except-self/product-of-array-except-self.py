import numpy
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 0:
            return []
        
        # Initialize the arrays
        left = [1] * n
        right = [1] * n
        result = [1] * n
        
        # Fill the left array
        for i in range(1, n):
            left[i] = left[i - 1] * nums[i - 1]
        
        # Fill the right array
        for i in range(n - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]
        
        # Calculate the result
        for i in range(n):
            result[i] = left[i] * right[i]
        
        return result