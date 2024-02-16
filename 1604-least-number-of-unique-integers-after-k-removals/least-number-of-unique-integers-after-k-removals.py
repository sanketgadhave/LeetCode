class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        num_dict = {}
        for num in arr:
            if num in num_dict.keys():
                num_dict[num] += 1
            else:
                num_dict[num] = 1
        
        values_list = list(num_dict.values())
        values_list.sort()
        dummy_list = values_list.copy()
        for ele in values_list:
            if k >= ele:
                k = k - ele
                dummy_list.remove(ele)
        
        return len(dummy_list)