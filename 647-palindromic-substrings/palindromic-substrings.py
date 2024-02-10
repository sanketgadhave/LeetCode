class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        count = count + len(s)
        for i in range(1, len(s)):
            step = i
            for j in range(0, (len(s) - i)):
                sub_st = s[j:step+1]
                if sub_st == sub_st[::-1]:
                    count += 1 
                step += 1
        
        return count