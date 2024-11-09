class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        max_len = max(len(word1), len(word2))
        output = ''
        for i in range(0, max_len):
            if i < len(word1):
                output+=word1[i]
            if i < len(word2):
                output+=word2[i]
        
        return output
            
