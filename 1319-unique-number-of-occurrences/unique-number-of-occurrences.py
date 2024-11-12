class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        sample_dict = {}
        for i in range(len(arr)):
            if arr[i] in sample_dict:
                sample_dict[arr[i]] += 1
            else:
                sample_dict[arr[i]] = 1
        
        value_list = sample_dict.values()
        if len(value_list) == len(set(value_list)):
            return True
        else:
            return False