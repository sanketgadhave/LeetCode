class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        right = len(nums) - 1
        op = 0
        while left < right:
            sum_po = nums[left]+nums[right]
            if sum_po == k:
                op += 1
                left+=1
                right-=1
            elif sum_po < k:
                left+=1
            else:
                right-=1
        
        return op
