class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        str_len = max(len(word1),len(word2))
        output_str = ''
        for i in range(0,str_len):
            if (i <= len(word1) - 1):
                output_str =  output_str + word1[i]
            if (i <= len(word2) - 1):
                output_str = output_str + word2[i]
            
        return output_str