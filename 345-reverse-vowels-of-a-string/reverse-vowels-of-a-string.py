class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel_list = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        start = 0
        end = len(s)-1
        s_list = list(s)
        while start<end:
            if s_list[start] in vowel_list or s_list[end] in vowel_list:
                if s_list[start] in vowel_list and s_list[end] in vowel_list:
                    s_list[start], s_list[end] = s_list[end], s_list[start]
                    start += 1
                    end -=1
                elif s_list[start] in vowel_list:
                    end -=1
                elif s_list[end] in vowel_list:
                    start +=1
            else:
                start +=1
                end -=1
        
        output = ''.join(char for char in s_list)
        return output

                