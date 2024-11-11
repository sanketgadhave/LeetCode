class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        min1 = float('inf')
        middle = float('inf')
        for i in range(len(nums)):
            if nums[i] <= min1:
                min1 = nums[i]
            elif nums[i] <= middle:
                middle = nums[i]
            else:
                return True
        
        return False