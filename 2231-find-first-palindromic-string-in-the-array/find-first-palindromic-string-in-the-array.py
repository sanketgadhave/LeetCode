class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        pal_str = ''
        for word in words:
            if word == word[::-1]:
                pal_str = word
                break
        
        return pal_str