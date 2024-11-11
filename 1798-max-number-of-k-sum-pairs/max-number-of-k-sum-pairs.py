class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        right = len(nums) - 1
        operations = 0
        while left<right:
            sum1 = nums[left]+nums[right]
            if sum1 == k:
                operations += 1
                left += 1
                right -= 1
            elif sum1 < k:
                left += 1
            else:
                right -= 1

        return operations
