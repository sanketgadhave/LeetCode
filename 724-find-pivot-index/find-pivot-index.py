class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = 0
        prefix_list = [0] * (len(nums)+1)
        for i in range(len(nums)):
            prefix = prefix + nums[i]
            prefix_list[i+1] = prefix
        
        postfix_list = [0] *(len(nums)+1)
        postfix = 0
        for i in range(len(nums)-1, -1, -1):
            postfix = postfix + nums[i]
            postfix_list[i] = postfix

        for i in range(len(nums)):
            if prefix_list[i] == postfix_list[i+1]:
                return i
        return -1