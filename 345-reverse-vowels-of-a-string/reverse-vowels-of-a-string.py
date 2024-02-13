class Solution:
    def reverseVowels(self, s: str) -> str:
        s_list = list(s)
        vowels = ['a', 'e', 'i', 'o', 'u']
        v_list = []
        count = 0
        for letter in s_list:
            if letter.lower() in vowels:
                s_list[count] = ''
                v_list.append(letter)
            count += 1
        
        count=0
        v_count=0
        v_list.reverse()
        for letter in s_list:
            if letter == '':
                s_list[count] = v_list[v_count]
                v_count += 1
            count += 1
        
        output_str = ''.join([str(letter) for letter in s_list])
        return output_str