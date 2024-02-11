class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        output_str = ''
        for i in range(1, len(str1)+1):
            sub_st = str1[0:i]
            if len(sub_st)*str1.count(sub_st) == len(str1): 
                if sub_st in str2:
                    if len(sub_st)*str2.count(sub_st) == len(str2):
                        if len(sub_st) > len(output_str):
                            output_str = sub_st
                
        return output_str