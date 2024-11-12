class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left = 0
        for i in range(len(nums)):
            if left == total_sum - left - nums[i]:
                return i
            else:
                left += nums[i]
        
        return -1