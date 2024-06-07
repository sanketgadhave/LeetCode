class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        final_str = ''
        for i in range(0, len(word1)):
            final_str = final_str+word1[i]
            if i == len(word2):
                final_str = final_str+word1[i+1:]
                break
            final_str = final_str+word2[i]

        if i < len(word2):
            final_str = final_str+word2[i+1:]
        return final_str
            
