class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        count_list = []
        count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count_list.append(count)
                count = 0
            else:
                count+=1
        
        if count != 0:
            count_list.append(count)
        if len(count_list) == 1:
            return len(nums)-1
        else:
            sum1 = 0
            for i in range(len(count_list)-1):
                sum1 = max(sum1, count_list[i]+count_list[i+1])

            return sum1 

                
                
