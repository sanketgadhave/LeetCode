from math import gcd
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        min_len = min(len(str1), len(str2))
        for i in range(min_len, 0, -1):
            if len(str1) % i == 0 and len(str2) % i == 0:
                candidate = str1[:i]
                if candidate * (len(str1)//i) == str1 and candidate * (len(str2)//i) == str2:
                    return candidate
                
        return ''

