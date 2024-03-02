class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        output_list = [num*num for num in nums]
        output_list.sort()
        return output_list