class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos_list = []
        neg_list = []
        final_list = []
        for num in nums:
            if num < 0:
                neg_list.append(num)
            else:
                pos_list.append(num)

        for i in range(0, len(pos_list)):
            final_list.append(pos_list[i])
            final_list.append(neg_list[i])
        
        return final_list