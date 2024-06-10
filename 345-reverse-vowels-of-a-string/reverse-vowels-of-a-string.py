class Solution:
    def reverseVowels(self, s: str) -> str:
        char_list = list(s)
        start = 0
        end = len(char_list) - 1
        vowel_list = ['a','e','i','o','u','A','E','I','O','U']
        while start < end:
            if char_list[start] in vowel_list:
                if char_list[end] in vowel_list:
                    temp = char_list[start]
                    char_list[start] = char_list[end]
                    char_list[end] = temp
                    start += 1
                    end -= 1
                    continue
                else:
                    end -= 1
                    continue

            start += 1
        return ''.join(char_list)