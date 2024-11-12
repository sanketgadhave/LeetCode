class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        output_num1 = []
        output_num2 = []
        final_output = []
        for i in range(len(nums1)):
            if nums1[i] not in nums2:
                output_num1.append(nums1[i])

        final_output.append(list(set(output_num1)))  
        for i in range(len(nums2)):
            if nums2[i] not in nums1:
                output_num2.append(nums2[i])
        
        final_output.append(list(set(output_num2)))
        return final_output 