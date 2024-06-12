class Solution:
    def sortColors(self, nums: List[int]) -> None:
        order = [0,1,2]
        a = 0
        for i in range(len(order)):
            for j in range(len(nums)):
                if order[i] == nums[j]:
                    nums[a], nums[j] = nums[j], nums[a]
                    a += 1

        